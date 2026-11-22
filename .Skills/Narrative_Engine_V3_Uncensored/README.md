# Narrative Engine V3 — Modular Skill Tree

**Package version:** 1.1.1  
**Operational AI-skill procedures:** Phases 1–13  
**Model/runtime testing:** pending for all regression specifications  
**Purpose:** A modular narrative concept and roleplay-project creation system that prepares project assets and handoffs for a separate roleplay AI. It does not act as that roleplayer.

## Start here

1. Read `SKILL.md` — root orchestrator.
2. Read `INDEX.md` — command and subsystem routing.
3. Read `IMPLEMENTATION_STATUS.md` — implementation and testing status.
4. Read `ARCHITECTURE_MAP.md` — target architecture and phase map.
5. Load the relevant subsystem skill and only its named dependencies.

Keep the folder structure intact. Do not flatten this package into one large prompt. The root skill routes; detailed procedures live in modular files and should be loaded progressively.

## Implemented systems

- **Phases 1–5:** root identity/orchestration; command routing, workflow, project isolation; Bedrocks; adaptive sections, information transfer, evidence/inference; tag registry and individual tag definitions.
- **Phase 6 — Analysis:** Analysis Sheet, concept analysis, image/reference analysis, context reconstruction, RP-log analysis, character analysis, and world analysis.
- **Phase 7 — Character & World Creation:** finished Character Sheets and World Sheets using adaptive sections and shared constraints.
- **Phase 8 — Context Sheet:** comprehensive, self-contained narrator-facing project handoff.
- **Phase 9 — Scenario:** requested quantity of opening messages only, with the four-part notation format and user-agency safeguards.
- **Phase 10 — Description:** human-facing Markdown descriptions, distinct from AI-facing handoffs.
- **Phase 11 — Lorebook Planning:** implementation handoff for another Lorebook Creator; no actual JSON or JavaScript is produced.
- **Phase 12 — Refinement & Expansion:** targeted patch edits and controlled additive development across supported artifacts.
- **Phase 13 — Quality Assurance:** mandatory internal finalization with coverage, consistency, and output-specific validators.

## Phase 12 at a glance

- `refinement/patch-refinement/SKILL.md` — minimal targeted patching.
- `refinement/patch-refinement/patch-operations.md` — edit operation semantics and preservation.
- `refinement/patch-refinement/artifact-dependency-map.md` — selective synchronization of existing dependent artifacts.
- `refinement/expansion/SKILL.md` — additive expansion without replacing established layers.
- `refinement/expansion/expansion-methods.md` — expansion method selector and depth controls.

## Phase 13 at a glance

- `quality/SKILL.md` — QA orchestration, severity, safe repair, revalidation, and concise reporting.
- `quality/coverage-validation/SKILL.md` — approved information transfer and Context Sheet completeness.
- `quality/consistency-validation/SKILL.md` — Bedrocks, canon, chronology, relationships, world rules, and cross-artifact checks.
- `quality/output-validation/SKILL.md` — artifact-specific output contracts and tag behavior.
- `tests/phase-13-quality-assurance-regression-tests.md` — 66 regression specifications.
- `tests/VALIDATION_RUN_TEMPLATE.md` — records actual model/runtime test executions.

## AI procedures versus executable code

This is a Markdown Skill system for an LLM. Its operating procedures are instructions, decision rules, routing logic, output contracts, and checks. It does not include executable Python/JavaScript functions, APIs, plugins, or an automated runtime.

“Implemented” means the AI instructions have been written. It does not mean a target model has passed behavioral testing. Regression files are specifications until executed against a selected LLM/runtime. Phase 13 is implemented as AI instructions; its test suite has not yet been executed against a target model/runtime.

## Source references

- `references/System Prompt V2.txt` — original V2 prompt preserved as a legacy baseline.
- `references/lorebook-creator-skill.zip` — supplied Lorebook Creator reference package.
- `references/NOTION_PLAN_REFERENCE.md` — pointer to the V3 architecture plan.
- Notion architecture plan: https://app.notion.com/p/41f081bf3aaf814b449fb9a7e7b369f
