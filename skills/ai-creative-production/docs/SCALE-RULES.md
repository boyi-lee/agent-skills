# Scale Rules

## 1. Asset separation

Model、Brand/SKU、Scene 必須分開管理。

原因：同一個 Model 要能穿很多 SKU，同一個 SKU 要能套不同 Model，同一個 Scene 要能被不同組合重複使用。

## 2. Stable IDs

建議格式：

- Model: `model-a`, `model-b`
- Brand: `descente`, `ash-golf`
- SKU: 使用品牌官方 SKU；若無則建立可追蹤 ID
- Scene: `daan-forest-park`, `urban-running`
- Job: `YYYYMMDD-HHMM-<brand>-<sku>-<model>-<scene>`

ID 建立後不可因顯示名稱改動而更名。

## 3. Source is immutable

`raw/` 與原始 Landing Page 資料只增不覆蓋。

清理後的素材放 `clean/`，生成圖放 `outputs/`。

## 4. One job = one traceable run

每次生成都要有獨立 job，並保存：

- 使用哪個 Model 版本
- 使用哪個 SKU 版本
- 使用哪個 Scene 版本
- 生成參數
- 輸出檔名
- Review 結果
- Final Gate 結果

## 5. Brand onboarding

新增品牌時，只能新增：

- brand profile
- SKU data
- 必要的 brand-specific parser/config

不要複製整套 workflow。

## 6. Model onboarding

新增 Model 時，只新增 Model Card、references、base images 與版本資訊。

不要為每個 Model 複製一套 SKU 或 workflow。

## 7. Scene onboarding

新增 Scene 時，只新增 Scene Card 與 references。

不要把場景資訊硬寫進生成程式。

## 8. Review is a gate

自動 Review 是篩選器，不是最終真理。

重大商品錯誤：直接 FAIL。

模糊案例：CHECK。

只有人工 Final Gate 後才可 production-ready。

## 9. Versioning

任何會影響輸出的項目都應版本化：

- model profile
- scene profile
- workflow
- review rubric
- product metadata

## 10. Scale target

架構必須能從：

`2 Models × 5 SKUs × 3 Scenes`

擴充到：

`N Models × N Brands × N SKUs × N Scenes`

而不需要重寫核心流程。