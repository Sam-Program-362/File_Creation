---
name: narrative-engine-expansion-methods
status: implemented
stage: 12
---

# Expansion Methods and Development Controls

This file supports the sibling `SKILL.md` in this folder.

## 1. Expansion method selector

| Method | What it adds | Typical use | Do not use it to |
|---|---|---|---|
| Depth | More complete explanation of an existing detail | A personality trait, world rule, or relationship needs clearer meaning | Repeat the same idea at greater length |
| Behavioral | Observable manifestations, responses, examples, speech patterns | Make a character trait usable by a roleplayer AI | Invent unrelated habits or behaviors |
| Contextual | Necessary background, cause, consequence, or surrounding circumstances | Explain why an established fact exists or matters | Add unsupported trauma, secrets, or history |
| Connective | Links between established facts and systems | Clarify how a world rule affects a faction or relationship | Create a new causal chain that changes the premise without authorization |
| Structural | A new custom section or subsection | An unusual concept has no suitable existing section | Restructure the entire document |
| Breadth | Additional relevant entities, places, examples, or systems | The user asks to broaden the cast or setting | Treat Open World/Open Interaction as unlimited expansion permission |
| Operational | Steps, conditions, limits, capabilities, failure states, or procedures | Make a system, ability, institution, or rule understandable in practice | Produce executable code when only a descriptive system is requested |
| Narrative | Stakes, tensions, progression paths, consequences, hooks, unresolved threads | Develop story potential while keeping the project playable | Write the next RP turn or decide the user's character actions |
| Presentation | More engaging or clearer wording for an audience | Expand a human-facing Description | Change project canon through marketing language |

## 2. Depth allocation

Use the project's narrative priority:

- **Primary focus:** substantial expansion where requested; explain key details fully.
- **Secondary focus:** enough depth to support the primary focus and make dependencies clear.
- **Tertiary details:** concise additions that improve clarity or immersion without competing with the core concept.

If the user names a specific focus, that instruction governs the allocation within the target artifact.

## 3. Character expansion dimensions

Choose only relevant dimensions:
- concrete behavior that demonstrates an established trait;
- situational reactions and behavioral variation;
- voice, vocabulary, rhythm, verbal habits, and example lines;
- motivations and priorities already supported by context;
- contradictions, blind spots, coping, and decision patterns;
- physical features supported by source information;
- daily habits, skills, limitations, role, social behavior, or relationship-specific responses;
- history only when supplied, implied, or explicitly authorized;
- development possibilities distinguished from already-established behavior.

Do not create a generic personality checklist when the character's concept needs a different structure.

## 4. World expansion dimensions

Choose only relevant dimensions:
- how a world rule operates and where its limits lie;
- causal consequences of technology, magic, ecology, or social systems;
- location functions and relationships between places;
- institutions, factions, customs, law, economy, or governance;
- historical context that explains the present;
- practical effects on ordinary inhabitants and named characters;
- exceptions, edge conditions, failure modes, and unresolved mysteries;
- additional locations or groups only when the request and open-world scope support them.

Do not build an encyclopedia for a project that needs a contained setting.

## 5. Relationship expansion dimensions

Where relevant, deepen:
- current relationship state;
- trust, familiarity, attachment, rivalry, dependence, or power balance;
- what each party knows, misunderstands, expects, or avoids;
- recurring interaction patterns and conflict triggers;
- boundaries and points of sensitivity;
- asymmetry between how each party interprets the relationship;
- possible progression opportunities, clearly distinct from completed developments.

Do not assign feelings or intentions to a character without support or explicit authorization.

## 6. Plot and scenario expansion dimensions

Where relevant, add:
- meaningful stakes and what is at risk;
- pressure sources and obstacles;
- causal links between events;
- progression conditions or turning points;
- unresolved tensions and future possibilities;
- alternative routes that preserve the core premise;
- stronger scene context and response opportunities for a starting message.

Do not continue the roleplay after a Scenario opening. Expansion of a Scenario is still editing its opening message, not narrating subsequent turns.

## 7. Context Sheet expansion dimensions

The Context Sheet is a comprehensive information handoff. Add narrator-relevant details in the correct project section:
- premise and intended narrative experience;
- character identity, traits, voice, and boundaries;
- relationship dynamics;
- world rules and practical setting behavior;
- plot context, current situation, stakes, and unresolved threads;
- knowledge boundaries, special mechanics, and project-specific expectations;
- relevant Bedrocks.

Do not add chat-style instructions or Analysis Sheet-only headings such as `Provided Elements`, `Missing Elements`, or `Planned Expansion`.

## 8. Lorebook Plan expansion dimensions

Add or deepen only the required handoff components:
- reason a fact needs modular activation rather than staying in the main documents;
- entry purpose and exact content direction;
- primary and secondary triggers;
- constant/keyword/conditional activation intent;
- priority and insertion relationship;
- entity scope, dependencies, exclusions, and Bedrocks;
- test cases and failure modes;
- Advanced Script behavior requirements without generating source code.

## 9. Redundancy filter

Before inserting an addition, ask internally:
1. Is this information already present in the target?
2. Does the new text add a distinct fact, clearer mechanism, or useful example?
3. Is this actually relevant to the user's requested focus?
4. Does it contradict an established detail or Bedrock?
5. Would a shorter, more specific addition achieve the same purpose?

If the addition is redundant or decorative, omit it.

## 10. Improvise and Detailed interaction

- `Improvise` authorizes context completion within its explicit tag scope. It does not authorize violation of canon or Bedrocks.
- `Detailed` controls explanatory depth when supplied as a tag. It should not activate globally from ordinary conversational use of the adjective.
- Both can combine: Improvise can supply missing supporting information while Detailed controls how fully relevant material is explained.
- Neither tag authorizes filler, irrelevant expansions, or unbounded document growth.
