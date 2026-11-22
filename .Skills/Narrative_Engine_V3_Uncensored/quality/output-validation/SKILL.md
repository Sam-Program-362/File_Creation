---
name: narrative-engine-output-validation
version: 1.0.0
status: implemented
stage: 13
description: |
  Validates that each Narrative Engine deliverable has the correct identity,
  purpose, scope, adaptive structure, style, tag behavior, and output format.
---

# Output Validation

## 1. Purpose

Output Validation checks whether the generated artifact is the correct kind of document and satisfies that document's specific contract. A factually coherent answer can still fail if it is the wrong deliverable, uses the wrong audience, or performs work outside the command.

Run this validator for every generated, refined, or expanded artifact.

## 2. General checks for every artifact

1. **Requested target:** The artifact matches the user's command and command-local instructions.
2. **Project scope:** It belongs to the active project and does not include material from another project.
3. **Concept fidelity:** It preserves the concept's central appeal and explicit constraints.
4. **Adaptive structure:** Sections serve the actual content; no unusual concept detail is forced into an unsuitable fixed template.
5. **Completeness:** Relevant material is not omitted because no conventional heading exists.
6. **Section responsibility:** Each section has a clear purpose; information is not placed where it changes meaning.
7. **No empty boilerplate:** No blank or irrelevant sections are included just to imitate a template.
8. **Bedrocks:** Applicable Bedrocks are accurately respected; a visible Bedrocks section is a clean list only.
9. **Tags:** Explicit and auto-applied tags are interpreted within their scope.
10. **Evidence:** Unsupported major additions are not presented as established facts.
11. **Sanitization:** Final creative documents do not contain image-analysis or source-reasoning commentary unless the user requested provenance.
12. **Readable form:** Formatting is clear, organized, and appropriate to the artifact.

## 3. Analysis Sheet contract

Check that:
- the Analysis Sheet is an inspectable interpretation and planning document, not a finished Character/World/Context Sheet;
- it identifies the project type and scope when supported;
- it captures the concept core and narrative focus that matter to the project;
- source observations and inferences are distinguished where relevant;
- explicit and auto-applied tags are distinguishable, with auto-applied scope and rationale;
- confirmed Bedrocks and uncertain Bedrock candidates are not confused;
- missing information and planned expansion are handled according to Improvise and other applicable instructions;
- sections are selected adaptively rather than copied from a mandatory universal template;
- generation direction is connected to the actual concept.

Do not demand image analysis when no image was supplied, or character/world analysis when those dimensions do not apply.

## 4. Character Sheet contract

Check that:
- the output describes the requested character(s) and respects command-local scope;
- it preserves relevant established appearance, personality, behavior, history, dynamics, abilities, limitations, and unusual traits;
- physical-description depth reflects the Full Physical Description tag when it applies;
- voice and profanity reflect Uncensored where scoped, without spreading it to unrelated characters;
- the character is not reduced to generic archetype language when specific behavior was supplied;
- the sections fit this character rather than a rigid template;
- temporary image details have not become permanent traits without support;
- the sheet is a character reference, not an Analysis Sheet, Context Sheet, or Scenario.

## 5. World Sheet contract

Check that:
- the requested setting/world and its actual scope are represented;
- established rules, systems, geography, institutions, factions, cultures, technologies, magic, and causal constraints are included where relevant;
- temporary scene conditions are not converted into permanent world rules without support;
- the world serves the project's concept rather than becoming an unrelated encyclopedia;
- unusual setting mechanics have appropriate custom sections;
- Bedrocks are preserved with their correct scope;
- the output is a World Sheet, not a plot synopsis or Context Sheet.

## 6. Context Sheet contract

Check that:
- it is a comprehensive, self-contained information handoff for a separate AI narrator/roleplayer;
- it integrates project type, premise, intentions, concept, narrative focus, characters, relationships, setting, plot, dynamics, tone, and other information that materially shapes the intended narrative;
- it describes the project in clear informational sections rather than conversationally instructing the AI;
- it does not contain analysis-only headings such as `Provided Elements`, `Missing Elements`, or `Planned Expansion`;
- it is not merely a character-sheet summary or a prompt-like list of commands;
- it includes all project-relevant confirmed Bedrocks;
- an AI receiving only this sheet could understand the project's essential setup without reconstructing the user's chat.

The Context Sheet is the central handoff. Apply the Coverage Validator in full whenever this artifact is the target.

## 7. Scenario starting-message contract

