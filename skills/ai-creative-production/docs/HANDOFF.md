# Handoff Guide

## Why this file exists

這個系統會跨 ChatGPT、Codex、其他聊天視窗與不同 AI Agent 持續開發。

任何接手者開始前必須先讀：

1. `README.md`
2. `docs/BUILD-PLAN.md`
3. `workflows/PIPELINE.md`
4. 本次會使用的 `skills/<skill-name>/SKILL.md`
5. 對應 MVP / job 文件

不要只看最新聊天就重設架構。

---

## Product Goal

最終系統要讓同一個真實 SKU，可以透過固定品牌 Model、合理 Styling、任意 Scene，產出可用於：

- Web / PDP / Lookbook
- EDM
- LINE OA / LINE Ads
- Meta Ads
- Google Ads / PMax

商品真實性優先於畫面創意。

---

## Canonical Architecture

```text
Core Assets
Brand / Model / SKU / Scene
        ↓
Product Understanding
        ↓
SKU USP Optimizer
        ↓
Styling Planner
        ↓
Image Generator
        ↓
Quality Review
        ↓ PASS only
Web / EDM / LINE / Ads Skills
        ↓
Channel Validation
        ↓
Human Final Gate
```

### Architecture Decisions

- 這是一個 modular system，不是一個巨大 Skill。
- Model、Brand、SKU、Scene 是共用資產。
- SKU 只能有一份 canonical source。
- Model 不屬於單一 SKU。
- Scene 可替換，不設固定預設地點。
- 每次生成必須建立 job。
- 原始商品資料不可被生成結果覆蓋。
- Channel Skills 不得修改 Product Identity。
- Review 結果只允許 PASS / CHECK / FAIL。
- Product Fidelity 重大錯誤直接 FAIL。
- 自動 Review 後仍保留人工 Final Gate。
- 採 USP-first：先確認商品賣點與證據，再決定場景、動作、構圖。
- 採 Shot Grammar，不採固定五張模板。
- Staff Styling 為 source content mode，可再分流成 Web / Meta 等 channel output。

---

## 9 Skill Modules

1. `product-understanding`
2. `sku-usp-optimizer`
3. `styling-planner`
4. `image-generator`
5. `quality-review`
6. `channel-web`
7. `channel-edm`
8. `channel-line`
9. `channel-ads`

每個 Skill 都有自己的 Purpose / Input / Output / Validation / Stop Rule。

---

## Model Direction

Model 的長期目的，是建立少量、固定、可重複使用的品牌虛擬 Model。

Model 不只是外貌資產，也承擔 audience signal：讓目標客群對穿著效果產生自我投射。

目前正式投入 MVP 的 approved model：

- `DV1 / Naomi Lin`

Model Card 至少描述：

- appearance
- body shape / proportion
- hair
- age impression
- styling direction
- audience signal
- category fit
- reference assets
- approved base images
- consistency constraints

---

## SKU Direction

Landing Page / SKU 進入系統後，Product Understanding 應盡量取得：

- brand
- product name
- SKU / variant
- product images
- front / back / side / detail / material classification
- color
- material / size
- immutable product features
- presentation clues
- source URLs / provenance

如果資料不足，不可猜測不存在的商品細節。

SKU 後續可延伸 USP Brief、Styling Plan 與多 Channel Output，但商品 source 不重複保存。

---

## USP Direction

`sku-usp-optimizer` 負責把已驗證商品事實轉成：

- USP priority
- evidence status
- visual proof requirement
- must-show details
- reject conditions
- channel-relevant visual signals

任何未驗證 claim 不可進 production copy。

每張母素材都必須回答：這張圖正在幫哪個 SKU 證明什麼？

---

## Styling Direction

Styling Planner 負責把商品事實與 USP 翻譯成：

- target / audience signal
- hero feature
- must-show detail
- dynamic shot plan
- pose / framing
- scene direction
- complementary item direction

Styling 建議是 recommendation，不可反向覆寫 Product Fact。

---

## Review Direction

至少包含：

1. Product Fidelity
2. USP Visibility
3. Model Consistency
4. Human Realism / Anatomy
5. Styling Relevance
6. Scene / Composition
7. Channel Compliance

Logo、顏色、圖案、剪裁、版型、商品長度等重大錯誤不可用平均分補救。

---

## Current Build Status — 2026-09-15

### 已完成

- Modular architecture 定義
- 9 個 Skill module，其中包含 `sku-usp-optimizer`
- Core Asset 單一來源原則
- Canonical workflow
- Eval framework
- Channel separation 原則
- Naomi / DV1 作為正式 MVP model
- 第一個舊 MVP case 保留
- 新 USP-first 真實 MVP case 已建立
- 17 張商品參考圖已從 Drive 實際讀取並 review
- 三個 SKU 的 Visual Lock 已建立
- 三個 SKU 的 USP Brief 已建立
- Dynamic Shot Plan 已建立
- Web Staff Styling + Meta Ads 共用母素材再分流的 Mode C 已正式採用

### Active Real MVP Case

`mvp/cases/descente-naomi-sr323rts77-sr322rkl71-sr322ucp71/`

Inputs:

```text
Model: DV1 / Naomi Lin
Top: SR323RTS77-BEG0
Bottom: SR322RKL71-BLK0
Cap: SR322UCP71-BRW0
```

已通過：

```text
Drive source assets
→ Product visual inspection
→ Visual Lock
→ USP Brief
→ Dynamic Shot Plan
```

母素材規劃為 M01–M06，再分流：

```text
Approved Mother Assets
├── Web Staff Styling
└── Meta Ads 4:5 / 9:16
```

### Active Visual Locks

- `SR323RTS77-BEG0`: light-beige regular-fit technical tee; red chest wordmark, black opposite-shoulder arrow, rear segmented marks, micro technical texture.
- `SR322RKL71-BLK0`: black women’s 6-inch running pocket leggings; wide waistband, fitted mid-thigh length, side pocket/panel seams, reflective dot graphics, lower outer-leg arrow logo.
- `SR322UCP71-BRW0`: muted taupe-brown curved-brim cap; cursive front `descente`, small `design that moves`, fabric rear strap + metal buckle, rear-side arrow logo.

### 下一個執行 Gate

1. Generation proof with Naomi / DV1 and the locked 3-SKU outfit
2. Shot-level Quality Review
3. Look-level consistency review
4. Approved mother-asset selection
5. Web Staff Styling derivative
6. Meta 4:5 / 9:16 derivative

### 尚未完成

- Generation stability regression across repeated runs
- Automated visual Product Fidelity QA
- Automated channel export
- Final operating Web UI / Dashboard

---

## Current Canonical Rule

不要跳過商品 source、Visual Lock、USP Evidence 或 Model approval，就直接生成 production evidence。

在 Active MVP 中，這四個前置條件目前均已具備，因此下一步應直接進 Generation proof，而不是重新討論架構。
