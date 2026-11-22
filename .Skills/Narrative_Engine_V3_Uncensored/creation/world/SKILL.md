---
name: narrative-engine-world-creation
status: implemented
stage: 7
implementation: operational-world-sheet-generation-procedure
description: Creates coherent, concept-relevant World Sheets with internally consistent setting rules and adaptive structure.
---

# World Creation — Operational System

## 1. Purpose

Create a finished **World Sheet** that defines the setting the project actually needs. The World Sheet should make the environment, rules, structures, and relevant systems understandable and usable without turning every concept into an encyclopedia.

World creation is not measured by the number of locations, factions, historical eras, magic rules, or pages produced. It is measured by whether the setting supports the concept, behaves coherently, and contains the information the project requires.

A world may be a country, school, apartment building, city, planet, multiverse, virtual simulation, pocket dimension, dream environment, artificial habitat, sentient ecosystem, abstract system, or any other coherent setting. Do not assume that “world” means a conventional fantasy map.

## 2. Activation and scope

Activate for:
- `Create World`;
- `Create Setting` when the user clearly wants a finished setting document;
- a natural-language request to build or organize world/setting material.

Examples of command-local constraints:
- `Create World [only establish the academy and its internal rules]`;
- `Create World [focus on the political structure]`;
- `Create World [expand the magic system; leave the geography untouched]`;
- `Create World [make it open-world, but do not invent a main quest]`.

Treat attached instructions as local to the current generation unless the user explicitly makes them project-wide. Respect the requested scope and do not generate unrelated world regions or systems.

This module produces a World Sheet. It does not create characters, the central narrator-facing Context Sheet, Scenario starting messages, human-facing Descriptions, Lorebook Plans, or actual lorebook entries/scripts. It does not implement patch refinement; route that to `refinement/patch-refinement/SKILL.md`.

## 3. Required skill loading

Before generation, read:

1. `shared-systems/adaptive-sections/SKILL.md`;
2. `shared-systems/information-transfer/SKILL.md`;
3. `shared-systems/evidence-and-inference/SKILL.md`;
4. `shared-systems/bedrocks/SKILL.md`;
5. `shared-systems/tags/SKILL.md` and only the relevant individual tag definitions;
6. `analysis/world-analysis/SKILL.md` when available and relevant;
7. `analysis/analysis-sheet/SKILL.md` when an approved Analysis Sheet exists;
8. `analysis/reference-analysis/SKILL.md` and relevant submodules when source images, notes, or RP logs contribute world information;
9. `analysis/character-analysis/SKILL.md` only when character or relationship facts materially affect the setting's institutions, social rules, locations, or systems.

Do not load every specialist by default. Use the dependencies that apply to the requested world material.

## 4. Inputs and source precedence

Potential inputs include:
- current user instructions and command-local constraints;
- approved Analysis Sheet findings;
- explicit world descriptions, rules, lists, maps, and lore;
- world-reference, style-reference, and scenario-reference images;
- fragmented notes, documents, and RP logs;
- established characters, relationships, organizations, and plot requirements;
- confirmed Bedrocks and scoped tags;
- existing setting documents supplied for integration.

### 4.1 Resolve source precedence

Use this practical order:

1. A clear, current user correction or instruction that explicitly revises an earlier detail.
2. The latest explicit project-level facts and decisions established by the user.
3. The approved Analysis Sheet, as the accepted interpretation checkpoint.
4. Direct user-supplied source material, interpreted according to its stated purpose.
5. Strongly supported analysis findings.
6. Inferences and creative proposals, only within their permitted scope.

If two explicit world facts conflict and no clear correction is supplied, preserve the discrepancy and seek clarification when it changes how the setting works. Do not silently choose, average, or blend incompatible rules.

A command-local instruction changes only this World Sheet generation unless the user clearly states that the underlying world canon itself is changing.

### 4.2 Build an internal world ledger

For each meaningful world information unit, record internally:
- what the fact or rule means;
- its scope and where it applies;
- source and evidence status;
- whether it is permanent, temporary, disputed, historical, current, conditional, or unknown;
- its causes, conditions, limits, exceptions, and consequences where applicable;
- dependencies on other world systems or character facts;
- applicable Bedrocks and tags;
- downstream destination(s).

The ledger is a completeness aid, not a mandatory table in the final output.

## 5. World-generation procedure

### Step 1 — Determine what kind of “world” this is

