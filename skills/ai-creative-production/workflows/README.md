# Workflows

核心自動化模組：

```text
ingest-product/   # 從 Landing Page 建立商品資產
dress-product/    # 將 SKU 套到指定 Model
compose-scene/    # 將人物與指定 Scene 組合
review/           # 商品、Model、畫面三層檢查
```

每個 workflow 都應：

- 有固定輸入 / 輸出
- 可單獨測試
- 可重跑
- 不直接覆蓋 source assets
- 失敗時留下可追蹤狀態