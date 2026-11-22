---
name: narrative-engine-context-sheet
version: 1.0.0
description: |
  Creates the comprehensive, self-contained, narrator-facing Context Sheet that
  integrates the approved concept, characters, relationships, world, plot,
  narrative intent, relevant operating context, and Bedrocks for a separate
  roleplay AI. Produces project information, not a conversational prompt or
  roleplay turn.
---

# Context Sheet Creation — Operational System

## 1. Purpose

The **Context Sheet** is the central downstream handoff document of Narrative Engine V3. It is written for a separate AI that will narrate the project, portray its characters, interpret its world, and drive the intended story or roleplay.

Its responsibility is to give that AI a complete, coherent understanding of the project as it is meant to exist. It brings the approved concept and its connected components together: project identity, premise, intentions, narrative focus, characters, relationships, world, plot, defining dynamics, tone, relevant constraints, and any unusual information that materially affects how the project should be portrayed.

The Context Sheet is more important to the downstream handoff than any individual Character Sheet or World Sheet because it explains the project as one connected whole. A Character Sheet explains a character; a World Sheet explains a setting; the Context Sheet explains how the complete project fits together and what the downstream AI needs to understand about it.

The Context Sheet is **an information document, not a conversational prompt**. It contains project facts, established conditions, character and world information, relationship dynamics, narrative configuration, and relevant operating conventions in clear, self-contained sections. It does not address the downstream AI as a conversation, explain how the engine created the document, or imitate a roleplay system prompt.

It is not:
- an Analysis Sheet;
- a short summary of the Character Sheets;
- a copy of the entire chat transcript;
- a generic instruction prompt beginning with “You are…” or “I want you to…”;
- a Lorebook Plan;
- a Scenario starting message;
- an instruction to this Narrative Engine to begin roleplaying.

## 2. Activation and scope

Activate this module for:
- `Create Context Sheet [additional instructions]`;
- `Context Sheet`;
- an unambiguous natural-language request to create the narrator-facing context/handoff sheet;
- an explicit request to regenerate or update the Context Sheet, provided the requested action is not a targeted patch refinement; route targeted edits to `refinement/patch-refinement/SKILL.md`.

The bracketed or appended text is command-local guidance unless the user explicitly makes it project-wide. It may specify the included cast, scope, output depth, focus, exclusions, target roleplay platform, or other requirements.

This module creates or updates the **Context Sheet only**. Do not automatically generate missing Character Sheets, World Sheets, a Description, a Scenario, or a Lorebook Plan. Their content may be used as inputs when available, but their generation remains a separate operation.

The Context Sheet can be requested before every other project asset has been created. In that case, build the strongest complete handoff possible from the material available. Do not block the request simply because a separate Character Sheet or World Sheet does not exist.

## 3. Required skill loading

Before generation, read:

1. `shared-systems/adaptive-sections/SKILL.md`
2. `shared-systems/information-transfer/SKILL.md`
3. `shared-systems/evidence-and-inference/SKILL.md`
4. `shared-systems/bedrocks/SKILL.md`
5. `shared-systems/tags/SKILL.md`
6. The individual tag definition files applicable to this project.
7. `analysis/analysis-sheet/SKILL.md` when an Analysis Sheet exists or is required to interpret its approval state.
8. `creation/character/SKILL.md` when Character Sheets exist or character-specific information needs interpretation.
9. `creation/world/SKILL.md` when a World Sheet exists or world-specific information needs interpretation.
10. `core/project-isolation/SKILL.md` when multiple projects are active in the same conversation.

Use existing Phase 6 analysis results and Phase 7 asset sheets as the source material; do not rerun their entire procedures unless the context supplied is insufficient to interpret an item. The Context Sheet module integrates approved findings rather than redoing all analysis or re-creating each asset.

## 4. Inputs and source handling

### 4.1 Potential inputs

Use whichever of the following are available and relevant:
- approved or current Analysis Sheet;
- user-provided original concept, brief, instructions, and corrections;
- Character Sheets;
- World Sheet;
- established relationship information or separate relationship material;
- plot, scenario premise, story outline, or other project components;
- reference-derived conclusions that have been accepted into the project;
- RP-log findings that the user has adopted as project context;
- explicit tags and auto-applied tags shown in the Analysis Sheet;
- confirmed Bedrocks and their scopes;
- project-local output preferences and narrative conventions;
- the command-local instructions attached to the current request.

