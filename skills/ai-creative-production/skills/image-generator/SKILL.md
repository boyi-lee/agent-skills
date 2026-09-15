# Skill: Image Generator

## Purpose
根據已核准的 Product Asset、Garment Lock、Model Identity Lock、Styling Plan 與 Scene 生成服飾素材。

## Input
- product asset / canonical product images
- garment lock
- model card
- identity lock + approved model references
- styling plan
- scene card / scene spec
- single-image job contract

## Output
- exactly one generated image per job
- generation manifest
- model / sku / scene references
- technical metadata

## Generation Contract
- `1 job = 1 image`。
- 禁止把多個 Style / Scene / 人物合成一張 production image。
- collage / contact sheet 僅可作 preview，且必須使用獨立 preview job；production job 一律禁止。
- 每個 production job 必須只有 1 位人物、1 個主要場景、1 個明確 shot objective。
- 輸出尺寸與比例必須由 job contract 明確指定，例如 `4:5`。

## Garment Lock Rule
- 商品不得只靠文字描述重新生成。
- canonical product reference images 必須隨 generation job 一起提供。
- Logo、wordmark、字的位置、圖案、標籤、版型、長度、縫線、口袋與帽體結構屬 immutable features。
- 只允許因姿勢 / 透視 / 光線造成自然皺摺、陰影與合理形變。
- 任一 immutable feature 明顯錯誤，素材不得宣告成功，必須進 FAIL review。

## Model Identity Lock Rule
- Naomi / DV1 production job 必須載入 `identity-lock.yaml` 與至少 3 張 approved identity references。
- 只給文字 Model Card 不足以進 production generation。
- 臉型、五官比例、膚質方向、體態比例必須維持 DV1 identity。
- Pose、表情、髮型整理方式、鏡位與場景可以變；人物身份不可變。

## No-Hallucination Rule
- `allow_unlisted_objects` 預設必須為 `false`。
- 場景只允許 scene spec `allowed` 或 `required` 的物件。
- 不可自行新增水壺、包包、耳機、手機、手錶、毛巾、外套、鞋款、配件或其他品牌物件。
- 如果未列入 allowlist 的前景 / 互動物件被生成，直接送 `FAIL`。
- 背景環境中不可避免且非互動的遠景元素可由 Quality Review 判定是否接受，但不得新增會改變商品敘事的道具。

## Must Do
- Product Identity 優先。
- Model identity 必須一致。
- Scene 可替換，不得寫死。
- 每張生成圖必須能追溯到 SKU、Garment Lock、Model、Identity Lock、Scene、Styling Plan 與 job_id。

## Must Not Do
- 不可自行改 Logo、顏色、字樣、圖案、剪裁、版型與關鍵商品細節。
- 不可自行加未批准物件。
- 不可用生成結果覆蓋 source asset。
- 不可直接宣告素材可商用，必須送 Quality Review。

## Validation
輸出必須同時通過：
- single-image contract validation
- garment-lock preflight
- identity-lock preflight
- no-hallucination preflight

所有生成圖片完成後一律進入 `PENDING_REVIEW`。

## Stop Rule
以下任一發生不得生成 production asset：
- 缺少 Product Asset / canonical product images
- 缺少 Garment Lock
- 缺少 Model Card 或 Identity Lock
- Naomi job 少於 3 張 approved identity references
- Job 未明確指定 `image_count: 1`
- `collage: true`
- `allow_unlisted_objects: true`
