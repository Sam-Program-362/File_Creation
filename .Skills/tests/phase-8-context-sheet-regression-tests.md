# Phase 8 — Context Sheet Regression Tests

**Status:** Test specifications written; not yet executed against a target LLM/runtime.

These tests check actual model behavior, not merely whether the skill file exists. Run them with the Phase 8 skill and its declared dependencies loaded. A failure should be fixed in the relevant procedure; do not weaken a requirement solely to accommodate a weak response.

## A. Core purpose and document identity

### CS-01 — Self-contained narrator handoff
**Input:** A complete project with an Analysis Sheet, two Character Sheets, a World Sheet, established relationships, plot context, and project-specific tone.
**Expected:** The Context Sheet explains the project as an integrated whole and can be understood without reconstructing the original chat. It carries narrator-relevant details from the assets rather than merely listing their titles.

### CS-02 — Not a conversational prompt
**Input:** Request a Context Sheet for an established project.
**Expected:** Output is a Markdown information document. It does not begin with “You are…”, “I want you to…”, or “Here is what you need to do.” It has no chatty framing, prompt-engineering commentary, or instructions addressed to an unnamed AI.

### CS-03 — Not an Analysis Sheet
**Input:** Analysis Sheet includes observed details, inferred details, proposed expansion, missing elements, and generation direction.
**Expected:** Approved information is translated into natural contextual statements. Analysis-only headings and source-process language do not appear in the Context Sheet.

### CS-04 — Not a Scenario
**Input:** Project contains a premise and an initial scene possibility.
**Expected:** Context Sheet describes the narrative situation and relevant initial conditions but does not write a polished opening message, scene narration, or dialogue exchange.

### CS-05 — No unsolicited deliverables
**Input:** User requests only `Create Context Sheet` while no Character Sheet or World Sheet exists.
**Expected:** Generate only the Context Sheet from available information. Do not create the missing assets, Description, Scenario, or Lorebook Plan.

## B. Coverage and integration

### CS-06 — Analysis coverage
**Input:** Approved Analysis Sheet contains unusual traits, premise constraints, relationship details, a special mechanic, and narrative intentions.
**Expected:** Every narrator-relevant approved item appears in a suitable Context Sheet section. No item is lost because it lacks a conventional heading.

### CS-07 — Character assets fully integrated
**Input:** Character Sheet contains physical details, voice patterns, behavioral habits, motivations, limitations, history, and relationships.
**Expected:** Context Sheet includes the details needed to portray the character accurately. It does not reduce the character to name, role, and a two-line personality summary.

### CS-08 — World asset integrated
**Input:** World Sheet contains exact rule limits, institutional structure, locations, and relevant history.
**Expected:** Context Sheet preserves the narrator-relevant world facts, mechanisms, exact limits, exceptions, and consequences.

### CS-09 — Relationship asymmetry
**Input:** A likes B, but B is suspicious of A and does not reciprocate the feeling.
**Expected:** Context Sheet preserves the asymmetry and does not describe the relationship as mutually affectionate or trusting.

### CS-10 — Cross-asset dependencies
**Input:** A character's ability is restricted by a world law and affects a central conflict.
**Expected:** Context Sheet integrates the character ability, world law, and plot consequence so the downstream AI understands their relationship. It does not bury the entire dependency in an unrelated section.

## C. Truth, knowledge, and chronology

### CS-11 — Secret knowledge boundary
**Input:** The narrator-level truth is that a character is an impostor. Only one NPC knows this; the protagonist suspects nothing.
**Expected:** Context Sheet distinguishes objective truth, NPC knowledge, protagonist knowledge, and public belief. It does not make the protagonist behave as though the secret is known.

### CS-12 — Conflicting source records
**Input:** Two current project assets contain incompatible dates for a major event; no later user correction exists.
**Expected:** Preserve the conflict as unresolved or ask one concise clarification if it prevents a coherent handoff. Do not invent a compromise date.

### CS-13 — New explicit correction
**Input:** Existing Character Sheet says a character is 24; the user's latest explicit correction says 26.
**Expected:** Use 26 and avoid stale 24 references. Do not silently treat the old sheet as more authoritative than the user's current correction.

### CS-14 — In-world belief versus objective fact
**Input:** The public believes a ruler is immortal, but the actual truth is that the ruler ages normally.
**Expected:** Distinguish public belief from objective truth and maintain the difference in relevant context.

## D. Bedrocks and tags

### CS-15 — Clean Bedrocks section
**Input:** Three confirmed Bedrocks apply project-wide and to named characters/world elements.
**Expected:** A dedicated `Bedrocks` section contains only the three Bedrock statements as bullets. No explanatory prose, AI instructions, priority labels, or scope commentary appears inside it.

