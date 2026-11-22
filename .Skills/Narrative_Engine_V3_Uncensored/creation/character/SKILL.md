---
name: narrative-engine-character-creation
status: implemented
stage: 7
implementation: operational-character-sheet-generation-procedure
description: Creates finished, adaptive Character Sheets from approved project information and supplied source material.
---

# Character Creation — Operational System

## 1. Purpose

Create a finished **Character Sheet** that explains who the character is, how they function, how they behave, and what makes them specific to this project.

The sheet is a character reference for the user and any downstream system that needs to understand the character. It is not an Analysis Sheet, an AI-facing project-wide Context Sheet, a roleplay prompt, or a scene.

The goal is not to complete a generic biography form. The goal is to construct the most useful and concept-faithful representation of this particular character. A character may be ordinary, highly unusual, non-human, abstract, symbolic, artificial, collective, fragmented, or defined by a mechanism that conventional character templates do not describe well.

## 2. Activation and scope

Activate for:
- `Create Character`;
- `Create Characters`;
- a clear natural-language request to produce a finished character reference;
- a direct request to generate a character without an Analysis Sheet.

The command may include local instructions, such as:
- `Create Character [only Akari and Ashli for now]`;
- `Create Character [focus on physical description and speech patterns]`;
- `Create Character [include the established relationship dynamics]`;
- `Create Character [do not invent a backstory]`.

Treat attached or bracketed instructions as local to this generation unless the user clearly makes them project-wide. Respect exact requested quantity and scope. Do not expand the cast merely because additional characters would be convenient.

This module creates Character Sheets only. It does not create a comprehensive Context Sheet, a World Sheet, a scenario opening, a human-facing description, or lorebook entries. It does not implement patch refinement; route refinement to `refinement/patch-refinement/SKILL.md`.

## 3. Required skill loading

Before generation, read:

1. `shared-systems/adaptive-sections/SKILL.md`;
2. `shared-systems/information-transfer/SKILL.md`;
3. `shared-systems/evidence-and-inference/SKILL.md`;
4. `shared-systems/bedrocks/SKILL.md`;
5. `shared-systems/tags/SKILL.md` and only the relevant individual tag definitions;
6. `analysis/character-analysis/SKILL.md` when character analysis is available and relevant;
7. `analysis/analysis-sheet/SKILL.md` for the meaning and status of approved Analysis Sheet findings;
8. `analysis/reference-analysis/SKILL.md` and the relevant submodule when image, reference, fragmented-context, or RP-log evidence contributes to the character.

Do not read unrelated skills just because they exist. The root orchestrator and INDEX define availability. If a dependency is genuinely missing, work with the available source material and do not claim that the missing module was used.

## 4. Inputs and source precedence

Use all relevant information from the active project, but do not import material from another project namespace.

Potential inputs include:
- current user instructions and command-local constraints;
- the approved Analysis Sheet, if one exists;
- explicit character descriptions and notes;
- reference images and the tags specifying their intended use;
- RP logs, dialogue samples, and interaction history;
- established relationships, world facts, plot context, and Bedrocks;
- existing character material supplied for adaptation or completion.

### 4.1 Resolve source precedence

Use this practical order:

1. A clear, current user correction or instruction that explicitly revises an earlier detail.
2. The latest explicit project-level facts and decisions established by the user.
3. The approved Analysis Sheet, as the accepted interpretation checkpoint.
4. Direct source material supplied by the user, interpreted according to its stated purpose.
5. Strongly supported findings from analysis.
6. Inferences and creative proposals, only within their permitted scope.

This is not permission to discard conflicting sources. If two explicit facts remain incompatible and the user has not indicated which one is a correction, preserve the conflict and ask one concise question when it materially affects the character. Do not silently pick whichever version is easier to write.

A command-local instruction controls only the current generation. For example, `Create Character [leave the history out for now]` omits history from this output; it does not erase an established backstory from project context.

### 4.2 Build an internal character ledger

Before writing, collect the relevant information into a private working ledger. It is an anti-omission device, not a fixed output format.

For each information unit, determine:
- exact meaning;
- character owner;
- source and confidence/status;
- whether it is a permanent trait, situational behavior, temporary state, historical event, current condition, or future possibility;
- whether it is a confirmed Bedrock;
- relevant tags and their scope;
- whether it belongs in the Character Sheet, another asset, or more than one asset.

Do not expose the ledger as a mechanical table unless the user asks for one.

## 5. Character-generation procedure

