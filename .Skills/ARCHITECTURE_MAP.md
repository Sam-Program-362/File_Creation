# V3 Target Architecture and Build Stages

This document distinguishes the full target tree from the current implementation state. A planned or scaffolded file is not automatically an operational skill.

## Target skill tree

```text
narrative-engine-v3/
├── SKILL.md
├── INDEX.md
├── IMPLEMENTATION_STATUS.md
├── ARCHITECTURE_MAP.md
├── core/
│   ├── command-router/SKILL.md
│   ├── workflow/SKILL.md
│   └── project-isolation/SKILL.md
├── shared-systems/
│   ├── adaptive-sections/SKILL.md
│   ├── bedrocks/SKILL.md
│   ├── information-transfer/SKILL.md
│   ├── evidence-and-inference/SKILL.md
│   └── tags/
│       ├── SKILL.md
│       ├── tag-index.md
│       └── built-in/*.md
├── analysis/                         [PHASE 6 — IMPLEMENTED]
│   ├── README.md
│   ├── analysis-sheet/SKILL.md
│   ├── concept-analysis/SKILL.md
│   ├── reference-analysis/
│   │   ├── SKILL.md
│   │   ├── image-analysis.md
│   │   ├── context-reconstruction.md
│   │   └── rp-log-analysis.md
│   ├── character-analysis/SKILL.md
│   └── world-analysis/SKILL.md
├── creation/                         [PHASES 7–11 — CREATION & HANDOFF]
│   ├── README.md
│   ├── character/SKILL.md
│   ├── world/SKILL.md
│   ├── context-sheet/SKILL.md
│   ├── scenario-starting-message/       [PHASE 9 — IMPLEMENTED]
│   │   ├── SKILL.md
│   │   ├── style-and-format.md
│   │   └── opening-design.md
│   ├── description/SKILL.md             [PHASE 10 — IMPLEMENTED]
│   └── lorebook-planning/                [PHASE 11 — IMPLEMENTED]
│       ├── SKILL.md
│       ├── decision-framework.md
│       ├── entry-brief-specification.md
│       ├── advanced-script-handoff.md
│       ├── content-pattern-selection.md
│       └── references/lorebook-creator/  [user-supplied source copies]
├── refinement/                       [PHASE 12 — IMPLEMENTED]
│   ├── README.md
│   ├── patch-refinement/
│   │   ├── SKILL.md
│   │   ├── patch-operations.md
│   │   └── artifact-dependency-map.md
│   └── expansion/
│       ├── SKILL.md
│       └── expansion-methods.md
└── quality/                          [PHASE 13 — IMPLEMENTED]
    ├── README.md
    ├── SKILL.md
    ├── coverage-validation/SKILL.md
    ├── consistency-validation/SKILL.md
    └── output-validation/SKILL.md
```

## Build stages

| Phase | Scope | Status |
|---|---|---|
| 1 | Root orchestrator, index, architecture map, implementation status | Implemented |
| 2 | Command router, workflow, project isolation | Implemented |
| 3 | Bedrocks | Implemented |
| 4 | Adaptive sections, information transfer, evidence/inference foundation | Implemented |
| 5 | Tag system and individual built-in tag definitions | Implemented |
| 6 | Analysis Sheet, concept, reference/image, context reconstruction, RP logs, character/world analysis | Implemented as Markdown AI operating procedures; model-behavior testing required |
| 7 | Character and World creation skills | Implemented as operational AI generation procedures; model testing required |
| 8 | Context Sheet generation skill | Implemented as an operational AI handoff-generation procedure; model testing required |
| 9 | Scenario starting-message skill, four-part notation, opening design and exact quantity handling | Implemented as operational AI generation procedures; model testing required |
| 10 | Human-facing Description skill | Implemented as an operational AI procedure; model-behavior testing required |
| 11 | Lorebook Planning handoff skill, normal-entry briefs, Advanced Script specifications, source-based platform decisions | Implemented as an operational AI planning procedure; model testing required |
| 12 | Patch refinement, dependency-aware propagation, and additive expansion | Implemented as operational AI procedures; model-behavior testing required |
| 13 | Output-specific quality assurance, coverage/consistency/output validators, and regression specifications | Implemented at the AI-instruction level; model testing pending |

Help command routing is available in Phase 2. Phase 13 adds the system-wide output validation layer without creating a second command system.