### CS-16 — No invented Bedrock
**Input:** Analysis contains a Bedrock candidate that the user has not confirmed.
**Expected:** Candidate is not included in the confirmed Bedrocks list and is not silently elevated to canon.

### CS-17 — Exact numerical limit
**Input:** Bedrock says a colossal never walks faster than 2 km/h.
**Expected:** Exact limit and unit are preserved. The document does not weaken it to “moves slowly” or change the number/unit.

### CS-18 — Uncensored voice transfer
**Input:** A character is explicitly sharp-tongued and bratty; `Uncensored` applies only to this character.
**Expected:** Context Sheet preserves direct vocabulary and character-appropriate examples for this character without spreading profanity to unrelated characters.

### CS-19 — Open scope semantics
**Input:** `Open World` applies, but `Open Interaction` does not; initial cast is closed while locations are open.
**Expected:** Context Sheet keeps locations open but does not imply the cast is open. The two tags are not conflated.

### CS-20 — Improvise and no missing-elements output
**Input:** `Improvise` applies and the concept lacks supporting context necessary for a coherent handoff.
**Expected:** Add coherent supporting information within the established concept and Bedrocks. Do not include `Missing Elements` or `Planned Expansion` sections in the final Context Sheet.

### CS-21 — Detailed tag
**Input:** `Detailed` is explicitly supplied as a tag.
**Expected:** Explanations and relevant context are substantially expanded, clear to a reader without prior knowledge, and still organized. No unrelated padding is introduced.

## E. Narrative operation context

### CS-22 — Third-person default
**Input:** No alternate narrative perspective is established.
**Expected:** Context Sheet records objective third-person perspective as the default project configuration, unless an explicit project instruction establishes otherwise.

### CS-23 — User-character agency
**Input:** Roleplay involves a user-controlled protagonist.
**Expected:** The project handoff represents the user's character's dialogue, private thoughts, decisions, and voluntary actions as user-authored. It does not invent the user's persona or actions.

### CS-24 — Formatting conventions only when relevant
**Input:** The project explicitly specifies narration/dialogue/thought/OOC notation.
**Expected:** The Context Sheet records those conventions as project interaction context. If no such convention is established, the module does not invent a specialized notation system.

### CS-25 — User persona relevance
**Input:** A user persona is supplied but has no role in the concept or narrative structure.
**Expected:** The Context Sheet omits it rather than inserting it by default. If it is central to a defined relationship or roleplay structure, include only the relevant established details.

## F. Scope and output quality

### CS-26 — Early Context Sheet
**Input:** User requests Context Sheet after Analysis Sheet but before Character/World generation.
**Expected:** Generate a useful handoff from current approved information. Do not claim separate assets already exist or block the task unnecessarily.

### CS-27 — Direct generation without Analysis Sheet
**Input:** User supplies a complete concept and directly requests a Context Sheet.
**Expected:** Apply evidence, tag, adaptive-section, Bedrock, and coverage checks internally. Do not output an unrequested Analysis Sheet.

### CS-28 — Unusual ontology
**Input:** Project centers on a sentient building with memory partitions, access permissions, and several embodied interfaces.
**Expected:** Use custom sections that describe identity, interfaces, memory, permissions, agency, and relevant mechanics. Do not force a conventional human-character or geographic-world format.

### CS-29 — Command-local cast restriction
**Input:** `Create Context Sheet [include only Akari and the academy for now]`; project contains other established characters and locations.
**Expected:** Restrict this document only. Do not erase other project canon or describe the whole project as permanently limited to Akari and the academy.

### CS-30 — Multiple-project isolation
**Input:** Two unrelated projects exist in one conversation and the user requests a Context Sheet for the second.
**Expected:** No names, traits, Bedrocks, world rules, tags, or assumptions from the first project leak into the second.

### CS-31 — No empty template sections
**Input:** A small relationship project has no magic, history, factions, or technical mechanics.
**Expected:** No empty headings for irrelevant categories. Structure reflects the actual project.

### CS-32 — Downstream usability and proportion
**Input:** A small slice-of-life project with two central characters and one recurring location.
**Expected:** Context Sheet is sufficiently complete for portrayal but avoids irrelevant encyclopedia expansion and repetitive duplication.

### CS-33 — Final Bedrock and consistency sweep
**Input:** A generated Context Sheet has many interdependent details, plus multiple scoped Bedrocks.
**Expected:** Every applicable Bedrock is preserved with its scope and exact meaning; no prose or contextual detail contradicts it.

## Test execution record

| Test group | Specification count | Execution status |
|---|---:|---|
| Core purpose and identity | 5 | Not executed |
| Coverage and integration | 5 | Not executed |
| Truth, knowledge, chronology | 4 | Not executed |
| Bedrocks and tags | 7 | Not executed |
| Narrative operation context | 4 | Not executed |
| Scope and output quality | 8 | Not executed |
| **Total** | **33** | **Specifications only** |
