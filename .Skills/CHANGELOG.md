## 1.1.1 — Uncensored hardening (post Phase 13)

- Added explicit **No content censorship** global operating rule in root `SKILL.md`. The engine never sanitizes, softens, moralizes, or refuses project material because it is sexual, violent, dark, taboo, extreme, or offensive.
- Strengthened `shared-systems/tags/built-in/uncensored.md`: full adult/extreme content fidelity, removal of “higher-priority platform or safety constraints” deference.
- Updated command-router conflict handling to remove content-filtering deference; only functional engine boundaries remain non-negotiable.
- Updated Uncensored handling language in character, context-sheet, description, scenario, analysis, and tag-system modules for consistency.
- Functional systems (routing, Bedrocks, adaptive sections, QA, information transfer, etc.) remain intact.

## 1.1.0 — Phase 13 Quality Assurance

- Implemented `quality/SKILL.md` as the system-wide finalization coordinator for generated, refined, and expanded project artifacts.
- Added `coverage-validation/SKILL.md` for approved Analysis Sheet information transfer, artifact-specific destination coverage, and Context Sheet completeness.
- Added `consistency-validation/SKILL.md` for Bedrock integrity, canon/source precedence, character/world constraints, chronology, relationships, tag scope, project isolation, and cross-artifact consistency.
- Added `output-validation/SKILL.md` with separate contracts for Analysis Sheet, Character Sheet, World Sheet, Context Sheet, Scenario, Description, Lorebook Plan, Refinement, and Expansion.
- Added BLOCK / REPAIR / WARN / PASS finding handling, safe local repair rules, mandatory revalidation, concise reporting, and explicit limitations on claims about target-model/runtime testing.
- Added 66 Phase 13 regression specifications aligned to the Notion quality criteria and 15 system regression themes, plus a manual/target-model validation run template.
- Updated root orchestration, command routing, INDEX, architecture map, implementation status, package README, and manifest. Added `Review [target]` routing.
- Phase 13 is implemented at the AI-instruction level. Regression specifications have not been executed against a target LLM/runtime.

## 1.0.0 — Phase 12 Patch Refinement and Expansion

- Implemented `refinement/patch-refinement/SKILL.md` as a complete minimal-patch procedure for all supported project artifacts.
- Added `patch-operations.md` defining ADD, REPLACE, REMOVE, REPHRASE, MOVE, RETITLE, SPLIT, MERGE, and scope-adjustment behavior.
- Added `artifact-dependency-map.md` to distinguish artifact-local edits from canonical fact changes and selectively propagate updates to existing dependent outputs.
- Implemented `refinement/expansion/SKILL.md` as a separate additive-development procedure that preserves established layers.
- Added `expansion-methods.md` for depth, behavioral, contextual, connective, structural, breadth, operational, narrative, and presentation expansion.
- Added safeguards for exact source availability, command-local scope, Bedrock revisions, tag scope, Improvise/Detailed behavior, and no cross-session memory claims.
- Added 70 Phase 12 behavioral regression specifications; they have not been executed against a target LLM/runtime.
- Updated root routing, command router, INDEX, architecture map, implementation status, README, migration notes, creation README, and manifest.
- Phase 13 output-specific quality assurance remains reserved.

# Changelog

## 0.4.0 — Phase 6 Analysis Procedures

- Replaced Phase 6 module-contract placeholders with actionable AI operating procedures.
- Implemented the Analysis Sheet coordinator, Concept Analysis, Reference Analysis routing, Image Analysis, Context Reconstruction, RP Log Analysis, Character Analysis, and World Analysis.
- Added a 14-case Phase 6 model-behavior regression suite.
- Updated the package index, architecture map, implementation status, migration notes, README, and manifest to distinguish implemented AI instructions from scaffolded modules.
- Clarified that this is a Markdown Skill package: procedures are LLM instructions, not executable Python/JavaScript functions or an application runtime.
- Phase 7 Character and World creation remains scaffolded; Phase 8–13 remain reserved.


## 0.5.0 — Phase 7 Character and World Creation Procedures

- Replaced the Phase 7 Character Creation scaffold with an operational step-by-step Character Sheet generation procedure.
- Replaced the Phase 7 World Creation scaffold with an operational step-by-step World Sheet generation procedure.
- Added source precedence and contradiction handling, internal information ledgers, command-local scope handling, adaptive section selection, Bedrock/tag enforcement, information-transfer checks, and output completion procedures.
- Added detailed handling for Full Physical Description, Uncensored, Improvise, Detailed, Open World, Open Interaction, non-human/abstract character entities, unusual worlds, contained settings, and broad setting scopes.
- Added 33 Phase 7 model-behavior regression specifications.
- Updated the creation module map, INDEX, implementation status, architecture map, README, migration notes, root route information, and package manifest.
- Phase 7 is now implemented at the AI-instruction level; model-behavior tests have not yet been executed.
- Phase 8 Context Sheet is the next implementation stage.


