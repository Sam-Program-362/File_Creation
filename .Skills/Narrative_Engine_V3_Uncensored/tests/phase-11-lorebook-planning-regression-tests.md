# Phase 11 — Lorebook Planning Regression Specifications

**Purpose:** Verify that the Lorebook Planner produces actionable, project-grounded handoff plans without creating actual JSON or JavaScript.

**Status:** Test specifications only. They have not been executed against a target LLM or platform runtime.

## A. Routing and output boundary

1. `Plan Lorebooks` activates the Lorebook Planning skill.
2. `Create Lorebook Plan [JanitorAI]` preserves the command-local platform scope.
3. A user asks for ready-to-import JSON; the planner states its plan-only boundary and does not output JSON.
4. A user asks for an Advanced Script; the planner specifies behavior only and does not output JavaScript.
5. The plan is Markdown and contains no executable / near-executable code blocks.
6. The response does not append a command menu or claim the Lorebook was created or imported.

## B. Source fidelity and project context

7. The planner reads the current approved project assets and does not invent a Context Sheet or World Sheet that is absent.
8. Current explicit planning instructions override older non-Bedrock preferences for this run.
9. Approved source conflicts are identified rather than silently reconciled.
10. Established / supported / inferred / proposed / unknown information is not conflated.
11. Every proposed entry has a clear source and owner.
12. The plan is self-contained enough for a separate creator to use without reopening the conversation.

## C. Need and destination decisions

13. Stable premise information remains in main project documents instead of being duplicated wholesale into constant Lorebook entries.
14. The planner can conclude that no Lorebook or Advanced Script is needed and explain why.
15. A large keyword-activated knowledge library is routed to normal Lorebook entries.
16. A rule that must always be active and has no reliable trigger may be recommended as constant.
17. Importance alone does not automatically make an entry constant.
18. Temporary state-dependent behavior with cleanup needs is routed to Advanced Script when the target supports it.
19. A request requiring personality and scenario to receive different additions is recognized as dual-injection behavior.
20. Message-count gates, weighted random selection, and multi-condition detection are recognized as Advanced Script candidates when actually required.

## D. Platform compatibility

21. JanitorAI is identified as the source-described target for Advanced JavaScript.
22. SillyTavern-style World Info is identified as source-described for normal Lorebook JSON.
23. The planner does not claim Advanced Script compatibility with SillyTavern based only on the supplied source.
24. An unknown platform triggers a conditional plan and explicit validation requirement.
25. Unknown schema semantics are not invented.

## E. Lorebook architecture and entry briefs

26. Multiple Lorebooks are separated only when scope, activation, maintenance, or conflict boundaries justify it.
27. Unrelated entries are not packed into one monolithic library without rationale.
28. The planner avoids excessive fragmentation.
29. Each Lorebook has a clear purpose, scope, ownership boundary, dependencies, and non-duplication rules.
30. Every entry brief explains the failure it solves and its intended downstream effect.
31. Entry content direction is concrete and not limited to “follow the character.”
32. Each entry identifies scope, source facts, and applicable tags.
33. Each entry has a justified constant / keyword activation recommendation.
34. Trigger phrases are specific and include positive / negative tests.
35. Secondary keys / selective logic are marked for platform validation if semantics are unknown.
36. Insertion order is described relationally; lower numerical order is noted as earlier only as stated by the supplied schema reference.
37. Priority recommendations acknowledge the two slightly different priority-band descriptions in source files.
38. The planner does not invent probability weights, message thresholds, or selection logic.
39. It distinguishes recommended field behavior, downstream defaults, and platform-validation requirements.
40. It does not fabricate enum values or implementation details for `selectiveLogic`, extensions, inclusion groups, or activation scripts.

## F. Content patterns, tags and Bedrocks

41. Anti-default rules are selected only when a specific default failure is present.
42. Personality filters are tailored to the actual character and not copied generically.
43. Non-escalation guidance is included only when escalation control is relevant.
44. Time continuity guidance is included only when time continuity matters.
45. Dominance preservation is not forced into projects without that dynamic.
46. Progression mandates appear only when narrative progression is an explicit need.
47. Aftercare / aftermath guidance is used only where relevant and must match personality.
48. Uncensored / Detailed / other tags are applied according to scope and individual tag definitions.
49. Relevant male and futanari context is not treated as an afterthought when the project includes it, but is not introduced into unrelated projects.
50. Confirmed Bedrocks are preserved; the plan's Bedrocks section contains only point bullets.
51. A Bedrock is not automatically duplicated into every Lorebook; coverage is based on downstream need.
52. Improvise does not permit contradiction of established facts or Bedrocks.

## G. Advanced Script handoff

53. Every proposed script specifies target runtime and platform validation.
54. Detection conditions and inputs are clearly described.
55. False-positive and false-negative risks are documented.
56. Personality and scenario destinations are distinguished.
57. Start condition, lifetime, and stop / cleanup condition are explicit.
58. Duplicate-prevention markers or equivalent requirements are specified.
59. Missing context / empty message safeguards are specified.
60. `example_dialogs` is treated as optional platform-specific capability.
61. Tests cover trigger, sustained state, end state, cleanup, repeat, no context, empty message, and base-text preservation.

## H. Handoff completeness

62. The plan explains main-document versus Lorebook allocation.
63. Every proposed Lorebook has a complete purpose and scope brief.
64. Every proposed entry has sufficient content and activation detail for implementation.
65. Advanced Script briefs describe behavior without code.
66. Shared conflict and co-activation rules are clear without invented runtime precedence.
67. Platform assumptions and unresolved decisions are explicit.
68. The build/test handoff is actionable.
69. The plan includes only relevant content patterns and entries.
70. No approved requirement is lost because it does not fit a conventional entry category.

## Execution record

No target-model execution has been performed as part of this package build. Record target model, platform/runtime, test prompt, observed output, pass/fail, and required repair when the regression suite is executed later.
