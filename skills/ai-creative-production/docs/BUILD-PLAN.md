# AI Creative Production System — Build Plan

## Goal

建立一個可擴張、可驗證、可交接的 AI 服飾素材生產系統，讓同一個 SKU 能被安全地轉換成官網、EDM、LINE OA / LINE Ads、Meta Ads 與 Google Ads 所需素材。

核心原則：

1. 商品真實性優先於生成自由度。
2. SKU、Model、Scene 都是共用資產，不屬於任何單一渠道。
3. Channel Skill 只能改變構圖、比例、版位、文字與用途，不得重新定義商品本身。
4. 所有自動化都必須可追蹤、可 Review、可被人工 Final Gate 擋下。
5. Source 一份，Output 多份。

---

## 6-Step Build Plan

### Step 1 — Repository Foundation
建立主 README、共用目錄、8 個 Skill 模組、Workflow、Evals、MVP 入口與 Handoff 規則。

完成條件：任何新聊天或 Codex 只讀 README + SKILL 文件，就知道系統目的、邊界與下一步。

### Step 2 — Core Asset Contracts
建立並固定：

- Brand Profile
- Model Card
- SKU Product Asset
- Scene Card
- Styling / Creative Brief
- Job Manifest

完成條件：每個資產都有唯一 ID、固定欄位與來源追蹤。

### Step 3 — Skill Contracts
建立 8 個獨立 Skill：

1. product-understanding
2. styling-planner
3. image-generator
4. quality-review
5. channel-web
6. channel-edm
7. channel-line
8. channel-ads

每個 Skill 都要有：Purpose、Input、Output、不可做的事、Validation、Stop Rule。

### Step 4 — Workflow Orchestration
把 Skills 串成標準工作流：

Landing Page URL
→ Product Understanding
→ Styling Planner
→ Image Generator
→ Quality Review
→ Channel Skill
→ Channel Review
→ Final Gate

完成條件：每一步都能獨立替換，不需要修改其他 Skill。

### Step 5 — Eval / Review System
建立自動與人工驗證規則：

- Product Fidelity
- Model Consistency
- Styling Relevance
- Scene / Composition Quality
- Channel Compliance

商品重大錯誤直接 FAIL，不得由其他分數抵銷。

### Step 6 — Real MVP Test
用一個真實品牌、真實 SKU、已建立 Model、任意 Scene 走完整流程。

第一個 MVP 只驗證：

- Landing Page 資料能正確抽取
- SKU 能建立完整 Product Asset
- AI 能產出合理 Styling Plan
- Model + SKU + Scene 能形成可執行 Job
- Review Gate 能指出錯誤
- 至少一個 Channel Skill 能產出正式規格

---

## MVP Success Definition

使用者只需提供：

- Brand
- Model
- Landing Page URL / SKU
- Scene（可選，亦可由 Styling Planner 建議）
- Output Channel

系統可以產出一個完整、可 Review、可追蹤的工作包。

第一版不要求完全無人操作。成功標準是大部分機械性工作自動完成，且人只處理高價值決策與 Final Gate。

---

## Non-Negotiable Rules

- Channel Skills 不可修改 Product Identity。
- 不得用生成圖反向覆蓋原始商品資料。
- 不得因為素材漂亮而忽略 SKU 細節錯誤。
- 不得讓不同 Channel 各自保存一份互相衝突的 SKU Source。
- 未通過 Quality Review 的素材不可進 Channel Production。
- 真實案例產生的新規則，需回寫到 schema / skill / eval，而不是只留在聊天紀錄。
