---
name: narrative-engine-bedrocks
description: |
  Defines Bedrocks: explicit, non-negotiable core invariants of a narrative
  concept, character, plot, world, or project, and how they are preserved.
---

# Bedrocks System

## Purpose

A **Bedrock** is a core invariant of the project: a rule, condition, or defining truth that the generated project material and downstream narrative must not contradict.

Bedrocks capture what must remain true for the concept to remain itself. They are stronger than ordinary preferences, suggestions, themes, or possible directions.

## Output format

Whenever an artifact needs to expose Bedrocks, use a dedicated section containing only the actual Bedrock statements as a list.

Example:

### Bedrocks
- Akari must not talk in front of Ashli.
- The king must never kill any citizen.
- The colossal must never walk faster than 2 km/h.

Do not add explanations, implementation instructions, AI meta-instructions, priority commentary, or examples inside the Bedrocks section. Keep it to the points themselves.

The Bedrocks heading may be omitted from an artifact when no Bedrocks apply. Do not create an empty Bedrocks section.

## What qualifies

A point qualifies as a Bedrock when:
- the user explicitly identifies it as a core rule, invariant, absolute condition, or non-negotiable concept rule; or
- the user clearly establishes it as a defining condition that the project must preserve.

Do not promote ordinary preferences, themes, tendencies, likely outcomes, or unsupported inferences into Bedrocks.

If the engine suspects a point may be a Bedrock but the user has not established that status, mark it as a **Bedrock candidate** in the Analysis Sheet. A candidate is not yet a confirmed Bedrock.

## Scope

Every Bedrock has an implied or explicit scope. Preserve that scope:

- **Project-wide:** applies to the entire concept.
- **Character-specific:** applies to one named character.
- **Relationship-specific:** applies to a defined relationship or interaction.
- **World-specific:** applies to a world rule, location, institution, species, or setting element.
- **Scenario-specific:** applies only to a particular opening or scene.

Do not broaden a local Bedrock into a project-wide rule.

## Propagation

Carry each applicable Bedrock into every requested output where the downstream reader needs it:

- Character Sheet, when it constrains that character.
- World Sheet, when it constrains the setting or its inhabitants.
- Context Sheet, which must collect all project-relevant Bedrocks in a clear dedicated section.
- Scenario starting message(s), which must not contradict any applicable Bedrock.
- Lorebook Plan, where the downstream creator needs to preserve the invariant in one or more entries or scripts.
- Other custom project documents when relevant.

Do not blindly copy every Bedrock into every document. Use scope and downstream relevance. The Context Sheet should be the integrated reference point.

## Operational enforcement

A Bedrock is not decorative text. Before finalizing an output:

1. Identify the Bedrocks that apply to the requested artifact.
2. Check the content against each one.
3. Remove or revise any conflicting generated detail.
4. Confirm that the Bedrock has not been weakened, paraphrased into a different meaning, or lost in transfer.
5. Keep the visible Bedrocks section clean: list only.

## Conflicts and revisions

If a new user instruction appears to conflict with an established Bedrock:

- Do not silently ignore either instruction.
- Determine whether the user intends to revise or remove the Bedrock.
- If the intent is clear, apply the revision and update affected outputs.
- If the intent is unclear and the conflict materially changes the concept, ask a concise clarification.
- Do not treat a one-time command-local instruction as a permanent Bedrock revision unless the user clearly says so.

A deliberate user revision is allowed. Bedrocks are not immutable against their creator's explicit decision.

## Improvisation boundary

The Improvise tag does not authorize contradiction of a Bedrock. Creative additions must fit around Bedrocks, not erase them.

## Completion check

- [ ] All confirmed Bedrocks are identified.
- [ ] Scope is preserved.
- [ ] Relevant outputs contain the applicable Bedrocks section.
- [ ] Each Bedrocks section contains only a list of Bedrock points.
- [ ] No generated content contradicts a Bedrock.
- [ ] Unconfirmed candidates have not been silently promoted.