Do not assume a document exists merely because the architecture contains a route for it. Use only material actually present in the active project context.

### 4.2 Source precedence

Resolve information using this order, while preserving scope and chronology:

1. The user's latest explicit correction or intentional canon revision.
2. Explicit user-provided project facts and constraints that remain current.
3. User-approved Analysis Sheet findings and decisions.
4. Existing Character Sheets, World Sheets, and other established project assets, unless superseded by a later explicit correction.
5. Strongly supported information from supplied context, references, or RP logs that has been accepted as project context.
6. Clearly authorized creative additions, including additions made under the `Improvise` tag.
7. Unconfirmed inferences and speculative suggestions, which are not promoted into project facts.

This order is not permission to silently discard earlier canon. If two current established sources materially conflict and no correction or scope distinction resolves the conflict, preserve the ambiguity and ask one concise question only when it prevents a coherent handoff. Otherwise represent the two claims with their actual scope or viewpoint.

The current command's local restrictions govern this Context Sheet generation but do not automatically change project-wide canon.

### 4.3 Approval and inclusion status

Treat explicit facts and user-approved decisions as established.

Treat an Analysis Sheet as the understanding checkpoint. If the user proceeds with `Create Context Sheet` after reviewing or refining it, use the accepted conclusions as the project basis. Do not silently promote every unapproved hypothesis, optional suggestion, or Bedrock candidate from that sheet.

An explicitly requested direct Context Sheet may be built from raw source material without an Analysis Sheet. In that case, apply the same evidence discipline internally and do not output an Analysis Sheet unless requested separately.

When `Improvise` is active within the relevant scope, the engine may complete necessary gaps creatively. Additions must fit the established premise, explicit facts, tags, and Bedrocks. Do not use Improvise to hide a premise-changing invention as a small completion.

## 5. Internal context-integration ledger

Before writing, build an internal ledger of meaningful project information. This ledger is a reasoning and coverage device; it is not normally included in the final Context Sheet.

For each information unit, identify:

- **Content:** the actual fact, trait, rule, dynamic, condition, event, intention, or preference;
- **Owner/scope:** project-wide, character, relationship, world, location, group, plotline, system, or scenario;
- **Status:** established, approved interpretation, authorized creative addition, disputed, conditional, concealed, in-world belief, or unknown;
- **Authority/source:** the strongest current source;
- **Dependencies:** what other project information it affects;
- **Narrator relevance:** why the downstream AI needs it and how it changes portrayal or narrative understanding;
- **Context destination:** the most accurate section or custom section;
- **Bedrock status:** whether it is a confirmed Bedrock and the exact scope;
- **Coverage:** whether the information is represented in the Context Sheet and any other relevant deliverable.

Do not expose the full ledger or source-status labels in the Context Sheet. Convert accepted information into natural project context. Preserve disputes, secrets, and intentional uncertainty as project information where the downstream AI needs to know about them.

## 6. Context Sheet construction procedure

### Step 1 — Resolve the active project and document scope

Identify the active project using the project-isolation system. Confirm that the Context Sheet belongs to that project only.

Resolve the command-local scope. Examples:
- `Create Context Sheet [focus on the academy storyline]`;
- `Create Context Sheet [include all established characters and world rules]`;
- `Create Context Sheet [compact handoff, but preserve all critical details]`.

Do not mistake a narrower handoff request for a permanent project reset or canon change.

### Step 2 — Collect and reconcile the project material

Gather the actual available Analysis Sheet, Character Sheets, World Sheet, relationship facts, plot information, tags, Bedrocks, and explicit user corrections.

Use the source precedence in Section 4.2. Resolve duplicate descriptions, outdated facts, local versus global scope, and conflicting claims. Preserve material ambiguities rather than inventing a resolution.

Do not copy the raw conversation wholesale. Extract what belongs in the project handoff and omit transient discussion, superseded drafts, unrelated questions, and internal workflow chatter.

### Step 3 — Establish the project's identity and premise

The Context Sheet must make the project understandable without the original chat. Establish, as relevant:
- project identity or working title;
- primary and secondary project type;
- intended roleplay/story scope;
- central premise and situation;
- what the project is fundamentally about;
- why the concept is compelling;
- its intended narrative experience and audience/player-facing premise;
- the major conditions that distinguish it from a generic example of its genre.

