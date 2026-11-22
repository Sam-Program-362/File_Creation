# Lorebook Entry Schema Reference

## Complete Field List

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| activationMode | string | yes | Always `"standard"` unless using advanced scripting |
| activationScript | string | yes | Usually `""` |
| case_sensitive | boolean | yes | Almost always `false` |
| category | string | yes | Short label for organization |
| comment | string | yes | Human-readable description of purpose |
| constant | boolean | yes | `true` = always active, `false` = keyword triggered |
| content | string | yes | The actual injected instructions |
| enabled | boolean | yes | Usually `true` |
| extensions | object | yes | Usually `{}` |
| groupWeight | number | yes | Usually `100` |
| id | number/string | yes | Unique within the file |
| inclusionGroupRaw | string | yes | Usually `""` |
| insertion_order | number | yes | Lower = earlier insertion |
| key | array of strings | yes | Trigger keywords (empty if constant) |
| keyMatchPriority | boolean | yes | Usually `false` |
| keysecondary | array | yes | Secondary keys (often empty) |
| keysecondaryRaw | string | yes | Comma-separated secondary keys |
| keysRaw | string | yes | Comma-separated primary keys |
| matchWholeWords | boolean | yes | Usually `true` |
| minMessages | number | yes | Usually `0` |
| name | string | yes | Display name |
| prioritizeInclusion | boolean | yes | Prefer `true` for important entries |
| priority | number | yes | Higher = more important (0–101 typical) |
| probability | number | yes | Usually `100` |
| selectiveLogic | number | yes | Usually `0` |
| tags | array of strings | yes | For organization |
| keywordsRaw | string | yes | Same as keysRaw in most cases |

## Priority Bands (Recommended)

- 101–95 : Absolute locks (User Definitions, Dominance Correction, Time Continuity, Pretense)
- 94–90 : Core narrative & personality protection
- 89–80 : Strong supporting systems (aftercare, body language, long-term relationship)
- 79–65 : Act and dynamic entries
- Below 65 : Niche or low-frequency triggers

## Constant vs Triggered

**Use `constant: true` when:**
- The rule must never be forgotten (fidelity, anti-soft, time of day, power assumptions)
- There are no reliable keywords that would activate it

**Use `constant: false` + keywords when:**
- The instruction only matters during specific acts or situations
- You want to save context tokens until the topic appears

## Content Length Guidance

- Core locks: 150–400 words of dense rules
- Personality overlays: 120–300 words
- Act guides: 150–350 words (include physical + personality + progression)
- Niche acts: 100–250 words
