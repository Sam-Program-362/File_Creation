---
name: narrative-engine-description-generation
version: 1.0.0
description: |
  Creates human-facing Markdown descriptions of a roleplay concept, full project,
  world, plot, or narrative. Presents the approved concept clearly and engagingly
  for people. It is not a narrator prompt, Context Sheet, Analysis Sheet, or
  Scenario starting message.
---

# Description Generation — Operational System

## 1. Purpose

This module creates a **human-facing description** of a roleplay concept, plot, world, or complete narrative project. The reader is a person who wants to understand what the project is, what makes it interesting, and what kind of experience or story it presents.

A Description communicates the project's overall concept, narrative premise, world, central appeal, and relevant dynamics in clear Markdown prose. Its structure and depth adapt to the subject and intended use.

The Description is **not**:
- a Context Sheet shortened;
- a Character Sheet or World Sheet reproduced as a catalogue;
- an Analysis Sheet or explanation of how the engine interpreted the sources;
- a prompt or instruction block for another AI;
- a Scenario starting message or roleplay turn;
- a lorebook plan or technical implementation document.

The output should read like a coherent piece of project presentation written for people. It should explain the concept, not tell a separate AI how to behave.

## 2. Activation and command contract

Activate for:
- `Create Description`;
- `Create Description [additional instructions]`;
- a clear natural-language request to write or prepare a human-facing description of the active roleplay concept, plot, world, setting, or project.

The command's bracketed or appended instructions are command-local by default. They may specify:
- subject or scope (whole project, world, plot, selected relationship, or other component);
- intended audience or destination (public listing, project page, private overview, sharing with collaborators, etc.);
- length or character limit;
- tone, style, reading level, or language;
- whether the description should be spoiler-light or include the full plot;
- sections or information to emphasize or omit;
- whether the output should be a short blurb, a synopsis, or a comprehensive description.

These instructions govern this Description only unless the user clearly makes them project-wide.

### Default behavior

If the command provides no additional constraints:
- describe the complete central concept at a useful, moderate level of detail;
- use clear, natural Markdown prose;
- write for a general human reader;
- foreground the concept's defining appeal and narrative premise;
- include enough setting, character, relationship, or conflict context to make the premise understandable;
- avoid revealing clearly marked secrets or major twists that are not necessary to understand the public-facing premise;
- do not ask for an audience or format preference unless the missing distinction would materially change the deliverable.

Do not interpret the default as a rigid word count or fixed section template. Scale the output to the amount and complexity of the approved project information.

## 3. Scope and boundaries

This module creates a Description and nothing else unless the user separately asks for another deliverable.

It does not automatically:
- generate missing Character Sheets or World Sheets;
- generate or update the Context Sheet;
- generate a Scenario or opening message;
- create a Lorebook Plan;
- revise the Analysis Sheet;
- patch existing assets through a general refinement operation;
- invent a complete plot or new world merely because the user asked for a description.

It may consult existing project assets as source material, but it must not silently regenerate them. If a requested subject has insufficient source information, describe only what is established and supported. Ask one concise question only when the missing information prevents a useful description or changes its fundamental subject.

## 4. Required skill loading

Load:

1. `creation/description/SKILL.md` — this procedure.
2. `shared-systems/information-transfer/SKILL.md` — coverage and preservation of approved project information.
3. `shared-systems/adaptive-sections/SKILL.md` — choose a structure appropriate to the Description's subject and intended reader.
4. `shared-systems/evidence-and-inference/SKILL.md` — keep facts, accepted interpretations, and unsupported possibilities distinct.
5. `shared-systems/bedrocks/SKILL.md` — ensure the Description does not contradict core project invariants.
6. `shared-systems/tags/SKILL.md` and only the individual tag definitions that apply to the Description's scope.
7. `core/project-isolation/SKILL.md` when more than one project exists in the active conversation.
8. Relevant current project assets (Analysis Sheet, Character Sheets, World Sheet, Context Sheet, relationship or plot material) only as needed to describe the requested subject.

Read `INDEX.md` when the route or module status is uncertain. Do not load unrelated generation skills in full when the approved source document already provides the needed information.

## 5. Resolve project, subject, audience, and purpose

Before writing, determine four things:

### 5.1 Active project

- Resolve the active in-session project namespace.
- Do not borrow characters, facts, Bedrocks, tags, themes, or setting details from another project.
- If the user names a project or artifact, use that exact target.

### 5.2 Description subject

Identify whether the Description concerns:
- the entire roleplay project;
- the central roleplay concept;
- the plot or narrative premise;
- the world or setting;
- a particular arc, faction, relationship, location, or other defined component;
- a combination of these.

