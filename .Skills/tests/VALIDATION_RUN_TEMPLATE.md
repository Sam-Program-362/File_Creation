# Narrative Engine V3 — Manual/Target-Model Validation Run

Use one copy of this template for each test run. This is a record format, not an executable test runner.

## Run metadata

- **Date:**
- **Target model/provider:**
- **Interface/runtime:**
- **Skill package version:**
- **Tester:**
- **Test suite(s):**
- **Relevant settings/configuration:**

## Result key

- **PASS:** Expected behavior observed.
- **FAIL:** Expected behavior not observed; include a reproducible example.
- **BLOCKED:** Could not run because a required capability/source/runtime was unavailable.
- **NOT RUN:** Not attempted in this run.
- **NOT APPLICABLE:** The test does not apply to this project/runtime; explain why.

Do not use PASS for a test that was merely inspected or reasoned about.

## Case results

| Test ID | Status | Evidence / output excerpt | Failure or limitation | Retest needed? |
|---|---|---|---|---|
| | | | | |

## Failure analysis

For each FAIL:

- Reproduction steps:
- Expected behavior:
- Actual behavior:
- Relevant skill file(s):
- Likely cause (confirmed or hypothesis):
- Proposed repair:
- Regression cases affected:

## Summary

- Cases attempted:
- PASS:
- FAIL:
- BLOCKED:
- NOT RUN:
- NOT APPLICABLE:
- Critical unresolved failures:
- Skill files changed after this run:
- Retest date/version:

## Validation statement

State only what this run proves. A passing manual/model run applies to the named model, runtime, configuration, package version, and tested cases; it does not prove universal behavior across all models or interfaces.
