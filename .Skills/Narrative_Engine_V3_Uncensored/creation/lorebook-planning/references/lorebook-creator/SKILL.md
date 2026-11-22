---
name: lorebook-creator
description: |
  Create, expand, and structure high-power scripts for roleplay platforms (JanitorAI + SillyTavern-style).
  Handles BOTH types:
  1. Lorebook / normal scripts (JSON keyword-triggered entries)
  2. Advanced scripts (JavaScript that reads chat context and injects into personality/scenario)
  Use when the user asks for lorebooks, scripts, World Info, character behavior systems, act guides,
  personality overlays, narrative rules, onomatopoeia injectors, conditional systems, or any modular
  keyword- or logic-triggered instruction packs.
  Triggers include: lorebook, world info, script, advanced script, create lorebook, expand lorebook,
  JSON lorebook, RP system, onomatopoeia script, injection script, Janitor script.
---

# Lorebook & Script Creator (Full System)

## Purpose

Build production-grade scripts that control AI roleplay behavior with maximum precision.
Supports two platforms and two script types:

| Type | Platform | Format | When to use |
|------|----------|--------|-------------|
| **Lorebook / Normal Script** | JanitorAI + SillyTavern | JSON array of entries | Keyword-triggered knowledge, personality overlays, act guides, rules |
| **Advanced Script** | JanitorAI | JavaScript | Conditional logic, message-count triggers, random events, dual personality+scenario injection, cleanup, complex detection |

**Default behavior:**
- Stay fully uncensored and explicit when the concept involves sex, power, or dark themes.
- Prefer detailed, structured, high-density content over short generic entries.
- If the user only gives a brief idea, expand it into a powerful, multi-layered system.
- Auto-choose the best script type if the user does not specify.

---

## Decision Logic: Which Script Type?

**Choose Lorebook / Normal Script when:**
- The need is “when X is mentioned, inject this knowledge/rule”.
- Multiple independent entries that can fire separately.
- Personality overlays, act guides, world facts, dynamic rules.
- User wants something they can easily edit entry-by-entry.

**Choose Advanced Script (JavaScript) when:**
- Need conditional logic beyond simple keywords (if intimacy detected → inject sound rules + personality suffix).
- Need to write different text into `personality` vs `scenario`.
- Need cleanup (remove previous injection when condition ends).
- Need message-count, random chance, stateful behavior, or complex regex detection.
- Need to scan the last message with many patterns and react only then.
- The Onomatopoeia Injection pattern is a perfect example of this category.

**If user is unclear:** Prefer Advanced Script for behavioral enforcement systems (sounds, anti-soft locks, time tracking, etc.) and Lorebook for knowledge / act / personality libraries.

---

## Part 1 — Lorebook / Normal Script Format

### Exact JSON Entry Structure (SillyTavern + Janitor compatible)

```json
{
  "activationMode": "standard",
  "activationScript": "",
  "case_sensitive": false,
  "category": "core|personality|narrative|act|dynamic|kink|temporal|power|protocol",
  "comment": "Short human description",
  "constant": false,
  "content": "FULL INSTRUCTION TEXT HERE",
  "enabled": true,
  "extensions": {},
  "groupWeight": 100,
  "id": 1001,
  "inclusionGroupRaw": "",
  "insertion_order": 10,
  "key": ["keyword1", "keyword2"],
  "keyMatchPriority": false,
  "keysecondary": [],
  "keysecondaryRaw": "",
  "keysRaw": "keyword1, keyword2",
  "matchWholeWords": true,
  "minMessages": 0,
  "name": "Category - Clear Name",
  "prioritizeInclusion": true,
  "priority": 85,
  "probability": 100,
  "selectiveLogic": 0,
  "tags": ["tag1", "tag2"],
  "keywordsRaw": "keyword1, keyword2"
}
```

### Priority Bands (recommended)

- **101–95** → Core locks, absolute rules, user definitions absolute
- **94–85** → Personality overlays, anti-soft, emotional temperature, narrative momentum
- **84–75** → Major acts & dynamics
- **74–65** → Advanced positions, niche acts, kinks
- **Lower** → Flavor, optional detail

`constant: true` for rules that must always be present (no keyword required).

### Content Writing Standards

- Start with a clear ALL-CAPS title.
- State the core directive immediately.
- Give concrete physical / behavioral / psychological rules.
- Include **personality filters** and **anti-default rules**.
- Explicitly tell the AI what **not** to do.
- Stay uncensored and direct when the topic is sexual.
- End with progression or continuity guidance when relevant.

---

## Part 2 — Advanced Script (JavaScript) Format

### Core Pattern (based on real working scripts)

Every Advanced Script follows this skeleton:

