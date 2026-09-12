# Skill: Styling Planner

## Purpose
根據 SKU、Brand、Model 與渠道目的，決定「這件商品應該怎麼被呈現」。

## Input
- brand_id
- sku_id / product asset
- model_id（可選）
- scene_id / scene spec（可選）
- channel（可選）

## Output
- target / audience signal
- styling direction
- hero feature
- must-show details
- recommended shots
- recommended scene type
- pose / framing guidance
- complementary item guidance
- creative rationale

## Must Do
- 先讀商品真實特徵，再決定拍法。
- Model 應傳遞品牌或品類 Target，而不是只當漂亮人物。
- 若商品有明確視覺特徵，例如背面圖案、特殊剪裁，需列為 must-show。

## Must Not Do
- 不修改 SKU 真實特徵。
- 不憑空創造商品功能。
- 不因渠道不同而改變商品身份。

## Validation
每個 styling plan 必須回答：給誰看、主打什麼、怎麼拍、為什麼。

## Stop Rule
若商品特徵不足以支撐 styling 判斷，退回 Product Understanding。
