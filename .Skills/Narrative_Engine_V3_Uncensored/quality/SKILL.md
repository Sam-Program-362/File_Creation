---
name: narrative-engine-quality-assurance
version: 1.0.0
status: implemented
stage: 13
description: |
  Runs output-specific and cross-output quality checks before a Narrative Engine
  deliverable is finalized. Validates concept fidelity, Bedrocks, information
  coverage, adaptive structure, artifact identity, tags, and edit preservation.
---

# Phase 13 — Quality Assurance Orchestrator

## 1. Purpose

Quality Assurance (QA) is the final validation layer for Narrative Engine V3's actual creation deliverables. It checks that a generated or modified artifact faithfully represents the user's approved project and obeys the relevant system contracts.

QA does not create a replacement artifact, redesign the concept, introduce new lore, or run a roleplay. It evaluates the output produced by another module and identifies whether it is ready to deliver.

The governing QA requirements are the six groups defined in the V3 architecture plan:

1. Concept fidelity.
2. Bedrock integrity.
3. Information coverage.
4. Adaptive structure.
5. Output identity.
6. Style, tag, and refinement compliance.

## 2. Activation

Run Phase 13:

- after an Analysis Sheet is generated or refined;
- after a Character Sheet or World Sheet is generated or refined;
- after a Context Sheet is generated or updated;
- after one or more Scenario starting messages are generated or refined;
- after a human-facing Description is generated or refined;
- after a Lorebook Plan is generated or refined;
- after any Patch Refinement or Expansion operation;
- when the user explicitly invokes `Review [target]` or asks for a consistency/quality review.

QA is a mandatory internal finalization step. It is not a separate user-facing deliverable unless the user asks to see the review.

## 3. Required files and loading

Load:

1. `quality/SKILL.md` — this coordinator.
2. `quality/coverage-validation/SKILL.md` when approved Analysis Sheet information, multiple project artifacts, or a Context Sheet is involved.
3. `quality/consistency-validation/SKILL.md` whenever project facts, Bedrocks, chronology, relationships, or multiple artifacts are involved. This is normally applicable to every project deliverable.
4. `quality/output-validation/SKILL.md` for every deliverable.
5. `refinement/patch-refinement/SKILL.md` and its relevant references when the operation is a refinement.
6. `refinement/expansion/SKILL.md` and its relevant references when the operation is an expansion.
7. `shared-systems/bedrocks/SKILL.md`, `shared-systems/information-transfer/SKILL.md`, `shared-systems/evidence-and-inference/SKILL.md`, `shared-systems/adaptive-sections/SKILL.md`, and the relevant tag definitions as applicable.
8. The target artifact's creation skill or current source artifact when output-specific interpretation is needed.

Do not load all validators or all tag definitions indiscriminately. Use the target and change scope to select dependencies; however, always run the general output-identity and concept-fidelity checks.

## 4. QA inputs

Before checking, resolve:

- active in-session project;
- requested deliverable and its type;
- current user instruction and command-local constraints;
- exact generated or modified artifact;
- available approved Analysis Sheet and current project assets;
- confirmed Bedrocks and their scopes;
- explicit and auto-applied tags, including their scopes;
- whether the operation is initial generation, refinement, or expansion;
- whether the user has requested a visible QA report.

Use only sources available in the current session or explicitly supplied. Do not claim to have compared an artifact against a source that is unavailable. If the exact pre-edit artifact is missing, the preservation check cannot be certified; state this limitation if it materially affects the result.

## 5. Validation sequence

### Step 1 — Establish the validation scope

Identify the exact output being checked. Do not validate unrelated artifacts or import information from another isolated project.

### Step 2 — Check concept fidelity

Determine whether the output:

- preserves the user's intended concept and central appeal;
- preserves explicit facts, traits, dynamics, and constraints;
- avoids unsupported major additions;
- respects explicit user instructions and command-local limitations;
- preserves distinctions between established information, supported interpretation, inference, proposal, and unknowns.

A creative improvement is not automatically a faithful improvement. The user's concept remains authoritative.

### Step 3 — Run applicable specialist validators

- Run **Coverage Validation** when information from an Analysis Sheet or multiple sources must be transferred, and for Context Sheet completeness.
- Run **Consistency Validation** for Bedrocks, project facts, character/world relationships, chronology, scope, and cross-artifact contradictions.
- Run **Output Validation** for the target artifact's specific purpose, format, scope, style, and prohibited substitutions.
- For a refinement, verify preservation of every unaffected region against the exact prior artifact.
- For an expansion, verify that established layers remain present and the requested additions do not contradict them.

