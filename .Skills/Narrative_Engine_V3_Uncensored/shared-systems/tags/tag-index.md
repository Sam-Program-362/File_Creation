# Built-in Tag Index

| Canonical tag | Definition file | Main function | Legacy alias |
|---|---|---|---|
| Full Physical Description | `full-physical-description.md` | Detailed full-body physical description | `character_description` |
| World Reference | `world-reference.md` | Extract environmental / setting information | `world_reference` |
| Scenario Reference | `scenario-reference.md` | Treat source as a particular scene or moment | `scenario_reference` |
| Style Reference | `style-reference.md` | Extract artistic style and presentation | `style_reference` |
| Focus | `focus.md` | Prioritize selected information areas | `focus:[...]` |
| Exclude | `exclude.md` | Ignore selected reference elements | `exclude:[...]` |
| Improvise | `improvise.md` | Proactively complete missing context | New in V3 |
| Detailed | `detailed.md` | Activate extensive explanatory detail | New in V3 |
| Uncensored | `uncensored.md` | Preserve blunt language and voice where appropriate | New in V3 |
| Open Interaction | `open-interaction.md` | Keep the cast / participants open | New in V3 |
| Open World | `open-world.md` | Keep the setting / locations open | New in V3 |

## Tag syntax

Tags may be supplied in ordinary readable form, for example:

`Tags: Full Physical Description, Detailed`

Parameterized tags may be written as:

`Focus: appearance, personality`

`Exclude: expression, pose, background`

When a tag is scoped, make the scope clear:

`Tags for Akari: Full Physical Description, Uncensored`

The syntax is illustrative. The tag router should also understand clear natural-language tag declarations.