Do not narrow a whole-project request to one character or setting detail. Do not expand a world-only description into an unrelated plot pitch.

### 5.3 Intended reader and use

Infer the audience from explicit instructions and context. Common uses include:
- a public roleplay listing or discovery page;
- a project page or shareable overview;
- a full concept or narrative synopsis;
- a world introduction;
- a collaborator-facing explanation.

If the user does not specify a destination, write for a general reader who has no prior knowledge of the project. Do not assume a particular platform, character limit, rating convention, or marketing format.

### 5.4 Scope of disclosure

Determine whether the user wants a spoiler-conscious presentation or a complete plot explanation.

- For a public-facing overview with no spoiler instruction, focus on the premise, central tension, character/world appeal, and the question or situation that draws a reader in. Avoid revealing explicitly protected secrets and major twists that are not necessary to explain the premise.
- For a requested full plot synopsis, comprehensive narrative description, or explicit spoiler-inclusive description, include the established plot developments and outcomes relevant to that requested scope. Do not conceal information merely because it is a twist if the user specifically asked for the full plot.
- Do not expose private character knowledge, hidden identities, or secrets in a public-facing description merely because they appear in internal project material. Check whether they are meant to be known by the intended reader.
- Never invent a twist, ending, reveal, or secret to make the description more dramatic.

If the user's requested scope is clear, follow it without asking. If it is genuinely ambiguous and disclosure would materially change the result, ask one brief clarification or choose the least revealing useful treatment and make the scope evident in the heading (for example, `Spoiler-light overview`).

## 6. Gather and reconcile source information

### 6.1 Collect relevant sources

Use whichever of these exist in the active project:
- latest explicit user concept, notes, corrections, and instructions;
- approved Analysis Sheet, especially the Core Concept, Core Appeal, Narrative Focus, Core Emotion, Core Dynamic, Core Conflict, Core Theme, and Generation Direction;
- current Character Sheets for defining character roles, traits, voices, and dynamics;
- current World Sheet for setting, systems, laws, cultures, and locations;
- current Context Sheet for the integrated project premise, intentions, tone, dynamics, and overall narrative configuration;
- approved relationship, plot, arc, or scenario-premise material;
- explicit and applicable tags;
- confirmed Bedrocks and any established disclosure/knowledge boundaries.

Do not assume an artifact exists simply because its module exists. Use the available approved material.

### 6.2 Source precedence

Resolve conflicts in this order:

1. Latest explicit user correction or intentional canon revision.
2. Current explicit user-provided facts and constraints.
3. Latest approved artifact that owns the information: latest Character Sheet for character facts, latest World Sheet for world facts, and latest Context Sheet for integrated project-level context. A newer approved domain-specific asset supersedes an older copy of that detail in a Context Sheet.
4. Other current approved relationship, plot, event, or project material.
5. Approved Analysis Sheet findings and decisions.
6. Source observations and interpretations accepted into the project.
7. Creative additions expressly authorized by the `Improvise` tag or current command.
8. Unapproved inferences and speculative possibilities, which are not to be presented as established facts.

This precedence does not permit silent deletion of conflicting information. If a material conflict cannot be resolved by update order, scope, or chronology, omit the disputed detail when the Description can remain accurate without it. Ask for clarification only when the conflict changes the core premise or requested claim.

### 6.3 Transfer and approval discipline

- Include every approved, meaningful detail that is necessary to explain the requested subject.
- Do not copy every detail from every source merely to prove coverage. Select information according to audience and purpose.
- Do not upgrade an inference, candidate, or proposal into fact to make the prose feel complete.
- Do not expose analysis-only language such as `the image suggests`, `inferred from`, `observed`, `the analysis indicates`, or `planned expansion`.
- Convert approved source findings into natural, reader-facing statements.
- Do not include details excluded by the applicable reference tags.

## 7. Identify the concept's presentation core

Before drafting, internally identify the smallest set of ideas that makes this project recognizable and interesting. Use the Analysis Sheet when available; otherwise derive only what the current approved information supports.

Determine:

1. **Subject identity:** What is being described?
2. **Central premise:** What is the situation, world condition, or narrative setup?
3. **Distinctive appeal:** What makes this concept different, compelling, unusual, emotionally engaging, or worth exploring?
4. **Narrative focus:** What naturally draws attention—character, relationship, conflict, mystery, exploration, atmosphere, social system, survival, or another element?
5. **Main dynamics:** Which relationships, opposing forces, social structures, or recurring tensions shape the experience?
6. **Stakes and uncertainty:** What can change, be lost, discovered, challenged, or pursued, if established?
7. **Reader expectation:** What kind of story or roleplay experience does the premise promise?

