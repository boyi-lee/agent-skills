---
name: ai-creative-production
description: 將固定品牌 Model、品牌 SKU 與場景組合成可驗證的 Meta 廣告素材生產工作流。用於從 Landing Page URL 自動建立商品資產、生成穿著圖、場景圖與 Review Gate。
---

# AI Creative Production

## Outcome

給定：

- 一個既有 Model ID
- 一個 Scene ID
- 一個商品 Landing Page URL
- 一組輸出尺寸

產出：

- 已建立 / 更新的 SKU 資料
- 生成候選圖
- Review 報告
- PASS / CHECK / FAIL 狀態
- 可供人工 Final Gate 的素材

## Non-negotiable Rules

1. 不可把 Model、SKU、Scene 混成同一份不可拆資料。
2. 不可覆蓋原始商品圖。
3. 不可把「看起來差不多」當作商品一致性通過。
4. Logo、顏色、版型、關鍵剪裁明顯錯誤時必須 FAIL。
5. Model 身份若明顯漂移，必須 CHECK 或 FAIL。
6. 自動 Review 不能取代人工 Final Gate。
7. 每次生成必須建立可追蹤的 job 記錄。
8. 若來源商品圖不足，必須標記資料不足，不可幻想缺失細節。

## Required Inputs

```yaml
model: <model-id>
scene: <scene-id>
landing_page_url: <url>
output:
  ratios: ["4:5", "9:16"]
```

## Workflow

### Step 1: Resolve Model
讀取 `models/<model-id>/profile.yaml` 與基準圖。

驗證：Model 必須存在且狀態為 approved。

### Step 2: Resolve Scene
讀取 `scenes/<scene-id>/scene.yaml` 與參考圖。

驗證：Scene 必須存在。

### Step 3: Ingest Landing Page
建立或更新：

`brands/<brand-id>/skus/<sku>/`

至少保存：

- 原始 URL
- 商品名稱
- SKU
- 商品圖片
- 圖片來源
- 關鍵不可變商品特徵

### Step 4: Normalize Product Assets
將抓到的圖片分類為：

- front
- back
- side
- detail
- material
- logo / graphic

不可確定的圖片必須標記 unknown，不可硬猜。

### Step 5: Create Job
建立 `jobs/<job-id>/job.yaml`，記錄：

- model_id
- scene_id
- brand_id
- sku
- landing_page_url
- output spec
- input asset version
- workflow version

### Step 6: Generate
目標流程：

`Model + Product + Scene → Candidate Images`

生成時商品身份優先於畫面創意。

### Step 7: Review
依 `templates/review-checklist.md` 進行三層檢查：

1. Product fidelity
2. Model consistency
3. Creative quality

### Step 8: Decide

- PASS → `outputs/<job-id>/approved/`
- CHECK → 保留於 candidates，等待人工確認
- FAIL → `outputs/<job-id>/rejected/`

### Step 9: Final Gate
只有人工核准後，素材才能被標記為 production-ready。

## Stop Rules

遇到以下情況停止自動往下：

- Landing Page 無法取得商品圖
- SKU 無法辨識且可能混入多商品
- 商品關鍵細節來源不足
- Model profile 不完整
- Review 發現關鍵商品錯誤

## MVP Build Order

1. 資料格式與資料夾
2. Landing Page ingestion
3. 1 Model 建檔
4. 1 Scene 建檔
5. 1 SKU 端到端生成
6. Review Gate
7. 擴至 5 SKU
8. 擴至 2 Models / 3 Scenes

## Definition of Done

一個 job 完成必須具備：

- 可追溯的輸入
- 可重跑的設定
- 生成輸出
- Review 結果
- Final Gate 狀態
- 未修改 source assets