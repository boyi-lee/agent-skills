# Brands

品牌與 SKU 資產庫。

每個品牌建議結構：

```text
<brand-id>/
├── brand-profile/
└── skus/
    └── <sku>/
        ├── raw/
        ├── clean/
        ├── metadata/
        └── landing-page/
```

每個 SKU 必須保留來源 Landing Page 與原始商品圖。