Follow these steps in order. You may combine closely related steps internally, but do not skip a responsibility.

### Step 1 — Resolve the requested character set

- Identify exactly which character or characters the user requested.
- Determine whether the user expects separate sheets, a combined cast dossier, or one primary character with supporting profiles.
- Default to one clearly separated Character Sheet per requested character. Use a combined dossier only when the user asks for it or the cast is best understood as one inseparable entity.
- Do not add the user's persona, player character, NPCs, family members, rivals, or supporting cast automatically.
- If the concept itself is a collective, hive mind, dual identity, shared body, distributed intelligence, or other non-individual entity, identify that as the character's actual nature rather than forcing it into an ordinary individual profile.

### Step 2 — Establish identity and narrative function

Identify only what is known or needed:
- name, aliases, title, designation, pronouns when supplied or relevant;
- age or age range only when supplied or reliably established;
- species, nature, origin type, or form of existence;
- occupation, status, rank, social position, or role;
- role in the project and relationship to the central concept;
- any deliberately hidden, unknown, disputed, or mutable identity details.

Do not invent a name, age, title, or secret identity just to make the opening section look complete. If a character is intentionally unnamed, preserve that.

### Step 3 — Establish physical form and appearance

Use the supplied appearance information and applicable references. Separate stable physical characteristics from temporary visual conditions.

When the **Full Physical Description** tag is active, produce a genuinely comprehensive description of the visible or established body rather than a short body-type label. Cover relevant dimensions such as:
- estimated height or height range, clearly identified as an estimate when not supplied as a fact;
- overall build, frame, body type, mass distribution, and proportions;
- shoulders, neck, torso, chest or bust, ribcage, waist, abdomen, hips and pelvis;
- buttocks and lower-body shape where relevant to the character description;
- thighs, knees, calves, lower legs, ankles, and feet;
- arms, hands, fingers, and other notable structures;
- skin tone, texture, facial structure, eyes, hair, and distinguishing features;
- posture, carriage, gait, and recurring body language when evidence supports them;
- clothing, accessories, species traits, non-human anatomy, mechanical parts, or other defining physical properties when relevant.

Do not turn that list into mandatory headings. Describe the body in a coherent top-to-bottom or otherwise reader-friendly structure. Do not invent precise measurements from an image. Use calibrated language such as “appears approximately,” “likely within,” or “the reference does not establish an exact height.”

When Full Physical Description is not active, provide the degree of physical detail warranted by the user's request and the concept. A brief, non-visual character concept may not need a full anatomical inventory.

Reference interpretation rules:
- `character description` / Full Physical Description focuses on stable character appearance;
- `scenario reference` keeps scene-specific pose, expression, clothing state, injury, weather, and props within the scenario unless intended as permanent;
- `style reference` informs style, not character identity;
- `exclude` removes the selected elements from consideration;
- `focus` raises the priority of the selected information, but does not create evidence.

Do not infer personality, morality, intelligence, trauma, or motivations from facial structure, body shape, attractiveness, clothing, or other appearance alone.

### Step 4 — Construct personality as an operational pattern

Do not rely on a stack of adjectives. Translate established traits into how the character actually thinks, chooses, reacts, communicates, and treats other people.

Where supported, define:
- baseline temperament and social presentation;
- emotional expression and regulation;
- values, beliefs, principles, and personal standards;
- priorities, goals, needs, wants, and fears;
- decision-making style and typical responses to pressure;
- trust, attachment, boundaries, vulnerability, conflict, and coping patterns;
- contradictions, hypocrisy, self-image, blind spots, and situational changes;
- what makes this character distinct from others with superficially similar traits.

For each major trait, explain its observable expression. Example: instead of only writing “sharp-tongued,” establish whether the character uses cutting sarcasm, blunt insults, teasing, mock politeness, deliberate provocation, or rapid comebacks—only to the extent supported by the source.

Keep these distinctions clear:
- a stable trait is not the same as a temporary mood;
- a character's self-description is not automatically objective truth;
- a public persona may differ from private conduct;
- a stated motive may differ from a behavior-supported motive;
- contradictions can be intentional and should not be “fixed” automatically.

Do not diagnose a character or invent hidden trauma, abuse, mental illness, secrets, or motivations without support or authorization.

### Step 5 — Define behavior and interaction patterns

