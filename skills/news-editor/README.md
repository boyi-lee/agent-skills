# News Editor Skill

A Traditional Chinese (Taiwan) newsroom editing skill for copy editing, rewriting, headline/lead refinement, attribution checks, and fact-preserving final review.

## Design goals

1. Preserve facts before improving prose.
2. Separate hard newsroom rules from optional author/style modules.
3. Make edits explainable through before/after diffs.
4. Avoid adding unsupported facts, causal claims, quotes, prices, dates, rankings, or superlatives.
5. Support repeatable editorial workflows instead of one-off prompting.

## Structure

- `SKILL.md` — skill entry point and routing
- `references/` — newsroom rules and style references
- `workflows/` — copy-edit, rewrite, and final-review flows
- `rules/vale/` — deterministic lint rules to be added incrementally
- `tests/` — regression and before/after fixtures

## Style modules

The core newsroom rules are style-neutral. Author-specific observations belong in separate reference files.

Current author module:
- `references/author-wu-wenyuan-style.md`

The author module is derived from public Up Media articles and should be treated as a pattern library, not a license to copy distinctive wording.
