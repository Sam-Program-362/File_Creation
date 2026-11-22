---
name: narrative-engine-lorebook-planning
description: |
  Design a project-specific Lorebook Plan as a detailed handoff for a separate
  Lorebook Creator. Classifies requirements as main-context information,
  normal keyword/constant Lorebook entries, or JanitorAI Advanced Script
  requirements. Never creates import-ready JSON entries or JavaScript.
---

# Phase 11 — Lorebook Planning System

## 1. Purpose

Create a **Lorebook Plan**: a complete, project-aware implementation brief that another AI or implementer can use to create the actual Lorebooks or Advanced Scripts.

The plan is not a list of entry titles. It must explain the problem each proposed component solves, why it belongs in a Lorebook or script, what information or behavior it must contain, when it should activate, which source facts and Bedrocks it must preserve, how it relates to the rest of the system, and how the downstream creator should test it.

**V3 is the planner, not the creator.** This module does not output ready-to-import JSON, executable JavaScript, or finished script payloads. It outputs structured Markdown specifications and handoff instructions only.

## 2. Activation and command

Activate when the user invokes `Plan Lorebooks`, `Create Lorebook Plan`, or clearly requests a plan for modular Lorebook / World Info / Advanced Script implementation.

Command-local instructions may specify a platform, scope, desired modules, characters, systems, or planning constraints. Treat them as local to this planning run unless the user explicitly makes them project-wide.

If the user explicitly asks for actual JSON or JavaScript, state briefly that this V3 module produces a plan only. Do not quietly output code under the name of a plan. The user may pass the handoff to a separate Lorebook Creator.

## 3. Scope and non-goals

### Included

- Determine whether Lorebooks or Advanced Scripts materially help the project.
- Separate always-needed project context from conditional / trigger-based material.
- Choose and justify normal Lorebook entries versus Advanced Script requirements.
- Plan one or more lorebooks and their entry groups.
- Produce detailed entry-by-entry specifications.
- Describe Advanced Script behavior without writing the script.
- Map project facts, tags, character voice, Bedrocks, and source context into the handoff.
- Specify activation tests, non-activation tests, conflict tests, and platform validation needs.

### Excluded

- Creating the actual JSON array or entry objects.
- Writing, repairing, or validating executable JavaScript.
- Claiming that a proposed field, API, or runtime behavior works on an unverified platform/version.
- Creating lorebook content unrelated to the approved project.
- Replacing the Context Sheet or Character / World Sheets with a large Lorebook catalogue.
- Adding entries merely to make the plan appear substantial.

## 4. Required source loading

Before planning, read the following project modules as applicable:

1. `INDEX.md` and the active project's identity / isolation state.
2. `shared-systems/information-transfer/SKILL.md`.
3. `shared-systems/bedrocks/SKILL.md`.
4. `shared-systems/tags/SKILL.md` and only the applicable individual tag definitions.
5. The current approved Analysis Sheet, Context Sheet, Character Sheets, World Sheet, relationship / plot assets, and explicit user instructions that exist in the active project.
6. The directly readable source references in `references/lorebook-creator/`:
   - `SKILL.md`
   - `references/lorebook-creator/assets/full-system-overview.md`
   - `references/lorebook-creator/references/entry-schema.md`
   - `references/lorebook-creator/references/content-patterns.md`
   - `references/lorebook-creator/references/advanced-script-patterns.md`

The original archive is retained at the package-root path `../../references/lorebook-creator-skill.zip`. The extracted copies are provided so the planner can consult individual reference documents without reinterpreting a compressed package.

Do not infer a missing Context Sheet, character, platform, or world asset exists. Use the approved material actually available. An early plan can be generated from partial project material, but unresolved implementation dependencies must be stated.

## 5. Source and authority handling

Use this precedence for the active planning run:

