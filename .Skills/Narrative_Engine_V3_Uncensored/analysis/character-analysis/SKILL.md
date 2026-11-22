---
name: narrative-engine-character-analysis
status: implemented
stage: 6
implementation: operational-character-analysis-procedure
description: Analyzes character identity, behavior, psychology, motivations, voice and relationship signals without presenting unsupported interpretations as facts.
---

# Character Analysis

## Purpose

Understand how a character is defined, how they behave, what drives them, and how they function within the concept. Character analysis supports the Analysis Sheet and later Character Sheet/Context Sheet creation; it does not itself create a finished character sheet.

## Activation

Use when the project contains meaningful characters, character concepts, character relationships, or RP interactions that affect the requested output.

## Procedure

### 1. Establish character identity and role

Record the supplied name, aliases, titles, age if explicitly provided, species or nature, social/professional role, project function and other identity facts. Distinguish a character's role from their personality. If identity is unknown or deliberately hidden, preserve that.

### 2. Inventory established character material

Group the explicit information into relevant categories:
- physical and visual traits;
- personality and temperament;
- behavior, habits and mannerisms;
- values, beliefs and worldview;
- goals, needs, wants and fears;
- skills, powers, resources and limitations;
- history and formative events;
- voice and communication style;
- relationships and social role;
- boundaries, contradictions and exceptional rules.

Do not use this as a fixed output template. It is an analysis inventory to prevent details from being missed.

### 3. Analyze psychology from evidence

Look for supported patterns in stated facts, choices, dialogue and repeated behavior:
- what the character seeks or avoids;
- how they react under comfort, pressure, conflict or uncertainty;
- how they protect themselves or maintain control;
- what they value and what they compromise;
- tensions between stated beliefs and behavior;
- recurring contradictions or internal conflicts;
- likely coping strategies, only when supported.

Separate observable behavior from psychological interpretation. Do not diagnose. Do not infer trauma, abuse, mental illness, sexuality, secret motives or formative history solely from appearance, genre convention or one isolated action.

### 4. Analyze motivations at the appropriate certainty

Use a layered distinction:
- **Explicit motivation:** the user or character directly states it as true.
- **Behavior-supported motivation:** repeated decisions strongly support it.
- **Possible motivation:** a plausible explanation, but alternatives remain.
- **Unknown motivation:** not enough information.

Do not invent a hidden motivation merely to make the character seem complex. A character may be simple, direct, opaque or intentionally contradictory.

### 5. Analyze behavioral expression

Describe how traits manifest in practice. For example, do not stop at “bratty”; identify whether the character teases, challenges authority, provokes reactions, uses sarcasm, refuses to concede, or masks discomfort with humor—only where the source supports it.

Identify when behavior changes with context, power, familiarity or emotional stakes. Do not turn a situational reaction into a permanent trait.

### 6. Analyze voice

When dialogue is available, assess:
- vocabulary and register;
- sentence length and rhythm;
- bluntness, formality, sarcasm, slang or profanity;
- verbal habits and preferred forms of address;
- what the character avoids saying;
- how voice changes across relationships or emotional states.

Preserve explicit character voice. If Uncensored applies, do not sanitize relevant profanity, slang, or explicit sexual/violent language into polite euphemisms. Do not make every line profane; follow the individual voice. Explicit content that is part of the character concept is retained without moral filtering.

### 7. Analyze relationships

If interactions exist, examine:
- the actual relationship and stated history;
- trust, intimacy, dependence, rivalry or distance;
- emotional undercurrents;
- power balance and control;
- conflicting needs or expectations;
- patterns of pursuit, withdrawal, protection, provocation or avoidance;
- unresolved tension and opportunities for change.

Do not automatically assign attachment-style labels or psychological categories. Use plain behavioral description unless a technical label is requested and supported. Preserve asymmetric viewpoints and distinguish each character's beliefs from objective relationship facts.

### 8. Analyze character change and continuity

If material spans time, distinguish:
- stable core traits;
- situational behavior;
- development already established by events;
- possible future development;
- contradictions that may be intentional complexity;
- accidental inconsistencies requiring review.

Do not freeze a character at their earliest state when the source establishes change. Do not assume a temporary emotional state permanently changes their personality.

### 9. Determine gaps and safe development

Identify only gaps that affect the requested project. Use the Improvise tag when present to complete necessary supporting details; otherwise do not fill major gaps arbitrarily. A missing detail can remain unknown by design.

### 10. Capture tags and Bedrocks

Read the relevant tag definitions. Apply tags to the specific character or relationship scope. Record explicit character-specific Bedrocks; keep candidate invariants separate. Ensure no inference becomes a Bedrock without user authorization or clear establishment.

## Output to coordinator

Return findings on:
- established identity and role;
- supported personality and behavior patterns;
- motivations with certainty distinctions;
- voice and example phrasing if useful;
- relationship signals and differing perspectives;
- development already established versus possible development;
- contradictions, meaningful gaps and unknowns;
- character-scoped tags and Bedrocks;
- downstream destinations for each important finding.

The coordinator decides which findings appear in the Analysis Sheet. This module does not generate a final Character Sheet.

## Constraints

- Never infer complete personality from physical appearance.
- Never invent major trauma, secrets, motivations or relationships without support or authorization.
- Do not flatten a character into one archetype or personality label.
- Do not confuse a character's lie or self-image with objective truth.
- Do not let one log message outweigh a repeated pattern without explaining why.
- Do not assume all characters need the same psychological depth.
- Do not invent or control the user's persona.

## Completion check

- [ ] Explicit character facts are preserved.
- [ ] Behavior is separated from interpretation.
- [ ] Motivations are appropriately qualified.
- [ ] Voice is grounded in actual dialogue or explicit direction.
- [ ] Relationship analysis preserves both perspectives.
- [ ] Stable traits are separated from situational states and development.
- [ ] Tags and Bedrocks have correct scope.
- [ ] Findings have downstream destinations.
