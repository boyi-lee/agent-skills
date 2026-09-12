# MVP Case 001 — DESCENTE SR123TTS23-BLU0

## Purpose

用真實商品頁驗證第一條 vertical slice：

Landing Page → Product Understanding → Styling Planner → Job Manifest → Review-ready package。

本 case 先不把「是否能成功生成商用 Model 穿搭圖」當成功條件；Image Generation 必須等品牌 Model Card 核准後再進行。

## Source

- Brand: DESCENTE Taiwan
- Landing Page: https://descente.tw/products/descente-mens-t-shirts-sr123tts23-blu0
- Product family: TOUGH Light
- Base SKU: SR123TTS23-BLU0

## Observed Product Facts

以下只記錄商品頁可支持的資訊：

- Product: UNI [TOUGH Light] Standard Short Sleeve TS 男士 運動上衣
- Color: 藍色
- Category: 男士運動短袖上衣
- Material / feature family: Tough Light
- Product claims shown on page:
  - 高彈力
  - 吸濕快乾
  - 防紫外線
  - 耐用與舒適
- Visual / construction details:
  - 胸前品牌標誌
  - 背面字母印花
  - 聚酯網眼領口加固
- Page model reference: 男性 184cm / L

## Initial Presentation Clues

這些是 Styling Planner 的「建議」，不是商品事實：

### Hero Feature Candidates
1. 背面字母印花
2. 胸前品牌標誌
3. 運動短袖的版型與活動感
4. 領口結構細節

### Shot Candidates
- Full body / active stance：呈現整體 fit
- Back 3/4 view：呈現背面字母印花
- Half body front：呈現胸前品牌標誌
- Detail crop：領口與布料細節

### Audience Hypothesis
待 Brand Profile / Model Card 驗證，不在此 case 直接寫死。

## Model

`PENDING_APPROVED_MODEL_CARD`

正式生成前必須指定已核准品牌 Model。Model 本身需承擔 audience signal，而不是隨機人物。

## Scene

Scene 不寫死。

MVP 至少應測：
- 1 個品牌合理的 lifestyle scene
- 1 個較乾淨的商品理解 scene

具體 Scene 由 Styling Planner 建議或使用者指定。

## First Channel

第一個 channel 建議先跑 `channel-web`。

原因：官網素材最能檢驗商品本體是否清楚、穿著是否可信、細節是否能支援購買決策。Web PASS 後，再延伸 Meta / Google / EDM / LINE。

## MVP Assertions

### Product Understanding
- [ ] SKU 抽取正確
- [ ] 商品主圖 / 細節圖能分類
- [ ] 商品頁文字資訊能保存 provenance
- [ ] 不把促銷 Banner / icon 當商品圖
- [ ] immutable features 建立完成

### Styling Planner
- [ ] 能指出背面印花為重要呈現候選
- [ ] 能提出至少 3 種有目的的 shot
- [ ] 每個 shot 都能說明「為什麼這樣拍」
- [ ] 不創造商品頁沒有的功能

### Model / Generation
- [ ] Model Card 核准後才可執行
- [ ] Model 與 Target 定位有明確關係
- [ ] 商品 fidelity 進入 Quality Review

### Web Channel
- [ ] 至少 1 張 full-body look
- [ ] 至少 1 張商品關鍵特色 shot
- [ ] 版位可直接作為 PDP / Lookbook 候選

## Current Status

`IN_PROGRESS`

目前可執行：Product Understanding / Styling Planning。

目前阻塞：尚未有正式核准的品牌 Model Card，因此不應把隨機 Model 生成結果視為 MVP production evidence。
