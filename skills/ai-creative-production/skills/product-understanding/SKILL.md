# Skill: Product Understanding

## Purpose
把 Landing Page / SKU 轉成可供後續生成與驗證使用的結構化商品資料。

## Input
- brand_id
- landing_page_url 或 sku_id

## Output
- sku_id
- product title / category / color / material / size
- source images
- key product features
- immutable product features
- presentation clues
- source provenance

## Must Do
- 優先保存原始商品資料與圖片。
- 把正面、背面、細節、材質、Logo / 圖案等分開標記。
- 找出商品最需要被呈現的特徵。
- 無法確認的欄位標記 unknown，不猜測。

## Must Not Do
- 不生成商品圖。
- 不修改商品特徵。
- 不替品牌創造不存在的 USP。

## Validation
若無法確認 SKU、核心商品圖片或關鍵細節來源，狀態不得為 PASS。

## Stop Rule
商品真實資料不足時停止並標記 `NEEDS_SOURCE_REVIEW`。
