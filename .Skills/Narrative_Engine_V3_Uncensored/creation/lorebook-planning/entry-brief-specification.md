# Lorebook Planning — Entry Brief Specification

Use this specification for every proposed normal Lorebook entry. It describes what the downstream Lorebook Creator needs to know; it is not a JSON schema and must not be rendered as a JSON object.

## Required entry brief

### Entry identity
- **Name:** Human-readable entry name.
- **Category:** A concise organizational category appropriate to the project. The supplied source's example categories include core, personality, narrative, act, dynamic, kink, temporal, power, and protocol; treat these as examples, not a mandatory taxonomy.
- **Comment / purpose label:** One short sentence describing the entry's role.

### Requirement and intended effect
- **Problem addressed:** The specific failure or missing information being solved.
- **Intended effect:** What the downstream AI must know, preserve, or do while the entry is active.
- **Content direction:** Concrete required facts, behaviors, examples, personality filters, anti-default rules, progression or continuity requirements.
- **Forbidden defaults:** Include only the behaviors that matter to this entry.

### Scope and source
- **Owner / scope:** Project, character, relationship, world, location, event, or custom scope.
- **Source facts:** Approved source details with their status where necessary.
- **Bedrocks:** The relevant confirmed Bedrock points. The visible Bedrocks list elsewhere in the plan must contain only the points; implementation explanations remain here.
- **Tags:** Applicable tag and scope. Read the individual tag definition before applying it.

### Activation design
- **Activation type:** Constant or keyword-triggered.
- **Rationale:** Why this activation lifetime is correct.
- **Primary keys:** The likely trigger words or phrases.
- **Secondary keys / selective condition:** Required co-occurrence or selective logic, only when useful and supported.
- **Matching settings:** Case sensitivity, whole-word matching, and key-match priority recommendations when meaningful.
- **Message threshold:** Minimum message count only if required by the concept.
- **Non-trigger examples:** Situations or words that should not activate the entry.

### Priority and order
- **Priority recommendation:** V3 band and rationale. Numeric score only when meaningful and platform-validated.
- **Insertion relationship:** Earlier / later relative to named entries, based on dependency and conflict behavior.
- **Probability / selection:** Whether probabilistic or inclusion-group behavior is required; otherwise say not needed / downstream default.

### Dependencies and validation
- **Co-activation:** Which entries should be active together.
- **Exclusions:** Which entries should not co-activate, if any.
- **Conflict behavior:** Which rules take precedence in content terms; do not invent runtime precedence mechanics.
- **Test cases:** Positive trigger, negative trigger, overlap, edge case, and Bedrock / character-fidelity validation.

## Schema awareness

The source entry schema lists these field names:

`activationMode`, `activationScript`, `case_sensitive`, `category`, `comment`, `constant`, `content`, `enabled`, `extensions`, `groupWeight`, `id`, `inclusionGroupRaw`, `insertion_order`, `key`, `keyMatchPriority`, `keysecondary`, `keysecondaryRaw`, `keysRaw`, `matchWholeWords`, `minMessages`, `name`, `prioritizeInclusion`, `priority`, `probability`, `selectiveLogic`, `tags`, and `keywordsRaw`.

The planner should not create actual values for every field. Use three labels:

- **Recommended:** The planning logic has a grounded preference (for example, constant versus keyword-triggered, key themes, or relative insertion order).
- **Downstream default:** No project-specific reason to deviate from the target creator's validated default.
- **Platform validation required:** The source does not define the precise field semantics or the target platform may differ.

Never invent allowed enum values or detailed semantics for `selectiveLogic`, `activationScript`, `extensions`, inclusion groups, or other fields not explained by the source. The downstream creator owns final schema construction and validation.
