# Evals

Evals 用來驗證系統輸出是否符合商用標準，而不是只判斷「好不好看」。

## Eval Layers

### 1. Product Fidelity
檢查：
- 顏色
- Logo
- 圖案
- 剪裁
- 版型
- 領口 / 袖口 / 褲型
- 關鍵商品細節

重大商品錯誤 = HARD FAIL。

### 2. Model Consistency
檢查：
- 臉部身份
- 身形比例
- 髮型 / 年齡感 / 品牌角色特徵
- 人體異常

### 3. Styling Relevance
檢查：
- 是否真的呈現 hero feature
- Model 是否對應目標族群
- Pose / Scene / 搭配是否合理
- 是否符合品牌與品類

### 4. Scene / Composition
檢查：
- Scene 是否符合 job spec
- 光影是否自然
- 構圖是否可用
- 商品是否被遮擋或失焦

### 5. Channel Compliance
依 Web / EDM / LINE / Ads 各自規格檢查尺寸、安全區、可讀性與版位需求。

## Result

只允許：
- PASS
- CHECK
- FAIL

## Hard-Fail Principle

Product Fidelity 的重大錯誤不可用總分平均掉。

例如：Logo 錯誤，即使構圖、人物、場景全部高分，仍然 FAIL。

## Learning Loop

每次真實 MVP / production 出現新的失敗類型，必須：
1. 記錄 failure case
2. 判斷屬於哪個 Skill
3. 更新 rule / schema / eval
4. 補 regression case

不要只在聊天中記得。
