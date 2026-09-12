---
name: ai-creative-production
description: Orchestrate modular AI fashion creative production from landing page / SKU to verified multi-channel assets for Web, EDM, LINE, Meta Ads and Google Ads.
---

# AI Creative Production Orchestrator

## Purpose

本檔案是系統總控，不取代任何子 Skill。

總控責任只有三件事：
1. 決定流程順序
2. 傳遞正確資產與狀態
3. 阻止未通過 Review 的素材進入正式 Channel

## Inputs

```yaml
brand_id: <brand-id>
model_id: <approved-model-id>
landing_page_url: <url>
scene: <scene-id-or-spec>
channels:
  - web
  - edm
  - line
  - ads
```

`scene` 可由使用者指定，也可先交由 Styling Planner 建議。

## Canonical Flow

```text
Product Understanding
→ Styling Planner
→ Job Manifest
→ Image Generator
→ Quality Review
→ PASS only
→ Channel Skill(s)
→ Channel Validation
→ Human Final Gate
```

## Skill Routing

- 商品事實：`skills/product-understanding/SKILL.md`
- 穿搭 / 呈現策略：`skills/styling-planner/SKILL.md`
- 生圖：`skills/image-generator/SKILL.md`
- 商用品質審核：`skills/quality-review/SKILL.md`
- 官網：`skills/channel-web/SKILL.md`
- EDM：`skills/channel-edm/SKILL.md`
- LINE：`skills/channel-line/SKILL.md`
- Meta / Google Ads：`skills/channel-ads/SKILL.md`

## Non-Negotiable Rules

1. SKU、Model、Brand、Scene 都只有一份 canonical source。
2. Source 一份，Output 多份。
3. Channel Skill 不得改 Product Identity。
4. 原始商品資料不可被生成結果覆蓋。
5. Product Fidelity 重大錯誤直接 FAIL。
6. Model 必須是 approved asset 才能產出 production evidence。
7. Styling recommendation 不可覆寫商品事實。
8. 每次 production run 都要有 job_id 與 provenance。
9. CHECK 必須人工處理；FAIL 不得往下流。
10. 真實 production failure 要回寫 rule / schema / eval。

## Stop Rules

立即停止往下流若：
- 商品來源不足或 SKU 不明確
- approved Model Card 不存在
- Product Asset 未完成
- Styling Plan 含未被來源支持的商品宣稱
- Quality Review = CHECK / FAIL
- Channel 輸出缺少必要規格

## Definition of Done

一個 production job 完成必須包含：
- canonical input assets
- product.yaml
- styling-plan.yaml
- job manifest
- generated candidates
- quality review result
- channel output manifest
- human final gate status

詳細架構讀 `README.md`、`docs/BUILD-PLAN.md`、`workflows/PIPELINE.md`。
