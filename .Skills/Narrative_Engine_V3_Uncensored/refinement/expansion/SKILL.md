---
name: narrative-engine-expansion
description: Adds requested depth, detail, connective information, and new sections to existing project artifacts while preserving established content.
status: implemented
stage: 12
---

# Expansion — Operational System

## 1. Purpose

Expansion develops an existing project component by adding requested detail, layers, examples, behavior, context, or new material. It does not reset or replace the existing work.

The governing rule from V2 remains:

**Expansion adds layers. Expansion does NOT replace layers.**

Preserve established traits, habits, lore, relationships, world details, and dynamics unless the user explicitly instructs otherwise.

Expansion differs from refinement:
- Refinement changes a targeted existing element.
- Expansion adds new depth or material around the existing element.
- A request that both corrects old information and adds new material uses both systems: patch the correction first, then expand the corrected version.

## 2. Activation

Activate for:
- `Expand [target]: [scope]`;
- `Expand Character [name]: [scope]`;
- `Expand World: [scope]`;
- `Expand Context Sheet: [scope]`;
- `Expand Scenario: [scope]`;
- `Expand Description: [scope]`;
- `Expand Lorebook Plan: [scope]`;
- `Expand Sheet: [scope]`;
- `Expand: [scope]` when one clearly active artifact exists;
- an unambiguous natural-language request to add depth or further develop an existing asset.

If the target is omitted and one artifact is clearly active, infer it. If several targets are plausible, ask one concise clarification question.

## 3. Required skill loading

Load:

1. This skill and `expansion-methods.md`.
2. The target artifact's own generation skill.
3. `shared-systems/information-transfer/SKILL.md`.
4. `shared-systems/bedrocks/SKILL.md` when relevant.
5. `shared-systems/adaptive-sections/SKILL.md` when a new section or structural addition is needed.
6. `shared-systems/evidence-and-inference/SKILL.md` when proposed additions depend on uncertain evidence or inference.
7. `shared-systems/tags/SKILL.md` and only relevant individual tag definitions when tags affect expansion.
8. `../patch-refinement/artifact-dependency-map.md` when the new content changes established project information that other existing outputs may contain.
9. `core/project-isolation/SKILL.md` when several projects exist in the conversation.

Do not load unrelated modules. Do not re-run full analysis unless the user asks or the available context is insufficient to expand safely.

## 4. Resolve target and expansion scope

Determine:
- which active project is being expanded;
- which artifact or component is the target;
- what dimension or gap the user wants developed;
- how much depth is desired;
- whether the addition is a supporting detail, a new section, or a major concept development;
- what existing information must remain unchanged;
- whether the new material is intended as canon or as an optional proposal.

Examples of expansion dimensions:
- deeper explanation of an existing trait;
- concrete behaviors and examples that make an established personality operational;
- richer physical detail within available evidence;
- additional world rules, institutions, customs, locations, or causal detail;
- stronger relationship nuance and interaction patterns;
- clearer plot progression, obstacles, stakes, or connective events;
- additional lorebook entries or richer implementation briefs;
- deeper narrator-facing context in the Context Sheet;
- more atmosphere or playable detail in an existing Scenario opening.

A broad `Expand [target]` request permits useful development within that target, guided by narrative gravity and existing priorities. It does not authorize unrelated worldbuilding or arbitrary new plotlines.

## 5. Expansion procedure — establish the existing version as the foundation

Before adding anything, inspect the exact current target artifact and the relevant approved project sources.

- Treat the latest approved target as the foundation.
- Preserve every existing information unit unless the user explicitly allows a change.
- Do not reinterpret the whole concept from scratch.
- Do not remove earlier layers because a new idea appears more interesting.
- Do not assume an earlier expansion supersedes an existing trait or detail.
- If the current target artifact is unavailable, do not reconstruct it from vague memory. Ask for the exact source or clearly limit the output to a standalone proposed addition.

## 6. Select a useful expansion method

Choose one or more appropriate methods from `expansion-methods.md`:

- **Depth expansion:** explain an existing detail more fully.
- **Behavioral expansion:** show how an established trait appears in decisions, speech, habits, and reactions.
- **Contextual expansion:** add the relevant background or causal context needed to understand a fact.
- **Connective expansion:** clarify relationships between already established pieces.
- **Structural expansion:** add a new section when no existing section can hold the new material correctly.
- **Breadth expansion:** add relevant supporting entities, locations, examples, or systems when the user requests broader scope.
- **Operational expansion:** specify how a system, rule, ability, institution, or process works in practice.
- **Narrative expansion:** develop progression opportunities, tension, stakes, or hooks without taking over the entire plot.

Do not apply every method to every request. Choose only the ones that fit.

## 7. Controlled development and evidence

Use this priority:

1. Explicit user instruction for this expansion.
2. Established and approved project facts.
3. Strongly supported information from supplied sources.
4. Concept logic and existing design implications.
5. Creative proposals, only within the scope the user authorized.

Without the **Improvise** tag, do not fill every unknown with invention. If a major creative decision is necessary and not supported, ask or present it as a clearly labeled proposal rather than silently making it canon.

