---
name: narrative-engine-coverage-validation
version: 1.0.0
status: implemented
stage: 13
description: |
  Checks that every approved, meaningful project information unit reaches the
  appropriate requested artifact and that the Context Sheet is a complete handoff.
---

# Coverage Validation

## 1. Purpose

Coverage Validation prevents meaningful, approved project information from being lost between the Analysis Sheet, source materials, and final deliverables.

It operationalizes the Information Transfer system. It does not require copying every sentence into every document. It requires each meaningful point to appear wherever it is needed by the intended reader.

## 2. Activation

Run when:

- a final artifact is generated from an approved Analysis Sheet;
- a Context Sheet is generated or updated;
- several Character, World, relationship, plot, or other assets must be integrated;
- a Lorebook Plan must carry project context into another creator;
- a canonical fact is changed and dependent outputs may become stale;
- the user explicitly requests a coverage audit.

For a small standalone output with no Analysis Sheet or multi-source context, perform a proportionate coverage check against the direct user request. Do not invent an Analysis Sheet merely to fill a coverage table.

## 3. Required inputs

- exact target artifact;
- current approved Analysis Sheet, if available;
- direct user-provided source context and approved corrections;
- current Character Sheets, World Sheet, Context Sheet, and other assets relevant to the target;
- confirmed Bedrocks and scopes;
- requested output type and command-local constraints.

If a source artifact is unavailable, mark the corresponding comparison as unavailable. Never claim full coverage from a summary when the exact approved information is not accessible.

## 4. Coverage method

### Step 1 — Extract meaningful information units

Read the applicable approved sources and identify distinct information units. A unit may be a fact, trait, behavior, relationship dynamic, world rule, plot event, premise detail, intention, tone requirement, limitation, or approved creative decision.

Do not treat every sentence as a separate unit when several sentences express one coherent fact. Conversely, do not combine unrelated facts into a broad unit that hides omissions.

Exclude from required coverage:
- rejected interpretations and superseded facts;
- unapproved proposals and unresolved possibilities;
- analysis commentary about how a detail was inferred;
- unrelated conversation and command-local instructions that do not belong in the artifact.

Retain an uncertainty marker internally where the item's approval status is unclear.

### Step 2 — Assign ownership and destination

For each unit, determine:

1. its meaning;
2. its status (established, observed, supported, inferred, proposed, unknown, or user-approved);
3. its owner (project, character, relationship, world, location, system, event, plotline, or scenario);
4. its relevant downstream audience;
5. which requested artifact(s) need it;
6. the form in which it belongs (ordinary prose, custom section, Bedrock bullet, or Lorebook Plan brief).

Use the Information Transfer destination guidance. These are routing aids, not hard-coded categories.

### Step 3 — Compare target and source

For each unit assigned to the target artifact, verify that the meaning is present and accurate. A merely similar phrase is insufficient if it changes the actual constraint, intensity, scope, condition, chronology, or relationship.

Use these internal statuses:

- **COVERED:** accurately represented in the correct place.
- **PARTIAL:** some meaning is present, but a material aspect is missing or weakened.
- **MISSING:** the target should contain it but does not.
- **MISPLACED:** present under a section or owner that distorts its meaning.
- **NOT APPLICABLE:** this artifact does not need the point; it is covered elsewhere or is outside the target's purpose.
- **UNRESOLVED:** source status or destination cannot be determined confidently.

### Step 4 — Special coverage checks

#### Analysis Sheet transfer

When a user-approved Analysis Sheet exists, verify that each approved, meaningful conclusion is assigned to its correct final destination. Do not transfer rejected, speculative, or unapproved material as established information.

#### Character and World Sheets

Confirm that all information owned by the requested character or world is represented, including unusual information that required a custom section. A standard heading is never a valid reason to drop an item.

#### Context Sheet

The Context Sheet is the central integrated handoff. It must be independently understandable by a separate narrator/roleplayer AI without reconstructing the conversation.

Check for complete coverage of all project information that materially shapes the intended narrative, including as relevant:
- project type, scope, premise, and intention;
- central concept, appeal, focus, and dynamics;
- character identities, roles, traits, behavior, voice, and relevant individual constraints;
- relationships and interaction patterns;
- world and setting facts, rules, systems, and relevant locations;
- plot situation, conflict, and progression context;
- tone and narrative configuration;
- special mechanics, terminology, knowledge boundaries, and user-character agency constraints where established;
- every project-relevant confirmed Bedrock.

Do not accept a Context Sheet that is only a compressed list of Character Sheets or a short premise summary. It must explain how the parts relate.

#### Scenario

Check only the context relevant to the requested opening(s). Each opening must preserve the scenario's applicable facts, character voices, relationships, and Bedrocks. It does not need to repeat the entire world encyclopedia.

#### Description

Check that it communicates the requested concept, world, plot, central appeal, and relevant dynamics to a human reader. Do not require confidential or spoiler-sensitive details when the selected disclosure scope excludes them.

#### Lorebook Plan

When requested, ensure the handoff contains sufficient context for the separate creator: what belongs in each Lorebook/entry, why it is needed, activation intent, scope, content direction, applicable Bedrocks, dependencies, exclusions, and tests. Do not require every project fact to be duplicated in Lorebooks when the Context Sheet is the correct home.

### Step 5 — Detect orphaned information

An orphan is an approved, meaningful information unit with no appropriate destination in the requested deliverable set. Report it internally as a coverage failure.

Do not treat information as orphaned merely because it is not repeated in an irrelevant artifact. For example, a minor physical trait need not appear in a public spoiler-light Description unless it materially defines the pitch.

### Step 6 — Repair and recheck

- Add a missing unit only to the artifact(s) that need it.
- Restore the original meaning and scope; do not embellish it while repairing coverage.
- Create a custom section if no existing section fits.
- If the unit is ambiguous or approval is unclear, do not promote it. Flag it as unresolved or ask when materially necessary.
- Re-run coverage after repairs.

## 5. Coverage failure conditions

Treat the following as material failures:
- approved core premise or narrative intention omitted from Context Sheet;
- a confirmed Bedrock omitted from a required applicable Bedrocks section;
- a character-specific defining trait or important dynamic omitted from the relevant Character Sheet;
- a world rule or defining world mechanic omitted from the World Sheet;
- an important relationship or plot condition lost during synthesis;
- an unusual project detail dropped because no template heading existed;
- an approved constraint weakened during transfer.

Severity depends on the item's importance and the output's purpose. Missing tertiary flavor in a concise Description is not equivalent to missing a core rule from the Context Sheet.

## 6. Output/report behavior

Coverage results are internal by default. Do not append a coverage matrix to normal generation.

When the user asks for an audit, provide a compact list of material omissions, partial transfers, and unresolved source items, with their correct destinations. Do not reproduce the entire source Analysis Sheet as an audit report.

## 7. Completion checklist

- [ ] All available approved source materials were inspected.
- [ ] Meaningful information units were identified without merging unrelated facts.
- [ ] Approval status and ownership were respected.
- [ ] Each unit was assigned to the appropriate requested destination(s).
- [ ] The target contains all units it needs, with accurate meaning and scope.
- [ ] Unusual details were not lost because a standard section was unavailable.
- [ ] The Context Sheet is self-contained whenever it is the target.
- [ ] No irrelevant facts were forced into unrelated outputs.
- [ ] Repairs were rechecked.
