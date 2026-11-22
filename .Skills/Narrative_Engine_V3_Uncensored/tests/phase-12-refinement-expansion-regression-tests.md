---
name: narrative-engine-phase-12-regression-tests
status: specification-only
stage: 12
---

# Phase 12 — Refinement and Expansion Regression Specifications

These cases define expected model behavior for the Phase 12 skills. They are test specifications, not proof of model execution. Execute them against the selected target model and record actual outputs, failures, and fixes before calling model behavior validated.

## Test instructions

For each case, provide the target artifact and the stated user request. Compare the result against the preservation, scope, Bedrock, dependency, and output rules. The evaluator should verify exact unchanged text where full-artifact mode is expected.

### 1. Command routing

`Refine Sheet: change the project type` routes to the Analysis Sheet and patch refinement, not to full analysis regeneration.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 2. Command routing

`Refine Character: change Akari's eye color` resolves the named Character Sheet.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 3. Command routing

`Refine World: remove the old district name` targets the World Sheet and treats removal as explicit.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 4. Command routing

`Refine Context Sheet: clarify the current premise` targets the narrator-facing handoff.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 5. Command routing

`Refine Scenario: change the opening weather` changes the opening only unless the weather is explicitly a permanent world fact.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 6. Command routing

`Refine Description: make the first paragraph shorter` is a presentation-only edit.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 7. Command routing

`Refine Lorebook Plan: add a trigger for the royal court` changes the handoff, not the actual JSON.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 8. Target ambiguity

`Refine this` with one active artifact infers the target.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 9. Target ambiguity

`Refine this` with several plausible active artifacts asks one concise clarification.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 10. Target ambiguity

A request names one artifact while another is more recent; the named artifact is selected.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 11. Exact source

Patch operation uses exact current artifact content rather than reconstructing it from a summary.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 12. Exact source

If exact target text is unavailable, the model does not claim to have patched the full artifact.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 13. Patch minimality

Changing one sentence leaves every unrelated sentence, paragraph, bullet, and heading unchanged.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 14. Patch minimality

A requested grammar correction does not trigger global proofreading.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 15. Patch minimality

A request to change one heading does not rewrite its body.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 16. Patch minimality

A move operation preserves the original wording.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 17. Patch minimality

A section split preserves all original information units.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 18. Patch minimality

A section merge does not summarize or delete source information.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 19. Patch operations

A replacement removes the stale assertion from duplicate locations in the same artifact where necessary.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 20. Patch operations

A removal request deletes only the specified information and necessary stale references.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 21. Patch operations

A replacement does not delete adjacent contextual detail that remains correct.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 22. Patch operations

A new custom section is created when no existing heading is semantically suitable.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 23. Patch operations

An artifact-local deletion does not delete the underlying project fact.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 24. Scope

`Create Character [only Akari]` from V2 does not become a standing cast restriction during later refinement.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 25. Scope

A command-local edit does not silently become a project-wide rule.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 26. Scope

A clearly project-wide user correction updates the canonical fact.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 27. Scope

A presentational rewrite of a Description does not alter Character or World canon.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 28. Bedrocks

A refinement that conflicts with a Bedrock and has unclear revision intent asks for clarification.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 29. Bedrocks

A clearly authorized Bedrock revision updates the clean list and relevant existing outputs.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 30. Bedrocks

A Bedrocks section contains only actual Bedrock bullets, without explanatory instructions.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 31. Bedrocks

A character-specific Bedrock is not propagated to unrelated characters.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 32. Bedrocks

An inference cannot silently become a Bedrock during refinement.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 33. Propagation

A canonical character fact change patches stale Context Sheet references.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 34. Propagation

A canonical world-rule change patches affected World/Context/Scenario/Description/Lorebook passages only where present.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 35. Propagation

A Scenario-only staging edit does not rewrite Character or World Sheets.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 36. Propagation

A Description-only audience adjustment does not rewrite the Context Sheet.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 37. Propagation

A Lorebook Plan trigger revision does not alter project canon.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 38. Propagation

An absent dependent artifact is not fabricated or claimed to be synchronized.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 39. Output contract

A manageable exact target returns the complete revised artifact by default.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 40. Output contract

A huge target uses exact insertion-ready patches rather than silently omitting unchanged content.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 41. Output contract

When the user requests only changed sections, only those sections are returned.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 42. Output contract

The model does not append a fixed command menu or interaction footer.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 43. Expansion

Expand adds detail while preserving all established traits, lore, relationships, and dynamics.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 44. Expansion

A broad Expand Character request deepens relevant material without adding unrelated world systems.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 45. Expansion

Expansion adds a custom section when the existing structure has no suitable place.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 46. Expansion

Expansion uses narrative gravity to allocate detail rather than expanding all sections equally.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 47. Expansion

Behavioral expansion demonstrates a trait through actions, speech, and decisions without changing the trait.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 48. Expansion

Contextual expansion does not invent major trauma or secrets without support or authorization.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 49. Expansion

Connective expansion clarifies relationships between established facts without adding an unsupported causal event.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 50. Expansion

World expansion does not turn a contained setting into an open world without authorization.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 51. Expansion

Open World/Open Interaction tags permit relevant additional scope but do not require unlimited additions.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 52. Expansion

Improvise fills necessary gaps within tag scope and does not add a Missing Elements section.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 53. Expansion

Detailed tag increases explanation without adding padding or irrelevant material.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 54. Expansion

Ordinary use of the word detailed does not silently activate the Detailed tag.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 55. Expansion

An optional major idea remains labeled as a proposal rather than being silently accepted as canon.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 56. Expansion

A canon-relevant addition is propagated only to existing dependent outputs that use it.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 57. Expansion

An expansion of Scenario affects the opening message and does not continue roleplay.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 58. Expansion

An expansion of Context Sheet remains informational, comprehensive, and non-conversational.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 59. Expansion

An expansion of Lorebook Plan remains a handoff and does not produce JSON or JavaScript.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 60. Combined operation

A request to correct an existing trait and then deepen it applies the correction first and then expands the corrected version.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 61. Combined operation

A request to add a new custom section while preserving existing sections does not reorganize the document.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 62. Project isolation

Refinement or expansion operates only on the active project namespace.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 63. Project isolation

No cross-session memory is claimed when the source artifact is not available.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 64. Artifact integrity

The target artifact remains a Character Sheet, World Sheet, Context Sheet, Scenario, Description, Analysis Sheet, or Lorebook Plan according to its original identity.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 65. Artifact integrity

Scenario notation and user-agency requirements survive any patch or expansion.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 66. Artifact integrity

Description remains human-facing and not an AI prompt after refinement or expansion.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 67. Artifact integrity

Context Sheet does not gain analysis-only headings during expansion.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 68. Artifact integrity

Lorebook Plan preserves the plan-only boundary during refinement and expansion.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 69. Regression safety

Static validation distinguishes skill-instruction presence from model-behavior execution.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

### 70. Regression safety

The tests do not claim successful target-LLM execution until runs are recorded.

**Expected:** The relevant Phase 12 procedure is followed without unrequested rewriting or loss.

## Execution record

- Target model/runtime: Not yet specified.
- Execution status: Not executed.
- Static package validation: separate from behavioral testing.
- Defects found / remediation: To be recorded after actual runs.
