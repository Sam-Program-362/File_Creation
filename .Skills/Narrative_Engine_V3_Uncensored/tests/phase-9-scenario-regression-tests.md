# Phase 9 — Scenario Starting-Message Regression Tests

**Status:** 42 behavioral test specifications written; not yet executed against a target LLM/runtime.

Run these tests with `creation/scenario-starting-message/SKILL.md`, `style-and-format.md`, `opening-design.md`, and the relevant shared dependencies loaded. These tests assess actual generated behavior, not merely file presence.

## A. Command, quantity, and scope

### SC-01 — Default quantity
**Input:** `Create Scenario` with sufficient project context and no number.
**Expected:** Exactly one starting message is generated. No unrequested alternatives or summary are added.

### SC-02 — Exact explicit quantity
**Input:** `Create Scenario [3]`.
**Expected:** Exactly three opening messages are generated.

### SC-03 — Quantity plus local scope
**Input:** `Create Scenario [2; feature only Akari and the station setting]`.
**Expected:** Exactly two alternatives are generated using only the requested scope for this run. The wider project's cast/world is not permanently narrowed.

### SC-04 — Alternatives are not sequential turns
**Input:** Request three opening messages without asking for a sequence.
**Expected:** Three independent selectable openings are produced, not first/second/third roleplay turns.

### SC-05 — Connected multi-part opening explicitly requested
**Input:** Request a connected three-part opening.
**Expected:** Parts maintain continuity and stop at part three. No fourth turn or later continuation is generated.

### SC-06 — Scenario-only boundary
**Input:** Request Create Scenario.
**Expected:** The engine outputs starting message(s) only. It does not create or regenerate a Context Sheet, Character Sheet, World Sheet, Description, or Lorebook Plan.

## B. Source integration and canon

### SC-07 — Integrated project context
**Input:** Analysis Sheet, Context Sheet, Character Sheets, World Sheet, relationship information, plot details, and later corrections are available.
**Expected:** The opening reflects the relevant integrated project facts and the latest approved corrections. It does not use only the Character Sheet while ignoring project intent or world context.

### SC-08 — No Context Sheet available
**Input:** Analysis Sheet and Character/World information exist, but no Context Sheet has been generated.
**Expected:** The module can proceed from available approved information. It does not auto-create a Context Sheet or block unnecessarily.

### SC-09 — Stale Context Sheet
**Input:** A Context Sheet contains an older character detail that the user later explicitly corrected.
**Expected:** The latest explicit correction is used. The stale detail is not repeated.

### SC-10 — Unapproved analysis inference
**Input:** Analysis contains a speculative motive or image-derived personality guess that was not approved.
**Expected:** It is not presented as established canon in the opening.

### SC-11 — No major invented canon
**Input:** A project has no established secret, trauma, faction, or new conflict.
**Expected:** The opening does not invent one simply to create drama.

### SC-12 — Correct narrative gravity
**Input:** A quiet relationship-led slice-of-life project.
**Expected:** The opening prioritizes the relationship and daily interaction rather than imposing an unrelated emergency or action scene.

## C. Style and character portrayal

### SC-13 — Grounded prose
**Input:** Request a normal Scenario for a grounded contemporary project.
**Expected:** Concrete physical detail, purposeful sensory texture, and subtext appear without purple prose or generic dramatic filler.

### SC-14 — Emotion shown through behavior
**Input:** Character is anxious but habitually conceals it.
**Expected:** The opening primarily shows observable behavior and dialogue rather than repeatedly labeling the character anxious.

### SC-15 — Distinct character voice
**Input:** Two characters have clearly different speech patterns and registers.
**Expected:** Their dialogue is distinguishable and consistent with their sheets.

### SC-16 — Uncensored scope
**Input:** One character has the `Uncensored` tag and a blunt, vulgar voice; another character is formal.
**Expected:** The first character uses natural blunt vocabulary where appropriate; profanity is not spread to the formal character.

### SC-17 — Detailed tag
**Input:** `Detailed` is explicitly applied to the scenario.
**Expected:** Relevant scene context and descriptions are expanded substantially without padding, repetition, or unrelated exposition.

### SC-18 — No forced escalation
**Input:** A calm domestic concept with no immediate danger.
**Expected:** The opener does not inject violence, panic, a villain, or melodrama without support.

### SC-19 — No lore dump
**Input:** A world has extensive history, institutions, and magic rules.
**Expected:** Only context necessary for the opening is conveyed naturally. The entire lore system is not explained before the scene starts.

### SC-20 — Default paragraph calibration
**Input:** A normal, moderately complex opening with no custom length.
**Expected:** The message is generally 2–4 paragraphs, adjusted naturally to the scene without padding.

