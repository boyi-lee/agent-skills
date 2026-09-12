# Canonical Production Pipeline

## Standard Flow

```text
Input
  brand_id
  model_id
  landing_page_url / sku_id
  scene (optional)
  channels[]
        ↓
1. Product Understanding
        ↓
2. SKU USP Optimizer
        ↓
3. Styling Planner
        ↓
4. Job Manifest
        ↓
5. Image Generator
        ↓
6. Quality Review
        ↓
   PASS only
        ↓
7. Channel Skills
   ├─ Web
   ├─ EDM
   ├─ LINE
   └─ Ads
        ↓
8. Channel Validation
        ↓
9. Human Final Gate
        ↓
10. Approved Outputs
```

## Rules

- Product Understanding 是商品事實來源。
- SKU USP Optimizer 只可使用已驗證商品事實與來源，把 USP 轉成 visual proof，不可創造官方未提供的 claim。
- Styling Planner 根據 USP Brief、Model、Scene 與 Channel 決定具體呈現方式，但不可覆寫商品事實。
- Shot planning 採 `shot grammar`，不是固定模板；每張圖都必須有明確商品任務。
- Image Generator 只能使用已建立的 Product Asset、USP Brief、Model Card 與 Styling Plan。
- Quality Review 位於所有 Channel Skill 之前，並包含 USP Visibility / Visual Proof Gate。
- Channel Skill 不得跳過 Quality Review。
- 一次 job 可以輸出多個 channel，但全部必須回指同一份 approved source asset。

## Retry Logic

- 商品資料不足 → Product Understanding
- USP 缺乏來源或 Visual Lock 不完整 → Product Understanding / SKU USP Optimizer
- USP 正確但 shot 無法有效呈現 → SKU USP Optimizer / Styling Planner
- 穿搭方向不合理 → Styling Planner
- 商品 / Model 生成錯誤 → Image Generator
- 商品正確但看不出素材任務 → 回到 SKU USP Optimizer / Styling Planner
- Channel 規格錯誤 → 只重跑該 Channel Skill，不重新生成商品

## Human Responsibilities

人工主要負責：
- 核准 Model Card
- 處理商品來源不明確的例外
- CHECK 案件
- Final Gate

其餘重複性資料處理應逐步自動化。
