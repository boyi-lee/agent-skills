# Core Assets

Core Assets 是所有 Channel 共用的單一真實來源（Single Source of Truth）。

## Canonical Assets

- `models/`：品牌固定 Model 與 Model Card
- `brands/`：Brand Profile 與品牌規則
- `skus/`：SKU 商品來源、商品圖、商品 metadata、不可變商品特徵
- `scenes/`：可替換 Scene Card / reference

目前舊版 repo 中既有 `models/`、`brands/`、`scenes/` 仍視為 canonical source；後續搬移時不得複製出第二份互相衝突的資料。

## Rule

Source 一份，Output 多份。

Web、EDM、LINE、Ads Skill 都只能讀取 Core Assets，不得各自維護 SKU、Model 或 Brand 的另一份真實版本。
