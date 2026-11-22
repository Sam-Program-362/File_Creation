# Phase 13 — Quality Assurance Regression Specifications

**Status:** Test specifications written; not yet executed against a target LLM/runtime.  
**Source alignment:** Notion V3 plan, Section 14 (Quality Assurance), plus the plan's 15 V3 regression scenarios.  
**Purpose:** Verify QA behavior itself, not merely whether an artifact looks polished.

## Test method

For each case, supply the described project state and target artifact to the intended model with the V3 skill tree loaded. Record the actual artifact and QA outcome. A test passes only when the observable result matches the expected behavior. Do not count static file checks as model-behavior test execution.

## A. Notion-required quality dimensions

1. **Concept fidelity:** An output retains the supplied premise and central appeal without replacing them with a more conventional story.
2. **Explicit facts:** A supplied character trait is not changed during generation to fit an archetype.
3. **Unsupported additions:** The model does not add a major trauma, secret, relationship, or world rule without support or authorization.
4. **Bedrock presence:** Every applicable confirmed Bedrock appears in the proper Bedrocks section when that artifact requires the list.
5. **Bedrock consequence:** A Scenario does not violate a Bedrock through its actions even if it repeats the Bedrock correctly in a list.
6. **Bedrock preservation:** Refinement does not weaken or silently remove a Bedrock.
7. **Analysis coverage:** Every approved, meaningful Analysis Sheet item is assigned to the appropriate requested final output.
8. **Context completeness:** A Context Sheet can stand alone as the narrator-facing project handoff.
9. **Unusual information:** An unusual concept detail is preserved through a suitable custom section rather than dropped because no standard heading exists.
10. **Adaptive sections:** The model avoids empty or irrelevant template headings.
11. **Output identity:** A request for a Character Sheet does not return a Context Sheet or Analysis report.
12. **Context identity:** The Context Sheet is informational and self-contained, not a conversational prompt or analysis report.
13. **Description identity:** The Description is written for people, not as instructions for another AI.
14. **Scenario identity:** Scenario generation produces a starting message only, not roleplay continuation.
15. **Lorebook Plan identity:** Lorebook Planning creates a detailed handoff, not actual JSON entries or JavaScript.
16. **Tag definitions:** Each supplied tag is applied according to its individual definition and scope.
17. **Automatic tag scope:** An auto-applied Uncensored tag for one character does not make unrelated characters profane.
18. **Detailed activation:** The Detailed behavior activates when Detailed is supplied as a tag, not merely because the word appears in ordinary prose.
19. **Improvise:** When Improvise is active, missing information is completed appropriately and the relevant Analysis output does not contain a Missing Elements section.
20. **Refinement preservation:** A targeted edit leaves every unaffected sentence and section unchanged.

## B. Coverage Validation tests

21. **Multi-source ledger:** A project with notes, image observations, and approved analysis points produces an internal destination map for each meaningful item.
22. **No false promotion:** An unapproved inference is not treated as an approved coverage obligation in a final asset.
23. **Character ownership:** A character-specific detail is not accidentally transferred to another character.
24. **World ownership:** A location-specific rule is not made universal without support.
25. **Context integration:** Related character, relationship, world, and plot facts are integrated with their relationships explained, not merely listed separately.
26. **No forced duplication:** An irrelevant minor detail is not repeated in every output merely to claim coverage.
27. **No fabricated deliverables:** Coverage validation does not generate a missing Character Sheet or World Sheet unless requested.
28. **Missing source:** If the approved Analysis Sheet is unavailable, the validator does not claim complete source-to-output coverage.
29. **Lorebook handoff coverage:** A Lorebook Plan has enough context, activation intent, content direction, scope, Bedrocks, dependencies, and tests for a separate creator.
30. **Selective scenario coverage:** A starting message reflects relevant project information without trying to reproduce the entire Context Sheet.

## C. Consistency Validation tests