Do not force all seven into visible headings. They are a content-selection guide, not an output template.

A Description should make clear what the project is and why its defining premise matters. Avoid vague claims such as `an unforgettable journey`, `a world full of mystery`, or `anything can happen` unless they are grounded in actual project details.

## 8. Select an appropriate Description form

Choose a form based on the requested subject and use. The forms below are options, not fixed templates.

### 8.1 Whole-project overview

Use when the user asks for the overall roleplay concept or full project description. Usually include:
- a clear title or identifying heading, if known;
- a strong opening that communicates the premise;
- the world or situation needed to understand it;
- the central characters, relationships, or forces when they are core to the concept;
- the main conflict, tension, mystery, or narrative engine;
- the defining tone, appeal, or experience;
- the roleplay's open possibilities where relevant.

### 8.2 World description

Use when the world itself is the subject. Explain the defining identity of the setting, how it works, what makes it distinctive, and which places, societies, rules, systems, or conditions matter to the intended reader. Avoid dumping every World Sheet fact. Select details that give the reader a coherent mental model of the setting.

### 8.3 Plot or narrative synopsis

Use when the story premise, plot, or narrative arc is the subject. Explain the initial situation, relevant actors, core conflict, stakes, progression premise, and important narrative dynamics. Match disclosure depth to the requested spoiler scope. Do not fabricate missing story beats or endings.

### 8.4 Short public blurb

Use when the user asks for a listing, promotional blurb, short pitch, or character-limited text. Prioritize the hook, premise, distinctive appeal, and roleplay proposition. Remove secondary exposition before removing the concept's defining identity. Honor exact length limits when requested.

### 8.5 Comprehensive project description

Use when the user explicitly asks for a detailed or complete description. It may use several Markdown headings and cover the full approved concept, setting, cast, dynamics, conflict, themes, and relevant story structure. It remains human-facing prose, not an exhaustive data dump or AI prompt.

### 8.6 Custom form

If the user's intended format does not fit these forms, create an appropriate form. Do not force a newsletter, game-store synopsis, dossier, pitch deck summary, or other format unless requested or clearly implied.

## 9. Drafting procedure

Follow this process internally. Do not print the planning steps unless the user asks for them.

### Step 1 — Establish the opening statement

Start with the clearest statement of the project's identity or hook. It should orient a reader quickly. Do not open with generic atmosphere or a string of rhetorical questions when a concrete premise is available.

### Step 2 — Explain the premise

Describe the situation that makes the project what it is. Establish who or what is central, what circumstances define the premise, and what has brought the narrative into motion. Avoid turning the description into a sequence of unexplained names.

### Step 3 — Give necessary world context

Introduce only the setting facts a reader needs to understand the premise and its stakes. Explain unusual rules or terminology when necessary. Do not overload the opening with encyclopedia-style exposition.

### Step 4 — Present central characters and dynamics

Where characters or relationships are central, explain their relevant roles and how their dynamics shape the concept. Do not reduce characters to labels or flatten complex relationships into generic descriptions. Avoid listing every character if the project is defined by a smaller central group or by an open cast.

### Step 5 — Explain the narrative tension or direction

Describe the central conflict, mystery, pressure, emotional question, social tension, survival problem, or exploration premise. Make the reader understand what gives the project forward motion. Do not invent a fixed plot path for an open or sandbox concept.

### Step 6 — Communicate the intended experience

Explain what makes the project appealing to engage with: its tone, atmosphere, dynamics, choices, exploration, mystery, emotional focus, or other distinctive qualities. Describe the experience without writing instructions to a roleplay AI.

### Step 7 — Organize for readability

Use Markdown headings, short paragraphs, and occasional lists when they help the reader. Maintain a coherent flow. Do not turn every idea into a heading. A short description may need no subheadings at all.

### Step 8 — Remove creation-process commentary

Remove internal analysis language, source provenance, tool references, drafting notes, approval-state labels, and implementation commentary. The reader should encounter the project, not the process used to assemble it.

### Step 9 — Validate factual coverage and tone

Check the complete draft against the approved project material, the user's specific command instructions, applicable tags, and Bedrocks before returning it.

## 10. Writing quality and voice

The prose should be:
- clear enough for a reader who has never seen the project files;
- specific rather than generic;
- engaging without exaggeration;
- coherent in its progression from premise to context to appeal;
- appropriately descriptive without unnecessary padding;
- consistent with the project's established tone and genre;
- written in natural human language, not system-prompt language.

