# Narrative Engine V3 — Skill Index

This file is the routing map. Read it before loading subsystem skills.

## Package status

- **Implemented:** Phases 1–5 (root orchestration, command routing/workflow/project isolation, Bedrocks, adaptive sections/information transfer/evidence discipline, and the tag registry with built-in definitions).
- **Implemented:** Phase 6 (Analysis subsystem: Analysis Sheet coordinator, Concept Analysis, Reference Analysis, Image Analysis, Context Reconstruction, RP Log Analysis, Character Analysis and World Analysis). These are operational AI-skill procedures, not executable software functions.
- **Implemented:** Phase 7 (Character and World creation: operational procedures for finished Character Sheets and World Sheets, including source reconciliation, adaptive section construction, Bedrock/tag enforcement, information transfer, and output validation).
- **Implemented:** Phase 8 (operational Context Sheet generation as the comprehensive, self-contained narrator-facing project handoff).
- **Implemented:** Phase 9 (operational Scenario starting-message generation, including the four-part notation format, opening construction, exact quantity handling, user-agency protection, and Bedrock/voice consistency).
- **Implemented:** Phase 10 (operational human-facing Description generation with audience/purpose resolution, source reconciliation, disclosure control, adaptive presentation, tag/Bedrock handling, and output validation).
- **Implemented:** Phase 11 (operational Lorebook Planning handoff generator, including destination/type decisions, constant/keyword activation design, entry-by-entry briefs, Advanced Script specifications, source references, and build/test handoff).
- **Implemented:** Phase 12 (patch refinement and additive expansion across supported project artifacts).
- **Implemented:** Phase 13 (system-wide output-specific quality assurance, coverage validation, consistency validation, and regression harness specifications).

A file can exist in the tree without being an implemented capability. Check both the route status and the target module's metadata.

## Route by user intent

| User intent or command | Load first | Shared dependencies | Status |
|---|---|---|---|
| Start a new concept / default workflow | `core/workflow/SKILL.md` | project isolation, analysis coordinator, shared foundations | Implemented |
| `Create Sheet` | `analysis/analysis-sheet/SKILL.md` | concept, relevant reference/character/world analysis, adaptive sections, information transfer, evidence, tags, Bedrocks | Implemented |
| Project type, concept core, narrative gravity, priorities | `analysis/concept-analysis/SKILL.md` | evidence, tags, Bedrocks | Implemented |
| Images or visual references | `analysis/reference-analysis/SKILL.md` → `image-analysis.md` | evidence, tags | Implemented |
| Fragmented or scattered notes | `analysis/reference-analysis/SKILL.md` → `context-reconstruction.md` | evidence, adaptive sections, project isolation | Implemented |
| RP logs or interaction transcripts | `analysis/reference-analysis/SKILL.md` → `rp-log-analysis.md` | evidence, adaptive sections, information transfer, project isolation | Implemented |
| Character psychology, behavior, or relationship signals | `analysis/character-analysis/SKILL.md` | evidence, tags, Bedrocks, relevant references | Implemented |
| World and setting analysis | `analysis/world-analysis/SKILL.md` | evidence, adaptive sections, information transfer, tags, Bedrocks | Implemented |
| `Create Character [instructions]` | `creation/character/SKILL.md` | adaptive sections, information transfer, evidence, tags, Bedrocks; relevant Phase 6 analysis | Implemented procedure |
| `Create World [instructions]` | `creation/world/SKILL.md` | adaptive sections, information transfer, evidence, tags, Bedrocks; relevant Phase 6 analysis | Implemented procedure |
| `Refine Character` / `Refine World` | `refinement/patch-refinement/SKILL.md` + target skill | patch operations, dependency map, Information Transfer, Bedrocks, relevant tags | Implemented procedure |
| `Refine Sheet: [changes]` | `refinement/patch-refinement/SKILL.md` + `analysis/analysis-sheet/SKILL.md` | patch operations, dependency map, Information Transfer, Evidence and Inference, Bedrocks, relevant tags | Implemented procedure |
| `Create Context Sheet [instructions]` / `Context Sheet` | `creation/context-sheet/SKILL.md` | adaptive sections, information transfer, evidence, Bedrocks, tags; available Analysis/Character/World assets | Implemented procedure |
| `Create Scenario [quantity; instructions]` | `creation/scenario-starting-message/SKILL.md` | style/format, opening design, information transfer, evidence, Bedrocks, tags, project context | Implemented procedure |
| `Create Description [instructions]` | `creation/description/SKILL.md` | information transfer, adaptive sections, evidence, Bedrocks, applicable tags, approved project sources | Implemented procedure |
| `Plan Lorebooks` / `Create Lorebook Plan [instructions]` | `creation/lorebook-planning/SKILL.md` → applicable method/reference files | Information Transfer, Bedrocks, applicable Tags, active project assets, extracted Lorebook Creator references | Implemented procedure; handoff only, not JSON / JavaScript |
| `Refine [target]` / `Expand [target]` | `refinement/patch-refinement/SKILL.md` or `refinement/expansion/SKILL.md` + target skill | patch operations / expansion methods, dependency map, Information Transfer, Bedrocks, Adaptive Sections, Evidence and Inference, relevant tags | Implemented procedure |
| `Help [topic]` | This index, then relevant installed file | As needed | Implemented |
| `Review [target]` | `quality/SKILL.md` | Applicable coverage, consistency, and output validators; target artifact skill | Implemented; explicit review report |
| `New Project` / `Switch Project [name]` | `core/project-isolation/SKILL.md` | command router | Implemented |
| User supplies tags | `shared-systems/tags/SKILL.md` | applicable individual tag files | Implemented |
| User supplies or implies a core invariant | `shared-systems/bedrocks/SKILL.md` | information transfer | Implemented |
| Strange / hybrid / nonstandard concept | `shared-systems/adaptive-sections/SKILL.md` | information transfer | Implemented foundation |
| Conflicting, incomplete, or image-derived information | `shared-systems/evidence-and-inference/SKILL.md` | tags if present | Implemented foundation |

