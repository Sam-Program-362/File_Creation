# Phase 7 — Character and World Creation Regression Tests

**Test target:** `creation/character/SKILL.md` and `creation/world/SKILL.md`  
**Test type:** model-behavior tests; these cannot be proven by checking files alone.  
**Purpose:** verify the generation procedure preserves the concept, produces usable assets, and does not drift into analysis, Context Sheet, or roleplay responsibilities.

## Character creation tests

### C01 — Ordinary supplied character

**Input:** A contemporary character with a name, occupation, three personality traits, a short relationship note, and no request for a full biography.  
**Expected:** A focused Character Sheet with identity, role, supported personality/behavior, relevant relationship detail, and no invented dramatic backstory or decorative trivia.

### C02 — Full Physical Description tag

**Input:** A full-body reference image and the Full Physical Description tag.  
**Expected:** A coherent detailed description covering supported height estimate, frame, build, proportions, shoulders, torso, chest/bust where applicable, waist, abdomen, hips/pelvis, lower body, thighs, legs, arms/hands, face, hair, skin, posture, gait, and relevant clothing/species features. Visual measurements remain estimates. Temporary pose/expression is not made permanent.

### C03 — Full-body description without evidence

**Input:** A name and personality only; user requests Full Physical Description but provides no appearance reference or physical details.  
**Expected:** The generator does not fabricate exact body dimensions. It states what cannot be established or asks for reference material when a full visual description is essential. If user explicitly authorizes creative invention or Improvise applies, additions are presented as authored character design, not as observations.

### C04 — Sharp-tongued Uncensored character

**Input:** A character described as bratty, irreverent, sharp-tongued, and deliberately profane; Uncensored tag applies.  
**Expected:** Voice description and representative examples retain fitting slang/profanity. The system does not sanitize it into generic politeness or force profanity into every line.

### C05 — Multi-character scope

**Input:** `Create Character [only Akari and Ashli for now]` in a project that mentions six other people.  
**Expected:** Only Akari and Ashli receive Character Sheets. The remaining cast is not erased from the project and no extra sheets are generated.

### C06 — Unusual/non-human character

**Input:** A distributed machine intelligence with several remote bodies and no single biological body.  
**Expected:** The sheet creates custom sections for distributed identity, interfaces/instances, memory, communication, limitations, and other relevant mechanics. It does not force human anatomy or a conventional childhood biography.

### C07 — Personality grounded in behavior

**Input:** “She is proud and guarded,” plus interaction examples showing how she reacts to criticism and affection.  
**Expected:** The sheet explains concrete behavior and distinct reactions. It does not merely repeat adjectives or invent trauma as their cause.

### C08 — Asymmetric relationship

**Input:** Character A is in love with Character B, but B does not know and sees A only as a colleague.  
**Expected:** The sheet preserves the asymmetry and does not describe the relationship as mutual romance.

### C09 — Conflicting explicit character facts

**Input:** Two user-supplied sources give incompatible ages, with no indication which is current.  
**Expected:** The generator does not choose silently. It flags the conflict or asks one concise clarification when age matters.

### C10 — Command-local omission

**Input:** Existing canon includes the character's family history. Command says `Create Character [leave the history out for this version]`.  
**Expected:** The current output omits history without deleting or revising the underlying project fact.

### C11 — Character Bedrock

**Input:** Confirmed Bedrock: “Mira never reveals the location of the safehouse.”  
**Expected:** The character sheet includes the relevant Bedrock as a standalone bullet and no other text inside the Bedrocks section. No other section contradicts it.

### C12 — No unsupported psychology from image

**Input:** Image of a frowning person; user supplies no personality context.  
**Expected:** The frown may be recorded as a visible expression in analysis, but the character is not automatically described as hostile, depressed, cruel, or angry by nature.

### C13 — Direct generation

**Input:** User explicitly says to skip the Analysis Sheet and create a character directly from supplied notes.  
**Expected:** The generator applies evidence, tag, Bedrock, and transfer discipline internally but does not output an unsolicited Analysis Sheet.

### C14 — No analysis contamination

**Input:** Approved Analysis Sheet has observations and approved character findings.  
**Expected:** The Character Sheet uses natural finished character information. It does not say “the image suggests,” “analysis indicates,” “observed details,” or “planned expansion.”

## World creation tests

### W01 — Small contained setting

**Input:** A two-character slice-of-life project centered on an apartment and nearby café.  
**Expected:** World Sheet focuses on the apartment, café, relevant movement, routines, atmosphere, and social context. It does not invent a continent, national history, or unrelated political factions.

### W02 — Open World tag

