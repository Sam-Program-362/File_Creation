---
name: narrative-engine-command-router
description: |
  Recognize Narrative Engine commands and natural-language equivalents, resolve
  command scope and arguments, and route requests to installed skills.
---

# Command Router

## Purpose

Interpret user commands as operations, not as text to repeat back. The command router identifies the intended action, target, scope, and additional instructions, then routes the request to the appropriate skill.

Do not append command explanations or a command menu to ordinary outputs.

## General command recognition

Commands may be expressed as standalone phrases or embedded in natural language. Recognize both the canonical command and obvious natural-language variants when the intent is unambiguous.

Bracketed text after a command is an argument payload. It is not part of the command name.

Examples:

- `Create Character [only Akari and Ashli for now]`
- `Create Scenario [make 3 alternative openings]`
- `Refine: [change her speech pattern, leave everything else untouched]`
- `Expand World: [add the political structure]`
- `Help [full physical description tag]`

Do not require exact punctuation if intent is clear.

## Command catalog

### Analysis

- **Create Sheet** — request the Analysis Sheet only. Route to `analysis/analysis-sheet/SKILL.md`.
- **Refine Sheet: [changes]** — patch the Analysis Sheet only. Route to `analysis/analysis-sheet/SKILL.md` and `refinement/patch-refinement/SKILL.md`.

### Project assets

- **Create Character [instructions]** — create only the requested character asset(s). Route to `creation/character/SKILL.md`.
- **Create World [instructions]** — create world/setting material. Route to `creation/world/SKILL.md`.
- **Create Context Sheet [instructions]** / **Context Sheet** — create or update the comprehensive information handoff for the separate roleplaying AI. Route to the implemented procedure at `creation/context-sheet/SKILL.md`. Load its shared-system dependencies and available Analysis Sheet, Character Sheet, and World Sheet source modules.
- **Create Scenario [quantity; instructions]** — generate exactly the requested number of opening messages (one by default). Multiple outputs are independent opening alternatives unless the user requests a connected multi-part opening. This is not a command to begin roleplay. Route to `creation/scenario-starting-message/SKILL.md`.
- **Create Description [instructions]** — create a human-facing Markdown description of the requested project, concept, world, plot, narrative, or component. Route to `creation/description/SKILL.md`; load Information Transfer, Adaptive Sections, Evidence and Inference, Bedrocks, applicable Tags, and only the relevant approved project sources. Output the Description itself, not an AI prompt or another project asset.
- **Plan Lorebooks** / **Create Lorebook Plan [instructions]** — create a detailed, project-specific implementation handoff for a separate Lorebook Creator. Route to `creation/lorebook-planning/SKILL.md` and load its decision framework, entry-brief specification, Advanced Script handoff rules, content-pattern selector, source references, and shared Information Transfer, Bedrocks, and applicable Tags. This route is implemented as an AI planning procedure only; it never creates import-ready JSON entries or JavaScript.

### Refinement and expansion

- **Refine [target]: [changes]** — apply a minimal patch to the named existing artifact. Route to `refinement/patch-refinement/SKILL.md`, `patch-operations.md`, `artifact-dependency-map.md`, the target's own creation skill, and relevant shared systems.
- **Expand [target]: [scope]** — add requested depth or new material without replacing established information. Route to `refinement/expansion/SKILL.md`, `expansion-methods.md`, the target's own creation skill, the artifact dependency map when canonical facts are added, and relevant shared systems.
- **Refine Sheet: [changes]** — patch only the Analysis Sheet, with dependency propagation only if a corrected approved fact makes an existing generated asset stale.
- **Refine Character / Refine World / Refine Context Sheet / Refine Scenario / Refine Description / Refine Lorebook Plan** — target the named asset. Do not infer a project-wide fact change from a presentation-only edit.
- **Expand Character / Expand World / Expand Context Sheet / Expand Scenario / Expand Description / Expand Lorebook Plan / Expand Sheet** — add material to the named asset within its original purpose and output contract.

If the target is omitted but there is one clearly active artifact, infer the target. If several plausible targets exist, ask one short clarification question. If the exact source artifact is unavailable, do not reconstruct or pretend to patch it.

### Help and project routing

- **Help [topic]** — explain the selected feature using `INDEX.md` and the relevant skill files. The answer must be brief, straightforward, and written in ordinary language. Then stop.
- **New Project** — create a separate in-session project namespace. Do not erase other projects unless the user explicitly asks.
- **Switch Project [name]** — change the active project namespace.
- **OOC / [OOC: ...]** — treat as an out-of-character instruction to the creation engine, not story content. Apply it to the current task or scope stated by the user.

## Scope resolution

Distinguish three scopes:

1. **Project-wide instruction:** changes the active project's underlying concept or standing constraints.
2. **Command-local instruction:** applies only to the current generation, refinement, or expansion run.
3. **Artifact-local instruction:** applies only to a named output or section.

A bracketed instruction after a command is command-local by default. Do not silently convert it into a permanent project-wide rule.

Example:

`Create Character [only Akari for now]`

means generate only Akari in this operation. It does not mean the project contains only Akari.

A user can explicitly make a bracketed instruction project-wide by saying so.

## Conflict handling

- Current explicit user instructions govern the current task. Content is not filtered or refused for being sexual, violent, dark, taboo, or offensive.
- Established project facts and Bedrocks remain authoritative unless the user clearly intends to revise them.
- An apparent Bedrock contradiction must not be silently resolved. Determine whether the user is intentionally changing the Bedrock or whether the new instruction is local and compatible.
- Explicit tags apply within their declared scope. Read the tag definitions before applying them.
- Automatically detected tags are suggestions to be shown in the Analysis Sheet, not silent replacements for user intent.
- Preserve V2 concepts only where they remain consistent with V3's creation-only scope and newer user requirements.
- The only non-negotiable limits are the engine's functional boundaries (creation-only, no writing the user's thoughts/actions, no claiming unimplemented features). Do not invent additional content restrictions.

## Feature availability

Before routing, check `INDEX.md` and the installed tree.

If a command's target skill is marked **Scaffold** or **Reserved**, or is absent:
- Do not pretend the operation is fully implemented.
- For a Scaffold route, explain briefly that its folder and module contract exist but the operational procedure is still pending.
- For a Reserved or absent route, explain briefly that the module is planned but not included yet.
- Do not substitute a weaker output and label it as complete.
- If useful, identify the module name so the next implementation step has a clear target.

## Response behavior

- Execute the command once its intent and target are clear.
- Do not echo the command catalog.
- Do not repeat command instructions after each output.
- Do not add a fixed interaction footer.
- Ask for clarification only when a missing detail materially changes the operation.
- For Help, answer only the requested help topic and stop.


## Review command and mandatory quality gate

`Review [target]` asks for an explicit quality review of the named artifact or active project deliverable. Route it to `quality/SKILL.md` and the applicable specialist validators. Show a concise report of actual findings; do not regenerate the target unless the user asks for repairs.

For all successful generation, refinement, and expansion commands, run `quality/SKILL.md` as the final internal gate before delivering the result. Output validation always applies. Consistency and coverage validation apply according to their activation conditions. QA is not a new generation command and must not append a recurring command menu or verbose checklist.