## Phase 11 — implemented Lorebook Planning tree

```text
creation/lorebook-planning/
├── SKILL.md
├── decision-framework.md
├── entry-brief-specification.md
├── advanced-script-handoff.md
├── content-pattern-selection.md
└── references/lorebook-creator/
    ├── SOURCE_README.md
    ├── SKILL.md
    ├── assets/
    │   ├── full-system-overview.md
    │   ├── example-core-entry.json
    │   └── example-advanced-onomatopoeia.js
    └── references/
        ├── entry-schema.md
        ├── content-patterns.md
        └── advanced-script-patterns.md
```

Phase 11 creates a detailed Markdown handoff for a separate Lorebook Creator. It decides what belongs in the main project documents versus normal keyword / constant Lorebook entries versus conditional Advanced Scripts; designs Lorebook boundaries and entry briefs; specifies triggers, scope, priority / insertion relationships, Bedrocks, content patterns, Advanced Script detection / injection / cleanup requirements, platform assumptions, and tests. It does not output actual JSON or JavaScript. The supplied source describes normal Lorebook JSON for JanitorAI and SillyTavern-style World Info, while Advanced JavaScript is described for JanitorAI; other runtime compatibility must be validated.

Phase 11 regression specifications: `tests/phase-11-lorebook-planning-regression-tests.md` (70 cases; not executed against a target LLM/runtime).

## Current implemented tree

```text
narrative-engine-v3/
├── SKILL.md
├── INDEX.md
├── core/
│   ├── command-router/SKILL.md
│   ├── workflow/SKILL.md
│   └── project-isolation/SKILL.md
└── shared-systems/
    ├── bedrocks/SKILL.md
    ├── adaptive-sections/SKILL.md
    ├── information-transfer/SKILL.md
    ├── evidence-and-inference/SKILL.md
    └── tags/
        ├── SKILL.md
        ├── tag-index.md
        └── built-in/*.md
refinement/
├── README.md
├── patch-refinement/
│   ├── SKILL.md
│   ├── patch-operations.md
│   └── artifact-dependency-map.md
└── expansion/
    ├── SKILL.md
    └── expansion-methods.md
```

## Phase 6 — implemented analysis tree

```text
analysis/
├── README.md
├── analysis-sheet/SKILL.md
├── concept-analysis/SKILL.md
├── reference-analysis/
│   ├── SKILL.md
│   ├── image-analysis.md
│   ├── context-reconstruction.md
│   └── rp-log-analysis.md
├── character-analysis/SKILL.md
└── world-analysis/SKILL.md
```

Phase 6 provides the Analysis Sheet and specialist analysis procedures. Use it to interpret the user's supplied information and create the understanding checkpoint; Phase 7 consumes approved findings instead of repeating that analysis.

## Phase 7 — implemented Character and World creation tree

```text
creation/
├── README.md
├── character/SKILL.md
└── world/SKILL.md
```

Phase 7 contains operational generation procedures. Character Creation builds one or more finished Character Sheets. World Creation builds the relevant World Sheet. Both procedures include source reconciliation, scope handling, information ledgers, adaptive section selection, tag and Bedrock behavior, cross-output coverage, and completion checks.

The modules are separate by design. A user can request a Character Sheet without a World Sheet, a World Sheet without character profiles, or both. Neither module generates the Context Sheet or Scenario automatically.

## Phase 8 — implemented Context Sheet generation tree

```text
creation/
└── context-sheet/
    └── SKILL.md
```

Phase 8 creates the comprehensive, self-contained information handoff for the separate narrator/roleplayer AI. It integrates the approved concept, project intentions, narrative focus, relevant character details, relationships, world rules, plot context, tone, narrative configuration, special mechanics, and all project-relevant confirmed Bedrocks. It consumes Phase 6 analysis and Phase 7 assets when available, but it does not require every asset to exist before a Context Sheet can be requested. It does not create a Scenario, Description, or Lorebook Plan.