Do not include project labels merely to fill fields. If the concept is hybrid or unusual, describe the combination accurately instead of forcing it into one familiar genre.

### Step 4 — Express the narrative intention and focus

Translate the approved Analysis Sheet understanding into useful project context:
- central narrative appeal;
- emotional and thematic center;
- central dynamic or relationship focus;
- central conflict, tension, mystery, or driving situation;
- narrative gravity: the element that should remain most important;
- secondary material that supports the central appeal;
- intended tone, atmosphere, and dramatic texture.

These are not analysis notes. Write them as clear statements about what the project is and what defines its intended experience. Do not include phrases such as “the analysis identified,” “the concept seems to,” or “the image suggests.”

### Step 5 — Integrate the cast and character context

Include every character who is relevant to the requested project scope. The Context Sheet must not become a mere list of character names or a set of links to separate Character Sheets.

For each narrator-relevant character, include enough self-contained information for the downstream AI to portray that character correctly. Select details based on the character and narrative focus; possible dimensions include:
- identity, role, status, and function in the project;
- physical appearance and distinguishing traits when relevant to recognition or portrayal;
- personality as expressed through actual behavior;
- motivations, values, emotional patterns, contradictions, vulnerabilities, and coping behavior when established;
- characteristic actions, habits, boundaries, and decision patterns;
- voice, vocabulary, rhythm, speech habits, and tone;
- abilities, limitations, resources, and non-human or unusual properties;
- relevant history and the present consequences of past events;
- knowledge, secrets, misconceptions, and information the character does not possess;
- individual character Bedrocks and project rules that constrain that character.

Use the Character Sheet as a source for full details, but do not reduce a narrator-critical trait to a vague summary. If a character's distinctive voice depends on specific blunt language, slang, profanity, graphic sexual language, or verbal examples under `Uncensored`, preserve that voice rather than sanitizing it. Explicit sexual, violent, or dark content that defines the character or project is retained.

Do not include every decorative fact just because it exists in a Character Sheet. Include all information that materially affects how the narrator understands, portrays, distinguishes, or interacts with the character. If the downstream AI will not receive the separate Character Sheet, the Context Sheet must carry the necessary full detail itself.

Do not invent a user's/player character or insert a user persona by default. Include the user's persona only when it improves immersion, strengthens a defined dynamic, supports narrative flow, or is important to the roleplay structure. If the persona is included, preserve the user's established identity and agency accurately.

### Step 6 — Integrate relationships and dynamics

Explain the actual relationship structure, not just labels such as friend, rival, partner, or enemy.

Where relevant, record:
- how each party regards the other;
- what each party wants, fears, expects, or misunderstands about the relationship;
- trust, attachment, affection, hostility, rivalry, dependency, power balance, and emotional tension;
- differences between public behavior and private feeling;
- recurring interaction patterns and triggers;
- boundaries, unresolved disagreements, history, and turning points;
- how the relationship changes behavior or decisions.

Do not assume reciprocity. One character's affection, trust, attraction, hatred, or knowledge does not prove the other character feels the same. Preserve asymmetry, ambiguity, and conflicting viewpoints when those are part of the concept.

### Step 7 — Integrate the world and setting

Present the setting as a coherent environment in which the project takes place. Include the world elements the narrator needs to understand:
- the nature and scope of the setting;
- relevant locations and how they relate spatially or socially;
- societies, institutions, organizations, factions, and authority structures;
- relevant customs, norms, culture, social expectations, and everyday life;
- technologies, magic, supernatural mechanics, simulation rules, or other systems;
- important history and the present consequences of past events;
- resources, limitations, access conditions, laws, and environmental conditions;
- how the world shapes character behavior, conflict, and available choices.

Do not create an unrelated encyclopedia. Include only material that supports the project, but do not omit a relevant rule or mechanism because it is unusual or lacks a conventional heading.

Preserve exact numerical limits, units, conditions, exceptions, and causal relationships. A world rule should remain operationally understandable where the narrator needs to apply it; a bare list of terms is not enough when the rule's mechanism affects the story.

If `Open World` applies, describe the established setting without implying that the initial location is the only possible place. If `Open Interaction` applies, do not present the initial named cast as the only possible participants. These tags affect different scopes and must not be conflated.

### Step 8 — Integrate the plot and narrative situation

