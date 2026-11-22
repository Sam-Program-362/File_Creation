# Lorebook Planning — Advanced Script Handoff

This file defines the required design brief for Advanced Scripts. It does not contain a script template and must not produce JavaScript.

## When to propose this type

The supplied Lorebook Creator describes Advanced Scripts as JanitorAI JavaScript for conditional detection, message-count triggers, random events, dual personality/scenario injection, cleanup, and complex detection. Do not assume the same Advanced Script API or support exists on another platform.

Use this route when simple keyword entries cannot reliably express the requirement, especially a temporary behavior that should appear only while a detected state is active.

## Handoff contents

For each proposed script, describe:

1. **Identity and purpose:** Name and the precise behavior it is meant to control.
2. **Target runtime:** JanitorAI or an explicitly stated other target; version must be confirmed by the downstream creator.
3. **Activation condition:** The state or event that makes the behavior active. Define this in natural language with enough specificity to avoid ambiguity.
4. **Detection inputs:** The supplied reference describes chat last message, total message count, recent messages, and user name, plus character personality and scenario strings. State exactly which information is needed. Do not assume undocumented inputs.
5. **Detection approach:** Curated keyword/regex matching, message-count gate, multiple conditions, weighted selection, or other supported pattern.
6. **False-positive controls:** Common words, quoted text, negation, unrelated context, or scene types that must not trigger it.
7. **False-negative coverage:** Natural terms, phrasing, inflections, and context needed for correct activation.
8. **Injection destinations:** Personality, scenario, or both. Define the distinct role of content in each destination.
9. **Injection content brief:** Exact concepts, behavior, boundaries, voice filters, and Bedrocks the eventual injected note must communicate. Do not write the executable note as a full final string unless the separate creator asks for content drafting; this planner specifies the brief.
10. **Lifetime and cleanup:** When the injection begins, whether it persists over multiple messages, the exact condition for ending, and what must be removed.
11. **Duplicate prevention:** Require a unique marker or equivalent platform-validated mechanism so a repeated run does not append the same injection over and over.
12. **Safety guards:** The source skeleton checks that context, chat, and character exist and returns for an empty last message. Require equivalent defensive handling in the downstream implementation.
13. **Interaction with other modules:** Normal Lorebook entries or main-document rules that overlap, and how the content should be coordinated.
14. **Runtime uncertainties:** Any unsupported or undocumented API, field, lifecycle, persistence, or write behavior requiring validation.
15. **Test matrix:** Trigger, non-trigger, sustained state, state exit, cleanup, duplicate execution, empty message, missing context, false-positive terms, message-count boundary, multiple conditions, and preserved base character text.

## Source-described input / output surface

The supplied material describes these reads:
- `context.chat.last_message`
- `context.chat.message_count`
- `context.chat.last_messages`
- `context.chat.user_name`
- `context.character.personality`
- `context.character.scenario`

It describes writes to:
- `context.character.personality`
- `context.character.scenario`

It notes that some environments may also allow `example_dialogs`. Treat that as optional and validate it before planning around it.

## Pattern choices

- **Detection → injection → cleanup:** use for a temporary state-dependent note. Specify the same marker strategy for both detection and cleanup.
- **Dual injection:** use when behavior guidance belongs in personality while situational rules belong in scenario.
- **Message-count gate:** use only when a project milestone genuinely depends on count.
- **Weighted random:** use only when a randomized event or variation is requested, with selection scope and repeat behavior defined.
- **Multi-condition engine:** use only when the behavior genuinely depends on multiple simultaneous signals.

Do not recommend a script simply because it can be written. Use normal Lorebook entries where they can meet the requirement more simply and reliably.