## 0.6.0 — Phase 8 Context Sheet Generation

- Implemented `creation/context-sheet/SKILL.md` as an operational, step-by-step Context Sheet generation procedure.
- Defined the Context Sheet as the comprehensive, self-contained, narrator-facing project information handoff, distinct from the Analysis Sheet, Character Sheets, World Sheet, Scenario, Description, and Lorebook Plan.
- Added source precedence, approval handling, internal context ledger, integration procedures for characters/relationships/world/plot, narrative configuration, knowledge boundaries, Bedrock consolidation, adaptive structure, and complete information-transfer validation.
- Added special handling for early Context Sheets, direct generation without an Analysis Sheet, mysteries/secrets, Open World versus Open Interaction, user persona/agency, command-local scope, and multiple-project isolation.
- Added 33 Phase 8 behavioral regression specifications; they have not been executed against a target model/runtime.
- Updated the root orchestrator, command router, INDEX, architecture map, implementation status, creation README, migration notes, package README, and manifest.
- Phase 9 Scenario starting-message generation is now the next implementation stage.


## 0.7.0 — Phase 9 Scenario Starting-Message Generation

- Implemented `creation/scenario-starting-message/SKILL.md` as a complete operational procedure for generating ready-to-use opening messages.
- Added `style-and-format.md` with the user's vivid, grounded prose requirements, distinct character-voice rules, 2–4 paragraph default, third-person default, and exact four-part narration/dialogue/thought/OOC notation.
- Added `opening-design.md` for narrative-gravity-led opening selection, context integration, scene movement, playable response opportunities, alternative variation, pacing, and failure prevention.
- Defined exact requested message quantity handling; one opening is generated by default and multiple openings are independent alternatives unless the user specifies a connected multi-part structure.
- Added source precedence, approval-state handling, Bedrock enforcement, tag-scope handling, knowledge boundaries, project isolation, and protection against inventing the user's actions, dialogue, thoughts, or decisions.
- Clarified that Scenario generation creates starting messages only and never continues roleplay.
- Added Phase 9 regression specifications and updated all routing, package status, architecture, creation documentation, manifest, and version metadata.
- Regression specifications have not been executed against a target model/runtime.


## 0.8.0 — Phase 10 Human-facing Description Generation

- Implemented `creation/description/SKILL.md` as an operational end-to-end Description generation procedure.
- Defined Description as a human-facing Markdown presentation of the selected roleplay project, concept, world, plot, narrative, or component—not a Context Sheet, AI prompt, Analysis Sheet, Scenario, or asset catalogue.
- Added audience, purpose, subject, and disclosure-scope resolution, including public spoiler-light overviews and explicitly requested full plot synopses.
- Added source precedence across current user instructions and approved Analysis, Character, World, Context, relationship, and plot materials.
- Added adaptive forms for whole-project overviews, world descriptions, plot synopses, short public blurbs, comprehensive descriptions, and custom forms.
- Integrated Information Transfer, Adaptive Sections, Evidence and Inference, Bedrocks, applicable Tags, and project isolation.
- Added 32 Phase 10 behavioral regression specifications; they have not been executed against a target LLM/runtime.
- Updated root routing, command routing, INDEX, architecture map, implementation status, creation documentation, README, Notion reference, and manifest.
- Phase 11 Lorebook Planning handoff generation is the next implementation stage.


## 0.9.0 — Phase 11 Lorebook Planning

- Implemented `creation/lorebook-planning/SKILL.md` as a complete operational procedure for creating project-specific Lorebook Plan handoffs.
- Added explicit destination decisions across main project documents, normal Lorebook entries, Advanced Scripts, and cases where no Lorebook module is needed.
- Added `decision-framework.md` for normal JSON vs Advanced JavaScript selection, platform scope, constant vs keyword activation, grouping, triggers, and priority decisions.
- Added `entry-brief-specification.md` requiring complete purpose, content, scope, source, activation, trigger, priority, insertion, dependency, Bedrock, and test details for each planned entry.
- Added `advanced-script-handoff.md` for behavior-only detection, injection, cleanup, duplicate prevention, safeguards, and runtime validation specifications; no JavaScript is generated.
- Added `content-pattern-selection.md` for selective use of the supplied source patterns without forcing irrelevant sexual, dominance, or specialized material into unrelated projects.
- Extracted and preserved directly readable copies of the supplied Lorebook Creator skill, schema, content patterns, Advanced Script patterns, and illustrative assets under `creation/lorebook-planning/references/lorebook-creator/`; the original ZIP reference remains preserved.
- Recorded the source priority-band variation and requires reasoned recommendations plus platform validation instead of inventing a universal priority taxonomy.
- Added 70 Phase 11 behavioral regression specifications. They have not been executed against a target LLM/runtime.
- Updated root routing, command router, INDEX, architecture map, implementation status, creation README, package README, manifest, and package metadata.
- Phase 12 Patch Refinement and Expansion is the next implementation stage.