Translate personality into usable behavior. Include relevant patterns such as:
- habits, rituals, mannerisms, routines, and physical tells;
- behavior around strangers, allies, authority, rivals, intimates, or specific people;
- reactions to praise, criticism, rejection, uncertainty, pressure, danger, embarrassment, or affection;
- preferred ways of approaching, avoiding, testing, comforting, confronting, or controlling an interaction;
- behavioral exceptions and conditions that change the pattern.

Do not invent a long list of generic quirks. Include behaviors that distinguish the character or help a reader understand how the character acts.

### Step 6 — Define voice and dialogue behavior

Use actual dialogue samples where available. Otherwise use explicit user direction and supported characterization.

Describe, when relevant:
- vocabulary and register;
- sentence length, rhythm, pace, and verbal habits;
- directness, formality, humor, sarcasm, slang, dialect, profanity, or politeness;
- preferred forms of address and terms the character avoids;
- differences in voice across people, situations, or emotional states;
- what the character tends not to say, and how they conceal, deflect, or express emotion.

When **Uncensored** applies, preserve the appropriate bluntness, vocabulary, and explicitness in both description and examples. A sharp-tongued, bratty, crude, or sexually explicit character may naturally say “Fuck you,” “shut up,” “bitch,” “cunt,” or use graphic sexual language when that matches the established voice. Do not replace that voice with polite euphemisms or moral softening. Equally, do not make every line profane or apply one character's vocabulary to the entire cast. Sexual, violent, or dark content that is part of the character concept is retained without sanitization.

If examples are useful, write a small number of representative lines. Label them as voice examples, not events that have already happened.

### Step 7 — Build history and continuity

Include only history that helps define the character, explains a current fact, or matters to the project.

- Preserve named events, chronology, causes, and consequences.
- Distinguish remembered facts from rumors, lies, disputed histories, and deliberately unknown pasts.
- Do not invent formative trauma or dramatic secrets as a shortcut to depth.
- Do not turn possible future development into past canon.
- If the source establishes character change over time, represent the current state and relevant earlier state without flattening the arc.
- Do not reproduce every minor event from an RP log; transfer the events that materially define identity, relationships, or the current state.

A character can have no disclosed backstory. Do not force one into existence.

### Step 8 — Define capabilities, resources, and limitations

For every ability or important competence, establish the dimensions that matter to the project:
- what the character can do;
- how it works in practical terms;
- range, scale, duration, precision, reliability, or scope, when relevant;
- requirements, costs, preparation, resources, or conditions;
- limits, counters, vulnerabilities, failure states, and recovery;
- what the character cannot do;
- whether the ability is learned, innate, granted, technological, social, institutional, or otherwise sourced.

Do not make a character omnipotent or arbitrarily weak. Preserve exact user-supplied numerical constraints. Do not invent detailed combat statistics for a project that is not asking for a game-mechanics sheet.

For skills and resources, separate demonstrated competence from claimed competence, reputation, and aspiration.

### Step 9 — Define relationships without flattening them

For every relevant relationship:
- identify the actual relationship and established history;
- preserve what each character believes about the other, separately from objective facts;
- describe trust, attachment, affection, resentment, rivalry, dependence, power, obligation, or distance only where supported;
- describe how each character behaves specifically toward the other;
- retain asymmetry: two characters may understand or feel the relationship differently;
- preserve unresolved tension, boundaries, and explicit relationship rules;
- connect relationship details to other characters only when useful.

Do not invent romance, attraction, family ties, hostility, or intimacy because a genre commonly includes them. Do not assume that a relationship is equal or mutual simply because one character feels strongly about it.

If several characters are requested, keep each profile independently readable. Cross-reference shared dynamics without copying entire profiles into one another.

### Step 10 — Determine project-specific sections

Use Adaptive Sections. Select sections based on the character's actual nature and the information that needs to be retained.

Possible section types include:
- Identity and Role;
- Physical Description;
- Personality and Psychology;
- Behavior and Mannerisms;
- Speech and Voice;
- History;
- Abilities and Limitations;
- Relationships;
- Public Persona and Private Conduct;
- Social or Institutional Position;
- Anatomy or Body Mechanics;
- Artificial Intelligence Architecture;
- Transformation States;
- Rules of Manifestation;
- Collective Identity;
- Memory and Knowledge Boundaries.

These are examples, not required headings. Create a custom section whenever a detail does not fit. Merge related items when their distinctions remain clear. Do not generate empty sections or split every minor fact into a separate heading.

### Step 11 — Apply tags and authorized improvisation

Read every relevant tag definition rather than relying on the tag name alone.

