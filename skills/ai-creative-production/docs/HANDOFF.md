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

---

## 8 Skill Modules

1. `product-understanding`
2. `styling-planner`
3. `image-generator`
4. `quality-review`
5. `channel-web`
6. `channel-edm`
7. `channel-line`
8. `channel-ads`

每個 Skill 都有自己的 Purpose / Input / Output / Validation / Stop Rule。

---

## Model Direction

Model 的長期目的，是建立少量、固定、可重複使用的品牌虛擬 Model。

Model 不只是外貌資產，也承擔 audience signal：讓目標客群對穿著效果產生自我投射。

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

SKU 後續可延伸 Styling Plan 與多 Channel Output，但商品 source 不重複保存。

---

## Styling Direction

Styling Planner 負責把商品事實翻譯成：

- target / audience signal
- hero feature
- must-show detail
- shot list
- pose / framing
- scene direction
- complementary item direction

Styling 建議是 recommendation，不可反向覆寫 Product Fact。

---

## Review Direction

至少包含：

1. Product Fidelity
2. Model Consistency
3. Styling Relevance
4. Scene / Composition
5. Channel Compliance

Logo、顏色、圖案、剪裁、版型等重大錯誤不可用平均分補救。

---

## Build Plan

完整建立分 6 步：

1. Repository Foundation
2. Core Asset Contracts
3. Skill Contracts
4. Workflow Orchestration
5. Eval / Review System
6. Real MVP Test

詳見 `docs/BUILD-PLAN.md`。

---

## Current Build Status — 2026-09-13

### 已完成

- Modular architecture 定義
- 8 個 Skill contract
- Core Asset 單一來源原則
- Canonical workflow
- Eval framework
- Channel separation 原則
- 第一個真實 MVP case 建立
- 既有 ingestion / job / review_gate 骨架保留

### Real MVP Case

`mvp/cases/descente-sr123tts23-blu0/`

目前先驗證：

```text
Landing Page
→ Product Understanding
→ Styling Planner
→ Job / Review-ready package
```

第一個 Channel baseline 採 `channel-web`。

### 尚未完成

- 正式 Brand Profile schema 完整化
- 正式 approved Model Card / reference set
- SKU / Styling schema 升級
- 真實 runtime ingestion regression test
- Image Generation engine 選型與 first proof
- 視覺 Product Fidelity 自動 QA
- Channel-specific export automation

---

## Next Canonical Task

優先完成 Step 2 / Step 5 的可執行資料契約：

1. 升級 Brand Profile / Model Card / Product Asset / Styling Plan schemas
2. 對 Real MVP Case 產出第一份 `product.yaml`
3. 產出第一份 `styling-plan.yaml`
4. 建立對應 eval checklist
5. 等 approved Model Card 後再進 Image Generation

不要跳過商品 source 與 Model approval，直接用隨機人物生成 production evidence。
