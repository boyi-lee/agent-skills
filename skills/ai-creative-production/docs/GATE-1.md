# Gate 1 — Asset Ingestion & Readiness

## 目的

先證明資料流能跑通，再進入昂貴且難驗證的圖像生成。

Gate 1 不解決「衣服穿得夠不夠像」，只解決：

1. Landing Page URL 能被讀取
2. 商品來源與圖片能被保存
3. Brand / SKU 能建立固定位置
4. Model / Scene / Product 都有正式資料卡
5. Scene 可以被自由替換，不綁定任何預設地點
6. 每次生成前能檢查資料是否完整
7. 每次工作都能建立可追蹤 job

## 最小執行順序

```bash
cd skills/ai-creative-production
python -m pip install -r requirements.txt

python workflows/ingest_product.py \
  "https://example.com/product" \
  --brand <brand-id> \
  --sku <sku>

python workflows/review_gate.py \
  --model <model-id> \
  --scene <scene-id> \
  --brand <brand-id> \
  --sku <sku-slug>

python workflows/create_job.py \
  --model <model-id> \
  --scene <scene-id> \
  --brand <brand-id> \
  --sku <sku-slug> \
  --ratio 4:5
```

> `<scene-id>` 可以是任何已建立的 Scene Card，例如公園、健身房、球場、城市街道、棚拍等。任何文件裡出現的具體場景都只是範例，不是系統預設值。

## 預期結果

商品資料：

```text
brands/<brand-id>/skus/<sku-slug>/
├── raw/
│   ├── landing-page.html
│   ├── source-url.txt
│   └── image-001...
├── product.yaml
└── ingestion-report.json
```

工作資料：

```text
jobs/<job-id>/
├── job.yaml
├── candidates/
└── review/
```

## Gate 1 PASS 條件

在進入正式生成前：

- Model Card 已人工核准
- Model 有 approved base images
- 本次指定 Scene Card 可讀且資料完整
- Product 有 Landing Page source URL
- Product 至少有一張來源商品圖
- Product 已人工確認來源正確

只要缺一項，`review_gate.py` 回傳 `CHECK`，不應進入批次生成。

## Scene 原則

Scene 是「本次生成工作的可替換輸入」，不是固定品牌資產綁定。

Scene 可以來自：

- 文字描述
- 真實地點
- 使用者提供的參考圖片
- 已建立 Scene Card
- 品牌核准的場景模板

核心 workflow 不得寫死任何特定地點名稱。

## 已知限制

目前通用 ingestion 只能盡力讀取 HTML、JSON-LD、Open Graph 與 img 標籤。

遇到以下網站時需要 brand-specific adapter：

- JavaScript 動態載入商品圖
- 圖片藏在特殊 API / GraphQL
- 防爬限制
- 同頁包含大量非商品圖片

因此 scale 原則不是把所有例外塞進單一 scraper，而是：

```text
Generic Ingestor
  ├── Shopify Adapter
  ├── Brand-specific Adapter
  └── Manual fallback
```

## 下一個 Gate

Gate 2 才開始處理：

- 商品圖片分類（正面 / 背面 / 細節 / 材質）
- Model approved reference set
- 通用 Scene 輸入與 reference set
- 第一個試穿 / 合成 engine
- 生成後 Product Fidelity / Model Consistency / Scene Match Review

在 Gate 1 沒跑通以前，不提前堆圖像模型。