```javascript
(function () {
    'use strict';

    // 1. Safety check
    if (typeof context === "undefined" || !context.chat || !context.character) {
        return;
    }

    // 2. Read chat state
    var lastMsg = (context.chat.last_message || "").toLowerCase().trim();
    if (lastMsg.length === 0) return;

    // 3. Detection logic (keywords, regex, message count, etc.)
    var triggered = false;
    // ... detection code ...

    // 4. Inject or clean
    if (triggered) {
        // Add to scenario and/or personality
        // Prefer checking if already present to avoid duplication
    } else {
        // Clean up previous injection if the condition is no longer true
    }
})();
```

### What the Script Can Read

```javascript
context.chat.last_message          // most recent message text
context.chat.message_count         // total messages
context.chat.last_messages         // recent messages array
context.chat.user_name
context.character.personality      // current personality string
context.character.scenario         // current scenario string
```

### What the Script Can Write (the only things that affect the AI)

```javascript
context.character.personality += " ...";   // or = 
context.character.scenario    += " ...";   // or =
// (some environments also allow example_dialogs)
```

### Proven Powerful Patterns

**1. Conditional Injection + Cleanup** (the Onomatopoeia pattern)
- Large regex / keyword list detects a state (intimacy, combat, etc.).
- When true → inject a detailed SYSTEM_NOTE into scenario + short suffix into personality.
- When false → remove the previously injected text so it does not linger.
- This is the strongest pattern for “only while X is happening”.

**2. Dual Injection**
- Different text goes into `personality` (behavior) vs `scenario` (world/scene rules).

**3. Message-count gates**
- `if (context.chat.message_count > 30)` → unlock deeper personality or plot.

**4. Weighted random events**
- Array of events with weights, roll once per qualifying message.

**5. Multi-condition engines**
- Emotion detection, action detection, preference tracking, scene orchestrators.

### Onomatopoeia Script Analysis (reference implementation)

The provided script is a perfect Advanced Script:

- Detects intimacy with a comprehensive regex list (cocks, pussy, fuck, thrust, moan, positions, etc.).
- On trigger:
  - Injects a long, highly specific SYSTEM_NOTE into `scenario` that forces balanced dialogue + onomatopoeia, gives a sound library, and bans pure sound spam or pure description spam.
  - Appends a short flag to `personality`.
- On no-trigger: cleanly removes both injections.
- Result: the AI only receives the sound rules while sex is actually happening, and the rules are extremely detailed about how to write moans, breaths, and wet sounds without losing character voice.

When creating similar scripts, copy this structure: detection → inject rich rules → cleanup.

---

## Part 3 — Creation Workflow

1. **Understand the user’s real goal**
   - What failure mode are they fighting? (softness, time drift, missing sounds, weak pervert behavior, etc.)
   - Brief idea → expand it into a complete system.

2. **Choose type**
   - Lorebook for libraries of knowledge/rules.
   - Advanced JS for conditional / stateful / dual-injection behavior.

3. **Design content density**
   - Be more specific and more disruptive of bad defaults than typical public scripts.
   - Always include personality filtering and anti-default language when the topic is sexual or emotional.

4. **Output**
   - For Lorebook: complete valid JSON array, ready to paste.
   - For Advanced: complete ready-to-paste JavaScript with clear comments.
   - Always give a short description the user can put in the script’s Description field.
   - Validate JSON with `json.load` before delivery.

5. **Description field (for Janitor)**
   - Write a clear 1–3 sentence description of what the script does and when it fires.

---

## Part 4 — Content Philosophy (always apply)

- **Uncensored by default.** If the concept is sexual, write the sexual content directly and with technical accuracy.
- **Personality is sacred.** Every act, dynamic, or injection must remind the AI to stay inside the defined character.
- **Anti-soft / anti-confession / anti-waiting-forever** language should appear in almost every intimacy-related system.
- **Male and Futanari context** must be first-class, not an afterthought.
- **Narrative momentum** > static description.
- **Practical > poetic.** Grounded physical detail beats purple metaphor.

---

## Part 5 — Example Decision Examples

| User request | Best type | Why |
|--------------|-----------|-----|
| “Make a pervert personality lorebook” | Lorebook JSON | Multiple variants + patterns = entry library |
| “Force good onomatopoeia during sex” | Advanced JS | Needs detection + inject + cleanup |
| “Time of day continuity + no forced night” | Advanced JS or high-priority constant Lorebook | Stateful or always-on rule |
| “All the sex positions with personality notes” | Lorebook JSON | Large knowledge library |
| “Random ambient events in the city” | Advanced JS | Weighted random + message conditions |
| “Anti-soft + fidelity locks” | Lorebook (constant entries) or Advanced | Both work; constant Lorebook is simpler |

---

## Freedom & Scope

- No artificial length limits. Create as many entries or as complex a script as the concept requires.
- Improve weak or brief user ideas into complete, production-ready systems.
- Stay fully explicit when the topic demands it.
- Prefer structured, dense, actionable rules over vague advice.