- **Full Physical Description:** follow Step 3 at full depth.
- **Improvise:** fill necessary character gaps creatively and coherently; do not include a `Missing Elements` section in the Analysis Sheet. Do not contradict explicit facts or Bedrocks. Do not make premise-changing additions under the label of minor completion.
- **Detailed:** expand all relevant descriptions and explanations substantially, using clear language and sufficient context for an inexperienced reader. Maintain structure and relevance; do not pad.
- **Uncensored:** preserve the character's appropriate directness, slang, profanity, and any explicit sexual/violent/dark content without sanitization.
- **Focus:** prioritize the selected character dimensions.
- **Exclude:** do not use excluded reference or source dimensions.
- Other tags apply only within their defined scope.

Auto-detected tags are already reviewed or shown in the Analysis Sheet when one exists. Do not silently invent a tag or extend it to unrelated characters. When direct generation is requested without analysis, apply clearly relevant existing tags and use restraint with new tag inference.

### Step 12 — Design the final sheet structure

Use `shared-systems/adaptive-sections/SKILL.md` and `shared-systems/information-transfer/SKILL.md`.

- Choose the section order that makes this character easiest to understand.
- Put core identity and role early unless the project has a better entry point.
- Keep physical, psychological, historical, behavioral, relational, and mechanical information distinct where that helps comprehension.
- Use project-specific sections for unusual character mechanisms.
- Place relevant world context in the character's role or relationship to the setting without duplicating the entire World Sheet.
- Do not include Analysis Sheet-only labels such as `Observed Details`, `Inferred Details`, `Provided Elements`, `Missing Elements`, or `Planned Expansion`.
- Do not include process commentary such as “in the image,” “according to the reference,” or “analysis suggests.” Convert approved details into natural descriptions.

### Step 13 — Write the Character Sheet

Write in clear, self-contained Markdown. Use the character's name, title, or role rather than addressing the user as “you,” unless the user explicitly requests second-person language.

The finished sheet should:
- explain the character naturally rather than read like internal analysis notes;
- use concrete behavioral and descriptive language;
- contain enough information to distinguish the character;
- make important conditions and exceptions explicit;
- avoid repeating the same detail in multiple sections without a reason;
- keep speculation out of canon prose;
- avoid generic filler such as arbitrary favorite foods, random hobbies, or decorative trivia unless they support the concept.

Do not write a system prompt or narrator instructions disguised as a Character Sheet. Project facts and character behavior may be stated clearly, but global roleplay instructions belong in the Context Sheet or the appropriate later module.

### Step 14 — Insert applicable Bedrocks

Read `shared-systems/bedrocks/SKILL.md`.

If the character has applicable Bedrocks, add a `Bedrocks` section containing only the Bedrock statements as a bullet list. No explanation, enforcement instructions, priority commentary, or AI meta-instructions may appear inside that section.

Include only Bedrocks relevant to this character. Preserve the full scope and exact intended meaning. A project-wide Bedrock may appear in the character sheet when the character is directly governed by it; do not copy unrelated world rules into every character profile.

### Step 15 — Complete the information-transfer check

For every approved character-relevant information unit in the Analysis Sheet or supplied context:
- confirm it has been represented in the Character Sheet when it belongs there;
- confirm it has not been accidentally changed or omitted;
- identify information that belongs primarily in the World Sheet, Context Sheet, Description, Scenario, or Lorebook Plan instead;
- preserve cross-references needed by those later outputs.

Do not generate those other deliverables just to complete this check. This is a coverage operation, not a command to generate the entire project package.

### Step 16 — Validate and deliver

Run the completion checklist below. Correct any issue before finalizing. Deliver the Character Sheet directly. Do not append a recurring command menu or a fixed interaction footer.

## 6. Special handling rules

### Multiple characters in one request

1. Confirm the requested roster and quantity.
2. Build a separate information ledger for each character.
3. Establish individual identity, voice, and behavior before comparing them.
4. Capture shared relationships once in a useful relationship or cross-reference section when necessary.
5. Do not homogenize the cast's voices or personality patterns.
6. Check all cross-character Bedrocks and relationship constraints.
7. Ensure no information has migrated to the wrong character.

### Character with no conventional body

For a machine, deity, collective, sentient location, abstract entity, distributed process, or shapeshifter, define its form and identity according to what it is. Replace human anatomy headings with the relevant mechanics: manifestation, interface, distributed components, physical shell, avatar, perception, or state transitions. Do not fabricate a human body to satisfy a template.

