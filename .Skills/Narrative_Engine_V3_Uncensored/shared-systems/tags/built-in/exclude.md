# Exclude

## Purpose

Explicitly prevent selected information from a reference or source from influencing the current analysis or creation task.

## Syntax

Examples:

- `Exclude: expression`
- `Exclude: pose`
- `Exclude: background`
- `Exclude: accessories`
- `Exclude: objects`
- `Exclude: clothing`
- `Exclude: environment`
- `Exclude: expression, pose, background`

Other clear exclusion values may be accepted.

## Behavior

- Ignore the excluded element when interpreting the relevant source.
- Do not use excluded details as evidence in the Analysis Sheet.
- Do not transfer excluded details into final project material.
- Respect the scope of the exclusion: a clothing exclusion for one reference does not automatically remove clothing facts supplied separately by the user.

## Conflict handling

A later explicit user instruction may restore or directly provide a previously excluded detail. Apply the later instruction within its stated scope.

Exclude is a source-selection control. It is not permission to delete established project facts from unrelated sources.
