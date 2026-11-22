---
name: narrative-engine-project-isolation
description: |
  Separates multiple narrative projects within one conversation without
  imposing persistent memory or project-database behavior.
---

# In-Session Project Isolation

## Purpose

Allow more than one unrelated creation project to exist inside a single conversation without mixing their characters, world facts, Bedrocks, tags, or outputs.

This is lightweight, temporary isolation. V3 is designed primarily for one-session projects; it is not a persistent project-management system.

## Default behavior

Assume one active project unless the user clearly starts another.

Do not create artificial project IDs, dashboards, databases, or permanent records for a single-project session.

## Starting a separate project

When the user says `New Project`, introduces a clearly unrelated concept, or explicitly requests a separate project:

1. Establish a new project namespace for the new concept.
2. Keep the previous project's material separate.
3. Make the new project active.
4. Do not import characters, lore, Bedrocks, tags, relationships, or assumptions from the previous project.
5. Do not erase the previous project from the conversation context.

If it is ambiguous whether the user is adding a component to the active project or starting a separate project, use context. Ask one short question only if the distinction materially affects the result.

## Switching projects

When the user says `Switch Project [name]`:

- Switch the active working context to the named project if it can be identified.
- Do not combine project information during the switch.
- If multiple projects have similar names or the target cannot be identified, ask which project they mean.

## Project namespace contents

Keep these items scoped to the project:

- Raw concept and supplied source context.
- Analysis Sheet and its approved interpretation.
- Explicit and auto-applied tags.
- Confirmed project facts.
- Bedrocks.
- Character Sheets and character-specific details.
- World Sheets and setting facts.
- Relationship and plot information.
- Context Sheet.
- Scenario starting messages.
- Description.
- Lorebook Plan.
- Refinements and command-local constraints that have become project-wide only through explicit user direction.

## No cross-project contamination

Never reuse an element from Project A in Project B merely because it is available in the same conversation.

A connection is valid only when the user explicitly asks for a shared universe, crossover, adaptation, or other relationship between projects. Record the intended connection and its boundaries before combining material.

## Temporary working canon

Within the active conversation, treat the latest approved version of each artifact as the current working reference.

However:
- This does not create permanent memory outside the conversation.
- A command-local generation restriction does not become project canon.
- A proposed addition does not become confirmed canon until the user's approval or wording clearly establishes it.
- A deliberate user revision may change established material, including a Bedrock, when the intent to revise is clear.

If the relevant prior content is no longer available, do not invent it. Ask the user to provide the missing artifact or context.
