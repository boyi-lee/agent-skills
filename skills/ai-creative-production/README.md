# AI Creative Production Skill

## Purpose

建立一套可 scale、可驗證、可交接的 AI 廣告素材生產系統。

核心使用情境：

> 指定 `Model` + 指定任意 `Scene` + 貼上商品 Landing Page URL → 系統自動抓取商品資料與圖片 → 將正確商品套用到固定品牌 Model → 生成廣告圖 → 自動 Review → 人工 Final Gate。

這個專案的重點不是「讓 AI 畫一件很像的衣服」，而是把 **Model、商品 SKU、Scene** 都當成可重複使用、可自由替換的資產，再由工作流組合。

---

## Core Objects

系統只有三個主要資產：

1. **Model**：固定品牌虛擬模特兒，保存樣貌、身形、髮型、氣質、基準圖與一致性規則。
2. **Brand / SKU**：品牌底下的商品資料，每個 SKU 保存 Landing Page、商品圖、細節圖與不可被改動的商品特徵。
3. **Scene**：獨立、可替換的場景輸入。可以是真實地點、室內空間、棚拍、城市街道、自然環境，或由文字 / 參考圖定義的任何背景。

最終工作只是：

`Model + SKU + Scene + Output Spec → Generate → Review → Final`

---

## Target Workflow

```text
1. 選 Model
2. 指定 Scene（可為任何背景 / 地點 / 場景設定）
3. 貼 Landing Page URL
4. 自動抓商品名稱 / SKU / 商品圖 / 細節圖
5. 自動建立 SKU 資料
6. 套用商品到固定 Model
7. 依指定 Scene 與尺寸生成
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
├── models/                 # 固定品牌 Model 資產
│   └── <model-id>/
│       ├── card/
│       ├── references/
│       ├── base-images/
│       └── profile.yaml
├── brands/                 # 品牌與 SKU 資產
│   └── <brand-id>/
│       ├── brand-profile/
│       └── skus/
│           └── <sku>/
│               ├── raw/
│               ├── clean/
│               ├── metadata/
│               └── landing-page/
├── scenes/                 # 可替換 Scene 資產
│   └── <scene-id>/
│       ├── references/
│       └── scene.yaml
├── workflows/
├── jobs/
├── outputs/
├── reviews/
├── schemas/
├── templates/
└── docs/
```

---

## Model Strategy

Model 不屬於任何單一 SKU。

每個 Model 是獨立品牌資產，可以重複穿數十或數百個 SKU。

可用真人 / Instagram 作為方向參考，但 production 角色必須重新建立成品牌自己的虛擬 Model。

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

Scene 與 Model、SKU 完全分離，且 **不設固定預設場景**。

Scene 可以來自：

- 文字描述
- 真實地點名稱
- 使用者提供的參考圖片
- 已核准的品牌場景模板
- 既有 Scene Card

例如今天可以是公園，下一次可以是健身房、球場、街道、辦公室、棚拍或任何其他背景。

Scene 的責任只描述：

- 背景 / 地點
- 時間
- 光線
- 天氣（如適用）
- 畫面氣氛
- 構圖限制
- 必須保留 / 不可出現的場景特徵

新增或替換 Scene 不應修改 Model、SKU 或核心工作流。

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

### 3. Creative / Scene Review
- 是否符合本次指定 Scene
- 光影是否自然
- 構圖是否適合廣告
- 是否符合指定尺寸

結果只允許：`PASS` / `CHECK` / `FAIL`。

任何重大商品錯誤應直接 `FAIL`。

---

## Scale Principles

1. **Model、SKU、Scene 分離**，避免重複資料。
2. 所有資產使用固定 ID。
3. 原始資料永遠保留，生成資料不可覆蓋 source。
4. 每次生成都是一個 `job`。
5. 所有自動化都必須能被人工 Final Gate 擋下。
6. 新品牌只能新增 brand config，不應重寫 workflow。
7. 新 Model 只能新增 Model Card。
8. 新 Scene 只能新增 / 指定 Scene Card，不應修改 Model 或 SKU。
9. 任何範例 Scene 都只是 example，不得被實作成系統預設值。

詳細規範見 `docs/SCALE-RULES.md`。

---

## MVP

- 2 個固定 Model
- 1 個品牌
- 5 個 SKU
- 至少 3 個可替換 Scene 測試
- 2 種尺寸：4:5、9:16
- URL 自動抓商品
- 自動生成
- 自動 Review
- 人工 Final Gate

成功定義：

> 使用者只需要指定 Model、任意 Scene、Landing Page URL 與輸出尺寸，大部分流程能自動完成；人只負責最後確認。

---

## Generic Example Request

```yaml
model: model-a
scene: <any-scene-id-or-scene-spec>
brand: <brand-id>
landing_page_url: https://example.com/product
output:
  ratios:
    - 4:5
    - 9:16
```

預期結果：

> 指定 Model 穿著 Landing Page 中正確商品，出現在本次指定 Scene 中，商品外觀與原頁面高度一致，並產出可供 Meta 廣告 Review 的素材。

---

## Current Status

已完成：問題定義、系統邏輯、資料夾架構、Model / Brand / SKU / Scene 分離原則、Review Gate、Scale 原則、Gate 1 ingestion 骨架。

下一階段：先讓 `1 Model + 1 SKU + 1 任意 Scene` 從 URL 一路跑到 Review，再擴張。