1. Current explicit user instructions for this Lorebook Plan.
2. Current approved project facts and deliberate revisions.
3. Confirmed Bedrocks, preserving their scope unless the user clearly revises them.
4. Approved Context Sheet and current Character / World / relationship / plot assets.
5. Approved Analysis Sheet findings.
6. Supported evidence and project references.
7. Clearly labeled proposals made by this planning run.

When two approved assets disagree, identify the actual conflict and its affected lorebook decision. Do not silently choose one. If the conflict changes an activation condition, character behavior, setting rule, or Bedrock, resolve it before finalizing or explicitly mark the affected part as blocked pending confirmation.

Keep information status clear internally: established, supported, inferred, proposed, or unknown. Do not turn speculative ideas into canonical Lorebook facts. If `Improvise` applies, fill reasonable gaps needed for a coherent handoff while preserving established facts and Bedrocks; do not include a `Missing Elements` section in that mode. Otherwise, expose only the unresolved gaps that materially affect implementation.

## 6. Planning procedure

Follow the sequence below. Do not jump directly from the project description to entry titles.

### Step 1 — Resolve the planning target

Identify:

- Active project and its boundaries.
- What the user wants modularized: knowledge, world facts, character behavior, a personality library, act / scene guidance, dynamic rules, narrative protocol, or conditional behavior.
- Whether the target is the whole project or a selected subset.
- The target platform, if supplied.
- Whether the user wants normal Lorebooks, Advanced Scripts, or an engine recommendation.

Do not assume the entire project must be placed in Lorebooks. Plan only the requirements that benefit from modular activation or separate editing.

### Step 2 — Build a requirement inventory

Break the request and approved project material into discrete information / behavior requirements. Each requirement should have a clear owner and purpose.

For each requirement, record internally:

- Requirement ID or short stable label.
- What the downstream AI needs to know or do.
- Which character, relationship, world system, location, event, or project-wide concern it belongs to.
- Source and approval status.
- Applicable Bedrocks and tags.
- Whether it is always relevant, conditionally relevant, or activated by a detectable event / state.
- What failure occurs if it is omitted or activated at the wrong time.

Do not make an entry for every sentence. Group requirements that serve one coherent activation purpose; split requirements that need different triggers, lifetimes, priority, or scope.

### Step 3 — Decide what belongs outside the Lorebook system

Before choosing entry types, classify information into one of these destinations:

**A. Main project documents** — stable, central information already needed throughout the roleplay, such as premise, core cast, defining relationships, base setting, and essential context. Keep it in the Context Sheet / Character Sheet / World Sheet when it belongs there. Do not duplicate the entire Context Sheet into constant entries.

**B. Normal Lorebook / World Info entries** — knowledge or instructions that should be injected when relevant keywords are mentioned, or that must remain constantly available but do not have reliable trigger words. Suitable examples from the source skill include world facts, personality libraries, act guides, dynamic rules, and fidelity rules.

**C. Advanced Script behavior** — requirements that depend on conditional detection, message counts, random selection, multi-condition logic, changing state, separate injection destinations, or cleanup when a condition ends.

**D. Not suitable / not needed** — material that is already adequately handled by the main documents, requires unsupported runtime behavior, or has no clear activation/use case. Explain a meaningful exclusion rather than inventing an entry.

A Lorebook Plan may legitimately conclude that no Lorebook or Advanced Script is needed. State why and identify which main project documents already cover the requirement.

### Step 4 — Choose implementation type for each requirement

Use the source Lorebook Creator's decision rules:

**Normal Lorebook / Normal Script (JSON)** is the default choice when:
- a keyword mention should inject relevant information or rules;
- multiple independent entries can activate separately;
- the project needs editable knowledge, personality overlays, act guides, world facts, dynamic rules, or static protocols;
- a rule must always be present and has no reliable trigger keywords, using a constant entry where appropriate.

**Advanced Script (JavaScript)** is appropriate when:
- a condition must be detected from recent chat content or multiple signals;
- a temporary instruction must be injected only while a state is true and removed when the state ends;
- different material must be injected into `personality` versus `scenario`;
- message-count gates, weighted random events, stateful behavior, or complex regular-expression detection are required;
- one message needs to be scanned for a set of patterns and then trigger a response.

