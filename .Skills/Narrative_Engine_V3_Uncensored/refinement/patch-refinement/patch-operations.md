---
name: narrative-engine-patch-operations
status: implemented
stage: 12
---

# Patch Operations and Preservation Rules

This reference defines how Patch Refinement edits the text of an existing artifact. It is loaded by the sibling `SKILL.md` in this folder.

## 1. Operation definitions

| Operation | Allowed effect | Preservation rule |
|---|---|---|
| ADD | Insert new requested information | Existing text remains untouched; insert at the most relevant location. |
| REPLACE | Correct a specific statement or block | Replace only the smallest complete unit that is actually wrong or outdated. |
| REMOVE | Delete explicitly unwanted information | Remove only the specified material; check for dependent references that become false. |
| REPHRASE | Change wording without changing meaning | Keep the same facts, scope, tone, and degree of certainty. |
| MOVE | Reposition content | Move the original wording unchanged unless wording edits were also requested. |
| RETITLE | Change a heading/label | Do not rewrite its body or neighboring sections. |
| SPLIT | Divide one section into multiple sections | Preserve all original content and assign every part to the correct new section. |
| MERGE | Combine sections | Preserve every information unit; do not compress or summarize during merge unless requested. |
| SCOPE ADJUSTMENT | Change which entities, situations, or time period a statement covers | State the precise new scope; inspect dependent references for accidental overgeneralization. |

## 2. Exact preservation standard

Treat each existing sentence, paragraph, bullet, section, and ordering decision as intentional unless the user identifies it for change.

Do not:
- rewrite a paragraph because a sentence inside it changed;
- alter style, punctuation, grammar, headings, or formatting outside the patch;
- rename neighboring sections to make them look consistent;
- replace a detailed passage with a shorter summary;
- remove repeated facts merely because they appear redundant, unless the user requests deduplication or the repetition creates a specific contradiction;
- introduce new examples or explanations unrelated to the request.

If the requested edit makes a sentence grammatically dependent on adjacent text, make the smallest adjacent correction required for readability. Do not use that as permission to rewrite the whole paragraph.

## 3. Replacement rules

A REPLACE operation is appropriate when the old statement is explicitly wrong, outdated, or being intentionally revised.

- Replace the entire smallest coherent statement, not an isolated word that leaves a broken sentence.
- Search the same artifact for duplicate instances of the obsolete fact.
- Update duplicate instances only when they assert the same changed fact.
- Preserve other uses of the same word or concept when they are not affected.

## 4. Deletion rules

Deletion requires clear authorization.

- If the user says remove, delete, omit permanently, or no longer include a specified element, remove that element from the target.
- If the deleted element is canon-relevant, inspect dependent artifacts and remove or update stale references only when needed.
- If a deletion would remove a Bedrock, clarify whether the user intends to revise the Bedrock unless the intention is unmistakable.
- Do not equate “remove from this Description/Scenario” with “remove from project canon.”

## 5. Addition rules

When adding material:

- Place it in the section that owns the information.
- If no suitable section exists, create a narrowly scoped, project-appropriate section using Adaptive Sections.
- Do not force the content into a semantically wrong section.
- Do not duplicate it in several sections of the same artifact unless cross-reference or repetition is genuinely needed for usability.
- Apply Information Transfer to determine which other outputs also need the fact.

## 6. Structural edit rules

Section isolation means a change to one section should not disturb unrelated sections. It does not mean sections are factually independent.

- Do not reorganize the entire artifact when one section is moved or split.
- Preserve every information unit when moving or merging material.
- If a section boundary causes required information to be lost or misclassified, create a suitable section rather than dropping the detail.
- Bedrocks remain in their dedicated clean list section; do not merge explanations into that list.

## 7. Conflict classes

| Conflict | Handling |
|---|---|
| User clearly says an earlier fact was wrong | Replace the old fact and update affected references. |
| User clearly revises an existing project fact | Treat as a canonical change; propagate where relevant. |
| New instruction conflicts with a Bedrock, but intent to revise is clear | Revise the Bedrock and affected assets. |
| New instruction conflicts with a Bedrock, intent is unclear | Ask one concise clarification. |
| Two explicit sources conflict and neither is clearly newer/corrective | Preserve the conflict; ask only if it materially affects the patch. |
| Inference conflicts with an explicit fact | Explicit fact wins; remove/correct the inference only where it is being used as asserted content. |
| A downstream artifact is stale relative to a newer approved source | Patch the stale reference without changing the current source. |
| A local command constraint appears to conflict with project canon | Apply it only to the current operation unless the user says it changes canon. |

## 8. Output modes

### Complete artifact mode — default

Return the full revised artifact when:
- the exact previous version is available;
- the complete text can be returned without truncation;
- unchanged content can be preserved verbatim.

### Exact patch mode

Use when the source is very long or the user asks for patch-only output. Include:
- artifact name;
- exact section/anchor;
- operation (add, replace, remove, etc.);
- the complete new block;
- what remains unchanged.

Never output a vague instruction such as “update the character's personality section” when exact replacement text can be provided.

### Diff/summary mode

Use only when requested. Summarize changed locations and operation types without rewriting the artifact.

## 9. Patch integrity checks

A patch is not complete until the system checks that:
- the patch anchor matched the intended content;
- no duplicate or stale version remains in the target;
- all unmodified content is preserved;
- dependencies were examined according to the dependency map;
- Bedrocks remain intact or were deliberately revised;
- the output remains valid for its artifact type.
