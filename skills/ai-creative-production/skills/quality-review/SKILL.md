# Skill: Quality Review

## Purpose
在任何渠道加工前，驗證商品、Model、Styling 與畫面是否符合商用標準。

## Input
- generated image
- source product asset
- model card
- styling plan
- scene spec

## Output
- PASS / CHECK / FAIL
- issue list
- severity
- repair suggestion
- review evidence

## Hard Fail
以下任一發生即 FAIL：
- Logo 明顯錯誤或遺失
- 商品顏色明顯錯誤
- 版型 / 圖案 / 剪裁與 source 不符
- 生成出不存在的商品細節
- Model 身份明顯漂移
- 人體嚴重異常

## Review Dimensions
- Product Fidelity
- Model Consistency
- Styling Relevance
- Scene / Lighting / Composition
- Technical Quality

## Rule
重大商品錯誤不得由其他高分抵銷。

## Stop Rule
只有 PASS 素材可進 Channel Skill；CHECK 需人工確認；FAIL 退回前一階段。
