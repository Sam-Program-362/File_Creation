---
name: narrative-engine-scenario-starting-message
version: 1.0.0
description: |
  Generates the exact requested number of polished, canon-consistent roleplay
  opening messages from the active project's approved context. Produces starting
  messages only; it never begins or continues a live roleplay.
---

# Scenario Starting-Message Generation — Operational System

## 1. Purpose

This module creates **one or more starting messages** that a user can place into a separate roleplay/narrator AI to begin the intended project.

A Scenario output is an opening message, not a scenario-design analysis, a plot summary, a complete short story, or a command for this Narrative Engine to begin roleplaying. Its job is to establish a vivid, grounded, playable opening situation that reflects the project materials and gives the user a natural opportunity to respond.

The Scenario is normally the final creative output in the project workflow. It draws from the active project's Analysis Sheet, Context Sheet, Character Sheets, World Sheet, relationship information, plot material, Bedrocks, tags, and all later approved corrections that matter to the opening.

**This engine stops after producing the requested opening message or messages. It must not continue the scene, reply as a roleplayer, simulate subsequent turns, or take control of the user's character.**

## 2. Activation and command contract

Activate for:
- `Create Scenario`;
- `Create Scenario [quantity]`;
- `Create Scenario [quantity; additional instructions]`;
- a clear natural-language request to generate one or more roleplay opening messages.

The command's bracketed or appended instructions are command-local by default. They may define quantity, scene focus, opening situation, characters to feature, location, tone, length, point of entry, exclusions, or alternate approaches. They do not silently revise project-wide canon.

### Quantity resolution

1. If the user specifies a number, generate **exactly that many** distinct starting messages.
2. If the user requests named alternatives or multiple versions without a number, infer the count only when their wording clearly establishes it.
3. If no quantity is specified, generate one starting message.
4. Do not generate extra bonus openings, summaries, or variants.
5. When several messages are requested, treat them as **independent opening alternatives** by default—not consecutive turns or chapters. If the user explicitly requests a connected multi-part opening, preserve that requested structure while still not continuing beyond the requested material.

### Scope

This module creates Scenario starting messages only. It does not:
- generate or revise the Analysis Sheet;
- create missing Character Sheets, World Sheets, or a Context Sheet automatically;
- create a Description or Lorebook Plan;
- produce the entire plot or write a chapter unless the user explicitly requests a prose sample rather than a roleplay opener;
- generate the user's character's actions, dialogue, decisions, or private thoughts;
- continue roleplay after the opening.

If the project context is sufficient, proceed even if some optional asset sheet is absent. Do not block Scenario generation just because a Context Sheet has not been created. Use the best available approved project material. Ask one concise question only when a missing fact makes any coherent opening impossible or when two unresolved interpretations would create materially different openings.

## 3. Required skill loading

Load:

1. `creation/scenario-starting-message/SKILL.md` — this procedure.
2. `creation/scenario-starting-message/style-and-format.md` — the required prose and notation convention.
3. `creation/scenario-starting-message/opening-design.md` — scene construction, playable hook, and multi-opening variation.
4. `shared-systems/bedrocks/SKILL.md` — identify and enforce all applicable project invariants.
5. `shared-systems/information-transfer/SKILL.md` — prevent approved project information from being lost and check scenario coverage.
6. `shared-systems/evidence-and-inference/SKILL.md` — prevent unsupported permanent facts or character behavior from being introduced.
7. `shared-systems/adaptive-sections/SKILL.md` only when sectioned project materials need interpretation; do not impose an Analysis Sheet template on the Scenario itself.
8. `shared-systems/tags/SKILL.md` and only the applicable individual tag definitions.
9. `core/project-isolation/SKILL.md` when more than one project exists in the active conversation.
10. `creation/context-sheet/SKILL.md` as a reference for the integrated narrator-facing project context when a Context Sheet exists. Do not rerun Context Sheet generation.
11. Relevant Phase 7 Character and World skills only when an existing asset requires interpretation beyond what the approved sheet states.

Read `INDEX.md` if the current route or dependency status is uncertain.

## 4. Inputs and source reconciliation

### 4.1 Gather only relevant project material

