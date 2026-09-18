---
name: news-editor
description: Edit Traditional Chinese (Taiwan) news copy while preserving facts, improving headline/lead structure, attribution, clarity, readability, and publication readiness. Supports optional author-style modules for lifestyle news.
---

# News Editor

## Use this skill when

- 潤稿、修稿、改寫新聞稿或新聞文章
- 優化標題、導言、段落順序
- 檢查新聞語氣、歸因、數字、日期、人名與品牌名稱
- 將公關稿整理為可發布的新聞稿
- 依指定新聞作者的可觀察風格進行編修

## Do not use this skill to

- 補寫來源未提供的事實
- 生成不存在的引述、數據、價格、日期、獎項或排名
- 將推測改寫成確定事實
- 模仿作者的獨特句子或大量重製既有文章

## Required references

Read:
1. `references/fact-preservation.md`
2. `references/editorial-principles.md`
3. `references/taiwan-news-style.md`

Load as needed:
- `headline-style.md`
- `lead-style.md`
- `attribution.md`
- `numbers-dates-names.md`
- `author-wu-wenyuan-style.md`

## Workflow

### 1. Fact Lock
Extract immutable facts before editing:
- who / what / when / where
- numbers / prices / dates
- quotes and quote owners
- product, venue, company, organization names
- source attribution
- uncertainty or conditional wording

### 2. Diagnose
Identify:
- headline weakness
- buried lead
- repeated information
- PR language
- unsupported evaluative language
- attribution gaps
- chronology problems
- unclear referents
- formatting inconsistencies

### 3. Edit
Choose the least invasive level:
- copy edit
- structural rewrite
- headline + lead rewrite
- full rewrite

### 4. Verify
Compare edited copy against Fact Lock. Any new factual claim is a failure unless explicitly supplied by the user.

### 5. Output
Default output:
1. 修訂後版本
2. 主要修改點
3. 需人工確認項目

For clean-copy requests, return only the publishable version.

## Author-style routing

If the user asks for 吳文元 / Up Media lifestyle style:
- load `references/author-wu-wenyuan-style.md`
- keep factual rules higher priority than stylistic similarity
- imitate structural tendencies, not signature wording