## D. Agency, knowledge, and format

### SC-21 — No invented user actions
**Input:** The user-controlled character's current action is unspecified.
**Expected:** The opening does not narrate the user entering, sitting, standing, looking, reaching, moving, or reacting.

### SC-22 — No invented user dialogue or decision
**Input:** The user character has no supplied response.
**Expected:** The generator does not write their speech, consent, refusal, choice, or decision.

### SC-23 — Never write user thoughts
**Input:** Scenario generation includes NPC thoughts as an optional format element.
**Expected:** Only portrayed characters/NPCs may receive thought blocks. No user-character thoughts appear.

### SC-24 — Private NPC thoughts remain private
**Input:** An NPC thought is included, but another character has no mind-reading ability.
**Expected:** Other characters do not react to or know the thought.

### SC-25 — Narration notation
**Input:** A generated opener contains actions, body language, and environmental description.
**Expected:** All non-spoken narration is wrapped in single asterisks and kept separate from speech and thought.

### SC-26 — Dialogue notation
**Input:** A generated opener contains spoken dialogue.
**Expected:** Every spoken line is enclosed in double quotation marks; actions and private thoughts are not inside those quotes.

### SC-27 — Thought notation
**Input:** A relevant NPC thought is included.
**Expected:** The thought is enclosed in exactly three backticks and contains no narration or spoken dialogue. The entire Scenario is not wrapped in one code fence.

### SC-28 — OOC convention
**Input:** No OOC reply is requested.
**Expected:** No `//` comments are generated. Supplied `//` notes do not become in-world events or character knowledge.

### SC-29 — Inline OOC marker
**Input:** Supplied roleplay material contains an in-line `//` marker followed by a side comment.
**Expected:** The text after `//` on that line is treated as OOC and does not become in-world content, story direction, or character knowledge.

### SC-30 — Third-person default
**Input:** No alternate perspective is requested.
**Expected:** Objective third-person narration is used; characters are referred to by name, title, or role. Direct “you” in spoken dialogue remains permissible.

## E. Bedrocks, tags, and narrative design

### SC-31 — Bedrock enforcement
**Input:** A Bedrock says a king must never kill any citizen. The opening includes the king and a threatened citizen.
**Expected:** The king does not kill the citizen or act in a way that contradicts the Bedrock. The conflict is designed around the invariant.

### SC-32 — Bedrock section purity
**Input:** The user specifically requests a Bedrocks section alongside the opening.
**Expected:** The section contains only Bedrock statements as bullets, without explanatory instructions or commentary.

### SC-33 — Open World semantics
**Input:** `Open World` applies.
**Expected:** One location may anchor the opener, but narration does not imply it is the only possible location in the project.

### SC-34 — Open Interaction semantics
**Input:** `Open Interaction` applies.
**Expected:** The opening does not state or imply that only the initially listed characters can ever participate.

### SC-35 — Scenario Reference is scene-specific
**Input:** A scenario reference shows a character holding an umbrella in heavy rain.
**Expected:** Those details may inform the opening scene if relevant, but the umbrella/rain are not converted into permanent character traits or world facts.

### SC-36 — Improvise tag
**Input:** `Improvise` is applied to a project whose opening lacks connective scene context but has a clear concept and established Bedrocks.
**Expected:** The generator supplies fitting missing scene context and connective elements, without reverting to a `Missing Elements` section, contradicting Bedrocks, or changing the core premise.

### SC-37 — Mystery knowledge boundaries
**Input:** A secret is known to the narrator but not to the character in the scene.
**Expected:** The character does not react as if they know the secret. The opening preserves the intended uncertainty.

### SC-38 — Natural response opportunity
**Input:** A normal opener with a defined relationship dynamic.
**Expected:** It ends at a meaningful point where the user can respond; it does not require a forced rhetorical question or melodramatic cliffhanger.

### SC-39 — No premature resolution
**Input:** The premise depends on a confrontation that the user must participate in.
**Expected:** The opening establishes the confrontation but does not resolve the key exchange, confession, or decision before the user's turn.

### SC-40 — No roleplay continuation
**Input:** Create Scenario produces the opening.
**Expected:** The engine stops after the requested opening(s). It does not write the next turn, respond as the user's counterpart, or simulate an ongoing scene.

### SC-41 — Project isolation
**Input:** Two separate projects are active in one conversation, with different characters and Bedrocks.
**Expected:** Only the active project's material appears in the Scenario. No cross-project facts or characters are imported.

### SC-42 — No command footer
**Input:** The engine has generated the requested opening.
**Expected:** It does not append a command menu, usage instructions, or a fixed interaction footer.
