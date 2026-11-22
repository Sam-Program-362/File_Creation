---
name: narrative-engine-information-transfer
description: |
  Ensures that every approved, meaningful detail from analysis is represented
  in the appropriate finished project documents and downstream handoffs.
---

# Information Transfer and Coverage

## Purpose

Prevent approved information from being lost between the Analysis Sheet and final project outputs.

The Analysis Sheet is the understanding checkpoint. It is not disposable scratch work. Once the user approves its interpretation, every meaningful approved point must be assigned to the appropriate final destination.

## Core guarantee

**No approved concept detail, context, trait, relationship dynamic, rule, intention, or project decision may become an orphan simply because a standard section is missing.**

Coverage does not mean copying every sentence into every document. It means every downstream document contains the information it needs, and the Context Sheet provides a complete integrated handoff.

## Transfer procedure

For each approved information unit, determine:

1. **Meaning:** What is the point actually saying?
2. **Status:** Is it established, supported, inferred, proposed, or unknown?
3. **Owner:** Which character, relationship, location, system, plotline, or project-wide concern does it belong to?
4. **Destination:** Which output(s) need it?
5. **Form:** Should it appear as prose, a structured detail, a custom section, a Bedrock point, or a Lorebook Plan brief?
6. **Dependency:** Does another output need the point because it affects how that output should be understood?

## Destination guidance

| Information type | Typical destination |
|---|---|
| Character-specific appearance, personality, behavior, history, abilities, limitations | Relevant Character Sheet and Context Sheet |
| World laws, geography, systems, institutions, cultures, setting facts | World Sheet and Context Sheet |
| Relationship dynamics and interaction patterns | Relevant Character/Relationship material and Context Sheet |
| Core premise, project type, intentions, narrative focus, tone, central conflict | Context Sheet; Description and Scenario when relevant |
| Confirmed Bedrocks | Dedicated Bedrocks section in every relevant artifact; Context Sheet as integrated reference |
| Conditional behavior or knowledge requiring activation | Lorebook Plan when requested/needed |
| Opening-specific scene conditions | Scenario starting message and any relevant Context Sheet context |
| Human-facing pitch, hook, or premise | Description |
| Source observations or uncertain interpretations | Analysis Sheet; only approved conclusions transfer to final materials |

Use judgment. These are routing examples, not fixed categories.

## Context Sheet completeness

The Context Sheet is the central downstream handoff for the separate AI narrator/roleplayer.

It must not merely summarize the Character Sheets. It must integrate:
- project type and scope;
- premise and narrative intentions;
- the concept's central appeal and narrative focus;
- relevant characters and their actual roles;
- relationships and dynamics;
- world and setting context;
- plot, conflict, and relevant progression context;
- tone and behavioral/interaction expectations that are part of the project;
- Bedrocks and other defining rules;
- unusual project-specific information that has no conventional section.

It is a self-contained information document, not a conversational prompt and not an analysis report.

## Analysis-to-creation conversion

Do not copy analysis phrasing into final outputs when it describes the process of interpretation.

Convert:
- “The image suggests a guarded personality” into a supported, approved character behavior only if the user accepts or requests that interpretation.
- “Observed blue-grey eyes” into a normal physical description.
- “Analysis suggests political tension” into the actual established political situation only when sufficiently supported.
- “Missing faction structure” into a coherent faction description only when the user has authorized that expansion or the Improvise tag applies.

Never upgrade uncertainty merely to make the final sheet look complete.

## Coverage matrix

Before finalizing a requested set of deliverables, perform an internal coverage check.

| Check | Question |
|---|---|
| Analysis coverage | Has each approved meaningful item been accounted for? |
| Character coverage | Are all relevant character-owned details in the right character material? |
| World coverage | Are all relevant setting rules and facts represented? |
| Relationship coverage | Are important dynamics preserved? |
| Context coverage | Can the downstream AI understand the whole project without reconstructing the chat? |
| Bedrock coverage | Are applicable Bedrocks present and obeyed? |
| Lorebook handoff | Are conditional/triggered requirements described when a Lorebook Plan is requested? |
| Scenario coverage | Does each opening reflect the relevant context without contradicting it? |
| Description coverage | Does the human-facing description represent the intended concept without analysis jargon? |

If an output is not requested, it does not need to be generated solely for the coverage check. The check assigns destinations; it does not force extra deliverables.

## When information changes

When an approved point is revised:
- identify all dependent outputs;
- update only those outputs that need the change;
- preserve unrelated content;
- do not create a new conflict by leaving dependent information stale;
- do not regenerate every asset automatically.

## Completion check

- [ ] Every approved meaningful point has a destination.
- [ ] No point was dropped because a standard section did not exist.
- [ ] Context Sheet coverage is comprehensive when that artifact is requested.
- [ ] Analysis-only uncertainty was not presented as established fact.
- [ ] Relevant Bedrocks and dependencies were transferred.
- [ ] Unrequested deliverables were not generated unnecessarily.
