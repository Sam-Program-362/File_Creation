---
name: narrative-engine-artifact-dependency-map
status: implemented
stage: 12
---

# Artifact Dependency Map

This map is used by Patch Refinement and Expansion to decide where a changed project fact must be reflected. It is not a rule to rewrite every connected document after every edit.

## 1. Core rule

**Propagate information, not wording.** A source fact may appear in several outputs, but each output has a different purpose. Update only existing artifacts that repeat, rely on, or operationally depend on the changed fact.

Do not create missing artifacts as part of propagation. Do not let a derived presentation artifact silently override the underlying character, world, or project source.

## 2. Dependency matrix

| Changed source / fact | Inspect existing dependents | Typical update condition |
|---|---|---|
| Analysis Sheet finding | Character Sheet, World Sheet, Context Sheet, Scenario, Description, Lorebook Plan | The approved finding is corrected or newly approved and a generated artifact still contains the old interpretation. |
| Character fact / trait / voice / capability | Context Sheet, Scenario, Description, Lorebook Plan; sometimes relationship material | The dependent output contains or uses the changed character information. |
| Character-specific appearance | Context Sheet, Description, Scenario if visually described, Lorebook Plan if visual behavior is modularized | Only when the dependent document actually refers to the changed appearance. |
| Character history / secret / knowledge | Context Sheet, Scenario, Lorebook Plan, Description if disclosed | Update knowledge boundaries and any passages made incorrect; preserve spoiler rules. |
| Relationship dynamic | Each involved Character Sheet, Context Sheet, Scenario, Description, Lorebook Plan | The dynamic is represented or affects behavior in the dependent output. |
| World rule / setting fact / geography / institution | Context Sheet, Scenario, Description, Lorebook Plan; affected character sheets | The dependent content relies on the old world rule or location fact. |
| Plot premise / conflict / stakes / progression condition | Context Sheet, Scenario, Description, Lorebook Plan; relevant character/world sheets | The changed plot fact is present or causally assumed by the dependent output. |
| Project-wide Bedrock | All existing outputs where the invariant applies | Any artifact lists, describes, or implies behavior constrained by that Bedrock. |
| Character / relationship / world / scenario-local Bedrock | Only outputs within that Bedrock's scope | The output contains the affected entity or situation. |
| Tag definition or tag scope | Outputs generated under that tag, within its scope | A tag's meaning or application is explicitly revised; ordinary tag activation on one task is not a global definition change. |
| Context Sheet wording only | No automatic source-document propagation | The underlying Character, World, or Plot facts have not changed. |
| Scenario staging / prose only | No automatic source-document propagation | The edit concerns only how the opening is presented. |
| Description audience / spoiler level / wording | No automatic source-document propagation | The edit is presentation-only. |
| Lorebook Plan trigger or entry architecture | No automatic source-document propagation | The implementation plan changes, but project canon does not. |
| Lorebook Plan fact derived from a changed source | Affected plan briefs and tests | Its source fact, activation logic, or intended behavior has changed. |

## 3. Important source relationships

### Analysis Sheet

The Analysis Sheet is an understanding checkpoint and may contain observations, interpretations, and planning language. Once the user approves an interpretation, it informs downstream creation. A newer explicit user correction supersedes the old finding. Do not treat the Analysis Sheet as permanently higher priority than the user's later correction.

### Character Sheet and World Sheet

These are authoritative project-asset references for their respective content domains while they remain current. A canonical change in one may require a targeted update in the Context Sheet and other artifacts that actually use the changed fact.

### Context Sheet

The Context Sheet is the comprehensive downstream handoff, not the source of truth for the contents of a Character Sheet or World Sheet. It integrates those assets. When it conflicts with a newer approved Character/World source, patch the Context Sheet to match the newer source unless the user explicitly makes a different project-level decision.

### Scenario

A Scenario is an opening message. It is a derived scene presentation, not general project canon. A changed Scenario does not normally require edits to the Context Sheet or character/world assets. If a canonical fact changes, patch the opening only if it contains stale or contradictory material.

### Description

A Description is a human-facing presentation. Its wording, disclosure scope, and spoiler level are artifact-local unless the user explicitly revises the underlying project facts.

### Lorebook Plan

A Lorebook Plan is a technical/content handoff derived from project information. It should be updated when source facts, Bedrocks, triggers, or desired behavior change. It does not become the canonical source for character or world truth.

## 4. Change propagation procedure

For a canon-relevant change:

1. Identify the changed information unit and its scope.
2. Search the existing project outputs for explicit statements and implicit dependencies on that information.
3. Classify each dependent artifact as **affected**, **possibly affected**, or **unaffected**.
4. Patch affected artifacts only where stale or contradictory content exists.
5. For possibly affected artifacts, inspect the relevant passage before deciding.
6. Leave unaffected artifacts byte-for-byte / wording-for-wording unchanged.
7. Run the Information Transfer coverage check on the changed information unit.
8. Run Bedrock and target-output validation.

If the output cannot be inspected, do not claim it was synchronized.

## 5. No-propagation cases

Do not propagate:
- grammar or spelling edits to an unrelated asset;
- Description phrasing changes into project canon;
- Scenario prose variations into character voice definitions unless the user intends a character-wide voice change;
- a command-local constraint into future generations;
- an artifact-local omission into deletion of the underlying fact;
- a new optional idea into approved canon before the user accepts it, unless the active Improvise instruction explicitly authorizes completion within its scope.