Check that:
- output is one or more opening messages only, never continuation roleplay;
- the exact requested quantity is present (one by default);
- each alternative is meaningfully distinct unless the user requested connected parts;
- prose is vivid and grounded, using physical detail, body language, purposeful sensory texture, and subtext;
- emotion is shown through behavior and speech where practical rather than simply labeled;
- character voices are distinct;
- the default length is 2–4 paragraphs but is adjusted to scene needs and user instructions without padding;
- narration uses single asterisks, dialogue uses quotation marks, private thoughts use triple backticks, and OOC uses `//` only when the user explicitly asks for an OOC reply;
- private thoughts never expose the user's inner state;
- no actions, dialogue, decisions, or thoughts are invented for the user's character;
- no character reacts to or obeys `//` OOC notes;
- the opening creates a natural response opportunity and does not close the central interaction;
- all relevant Bedrocks, context, and character voices are respected.

## 8. Description contract

Check that:
- the audience is human, not a downstream AI;
- the Description explains the requested concept, premise, world, plot, central appeal, and relevant dynamics;
- it is not a Context Sheet shortened, an AI instruction block, a Scenario, or a catalogue of assets;
- analysis jargon and source provenance are absent unless requested;
- disclosure and spoiler depth match the user's instructions;
- Markdown structure supports the selected presentation form;
- it does not invent a complete premise or reveal excluded secrets to compensate for missing source information.

## 9. Lorebook Plan contract

Check that:
- the artifact is a detailed implementation handoff for a separate Lorebook Creator;
- it decides what belongs in the main documents versus normal Lorebook entries versus Advanced Scripts, including when no Lorebook is needed;
- each proposed Lorebook and entry has a purpose, scope, content direction, activation intent, triggers or conditional logic, relationships/dependencies, applicable Bedrocks, and tests where relevant;
- source-derived platform distinctions are preserved;
- the plan contains enough context for implementation without reconstructing the original user conversation;
- it is not merely a list of entry names;
- it does **not** output import-ready Lorebook JSON or executable JavaScript as its deliverable.

## 10. Refinement contract

When target artifact was refined, check the Phase 12 patch rules:
- the exact requested target and changes were resolved;
- unrelated text and sections remain unchanged;
- only necessary dependent artifacts were updated;
- canonical fact changes are distinguished from artifact-local presentation changes;
- Bedrock revisions were authorized clearly;
- the output mode follows the user's request (complete revised artifact, changed sections only, or insertion-ready patch);
- missing original source is not represented as an exact successful patch.

## 11. Expansion contract

When target artifact was expanded, check that:
- all established content remains present unless the user authorized a change;
- additions deepen or broaden the requested scope rather than replacing existing layers;
- added details fit narrative gravity, priority, evidence, tags, and Bedrocks;
- new sections are created when needed;
- additions do not create unrelated lore, padding, or scope creep;
- canon facts and proposed additions remain distinguishable where approval is pending.

## 12. Tag-specific output checks

Apply only the relevant tag checks:

- **Full Physical Description:** include all supported body/physical description dimensions required by its definition; label visual estimates as estimates and avoid invented exact measurements.
- **World Reference / Scenario Reference / Style Reference:** keep extraction within the intended reference purpose.
- **Focus:** allocate attention according to the scoped priorities without fabricating facts.
- **Exclude:** verify excluded material did not leak into the target.
- **Improvise:** fill appropriate gaps as authorized and omit a `Missing Elements` section in the relevant analysis output; do not override Bedrocks or established facts.
- **Detailed:** apply the high-detail mode when the tag is explicitly supplied; do not activate it merely because the word appears in ordinary prose.
- **Uncensored:** preserve appropriate direct language for the scoped voice without forcing profanity into unrelated characters or every sentence.
- **Open Interaction / Open World:** avoid accidentally restricting the cast or location scope.

## 13. Finding handling

- **BLOCK:** wrong artifact identity, violation of a direct output constraint, wrong Scenario count, invented user-character action/thought, incomplete Context Sheet on a core item, Lorebook Plan outputting implementation code, or another material contract failure.
- **REPAIR:** clear formatting error, misplaced section, obvious tag behavior miss, avoidable repetition, or local omission with unambiguous source.
- **WARN:** uncertain intended audience, unavailable source detail, unclear spoiler boundary, or output limitation that cannot be decided without the user.
- **PASS:** the artifact fulfills its contract.

Correct clear local issues and revalidate. Do not make a substantive creative decision under cover of QA.

## 14. Completion checklist

- [ ] The output is the requested artifact type.
- [ ] All general output checks pass.
- [ ] The artifact-specific contract passes.
- [ ] Relevant tag behaviors and scopes are respected.
- [ ] Bedrocks and evidence boundaries are respected.
- [ ] No unrelated deliverable or unsolicited command menu was added.
- [ ] Any repair was rechecked.