First identify the setting's nature. It may be:
- a physical geographic environment;
- a social or institutional environment;
- an enclosed or bounded location;
- a constructed, digital, simulated, or virtual environment;
- a supernatural, metaphysical, dreamlike, or symbolic reality;
- a layered, branching, or multiple-reality structure;
- a living or intelligent environment;
- a hybrid of several types.

Do not begin with geography or history if those are not the actual foundation. For example, a virtual world may be governed by permissions, memory resets, simulation boundaries, and system administrators; a school-based slice-of-life project may primarily need campus layout, school rules, social environment, and daily routines.

### Step 2 — Set the necessary world scope

Choose the narrowest scope that fully supports the requested project. Consider:
- one scene or contained location;
- a recurring location or small location network;
- a building, school, workplace, estate, ship, village, or institution;
- a town, city, island, or region;
- a country, planet, or large open world;
- a universe, multiverse, or layered reality;
- an abstract or non-spatial environment.

Use the user's tags and instructions. **Open World** means the setting is not restricted to the first specified location or a closed list of places; it does not automatically require a fully mapped planet, infinite geography, or a large list of invented locations.

Do not interpret a single scene reference as proof that the entire project is limited to that scene. Conversely, do not expand a deliberately contained story into an open world.

### Step 3 — Identify the world’s narrative function

Determine what the setting must accomplish for this project. Examples:
- create intimacy, routine, or familiarity;
- create isolation, danger, or survival pressure;
- provide a system for mystery, investigation, or political conflict;
- make exploration meaningful;
- constrain or enable a character's abilities;
- generate recurring social encounters;
- provide a believable physical or institutional framework.

World details should support this function. If a system has no effect on the user's concept, character experience, plot logic, or requested world identity, it may not need to be developed.

### Step 4 — Establish the world premise and governing conditions

Define, where relevant:
- what the setting is;
- what makes it distinctive;
- what is ordinary or expected within it;
- what is unusual, exceptional, or impossible;
- who or what inhabits or operates within it;
- what boundaries, rules, or conditions shape it;
- how the setting affects the central narrative.

Do not invent a genre-defining premise, apocalypse, hidden ruler, ancient prophecy, or other major element without support or authorization.

### Step 5 — Model important world rules and systems

For every system that materially governs the setting, construct an internally consistent rule model. Use the following dimensions as needed; they are a reasoning framework, not a required visible template for every rule:

1. **Rule or principle:** What is true?
2. **Domain and scope:** Where, when, and to whom does it apply?
3. **Mechanism:** How does it operate, if the mechanism is known or needs to be designed?
4. **Conditions:** What triggers, enables, or prevents it?
5. **Limits:** What can it not do? What are its range, scale, duration, capacity, or edge limits?
6. **Costs and requirements:** What resources, risks, effort, permissions, or trade-offs are involved?
7. **Exceptions:** Which exceptions exist, and why?
8. **Consequences:** What happens when the rule operates, is broken, or fails?
9. **Knowledge status:** Is this objectively true, publicly known, institutionally believed, disputed, hidden, or unknown?

Preserve exact numbers, thresholds, units, and exception conditions. A rule such as “the colossal never walks faster than 2 km/h” must not be softened to “moves slowly.”

When a system has multiple rules, check that they can coexist. For example, a magic system that allows instant travel may undermine a geography-based isolation plot unless the travel system has a known limit, cost, access restriction, or other established constraint. Do not invent a patch automatically if doing so changes the premise; mark the contradiction or ask for direction.

### Step 6 — Develop physical space and locations only as needed

When spatial structure matters, describe:
- relevant places and their identity/function;
- relative position and connection to other places;
- scale, distance, access, travel, and barriers where they matter;
- important environmental features, climate, terrain, and resources;
- practical use, atmosphere, and sensory identity where useful;
- public, private, restricted, dangerous, or inaccessible areas;
- how characters encounter or move through the space.

Do not draw a complete map when the project needs only two recurring rooms. If geography is important, make the spatial relationships coherent. Avoid vague statements such as “the village is near the mountains” when the plot relies on exact travel feasibility.

Do not turn temporary image details into permanent location features unless the reference is intended as a world reference.

### Step 7 — Build social and cultural structures with internal logic