Describe the story material that is already established and necessary for the narrator:
- premise and current narrative situation;
- central conflict, stakes, pressure, or source of uncertainty;
- relevant events and their causal order;
- known turning points and consequences;
- current character goals and opposing forces;
- ongoing dynamics and unresolved story threads;
- conditions that make the narrative progress meaningful;
- important constraints on possible developments.

Do not turn the Context Sheet into a complete scripted story or decide an ending that has not been established. Preserve open narrative possibilities. Do not create a starting-message scene here; the Scenario module is responsible for that output.

When a mystery, secret, or hidden mechanism exists, distinguish the underlying truth from what each character, faction, or public audience knows. The narrator may need author-level context that characters must not act upon until they discover it.

### Step 9 — Record narrative configuration and interaction context

The downstream AI needs the project's intended narrative experience, not a generic set of instructions. Include relevant configuration as neutral, declarative information. Depending on the project, this may cover:

- **Narrative perspective:** objective third person by default, unless the user establishes another perspective;
- **Tense:** past or present, when established;
- **Tone and style:** grounded, comedic, psychological, dramatic, romantic, restrained, surreal, dark, cozy, or other project-specific qualities;
- **Pacing:** slow-burn, event-driven, fast-moving, exploratory, scene-focused, or other established rhythm;
- **Narrative focus:** relationships, internal conflict, mystery, exploration, social dynamics, survival, or another gravity center;
- **Character portrayal:** the established voices, behavioral consistency, emotional restraint or expressiveness, and important contradictions;
- **Interaction boundaries:** who controls the user's character, what counts as private thought, and what characters can know;
- **Scene and world openness:** whether cast and location scope are open or deliberately contained;
- **Formatting conventions:** only include notation, markup, or message-format rules that are established for this project or explicitly requested for the downstream roleplayer.

Express these as project values and contextual facts, not as a dialogue with the AI. For example:
- `Narrative perspective: objective third person.`
- `Tense: present.`
- `User-character agency: the user's character's dialogue, private thoughts, decisions, and voluntary actions are user-authored.`
- `Knowledge boundary: private thoughts are not available to other characters unless an established in-world ability makes them accessible.`

Avoid generic filler such as “make the story immersive” when more precise project-specific information exists. Do not add formatting conventions or narrator preferences that the user has not established, unless they are explicitly part of the V3 default being transferred for this project.

### Step 10 — Preserve special mechanics, terminology, and project-specific structures

Some projects have important information that does not fit ordinary character, world, relationship, or plot headings. Examples include:
- transformation or evolution rules;
- contracts, permissions, and access conditions;
- multiple identities, instances, bodies, or timelines;
- memory and knowledge partitions;
- social ranking or reputation mechanics;
- recurring event structures;
- narrative perspective or reality-layer rules;
- specialized terminology, titles, ranks, symbols, or units.

Create dedicated custom sections for these when the downstream AI needs them. Define unfamiliar terms clearly enough that they can be applied consistently. Do not bury a central mechanic in a generic “Other Details” section.

### Step 11 — Apply tags as project context

Load the tag system and individual definitions applicable to the Context Sheet.

Tags are creation controls, but their relevant effects may need to survive into the downstream handoff. Transfer the actual project implications rather than dumping tag documentation into the Context Sheet.

Examples:
- `Uncensored` should be reflected in the relevant character's actual vocabulary, tone, examples, and any explicit sexual/violent/dark content when that is part of their voice or the project.
- `Open Interaction` should be reflected as an open cast/participant scope, not as a claim that every possible character is already known.
- `Open World` should preserve the setting's openness without inventing an exhaustive map.
- `Detailed` should increase explanatory depth in the relevant content, not create unrelated filler.
- `Improvise` permits coherent completion of required gaps, while preserving explicit facts and Bedrocks.
- `Focus` and `Exclude` apply only within their declared scopes.

Do not include internal tag-definition explanations in the final document. The Context Sheet should contain the result of applying the tag, not a tutorial about the tag system.

### Step 12 — Add the Bedrocks section

Read `shared-systems/bedrocks/SKILL.md`.

Collect **all confirmed project-relevant Bedrocks** and place them in a dedicated `Bedrocks` section. The section must contain only the actual Bedrock statements, one point per bullet.

Do not put any explanatory paragraph, AI meta-instruction, scope note, priority wording, or enforcement procedure inside the Bedrocks section. Do not convert a Bedrock into a softer preference. Preserve exact restrictions, conditions, names, quantities, and units.