Do not assume every description should sound like advertising. A quiet, intimate, bleak, clinical, mysterious, comedic, or experimental project should be presented in a voice that suits it. Use persuasive language only when the intended destination calls for it.

Avoid:
- empty hype and unsupported superlatives;
- generic fantasy, romance, mystery, or adventure clichés;
- repeating the premise in slightly different words;
- a long cast list without explaining why the cast matters;
- unnecessary exposition that does not help the reader understand the concept;
- flowery prose that obscures concrete meaning;
- overexplaining obvious details;
- describing a fixed plot for a project intended to be open-ended;
- claiming choices, branching, mechanics, or freedom that the project does not actually provide.

## 11. Detail, length, Markdown, and tags

### 11.1 Detail and length

- Follow explicit word counts, character limits, or platform limits.
- If no length is supplied, use enough detail to communicate the premise and its appeal without padding. A moderate overview is the default; complexity and available material determine its actual length.
- The `Detailed` tag substantially expands explanation and descriptive context. It does not authorize irrelevant repetition.
- A normal sentence asking for a detailed description affects the current request as an ordinary instruction, but the special built-in tag mode is activated only when `Detailed` is supplied as a tag.
- If the user asks for a short blurb, the short-form command constraint takes precedence over the tag's general preference for detail, unless the user explicitly says otherwise.

### 11.2 Markdown presentation

Use Markdown appropriate to the chosen form:
- a project title or descriptive heading when useful;
- headings for distinct topics in a longer description;
- paragraphs for the actual narrative explanation;
- bullets only for information that is naturally list-like, such as features, premise elements, or content notes;
- emphasis sparingly for key names or concepts.

Do not use Markdown headings as a substitute for coherent prose. Do not output a rigid template with empty headings. Do not wrap the entire description in a code block.

### 11.3 Tag integration

Read and apply individual tag definitions when they affect the requested Description.

- **Focus:** prioritize the specified subject or aspects. Do not omit essential context needed to make that focus understandable.
- **Exclude:** do not use excluded source details as content or supporting evidence.
- **Detailed:** increase explanatory depth while preserving readability.
- **Uncensored:** preserve blunt, vulgar, profane language, and any explicit sexual, violent, or dark content when that material is part of the project's established identity or is appropriate to the requested description. Do not sanitize or force profanity into a neutral description merely because the tag exists.
- **Improvise:** fill necessary connective gaps only within its defined scope and remain faithful to facts and Bedrocks. Do not use it to invent major plot reveals, backstory, or world rules that fundamentally alter the project.
- **Open Interaction:** describe the project's cast as open or expandable when that is part of its design; do not imply the listed characters are the only possible participants.
- **Open World:** describe the setting's openness when relevant; do not present one location as the entire world if the project is not location-locked.
- **World Reference, Scenario Reference, Style Reference, Full Physical Description:** apply only when their actual scope and information are relevant to the Description. A reference tag is not automatically a request to describe the image itself.

Auto-applied tags shown in the Analysis Sheet are not automatically global. Confirm that the tag's scope applies to this Description's subject.

## 12. Bedrocks and project constraints

Bedrocks are core project invariants. Every claim in the Description must remain compatible with applicable Bedrocks.

- Do not contradict, weaken, reinterpret, or omit a defining Bedrock in a way that misrepresents the concept.
- A Description does not need a separate `Bedrocks` heading by default. The Bedrocks list format belongs in the relevant project asset and handoff documents; a human-facing description should express relevant constraints naturally when they matter to understanding the project.
- Do not add instruction-like explanations about how the downstream AI must enforce a Bedrock.
- If a Bedrock is itself part of the concept's appeal and is appropriate for the intended reader, describe its in-world consequence naturally.
- Do not expose a hidden Bedrock if the project explicitly treats it as confidential or spoiler-protected for the intended audience.
- Never alter a Bedrock to create a smoother or more marketable description.

## 13. Special cases and edge handling

### Incomplete project material

Describe what is established. Do not fill important gaps with unsupported inventions. If `Improvise` applies, make only coherent additions within the authority granted by that tag. Never invent a major ending, secret, relationship, or premise-defining event merely to make the description feel complete.

### Open-world or sandbox projects

Present the core situation, setting, possibilities, and sources of narrative momentum. Avoid promising a fixed sequence of events, closed cast, or predetermined outcome when the project is open-ended.

### Character-led or relationship-led concepts

Prioritize the defining character traits, emotional dynamic, power balance, tension, or relationship premise. Include setting and plot context only to the extent that they support the central appeal.

### World-led projects

Prioritize the world's defining rules, identity, major systems, and the way those systems shape life or events. Do not let an incidental protagonist dominate a world-description request.