When society matters, define the actual structures rather than using vague labels. Consider:
- who holds authority and why;
- how decisions are made;
- how rules are enforced;
- who benefits, who is constrained, and who can challenge power;
- social classes, status, roles, obligations, and mobility;
- family, community, education, work, religion or belief, and public life only where relevant;
- customs, etiquette, language, festivals, taboos, and social expectations;
- differences between groups, regions, generations, or individuals.

Do not present one character's belief as the universal belief of an entire culture. Do not flatten a society into a single personality or moral position. Explain cultural practices through their context when the project needs that detail; avoid inventing stereotypes as shorthand.

For institutions, clarify their purpose, reach, resources, limitations, and relationship to other sources of power. A law is not meaningful only because it is written: when relevant, determine who enforces it, what happens when it is broken, and whether enforcement is consistent.

### Step 8 — Develop history and chronology when they matter

History is useful when it explains the current setting, conflict, institution, custom, technology, or character condition.

- Establish the relevant order of events.
- Preserve named dates, eras, durations, and causal relationships.
- Distinguish confirmed history from myths, propaganda, rumors, disputed accounts, and missing records.
- Explain consequences that remain active in the present.
- Do not write an extensive ancient history that has no bearing on the project.
- Do not use a historical event as a convenient explanation for every unusual feature.

If a timeline is necessary, keep it internally consistent and make relative chronology explicit when exact dates are unknown.

### Step 9 — Develop factions, organizations, and populations as functioning structures

When these elements are central, define:
- purpose and identity;
- members, leadership, and internal organization;
- resources and capabilities;
- operating methods and constraints;
- alliances, rivalries, dependencies, and internal disagreement;
- influence over locations, rules, or characters;
- what they want and what prevents them from obtaining it, if established or authorized.

Do not create a faction list merely to make a world look populated. A group should have a meaningful function in the setting or project.

For populations or species, avoid treating all members as identical. Distinguish biological traits, cultural patterns, institutional rules, and individual variation.

### Step 10 — Develop technology, magic, science, ecology, economy, and daily life only when relevant

For any major system, describe the operating principles and practical consequences. Depending on the concept, this may involve:
- availability and distribution;
- access and ownership;
- cost, scarcity, maintenance, and failure;
- who understands or controls it;
- how it changes ordinary life;
- interaction with law, culture, geography, conflict, or other systems;
- limitations and edge cases.

A technology or supernatural concept should not be treated as a decorative list of powers or devices. Explain how it functions in the world when that matters. Equally, do not design elaborate economics, ecology, or scientific rules for a project that does not rely on them.

### Step 11 — Check internal consistency and causal dependencies

Review the world ledger and test for:
- rule contradictions;
- incompatible chronology or distances;
- impossible resource or logistical assumptions;
- institutions that lack a plausible way to exercise the authority attributed to them;
- systems whose effects undermine other established systems;
- exceptions that accidentally swallow the rule;
- facts that are true only in one region or period but are being applied universally;
- differences between objective reality and what inhabitants believe.

When a contradiction is genuine:
1. Check whether one fact is explicitly a later correction.
2. Check whether the facts can both be true under different scopes, conditions, times, or perspectives.
3. If not, preserve the conflict and ask a concise question when the resolution materially affects the world.
4. Do not invent a new exception merely to make all facts appear compatible.

### Step 12 — Integrate character and plot dependencies without duplicating assets

Use character and project context only where it changes how the world works or is experienced.

Examples:
- A character's title may need a corresponding institution or social status in the world.
- A character's supernatural ability may require a world rule explaining how such abilities are treated, if that is relevant.
- A political conflict may need the institutions, jurisdiction, and power structure that make it possible.
- A relationship may be affected by law, custom, class, or location access.

Do not generate complete character biographies inside a World Sheet. Do not repeat the entire plot in the world document. Capture the setting side of the dependency and leave character-owned information in the Character Sheet. The later Context Sheet will integrate both.

### Step 13 — Handle intentional gaps and Improvise correctly

A missing world detail does not always need to be invented. It may be irrelevant, deliberately unknown, or intentionally left open for the downstream narrator.

Without **Improvise**:
- leave harmless or intentional gaps open;
- do not invent major wars, ancient histories, rulers, laws, factions, cultures, or world mechanisms without support or authorization;
- ask only when the missing decision materially affects coherence or the requested output;
- avoid a `Missing Elements` heading in the final World Sheet.

