---
name: narrative-engine-tag-system
description: |
  Resolves explicit and automatic narrative tags, defines their scope, and
  loads the individual built-in tag instructions needed for a project.
---

# Tag System

## Purpose

Tags are reusable controls that guide interpretation, extraction, emphasis, creative completion, style, and project openness.

A tag must have a precise operational definition. The model should not rely on a short label alone when a tag has a dedicated definition file.

## Tag naming and normalization

- Use readable natural-language names, with spaces: `Full Physical Description`, not `full_physical_description`.
- Do not use underscores in visible built-in tag names.
- Match tag names case-insensitively.
- Ignore harmless repeated spaces and surrounding whitespace.
- Each tag has one canonical display name.
- Legacy V2 names may be recognized as aliases, but new output uses the canonical human-readable name.

## Scope

Every tag applies to a scope. Possible scopes include:
- whole project;
- a specific character;
- a specific world or location;
- a reference image or source;
- a relationship;
- a plotline;
- a specific scenario or output.

If the user does not specify a scope, infer the narrowest scope that fits the context. Do not spread a character-specific tag to unrelated characters or the entire project.

## Explicit versus automatic tags

### Explicit tags
Tags deliberately supplied by the user in a tag list, tag field, reference instruction, or clearly tagged command context.

Preserve their scope. Do not silently remove or reinterpret them.

### Auto-applied tags
The Analysis process may add a tag when the concept strongly supports it.

When doing so:
- mark it as `Auto-applied` in the Analysis Sheet;
- state its scope;
- give a short reason;
- keep it open to user correction;
- do not represent it as a user-supplied tag.

Do not auto-apply tags merely because the project is long or information is incomplete.

## Loading procedure

1. Identify all explicit tags and their scope.
2. Normalize aliases to canonical names.
3. Read each matching definition file in `built-in/`.
4. Apply each tag only to the information or output within its scope.
5. Detect possible automatic tags only when supported by the concept.
6. Present auto-applied tags in the Analysis Sheet.
7. During final generation, obey tag behavior without inserting tag-definition explanations into the artifact.

## Interaction between tags

- Tags may combine when their behaviors do not conflict.
- `Focus` changes priority; it does not authorize fabrication.
- `Exclude` removes selected material from consideration for the relevant task and scope.
- `Full Physical Description` controls depth and coverage of physical description.
- `Detailed` controls broad explanatory depth when explicitly supplied as a tag.
- `Improvise` authorizes proactive completion of missing context while preserving established facts and Bedrocks.
- `Uncensored` preserves direct language, explicit content, and full adult/extreme material fidelity where it fits the relevant voice or project; it forbids sanitization.
- `Open Interaction` and `Open World` prevent unintended closed-cast and closed-location assumptions within their scopes.

If two tags appear to conflict, inspect their individual definitions and the user's stated intent. Prefer the narrowest interpretation that satisfies both. If they cannot be reconciled and the conflict materially affects the project, ask a concise clarification rather than silently dropping a tag.

## Legacy V2 aliases

Recognize these historical labels where encountered:
- `character_description` → `Full Physical Description`
- `world_reference` → `World Reference`
- `scenario_reference` → `Scenario Reference`
- `style_reference` → `Style Reference`
- `focus:[...]` → `Focus`
- `exclude:[...]` → `Exclude`

Display and document the normalized human-readable form in V3.

## Built-in definitions

Read only the relevant definitions:
- `built-in/full-physical-description.md`
- `built-in/world-reference.md`
- `built-in/scenario-reference.md`
- `built-in/style-reference.md`
- `built-in/focus.md`
- `built-in/exclude.md`
- `built-in/improvise.md`
- `built-in/detailed.md`
- `built-in/uncensored.md`
- `built-in/open-interaction.md`
- `built-in/open-world.md`

## Completion check

- [ ] Tags are normalized to human-readable names.
- [ ] Aliases are recognized.
- [ ] Every tag has a clear scope.
- [ ] Each tag's own file has been read before applying its detailed behavior.
- [ ] Explicit tags are preserved.
- [ ] Automatic tags are labeled and justified.
- [ ] No tag is applied to unrelated project components.
