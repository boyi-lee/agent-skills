# Handoff Guide

## Why this file exists

這個專案會跨 ChatGPT、Codex、其他聊天視窗與不同 AI Agent 持續開發。

任何接手者在開始修改前，必須先讀：

1. `README.md`
2. `SKILL.md`
3. `docs/SCALE-RULES.md`
4. `docs/HANDOFF.md`

不要只看最新對話就重設架構。

---

## Product Goal

最終使用者操作應接近：

```text
指定 Model A
+ 指定 Scene: 大安森林公園
+ 貼商品 Landing Page URL
+ 指定 4:5 / 9:16
→ 自動取得商品圖與商品資訊
→ 建立 / 更新 SKU 資產
→ Model A 穿上正確商品
→ 放入指定場景
→ 生成候選圖
→ 自動 Review
→ 人工 Final Gate
```

## Architecture Decisions Already Made

以下決策視為目前 canonical，不應無理由推翻：

- Model、SKU、Scene 是三個獨立資產庫。
- Model 不放在 SKU 底下。
- SKU 必須隸屬 Brand。
- Scene 可跨品牌、Model、SKU 重複使用。
- 每次生成必須建立 job。
- 原始 Landing Page 與商品圖不可被生成流程覆蓋。
- Review 結果只允許 PASS / CHECK / FAIL。
- 自動 Review 後仍保留人工 Final Gate。
- 商品身份正確性優先於畫面創意。

## Model Direction

Model 的長期目的，是建立少量、固定、可重複使用的品牌虛擬 Model。

真人或 Instagram 可以作為視覺方向參考，但最終品牌 Model 應形成獨立角色，不應只是把真人臉稍微改掉後持續商用。

Model Card 至少描述：

- appearance
- body shape / proportion
- hair
- age impression
- styling direction
- personality / visual mood
- reference assets
- approved base images
- consistency constraints

## SKU Direction

使用者輸入 Landing Page URL 後，系統應盡量自動取得：

- brand
- product name
- SKU
- product images
- front / back / side / detail / material classification
- color
- immutable product features
- source URLs

如果資料不足，不可猜測不存在的商品細節。

## Review Direction

Review 分三層：

1. Product fidelity
2. Model consistency
3. Creative quality

重大商品錯誤，例如錯 Logo、錯顏色、錯版型、錯圖案，應直接 FAIL。

## MVP Scope

第一個完整測試只做：

`1 Model + 1 Brand + 1 SKU + 1 Scene + 1 ratio`

確認端到端可跑，再擴充到：

`2 Models + 5 SKUs + 3 Scenes + 4:5 / 9:16`

## Next Recommended Build Task

下一個 Agent 應優先做：

### Gate 1: Asset schemas + ingestion skeleton

完成條件：

- Model profile schema 可讀
- Scene schema 可讀
- Job schema 可讀
- 可輸入一個 Landing Page URL
- 能建立 brand / SKU 資料夾
- 能保存抓到的原始圖片與 source URL
- 暫時不需要先解決最終 AI 穿衣品質

先把資料流跑通，再測圖像模型。不要反過來先堆一坨難以維護的生成節點。