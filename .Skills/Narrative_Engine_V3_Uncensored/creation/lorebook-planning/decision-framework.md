# Lorebook Planning — Decision Framework

This file supports `creation/lorebook-planning/SKILL.md`. It is an operational decision aid, not a second command router.

## 1. Destination decision

Ask what the requirement needs from the downstream AI and how often it must be available.

| Requirement shape | Preferred destination | Reason |
|---|---|---|
| Core premise, cast identity, base relationships, essential setting context | Context / Character / World documents | These are foundational project facts, not an activation library. |
| A large set of facts or instructions that become relevant when a subject is mentioned | Normal keyword Lorebook | The source system is designed for independent keyword-activated entries. |
| A rule that must be available at all times and has no dependable trigger words | Constant normal Lorebook entry, if it is not already adequately present in the main context | The source defines constant entries for always-needed rules without keyword activation. |
| A personality or behavior overlay with a clear trigger phrase or context | Normal Lorebook, unless it requires state detection / cleanup | Independent entries can be edited and activated separately. |
| A temporary rule that begins and ends with a detected state | Advanced Script, when the target is JanitorAI and the runtime supports the required hooks | The source's strongest pattern is detection → injection → cleanup. |
| Different text must be injected into character personality and scenario | Advanced Script, target-dependent | The source describes dual injection into these two destinations. |
| Behavior gated by message count, weighted randomness, or multiple simultaneous conditions | Advanced Script, target-dependent | These are beyond simple keyword matching in the source's decision logic. |
| No clear activation use case, or main documents already solve the need | No Lorebook component | Avoid unnecessary modularization. |

## 2. Platform decision

- **JanitorAI:** The supplied source describes both normal JSON Lorebooks and Advanced JavaScript Scripts.
- **SillyTavern-style World Info:** The supplied source describes normal JSON Lorebook entries. It does not establish Advanced Script support for SillyTavern.
- **Other / unspecified platform:** Do not infer compatibility. Produce a conditional design and mark schema / runtime verification as required.

If one project requires both normal entries and Advanced Script behavior, keep platform compatibility visible at the Lorebook / script level. Do not assume a portable single package.

## 3. Constant versus keyword activation

Use `constant: true` only where the material must always be active and there is no dependable keyword. Use `constant: false` plus deliberate keys when activation is situational.

Distinguish these questions:

1. Is the rule important? (Priority.)
2. Is the rule always needed? (Activation lifetime.)
3. Can it be reliably detected with keys? (Trigger reliability.)

Do not use “important” as a synonym for “constant.”

## 4. Grouping and splitting

Group entries when they share a domain, activation logic, editing purpose, and likely to be needed together.
Split when they have different triggers, lifetimes, scopes, owners, or conflict risks.

A simple review test:
- Would the entries usually be relevant in the same scene or topic?
- Can they safely share an activation boundary?
- Would editing one entry require changing the other?
- Is there a clear reason for a separate Lorebook (platform setup, owner, or reusable scope)?

If all answers point to one cohesive library, keep it together. If their activation boundaries diverge, separate them.

## 5. Trigger design

A useful trigger is likely to appear when the information is needed and unlikely to appear in unrelated contexts.

For each entry, test:
- exact term or phrase;
- natural synonyms and common inflections;
- alternate spelling or punctuation when relevant;
- a misleading or unrelated sentence containing the same word;
- a nearby topic where the entry should not activate;
- co-occurrence with a secondary key when selective activation is intended.

Prefer specific terms over broad common words. Do not list every conceivable synonym if that makes accidental activation likely.

The supplied schema includes primary keys, secondary keys, key matching priority, whole-word matching, and selective logic fields. The source does not define all platform semantics for these fields; the downstream creator must verify exact behavior.

## 6. Priority and insertion ordering

Use the Notion plan's V3 priority bands as initial labels, while acknowledging the alternate finer-grained ranges in `references/lorebook-creator/references/entry-schema.md`. Explain relative importance; do not pretend exact ranking semantics are universal.

Specify insertion relationships in words (for example, “this core rule should be inserted before the character-specific overlay”). The source schema says lower `insertion_order` values are earlier. The exact effects of insertion ordering and priority on a given runtime must be tested.

## 7. Conditional behavior check

A requirement likely needs Advanced Script planning when all or most of these are true:
- activation depends on state, not only topic words;
- the system must react to the latest message or recent messages;
- the instruction is temporary;
- there must be cleanup when the condition stops;
- it must add separate content to personality and scenario;
- message count, weighted random behavior, or multi-condition logic is required.

If a normal Lorebook entry can do the job reliably, prefer the simpler entry format.
