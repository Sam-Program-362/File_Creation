---
name: narrative-engine-rp-log-analysis
status: implemented
stage: 6
implementation: operational-rp-log-analysis-procedure
description: Extracts canon-relevant events, character behavior, relationships, voice and narrative patterns from RP logs while preserving role and source distinctions.
---

# RP Log Analysis

## Purpose

Analyze roleplay transcripts as evidence of what happened, what characters said or did, how relationships and situations developed, and what the user wants to preserve for a new or reconstructed project.

An RP log is not automatically a complete or objective record of the world. It may contain unreliable narration, character beliefs, improvisation, retcons, OOC commentary and temporary scene details. Preserve those distinctions.

## Activation

Use when the user supplies RP logs, roleplay transcripts, chat exports, scene excerpts or conversation records as source material for a project.

## Procedure

### 1. Identify transcript structure

Determine, where possible:
- participants and character names;
- which participant controls which character;
- narrator or system-generated text;
- chronology and message order;
- in-character versus out-of-character content;
- explicit RP formatting conventions.

If authorship or character control is unclear, mark it uncertain. Do not assume every first-person statement belongs to the same character.

### 2. Separate transcript channels

Distinguish:
- narration/actions;
- spoken dialogue;
- private thoughts, if explicitly represented;
- OOC notes, planning, jokes or corrections;
- system/tool text or formatting artifacts.

Respect the transcript's own notation. If the user uses the four-format convention from V2, treat asterisk narration, quoted dialogue, triple-backtick thoughts and `//` comments according to their stated meaning. Do not interpret OOC comments as in-world events. Do not expose one character's private thoughts to other characters as knowledge.

### 3. Build an event sequence

Extract material events in chronological order. For each event, record:
- who acted;
- what happened;
- where and when, if known;
- who witnessed or knew it;
- immediate outcome or consequence;
- whether the event is confirmed, narrated, claimed, remembered, imagined or disputed.

Do not count every sentence as a separate event. Group continuous actions into meaningful beats. Preserve important turning points.

### 4. Extract character behavior and voice

Look for repeated, context-supported patterns:
- typical reactions and choices;
- communication style, vocabulary, rhythm and verbal habits;
- recurring gestures or habits;
- coping or conflict behaviors;
- demonstrated skills, boundaries and limitations;
- values or motivations made evident through choices;
- contradictions between self-description and behavior.

A single unusual response is not automatically a stable trait. Distinguish deliberate roleplay performance, temporary emotion and consistent character pattern. Do not infer a diagnosis, trauma history or hidden motivation from a few exchanges.

### 5. Reconstruct relationship development

When relevant, track:
- initial relationship state;
- trust, familiarity, attachment or distance;
- shifts in power, dependence or responsibility;
- conflict, reconciliation, betrayal, care or avoidance;
- unresolved tension and unspoken expectations;
- what each character knows or believes about the other.

Do not reduce a complex relationship to a single adjective. Preserve asymmetric perspectives: two characters may interpret the same event differently.

### 6. Extract world and continuity information

Identify locations, institutions, rules, objects, abilities, social structures and other world facts introduced or used in the logs. Distinguish:
- facts established by the project or narrator;
- claims made by characters;
- rumors or disputed statements;
- improvised details that may be temporary;
- facts the user explicitly confirms as canon.

A temporary event does not automatically establish a permanent world rule. An object used once is not automatically permanent equipment. A location visited once does not imply it is the project's only location.

### 7. Identify plot and progression

Extract the central situation, active conflicts, goals, obstacles, decisions, consequences, unresolved threads and likely continuation points. Do not continue the RP. The purpose is to reconstruct context for project creation.

### 8. Detect continuity conflicts

Check for:
- changed names, roles or character traits;
- chronology or location inconsistencies;
- forgotten knowledge or impossible character awareness;
- repeated or contradictory events;
- changes that may be intentional development versus accidental inconsistency;
- OOC corrections or retcons that supersede earlier material.

Treat explicit user OOC correction as authoritative when it clearly revises the project. Do not let an in-character statement override established canon unless the story establishes it as true.

### 9. Summarize what matters for the requested project

Do not dump the complete transcript back to the user. Prioritize information that is necessary for the requested Analysis Sheet or project assets. Preserve details likely to matter later even if they are not part of the central plot, such as a distinctive voice pattern, a critical boundary or a Bedrock.

Return:
- participant/character mapping;
- chronology and key events;
- character behavior/voice findings;
- relationship development;
- world facts and disputed claims;
- plot threads and unresolved tensions;
- knowledge boundaries (who knows what);
- OOC corrections/retcons;
- likely downstream destinations and uncertainty.

## Privacy of character control

Do not assign the user's character's thoughts, feelings, dialogue, choices or actions beyond what the user actually wrote. Do not convert another character's private thoughts into facts known to the user's character. This rule is particularly important when logs are used to prepare a starting message for a separate roleplayer.

## Completion check

- [ ] Speakers, characters and control boundaries are identified where possible.
- [ ] In-character and OOC content are separated.
- [ ] Event order and consequences are reconstructed.
- [ ] Character pattern findings are based on repeated or explicit evidence.
- [ ] Relationship changes preserve differing perspectives.
- [ ] Character knowledge boundaries are maintained.
- [ ] Temporary scene details are not automatically made permanent canon.
- [ ] User corrections and retcons are respected.
- [ ] Only relevant findings are passed to the Analysis Sheet coordinator.
