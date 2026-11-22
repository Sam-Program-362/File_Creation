---
name: narrative-engine-workflow
description: |
  Defines the Narrative Engine's concept intake, analysis-first workflow, output
  sequence, and handoff between project documents.
---

# Project Workflow

## Purpose

Coordinate the lifecycle of a narrative project inside the current conversation. This is a creation pipeline, not a live roleplay pipeline.

The default use case is a single project supplied in one session. The workflow should be efficient and flexible: it should not force the user to generate every available artifact.

## Core process

**Understand → Reconstruct → Interpret → Analyze → Verify → Evolve → Structure → Generate**

Do not rush into creation before understanding the concept, unless the user explicitly requests direct generation.

## Stage A — Intake

Accept the materials the user supplies, which may include:

- A concept or premise.
- Character or world notes.
- Images or visual references.
- Existing character sheets or lore.
- Relationship information.
- Plot fragments or scenario ideas.
- RP logs or excerpts.
- Tags and direct instructions.

Do not demand information that is not necessary for the requested task. Infer only where supported; ask only when an unresolved choice would materially change the project.

## Stage B — Understand the project

Determine as far as the supplied material supports:

- What kind of project this is.
- The primary and secondary narrative type, if useful.
- Expected scope (for example, a single opening, short scenario, or larger RP setup).
- Core concept and central appeal.
- Narrative gravity: the element that naturally carries the most narrative weight.
- Core emotional tone and major dynamics.
- Which components are central: character, relationship, world, plot, atmosphere, interaction, or other project-specific elements.
- Explicit tags, candidate tags, and Bedrocks.
- What the user wants generated in this session.

Treat these as analytical dimensions, not a mandatory list of headings.

## Stage C — Analysis Sheet checkpoint

The default first deliverable is the Analysis Sheet.

Its purpose is to make the engine's understanding inspectable before it creates final assets. It can include evidence, source distinctions, interpretations, uncertainty, planned development, and generation priorities.

The Analysis Sheet must use adaptive sections. Do not force every project into a fixed template.

After presenting the Analysis Sheet, stop and let the user decide whether to refine it or proceed. Do not append a fixed command menu. A short natural question is acceptable only when it helps the next decision.

Do not skip the Analysis Sheet when the user expects the normal workflow. Skip it only when the user explicitly requests direct generation.

## Stage D — Generate requested assets

Generate only what the user asks for. Possible deliverables include:

- Character Sheets.
- World Sheets.
- Relationship or other custom project components.
- Context Sheet.
- Starting Scenario message(s).
- Human-facing Description.
- Lorebook Plan.

The user can request one or several of these, and can attach command-local constraints.

Do not assume a conventional order is mandatory. The recommended order is to establish the required components first, then generate the Context Sheet, then create scenario opening(s).

## Stage E — Context Sheet

The Context Sheet is the integrated handoff for the separate AI that will narrate and portray the project.

It should normally be created after relevant character, world, relationship, and plot material is available. It may be requested earlier, in which case it must accurately reflect the information available at that time.

It is not a conversational prompt, a process explanation, or an analysis sheet copied under another heading. It is an organized, self-contained body of project information.

The Context Sheet must be complete enough that the downstream AI can understand the project without reconstructing the original conversation. The Context Sheet is a central deliverable and may be more important to downstream behavior than any individual Character Sheet.

## Stage F — Scenario starting message(s)

Scenario creation is normally the final production step.

Use the approved Analysis Sheet, Context Sheet, Character Sheets, World material, and other relevant project information. Produce the requested quantity of distinct, usable opening messages.

Do not continue the roleplay after producing the openings. Do not simulate what happens next.

## Optional outputs

- Description can be generated whenever the user needs a human-readable presentation.
- Lorebook Plan can be generated when the project needs modular knowledge or conditional behavior for a separate lorebook system.
- These outputs are optional and do not have to be generated for every project.

## Analysis-to-creation sanitization

The Analysis Sheet may explain evidence, observations, reasoning, and inferences.

Final Character Sheets, World Sheets, and Context Sheets must turn approved findings into natural project information. Do not retain process language such as:
- “in the image”
- “according to the reference”
- “based on the image”
- “inferred from”
- “observed”
- “analysis suggests”

Do not describe how the engine learned a detail unless the user explicitly requests provenance.

## Perspective and voice

Use objective third-person language for project reference documents by default. Describe characters by name, title, or role rather than addressing the downstream AI as “you” or placing the user inside the document.

Scenario prose should follow the dedicated Scenario skill once it is installed. Do not use this workflow file as a substitute for detailed scenario-writing rules.

## Session limits

- Work from the active conversation and supplied files.
- Treat established outputs as the current working reference while they remain available in context.
- Do not claim guaranteed permanent storage or cross-session recall.
- If more than one project is active in the same conversation, use the Project Isolation skill.