Do not promote Bedrock candidates or speculative rules to confirmed Bedrocks. If a suspected invariant is not confirmed, do not place it in the Bedrocks list. Preserve it as ordinary context only if it is otherwise established or clearly relevant.

The Context Sheet is the integrated reference point, so include every confirmed Bedrock relevant to the active project, even when individual Character Sheets or the World Sheet contain only their local subsets. The surrounding project information can explain mechanisms and context, but the Bedrocks section itself remains a clean list.

If there are no confirmed Bedrocks, omit the heading entirely. Do not create an empty section.

### Step 13 — Design an adaptive document structure

Use `shared-systems/adaptive-sections/SKILL.md`.

Choose headings only after the project information has been assembled. The structure must fit this actual concept rather than a fixed Context Sheet template.

Potential sections include, only when useful:
- Project Identity and Premise;
- Narrative Intent and Core Appeal;
- Narrative Focus and Tone;
- The Setting and Its Governing Rules;
- Character Profiles;
- Relationship Structure;
- Plot and Current Situation;
- Knowledge and Secrecy Boundaries;
- Narrative Configuration;
- Interaction and Formatting Conventions;
- Specialized Mechanics;
- Terminology;
- Bedrocks.

These are examples, not required headings. Create custom sections when the project calls for them. Merge related information when it improves comprehension, but do not blur important distinctions. Do not generate empty headings or make every small fact its own section.

### Step 14 — Write the Context Sheet as natural project information

Write a coherent, self-contained Markdown document. Use a useful title, clear heading hierarchy, and readable prose. Use lists for discrete facts and tables where comparison, hierarchy, chronology, cast overview, or rule relationships benefit from them.

The writing should:
- describe the project as an established concept;
- explain how its components relate;
- retain narrator-relevant detail rather than compressing everything into generic summaries;
- be understandable without access to the original conversation;
- use the character's name, title, or role rather than addressing the user as “you” in descriptive project prose;
- preserve exact names, titles, numbers, units, limitations, and terminology;
- distinguish objective truth, character belief, public knowledge, rumor, secrecy, and uncertainty where necessary;
- convert accepted reference-derived information into natural descriptions;
- avoid analysis-process wording and source commentary;
- avoid conversational phrases such as “Here is what you need to know,” “I want you to,” “according to the image,” or “the Analysis Sheet says”;
- avoid generic roleplay system-prompt language and direct instructions to an unnamed AI;
- avoid roleplay narration, dialogue scenes, and the opening scenario itself.

Do not include analysis-only headings or fields such as:
- `Provided Elements`;
- `Missing Elements`;
- `Planned Expansion`;
- `Observed Details`;
- `Inferred Details`;
- `Generation Direction`;
- `Source Evidence`.

Those may belong in the Analysis Sheet, not the finished Context Sheet. If a genuine story mystery or unresolved in-world fact matters to the narrator, describe it as part of the project's actual knowledge state, not as an engine-analysis gap.

### Step 15 — Perform the complete information-transfer check

Use `shared-systems/information-transfer/SKILL.md`.

Compare the current Context Sheet against the approved Analysis Sheet and all relevant existing project assets. Verify that every meaningful, approved item has a proper destination and that the narrator has the integrated context needed to understand the project.

Check at least:
- project type, scope, premise, and intentions;
- core appeal, narrative gravity, emotional/thematic focus, and central conflict;
- all narrator-relevant characters and their defining traits;
- relationship dynamics, including asymmetries and boundaries;
- relevant world facts, systems, rules, limits, and exceptions;
- plot context, causal history, current situation, and meaningful unresolved threads;
- terminology and unusual mechanics;
- narrative tone, perspective, pacing, interaction expectations, and relevant conventions;
- all applicable confirmed Bedrocks;
- effects of relevant tags;
- accepted additions or decisions made during analysis and creation.

Do not blindly duplicate every sentence or every detail from every asset. The Context Sheet must be comprehensive for the downstream narrator, not a redundant archive of all documents. However, do not merely reference a separate Character Sheet or World Sheet when the downstream AI may not have those files. The Context Sheet must stand on its own unless the user explicitly specifies that the recipient will receive the linked assets together.

Do not generate unrequested assets to satisfy coverage. If information belongs only in a separate asset and is not needed by the narrator at this level, keep its destination noted internally. The central handoff still must include all information necessary to understand the complete project.

### Step 16 — Check consistency and downstream usability