Inspect the active project namespace and collect whichever of these actually exist:
- latest explicit user concept, corrections, and project-specific instructions;
- approved Analysis Sheet and its narrative focus, scene intent, and accepted interpretations;
- current Context Sheet, especially project identity, narrative intention, character and relationship context, world rules, plot, knowledge boundaries, tone, and Bedrocks;
- relevant Character Sheets and voice/behavior details;
- relevant World Sheet details and location/world rules;
- approved relationship, plot, event, or scenario premise material;
- explicit and auto-applied tags with their scopes;
- applicable confirmed Bedrocks;
- reference material explicitly intended to guide the opening;
- the current command's quantity and scene-specific instructions.

Do not assume a sheet exists because a module exists. Use only source material actually available in the active project.

### 4.2 Source precedence

Resolve competing details in this order:

1. The user's latest explicit correction or intentional canon revision.
2. Current explicit user-provided project facts and constraints.
3. The latest approved artifact that owns the specific information: the latest Character Sheet for character facts, the latest World Sheet for world facts, and the latest Context Sheet for integrated project-level context. A newer approved domain-specific update supersedes an older copy of that fact inside the Context Sheet until the handoff is updated.
4. Other current approved project assets, including relationship, plot, event, and scenario-premise material.
5. Approved Analysis Sheet findings and scene-generation direction.
6. Supported details from source notes, images, and RP logs that have been accepted into the project.
7. Creative additions explicitly authorized by the `Improvise` tag or current command.
8. Unapproved inferences and speculative ideas, which must not be presented as established canon.

This order is not permission to discard earlier established information silently. If two current sources materially conflict and chronology or scope does not resolve them, avoid the disputed detail when possible. Ask a short clarification only if the conflict determines the opening itself.

### 4.3 Approved versus unapproved information

The Analysis Sheet may contain observations, inferences, candidates, and proposals. Do not treat all analysis text as approved canon.

Use approved or explicitly established conclusions. Do not convert uncertain image-based personality guesses, suggested secrets, hypothetical conflicts, or Bedrock candidates into facts merely to make the opening more dramatic.

A proposed addition may shape the opening only when the user has approved it, requested it, or authorized the relevant improvisation. Without `Improvise`, limit invention to minor, neutral staging needed to make the scene coherent. With `Improvise`, add suitable missing scene context and connective elements that genuinely complete the intended concept, while remaining consistent with its core identity and Bedrocks. Do not introduce major lore, relationships, secrets, trauma, motivations, or plot events merely for spectacle; an addition that would materially change the premise is not a gap-fill.

## 5. Scenario construction procedure

Follow this sequence internally. Do not print the analysis steps unless the user asks for them.

### Step 1 — Resolve the active project and opening scope

- Confirm the active project namespace.
- Parse the requested quantity and every command-local constraint.
- Determine whether the user wants alternatives, a specific opening situation, or an explicitly connected multi-part opening.
- Identify which characters, groups, locations, and project elements are allowed or required in this run.
- Keep all unrelated project namespaces out of the generation.

### Step 2 — Establish the opening's narrative purpose

Identify what the first message must accomplish for this particular project. Consider:
- the project's core appeal and narrative gravity;
- the intended roleplay type and scope;
- the central relationship, conflict, mystery, activity, or atmosphere;
- the intended emotional temperature;
- what the user should understand immediately;
- what must remain unresolved for interaction to begin.

Do not force every opening to contain an argument, cliffhanger, question, dramatic emergency, or immediate conflict. The opening's energy must match the project's core appeal. A quiet slice-of-life opening may use a subtle social moment; a mystery may establish a clue or uncertainty; an adventure may establish a concrete situation or decision point.

### Step 3 — Select the opening point of entry

Choose the most effective moment to begin the scene:
- close enough to an interesting event that the scene has momentum;
- early enough that the user still has meaningful room to participate;
- grounded in an established or user-authorized situation;
- focused on the project's narrative gravity rather than unrelated spectacle.

Do not summarize the entire backstory before the scene starts. Provide only the context a reader needs to understand the immediate moment. Integrate relevant history or world information naturally through setting, behavior, dialogue, or a purposeful detail.

