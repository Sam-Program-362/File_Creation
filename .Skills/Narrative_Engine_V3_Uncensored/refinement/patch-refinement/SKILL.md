---
name: narrative-engine-patch-refinement
description: Applies minimal, precise revisions to existing Narrative Engine artifacts while preserving all unrelated content and synchronizing only genuine dependencies.
status: implemented
stage: 12
---

# Patch Refinement — Operational System

## 1. Purpose

Patch Refinement changes an existing artifact without regenerating or stylistically rewriting the entire document. Its governing rule is:

**Refinement is NOT regeneration. Treat the current artifact as authoritative and modify only the requested material plus dependencies that genuinely require an update.**

The system preserves every unaffected sentence, paragraph, bullet, heading, and section exactly wherever possible. It does not paraphrase, reorganize, simplify, shorten, polish, expand, or improve unrelated material.

This directly carries forward V2's Patch Refinement Engine and Content Preservation Rule, adapted to V3's multiple distinct deliverables and dependency-aware information transfer.

## 2. Activation

Activate for:

- `Refine: [changes]` when one target artifact is clearly active;
- `Refine [target]: [changes]`;
- `Refine Sheet: [changes]` for the Analysis Sheet;
- `Refine Character: [changes]` or `Refine Character [name]: [changes]`;
- `Refine World: [changes]`;
- `Refine Context Sheet: [changes]`;
- `Refine Scenario: [changes]`;
- `Refine Description: [changes]`;
- `Refine Lorebook Plan: [changes]`;
- an unambiguous natural-language request to alter a previously generated artifact without rebuilding it.

The target skill is always loaded alongside this module. Examples:

- Character target: `creation/character/SKILL.md`.
- World target: `creation/world/SKILL.md`.
- Context Sheet target: `creation/context-sheet/SKILL.md`.
- Scenario target: `creation/scenario-starting-message/SKILL.md` and its relevant references.
- Description target: `creation/description/SKILL.md`.
- Lorebook Plan target: `creation/lorebook-planning/SKILL.md` and the relevant planning references.
- Analysis Sheet target: `analysis/analysis-sheet/SKILL.md` and relevant analysis modules.

## 3. Required skill loading

Load:

1. This skill.
2. `patch-operations.md`.
3. `artifact-dependency-map.md`.
4. The target artifact's own generation skill.
5. `shared-systems/information-transfer/SKILL.md`.
6. `shared-systems/bedrocks/SKILL.md` when the artifact or change is subject to Bedrocks.
7. `shared-systems/adaptive-sections/SKILL.md` if a section is added, removed, renamed, split, merged, or structurally changed.
8. `shared-systems/evidence-and-inference/SKILL.md` if the change corrects or adds source-derived information or an inference.
9. `shared-systems/tags/SKILL.md` and relevant individual tag definitions when a tag affects the requested change.
10. `core/project-isolation/SKILL.md` when more than one project exists in the session.

Do not load unrelated creation modules. Use the dependency map to decide whether another existing asset is actually affected.

## 4. Source and canonical-version resolution

Before editing, locate the **exact current version** of the target artifact.

Use this order:

1. A clear, current user instruction that explicitly corrects or revises the relevant fact.
2. The latest approved version of the named artifact in the active project.
3. The latest explicit project facts and decisions supplied by the user.
4. The approved Analysis Sheet for decisions that have not since been revised.
5. Other current assets that contain relevant cross-references.
6. Earlier drafts or source material only to clarify history, not to silently override approved current content.

The last generated/approved artifact is the current working version for the active project while it remains available. Do not reinterpret the entire project from scratch.

### If the exact artifact is unavailable

- Do not fabricate a reconstructed version from a title, summary, or vague memory.
- If the user supplied a file or source, inspect that exact source before editing.
- If the artifact existed earlier in the current conversation but is no longer available in usable context, say that the exact text is unavailable and ask the user to paste or attach it.
- If only one small requested statement is directly available, you may provide a proposed replacement for that statement, but do not claim to have patched the entire artifact.

## 5. Resolve the target and edit scope

Identify:

- active project;
- target artifact type;
- specific character, world, relationship, section, entry, message, or component if applicable;
- exact statement(s) or area to change;
- requested result;
- any explicit preservation or exclusion instructions;
- whether the change is artifact-local, project-canonical, or a deliberate revision of a Bedrock.

### Target inference

- If the target is named, use it.
- If the target is omitted and exactly one plausible artifact is active, infer it.
- If several plausible targets exist, ask one concise clarification question.
- Do not default to “latest project” when the request clearly names a particular artifact.

### Three change scopes

