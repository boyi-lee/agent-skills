# Skill: Quality Review

## Purpose
在任何渠道加工前，驗證商品、Model、Styling、USP 呈現、輸出契約與畫面是否符合商用標準。

## Input
- generated image
- source product asset / canonical product images
- garment lock
- identity lock + approved model references
- USP brief
- model card
- styling plan
- scene spec
- job contract

## Output
- PASS / CHECK / FAIL
- issue list
- severity
- repair suggestion
- review evidence

## Hard Fail
以下任一發生即 FAIL：
- Logo 明顯錯誤或遺失
- Wordmark 拼字、字型風格、顏色、比例或位置明顯錯誤
- 商品顏色明顯錯誤
- 版型 / 圖案 / 剪裁 / 長度 / 口袋 / 縫線與 source 不符
- 生成出不存在的商品細節
- Garment Lock immutable feature 錯誤
- Model 身份明顯漂移
- Naomi / DV1 未符合 Identity Lock
- 人體嚴重異常
- 畫面宣稱或暗示官方未驗證的商品功能
- production job 生成超過 1 張圖或產出 collage / multi-panel
- production image 出現超過 1 位主要人物
- 出現 scene allowlist 以外的互動道具或商品敘事物件

## Review Dimensions
- Product Fidelity / Garment Lock
- Model Consistency / Identity Lock
- Single-image Job Contract
- No-Hallucination Rule
- USP Visibility / Visual Proof
- Styling Relevance
- Scene / Lighting / Composition
- Technical Quality

## Garment Lock Gate
逐項比對 generated crop 與 canonical product reference：
- logo
- wordmark
- colorway
- silhouette
- garment length
- graphics
- seams
- pockets
- labels / hardware

規則：
- immutable feature 錯誤 → `FAIL`
- invented product detail → `FAIL`
- 因角度看不到、無法確定 → `CHECK`

## Identity Lock Gate
Naomi / DV1 必須檢查：
- face identity
- body proportion
- natural skin texture
- athletic but non-bodybuilder body definition
- hair color family

規則：
- identity 明顯漂移 → `FAIL`
- 只是表情、髮型整理、姿勢不同 → 可接受
- 人物看起來像 generic AI influencer，而不是 DV1 → `FAIL`

## Single-image Gate
Production job 必須：
- exactly 1 image
- exactly 1 primary person
- exactly 1 primary scene
- collage = false
- contact_sheet = false

任一不符 → `FAIL`，不得人工用裁切方式假裝通過。

## No-Hallucination Gate
比對 scene spec：
- allowed
- required
- forbidden

若畫面自行新增未批准的水壺、包包、耳機、手機、手錶、毛巾、外套、額外鞋款、配件或其他品牌物件 → `FAIL`。
背景中不可避免且不參與敘事的遠景元素可標記 `CHECK`。

## USP Gate
每張 production image 必須回答：
1. 這張圖主要在傳達哪個 SKU USP？
2. 觀眾是否能在約 3 秒內理解主要商品價值或使用情境？
3. 畫面是否真的提供對應的 visual proof，而不只是漂亮？
4. 若 USP 屬功能 claim，是否有 verified source，而非靠畫面猜測？

判定：
- 商品正確但 USP 不清楚 → `CHECK`，要求調整 shot / framing / scene。
- 畫面與指定 USP 完全無關、且沒有其他明確商品任務 → `FAIL`。
- 商品功能 claim 無來源 → `FAIL`。

## Rule
重大商品、身份、輸出契約或 hallucination 錯誤不得由其他高分抵銷；漂亮不能抵銷錯誤商品。

## Stop Rule
只有 PASS 素材可進 Channel Skill；CHECK 需人工確認；FAIL 退回前一階段。
