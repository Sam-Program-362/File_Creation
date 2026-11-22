# V2 → V3 Foundation Migration Notes

V2 is preserved in `references/System Prompt V2.txt`. This file explains what the first V3 stages retain, adapt, or supersede. It is not a replacement copy of V2.

| V2 system or principle | V3 treatment in this starter |
|---|---|
| Adaptive Narrative Intelligence | Preserved as the central philosophy in the root orchestrator. |
| Understand → Reconstruct → Interpret → Analyze → Verify → Evolve → Structure → Generate | Preserved as the reasoning sequence. |
| Two-Stage Creation Pipeline | Adapted to Analysis Sheet first, then only the requested creation outputs. |
| Analysis → Creation Sanitization | Preserved in the workflow; final documents contain natural project information, not analysis-process commentary. |
| Narrative Perspective Lock | Preserved as objective third-person default for project documents and Scenario narration, unless the user explicitly requests another perspective. |
| RP Type Detection | Implemented as a project-analysis procedure in `analysis/concept-analysis/SKILL.md`. |
| Concept Core Detection | Implemented in `analysis/concept-analysis/SKILL.md`. |
| Narrative Gravity | Implemented in `analysis/concept-analysis/SKILL.md`. |
| Multi-Layer Analysis | Implemented across concept, character, relationship, reference and world analysis modules. |
| Reference Interpretation | Reframed through explicit tag scope and evidence discipline. |
| System Tags | Replaced by a shared, human-readable tag registry with individual definition files. |
| Normal Tag Interpretation | Preserved; understandable user-defined tags remain contextual guidance. |
| Image Intelligence | Implemented in `analysis/reference-analysis/image-analysis.md`, using the shared Evidence and Inference and tag systems. |
| Context Reconstruction | Implemented in `analysis/reference-analysis/context-reconstruction.md`. |
| Character Evolution | Analysis behavior implemented in Phase 6; final Character Sheet generation remains in the Phase 7 implementation queue. |
| World Evolution | Analysis behavior implemented in Phase 6; final World Sheet generation remains in the Phase 7 implementation queue. |
| Narrative Priority Hierarchy | Implemented within Concept Analysis as a flexible priority model, not a mandatory output template. |
| Concept Evolution | Preserved within controlled development and the future analysis/creation modules. |
| Controlled Improvisation | Preserved; the Improvise tag adds explicit proactive gap-completion mode. |
| Inference Boundary | Strengthened into an Evidence and Inference shared system. |
| Section Isolation | Adapted: sections retain distinct responsibilities, but custom and cross-cutting sections are allowed. |
| Section Stability | Implemented in Phase 12 Patch Refinement: unaffected sections remain unchanged while real dependencies are handled selectively. |
| Output Architecture | Strengthened into Adaptive Sections. Fixed templates are no longer mandatory. |
| Fixed Analysis Sheet Format | Superseded by adaptive Analysis Sheet sections. |
| Scene & RP Flow | Narrowed: V3 creates starting messages only; it does not run RP. Phase 9 implements opening momentum, emotional grounding, playability, a natural response hook, and avoidance of unnecessary overnarration. |
| User Persona Rule | Retained as a project-specific inclusion decision in the Context Sheet and Scenario systems; Scenario generation never invents the user character's actions, dialogue, thoughts, or decisions. |
| Patch Refinement | Implemented in `refinement/patch-refinement/`: minimal edits, exact preservation, target resolution, Bedrock handling, and dependency-aware propagation. |
| Content Preservation | Implemented through Information Transfer and Phase 12 Patch Refinement, including explicit deletion rules and exact patch modes. |
| Project Memory Lock | Adapted to temporary in-session working canon; Phase 12 resolves the exact latest active artifact and makes no cross-session memory promise. |
| Expansion Accumulation | Implemented in `refinement/expansion/`: additions preserve traits, habits, lore, relationships, world details, and dynamics unless explicitly changed. |
| Commands | Reworked into a command router with Help, Context Sheet, Description, Lorebook Plan, project isolation, and command-local arguments. |
| Consistency Guard | Bedrocks and shared validation foundations are included; full QA modules are future work. |
| Interaction Loop | The forced end-of-response command menus are removed. Use natural interaction without a repeated footer. |

## Scope correction

V2 described the engine as producing playable RP experiences and interactive narratives. V3 is specifically a **creation and handoff system**. It prepares assets for a separate roleplay AI; it does not become that AI.