**A. Artifact-local change** — changes only how information is expressed or organized in one deliverable. Examples: fix a sentence in a Description, adjust a heading, change the formatting of a Scenario, or shorten one section without changing the underlying project fact.

**B. Canonical project-fact change** — changes an established fact, trait, behavior, relationship, setting rule, plot condition, or other project truth. The target artifact is patched first; then inspect existing dependent outputs and update only those passages that now contain stale or contradictory information.

**C. Bedrock revision** — intentionally changes or removes a core invariant. Apply only when the user's intention to revise that Bedrock is clear. Update the clean Bedrocks list and relevant dependent passages. If the request merely appears to conflict with a Bedrock and the intention is unclear, ask before changing it.

A command-local instruction affects only that operation unless the user clearly makes it project-wide. A request to change a character fact is usually canonical when it describes the character, but a presentation-only wording change is artifact-local.

## 6. Classify the requested edit

Determine the smallest operation or combination of operations that accomplishes the request:

- **ADD** — insert genuinely new information into the correct location.
- **REPLACE** — replace a specific incorrect or outdated statement with the requested one.
- **REMOVE** — delete information only when the user explicitly asks for its removal or the removal is essential to correct an explicitly identified contradiction.
- **REPHRASE** — change wording while preserving the same meaning.
- **MOVE** — move material to a more appropriate section without changing its meaning.
- **RETITLE** — rename a heading or label only.
- **SPLIT / MERGE** — change section boundaries only when explicitly requested or necessary to carry out the requested structural edit.
- **SCOPE ADJUSTMENT** — change the audience, entity, timeframe, or conditions covered by a statement, only as requested.

Do not convert a simple correction into a full rewrite. Do not use REPHRASE as an excuse to improve neighboring prose.

## 7. Internal patch plan

Before applying edits, build a compact internal patch plan. Do not expose it by default.

For every proposed change, record:

1. target artifact and exact location;
2. operation type;
3. current content anchor;
4. requested new content or action;
5. reason the change is necessary;
6. whether it changes canonical project information;
7. existing dependent outputs that contain or rely on the changed information;
8. constraints to preserve, especially Bedrocks and scoped tags.

Use the smallest reliable text region as the edit anchor. A patch should not depend on matching a broad paragraph if a unique sentence or bullet is sufficient.

If a requested change requires multiple edits, order them so that the primary fact is corrected first, then dependent references, then structure/formatting.

## 8. Patch application procedure

1. Keep the original artifact as the baseline.
2. Apply only the planned operations.
3. Preserve all untouched wording, order, headings, formatting, and section boundaries exactly.
4. Do not add explanatory commentary inside the artifact unless the user asked for it.
5. Do not silently delete information. When replacing an incorrect statement, ensure the obsolete version does not remain elsewhere in the same artifact as an apparent competing fact.
6. If a new section is required, use Adaptive Sections and place it where it belongs without restructuring unrelated content.
7. Preserve a clean Bedrocks section containing only Bedrock points.
8. Do not expose analysis provenance in finished Character, World, Context, Scenario, or Description material.

See `patch-operations.md` for detailed change semantics and output modes.

## 9. Dependency handling and propagation

A canon-relevant edit may affect more than the target document. Use `artifact-dependency-map.md`.

The rule is **minimal change with complete dependency handling**:

- Inspect the artifacts that plausibly depend on the changed fact.
- Update an existing dependent artifact only where it repeats, references, or relies on the outdated information.
- Preserve unaffected sections in those dependent artifacts too.
- Do not create a deliverable that does not already exist or was not requested.
- Do not rewrite an entire Context Sheet, Scenario, Description, or Lorebook Plan merely because one fact changed.
- Do not propagate presentation-only edits as project facts.
- Do not let derived documents (such as a Description or Scenario) silently become the source of truth for the underlying Character/World/Project.

If a dependent artifact is not present in the active session, do not invent its contents. Record the dependency as not currently patchable and state that only when it materially matters to the user.

## 10. Special handling

### Analysis Sheet refinements

- Patch the Analysis Sheet only unless the user also requests asset updates.
- If an approved analysis finding is corrected before creation, later creation must use the corrected finding.
- If a previously generated asset already contains the old fact and the user has changed the canonical project fact, inspect and patch that asset only where affected.

### Character and World refinements

- Preserve all existing character/world details not covered by the requested change.
- If a fact changes the character or world canon, inspect dependent Context Sheet, Scenario, Description, and Lorebook Plan passages where applicable.
- A character-only presentation adjustment does not automatically change the world or other characters.

### Context Sheet refinements