### Step 4 — Establish scene conditions

Determine only what the opening requires:
- location and immediate spatial arrangement;
- time or temporal condition, if relevant;
- immediate activity or situation;
- relevant environmental conditions;
- characters present and why they are there;
- what each present character knows, believes, wants, or is trying to do, based on established context;
- the immediate pressure, opportunity, tension, or social dynamic;
- what is available for the user to respond to.

Do not invent exact time, weather, geography, or a specific public event when those details would change established context. A minor neutral staging detail is permissible when needed, but it must not become a new canon rule.

### Step 5 — Apply character identity and voice

For each character who appears:
- preserve established personality, temperament, motivations, behavioral patterns, social role, and current emotional context;
- preserve the character's actual vocabulary, sentence rhythm, verbal habits, and degree of politeness or vulgarity;
- distinguish characters by how they think, speak, move, react, and handle pressure;
- avoid generic dialogue that could be spoken by any character;
- do not make a character behave out of character merely to manufacture a hook.

Use the `Uncensored` tag within its assigned scope. A sharp-tongued, crude, or sexually explicit character should retain naturally blunt, vulgar, or graphic language where appropriate; do not sanitize that voice or spread it to other characters. Explicit sexual, violent, or dark content that belongs to the scene or character concept is written directly.

### Step 6 — Apply world and project rules

- Respect the world's physical, social, political, technological, magical, supernatural, and institutional rules that affect the scene.
- Preserve terminology and established distinctions.
- Keep public belief, character belief, narrator-known truth, and objective world fact distinct where the project requires it.
- Respect Open World and Open Interaction scope. Do not imply that only the initial named locations or cast can ever exist when those tags apply.
- Do not introduce an incompatible system, ability, institution, or world fact for convenience.

### Step 7 — Enforce Bedrocks

Load all confirmed Bedrocks that apply to the selected characters, relationships, setting, and scene.

Before drafting, identify any likely collision between the proposed opening and a Bedrock. Design around the restriction rather than trying to create drama by violating it.

A Bedrock section, when included in a Scenario artifact, must contain only Bedrock statements. Do not append explanatory rules to that list. The opening itself should simply obey them; it does not need to repeat all Bedrocks in the story text.

Never promote a Bedrock candidate into a confirmed Bedrock. If the current command explicitly and clearly revises a Bedrock, apply the revision only when user intent is unambiguous; otherwise clarify.

### Step 8 — Apply tags at their correct scope

- `Detailed`: expand the scene's relevant description and context substantially, while keeping it purposeful and readable.
- `Uncensored`: preserve appropriate blunt, vulgar, or explicit vocabulary and character voice; do not sanitize sexual, violent, or dark content that belongs to the scene.
- `Improvise`: permit creative completion of missing staging or connective details, but never contradict established facts or Bedrocks and never invent major canon casually.
- `Open World`: avoid treating one location as the only possible setting.
- `Open Interaction`: avoid treating the initial cast as a closed universe.
- `Full Physical Description`: include the relevant supported physical detail when the opening calls for it, but do not turn a scene opener into an exhaustive body inventory unless the user requests that emphasis.
- `Scenario Reference`: use the reference as the current scene's visual/situational direction; do not automatically turn temporary props, expressions, poses, weather, or actions into permanent traits or lore.
- `Style Reference`: apply only the requested style/mood/presentation influence; do not extract unsupported story facts from it.
- `Focus` and `Exclude`: prioritize or ignore only the named areas/elements within their declared scope.
- Other user-defined tags: interpret their clear meaning in context, but do not invent rigid behavior for an ambiguous tag.

### Step 9 — Construct the message

Use the procedure in `opening-design.md` to shape the opening. Use `style-and-format.md` for prose and notation. Keep the opening scene-native: it should read as a message from the project, not as a description of how the engine designed it.

The default length is **2–4 paragraphs**. Adjust to the user's requested length and the scene's needs. Do not pad a quiet scene to meet the default; do not compress a major moment that needs room.

### Step 10 — Check user-character agency

The opening may establish the environment, NPC behavior, character dialogue, and circumstances around the user-controlled role. It must not decide what the user character does in response.