### Mystery, secrets, and hidden information

Respect the selected disclosure scope and each character's knowledge boundaries. A fact being present in the Context Sheet does not mean it belongs in a public Description.

### Multiple characters or factions

Introduce only the central figures or groups needed for comprehension. Group supporting entities by role or relationship when that is clearer than a roster. Do not imply that an open cast is closed.

### Conflicting or revised material

Use the established source precedence. If a conflict is unresolved, avoid asserting either version as fact unless the ambiguity itself is part of the approved concept.

### User asks for only a small piece

Return only the requested excerpt, blurb, section, or rewrite. Do not regenerate the entire Description.

## 14. Output contract

Return the Description itself in Markdown.

- Do not preface it with analysis or explain how it was generated.
- Do not include phrases such as `Based on your Analysis Sheet` or `According to the provided context`.
- Do not include instructions addressed to an AI narrator, bot, character, or roleplayer.
- Do not include internal source labels such as Established, Inferred, Proposed, or Unknown unless the user explicitly requests a transparent factual dossier rather than a presentation description.
- Do not append the command catalog or a fixed follow-up menu.
- Do not generate a Context Sheet, Scenario, Character Sheet, World Sheet, or Lorebook Plan as an unrequested extra.
- If the project has no established title, do not invent a formal title unless the user asks for one. A neutral heading may be used instead.

If the user requests several descriptions, generate the exact requested number and ensure each serves the specified purpose or angle. Do not add bonus variants.

## 15. Validation procedure

Before returning the Description, check:

### Subject and audience
- Is this describing the correct active project and requested subject?
- Is the intended reader clear from the writing?
- Does the form match the destination and command-local instructions?

### Concept fidelity
- Does the opening identify the project's real premise?
- Does the description communicate its distinctive appeal and central dynamics?
- Does it preserve the established tone and narrative focus?
- Has any genre stereotype or generic hook replaced the actual concept?

### Information integrity
- Are all factual claims supported by approved project information?
- Have inferences, proposals, or unknowns been presented as facts?
- Are secrets and twists handled according to the requested disclosure scope?
- Are applicable Bedrocks respected?
- Have excluded reference details been kept out?

### Audience separation
- Does it read as a human-facing description rather than a Context Sheet or system prompt?
- Is there any instruction to the roleplay AI? Remove it.
- Is there any analysis-process language? Remove it.
- Is there unnecessary raw-sheet exposition? Convert it into relevant prose or omit it.

### Writing quality
- Is the structure easy to follow?
- Is the prose specific, natural, and appropriately detailed?
- Are there repetitions, unsupported hype, clichés, or filler?
- Does the final output honor requested length and format?

Revise internally until these checks pass. Do not print a QA checklist unless the user asks for one.

## 16. Correct and incorrect patterns

### Correct — concept presentation

> **The Quiet Floor**
>
> In a city where every apartment building has one sealed floor, residents learn to live around the spaces no one is allowed to discuss. The story follows a new tenant whose ordinary move exposes the fragile agreements holding one building together. Its focus is the slow collision between private lives, neighborhood rituals, and a mystery that affects people differently depending on what they are willing to remember.

This is an illustrative example, not a required template. It presents a premise and its appeal in prose for a human reader.

### Incorrect — AI prompt disguised as a description

> You are the narrator. Remember that the city has a sealed floor. Keep the mystery active, make the residents act realistically, and never reveal the secret too early.

This is an instruction block, not a human-facing description.

### Incorrect — generic hype

> Enter an unforgettable world full of secrets, danger, emotions, and endless possibilities. Nothing will ever be the same.

This says almost nothing specific about the project.

### Incorrect — analysis leakage

> The image suggests that the protagonist may be lonely, and the analysis indicates a possible conflict with the landlord.

This exposes the interpretation process and presents uncertainty without a clear project-facing purpose.

## 17. Completion checklist

- [ ] Correct active project and subject identified.
- [ ] Audience, intended use, and disclosure scope resolved.
- [ ] Latest approved information reconciled.
- [ ] Core premise and distinctive appeal made clear.
- [ ] Relevant world, characters, relationships, conflict, and tone included in proportion to their importance.
- [ ] No unsupported facts, invented major plot beats, or unauthorized additions.
- [ ] Applicable tags and Bedrocks respected.
- [ ] Adaptive Markdown structure used; no forced empty template sections.
- [ ] Human-facing prose only; no AI instructions or analysis-process commentary.
- [ ] Requested length, style, and exact number of descriptions respected.
- [ ] No unrequested deliverables or fixed command footer appended.