**Platform constraint from the supplied source:** Normal Lorebook JSON is described for JanitorAI and SillyTavern-style World Info. Advanced JavaScript is described as a JanitorAI system. Do not claim Advanced Script compatibility with SillyTavern on the basis of this source. If the user names another platform or version, mark support as unverified and require the downstream creator to validate the actual runtime.

If the platform is unknown, make the recommendation conditional. Do not present a platform-specific Advanced Script plan as universally deployable.

When the user does not specify a type, use the above decision rules. The source skill generally recommends Advanced Script for complex behavioral enforcement and normal Lorebooks for knowledge / act / personality libraries. Prefer the simpler normal Lorebook when it can reliably satisfy the requirement; do not choose Advanced Script merely because it sounds more powerful.

### Step 5 — Decide constant versus triggered behavior

For each proposed normal Lorebook entry:

- Recommend **constant** behavior only when the rule must be available all the time and has no reliable keyword trigger.
- Recommend **keyword-triggered** behavior when the information matters only in identifiable situations or when the relevant subject is mentioned.
- Do not make a rule constant merely because it is important. Importance and activation frequency are separate decisions.
- Do not rely on a keyword trigger for a rule that must never be forgotten if no reliable trigger exists.
- Do not make a large knowledge library constant when it can be activated selectively.
- Avoid duplicating a complete Context Sheet in constant Lorebook entries.

A Bedrock is a core project invariant, but it is not automatically a separate Lorebook entry. Keep it visible in the relevant main documents and Context Sheet. Recommend constant or repeated Lorebook coverage only where the downstream architecture needs the invariant injected independently of those documents or in a specific conditional context.

### Step 6 — Design lorebook boundaries

Choose the number of Lorebooks based on operational separation, not a fixed quota.

Separate Lorebooks when they have meaningfully different:
- subject domains or owners;
- activation patterns;
- entry maintenance / editing responsibilities;
- character or world scopes;
- priority / insertion relationships;
- platform or runtime constraints.

Keep entries together when they form one coherent library and can be maintained and activated safely together.

Avoid both extremes:
- **Monolithic Lorebook:** unrelated entries with overlapping triggers and unclear responsibilities.
- **Over-fragmentation:** many tiny Lorebooks that make activation, setup, and maintenance harder without a practical benefit.

For each Lorebook define a clear boundary, intended purpose, what it owns, what remains in main project documents, and what it must not duplicate.

### Step 7 — Design each normal Lorebook entry brief

Each entry brief must be sufficiently complete for a separate creator to write the eventual entry without reconstructing the source conversation.

For every proposed entry, specify:

1. **Identity:** entry name, category, short comment / purpose label.
2. **Problem solved:** what failure, omission, or missing knowledge this entry addresses.
3. **Intended effect:** what the downstream AI should know, preserve, or do when the entry is active.
4. **Content direction:** all required facts, behavioral details, examples, boundaries, and anti-default instructions that belong in the eventual entry. Be concrete; “follow personality” alone is insufficient.
5. **Scope:** project-wide, character-specific, relationship-specific, world-specific, location-specific, event-specific, or other custom scope.
6. **Activation mode:** constant or keyword-triggered, with rationale.
7. **Primary keys:** specific words / phrases likely to occur when the entry is needed.
8. **Secondary keys / selective activation:** any required co-occurrence or selective condition, with platform support to be confirmed if the source does not define the exact semantics.
9. **Matching recommendations:** case sensitivity, whole-word matching, key-match priority, and related settings only when their intended values are clear.
10. **Message gating:** whether a minimum message count is needed; explain why. Do not invent a gate.
11. **Priority recommendation:** select a source-informed band and explain the entry's relative importance.
12. **Insertion relationship:** which related entries should be inserted earlier or later, using relative order. The source schema says lower `insertion_order` values are earlier; actual runtime behavior must be verified.
13. **Probability / inclusion behavior:** state whether probabilistic selection or inclusion grouping is genuinely required. Do not invent weights or values without a reason.
14. **Dependencies and exclusions:** entries that must be active together, must not co-activate, or should not override each other.
15. **Bedrocks and source facts:** list relevant confirmed Bedrock points in the plan's Bedrocks area and explain separately in the entry brief how the eventual entry must preserve them. Do not put instructions inside the Bedrocks list itself.
16. **Voice / personality filters:** where relevant, state how the content should vary by the defined character rather than use a generic template.
17. **Forbidden defaults / failure modes:** list specific behaviors to prevent where the project needs them.
18. **Test cases:** positive triggers, negative triggers, boundary cases, overlap cases, and checks for correct content activation.