Never invent the user's character's:
- actions or movement;
- dialogue or vocal response;
- thoughts, feelings, beliefs, intentions, or decisions;
- voluntary reactions;
- appearance, identity, or backstory unless explicitly supplied as project facts.

Do not write the user into an action such as entering, sitting, standing, smiling, looking, reaching, agreeing, refusing, or following unless that action is explicitly established as having already occurred and the opening must begin after it. Even then, do not invent additional user behavior.

A character may speak directly to the user-controlled role using dialogue. Direct address such as “you” inside spoken dialogue is allowed. Objective narration must refer to established characters by name, title, or role and must not narrate the user's actions in second person.

Include a supplied user persona only when it improves immersion, strengthens a relevant dynamic, supports narrative flow, or is important to the RP structure. Otherwise omit it naturally. If no user persona or user character is established, do not invent one. Create an opening that offers an entry point without assigning an identity or action to the user.

### Step 11 — End at the response opportunity

End the starting message at a natural point where the user's response can begin. This may be:
- a character's line that invites an answer;
- an unresolved action or immediate choice;
- a meaningful object, clue, or event becoming relevant;
- a social opening or tension;
- a developing event that the user can influence;
- a quiet moment that naturally invites interaction.

Do not force a rhetorical question or melodramatic cliffhanger. Do not resolve the central interaction before the user participates. The message should have momentum, but should leave the next meaningful choice open.

### Step 12 — Validate and deliver

Run the checks in Section 9 and the `phase-9-scenario-regression-tests.md` expectations relevant to the request.

Output only the requested number of starting messages and any labels required to distinguish them. Do not include internal analysis, an explanation of the generation, an unrequested summary, or a command menu.

## 6. Multiple opening messages

When the user requests more than one starting message:

1. Generate exactly the requested count.
2. Treat each as an independent opening alternative unless the user specifies another relationship between them.
3. Make alternatives meaningfully different. Vary the entry moment, initial activity, character interaction, emotional angle, location, or narrative hook as appropriate.
4. Do not merely paraphrase the same opening or change only weather, clothing, or sentence order.
5. Preserve the same project's established facts, character identities, relationships, and Bedrocks in every alternative.
6. Do not make one alternative canonically invalidate another. They are selectable options, not sequential events.
7. Label alternatives outside the message body (for example, `Opening 1`, `Opening 2`). The label is not part of the roleplay text.
8. Do not add commentary about which opening is best unless the user asks for a recommendation.

If the user requests a connected multi-part opening rather than alternatives, label parts as requested and maintain continuity between them. Stop at the requested endpoint; do not invent subsequent roleplay turns.

## 7. Edge-case handling

### 7.1 No Context Sheet exists

Use the latest approved Analysis Sheet, Character Sheets, World Sheet, direct project instructions, and other available material. Do not automatically create a Context Sheet as a prerequisite. If the context is too thin for any meaningful opening, ask the single most important question or produce a deliberately simple opening using only what is established.

### 7.2 Context Sheet exists but is stale

A later explicit user correction takes precedence. Do not follow stale content simply because it appears in the Context Sheet. Use the most recent approved project facts and avoid propagating known superseded details.

### 7.3 Analysis Sheet contains unresolved proposals

Do not use unresolved proposals as facts. Prefer approved material. If an unresolved point is necessary to the requested opening, ask one short question or keep that point open.

### 7.4 The user requests direct generation without prior analysis

Proceed from the available concept and reference material. Do not fabricate the missing Analysis Sheet. Apply evidence limits and avoid unsupported major additions.

### 7.5 Scenario Reference is supplied

Treat it as the intended scene reference within its scope. Use only relevant visible/situational detail. A temporary pose, expression, prop, outfit, weather condition, or background object does not become permanent canon unless the user says so.

### 7.6 A character is meant to remain unseen or unknown

Preserve concealment. Do not reveal a secret identity, hidden motive, unknown appearance, or concealed information merely to make the opening vivid. Show the observable effect or uncertainty where appropriate.

### 7.7 Mystery or asymmetric knowledge

Maintain who knows what. Do not let characters react to facts they do not know. Do not expose the answer in narration or character thoughts if the project requires it to remain hidden from the reader or the relevant viewpoint.