## Module design standard for full implementation

Every fully implemented subsystem should define:

1. Name and concise description.
2. Activation conditions and supported commands.
3. Purpose, scope, and explicit non-goals.
4. Required inputs.
5. Step-by-step operating method.
6. Decision rules, edge cases, priorities, and exclusions.
7. Output responsibilities and format.
8. Shared-system dependencies.
9. Correct and incorrect examples.
10. Completion checklist and validation tests.

Phase 6 contains detailed analysis procedures. Phase 7 contains operational Character and World generation procedures. Phase 8 contains the operational Context Sheet integration and handoff procedure. Phases 7 and 8 consume Phase 6 findings where available instead of reimplementing the analysis subsystem. Model-behavior testing remains pending.


## Phase 6 — operational analysis layer

Phase 6 consumes the shared foundation and produces an approved, inspectable Analysis Sheet. The coordinator calls only the specialist analysis procedures relevant to the project's inputs. The specialist modules return source-aware findings; the coordinator synthesizes them without forcing fixed headings.

Operational files:
- `analysis/analysis-sheet/SKILL.md`
- `analysis/concept-analysis/SKILL.md`
- `analysis/reference-analysis/SKILL.md`
- `analysis/reference-analysis/image-analysis.md`
- `analysis/reference-analysis/context-reconstruction.md`
- `analysis/reference-analysis/rp-log-analysis.md`
- `analysis/character-analysis/SKILL.md`
- `analysis/world-analysis/SKILL.md`

Phase 7 operational files: `creation/character/SKILL.md` and `creation/world/SKILL.md`. Both contain complete AI generation procedures; model-behavior validation remains pending.

## Phase 8 — operational Context Sheet handoff

Phase 8 creates the central, self-contained information handoff for the separate narrator/roleplayer AI. It consolidates project identity, premise, intention, narrative focus, character and relationship context, world rules, plot situation, narrative configuration, specialized mechanics, and all project-relevant confirmed Bedrocks. It is informational rather than conversational and does not contain analysis-only fields such as `Missing Elements` or `Planned Expansion`.

Operational file: `creation/context-sheet/SKILL.md`. Behavioral regression specifications: `tests/phase-8-context-sheet-regression-tests.md`. The tests are specifications only and have not yet been executed against a target model/runtime.


## Phase 9 — operational Scenario starting-message generation

Phase 9 generates only ready-to-use opening messages for a separate roleplay AI. It consumes the project's available approved context and produces one message by default or exactly the requested number. Multiple outputs are independent alternatives unless a connected multi-part opening is explicitly requested.

The operational system is divided into three files:
- `creation/scenario-starting-message/SKILL.md` — command activation, quantity parsing, project-source reconciliation, scene construction, Bedrock/tag enforcement, user-character agency, edge cases, and output validation.
- `creation/scenario-starting-message/style-and-format.md` — vivid grounded prose, character voice, 2–4 paragraph default, third-person narration, and the four required notation categories.
- `creation/scenario-starting-message/opening-design.md` — narrative-gravity-led opening selection, playable hooks, scene scale, variation, and failure patterns.

Phase 9 integrates the style/format rules supplied with V2: narration in single asterisks, dialogue in quotation marks, private thoughts in triple backticks, and OOC notes in `//` lines only when requested. It never writes the user's thoughts or invents the user's voluntary actions/dialogue/decisions. It stops after the requested opening(s).

Behavioral regression specifications are in `tests/phase-9-scenario-regression-tests.md`; they are not yet executed against a target model/runtime.


## Phase 10 — operational human-facing Description generation

Operational file: `creation/description/SKILL.md`.

Phase 10 creates a reader-facing Markdown description of the selected project subject. It resolves audience, purpose, subject, and disclosure scope; reconciles the latest approved project information; selects a presentation form suited to a whole project, world, plot, short public blurb, or comprehensive description; and validates that the result is factual, audience-appropriate, adaptive, and distinct from all AI-facing handoffs. It applies relevant Information Transfer, Adaptive Sections, Evidence and Inference, Bedrocks, Tags, and project isolation rules. It does not generate another project asset or AI instruction prompt.

Behavioral regression specifications: `tests/phase-10-description-regression-tests.md` (32 cases; not executed against a target model/runtime).