- Keep the Context Sheet comprehensive and self-contained.
- Do not add Analysis Sheet-only headings such as `Provided Elements`, `Missing Elements`, or `Planned Expansion`.
- If the edit changes a source fact, synchronize only the other existing assets that need that fact.
- Do not change a Character Sheet or World Sheet merely because the Context Sheet's wording is being clarified, unless the underlying fact changes.

### Scenario refinements

- Patch the requested opening message(s) only.
- Preserve the four notation categories and user-character agency rules.
- If an opening's staging or wording changes but project canon does not, do not propagate the edit into the Context Sheet or source assets.
- If a scenario statement exposes a factual conflict, correct the Scenario to match current canon unless the user explicitly changes canon.

### Description refinements

- Keep the output human-facing.
- Do not turn the Description into an AI prompt or Context Sheet.
- Presentation edits remain local unless the user explicitly revises the underlying project fact.

### Lorebook Plan refinements

- Preserve the handoff-only boundary: no ready-to-import JSON or executable JavaScript.
- Update affected lorebook/entry briefs, triggers, priorities, dependencies, Bedrock references, or test requirements only where the requested change requires it.
- If project canon changes, do not silently treat the Lorebook Plan as the new source of truth; reconcile it against the current project assets.

## 11. Bedrocks and tags during refinement

- Never weaken, omit, contradict, or silently rewrite an applicable Bedrock.
- A clear user instruction can revise a Bedrock; a merely ambiguous conflict cannot.
- Keep the visible Bedrocks section as a plain list of Bedrock points, without extra instruction text.
- Preserve tag names, scopes, and effects unless the user asks to change them.
- If a tag's scope changes, inspect only the components affected by that tag.
- Do not infer `Improvise`, `Detailed`, `Uncensored`, `Open Interaction`, or `Open World` as globally active merely because one artifact is being refined.

## 12. Output contract

Default behavior:

- If the artifact is manageable and the exact baseline is available, return the **complete revised artifact**, preserving all unaffected content verbatim.
- If the artifact is too large to reproduce safely, provide an exact patch package: identify the target section/anchor, give the complete replacement or insertion text, and clearly state what must remain untouched. Do not silently summarize omitted sections.
- If the user asks for changed sections only, return only those sections and clearly identify the target artifact.
- If the user asks for the edit plan or diff, show the patch summary rather than applying an unrequested full rewrite.
- If the requested operation cannot safely be applied because the target or exact source is missing, say what is missing and do not pretend the patch is complete.

When dependent artifacts were also patched, list them briefly outside the artifact. Do not append a command menu or a generic invitation to refine again.

## 13. Correct and incorrect behavior examples

### Example A — one character fact changes

User request: `Refine Character [change Akari's eye color to amber; leave everything else untouched]`.

Correct behavior:
- replace only the exact eye-color statement in Akari's current Character Sheet;
- inspect the Context Sheet and other existing outputs for stale statements that specify another eye color;
- update only those stale passages;
- preserve all unrelated character description and formatting.

Incorrect behavior:
- regenerate Akari's entire Character Sheet;
- alter her hairstyle, personality, clothing, or backstory;
- rewrite the whole Context Sheet for style consistency.

### Example B — presentation-only correction

User request: `Refine Description [remove the mention of the northern capital from the public blurb]`.

Correct behavior: remove that mention from the Description only, unless the user explicitly says the capital no longer exists in the project.

Incorrect behavior: delete the capital from the World Sheet and Context Sheet or treat the omission as a canon change.

### Example C — Bedrock conflict

An existing Bedrock says the ruler never executes citizens. The user asks to add a scene in which the ruler orders a citizen's execution but does not say whether the Bedrock is changing.

Correct behavior: identify the contradiction and ask whether the user intends to revise the Bedrock or wants a different event.

Incorrect behavior: silently ignore the Bedrock or automatically rewrite it.

## 14. Final validation

Before returning the result, verify:

### Scope
- [ ] Correct active project and artifact were selected.
- [ ] Every change corresponds to the user's request.
- [ ] Command-local constraints were not converted into permanent rules.

### Preservation
- [ ] All unaffected sentences, paragraphs, bullets, headings, and section order remain identical where possible.
- [ ] No unrequested paraphrasing, polishing, compression, expansion, or reorganization occurred.
- [ ] No information was deleted unless explicitly requested or strictly necessary to remove an identified contradiction.

### Coherence
- [ ] The result agrees with the latest approved project facts.
- [ ] Relevant dependent artifacts were inspected and patched only where necessary.
- [ ] No stale duplicate statement remains in the target.
- [ ] Bedrocks and tag scopes remain correct.

### Output identity
- [ ] The target artifact still performs its original function.
- [ ] The artifact's own creation-skill output contract is respected.
- [ ] The result is a patch, not an accidental regeneration.

Do not print this checklist unless requested.