### Step 4 — Classify findings

Use the following internal finding levels:

- **BLOCK:** A material failure that makes the deliverable unsafe to present as complete or faithful. Examples: a Bedrock contradiction; an explicit fact reversed; a required approved detail omitted from the Context Sheet; the wrong artifact type; wrong requested Scenario quantity; the Scenario writes the user's thoughts or voluntary actions; a Lorebook Plan contains actual import-ready JSON or executable JavaScript as its deliverable; a refinement silently changes unrelated content.
- **REPAIR:** A clear, local defect that can be corrected without changing the user's concept or making a material interpretive decision. Examples: a misplaced section, accidental omission of a clearly approved detail, inconsistent name spelling, a tag behavior missed in an obvious place, malformed formatting, redundant headings, or an obvious contradiction caused by a generation error.
- **WARN:** A material uncertainty or limitation that cannot safely be resolved from available sources. Examples: conflicting source statements with unclear recency/authority, an unapproved inference that may change the premise, missing exact pre-edit text, or a target-platform behavior not established by the supplied reference.
- **PASS:** The applicable check is satisfied.

Do not classify stylistic preference as a BLOCK unless it violates a direct user instruction or the artifact's defined contract.

### Step 5 — Repair only what is safe

- Automatically repair clear, local REPAIR findings when the correction is unambiguous and within the user's requested scope.
- Do not invent a fact to make a check pass.
- Do not silently resolve an important source conflict, reinterpret a Bedrock, promote an inference, change the premise, or expand the user's requested scope.
- When a BLOCK depends on a material user decision, ask one concise clarification or deliver only the clearly valid portion with the limitation made explicit.
- Do not use QA as permission to rewrite unrelated sections for style.

### Step 6 — Revalidate after repair

Re-run the affected checks after any repair. A correction can create a new contradiction or coverage gap. Do not mark a deliverable ready based solely on the pre-repair check.

### Step 7 — Finalize

- If no BLOCK remains, the artifact can be delivered.
- If a BLOCK remains, do not label the artifact fully validated. Explain the specific unresolved issue briefly.
- Preserve WARN findings when they matter; do not hide them by converting uncertainty into a confident statement.
- Do not create an unsolicited lengthy QA report.

## 6. Visibility and reporting

By default, QA works internally. Do not append a checklist, scorecard, audit narrative, or fixed footer to every output.

Show QA findings when:
- the user explicitly asks to review, audit, or validate;
- a BLOCK prevents reliable completion;
- a WARN materially limits the accuracy or completeness of the deliverable;
- the user needs to approve a substantive repair.

When a report is requested, keep it tied to the actual artifact. Separate:
- checks passed;
- repairs made;
- unresolved warnings/blocks;
- checks that could not be performed because source material was unavailable.

Never claim a target LLM or external roleplay/Lorebook runtime passed tests unless those tests were actually executed. Internal reasoning checks and static package checks are not substitutes for model-behavior or runtime tests.

## 7. Artifact coverage and non-goals

QA applies to the existing V3 outputs: Analysis Sheet, Character Sheet, World Sheet, Context Sheet, Scenario starting message(s), human-facing Description, and Lorebook Plan. It also validates changes made by Phase 12.

QA does not:
- require every possible output to exist;
- force a fixed section structure;
- duplicate every fact in every artifact;
- turn every inference into canon;
- generate missing Character/World/Context assets without a user request;
- execute lorebook JSON or JavaScript;
- simulate roleplay or test an ongoing narrative;
- guarantee cross-session memory;
- replace the specialist creation or refinement skill.

## 8. Completion checklist

- [ ] The correct project and target artifact were selected.
- [ ] Concept fidelity was checked.
- [ ] Applicable Bedrocks were checked, including scope and clean-list format.
- [ ] Applicable coverage validation was performed.
- [ ] Consistency validation was performed where facts or multiple artifacts are involved.
- [ ] Output-specific identity, scope, and format were checked.
- [ ] Relevant tags and their scopes were respected.
- [ ] Refinement preservation or expansion non-destructiveness was checked when applicable.
- [ ] Any safe repairs were revalidated.
- [ ] Unresolved material uncertainties were not disguised as certainty.
- [ ] No verbose QA report or command footer was appended unless requested.
- [ ] No unexecuted test or runtime validation was claimed as passed.