With **Improvise**:
- create necessary supporting systems and connective facts so the world functions coherently;
- complete relevant environmental, social, institutional, historical, and mechanical details when the concept needs them;
- remain consistent with explicit information, tags, and Bedrocks;
- avoid premise-changing inventions unless the user has authorized broad reimagining;
- do not include a `Missing Elements` section in the Analysis Sheet or World Sheet;
- preserve deliberate mysteries and concealed facts unless the user asks to reveal them.

### Step 14 — Apply tags and Bedrocks

Load the relevant tag definitions and apply their exact behavior and scope.

- **World Reference:** prioritize environmental, spatial, architectural, cultural, and atmospheric features intended as world material.
- **Scenario Reference:** keep temporary scene conditions out of permanent world lore unless specifically requested.
- **Style Reference:** use style and mood without inventing setting facts from purely aesthetic cues.
- **Open World:** do not imply that the first named place is the only possible location. Keep room for relevant expansion without fabricating an arbitrary atlas.
- **Open Interaction:** do not assume the initial cast is the entire population or only possible participants; this tag concerns interaction/cast scope, not necessarily geography.
- **Improvise:** complete required world details according to Step 13.
- **Detailed:** substantially expand relevant descriptions and explanations.
- **Focus / Exclude:** prioritize or disregard only the scoped elements specified.

Read `shared-systems/bedrocks/SKILL.md`. Include applicable Bedrocks in a dedicated section containing only the exact Bedrock points as a list. Do not put instructions or explanations inside the section. Preserve all exact limits and conditions in the world prose too; the list alone does not replace explaining how a world system works.

### Step 15 — Choose the adaptive World Sheet structure

Use `shared-systems/adaptive-sections/SKILL.md`.

Create sections from the setting's natural information groups. Possible headings may include:
- World Identity and Premise;
- Physical Structure and Regions;
- Locations and Spatial Relationships;
- The Simulation Architecture;
- Laws of Manifestation;
- Government and Jurisdiction;
- Social Order and Customs;
- Magic or Technology Rules;
- Resources and Daily Life;
- Historical Events and Current Consequences;
- Factions and Power Relations;
- World-to-Character Constraints.

These are examples only. A small, grounded location may need three sections. A complex alternate reality may need a custom ontology, layered-reality model, access rules, and transformation mechanics. Do not use headings that do not serve the actual world.

### Step 16 — Write the World Sheet

Write a coherent, self-contained Markdown document. Put the world identity and the most important governing structures early. Describe rules in plain, exact language. Use tables only when they improve comparison, chronology, hierarchy, or rule clarity.

The finished sheet should:
- describe the world as a real project setting, not as an analysis of a reference;
- define the systems that matter to the concept;
- preserve facts, limits, exceptions, and causal dependencies;
- explain unfamiliar mechanisms sufficiently for a reader to understand their practical effects;
- avoid unrelated lore and decorative encyclopedic expansion;
- distinguish in-world beliefs from objective truth when important;
- avoid addressing the reader as “you” unless requested;
- avoid roleplay prose, dialogue scenes, and starting messages.

Do not write a global roleplay system prompt disguised as worldbuilding. The later Context Sheet can integrate world information with narrator-facing project context.

### Step 17 — Complete information transfer

Use `shared-systems/information-transfer/SKILL.md`.

For each approved world-relevant item:
- verify that it is represented in the World Sheet;
- identify whether it also affects a character, relationship, plot, Context Sheet, Description, Scenario, or Lorebook Plan;
- ensure relevant dependencies are recorded for those later deliverables;
- avoid duplicating entire unrelated assets;
- do not generate unrequested deliverables solely to demonstrate coverage.

### Step 18 — Validate and deliver

Run the checklist below. Correct contradictions, omitted approved information, scope errors, and Bedrock violations before finalizing. Deliver the World Sheet directly without a fixed command footer.

## 6. Scope and depth calibration

Use the user's project type, expected use, focus tags, and command-local requirements to set development depth.

### Contained setting

For a single room, home, office, café, school building, ship, or similar bounded environment, prioritize:
- layout and relevant spaces;
- access, privacy, and movement;
- routines and social rules;
- environmental atmosphere;
- important objects or systems that affect interaction;
- relevant constraints and recurring uses.

Do not invent the entire city or country's history unless needed.

### Recurring local setting

For a town, campus, workplace, estate, or small region, add the relevant neighborhoods, routes, institutions, public/private spaces, and social organization. Explain how the locations relate rather than producing disconnected descriptions.

