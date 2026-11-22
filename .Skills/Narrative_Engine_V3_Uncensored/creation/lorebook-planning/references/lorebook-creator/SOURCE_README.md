# Lorebook Creator — Source Reference Copies

These files are extracted copies of the user-provided `lorebook-creator-skill.zip`. They are reference material for Narrative Engine V3 Phase 11. They are not V3 planner instructions and are not to be edited as if they were the V3 implementation.

## Source files

- `SKILL.md` — original Lorebook & Script Creator skill, including its purpose, normal Lorebook / Advanced Script distinction, decision logic, entry JSON schema illustration, content standards, workflow, and content philosophy.
- `assets/full-system-overview.md` — concise supported-type and automatic-selection overview.
- `references/entry-schema.md` — field-by-field normal Lorebook entry schema and recommended priority/constant guidance.
- `references/content-patterns.md` — reusable content patterns, including anti-default rules, personality filters, non-escalation, time continuity, dominance preservation, progression, and personality-matched aftercare.
- `references/advanced-script-patterns.md` — JanitorAI Advanced Script patterns and detection/injection/cleanup guidance.
- `assets/example-core-entry.json` — original illustrative JSON entry example.
- `assets/example-advanced-onomatopoeia.js` — original illustrative Advanced Script example.

## Provenance and interpretation

The original archive is also retained at the package-root path `references/lorebook-creator-skill.zip`. These extracted files are copied from that user-supplied archive. The planner must preserve the source's stated platform scope: normal Lorebook JSON is described for JanitorAI and SillyTavern-style World Info; Advanced JavaScript is described for JanitorAI. Do not assume that all fields or script APIs have identical support across platform versions.

The original `SKILL.md` and `entry-schema.md` express priority bands at slightly different levels of granularity. Phase 11 records this discrepancy and requires a stated rationale and platform validation rather than pretending there is one universal priority taxonomy.