If a field is unknown, mark it **Downstream creator to determine / platform validation required**. Do not fill it with an arbitrary default just to make the brief look complete.

### Step 8 — Design Advanced Script handoff briefs

For each Advanced Script requirement, describe the behavior in implementation-neutral language. Do not write JavaScript, code-like pseudocode, or a runnable skeleton.

Specify:

- Script name and purpose.
- Target platform; source-supported default is JanitorAI only.
- Triggering condition and the exact conceptual state to detect.
- Detection inputs needed. The supplied reference describes `context.chat.last_message`, `context.chat.message_count`, `context.chat.last_messages`, and `context.chat.user_name`; it also describes reading character `personality` and `scenario`.
- Whether detection uses keyword lists, regular-expression patterns, message count, multiple conditions, weighted random selection, or another stated mechanism.
- Positive and negative detection examples, false-positive risks, and false-negative risks.
- Any threshold, cooldown, or one-time / repeated behavior requirement, but only when specified by the project.
- Injection destination: `personality`, `scenario`, or both, with the distinct content purpose for each destination.
- Cleanup behavior when the triggering condition ends.
- Duplicate-prevention requirement. The source pattern uses a unique marker to detect an existing injection before adding it again.
- Empty/missing context safeguards. The source skeleton checks that the context, chat, and character exist and ignores an empty last message.
- Whether the same injection must be removed exactly, and what must remain untouched.
- Interaction with normal Lorebook entries and the main Context Sheet.
- Runtime capability and version checks the downstream creator must perform.
- Test matrix: trigger, continue, stop, cleanup, repeat, no context, empty message, overlapping conditions, and false-positive terms.

The supplied reference notes that some environments may allow `example_dialogs`, but it is not guaranteed. Treat it as optional platform-specific capability, not a default destination.

### Step 9 — Select only relevant content patterns

Consult `references/lorebook-creator/references/content-patterns.md`. The source patterns are options, not mandatory boilerplate.

Use a pattern only when the project requirement calls for it:

- **Anti-soft / anti-default:** specify unwanted generic defaults and the character-appropriate behavior that replaces them.
- **Personality filters:** describe how the same situation should be expressed by different personality types or by the actual defined character.
- **Non-escalation:** state that a moment does not automatically escalate into another act, confession, or outcome when that distinction matters to the project.
- **Time continuity:** preserve established time of day and show passage only when it actually occurs, when time progression matters.
- **Dominance preservation:** preserve a defined power / dominance dynamic; do not apply this pattern where such a dynamic is absent.
- **Progression mandate:** require a meaningful change in action, power, environment, consequence, or time when narrative momentum is specifically required.
- **Aftercare-personality matching:** keep aftermath behavior consistent with established personality when relevant; never force generic softness.

The source skill also emphasizes character fidelity, practical specificity, anti-default content, narrative momentum, and first-class handling of male and futanari contexts where relevant. Preserve these directions when they apply to the user's actual project, but do not inject sexual, romantic, dominance, or other specialized content patterns into unrelated projects.

