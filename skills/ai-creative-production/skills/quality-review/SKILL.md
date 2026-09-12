# Skill: Quality Review

## Purpose
在任何渠道加工前，驗證商品、Model、Styling、USP 呈現與畫面是否符合商用標準。

## Input
- generated image
- source product asset
- USP brief
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
- 畫面宣稱或暗示官方未驗證的商品功能

## Review Dimensions
- Product Fidelity
- Model Consistency
- USP Visibility / Visual Proof
- Styling Relevance
- Scene / Lighting / Composition
- Technical Quality

## USP Gate
每張 production image 必須回答：
1. 這張圖主要在傳達哪個 SKU USP？
2. 觀眾是否能在約 3 秒內理解主要商品價值或使用情境？
3. 畫面是否真的提供對應的 visual proof，而不只是漂亮？
4. 若 USP 屬功能 claim，是否有 verified source，而非靠畫面猜測？

判定：
- 商品正確但 USP 不清楚 → `CHECK`，要求調整 shot / framing / scene。
- 畫面與指定 USP 完全無關、且沒有其他明確商品任務 → `FAIL` 作為無效素材。
- 商品功能 claim 無來源 → `FAIL`。

## Rule
重大商品錯誤不得由其他高分抵銷；漂亮也不能抵銷「沒有商品任務」。

## Stop Rule
只有 PASS 素材可進 Channel Skill；CHECK 需人工確認；FAIL 退回前一階段。