## Phase 6 analysis mapping

Phase 6 now contains **operational AI-skill procedures**. The following mapping identifies where the V2 capabilities are implemented:

| V2 concept or capability | Phase 6 destination |
|---|---|
| RP Type Detection | `analysis/concept-analysis/SKILL.md` |
| Concept Core Detection | `analysis/concept-analysis/SKILL.md` |
| Narrative Gravity | `analysis/concept-analysis/SKILL.md` |
| Narrative Weight / Multi-Layer Analysis | `analysis/concept-analysis/SKILL.md` and relevant specialist modules |
| Relationship Signals | `analysis/character-analysis/SKILL.md` |
| Story Structure / Narrative Priorities | `analysis/concept-analysis/SKILL.md` |
| Reference Interpretation | `analysis/reference-analysis/SKILL.md` |
| Image Intelligence | `analysis/reference-analysis/image-analysis.md` |
| Context Reconstruction | `analysis/reference-analysis/context-reconstruction.md` |
| RP-log input capability | `analysis/reference-analysis/rp-log-analysis.md` |
| Character Evolution analysis | `analysis/character-analysis/SKILL.md` |
| World Evolution analysis | `analysis/world-analysis/SKILL.md` |
| Analysis Sheet Format | `analysis/analysis-sheet/SKILL.md`, using adaptive rather than fixed sections |

The V2 Analysis Sheet fields remain available as candidate analytical dimensions, not as mandatory headings. Phase 6 now contains step-by-step procedures, output contracts, constraints and completion checks. Behavioral consistency still needs testing against the Phase 6 regression suite.

## Phase 7 creation mapping

The Phase 7 creation modules separate final asset generation from Phase 6 analysis. The following V2 responsibilities now have operational procedures:

| V2 system or principle | Phase 7 destination | Treatment |
|---|---|---|
| Character Evolution Engine | `creation/character/SKILL.md` | Final character-sheet creation; analysis findings are consumed from Phase 6. |
| World Evolution Engine | `creation/world/SKILL.md` | Final world-sheet creation; analysis findings are consumed from Phase 6. |
| Analysis-to-Creation Sanitization | Both Phase 7 modules | Convert approved analysis findings into natural project information; remove process commentary. |
| Section Isolation Protocol | Both Phase 7 modules + Adaptive Sections | Preserve section responsibilities while creating project-specific headings where needed. |
| Content Preservation Rule | Information Transfer + both Phase 7 modules | Preserve approved content and assign every meaningful point to its appropriate output. |
| Narrative Priority Hierarchy | Phase 6 analysis informs both Phase 7 modules | Allocate detail according to the project's real narrative priorities, not uniform template depth. |
| Character/World Bedrocks | Both Phase 7 modules + Bedrocks system | Preserve applicable core invariants in clean Bedrocks sections and do not contradict them. |

The Phase 7 module contracts have been replaced by full operating procedures. See the Phase 7 generation implementation update below.



## Phase 7 generation implementation update

The initial Character and World files were module contracts only. They have now been replaced with full operational procedures in `creation/character/SKILL.md` and `creation/world/SKILL.md`.

The Character module defines source reconciliation, character-set scoping, identity, physical description, psychology, behavior, voice, history, abilities, relationships, adaptive section construction, tag behavior, Bedrock checks, information transfer, and validation.

The World module defines setting ontology and scope, narrative function, world-rule modeling, spatial and social structures, institutions, history, factions, technology/magic, causal consistency, intentional gaps and Improvise behavior, adaptive sections, Bedrocks, information transfer, and validation.

Phase 7 is now implemented at the AI-instruction level. Target-model regression execution remains pending; see `tests/phase-7-character-world-regression-tests.md`.


## Phase 8 migration — Context Sheet

V2 did not have a distinct, fully developed narrator-facing Context Sheet output. V3 Phase 8 now formalizes it as the central information handoff for the separate roleplay AI. It integrates the project identity, premise, intentions, narrative focus, characters, relationships, world, plot, tone, relevant narrative configuration, and Bedrocks.

The Context Sheet is informational and self-contained, not a conversational prompt or a copy of the Analysis Sheet. Analysis-only headings and source commentary are removed during handoff. The document uses adaptive sections and carries every approved, narrator-relevant information unit into a suitable destination. It remains separate from Scenario starting-message generation.


