#!/usr/bin/env python3
"""Gate 1 structural review.

Checks whether canonical assets are complete enough to proceed to image generation.
This is not visual fidelity review yet. It prevents incomplete Model/Scene/Product
records from entering later expensive generation steps.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def gate(root: Path, model_id: str, scene_id: str, brand_id: str, sku: str) -> dict:
    model_path = root / "models" / model_id / "profile.yaml"
    scene_path = root / "scenes" / scene_id / "scene.yaml"
    product_path = root / "brands" / brand_id / "skus" / sku / "product.yaml"

    model = load_yaml(model_path)
    scene = load_yaml(scene_path)
    product = load_yaml(product_path)

    checks = {
        "model_exists": bool(model),
        "model_human_approved": model.get("review", {}).get("human_approved") is True,
        "model_has_base_images": bool(model.get("assets", {}).get("approved_base_images")),
        "scene_exists": bool(scene),
        "scene_human_approved": scene.get("review", {}).get("human_approved") is True,
        "product_exists": bool(product),
        "product_has_source_url": bool(product.get("source", {}).get("landing_page_url")),
        "product_has_images": bool(product.get("images")),
        "product_human_verified": product.get("review", {}).get("human_verified") is True,
    }

    blockers = [name for name, passed in checks.items() if not passed]
    decision = "PASS" if not blockers else "CHECK"

    return {
        "decision": decision,
        "checks": checks,
        "blockers": blockers,
        "note": "Gate 1 only checks asset readiness. Visual product/model fidelity is reviewed after generation.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Check whether assets are ready for generation.")
    parser.add_argument("--model", required=True)
    parser.add_argument("--scene", required=True)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--sku", required=True)
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()

    result = gate(Path(args.root), args.model, args.scene, args.brand, args.sku)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result["decision"] == "PASS" else 2)


if __name__ == "__main__":
    main()