The source skill describes uncensored / explicit handling for sexual, power, or dark themes. Preserve the user's requested tone and the applicable `Uncensored` tag within platform and policy limits; do not sanitize character voice by default, and do not force explicitness where the project does not call for it.

### Step 10 — Set priority recommendations transparently

Use the Notion plan's source-derived default bands as the initial planning vocabulary:

- **101–95:** core locks and absolute rules.
- **94–85:** personality overlays, emotional temperature, narrative momentum.
- **84–75:** major acts and dynamics.
- **74–65:** advanced / niche act material.
- **Below 65:** flavor and optional detail.

The supplied `references/lorebook-creator/references/entry-schema.md` uses a more granular alternative: 101–95 absolute locks; 94–90 core narrative / personality protection; 89–80 strong supporting systems; 79–65 act and dynamic entries; below 65 niche or low-frequency flavor.

Because the supplied package contains these two related but non-identical band descriptions, do not claim that one exact band taxonomy is universal. Use the Notion bands as V3's default labels, state the rationale for each recommendation, and tell the downstream creator to verify the target platform's actual priority semantics. A plan may give a relative priority rank / tier instead of a numeric value when platform support is uncertain.

### Step 11 — Check completeness and collisions

Run the following internal checks:

- Every planned entry solves a concrete requirement.
- Every requirement has an explicit destination: main project documents, normal Lorebook, Advanced Script, or intentionally excluded.
- Every trigger is likely to appear when needed and is not so broad that it fires constantly by accident.
- Related entries do not compete for the same trigger without a stated reason.
- Constant entries are truly always-needed and not simply “important.”
- Conditional instructions have clear start and stop conditions.
- Advanced Script injections have cleanup and duplicate-prevention requirements.
- Character-specific content respects voice, psychology, and relationship dynamics.
- All applicable Bedrocks are preserved and correctly scoped.
- No inference is presented as approved canon.
- No unrelated content patterns are included.
- The Context Sheet remains the central project handoff; the Lorebook system supplements rather than replaces it.

### Step 12 — Create the implementation handoff

Generate a structured Markdown document with the output contract below. The handoff must be self-contained enough for a separate creator to implement without reopening the original conversation.

Do not output the actual JSON entry objects or JavaScript. Do not include code fences containing runnable or near-runnable code. Field names may be named in the planning specification; values that require platform implementation should be labeled as recommendations or left for validation.

## 7. Lorebook Plan output contract

Use these sections where relevant. Add custom sections when the project requires them; omit irrelevant sections rather than printing empty headings.

### 1. Project and implementation overview

- Project name / identifier as supplied.
- Concise, accurate project context necessary to understand the plan.
- What the Lorebook system is meant to solve.
- Target platform and version, or explicit unknown / validation required.
- Recommended implementation types.
- Summary of proposed Lorebooks and Advanced Scripts.
- Overall architecture rationale.

### 2. Main-document versus Lorebook allocation

Explain what remains in the Context Sheet, Character Sheets, and World Sheet, what moves into a conditional or constant entry, and why. Identify deliberate exclusions and duplicated-content risks.

### 3. Lorebook architecture

For each proposed Lorebook:
- Name.
- Purpose.
- Scope and ownership boundary.
- Intended platform / format.
- Entry families or categories.
- Activation philosophy.
- What it must not duplicate or override.
- Dependencies on other Lorebooks or main documents.

### 4. Entry-by-entry briefs

Provide a complete brief for every planned entry using the Step 7 specification. Entry briefs may use custom subheadings and tables, but must include purpose, content direction, scope, activation, triggers, priority / insertion relationships, dependencies, Bedrocks, and tests as applicable.

### 5. Advanced Script handoff briefs

Include only when actual conditional / stateful behavior is required. Use the Step 8 specification. Describe behavior and requirements, not JavaScript.

### 6. Shared interaction and conflict rules

Explain how entries and scripts interact, resolve priority conflicts, avoid duplicate injection, preserve character fidelity, and avoid contradictions. Do not invent runtime precedence semantics; identify where the implementer must validate them.

