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
2. Styling Planner
        ↓
3. Job Manifest
        ↓
4. Image Generator
        ↓
5. Quality Review
        ↓
   PASS only
        ↓
6. Channel Skills
   ├─ Web
   ├─ EDM
   ├─ LINE
   └─ Ads
        ↓
7. Channel Validation
        ↓
8. Human Final Gate
        ↓
9. Approved Outputs
```

## Rules

- Product Understanding 是商品事實來源。
- Styling Planner 可以提出創意建議，但不可覆寫商品事實。
- Image Generator 只能使用已建立的 Product Asset、Model Card 與 Styling Plan。
- Quality Review 位於所有 Channel Skill 之前。
- Channel Skill 不得跳過 Quality Review。
- 一次 job 可以輸出多個 channel，但全部必須回指同一份 approved source asset。

## Retry Logic

- 商品資料不足 → Product Understanding
- 穿搭方向不合理 → Styling Planner
- 商品 / Model 生成錯誤 → Image Generator
- Channel 規格錯誤 → 只重跑 해당 Channel Skill，不重新生成商品

## Human Responsibilities

人工主要負責：
- 核准 Model Card
- 處理商品來源不明確的例外
- CHECK 案件
- Final Gate

其餘重複性資料處理應逐步自動化。