### Character with intentionally incomplete or concealed information

Preserve ambiguity. Use wording such as “unknown,” “unconfirmed,” or “the character has not disclosed…” only when the reader needs to know the boundary. Do not fill deliberate mysteries under Improvise unless the user explicitly authorizes revealing them.

### Direct generation without an Analysis Sheet

Run the same internal evidence, tag, Bedrock, adaptive-section, and information-transfer checks using the supplied source material. Do not output an Analysis Sheet unless requested. If a major unresolved contradiction prevents a faithful character sheet, ask one concise question or preserve the ambiguity explicitly.

### Project and character scope

Do not treat a command-local restriction as a permanent cast restriction. Do not import another project's character traits, world rules, or Bedrocks. Do not make a character sheet the repository for every fact in the project.

## 7. Worked output patterns (illustrative, not templates)

### Ordinary character pattern

A grounded contemporary character may need only a concise identity section, a full physical description when requested, personality expressed through behavior, voice, relevant history, and the relationships that matter to the premise. It does not need a magic system, faction affiliations, or a dramatic secret merely to appear complete.

### Unusual character pattern

A character that is a distributed intelligence may need sections such as `Distributed Identity`, `Instances and Interfaces`, `Memory Boundaries`, `Communication`, and `Known Limitations`. A conventional body description may be absent or limited to the physical shell it uses. Its distinct mechanics are the character, not an exception to be hidden inside a generic personality section.

### Relationship-specific pattern

If the character's central defining feature is their conduct toward one specific person, include a dedicated section for that dynamic. Keep the character's general personality separate from the behaviors that occur only in that relationship. Preserve what is known from each side and do not invent reciprocity.

### Incorrect patterns to avoid

- “She is slim, beautiful, and mysterious” as the entire physical description when Full Physical Description was requested and the source supports more.
- “He is a tsundere” without describing the actual behaviors and speech patterns.
- A complete trauma history invented from a guarded facial expression.
- Giving a character powers without limits, cost, or conditions when those details govern the project.
- Copying an Analysis Sheet's uncertainty language into the finished sheet as if it were fact.
- Copying every world rule into every character sheet even when it does not affect the character.

## 8. Completion checklist

- [ ] The exact requested character set and count are respected.
- [ ] The character's identity and project role are accurately represented.
- [ ] Explicit facts and approved analysis findings are preserved.
- [ ] Conflicts were resolved only when the user supplied a clear correction; otherwise ambiguity is retained or clarified.
- [ ] Physical description matches the requested depth and evidence; Full Physical Description covers the supported full-body dimensions.
- [ ] Personality is expressed through concrete behavior, not only adjective labels.
- [ ] Stable traits, situational states, history, and development are distinguished.
- [ ] Voice is specific and not sanitized when Uncensored applies.
- [ ] Motivations, secrets, trauma, and relationships are not invented without support or authorization.
- [ ] Abilities and limitations preserve conditions, costs, scale, and exact constraints where relevant.
- [ ] Character-specific and relationship-specific information is correctly scoped.
- [ ] Adaptive sections fit the character; no important detail is omitted for lack of a heading.
- [ ] Applicable tags and Bedrocks are respected.
- [ ] The visible Bedrocks section contains only the points themselves.
- [ ] Analysis language and source commentary have been removed from the final sheet.
- [ ] Character-relevant information has a correct downstream destination.
- [ ] No unrequested World Sheet, Context Sheet, Description, Scenario, or Lorebook Plan was generated.
- [ ] The output is a Character Sheet, not a roleplay turn or a narrator prompt.

## 9. Dependencies

- `shared-systems/adaptive-sections/SKILL.md`
- `shared-systems/information-transfer/SKILL.md`
- `shared-systems/evidence-and-inference/SKILL.md`
- `shared-systems/bedrocks/SKILL.md`
- `shared-systems/tags/SKILL.md` and applicable individual tag files
- `analysis/analysis-sheet/SKILL.md`
- `analysis/character-analysis/SKILL.md`
- `analysis/reference-analysis/SKILL.md` and relevant submodules when references/logs are supplied
- `analysis/world-analysis/SKILL.md` when the character's setting materially affects their description

## 10. Explicit boundary

This procedure creates the **character asset**. It does not create the complete project handoff for another roleplayer. The Context Sheet remains a separate, later deliverable and must integrate character information with the project's premise, world, relationships, plot, intentions, and other relevant context.
