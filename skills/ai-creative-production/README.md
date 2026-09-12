# AI Creative Production Skill

## Purpose

建立一套可 scale、可驗證、可交接的 AI 廣告素材生產系統。

核心使用情境：

> 指定 `Model A` + 指定場景（例如大安森林公園）+ 貼上商品 Landing Page URL → 系統自動抓取商品資料與圖片 → 將正確商品套用到固定品牌 Model → 生成廣告圖 → 自動 Review → 人工 Final Gate。

這個專案的重點不是「讓 AI 畫一件很像的衣服」，而是把 **Model、商品 SKU、場景** 都當成可重複使用的資產，再由工作流組合。

---

## Core Objects

系統只有三個主要資產：

1. **Model**：固定品牌虛擬模特兒，保存樣貌、身形、髮型、氣質、基準圖與一致性規則。
2. **Brand / SKU**：品牌底下的商品資料，每個 SKU 保存 Landing Page、商品圖、細節圖與不可被改動的商品特徵。
3. **Scene**：可重複使用的場景設定，例如大安森林公園、健身房、城市街道、高爾夫球場。

最終工作只是：

`Model + SKU + Scene + Output Spec → Generate → Review → Final`

---

## Target Workflow

```text
1. 選 Model
2. 選 Scene
3. 貼 Landing Page URL
4. 自動抓商品名稱 / SKU / 商品圖 / 細節圖
5. 自動建立 SKU 資料
6. 套用商品到固定 Model
7. 生成指定場景與尺寸
8. 自動 Review
   - 商品一致性
   - Model 一致性
   - 場景與畫面品質
9. PASS / CHECK / FAIL
10. 人工 Final Gate
11. 合格素材進入 Meta 素材池
```

---

## Folder Structure

```text
ai-creative-production/
├── README.md
├── SKILL.md
│
├── models/                 # 固定品牌 Model 資產
│   └── <model-id>/
│       ├── card/
│       ├── references/
│       ├── base-images/
│       └── profile.yaml
│
├── brands/                 # 品牌與 SKU 資產
│   └── <brand-id>/
│       ├── brand-profile/
│       └── skus/
│           └── <sku>/
│               ├── raw/
│               ├── clean/
│               ├── metadata/
│               └── landing-page/
│
├── scenes/                 # 可重複使用場景
│   └── <scene-id>/
│       ├── references/
│       └── scene.yaml
│
├── workflows/              # 自動化工作流
│   ├── ingest-product/
│   ├── build-model/
│   ├── dress-product/
│   ├── compose-scene/
│   └── review/
│
├── jobs/                   # 每次生成任務
│   └── <job-id>/
│
├── outputs/                # 生成結果
│   └── <job-id>/
│       ├── candidates/
│       ├── approved/
│       └── rejected/
│
├── reviews/                # Review 結果
│   └── <job-id>/
│
├── schemas/                # 固定資料格式
├── templates/              # 可複製模板
└── docs/                   # 架構、scale、handoff 文件
```

---

## Model Strategy

Model 不屬於任何單一 SKU。

每個 Model 是獨立品牌資產，可以重複穿數十或數百個 SKU。

可用真人 / Instagram 作為「方向參考」，但 production 角色必須重新建立成品牌自己的虛擬 Model：

```text
參考人物
→ 提取身形 / 年齡感 / 髮型 / 氣質方向
→ 改變可辨識身份特徵
→ 建立新角色
→ 固定角色卡與基準圖
→ 後續重複使用
```

Review 必須同時確認：

- 每次生成仍像同一個品牌 Model
- 不應與原參考真人高度相似到可被視為直接改造或複製

---

## SKU Strategy

使用者只需要貼商品 Landing Page URL。

系統目標自動完成：

```text
URL
→ 抓商品資訊
→ 抓全部可用商品圖片
→ 判斷正面 / 背面 / 細節 / 材質
→ 建 SKU 資料夾
→ 建商品 metadata
→ 送入生成流程
```

商品是不可任意重畫的核心資產。Logo、顏色、版型、領口、袖型、拼接、圖案等關鍵特徵若有明顯錯誤，不可直接通過 Review。

---

## Scene Strategy

Scene 與 Model、SKU 分離。

例：

- `daan-forest-park`
- `urban-running`
- `gym`
- `golf-course`
- `studio`

同一場景可以被不同 Model 與 SKU 重複使用。

---

## Review Gate

每張圖至少過三關：

### 1. Product Review
- 顏色
- Logo
- 版型
- 領口 / 袖口 / 褲型
- 拼接與商品細節
- 是否與 Landing Page 一致

### 2. Model Review
- 臉是否還是指定 Model
- 身形是否一致
- 髮型與主要身份特徵是否漂移
- 是否出現人體異常

### 3. Creative Review
- 場景是否正確
- 光影是否自然
- 構圖是否適合廣告
- 是否符合指定尺寸

結果只允許：

- `PASS`：可進 Final Gate
- `CHECK`：需要人工確認
- `FAIL`：淘汰或重新生成

任何重大商品錯誤應直接 `FAIL`，不得用整體美感分數補回來。

---

## Scale Principles

1. **Model、SKU、Scene 分離**，避免重複資料。
2. 所有資產使用固定 ID，不依賴人腦記名稱。
3. 原始資料永遠保留，生成資料不可覆蓋 source。
4. 每次生成都是一個 `job`，可追蹤輸入、輸出與 review。
5. 所有自動化都必須能被人工 Final Gate 擋下。
6. 新品牌只能新增 brand config，不應重寫整條 workflow。
7. 新 Model 只能新增 Model Card，不應修改 SKU 結構。
8. 新場景只能新增 Scene Card，不應修改 Model 或 SKU。

詳細規範見 `docs/SCALE-RULES.md`。

---

## MVP

第一階段不要一次做成巨獸。

MVP：

- 2 個固定 Model
- 1 個品牌
- 5 個 SKU
- 3 個 Scene
- 2 種尺寸：4:5、9:16
- URL 自動抓商品
- 自動生成
- 自動 Review
- 人工 Final Gate

成功定義：

> 使用者只需要指定 Model、Scene、Landing Page URL 與輸出尺寸，大部分流程能自動完成；人只負責最後確認。

---

## Example Request

```yaml
model: model-a
scene: daan-forest-park
brand: descente
landing_page_url: https://example.com/product
output:
  ratios:
    - 4:5
    - 9:16
```

預期結果：

> Model A 在大安森林公園，穿著 Landing Page 中正確商品，商品外觀與原頁面高度一致，並產出可供 Meta 廣告 Review 的 4:5 與 9:16 素材。

---

## Current Status

目前完成：

- 問題定義
- 系統邏輯
- 資料夾架構
- Model / Brand / SKU / Scene 資產分離原則
- Review Gate 原則
- Scale 原則

尚未完成：

- Landing Page crawler
- 商品圖片分類
- Model 建檔實作
- 商品上身實作
- 場景合成實作
- Review 自動評分
- 批次生成與 Meta 串接

下一階段應從 **MVP vertical slice** 開始：先讓 1 Model + 1 SKU + 1 Scene 從 URL 一路跑到 Review。