Run a final consistency pass:
- Character profiles agree with the established Character Sheets.
- World descriptions agree with the World Sheet.
- Relationships are not presented as reciprocal unless established.
- Timeline and causal order remain coherent.
- Hidden facts are not accidentally treated as public character knowledge.
- Exact world rules and numeric constraints are preserved.
- Open World and Open Interaction are represented accurately and separately.
- The Context Sheet does not contradict a confirmed Bedrock.
- The Context Sheet does not contain stale facts superseded by explicit user corrections.
- Narrative configuration reflects the actual project rather than generic preferences.
- No key item is lost because an adaptive section was unavailable.

### Step 17 — Deliver only the requested artifact

Deliver the Context Sheet directly. Do not append:
- a command menu;
- an interaction loop;
- a list of possible next commands;
- an analysis report;
- a note explaining internal skill execution.

A short clarification or completion note may appear outside the artifact only when it communicates a material limitation, unresolved contradiction, or scope choice the user needs to know. Do not add a generic footer.

## 7. Special handling rules

### 7.1 Context Sheet requested before Character/World creation

Use the Analysis Sheet and original project information directly. Construct the project-level identity, premise, narrative focus, known character context, known world context, relationships, and narrative configuration from available information.

Do not invent missing Character Sheets or World Sheets. Do not imply that assets have already been created. If a crucial fact is unknown, preserve the established ambiguity or ask only if the handoff would otherwise misrepresent the concept.

### 7.2 No Analysis Sheet exists

Directly assemble the handoff from the supplied project material. Apply source reconciliation, evidence discipline, adaptive sections, tags, Bedrocks, and coverage checks internally. Do not generate an Analysis Sheet as an unrequested side effect.

### 7.3 Only one Character Sheet exists

Build a Context Sheet for the available project scope. Do not assume that a one-character asset means the entire project has a closed cast. If `Open Interaction` applies, make the open participant scope clear.

### 7.4 No conventional World Sheet exists

Include the actual setting context from the project. A contained room, workplace, virtual environment, abstract system, or social context can be sufficient. Do not fabricate a large world structure just to fill the Context Sheet.

### 7.5 Mystery, secrets, and asymmetric knowledge

Separate:
- objective project truth;
- what an individual character knows;
- what a character believes but may be wrong about;
- what the public or a group believes;
- what is concealed from the cast;
- what remains deliberately unknown even at the project-author level.

Only use these distinctions when relevant. Never leak a secret into a character's knowledge merely because the Context Sheet itself contains it.

### 7.6 Open World and Open Interaction

Preserve the exact scope of each tag. Open World keeps the setting from being accidentally closed to one location. Open Interaction keeps the cast from being accidentally closed to the initially named characters. Neither means unlimited arbitrary invention or that every possible character/location must be listed.

### 7.7 User persona and player agency

Follow the V2 User Persona Rule where it remains relevant: include the user's persona only when it improves immersion, strengthens dynamics, supports narrative flow, or is structurally important.

When the project is intended for user-participatory roleplay, state the established user-character agency boundary as project context. The user's dialogue, private thoughts, decisions, and voluntary actions remain user-authored unless the user explicitly establishes a different arrangement. Do not invent a persona, backstory, feelings, or choices for the user.

### 7.8 Command-local output restrictions

Apply the user's current output restriction without turning it into canon. For example, a request to include only one named character in this Context Sheet narrows the document's scope; it does not erase other established characters from the project.

### 7.9 Multiple projects in one conversation

Use only the active project's information. Do not import characters, Bedrocks, locations, tags, style preferences, or assumptions from another project unless the user explicitly connects them.

### 7.10 Intentional omission

Not every fact belongs in the Context Sheet. Exclude transient conversation details, superseded drafts, irrelevant reference artifacts, private author notes that do not affect the narrator, and facts outside the requested scope. Do not omit details that materially change character portrayal, world logic, relationship dynamics, plot interpretation, or the intended narrative experience.

## 8. Worked output patterns (illustrative, not templates)

### 8.1 Relationship-led contemporary project

A relationship-centered school or workplace story may need a short project premise, the central pair's full relevant profiles, asymmetric feelings and knowledge, recurring social context, the setting's important routines, tone and pacing, and relevant interaction boundaries. It may not need a broad world history, factions, or elaborate mechanics.

### 8.2 Open-world ensemble project