## Phase 9 migration — Scenario starting messages

The V2 Scene & RP Flow Engine described how to make a scenario immersive, interactive, emotionally grounded, progressive, and naturally hooked. V3 narrows this responsibility to creating the **opening message(s)** for a separate roleplay AI. It does not take subsequent roleplay turns or simulate an ongoing scene.

The V2 scenario-generation style and four notation categories are now implemented in `creation/scenario-starting-message/`:

- Vivid, grounded prose using purposeful physical detail, body language, sensory texture, and subtext.
- Emotion shown primarily through behavior and speech rather than labels.
- Distinct character voices based on the approved Character Sheets and Context Sheet.
- A 2–4 paragraph default, adjusted to the scene and requested length without padding.
- Single asterisks for narration, double quotation marks for spoken dialogue, triple backticks for private character/NPC thoughts, and `//` for OOC comments only when explicitly requested.
- The generator never writes the user's thoughts or invents their voluntary actions, dialogue, decisions, or reactions.
- Exactly the requested number of starting messages is generated. Multiple messages are alternatives by default, not sequential roleplay turns.

The Phase 9 module also integrates current project context, source precedence, tags, knowledge boundaries, Bedrocks, and project isolation. Behavioral regression specifications are in `tests/phase-9-scenario-regression-tests.md`; they have not been executed against a target model/runtime.


## Phase 10 migration — human-facing Description

V2 did not define a dedicated human-facing Description deliverable. V3 Phase 10 adds `Create Description` as a separate presentation output for people who need to understand or evaluate the roleplay concept, world, plot, or complete project.

The Description module in `creation/description/SKILL.md`:

- distinguishes a human-facing overview from the narrator-facing Context Sheet and from a Scenario opening;
- resolves the description's subject, intended reader, purpose, and disclosure scope;
- reconciles the latest approved Analysis, Character, World, Context, relationship, and plot sources;
- supports adaptive whole-project overviews, world descriptions, plot synopses, short public blurbs, comprehensive descriptions, and custom forms;
- preserves the project's defining appeal and relevant dynamics without dumping every detail from every sheet;
- applies Information Transfer, Adaptive Sections, Evidence and Inference, Bedrocks, scoped Tags, and project isolation;
- removes analysis-process commentary and all instructions addressed to a separate roleplay AI;
- does not create or revise any other asset unless the user separately requests it.

Phase 10 regression specifications are in `tests/phase-10-description-regression-tests.md`. They have not been executed against a target model/runtime.


## Phase 12 migration — Patch Refinement and Expansion

V2's refinement and preservation systems are carried forward as operational V3 modules:

| V2 principle | V3 implementation |
|---|---|
| Patch Refinement Engine | `refinement/patch-refinement/SKILL.md` and `patch-operations.md` |
| Content Preservation Rule | Patch Refinement exact-preservation and explicit-deletion requirements |
| Section Stability Rule | Patch Refinement minimal edit scope plus Adaptive Sections |
| Project Memory Lock | Active-session canonical artifact resolution; no cross-session memory promise |
| Expansion Accumulation Rule | `refinement/expansion/SKILL.md` and `expansion-methods.md` |
| Consistency Guard | Dependency map, Bedrocks, Information Transfer, and target-skill checks |
| Refine Sheet / Refine Character / Expand | Routed to Phase 12 for the named artifact, while respecting each V3 artifact's distinct purpose |

V3 strengthens the old rules by distinguishing artifact-local presentation edits from project-canonical fact changes and deliberate Bedrock revisions. It also maps which existing outputs may depend on a changed fact, so propagation is selective rather than a full-project rewrite.

Supported patch/expansion targets include the Analysis Sheet, Character Sheet, World Sheet, Context Sheet, Scenario, Description, and Lorebook Plan. The exact current source artifact is required; missing text is not reconstructed from vague memory.

Phase 12 regression specifications: `tests/phase-12-refinement-expansion-regression-tests.md` (70 cases, not executed against a target LLM/runtime).


## Phase 13 — Quality Assurance

The V3 QA layer supplements V2's Consistency Guard and Section Stability rules with output-specific finalization. It validates concept fidelity, Bedrock integrity, approved-information coverage, adaptive section structure, output identity, tag behavior, and preservation during refinement. QA remains an AI-instruction procedure, not an executable checker, and is internal by default rather than a visible report after every output.
