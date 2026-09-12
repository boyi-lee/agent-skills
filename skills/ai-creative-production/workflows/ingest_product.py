#!/usr/bin/env python3
"""Gate 1: ingest one product Landing Page into the canonical Brand/SKU asset structure.

Scope is intentionally small:
- fetch page HTML
- collect likely product image URLs
- derive basic product metadata when available
- create brand/SKU folders
- save immutable source evidence + manifest

This script does NOT generate images and does NOT guess missing product details.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup

USER_AGENT = "ai-creative-production/0.1 (+product-asset-ingestion)"
IMAGE_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp", ".avif")


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "unknown"


def get_meta(soup: BeautifulSoup, *keys: str) -> str | None:
    for key in keys:
        tag = soup.find("meta", attrs={"property": key}) or soup.find("meta", attrs={"name": key})
        if tag and tag.get("content"):
            return tag["content"].strip()
    return None


def extract_jsonld(soup: BeautifulSoup) -> list[dict]:
    items: list[dict] = []
    for script in soup.find_all("script", attrs={"type": "application/ld+json"}):
        raw = script.string or script.get_text(strip=True)
        if not raw:
            continue
        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError:
            continue
        candidates = parsed if isinstance(parsed, list) else [parsed]
        for item in candidates:
            if isinstance(item, dict) and "@graph" in item and isinstance(item["@graph"], list):
                candidates.extend(x for x in item["@graph"] if isinstance(x, dict))
            if isinstance(item, dict):
                items.append(item)
    return items


def find_product_jsonld(items: list[dict]) -> dict:
    for item in items:
        item_type = item.get("@type")
        types = item_type if isinstance(item_type, list) else [item_type]
        if "Product" in types:
            return item
    return {}


def collect_image_urls(soup: BeautifulSoup, page_url: str, product_jsonld: dict) -> list[str]:
    urls: list[str] = []

    structured = product_jsonld.get("image")
    if isinstance(structured, str):
        urls.append(structured)
    elif isinstance(structured, list):
        urls.extend(x for x in structured if isinstance(x, str))

    for key in ("og:image", "twitter:image"):
        value = get_meta(soup, key)
        if value:
            urls.append(value)

    for img in soup.find_all("img"):
        for attr in ("src", "data-src", "data-original"):
            value = img.get(attr)
            if value:
                urls.append(value)
        srcset = img.get("srcset") or img.get("data-srcset")
        if srcset:
            for candidate in srcset.split(","):
                part = candidate.strip().split(" ")[0]
                if part:
                    urls.append(part)

    normalized: list[str] = []
    seen: set[str] = set()
    for raw in urls:
        url = urljoin(page_url, raw.strip())
        clean = url.split("#", 1)[0]
        lower_path = urlparse(clean).path.lower()
        if not any(ext in lower_path for ext in IMAGE_EXTENSIONS):
            continue
        if clean not in seen:
            seen.add(clean)
            normalized.append(clean)
    return normalized


def download_image(session: requests.Session, url: str, dest_dir: Path, index: int) -> dict | None:
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
    except requests.RequestException:
        return None

    content_type = (response.headers.get("content-type") or "").lower()
    if not content_type.startswith("image/"):
        return None

    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix not in IMAGE_EXTENSIONS:
        suffix = ".jpg"

    data = response.content
    sha256 = hashlib.sha256(data).hexdigest()
    filename = f"image-{index:03d}{suffix}"
    path = dest_dir / filename
    path.write_bytes(data)
    return {
        "source_url": url,
        "local_path": f"raw/{filename}",
        "role": "unknown",
        "checksum": sha256,
    }


def infer_brand(url: str, soup: BeautifulSoup, product_jsonld: dict, explicit: str | None) -> str:
    if explicit:
        return slugify(explicit)
    brand = product_jsonld.get("brand")
    if isinstance(brand, dict):
        brand = brand.get("name")
    if isinstance(brand, str) and brand.strip():
        return slugify(brand)
    site_name = get_meta(soup, "og:site_name")
    if site_name:
        return slugify(site_name)
    host = urlparse(url).netloc.replace("www.", "")
    return slugify(host.split(".")[0])


def infer_sku(product_jsonld: dict, explicit: str | None) -> str:
    if explicit:
        return explicit.strip()
    for key in ("sku", "mpn", "productID"):
        value = product_jsonld.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    return "unknown-sku"


def ingest(url: str, root: Path, brand: str | None, sku: str | None) -> Path:
    session = requests.Session()
    session.headers.update({"User-Agent": USER_AGENT})
    response = session.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    product_jsonld = find_product_jsonld(extract_jsonld(soup))

    brand_id = infer_brand(url, soup, product_jsonld, brand)
    sku_id = infer_sku(product_jsonld, sku)
    sku_folder = slugify(sku_id)

    asset_dir = root / "brands" / brand_id / "skus" / sku_folder
    raw_dir = asset_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    (raw_dir / "landing-page.html").write_text(response.text, encoding="utf-8")
    (raw_dir / "source-url.txt").write_text(url + "\n", encoding="utf-8")

    image_urls = collect_image_urls(soup, url, product_jsonld)
    images: list[dict] = []
    for index, image_url in enumerate(image_urls, start=1):
        downloaded = download_image(session, image_url, raw_dir, index)
        if downloaded:
            images.append(downloaded)

    name = product_jsonld.get("name") or get_meta(soup, "og:title")
    description = product_jsonld.get("description") or get_meta(soup, "og:description", "description")
    color = product_jsonld.get("color") if isinstance(product_jsonld.get("color"), str) else None
    category = product_jsonld.get("category") if isinstance(product_jsonld.get("category"), str) else None

    manifest = {
        "brand_id": brand_id,
        "sku": sku_id,
        "status": "draft",
        "version": "0.1.0",
        "source": {
            "landing_page_url": url,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        },
        "product": {
            "name": name,
            "color": color,
            "category": category,
            "description": description,
        },
        "images": images,
        "immutable_features": [
            "logo",
            "color",
            "silhouette",
            "collar",
            "sleeve_or_leg_shape",
            "graphic_or_panel_details",
        ],
        "review": {
            "source_complete": bool(images),
            "human_verified": False,
            "notes": "Image roles remain unknown until reviewed/classified.",
        },
    }
    (asset_dir / "product.yaml").write_text(
        yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )

    evidence = {
        "page_status_code": response.status_code,
        "image_url_count_discovered": len(image_urls),
        "image_count_downloaded": len(images),
        "jsonld_product_found": bool(product_jsonld),
    }
    (asset_dir / "ingestion-report.json").write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return asset_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Ingest one product landing page into Brand/SKU assets.")
    parser.add_argument("url")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--brand")
    parser.add_argument("--sku")
    args = parser.parse_args()

    output = ingest(args.url, Path(args.root), args.brand, args.sku)
    print(output)


if __name__ == "__main__":
    main()