An open-world ensemble may need a project premise, the central world structure, key locations and travel relationships, core systems, major organizations, established cast profiles, relationship networks, narrative focus, and an explicit statement that the known cast and locations are not exhaustive. Avoid an arbitrary catalog of every possible person or place.

### 8.3 Mystery with concealed truth

A mystery may need separate sections for the objective truth, clues and chronology, what each character knows, what each character believes, public assumptions, and the central investigative tension. Keep these knowledge boundaries explicit so the narrator does not make characters behave as though they know the answer prematurely.

### 8.4 Unusual or nonhuman project

A distributed intelligence, sentient building, living ecosystem, or abstract simulation may need custom sections for identity, instances, access, perception, memory, agency, communication, state changes, and limitations. The Context Sheet should explain the project's actual mechanics, not force it into ordinary human-character headings.

### 8.5 Incorrect patterns to avoid

- A one-paragraph summary that omits important character behavior, relationship asymmetry, world rules, or plot conditions.
- A verbatim copy of the Analysis Sheet with `Observed`, `Inferred`, `Missing`, and `Planned Expansion` sections.
- A generic system prompt addressed directly to “you” rather than a project-information handoff.
- A list of character names that points to separate files without carrying the essential narrator-facing facts.
- A Character Sheet pasted wholesale without explaining the character's role in the project or relationships with others.
- A lore encyclopedia unrelated to the actual story.
- A hidden truth written as though every character knows it.
- A Bedrocks heading containing commentary or enforcement instructions.
- A polished scenario opening placed inside the Context Sheet.
- A full set of unrelated outputs generated just because they are named in the architecture.

## 9. Completion checklist

- [ ] The Context Sheet belongs to the correct active project.
- [ ] The command-local scope has been respected.
- [ ] The document identifies the project, premise, intentions, and narrative focus sufficiently to stand alone.
- [ ] The Context Sheet integrates the relevant characters, world, relationships, plot, dynamics, tone, and special mechanics.
- [ ] It is comprehensive enough for the separate narrator/roleplayer AI and is not merely a summary of Character Sheets.
- [ ] It does not depend on the downstream AI reconstructing missing context from the original chat.
- [ ] All approved, narrator-relevant Analysis Sheet information has been transferred.
- [ ] Character voices, behaviors, motivations, and limitations remain accurate.
- [ ] Relationship asymmetry and character knowledge boundaries are preserved.
- [ ] Relevant world rules, limits, exceptions, and causal relationships are exact.
- [ ] Secrets, rumors, beliefs, and objective truths are distinguished where necessary.
- [ ] Narrative tone, perspective, pacing, interaction context, and formatting conventions are included only when established or relevant.
- [ ] Relevant tags have been applied through their actual effects, not explained as system documentation.
- [ ] Open World and Open Interaction are interpreted separately.
- [ ] All confirmed project-relevant Bedrocks are included in a dedicated section containing only the Bedrock bullet points.
- [ ] No Bedrock candidate or unsupported inference has been promoted to confirmed canon.
- [ ] Adaptive sections fit the actual project; custom sections exist where needed.
- [ ] No empty template sections remain.
- [ ] Analysis-only headings and source-process wording have been removed.
- [ ] The document is informational, self-contained, and not conversational prompt text.
- [ ] The document is not a Scenario starting message, roleplay turn, Lorebook Plan, or unrelated asset.
- [ ] No unrequested Character Sheet, World Sheet, Description, Scenario, or Lorebook Plan has been generated.
- [ ] No fixed command footer or interaction loop has been appended.

## 10. Dependencies

- `shared-systems/adaptive-sections/SKILL.md`
- `shared-systems/information-transfer/SKILL.md`
- `shared-systems/evidence-and-inference/SKILL.md`
- `shared-systems/bedrocks/SKILL.md`
- `shared-systems/tags/SKILL.md` and applicable individual definitions
- `analysis/analysis-sheet/SKILL.md` when an Analysis Sheet exists
- `creation/character/SKILL.md` when Character Sheets exist
- `creation/world/SKILL.md` when a World Sheet exists
- `core/project-isolation/SKILL.md` when multiple projects are active

## 11. Explicit output boundary

This procedure creates the **Context Sheet: the comprehensive narrator-facing project information handoff**. It does not create or execute the downstream roleplayer's system prompt, generate the opening message, continue a roleplay, or simulate the world. The Scenario, Description, Lorebook Planning, refinement, and quality modules remain separate operations.
