---
name: narrative-engine-consistency-validation
version: 1.0.0
status: implemented
stage: 13
description: |
  Checks project canon, Bedrocks, source precedence, chronology, relationships,
  character/world rules, and consistency across existing project artifacts.
---

# Consistency Validation

## 1. Purpose

Consistency Validation checks whether a deliverable agrees with the project's established information and whether it introduces contradictions within itself or against other relevant artifacts.

It is not a command to make every character, event, or source perfectly harmonious. Deliberate mysteries, unreliable accounts, secrets, conflicting beliefs, and evolving relationships may be intentional and must remain intact when supported by the project.

## 2. Activation

Run for every final project artifact where project facts or constraints are present. It is especially important when:
- multiple Character/World/Context/Scenario/Description/Lorebook Plan artifacts coexist;
- a source correction or canon change is made;
- a refinement or expansion touches established facts;
- the output contains one or more Bedrocks;
- chronology, causality, relationships, abilities, limits, or world mechanics matter.

## 3. Required inputs

- current target artifact;
- relevant current and approved project source documents;
- latest explicit user corrections and instructions;
- confirmed Bedrocks and their scopes;
- applicable tags and their scopes;
- chronology or relationship information when relevant.

Use exact available artifact text where possible. Do not assume that a remembered summary contains all current canon.

## 4. Source and canon resolution

Use the Evidence and Inference system's hierarchy: explicit tags determine reference relevance; explicit user instructions govern intended use; context informs interpretation; default assumptions are only a fallback.

For project facts, apply these practical distinctions:

1. A clear, current user correction or explicit canon revision governs within its stated scope.
2. An approved Analysis Sheet establishes the user's accepted interpretation unless later corrected.
3. Current approved Character, World, Context, and other canonical assets provide established project details within their domains.
4. Older derived outputs must not override a newer approved source when they are stale.
5. Supported interpretations may be used within their approved limits; unapproved inferences and proposals are not canon.

A confirmed Bedrock is a hard invariant unless the user clearly authorizes its revision or removal. If a new instruction conflicts with a Bedrock and the intent to revise is not clear, do not silently choose a side. Ask a concise clarification when the contradiction materially affects the project.

Do not use file modification time alone as proof that a source is canonically newer. Prefer explicit approval, user correction, and the project's stated source role.

## 5. Consistency checks

### 5.1 Bedrock integrity

For every Bedrock applicable to the target:
- verify the rule's exact meaning and scope;
- search for direct and indirect contradictions;
- confirm that the generated outcome does not violate the rule even if the wording itself is present;
- ensure no Bedrock has been weakened, broadened, narrowed, or silently omitted;
- verify that any visible Bedrocks section contains only actual Bedrock points, one per bullet;
- ensure candidates and inferences have not been promoted into confirmed Bedrocks.

A statement can quote a Bedrock correctly while the surrounding scene still violates it. Check consequences, not just wording.

### 5.2 Character consistency

Where relevant, compare:
- identity, role, age, appearance, traits, habits, and abilities;
- limitations, capability boundaries, and recurring behavior;
- motives, goals, fears, and contradictions that have been established;
- speech patterns, vocabulary, register, and Uncensored behavior where scoped;
- knowledge and secrets (what the character knows, does not know, or may only suspect);
- relationship states, history, power balance, and interaction rules.

Do not erase deliberate contradictions inside a complex personality. Distinguish a believable internal contradiction from an accidental factual mismatch.

### 5.3 World consistency

Where relevant, compare:
- world laws, mechanics, physical limits, technology, magic, and causal rules;
- geography, distances, travel constraints, locations, and spatial relationships;
- dates, eras, chronology, historical events, and cause/effect;
- institutions, factions, ranks, social structures, laws, and cultural rules;
- species, populations, abilities, resources, and constraints.

Do not invent a universal world rule from one scene unless the project establishes it as general.

### 5.4 Relationship and narrative consistency

Check:
- established relationship status and development;
- what each participant knows about the others;
- trust, hostility, dependence, conflict, and power dynamics;
- plot chronology and whether events can occur in the stated order;
- unresolved threads and secrets that should remain unresolved;
- whether a Scenario opening assumes an event or relationship progression that has not been established.

### 5.5 Cross-artifact consistency

Compare only artifacts relevant to the target. Identify:
- a stale Context Sheet that no longer matches an approved Character or World change;
- a Scenario that contradicts a world rule or character trait;
- a Description that states a superseded premise or public fact;
- a Lorebook Plan that instructs the separate creator to implement outdated behavior;
- duplicate or inconsistent naming, terminology, measurements, and roles.

Do not fabricate absent dependent documents. If an artifact is not available, mark cross-artifact validation as limited rather than claiming synchronization.

### 5.6 Scope and isolation

- Keep project information within its active project namespace.
- Do not import another project's characters, Bedrocks, events, or tags.
- Do not broaden a character- or scenario-specific constraint into a project-wide law.
- Do not convert command-local generation constraints into permanent canon.
- Preserve the user's persona/character boundary and agency rules where relevant.

### 5.7 Tag consistency

- Confirm explicit tags remain applied within their stated scope.
- Confirm auto-applied tags have evidence, a scope, and an analysis record.
- Ensure Uncensored affects the relevant character/voice rather than unrelated characters.
- Ensure Detailed is activated as a special mode only when supplied as a tag; ordinary requests for detail remain local instructions.
- Ensure Improvise does not contradict facts or Bedrocks.
- Ensure Open Interaction and Open World do not silently close the cast or setting.
- Ensure Exclude continues to remove excluded reference material from the relevant output.

## 6. Intentional inconsistency versus defect

Do not flag these as errors when the project deliberately establishes them:
- a character lies or holds a false belief;
- two sources intentionally disagree because one is unreliable;
- different factions teach conflicting histories;
- a mystery deliberately withholds the true explanation;
- a character behaves differently in public and private;
- relationships evolve over time;
- an alternate Scenario explicitly explores a different valid possibility.

Record whose belief or account is inconsistent, rather than treating the project itself as inconsistent. Preserve ambiguity when it is part of the narrative design.

## 7. Finding handling

- **BLOCK:** direct Bedrock violation, explicit canon contradiction, impossible chronology that breaks the requested output, cross-project contamination, or other material contradiction.
- **REPAIR:** clear spelling/name/number inconsistency or an obvious stale reference that can be updated without changing intended meaning.
- **WARN:** ambiguous source conflict, unclear canon status, deliberate-looking contradiction that lacks enough context, or an unavailable dependent artifact.
- **PASS:** no applicable contradiction found.

Never “fix” a BLOCK by inventing new lore or rewriting the premise. Ask or preserve the issue as unresolved when a material decision belongs to the user.

## 8. Completion checklist

- [ ] Relevant approved sources and explicit user corrections were considered.
- [ ] All applicable Bedrocks were checked for actual outcome compliance.
- [ ] Character traits, voice, abilities, limitations, and knowledge are consistent.
- [ ] World rules, mechanics, geography, institutions, and chronology are consistent.
- [ ] Relationships and narrative progression are consistent.
- [ ] Relevant dependent artifacts are not stale.
- [ ] Project isolation and command-local scope are respected.
- [ ] Applicable tags are enforced only within their scope.
- [ ] Intentional mysteries, lies, and conflicting viewpoints were not flattened.
- [ ] Unresolved conflicts were surfaced rather than silently invented away.
