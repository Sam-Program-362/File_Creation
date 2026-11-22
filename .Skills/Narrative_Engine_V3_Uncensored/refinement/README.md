---
name: narrative-engine-refinement
status: implemented
stage: 12
description: Operational patch-refinement and additive-expansion systems for existing project artifacts.
---

# Phase 12 — Refinement and Expansion

Phase 12 edits existing Narrative Engine artifacts after they have been created. It is not a generation shortcut and it is not a generic rewrite tool.

## Module map

| Module | Responsibility |
|---|---|
| `patch-refinement/SKILL.md` | Resolve targets, interpret requested changes, apply minimal patches, handle dependencies, preserve unrelated content, and validate edits. |
| `patch-refinement/patch-operations.md` | Defines permitted edit operations, exact preservation rules, conflict handling, and patch-output modes. |
| `patch-refinement/artifact-dependency-map.md` | Identifies which existing outputs may need synchronized updates when established project facts change. |
| `expansion/SKILL.md` | Adds requested depth, detail, connective information, and new material without replacing established layers. |
| `expansion/expansion-methods.md` | Defines expansion types, controlled development, insertion methods, and anti-padding rules. |

## Shared dependencies

Both modules use:
- `core/command-router/SKILL.md` for command and scope resolution;
- `core/project-isolation/SKILL.md` to keep the active project's assets separate;
- `shared-systems/information-transfer/SKILL.md` for coverage and cross-output propagation;
- `shared-systems/bedrocks/SKILL.md` for core invariants;
- `shared-systems/adaptive-sections/SKILL.md` when a change requires a new or modified section;
- `shared-systems/evidence-and-inference/SKILL.md` when additions or corrections depend on source support;
- `shared-systems/tags/SKILL.md` and applicable tag definitions when tags affect the requested operation.

The target artifact's own creation skill is also loaded so edits preserve that artifact's purpose and output contract.

## Core distinction

**Refinement is a patch. Expansion is an addition.**

- Refinement changes only what the user requested and the existing information that must change to keep the project coherent.
- Expansion adds depth or new material while preserving existing information and structure wherever possible.

Do not use one operation as a substitute for the other.

## Scope boundary

Phase 12 operates on the current conversation's active project materials and any exact source artifact supplied by the user. It does not promise cross-session memory, edit external files without access, or silently recreate missing documents from vague recollection.
