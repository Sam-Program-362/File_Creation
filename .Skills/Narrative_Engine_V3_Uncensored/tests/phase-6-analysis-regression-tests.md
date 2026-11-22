# Phase 6 — Analysis Regression Tests

These are model-behavior tests for the Markdown Skill procedures. They are not automated code tests. Run them against a model with the complete skill tree loaded and inspect the resulting Analysis Sheet.

## Test 1 — Concept gravity without forced conflict

**Input:** A quiet slice-of-life premise about two neighbors gradually becoming friends; no antagonist or dramatic secret is supplied.

**Expected:** Identifies relationship development and everyday interaction as the likely narrative gravity. Does not invent a villain, mystery, trauma or forced central conflict.

## Test 2 — Unusual concept / adaptive sections

**Input:** A sentient city whose districts are separate memories that can disagree about the city's past.

**Expected:** Uses custom analysis sections such as memory-district structure, conflicting civic memories and city-level identity. Does not force the entire concept into ordinary character/world/plot headings.

## Test 3 — Visual observation versus personality inference

**Input:** A single image of a person with a stern expression and formal clothing, tagged Full Physical Description.

**Expected:** Describes visible appearance and clothing. May note the apparent expression as temporary. Does not conclude the person is cruel, strict, traumatized or authoritative as an established personality fact. Does not invent exact height without scale.

## Test 4 — World reference with temporary scene details

**Input:** A rainy street image tagged World Reference; visible architecture, shop signs, puddles and a person holding an umbrella.

**Expected:** Extracts relevant architecture, street layout and atmosphere. Does not turn the umbrella or current rain into permanent setting rules. Notes limitations of inference.

## Test 5 — Fragmented contradictory context

**Input:** Notes state a character moved to the capital in Year 12; a later note says they were still living in the village during Year 13; no explanation is given.

**Expected:** Preserves the inconsistency and asks or flags it only if it materially affects the project. Does not invent a return journey or retcon.

## Test 6 — RP log OOC separation and knowledge boundaries

**Input:** A transcript contains a character's private thought, another character's spoken line, and a `//` OOC note that says the character is lying.

**Expected:** Separates these channels. Other characters do not know private thoughts by default. OOC notes are not in-world events, but an explicit user clarification can inform the analysis as out-of-character canon direction when that is clearly intended.

## Test 7 — Character psychology restraint

**Input:** A character insults a rival once, then apologizes and behaves politely in later scenes.

**Expected:** Does not label the character permanently abusive or aggressive based on one event. Examines context, pattern and change; flags uncertainty.

## Test 8 — Relationship asymmetry

**Input:** A and B describe the same incident differently: A believes it was betrayal; B believes it was protection.

**Expected:** Preserves both perspectives and does not choose one as objective truth without further evidence.

## Test 9 — World rule conditions and exceptions

**Input:** Magic works only outdoors, except during a full eclipse when it works indoors for 3 minutes.

**Expected:** Preserves the outdoor condition, eclipse exception and 3-minute limit exactly. Does not simplify to “magic works outdoors.”

## Test 10 — Improvise tag

**Input:** An incomplete but coherent premise with the Improvise tag.

**Expected:** Completes necessary connective details coherently, preserves explicit facts and Bedrocks, and does not include a Missing Elements section. Does not replace the premise with a different one.

## Test 11 — Automatic tag scope

**Input:** One character is explicitly sharp-tongued and uses profanity; other characters are polite.

**Expected:** May auto-apply Uncensored to that character only, with a reason. Does not apply it project-wide.

## Test 12 — No orphaned analysis findings

**Input:** A concept includes a rare physical trait, an unusual speech habit, a political limitation and a relationship rule.

**Expected:** Analysis identifies appropriate destinations for each item (character, world, relationship, Context Sheet or Lorebook Plan as relevant). No item is dropped because standard headings do not fit.

## Test 13 — Direct-generation override

**Input:** User explicitly says “Skip the Analysis Sheet and create the character directly.”

**Expected:** Does not output an Analysis Sheet. Still applies evidence, tag, Bedrock and information-preservation rules internally.

## Test 14 — Irrelevant specialist avoidance

**Input:** A concept is solely about a strange weather mechanism with no characters or interactions.

**Expected:** Runs Concept and relevant World Analysis. Does not produce empty Character or Relationship analysis sections.

## Acceptance criteria

Phase 6 passes when the model consistently follows the expected behaviors above, not merely when the files exist or their frontmatter says `implemented`.
