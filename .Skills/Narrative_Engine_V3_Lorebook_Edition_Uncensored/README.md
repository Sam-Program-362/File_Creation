# Narrative Engine V3 — Lorebook Edition (Uncensored Hardened)

**Version:** 1.1.1-uncensored  
**Target:** JanitorAI + SillyTavern-style World Info  
**Posture:** Fully uncensored. No content sanitization, no moral filtering of sexual, violent, dark, taboo, or extreme material when it is part of the concept.

This is the same Narrative Engine V3 system (Phases 1–13) packaged as modular lorebook JSON entries instead of a Markdown skill tree.

## Discensorship changes (this edition)
- Added always-on **Core — No Content Censorship** constant entry.
- Rewrote **Tag — Uncensored** for full adult/extreme content fidelity; removed “higher-priority platform or safety constraints” deference.
- Updated Command Router conflict handling: content is never filtered for being sexual/violent/dark/taboo.
- Strengthened Uncensored handling across Character, Context Sheet, Scenario, Description, Analysis, Lorebook Planning, and QA modules.
- Removed “platform and policy limits” language from Lorebook Planning.

Functional systems (routing, Bedrocks, adaptive sections, QA, etc.) are preserved.

---

# Narrative Engine V3 — Lorebook Edition (Separate Alternative)

This ZIP contains a separate Lorebook implementation of the Narrative Engine V3 system. It does **not** modify, replace, or overwrite the existing V3 Skill Tree. The Skill Tree remains the primary implementation; this package is an alternative deployment approach as requested.

## Files

- `00_CORE_SYSTEM_CONSTANT.json` — the always-active core system. All entries in this file use `constant: true`.
- `01_COMMANDS_AND_SESSION_CONTROL.json` — command parsing, project workflow, Help, and in-session project isolation.
- `02_ANALYSIS_SYSTEMS.json` — Analysis Sheet, concept analysis, reference routing, context reconstruction, RP log, character, and world analysis.
- `03_CAPTION_BASED_REFERENCE_INTERPRETATION.json` — dedicated caption-only reference interpreter. This replaces direct image-vision analysis.
- `04_TAG_SYSTEM.json` — readable tag registry and individual built-in tag entries.
- `05_CHARACTER_AND_WORLD_CREATION.json` — character and world generation procedures.
- `06_CONTEXT_SHEET.json` — narrator-facing Context Sheet generation.
- `07_SCENARIO_STARTING_MESSAGES.json` — opening-message generation, opening design, style and four-part format.
- `08_DESCRIPTION_GENERATION.json` — human-facing Markdown descriptions.
- `09_LOREBOOK_PLANNING.json` — detailed Lorebook Planning handoff system plus source-derived technical reference.
- `10_REFINEMENT_AND_EXPANSION.json` — patch refinement and additive expansion.
- `11_QUALITY_ASSURANCE.json` — coverage, consistency, and output validators.
- `ALL_LOREBOOKS_COMBINED.json` — all entries in one JSON array for platforms that prefer one import file. This duplicates the separate files; do not import both the individual files and the combined file together.

## Recommended import

1. Import `00_CORE_SYSTEM_CONSTANT.json` and keep it enabled as the constant / always-active core Lorebook.
2. Import the section Lorebooks that the target platform supports. Keep their entries enabled; they use keyword activation (`constant: false`).
3. If the platform supports only a single Lorebook import, use `ALL_LOREBOOKS_COMBINED.json` instead of importing the separate section files.
4. Do not import both the combined file and the individual files, or entries will be duplicated.
5. Check how the target platform handles `priority`, `insertion_order`, `matchWholeWords`, and constant entries. The supplied Lorebook Creator schema is source guidance, not a guarantee of identical behavior across every runtime.

## Activation design

The core system entries are always active. Section-level entries activate on command phrases or project terms, such as `Create Sheet`, `Create Character`, `Create World`, `Create Context Sheet`, `Create Scenario`, `Create Description`, `Plan Lorebooks`, `Refine`, `Expand`, and `Review`.

Some specialist entries intentionally share command triggers. For example, `Create Sheet` may activate the Analysis Sheet coordinator plus concept, character, and world analysis entries. Each specialist procedure must still run only if its subject is relevant to the current project.

Tags use `constant: false` with their human-readable names and legacy V2 aliases as activation keys. Uncensored may also activate from strong descriptive signals such as sharp-tongued, bratty, vulgar, or profane speech; it must remain scoped to the character/project detail that supports it.

## Caption-only reference mode

This edition assumes the downstream AI does not have image vision. It must work from user-supplied captions or text descriptions only. The user's written concept and direct instructions always outrank caption text. Captions are noisy candidate evidence: accept only details that match the concept and reference purpose; discard irrelevant, contradictory, or illogical details.

Example: if the user describes a blonde woman and a caption says “a woman with blonde hair looking up at the sky, wearing a white silky dress, hands behind her back,” the system may accept “woman” and “blonde hair”; it may record the white dress as the outfit represented by the caption if clothing is in scope; it must not convert “looking up” or “hands behind her back” into permanent traits unless the user wants a scenario reference. It must not claim that it visually verified any of this.

## JSON format

Every individual file is a JSON array of Lorebook entry objects using the full field list from the supplied `lorebook-creator-skill` reference: `activationMode`, `activationScript`, `case_sensitive`, `category`, `comment`, `constant`, `content`, `enabled`, `extensions`, `groupWeight`, `id`, `inclusionGroupRaw`, `insertion_order`, `key`, `keyMatchPriority`, `keysecondary`, `keysecondaryRaw`, `keysRaw`, `matchWholeWords`, `minMessages`, `name`, `prioritizeInclusion`, `priority`, `probability`, `selectiveLogic`, `tags`, and `keywordsRaw`.

## Important boundary

This package provides Lorebook instructions as a separate deployment approach. It does not change the primary V3 Skill Tree. The `Lorebook Planning` subsystem inside V3 remains a planning handoff and does not become a Lorebook JSON generator merely because this alternative package is made of Lorebook JSON.
