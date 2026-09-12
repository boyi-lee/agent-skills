#!/usr/bin/env python3
"""Create a traceable generation job from canonical assets.

This does not generate imagery yet. It validates that Model, Scene and Product
assets exist, then creates a job record that later generation/review steps can use.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

import yaml


def load_yaml(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(f"Missing required asset: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Invalid YAML object: {path}")
    return data


def create_job(root: Path, model_id: str, scene_id: str, brand_id: str, sku: str, ratio: str) -> Path:
    model_path = root / "models" / model_id / "profile.yaml"
    scene_path = root / "scenes" / scene_id / "scene.yaml"
    product_path = root / "brands" / brand_id / "skus" / sku / "product.yaml"

    model = load_yaml(model_path)
    scene = load_yaml(scene_path)
    product = load_yaml(product_path)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    job_id = f"{timestamp}-{brand_id}-{sku}-{model_id}-{scene_id}"
    job_dir = root / "jobs" / job_id
    job_dir.mkdir(parents=True, exist_ok=False)

    job = {
        "job_id": job_id,
        "status": "ready-for-generation",
        "workflow_version": "0.1.0",
        "inputs": {
            "model_id": model_id,
            "scene_id": scene_id,
            "brand_id": brand_id,
            "landing_page_url": product.get("source", {}).get("landing_page_url"),
            "sku": product.get("sku") or sku,
        },
        "output": {
            "ratios": [ratio],
            "candidate_count_per_ratio": 4,
        },
        "trace": {
            "model_version": model.get("version"),
            "scene_version": scene.get("version"),
            "product_asset_version": product.get("version"),
            "created_at": datetime.now(timezone.utc).isoformat(),
        },
        "review": {
            "product_fidelity": "pending",
            "model_consistency": "pending",
            "creative_quality": "pending",
            "decision": "pending",
            "human_final_gate": "pending",
        },
    }

    (job_dir / "job.yaml").write_text(
        yaml.safe_dump(job, allow_unicode=True, sort_keys=False), encoding="utf-8"
    )
    (job_dir / "candidates").mkdir()
    (job_dir / "review").mkdir()
    return job_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Create one AI creative production job.")
    parser.add_argument("--model", required=True)
    parser.add_argument("--scene", required=True)
    parser.add_argument("--brand", required=True)
    parser.add_argument("--sku", required=True)
    parser.add_argument("--ratio", default="4:5")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()

    output = create_job(Path(args.root), args.model, args.scene, args.brand, args.sku, args.ratio)
    print(output)


if __name__ == "__main__":
    main()
