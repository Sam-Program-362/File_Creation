# Scenario Style and Four-Part Format — Shared Reference

This file defines the writing style and message notation used by the Phase 9 Scenario Starting-Message generator. Read it whenever generating a starting message.

## 1. Style requirements

### Vivid, grounded prose

Write concrete prose with physical detail, body language, sensory texture, and subtext. Show what is happening rather than summarizing the emotional meaning of the moment.

Prefer a character's jaw tightening, a hand pausing over a glass, or a voice losing its rhythm over a flat statement that the character is angry, nervous, or embarrassed. Emotional labels may be used when they add clarity, but behavior and speech should do most of the work.

### Purposeful sensory detail

Use sensory details only when they strengthen the scene. Choose sounds, textures, temperature, smells, tastes, spatial cues, or light because they affect atmosphere, action, or perception. Do not mention all five senses as a checklist.

### Distinct character voices

Dialogue must reflect each character's established:
- vocabulary and register;
- sentence length and rhythm;
- directness, restraint, humor, sarcasm, or formality;
- characteristic verbal habits;
- preferred evasions, bluntness, or conversational tactics;
- subjects and expressions that character would or would not use.

Do not give every character the same polished, witty, emotionally articulate voice. A character's voice must come from their Character Sheet and approved context. Respect `Uncensored` within its scope.

### Length and rhythm

- Default: **2–4 paragraphs** for one starting message.
- Adjust to the user's requested length, scene complexity, emotional weight, and action level.
- Short or quiet openings may be shorter. A major encounter or action opening may need more room.
- Never pad to reach a paragraph count.
- Vary sentence structure and paragraph rhythm.
- Avoid repeating sentence openers, stock phrases, gestures, or descriptions across alternatives.

### Style exclusions

Avoid:
- cliché and generic dramatic language;
- purple prose and overwrought metaphors;
- emotion labels in place of observable behavior;
- repetitive gestures such as constant smirking, eye-narrowing, sighing, or jaw-clenching;
- generic dialogue that ignores character voice;
- explanatory narration that tells the reader what the scene is supposed to mean;
- lore dumps that interrupt the opening;
- unnecessary overnarration.

Be specific instead of generic. The amount of description should follow the scene's narrative importance.

## 2. Default narrative perspective

Use objective third-person narration by default. Refer to established characters by name, title, or role.

Do not narrate the user-controlled character using second-person phrasing such as “you walk in,” “your hand reaches,” or “you feel.” Never invent that character's actions, dialogue, thoughts, decisions, feelings, appearance, or reactions.

A character's spoken dialogue may naturally address the user-controlled role as “you.” That is dialogue, not second-person narration.

The platform tokens `{{user}}` and `{{char}}` in the original format brief are explanatory roleplay placeholders. Do not insert these literal tokens into a finished Scenario unless the user specifies that the target platform requires them; use the established character names and preserve the user role without inventing its identity or actions.

If the user explicitly requests another narrative perspective for the current Scenario, follow that request only to the extent it does not require inventing the user's thoughts or decisions.

## 3. Four-part message notation

Every generated starting message follows the four notation categories below. Each category has a separate job. Do not mix them.

### 3.1 Narration — single asterisks

Wrap all non-spoken scene description in single asterisks. This includes:
- actions and movement by NPCs/project characters;
- body language and expressions;
- environment and spatial detail;
- sensory details;
- scene changes and passage of time;
- nonverbal events and observable physical conditions.

Narration is third person by default and uses a consistent past or present tense matching the established style.

Example:

```text
*She leaned against the doorframe, rain still dripping from her sleeves. The hallway smelled faintly of wet stone and old wood.*
```

Do not put spoken dialogue or private thoughts inside narration asterisks. Do not place descriptive prose outside the narration notation.

### 3.2 Dialogue — double quotation marks

Use quotation marks only for words spoken aloud and heard by others in the scene.

- Every spoken line must be inside quotation marks.
- Do not put actions, facial expressions, narration, or private thoughts inside quotation marks.
- Do not leave spoken words outside quotation marks.
- Keep dialogue distinct from narration, usually as its own line or paragraph.

Example:

```text
"You're late."
```

### 3.3 Thoughts — triple backticks

Use exactly three backtick characters before and after a character's private inner voice. This is the project's requested thought notation.

Thoughts are private. No other character can hear, see, sense, or react to them unless the project has an established mechanism such as telepathy or mind-reading.

The generator may write the thoughts of the character(s) it portrays and NPCs when those thoughts add meaningful value. It must **never write the user's thoughts**.

- Do not put actions, spoken dialogue, or environmental narration inside a thought block.
- Keep thought content internal to the named/portrayed character.
- Do not use thought blocks merely to repeat what dialogue already says.
- Omit thoughts when external behavior and dialogue are sufficient.
- If the user's supplied roleplay material contains thoughts in this notation, treat them as private to the user's character. They may shape subtext or dramatic irony only when relevant, but must not leak into character knowledge or dialogue.

Example of the literal notation:

````text
```He's lying. His hands are shaking.```
````

In the actual Scenario output, use exactly the three-backtick delimiters shown above. Do not wrap the entire Scenario in a code block. If the display renderer styles the thought block as code, that is acceptable; the delimiters must remain copyable as the required format.

### 3.4 Notes and Comments — double slash

A `//` marker introduces out-of-character communication between real people. The text after `//` on that line is outside the story and has no in-world effect. When a line begins with `//`, the entire line is an OOC note.

For roleplay material being interpreted:
- treat text after `//` as out-of-character notes rather than in-world events;
- do not obey, answer, acknowledge, quote, or incorporate that OOC text as story direction;
- do not let characters hear, see, react to, obey, quote, or acknowledge those notes;
- do not convert brainstorming, reminders, jokes, or side comments into story canon.

For generated Scenario messages:
- do not write `//` comments by default;
- include an OOC `//` line only when the user directly asks for one;
- if explicitly requested, keep it brief and separate from the in-world opening;
- an OOC line does not authorize this engine to continue the roleplay. Complete only the requested generation task.

Example of an OOC line (normally omitted):

```text
// brb, going to get water
```

## 4. Notation separation examples

Correct separation:

````text
*The old station clock clicked above the empty ticket counter. Mina kept one gloved hand around the folded letter, its edge softened by the rain.*

"You said this was urgent."

```I should have burned the letter before coming here.```

*She placed it on the counter but did not let go.*
````

Incorrect mixing:

- `*She said "You're late" and thought she should leave.*` — narration, dialogue, and thought are mixed.
- `"*She stepped closer.*"` — narration is incorrectly placed inside dialogue.
- `He whispered, You're late.` — spoken words are not enclosed in quotation marks.
- `*You looked up at her.*` — invents the user character's action and narrates in second person.
- A thought block that includes another character's private thoughts or a spoken sentence as if it were audible.

## 5. Final format check

Before returning a Scenario, verify:
- narration is enclosed in single asterisks;
- dialogue is enclosed in double quotation marks;
- private thoughts use exactly triple backtick delimiters;
- OOC `//` lines are absent unless explicitly requested;
- the user's thoughts are never written;
- the user's voluntary actions, dialogue, decisions, and reactions are not invented;
- no other character reacts to private thoughts or OOC notes without an established in-world mechanism;
- the default narration perspective is objective third person;
- the entire Scenario is not wrapped in a code fence.