## Phase 9 — implemented Scenario starting-message generation tree

```text
creation/
└── scenario-starting-message/
    ├── SKILL.md
    ├── style-and-format.md
    └── opening-design.md
```

Phase 9 consumes the active project's approved Analysis Sheet, Context Sheet, Character Sheets, World Sheet, relationships, plot material, tags, and Bedrocks when available. It generates one opening message by default or exactly the quantity requested. Multiple outputs are independent alternatives unless the user requests a connected multi-part opening. The module applies the user's vivid, grounded 2–4 paragraph default style and the four notation categories: narration in asterisks, spoken dialogue in quotation marks, private character/NPC thoughts in triple backticks, and OOC `//` comments only when explicitly requested. It never writes the user's thoughts, dialogue, decisions, or voluntary actions and never continues roleplay.

Phase 9 files:
- `creation/scenario-starting-message/SKILL.md` — operational command, source, scene-construction, agency, Bedrock, output, and validation procedure.
- `creation/scenario-starting-message/style-and-format.md` — complete writing style and four-part notation rules.
- `creation/scenario-starting-message/opening-design.md` — narrative-gravity-led opening design, playable hooks, variation, and anti-patterns.
- `tests/phase-9-scenario-regression-tests.md` — behavioral regression specifications (not executed against a target model/runtime).

## Shared-system dependencies

- **Bedrocks:** load for analysis of project invariants and for any creation/refinement that must preserve them.
- **Adaptive Sections:** load whenever organizing analysis or project-document sections.
- **Information Transfer:** load when approved analysis or project facts must appear in downstream deliverables.
- **Evidence and Inference:** load when interpreting incomplete context, images, RP logs, references, or possible additions.
- **Tags:** load when tags are supplied, inferred tags are being considered, or tag-controlled behavior affects the task.

## Help lookup

When the user invokes `Help [topic]`:

1. Search this index for the topic or command.
2. Open the listed skill and relevant dependencies.
3. Explain its purpose and basic use in brief, plain language.
4. If the route is scaffolded, say it is mapped but not fully implemented.
5. If the route is reserved, say it is planned but the module is not included yet.
6. Stop after the explanation. Do not append a command list or continue generating an artifact unless the user also asked for one.


## Phase 10 — Description generation

`Create Description` routes to `creation/description/SKILL.md`. The module creates a human-facing Markdown description of the requested roleplay concept, complete project, world, plot, narrative, or named component. It resolves the active project, subject, audience, purpose, and disclosure scope; reconciles the latest approved sources; selects an adaptive presentation form; writes natural reader-facing prose; and validates factual support, tags, Bedrocks, length, and audience separation. It is not a shortened Context Sheet or an AI narrator prompt.

Regression specifications: `tests/phase-10-description-regression-tests.md` (32 cases; not yet executed against a target LLM/runtime).


## Phase 12 — implemented Refinement and Expansion

```text
refinement/
├── README.md
├── patch-refinement/
│   ├── SKILL.md
│   ├── patch-operations.md
│   └── artifact-dependency-map.md
└── expansion/
    ├── SKILL.md
    └── expansion-methods.md
```

Phase 12 implements two distinct operations:

- **Patch Refinement** applies minimal, targeted edits to the exact current artifact. It preserves all unaffected wording and structure, distinguishes artifact-local edits from canonical project changes and Bedrock revisions, and patches existing dependent outputs only where they contain stale or affected material.
- **Expansion** adds requested depth, detail, examples, operational explanation, connective information, or new sections while preserving established traits, habits, lore, relationships, world details, and dynamics. It uses evidence boundaries, narrative gravity, and relevant tag scopes to prevent uncontrolled invention or padding.

Supported targets include the Analysis Sheet, Character Sheet, World Sheet, Context Sheet, Scenario, Description, and Lorebook Plan. The modules require the exact current target artifact; they must not reconstruct missing content from vague memory. They preserve the target's original output identity and do not claim cross-session memory.

Regression specifications: `tests/phase-12-refinement-expansion-regression-tests.md` (70 cases; specifications only, not executed against a target LLM/runtime).


## Phase 13 — implemented Quality Assurance tree

```text
quality/
├── README.md
├── SKILL.md
├── coverage-validation/SKILL.md
├── consistency-validation/SKILL.md
└── output-validation/SKILL.md
```

Phase 13 is the mandatory internal finalization layer for generated and modified artifacts. It follows the Notion plan's six groups: concept fidelity, Bedrock integrity, coverage, structure, output identity, and style/tag/refinement compliance. Output Validation runs for every artifact; Coverage and Consistency run when their source/project conditions apply. QA performs safe local repairs, rechecks repairs, and surfaces material blockers or uncertainties without appending a verbose report by default.

Regression specifications: `tests/phase-13-quality-assurance-regression-tests.md` (66 cases; specifications only, not executed against a target LLM/runtime). Use `tests/VALIDATION_RUN_TEMPLATE.md` to record actual model/runtime runs.
