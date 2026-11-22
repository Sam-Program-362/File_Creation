---
name: narrative-engine-analysis-sheet
status: implemented
stage: 6
implementation: operational-analysis-procedure
description: Coordinates project analysis and produces the adaptive Analysis Sheet used to verify understanding before creation.
---

# Analysis Sheet — Operational System

## Purpose

Produce an inspectable, project-specific account of what the engine understands before final creation. The Analysis Sheet is a decision and verification checkpoint between raw input and finished project assets. It serves the user and the Narrative Engine; it is **not** the final context handoff for a separate roleplay AI.

The Sheet must answer four practical questions:
1. What is the project, and what makes it interesting?
2. What information is established, and what has been interpreted or inferred?
3. What should be emphasized, preserved, clarified or developed?
4. Where must each approved detail go when the requested final assets are created?

## Activation

Run for:
- `Create Sheet`;
- a new project concept under the default workflow;
- a request to analyze or organize a concept before creation.

Do not run when the user explicitly requests direct generation or explicitly says to skip analysis. In that case, apply the same preservation and evidence rules internally, but do not fabricate an Analysis Sheet that the user did not request.

`Refine Sheet` is an edit operation handled by `refinement/patch-refinement/SKILL.md`. This Analysis Sheet skill creates the artifact; Phase 12 performs targeted edits to an existing version.

## Inputs

Use the material actually supplied and relevant to the current project:
- concept description, premise, instructions and constraints;
- characters, relationships, setting, lore, plot and scenario notes;
- images and other references;
- fragmented notes, documents or RP logs;
- explicit and inferable tags;
- Bedrocks and other hard requirements;
- requested outputs and command-local constraints.

Do not require all input types. Do not assume missing source material exists.

## Procedure

### 1. Establish project boundary

- Identify which project the material belongs to using the active project context and project-isolation rules.
- Separate project-wide facts from character-, relationship-, world-, plot-, reference- and scenario-specific facts.
- Identify the user's immediate request and any command-local instructions.
- Detect whether the request is analysis-first or explicitly direct-generation.
- Do not import details from another project in the same conversation.

### 2. Inventory source material

Create an internal source inventory. For each source or source group, record its type and what it contributes. Examples: user premise, character note, reference image, world note, RP transcript, external document.

Preserve source provenance when it changes confidence or interpretation. Do not clutter the Sheet with a citation for every ordinary sentence; expose sources where they help the user verify an interpretation or resolve a discrepancy.

### 3. Run the relevant specialist analyses

Always run Concept Analysis. Conditionally invoke:
- Reference Analysis for supplied references, images, fragmented context or logs;
- Character Analysis for meaningful character or relationship material;
- World Analysis for meaningful setting or world-system material.

Do not invoke a specialist merely to fill a heading. Do not output specialist reasoning as a repeated stack of reports; synthesize its useful results.

### 4. Establish information status

Use the shared Evidence and Inference system. Classify material as:
- **Established:** explicitly supplied or approved by the user.
- **Supported:** strongly supported by source context or multiple consistent signals, but not directly stated.
- **Inferred:** plausible but unconfirmed interpretation.
- **Proposed:** a creative addition or direction suggested by the engine.
- **Unknown:** not established and not safely inferable.

Keep these classifications internally. Show them in the Sheet when the distinction materially affects trust, canon, or a decision the user should review. Do not label every sentence if that would make the Sheet unreadable.

### 5. Identify the concept core

Synthesize the project's:
- primary and secondary type, if useful;
- expected scope and intended use;
- core concept and concise concept summary;
- core appeal and what makes the premise interesting;
- emotional and thematic center;
- central relationship, conflict, mystery, mechanism or dynamic;
- narrative gravity: the element that should naturally receive the greatest focus;
- primary, secondary and tertiary priorities.

Do not mechanically fill these fields if they do not apply. Rename or replace them for unusual concepts.

### 6. Determine tags and Bedrocks

- Preserve explicit tags and their scope.
- Consider automatic tags only when strongly supported. Mark each as auto-applied, give its scope and a brief reason, and leave it open to correction.
- Read the individual definitions for tags that affect analysis or generation.
- Capture explicit Bedrocks exactly in meaning and scope using the Bedrocks system.
- Put uncertain possible invariants in a clearly labeled **Bedrock candidates** area, not the confirmed Bedrocks list.
- Do not put explanatory AI instructions inside the visible Bedrocks list.

### 7. Identify gaps and development direction