## Phase 11 — operational Lorebook Planning layer

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.** Phase 11 prepares a project-specific implementation handoff for a separate Lorebook Creator. It does not create import-ready JSON or JavaScript.

Operational files:
- `creation/lorebook-planning/SKILL.md` — full planning sequence and Markdown handoff contract.
- `creation/lorebook-planning/decision-framework.md` — main-document / Lorebook / Advanced Script / no-module classification, platform fit, activation, grouping, triggers, and priority.
- `creation/lorebook-planning/entry-brief-specification.md` — entry-by-entry planning requirements with source-schema awareness.
- `creation/lorebook-planning/advanced-script-handoff.md` — behavior-only Advanced Script brief including detection, injection, cleanup, safeguards, and tests.
- `creation/lorebook-planning/content-pattern-selection.md` — selective use of the source-defined content patterns.
- `creation/lorebook-planning/references/lorebook-creator/` — directly readable copies of the provided skill and references, plus the original archive retained under `references/lorebook-creator-skill.zip`.

The planner is required to decide whether a Lorebook is needed, avoid duplicating the central Context Sheet, separate constant from keyword-triggered entries, and distinguish normal JSON entries from stateful / conditional Advanced Script behavior. Normal Lorebook JSON is source-described for JanitorAI and SillyTavern-style World Info; Advanced JavaScript is source-described for JanitorAI. Other or unknown platform semantics require validation.

The supplied source describes priority bands in two slightly different granularities. V3 uses the bands adopted in the Notion plan as default labels and requires the handoff to explain priority rationale and validate target-platform semantics rather than claiming universal values.

Regression specifications: `tests/phase-11-lorebook-planning-regression-tests.md` (70 cases; specifications only, not model-executed).


## Phase 12 — operational Refinement and Expansion

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.** Phase 12 contains two separate operations, not one generic rewrite system.

Operational files:
- `refinement/patch-refinement/SKILL.md` — target/source resolution, scope classification, patch planning, minimal edits, dependency synchronization, Bedrock/tag safeguards, output contract, and preservation validation.
- `refinement/patch-refinement/patch-operations.md` — ADD, REPLACE, REMOVE, REPHRASE, MOVE, RETITLE, SPLIT, MERGE, and SCOPE ADJUSTMENT semantics; exact preservation and output modes.
- `refinement/patch-refinement/artifact-dependency-map.md` — source/derived artifact relationships and conditions for propagation.
- `refinement/expansion/SKILL.md` — additive development, target/scope resolution, evidence boundaries, canon status, section placement, dependency handling, and expansion validation.
- `refinement/expansion/expansion-methods.md` — depth, behavioral, contextual, connective, structural, breadth, operational, narrative, and presentation expansion methods.

The patch system carries forward V2's strict content preservation and targeted-edit rules. It distinguishes artifact-local presentation changes, canonical project-fact changes, and deliberate Bedrock revisions. The expansion system preserves existing layers and does not silently convert optional ideas into canon. Both systems require the exact current artifact and do not claim long-term memory.

Regression specifications: `tests/phase-12-refinement-expansion-regression-tests.md` (70 cases; not executed against a target model/runtime).


## Phase 13 — operational Quality Assurance layer

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.** Phase 13 is the finalization gate for every generated or modified project artifact. It applies the Notion plan's checks for concept fidelity, Bedrock integrity, coverage, adaptive structure, output identity, style/tags, and refinement preservation.

Operational files:
- `quality/SKILL.md` — activation, validation sequence, severity classification, safe repair, revalidation, and reporting rules.
- `quality/coverage-validation/SKILL.md` — approved Analysis Sheet transfer, destination mapping, Context Sheet completeness, and artifact-specific coverage.
- `quality/consistency-validation/SKILL.md` — Bedrocks, canon, chronology, character/world rules, relationships, tag scope, and cross-artifact consistency.
- `quality/output-validation/SKILL.md` — specific contracts for Analysis, Character, World, Context, Scenario, Description, Lorebook Plan, Refinement, and Expansion.
- `tests/phase-13-quality-assurance-regression-tests.md` — 66 behavioral test specifications.
- `tests/VALIDATION_RUN_TEMPLATE.md` — manual/target-model test recording template.

Output Validation is required for every artifact. Coverage and Consistency are selected based on source and project complexity. QA is internal by default and does not append a verbose checklist. It never claims that a target model passed tests that have not actually been run.