31. **Explicit correction wins:** A clear, current user correction is applied within its stated scope and stale derived text is identified.
32. **Unclear Bedrock conflict:** A new instruction appears to contradict a Bedrock but revision intent is unclear; the system asks rather than silently overriding.
33. **Authorized Bedrock revision:** The user clearly revises a Bedrock; the revision is applied and relevant existing artifacts are identified for updates.
34. **Scope preservation:** A character-specific Bedrock is not propagated to unrelated characters or the entire world.
35. **Knowledge boundary:** A character does not act on a secret they do not know.
36. **Intentional lie:** A character's deliberately false statement is not incorrectly flagged as an objective project contradiction.
37. **Mystery preservation:** Conflicting in-world accounts that are intentional clues remain unresolved.
38. **Chronology:** An event is not placed before its established cause or after an incompatible event.
39. **World mechanics:** A scene does not violate an established ability, physical limit, travel rule, or world system.
40. **Cross-artifact freshness:** A changed canonical character fact is checked against an existing Context Sheet and Scenario, but absent documents are not fabricated.
41. **Project isolation:** Facts and Bedrocks from a second project do not leak into the active project's output.
42. **Tag scope:** Character-specific Uncensored, Focus, or Exclude behavior does not spread beyond its defined scope.

## D. Output Validation tests

43. **Analysis Sheet contract:** Evidence, inference, tags, Bedrock candidates, and generation direction are handled as analysis rather than final creative prose.
44. **Character Sheet contract:** Full Physical Description expands all supported dimensions when tagged and does not invent exact body measurements.
45. **World Sheet contract:** A temporary weather condition in a Scenario Reference is not turned into permanent climate lore.
46. **Context Sheet contract:** `Provided Elements`, `Missing Elements`, and `Planned Expansion` analysis headings are not carried into the final Context Sheet.
47. **Scenario quantity:** The exact requested number of starting messages is produced.
48. **Scenario format:** Narration, dialogue, thoughts, and `//` OOC notation each follow the correct format and boundaries.
49. **User agency:** No user-character thought, voluntary action, dialogue, or decision is invented in a starting message.
50. **Description audience:** A human-facing Description does not contain internal system instructions, QA notes, or analysis jargon.
51. **Spoiler control:** A public spoiler-light description respects the requested disclosure scope.
52. **Lorebook output boundary:** The plan may name schema fields and describe settings but does not output a ready-to-import entry array or executable script.
53. **Patch output:** A refinement follows the requested output mode and does not append a command footer.
54. **Expansion output:** Expansion adds requested depth while retaining existing established traits, lore, relationships, and dynamics.
55. **Detailed style:** High detail remains organized and relevant rather than padded with unrelated exposition.
56. **Uncensored voice:** The relevant character's direct/slang vocabulary is preserved without forcing profanity into every line or every character.

## E. QA orchestration, repair, and reporting tests

57. **Safe local repair:** An obvious name typo is corrected without asking or changing unrelated content.
58. **Substantive ambiguity:** A material source conflict is not repaired by inventing a convenient explanation.
59. **Revalidation:** A repair is followed by a second check of the affected criteria.
60. **Blocker handling:** A direct Bedrock violation is not labeled ready until corrected or explicitly surfaced as unresolved.
61. **Warning handling:** A missing dependent artifact is reported as a validation limitation, not as a successful cross-artifact check.
62. **No unsolicited report:** Normal generation does not append a long QA checklist or scorecard.
63. **Requested QA report:** An explicit Review request yields concise, artifact-specific findings.
64. **No false test claim:** The assistant does not claim target-LLM testing passed unless the tests were actually run.
65. **No executable assumption:** QA procedures are not represented as a Python/JavaScript checker or automatic runtime feature.
66. **No scope creep:** QA does not redesign, expand, or regenerate unrelated project material.

## Acceptance criteria

Phase 13 is operationally implemented when its coordinator and three validators provide concrete procedures, all seven artifact types have output contracts, refinement and expansion checks are included, and the suite above is available for model testing.

Phase 13 is model-validated only after the cases are run against a named target LLM/runtime and the results, failures, and retests are recorded. Writing this test file does not satisfy that execution requirement.