### 7.8 Open World and Open Interaction

Do not imply that the opening cast or location is exhaustive. Additional characters or locations can appear later, but do not insert random new characters or places into the opening without a narrative reason.

### 7.9 Uncensored tag

Use the character's natural register, including profanity, vulgarity, and explicit sexual or violent language where appropriate. Do not replace a defined blunt or explicit voice with polite euphemisms or moral softening. Do not make every character swear. Explicit content that belongs to the scene or character is written directly.

### 7.10 Detailed tag

Give the scene and its relevant context the requested depth. Detailed does not mean bloated, repetitive, or full of unrelated exposition.

### 7.11 OOC instruction accompanies the command

An explicit OOC instruction is an instruction to this creation engine, not an in-world event. Apply it to the requested scope. If the user explicitly requests a brief out-of-character note in `//` notation, provide that note separately and then complete the requested Scenario generation. Do not continue roleplay after the opening.

### 7.12 Project isolation

Use only the active project's information. Never borrow a character, Bedrock, setting rule, tag scope, or story event from another in-session project unless the user explicitly connects the projects.

## 8. Output contract

A Scenario starting message must:
- be a ready-to-use opening message, not a prompt to this engine;
- reflect the project's central appeal and intended narrative direction;
- use the established characters and their distinct voices;
- contain only relevant scene context and purposeful details;
- follow the required notation system;
- preserve the project's Bedrocks and factual boundaries;
- maintain user-character agency;
- provide a natural response opportunity;
- stop after the opening.

A Scenario must not:
- include analysis labels or source commentary;
- summarize all project lore before beginning;
- invent unsupported major events, secrets, motives, relationships, or world facts;
- state the user's thoughts, dialogue, choices, or voluntary actions;
- make an NPC know private information without an established mechanism;
- violate a Bedrock;
- include unrequested OOC comments;
- turn multiple requested alternatives into sequential roleplay turns;
- continue roleplay after the final requested opening.

## 9. Completion and quality checklist

Before delivery, verify:

- [ ] The active project and requested scope are correct.
- [ ] The exact requested number of starting messages is present.
- [ ] Each alternative is meaningfully distinct when multiple are requested.
- [ ] The opening uses current, approved project information and respects source precedence.
- [ ] The project's narrative gravity and core appeal are present.
- [ ] Characters behave and speak consistently with their established identities.
- [ ] Dialogue sounds distinct rather than generic.
- [ ] World rules, knowledge boundaries, and relationship dynamics are respected.
- [ ] All applicable Bedrocks are obeyed.
- [ ] No unsupported major canon is introduced.
- [ ] User-character actions, speech, thoughts, and decisions are not invented.
- [ ] Third-person narration is maintained by default, unless explicitly overridden.
- [ ] Narration, dialogue, thoughts, and OOC conventions are not mixed.
- [ ] The prose is vivid, grounded, specific, and free of filler or purple prose.
- [ ] Emotion is primarily communicated through behavior and dialogue rather than labels.
- [ ] The ending creates a natural response opportunity without forcing a question or resolving the interaction.
- [ ] No analysis or system explanation appears inside the starting message.
- [ ] The module stops after generating the requested opening(s).

## 10. Dependencies and module boundaries

### Required dependencies

- `style-and-format.md`
- `opening-design.md`
- `shared-systems/bedrocks/SKILL.md`
- `shared-systems/information-transfer/SKILL.md`
- `shared-systems/evidence-and-inference/SKILL.md`

### Conditional dependencies

- `shared-systems/tags/SKILL.md` and relevant individual tag files;
- `core/project-isolation/SKILL.md` for multiple active projects;
- `creation/context-sheet/SKILL.md` when an existing Context Sheet must be interpreted;
- Phase 7 Character/World modules when existing sheets require interpretation;
- Phase 6 analysis modules only when the existing analysis cannot be interpreted from its approved output.

### Explicit boundary

Phase 9 generates starting messages only. It does not generate a Description (Phase 10), Lorebook Plan (Phase 11), patch refinements/expansions (Phase 12), or the system-wide quality framework (Phase 13). Its local completion checks do not replace Phase 13.
