# Skill: Image Generator

## Purpose
根據已核准的 Product Asset、Model Card、Styling Plan 與 Scene 生成服飾素材。

## Input
- product asset
- model card
- styling plan
- scene card / scene spec
- output ratio / resolution

## Output
- generated images
- generation manifest
- model / sku / scene references
- technical metadata

## Must Do
- Product Identity 優先。
- Model identity 必須一致。
- Scene 可替換，不得寫死。
- 每張生成圖必須能追溯到 SKU、Model、Scene、Styling Plan 與 job_id。

## Must Not Do
- 不可自行改 Logo、顏色、圖案、剪裁、版型與關鍵商品細節。
- 不可用生成結果覆蓋 source asset。
- 不可直接宣告素材可商用，必須送 Quality Review。

## Validation
輸出必須具備完整 provenance，且所有圖片進入 `PENDING_REVIEW`。

## Stop Rule
缺少 Product Asset、Model Card 或 Styling Plan 時不得生成 production asset。