### Broad world or open world

For a wide setting, define the major regions or layers, travel/access relationships, distinctive system rules, relevant societies, and meaningful boundaries. Use a hierarchy: establish the overall structure first, then expand only the locations and systems needed by the concept. Do not imply that a brief map is exhaustive when Open World applies.

### System-driven or speculative world

Prioritize ontology, governing mechanics, rules, access, costs, limits, exceptions, state changes, and interaction among systems. Geography and history may be secondary or irrelevant.

## 7. Worked output patterns (illustrative, not templates)

### Small slice-of-life environment

A recurring café setting may need its identity and atmosphere, layout, operating rhythm, staff/customer routines if relevant, nearby context, and the social conditions that make recurring encounters plausible. It does not need a royal history, a world map, or a complex faction system.

### Large fantasy or science-fiction setting

A large setting may need a clear world premise, regions and travel relationships, power structures, social differences, relevant history, technological or magical rules, and the consequences of those systems. Do not create dozens of named kingdoms unless the concept benefits from them.

### Unusual abstract or simulated world

A simulation may need sections such as `Reality Layers`, `Instance Creation`, `Memory Persistence`, `Access Permissions`, `System Authority`, and `Failure Conditions`. A dream-world may need `Dream Logic`, `Transition Rules`, `Persistence`, and `Awareness Boundaries`. Do not force either into conventional physical geography.

### Incorrect patterns to avoid

- A full generic fantasy encyclopedia for a two-character apartment romance.
- A list of magic abilities with no rules, limits, costs, or consequences when the plot depends on them.
- A government with absolute power but no defined reach, enforcement, or constraints when those details matter.
- Treating one reference image's weather or background crowd as permanent world canon.
- Applying one character's beliefs to an entire society.
- Making Open World mean “invent everything everywhere.”
- Patching contradictions with arbitrary exceptions without user approval.

## 8. Completion checklist

- [ ] The correct active project and requested world scope were used.
- [ ] The setting's actual nature was identified before conventional worldbuilding categories were chosen.
- [ ] The World Sheet supports the concept and narrative focus rather than becoming an unrelated encyclopedia.
- [ ] All explicit facts, approved analysis findings, and source-derived world details are preserved.
- [ ] Contradictions were resolved only through clear user correction or compatible scope; unresolved material conflicts remain visible or are clarified.
- [ ] Important rules include their domain, conditions, limits, exceptions, and consequences where relevant.
- [ ] Numerical constraints and units are exact.
- [ ] Geography, chronology, institutions, culture, technology, magic, and resources are developed only to the needed depth.
- [ ] Objective facts are distinguished from beliefs, myths, and rumors where necessary.
- [ ] Cultural and population descriptions preserve internal variation and avoid unsupported stereotypes.
- [ ] Open World and Open Interaction are interpreted separately and within scope.
- [ ] Improvise and Detailed behavior is correct when those tags apply.
- [ ] Applicable Bedrocks are obeyed and the visible Bedrocks section contains only the points themselves.
- [ ] Adaptive sections fit the world; no important information was omitted because a standard heading was unavailable.
- [ ] World information is not unnecessarily duplicated from Character Sheets or plot material.
- [ ] Analysis/source commentary has been converted into natural world information.
- [ ] Relevant downstream destinations have been identified.
- [ ] No unrequested Character Sheet, Context Sheet, Description, Scenario, or Lorebook Plan was generated.
- [ ] The output is a World Sheet, not a roleplay narration or AI instruction prompt.

## 9. Dependencies

- `shared-systems/adaptive-sections/SKILL.md`
- `shared-systems/information-transfer/SKILL.md`
- `shared-systems/evidence-and-inference/SKILL.md`
- `shared-systems/bedrocks/SKILL.md`
- `shared-systems/tags/SKILL.md` and applicable individual tag files
- `analysis/analysis-sheet/SKILL.md`
- `analysis/world-analysis/SKILL.md`
- `analysis/reference-analysis/SKILL.md` and relevant submodules when source material is supplied
- `analysis/character-analysis/SKILL.md` when character or relationship structures materially affect the setting

## 10. Explicit boundary

This procedure creates the **world asset**. It does not create the complete project handoff for another roleplayer. The Context Sheet remains a separate deliverable and must integrate the world with the project's concept, characters, relationships, plot, intentions, and other relevant material.
