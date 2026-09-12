# AI Creative Production System

## Purpose

建立一套可 scale、可驗證、可交接的 AI 服飾素材生產系統。

最終用途不是單一廣告平台，而是讓同一個真實 SKU 能安全地產出：

- 官網 / PDP / Lookbook
- EDM
- LINE OA / LINE Ads
- Meta Ads
- Google Ads / PMax

核心原則：**商品真實性優先於生成自由度。**

---

## System Concept

這不是一個巨大 Skill，而是一個由共用資產與多個專職 Skill 組成的系統。

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
┌─────────┬─────────┬─────────┬─────────┐
Web       EDM       LINE      Ads
Skill     Skill     Skill     Skill
```

### One Source, Many Outputs

SKU、Model、Brand、Scene 都只有一份 canonical source。

不同渠道只能加工已核准素材，不得各自建立另一份商品真相。

> Source 一份，Output 多份。

---

## Core Assets

### Brand
保存品牌定位、視覺規範、Target 邏輯與禁止事項。

### Model
品牌固定虛擬 Model。除了外貌與身形，也承擔 audience signal：讓目標客群看到素材時能產生「這就是我 / 我穿起來可能就是這樣」的投射。

### SKU
保存 Landing Page、商品圖、細節圖、材質、尺寸、Logo / 圖案 / 剪裁等不可任意更改的 Product Identity。

### Scene
獨立、可自由替換。可以是真實地點、室內、棚拍、街道、球場、自然環境、參考圖或純文字定義。

任何具體地點都只能是 example，不得寫死成系統預設。

---

## 8 Skills

### 1. `product-understanding`
回答：**這件商品到底是什麼？**

把 Landing Page / SKU 轉成結構化 Product Asset，保存來源證據並找出不可變商品特徵。

### 2. `styling-planner`
回答：**這件商品應該怎麼被呈現？**

根據商品、Brand、Model、Target 與用途決定 hero feature、shot、pose、搭配與 scene direction。

### 3. `image-generator`
回答：**如何把核准的商品、Model、Styling、Scene 生成成圖？**

不得自行改商品身份。

### 4. `quality-review`
回答：**這張圖能不能進正式渠道？**

Product Fidelity 有 Hard Fail 權限。Logo、顏色、版型、圖案等重大錯誤不能被其他高分抵銷。

### 5. `channel-web`
把 PASS 素材轉成 PDP / Lookbook / 官網版位。

### 6. `channel-edm`
把 PASS 素材轉成 EDM hero / product block / supporting visual。

### 7. `channel-line`
把 PASS 素材轉成 LINE OA / LINE Ads 的手機版位。

### 8. `channel-ads`
把 PASS 素材轉成 Meta / Google / PMax 等廣告素材變體。

---

## Canonical Workflow

```text
1. 指定 Brand
2. 指定 Model（或由 Brand rules 選擇）
3. 貼 Landing Page URL / SKU
4. 指定 Scene，或讓 Styling Planner 建議
5. 指定 Output Channel
6. Product Understanding
7. Styling Planner
8. 建立 Job Manifest
9. Image Generator
10. Quality Review
11. PASS → Channel Skill
12. Channel Validation
13. Human Final Gate
14. Approved Output
```

詳細見 `workflows/PIPELINE.md`。

---

## Repository Structure

```text
ai-creative-production/
├── README.md
├── SKILL.md
│
├── core-assets/
│   └── README.md
│
├── models/                     # 現有 canonical Model assets
├── brands/                     # 現有 canonical Brand / SKU assets
├── scenes/                     # 現有 canonical Scene assets
│
├── skills/
│   ├── product-understanding/
│   ├── styling-planner/
│   ├── image-generator/
│   ├── quality-review/
│   ├── channel-web/
│   ├── channel-edm/
│   ├── channel-line/
│   └── channel-ads/
│
├── workflows/
│   └── PIPELINE.md
├── evals/
│   └── README.md
├── mvp/
│   └── cases/
├── jobs/
├── outputs/
├── reviews/
├── schemas/
├── templates/
└── docs/
    ├── BUILD-PLAN.md
    ├── SCALE-RULES.md
    └── HANDOFF.md
```

目前保留舊版 `models/`、`brands/`、`scenes/` 路徑作為 canonical source，避免為了漂亮資料夾而複製資料。後續若正式獨立成新 repo，再做一次有版本紀錄的 migration。

---

## Quality Principles

1. 商品來源只有一份。
2. 原始商品資料不可被生成結果覆蓋。
3. Channel Skill 不可修改 Product Identity。
4. Model identity 必須可重複使用且可驗證。
5. Scene 可任意替換，不應影響 SKU / Model 定義。
6. 每次生成都是可追蹤 job。
7. 每張正式素材必須經 Quality Review。
8. 商品重大錯誤直接 FAIL。
9. 所有 Channel 都要有自己的輸出規格驗證。
10. 真實 production failure 必須回寫成 rule / eval / regression case。

---

## Build Plan

完整建立分為 6 步：

1. Repository Foundation
2. Core Asset Contracts
3. Skill Contracts
4. Workflow Orchestration
5. Eval / Review System
6. Real MVP Test

詳見 `docs/BUILD-PLAN.md`。

---

## Current MVP

第一個真實 case：

`mvp/cases/descente-sr123tts23-blu0/`

先驗證：

`Landing Page → Product Understanding → Styling Planner → Job / Review-ready package`

第一個 output channel 採 `channel-web`，因為官網最能檢驗商品穿著是否可信、細節是否足以支援購買決策。Web baseline 通過後，再延伸到 EDM、LINE、Meta 與 Google。

正式 Image Generation 前仍需一張已核准的品牌 Model Card。

---

## Handoff Rule

任何 ChatGPT、Codex 或其他 Agent 接手前至少先讀：

1. `README.md`
2. `docs/BUILD-PLAN.md`
3. `workflows/PIPELINE.md`
4. 本次會用到的 `skills/<skill-name>/SKILL.md`
5. 對應 MVP / job 文件

不得只靠聊天上下文重新發明架構。
