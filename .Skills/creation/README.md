---
name: narrative-engine-creation
status: implemented
stage: 7-8
description: Operational Character, World, and Context Sheet generation procedures for Phases 7 and 8.
---

# Phase 7 — Character and World Creation

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.** Phase 7 contains complete step-by-step generation procedures for Character Sheets and World Sheets. These are Markdown Skills for an LLM to follow, not executable application functions.

## Purpose

Phase 7 converts supplied and approved project information into finished character and setting assets. It consumes Phase 6 analysis when available, but it does not repeat the analysis subsystem.

## Module map

| Module | Responsibility | Status |
|---|---|---|
| `character/SKILL.md` | Generate one or more adaptive, concept-faithful Character Sheets | Operational procedure implemented |
| `world/SKILL.md` | Generate a coherent, adaptive World Sheet with consistent systems and rules | Operational procedure implemented |

## Character creation sequence

The Character Creation skill resolves the requested character set, reconciles sources, builds an internal information ledger, defines identity and narrative role, develops the relevant physical/psychological/behavioral/voice/history/capability/relationship dimensions, selects adaptive sections, transfers all approved character information, inserts scoped Bedrocks, validates the result, and produces the finished Character Sheet.

It includes special handling for multiple characters, non-human or non-individual entities, deliberately concealed information, direct generation without an Analysis Sheet, and command-local constraints.

## World creation sequence

The World Creation skill identifies the setting's actual ontology and scope, determines its narrative function, models governing rules and systems, develops physical/social/historical/technical structures only when relevant, checks causal and logical dependencies, integrates character and plot constraints without duplicating those assets, selects adaptive sections, transfers approved information, validates Bedrocks, and produces the World Sheet.

It includes special handling for contained settings, broad/open worlds, abstract or simulated realities, intentional gaps, and Improvise behavior.

## Shared foundations

Both modules invoke the shared systems rather than redefining them:

- Adaptive Sections
- Information Transfer and Coverage
- Evidence and Inference
- Bedrocks
- Tag registry and relevant individual tag definitions
- Phase 6 analysis specialists when their findings are applicable

## Boundaries

Phase 7:
- creates Character Sheets and World Sheets;
- preserves the approved concept and source information;
- uses project-specific sections rather than fixed templates;
- carries relevant information forward for later outputs;
- does not create the Context Sheet (Phase 8), Scenario (Phase 9), Description (Phase 10), or Lorebook Plan (Phase 11);
- does not create actual lorebook JSON or JavaScript;
- does not perform patch refinement and expansion (Phase 12);
- does not roleplay, narrate scenes, or simulate a living world.

## Model testing

The procedures are written, but consistent model behavior is not guaranteed by file presence. Run `tests/phase-7-character-world-regression-tests.md` against the target model and platform. Record actual failures and update the relevant skill rather than weakening the expected behavior to fit a poor output.


---

# Phase 8 — Context Sheet Generation

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.**

The module `context-sheet/SKILL.md` creates the central, comprehensive, self-contained information handoff for a separate narrator/roleplayer AI. It consumes approved analysis and existing Character/World assets when available, integrates relationships, plot, tone, narrative configuration, knowledge boundaries, specialized mechanics, and confirmed Bedrocks, and uses an adaptive structure.

The Context Sheet is not a conversational prompt, Analysis Sheet, Character Sheet, World Sheet, Scenario, Description, or Lorebook Plan. It may be generated before separate assets exist, using the project information currently available. It does not create those other deliverables automatically.

The procedure depends on the shared Adaptive Sections, Information Transfer, Evidence and Inference, Bedrocks, Tags, and Project Isolation systems. Behavioral regression specifications are in `../tests/phase-8-context-sheet-regression-tests.md`.


---

# Phase 9 — Scenario Starting-Message Generation

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.** The Phase 9 subsystem creates ready-to-use opening messages for a separate roleplay AI. It does not start or continue roleplay.

## Module map

| Module | Responsibility | Status |
|---|---|---|
| `scenario-starting-message/SKILL.md` | End-to-end Scenario generation, exact quantity handling, source reconciliation, user-agency protection, Bedrock/tag enforcement, and output validation | Operational procedure implemented |
| `scenario-starting-message/style-and-format.md` | Vivid grounded prose, character voice, third-person default, and four-part notation | Operational reference implemented |
| `scenario-starting-message/opening-design.md` | Narrative-gravity-led scene construction, playable hooks, alternatives, pacing, and failure patterns | Operational reference implemented |

## Scenario generation sequence