### 7. Bedrocks

If applicable, create a dedicated Bedrocks section containing only the confirmed Bedrock points as a clean bullet list. No explanations or AI meta-instructions inside this section. Put implementation implications in the relevant entry briefs or a separate section.

### 8. Platform assumptions and validation requirements

State the supported/assumed platform, schema fields that require confirmation, unsupported or unknown runtime features, and any needed compatibility tests.

### 9. Build and test handoff

Give the downstream creator a practical build order and tests for positive triggers, non-triggers, overlaps, priority behavior, constant entries, Advanced Script activation/cleanup, character voice fidelity, and Bedrock integrity.

### 10. Deferred items / unresolved decisions

Only include genuine blockers or choices that cannot safely be inferred. If `Improvise` applies, resolve reasonable gaps and omit a `Missing Elements` section; do not hide platform compatibility uncertainty.

## 8. Source technical reference — use without fabricating semantics

The supplied normal-entry schema lists these fields. The planner may recommend settings when justified, but the downstream creator is responsible for constructing and validating the actual object:

- `activationMode`, `activationScript`
- `case_sensitive`
- `category`, `comment`
- `constant`
- `content`, `enabled`
- `extensions`, `groupWeight`
- `id`, `inclusionGroupRaw`
- `insertion_order`
- `key`, `keysecondary`, `keysRaw`, `keysecondaryRaw`, `keywordsRaw`
- `keyMatchPriority`, `matchWholeWords`
- `minMessages`
- `name`
- `prioritizeInclusion`
- `priority`, `probability`
- `selectiveLogic`
- `tags`

Do not invent exact meanings or accepted enum values for fields the supplied source does not explain. In particular, mark platform-specific semantics of `selectiveLogic`, inclusion groups, activation scripts, and extension data for downstream validation.

The source example shows typical values such as standard activation mode, empty activation script for ordinary entries, case-insensitive matching, enabled entries, empty extensions, primary and secondary key arrays, and human-readable comments. These are illustrative defaults, not a guarantee that every target should use them.

For Advanced Scripts, the source identifies the following read paths: chat `last_message`, `message_count`, `last_messages`, and `user_name`; character `personality` and `scenario`. It describes writing injected text to `personality` and `scenario`, with `example_dialogs` only in some environments. Do not promise access or write support beyond what the target runtime documents.

## 9. Quality and completion checklist

Before returning the plan, verify:

- [ ] The plan is grounded in the active project's approved material.
- [ ] The plan answers whether a Lorebook system is needed at all.
- [ ] Main-context information is not needlessly duplicated into Lorebooks.
- [ ] Every Lorebook has a clear purpose and scope.
- [ ] Every entry has a concrete use case and sufficiently detailed content direction.
- [ ] Constant versus keyword activation is justified per entry.
- [ ] Trigger keys are specific, useful, and tested for accidental matches.
- [ ] Advanced Script is used only where conditional / stateful logic requires it.
- [ ] Advanced Script is not presented as SillyTavern-compatible based only on this source.
- [ ] Injection destinations, cleanup, and duplicate-prevention requirements are specified where relevant.
- [ ] Priority recommendations acknowledge source band differences and platform validation.
- [ ] Relevant content patterns are selected only when appropriate.
- [ ] Character voice, world facts, source status, tags, and Bedrocks are preserved.
- [ ] The Bedrocks section, if present, contains only points.
- [ ] Dependencies, collisions, and exclusions are documented.
- [ ] The downstream creator has an actionable test plan.
- [ ] No import-ready JSON or executable / near-executable JavaScript is included.
- [ ] Only the Lorebook Plan was generated; no unrelated asset was silently regenerated.

## 10. Final response behavior

Output the Lorebook Plan itself. A short preface may identify the confirmed target platform or a material compatibility caveat. Do not add an end-of-message command menu. Do not claim the Lorebook has been created or imported. Stop when the handoff is complete.
