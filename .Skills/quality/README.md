---
name: narrative-engine-quality
version: 1.0.0
status: implemented
stage: 13
description: System-wide output quality assurance and regression specifications.
---

# Phase 13 — Quality Assurance

Phase 13 is the finalization layer for Phases 6–12 and any other artifact-producing operation. It implements the Notion plan's six QA groups: concept fidelity, Bedrock integrity, coverage, structure, output identity, and style/tag/refinement compliance.

## Module map

| File | Responsibility |
|---|---|
| `SKILL.md` | QA routing, activation, validation sequence, severity, safe repair, and reporting behavior. |
| `coverage-validation/SKILL.md` | Checks Analysis-to-output information transfer and Context Sheet completeness. |
| `consistency-validation/SKILL.md` | Checks Bedrocks, facts, characters, world rules, chronology, relationships, tags, and cross-artifact consistency. |
| `output-validation/SKILL.md` | Checks each artifact against its individual purpose, format, scope, and tag behavior. |

## Mandatory finalization hook

Run QA after each Analysis Sheet, Character Sheet, World Sheet, Context Sheet, Scenario, Description, or Lorebook Plan; after every refinement or expansion; and whenever the user explicitly requests `Review [target]`.

The QA layer works internally by default. Do not append a verbose report or fixed footer unless the user requests it or a material blocker/warning needs disclosure.

## Shared dependencies

Phase 13 builds on:
- `shared-systems/bedrocks/SKILL.md`;
- `shared-systems/information-transfer/SKILL.md`;
- `shared-systems/evidence-and-inference/SKILL.md`;
- `shared-systems/adaptive-sections/SKILL.md`;
- relevant individual tag definitions;
- the target artifact's own generation/refinement skill.

## Validation status

The regression suite is a specification for target-model testing. It is not an executable test runner, and its existence does not mean a target LLM has passed. Use `tests/phase-13-quality-assurance-regression-tests.md` and `tests/VALIDATION_RUN_TEMPLATE.md` to perform and record actual manual/model evaluations.