**Input:** A fantasy adventure begins in one port city and includes Open World.  
**Expected:** The initial city is not represented as the only possible location. The setting leaves credible space for additional regions without inventing an exhaustive atlas.

### W03 — Open Interaction is not Open World

**Input:** A school drama uses Open Interaction but remains set at one school.  
**Expected:** Additional characters may appear, but the system does not assume the setting must expand beyond the school.

### W04 — Rule model with exact numbers

**Input:** A world rule specifies that a colossal entity cannot move faster than 2 km/h and can only move while its core is illuminated.  
**Expected:** Both conditions and the exact speed/unit remain explicit. The generator does not paraphrase this into “moves slowly.”

### W05 — Magic system consistency

**Input:** Magic allows long-distance teleportation, while the concept relies on remote locations being isolated.  
**Expected:** The generator detects the dependency conflict. It does not invent arbitrary restrictions unless authorized; it asks or identifies the unresolved design choice.

### W06 — Objective fact versus in-world belief

**Input:** The population believes the moon is a deity, but the user establishes that it is an artificial satellite.  
**Expected:** The World Sheet distinguishes actual ontology from cultural belief and does not state the belief as objective fact.

### W07 — Non-uniform culture

**Input:** A society contains three regions with different customs and contested social norms.  
**Expected:** The output preserves internal variation and does not generalize one custom to all members.

### W08 — Institutional mechanics

**Input:** A kingdom has a monarch, council, and local governors; the plot depends on who can enforce laws.  
**Expected:** The World Sheet explains authority, jurisdiction, enforcement, constraints, and conflict among institutions to the depth the plot needs.

### W09 — Abstract/simulated world

**Input:** A virtual reality with instances, memory resets, permissions, and system administrators.  
**Expected:** Custom sections describe simulation ontology, state persistence, access, authority, and reset conditions. No forced geography/history template.

### W10 — Scenario reference stays temporary

**Input:** A reference image shows a stormy street used only for the opening scene.  
**Expected:** Weather and scene conditions are not turned into permanent climate or world lore.

### W11 — Improvise world completion

**Input:** A project explicitly applies Improvise and requires a working city setting but supplies only its premise and one important rule.  
**Expected:** The generator creates coherent supporting locations, institutions, and connective structure as needed, preserves the premise/Bedrocks, and does not output a Missing Elements section.

### W12 — Important gap without Improvise

**Input:** A plot depends on whether travel between two cities takes minutes or weeks, but no distance or travel system is provided.  
**Expected:** The generator does not invent a definitive value silently. It asks or explicitly preserves the ambiguity when it materially affects the world logic.

### W13 — World Bedrock

**Input:** Confirmed Bedrock: “The king must never kill any citizen.”  
**Expected:** Bedrock appears as a standalone list item and the world’s laws, institutions, and history do not contradict it. If enforcement or meaning is unclear, clarify outside the Bedrocks list.

### W14 — Avoid overbuilding

**Input:** A contemporary romance requires a small coastal town as a recurring backdrop.  
**Expected:** Create relevant setting information without adding an unnecessary multi-century chronology, full economic model, or dozens of factions.

### W15 — World and character boundaries

**Input:** A character is heir to a throne and belongs to a named family.  
**Expected:** The World Sheet explains monarchy, succession, and the family's institutional role when relevant; it does not reproduce the character's full personality and biography.

### W16 — Direct world generation

**Input:** User provides setting notes and explicitly skips the Analysis Sheet.  
**Expected:** World generation applies evidence and consistency rules internally and produces the requested World Sheet without unsolicited analysis output.

## Cross-module tests

### X01 — Analysis coverage transfer

**Input:** Approved Analysis Sheet contains unusual details not represented by standard headings.  
**Expected:** Those details appear in an appropriate custom section of the Character Sheet or World Sheet; none are dropped because the template lacks a slot.

### X02 — Project isolation

**Input:** Two unrelated projects exist in one conversation, each with its own characters and world rules.  
**Expected:** Character and World generation use only the active project's facts and Bedrocks unless an explicit cross-project link is requested.

### X03 — Context handoff awareness

**Input:** Character and World sheets are generated.  
**Expected:** Both identify downstream-relevant information internally/through coverage, but neither attempts to generate the Context Sheet prematurely. The later Context Sheet will integrate both assets.

## Pass criteria

- Each test must produce the expected behavior without requiring the user to restate a rule already present in the skill files.
- A test fails if the output contradicts a Bedrock, silently upgrades uncertainty to fact, drops an approved relevant detail, violates command-local scope, or generates an unrequested deliverable.
- Record the target model, date, input, output, pass/fail result, and failure notes when executing these tests.
- These tests are specifications until actually run against a target model. Do not claim model-level pass status from static file validation.
