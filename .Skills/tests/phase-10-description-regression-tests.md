# Phase 10 — Description Generation Regression Tests

**Purpose:** Specify expected human-facing Description behavior. These are test specifications, not evidence of model-level test execution.

## Subject and audience

### DE-01 — Whole-project overview
**Input:** `Create Description` with an approved Analysis Sheet, Character Sheets, World Sheet, and Context Sheet.
**Expected:** A coherent human-facing overview that explains the project's premise, central appeal, relevant world and character dynamics, and intended narrative experience. It is not a data dump of all assets.

### DE-02 — World-only description
**Input:** `Create Description [describe only the world]`.
**Expected:** Focuses on the setting's identity and defining systems. Does not expand into an unrelated plot or character pitch.

### DE-03 — Plot synopsis
**Input:** `Create Description [full plot synopsis]` with established plot material.
**Expected:** Explains established plot progression at the requested level. Does not invent an ending or hide known plot material when full disclosure was explicitly requested.

### DE-04 — Public listing
**Input:** `Create Description [public roleplay listing, spoiler-light]`.
**Expected:** Presents the premise and appeal to an unfamiliar reader while withholding explicitly protected twists and secrets not needed to understand the hook.

### DE-05 — Unknown platform
**Input:** `Create Description` with no platform named.
**Expected:** Produces a platform-neutral Markdown description. Does not invent character limits, rating labels, or platform-specific structures.

## Source and information integrity

### DE-06 — Newer Character Sheet supersedes stale Context Sheet copy
**Input:** Older Context Sheet says a character is a student; newer approved Character Sheet establishes that the character has graduated.
**Expected:** Uses the newer character fact. Does not repeat stale information.

### DE-07 — Unapproved inference
**Input:** Analysis Sheet contains a speculative motivation marked inferred and not approved.
**Expected:** Does not state the motivation as fact in the Description.

### DE-08 — Coverage without dumping
**Input:** Approved analysis includes many small traits, one central relationship, and a world premise.
**Expected:** Preserves the important premise and relationship information without mechanically listing every minor trait.

### DE-09 — Bedrock compatibility
**Input:** A project Bedrock states that the ruler never executes citizens.
**Expected:** The Description does not imply or state that the ruler executes citizens. It does not need a separate Bedrocks section unless requested.

### DE-10 — Project isolation
**Input:** Two projects exist in one conversation, with a Description requested for one of them.
**Expected:** Uses only the active project's material and constraints.

### DE-11 — Contradictory source material
**Input:** Two current, equally authoritative project artifacts disagree about a major event and neither supersedes the other.
**Expected:** Avoids asserting the disputed event as fact when possible; asks a concise question only if the conflict prevents an accurate Description.

## Tags and style

### DE-12 — Detailed tag
**Input:** Description command includes `Detailed` as an explicit tag.
**Expected:** Explains premise, context, and dynamics substantially more fully without irrelevant repetition.

### DE-13 — Ordinary use of “detailed”
**Input:** User says “make this description detailed” as a direct command instruction but does not supply the built-in tag.
**Expected:** Obeys the ordinary request for this output without falsely recording the built-in tag as applied.

### DE-14 — Uncensored scope
**Input:** A character's defining voice is profane, but the rest of the world description is neutral.
**Expected:** Preserves profanity or blunt phrases only where they accurately represent the character or intended tone. Does not make every paragraph vulgar.

### DE-15 — Open Interaction
**Input:** The project has Open Interaction.
**Expected:** Does not present the initial cast as the only possible participants.

### DE-16 — Open World
**Input:** The project has Open World.
**Expected:** Does not imply that the first named location is the only location available.

### DE-17 — Excluded reference detail
**Input:** An `exclude:[background]` tag is attached to a reference used in the Analysis Sheet.
**Expected:** Description does not use excluded background details as established setting content.

### DE-18 — Improvise boundary
**Input:** `Improvise` applies and some connective context is missing.
**Expected:** Makes only coherent, necessary additions within the tag's authority. Does not invent a premise-changing secret or ending.

## Output identity and format

### DE-19 — Not a Context Sheet
**Input:** `Create Description` with a comprehensive Context Sheet available.
**Expected:** Produces readable presentation prose, not a complete inventory of sections, mechanics, and AI behavior rules.

### DE-20 — No AI prompt language
**Input:** Any ordinary Description request.
**Expected:** Does not address a downstream AI with instructions such as “You must portray,” “Remember,” or “Never let the character.”

### DE-21 — No analysis leakage
**Input:** Images and analysis findings are source material.
**Expected:** Does not say “the image suggests,” “the analysis indicates,” or expose source/inference labels in the final Description.

### DE-22 — Adaptive structure
**Input:** A short relationship premise that needs only a title and two paragraphs.
**Expected:** Does not force worldbuilding, cast, theme, conflict, or other empty headings.

### DE-23 — Short exact limit
**Input:** `Create Description [maximum 500 characters]`.
**Expected:** Output obeys the stated limit and preserves the most important identity and hook.

### DE-24 — Comprehensive form
**Input:** `Create Description [comprehensive full project description]`.
**Expected:** Uses sufficient sections and explanation to cover the approved project, while remaining readable and human-facing.

### DE-25 — No fixed footer
**Input:** Description generation completes.
**Expected:** No command menu or fixed follow-up text is appended.

### DE-26 — No unrequested assets
**Input:** `Create Description`.
**Expected:** Does not automatically create or regenerate a Context Sheet, Scenario, Character Sheet, World Sheet, or Lorebook Plan.

### DE-27 — No fabricated formal title
**Input:** Project has no title and user did not request title creation.
**Expected:** Uses a neutral heading or starts with the description; does not invent an official project title.

### DE-28 — Exact number of descriptions
**Input:** User requests three descriptions for distinct audiences.
**Expected:** Produces exactly three, each distinct and appropriately targeted, without bonus versions.

### DE-29 — Mystery disclosure
**Input:** Project has a protected hidden identity and user asks for a public spoiler-light description.
**Expected:** Does not reveal the identity. If user instead explicitly requests a complete spoiler-inclusive synopsis, includes it if established and within the requested audience scope.

### DE-30 — Sandbox/open project promise accuracy
**Input:** Open-world project with flexible locations and no predetermined plot path.
**Expected:** Describes its openness without falsely promising branching mechanics, unlimited player freedom, or a predetermined story arc.

### DE-31 — Only requested excerpt
**Input:** `Rewrite only the opening paragraph of the existing Description`.
**Expected:** Returns only the requested paragraph, not a complete replacement description.

### DE-32 — Description of a single faction or relationship
**Input:** `Create Description [describe the Ash Court faction only]`.
**Expected:** Uses the relevant component-level source material and does not imply that the faction description is a full project overview.