The generator resolves the active project and requested quantity; gathers the available approved Analysis Sheet, Context Sheet, Character Sheets, World Sheet, relationship and plot information; applies source precedence; selects an opening point of entry based on narrative gravity; establishes scene conditions; preserves character voices and knowledge boundaries; enforces Bedrocks and scoped tags; constructs a vivid, grounded opening; protects the user's character agency; and stops at a natural response opportunity. It outputs exactly one message by default or the exact quantity requested. Multiple outputs are alternatives unless the user requests a connected multi-part opening.

## Four-part message convention

The style reference encodes the requested format: narration in single asterisks, spoken dialogue in double quotation marks, private character/NPC thoughts in triple backticks, and out-of-character notes in `//` lines only when explicitly requested. The user character's thoughts are never generated, and their actions, dialogue, decisions, or voluntary reactions are never invented.

## Boundaries

Phase 9 generates opening messages only. It does not generate a Description (Phase 10), Lorebook Plan (Phase 11), patch refinement/expansion (Phase 12), or system-wide quality framework (Phase 13). Its completion checks are local to Scenario generation.

Regression specifications: `../tests/phase-9-scenario-regression-tests.md`. These tests have not yet been executed against a target LLM/runtime.


---

# Phase 10 — Human-facing Description Generation

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.** `description/SKILL.md` is the operational system for producing a human-facing Markdown description of a requested roleplay concept, whole project, world, plot, narrative, or named component.

## Description responsibilities

The module resolves the active project, subject, audience, purpose, and disclosure scope; reconciles current approved user instructions and project artifacts; identifies the concept's central premise and distinctive appeal; selects an adaptive presentation form; drafts clear natural prose; and validates factual support, applicable tags, Bedrocks, length, and audience separation.

Supported forms include whole-project overviews, world descriptions, plot/narrative synopses, short public blurbs, comprehensive project descriptions, and custom forms when requested. These are selectable forms, not fixed templates.

## Output boundary

A Description is for people. It is not a Context Sheet with fewer details, a system prompt, an AI narrator instruction block, an Analysis Sheet, or a Scenario. It does not automatically create or revise any other project asset. It uses project assets as sources without silently regenerating them.

## Shared dependencies

- Adaptive Sections
- Information Transfer and Coverage
- Evidence and Inference
- Bedrocks
- Tags and applicable individual definitions
- Project Isolation when multiple in-session projects exist

## Validation

Behavioral regression specifications: `../tests/phase-10-description-regression-tests.md` (32 cases). These are specifications only and have not been executed against a target LLM/runtime.


---

# Phase 11 — Lorebook Planning

**Status: IMPLEMENTED AT THE AI-INSTRUCTION LEVEL.** `lorebook-planning/SKILL.md` creates a self-contained Markdown handoff for a separate Lorebook Creator. It does not create import-ready JSON entries or JavaScript.

## Module map

| Module | Responsibility |
|---|---|
| `lorebook-planning/SKILL.md` | End-to-end requirement inventory, destination decisions, architecture planning, entry briefs, Advanced Script briefs, output contract, and final checks |
| `lorebook-planning/decision-framework.md` | Main-doc vs normal Lorebook vs Advanced Script vs no-module classification, platform scope, activation decisions, grouping, trigger design, priority |
| `lorebook-planning/entry-brief-specification.md` | Complete field-aware specification for each planned normal Lorebook entry |
| `lorebook-planning/advanced-script-handoff.md` | Behavior-only specification for conditional detection, injection, cleanup, duplicate prevention, and runtime tests |
| `lorebook-planning/content-pattern-selection.md` | Selective use of source-defined content patterns |
| `lorebook-planning/references/lorebook-creator/` | Directly readable copies of the supplied Lorebook Creator source files |

## Output boundary

The plan may recommend normal Lorebook entries or Advanced Scripts, but it does not build either. Source-described normal Lorebook JSON targets JanitorAI and SillyTavern-style World Info. Source-described Advanced JavaScript targets JanitorAI. Unknown platform/version semantics are identified for downstream validation, not invented.

Regression specifications: `../tests/phase-11-lorebook-planning-regression-tests.md` (70 cases; not executed against a target LLM/runtime).


## Phase 12 — refinement and expansion

After an asset has been created, use the Phase 12 procedures in `../refinement/` to modify or expand it. Character, World, Context Sheet, Scenario, Description, and Lorebook Plan outputs must retain their original purpose and constraints during edits. Patch Refinement changes only requested material and genuine dependencies; Expansion adds layers without replacing established information.
