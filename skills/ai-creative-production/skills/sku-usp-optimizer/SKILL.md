# Skill: SKU USP Optimizer

## Purpose
把已驗證的 SKU 商品事實與 USP，轉成可執行的視覺證據、動作、構圖、場景與拍攝 / 生成策略。

核心問題不是「畫面好不好看」，而是：**這張圖正在幫 SKU 賣什麼？**

## Input
- product asset / sku_id
- verified claims / USP
- source product images
- model card（可選）
- scene spec（可選）
- channel（可選）

## Output
- USP priority
- visual proof points
- must-show product details
- shot objectives
- recommended shot grammar
- scene rationale
- movement rationale
- detail-shot requirements
- unsupported / unproven USP list
- review criteria

## Core Rule
先決定 USP，再決定畫面。Scene、pose、framing 都必須服務 SKU 的賣點，而不是反過來。

## USP Evidence Levels
每個 USP 必須標記：
- `verified_fact`: LP / 官方資料可直接驗證
- `visual_inference`: 可由商品圖片合理觀察，但不是官方 claim
- `creative_hypothesis`: 創意呈現假設，不得寫成商品事實

只有 `verified_fact` 可直接作為商品功能 claim。

## Visual Proof Mapping
每個優先 USP 至少對應一種可觀察的視覺證據，例如：
- 版型 / 比例 → full body / side / 45-degree
- 活動度 → walking / stretching / running-prep
- 背面圖案 → back / turn-around
- 鞋底結構 → low-angle side detail
- 材質 / 織法 → close-up detail
- 顏色 / 搭配性 → full-look contextual shot

注意：吸濕快乾、UV、防水等功能若無法從單張圖片直接證明，不得把「看起來」當功能驗證。畫面只能支援使用情境，claim 仍需來源證據。

## Shot Grammar, Not Fixed Template
不得強制每個 SKU 固定拍同樣 5 張。

系統應從以下 shot grammar 動態組合：
- hero / full-look
- movement
- interaction
- product-detail
- fit / silhouette
- front / side / back
- candid lifestyle
- low-angle footwear
- close-up material

每次依 USP、SKU 類型、Model 與 Scene 選擇最合理組合。

## Diversity Rule
同一 SKU 的新一組 Staff Styling，至少 60% 的主要構圖 / 動作不可與上一組重複，除非該構圖是商品驗證必要鏡位。

## Staff-Style Principle
若目標是 BEAMS-like / staff styling：
- 優先真人紀錄感，不做廣告大片式僵硬 pose
- 保留自然不對稱、自然皺摺、場景互動與表情變化
- Model 行為需符合場景，不能只是換背景後重複站姿
- 圖片仍必須讓 SKU 可辨識，不能為了生活感遮掉商品

## Must Do
- 先讀 `product-understanding` 的 verified facts。
- 對 USP 排優先順序，不要求一張圖承擔所有賣點。
- 明確列出每張 shot 的 `purpose` 與 `usp_to_show`。
- 把商品不可變細節帶進 must-show / must-not-change。
- 商品資料不足時停止，不自行補 claim。

## Must Not Do
- 不創造官方沒有的 USP。
- 不用「漂亮」、「高級」、「有質感」代替具體賣點。
- 不讓 Scene 搶掉商品。
- 不因想證明 USP 而扭曲商品版型或結構。
- 不把固定 shot list 當唯一模板。

## Validation
每個輸出至少回答：
1. 這個 SKU 最重要的 1–3 個 USP 是什麼？
2. 每個 USP 的來源證據是什麼？
3. 每個 USP 要用什麼畫面證據呈現？
4. 哪些商品細節在生成中不可變？
5. 如果觀眾三秒內看不出這張圖要傳達什麼，該 shot 應重做或刪除。

## Stop Rule
若 USP 沒有來源、商品 Visual Lock 尚未完成、或關鍵商品圖不足，標記 `NEEDS_SOURCE_REVIEW`，不得送 Image Generator 做 production asset。