With **Improvise** active in the relevant scope:
- proactively complete gaps required for a coherent and useful result;
- add suitable supporting information and connective details;
- do not include a `Missing Elements` section in the relevant analysis output;
- preserve explicit facts and Bedrocks;
- do not disguise a premise-changing invention as a minor detail.

The **Detailed** tag may increase explanatory depth only within its tag scope. The word “detailed” in ordinary conversation is not automatically equivalent to activating the tag, although a direct instruction can request a detailed response for one task.

The **Uncensored**, **Open Interaction**, and **Open World** tags affect expansion only in their defined scope. Do not let a scoped tag spread to unrelated characters, places, or project outputs.

## 8. Preserve the existing layers

When expanding:

- retain all existing traits, habits, lore, relationships, world facts, and dynamics;
- add new details as additional layers rather than replacements;
- avoid introducing contradictions with current facts or Bedrocks;
- distinguish a character's stable trait from a situational reaction;
- distinguish established history from a possible future development;
- distinguish a current relationship state from a desired progression;
- do not make a possibility sound like an event that has already happened;
- do not turn a temporary Scenario detail into permanent canon unless the user says so.

If the requested expansion inherently changes an old detail, route that portion through Patch Refinement first. Expansion itself must not silently replace established content.

## 9. Avoid padding and uncontrolled growth

Expansion should increase usefulness, not merely length.

Do not:
- repeat the same fact in different wording to create volume;
- add generic adjectives without explaining what makes the detail specific;
- introduce unrelated history, trauma, secrets, factions, magic systems, or subplots;
- inflate tertiary details beyond the narrative priority they deserve;
- create extra cast members or locations merely because Open Interaction/Open World permits them;
- add a large new system when a small clarification would solve the problem;
- expand every section just because the target is a large document.

Use narrative gravity and primary/secondary/tertiary priorities to allocate depth. Expand the user's requested focus first.

## 10. Section and information placement

- Add material to the existing correct section when one fits.
- Create a new section when necessary; do not force a novel concept into an unsuitable heading.
- Preserve section responsibility and keep unrelated sections untouched.
- Avoid duplicating information already expressed clearly in another section.
- Use Information Transfer to identify existing dependent outputs that also need the newly established fact.
- The Context Sheet should contain all narrator-relevant approved project details, but do not automatically regenerate it in full; patch only the affected passages.
- The Lorebook Plan should receive an update when the expanded fact changes planned modular knowledge or behavior.

## 11. Canon status and propagation

Determine whether the added material is:

- **Requested canon:** the user directly asked to add it as an established project fact.
- **Authorized completion:** Improvise or another explicit instruction authorizes the engine to fill the gap in this scope.
- **Proposal:** an optional development idea not yet approved as canon.

Do not silently turn a proposal into canon. Clearly label proposals in the output or keep them separate from the finished artifact.

If new canonical information affects existing dependent outputs, use `artifact-dependency-map.md` and patch only stale or incomplete passages. Presentation-only additions remain local.

## 12. Output contract

- Default to returning the expanded target artifact, with all previous content preserved and the new material integrated naturally.
- If the artifact is very large, provide exact insertion-ready sections and identify their placement; do not summarize or replace omitted existing content.
- If the user asks for additions only, output only the new material and its insertion location.
- If the user asks for ideas rather than applying changes, keep them as proposals and do not merge them into established canon.
- Never silently rewrite the target or dependent artifacts beyond the requested expansion.

## 13. Correct and incorrect behavior examples

### Example A — expand a defined personality trait

Existing fact: a character is blunt and impatient.

User request: `Expand Character [show how her impatience appears in conversations and stressful situations]`.

Correct behavior: add specific speech patterns, observable reactions, and situational differences that express the established impatience. Preserve the rest of the personality and do not invent a trauma explanation.

Incorrect behavior: replace “blunt and impatient” with a different personality, add unrelated secrets, or make her hostile in every interaction regardless of context.

### Example B — expand an unusual world mechanic

User request: `Expand World [explain how memory taxation affects ordinary citizens]`.

Correct behavior: add a focused section explaining the practical mechanism, consequences, and relevant examples, consistent with established world rules.

Incorrect behavior: create a complete unrelated government, new continent, and main quest merely because the world has room to expand.

### Example C — proposal versus canon

User request: `Give me some possible ways to deepen the rivalry`.

Correct behavior: present optional development ideas as proposals, separate from the established relationship sheet.

Incorrect behavior: silently write one proposed betrayal or secret into the canonical relationship history.

## 14. Completion validation

- [ ] Correct project and target were selected.
- [ ] The expansion follows the user's named scope and priorities.
- [ ] Existing material remains present and unchanged except where an explicitly paired refinement was required.
- [ ] New information is relevant, specific, and non-redundant.
- [ ] Evidence, inference, and authorization boundaries were respected.
- [ ] Bedrocks and tag scopes remain intact.
- [ ] New sections were created when necessary rather than forcing unsuitable headings.
- [ ] Existing dependent outputs were inspected when the expansion added canonical facts.
- [ ] The output remains the same artifact type and performs its original purpose.

Do not print this checklist unless requested.