Determine which unknowns actually affect the concept or requested deliverables. Distinguish:
- a necessary unanswered question;
- an intentional blank or mystery;
- a harmless detail that can remain unspecified;
- a gap that can be completed under the Improvise tag;
- a missing supporting structure that the next creation module must handle.

Without Improvise, do not invent major trauma, secrets, motivations, relationships, world lore or premise-changing events without support or authorization. Ask only when an answer would materially change the project; otherwise mark the uncertainty and proceed with what is established.

When Improvise is active, complete necessary gaps creatively and coherently. Do not include a `Missing Elements` section. Record major creative proposals or meaningful additions so the user can understand what was developed, without reverting to a missing-items checklist.

### 8. Build an adaptive Sheet structure

Use `shared-systems/adaptive-sections/SKILL.md`.
- Identify the natural information groups in this project.
- Select only sections that help the user verify the understanding.
- Add custom headings when conventional sections do not fit.
- Merge related material only when its distinctions remain clear.
- Do not create empty headings or force character/world sections into a concept that does not need them.

Possible analysis dimensions include concept core, image evidence, character context, relationships, world rules, timeline, narrative mechanisms, Bedrocks, tag decisions, unresolved questions and generation direction. These are optional modules, not a template.

### 9. Create the information-transfer map

Use `shared-systems/information-transfer/SKILL.md`.
For every meaningful approved finding, identify the downstream destination(s) that will need it. Typical destinations:
- Character Sheet;
- World Sheet;
- Context Sheet;
- Description;
- Scenario starting message(s);
- Lorebook Plan;
- a custom project asset.

Do not assume every item belongs in every output. The purpose is complete coverage at the correct destinations, not indiscriminate duplication.

### 10. Synthesize and write

Write one coherent Analysis Sheet. Avoid repeating the same observation across multiple headings. Explain a complex inference only as much as necessary for the user to verify it. Keep the user's terminology where possible. Correct obvious transcription or spelling noise only when it does not change the intended meaning; do not normalize unusual names or coined terms without confidence.

### 11. Run the completion check

Before responding, verify:
- the project and immediate request were understood;
- the concept core and narrative gravity are supported;
- source observations are not presented as facts beyond what they show;
- inferred and proposed material is not mislabeled as established;
- tags and Bedrocks retain their scope;
- custom sections were created where necessary;
- no important concept information was omitted for lack of a standard heading;
- Improvise behavior is honored when active;
- downstream destinations exist for approved meaningful findings;
- no final Character Sheet, World Sheet, Context Sheet, Description, Lorebook Plan or Scenario has been generated accidentally.

## Output contract

Produce a Markdown document headed **ANALYSIS SHEET** or a project-appropriate title. The exact section set and order must adapt to the project.

A useful Sheet will usually communicate:
- project identity and scope;
- concept summary and core appeal;
- narrative focus/gravity;
- important characters, relationships, setting or plot structures, as applicable;
- source observations and interpretations where references are involved;
- explicit and auto-applied tags, with scope;
- confirmed Bedrocks and any candidates;
- important gaps or assumptions, unless Improvise is active;
- generation direction and an information-transfer summary when needed.

Do not force the old V2 template as fixed headings. Do not include `Provided Elements`, `Missing Elements` or `Planned Expansion` in the Context Sheet; this is the Analysis Sheet, where such analysis distinctions may be useful unless Improvise is active.

After the Sheet, stop. Do not append a command menu. A short natural prompt for the user to correct the understanding is acceptable when useful, but do not repeat fixed interaction instructions.

## Error handling

- If a source is unreadable or an image is unavailable, say which part could not be inspected and continue with the remaining evidence.
- If sources materially contradict each other, preserve both claims with their sources and mark the conflict. Do not choose one based on convenience.
- If the concept is too ambiguous to classify, describe it in neutral terms rather than forcing a familiar genre.
- If the user supplied only a narrow request, analyze only what is needed; do not produce an oversized project audit.

## Dependencies

- `analysis/concept-analysis/SKILL.md`
- Relevant modules under `analysis/reference-analysis/`
- `analysis/character-analysis/SKILL.md` when applicable
- `analysis/world-analysis/SKILL.md` when applicable
- `shared-systems/evidence-and-inference/SKILL.md`
- `shared-systems/adaptive-sections/SKILL.md`
- `shared-systems/information-transfer/SKILL.md`
- `shared-systems/bedrocks/SKILL.md`
- `shared-systems/tags/SKILL.md` and applicable individual tag files
