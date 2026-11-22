# Advanced Script Patterns (JanitorAI JavaScript)

## Core Safety + Context Skeleton

```javascript
(function () {
    'use strict';
    if (typeof context === "undefined" || !context.chat || !context.character) {
        return;
    }
    var lastMsg = (context.chat.last_message || "").toLowerCase().trim();
    if (lastMsg.length === 0) return;

    // ... your logic here ...
})();
```

## Pattern 1: Conditional Injection + Cleanup (Strongest for temporary rules)

Used by the Onomatopoeia Injection Script.

```javascript
var NOTE_MARKER = "[SYSTEM NOTE: When the scene contains intimacy";
var SYSTEM_NOTE = "[SYSTEM NOTE: ... long detailed rules ...]";
var PERSONALITY_SUFFIX = " Currently engaged in intimate activity.";

var triggered = false;
// large regex list or keyword checks
for (var i = 0; i < triggerPatterns.length; i++) {
    if (triggerPatterns[i].test(lastMsg)) {
        triggered = true;
        break;
    }
}

var personality = context.character.personality || "";
var scenario = context.character.scenario || "";

if (triggered) {
    if (scenario.indexOf(NOTE_MARKER) === -1) {
        context.character.scenario = SYSTEM_NOTE + "\n" + scenario;
    }
    if (personality.indexOf(PERSONALITY_SUFFIX) === -1) {
        context.character.personality = personality + PERSONALITY_SUFFIX;
    }
} else {
    if (scenario.indexOf(NOTE_MARKER) !== -1) {
        context.character.scenario = scenario.replace(SYSTEM_NOTE + "\n", "");
    }
    if (personality.indexOf(PERSONALITY_SUFFIX) !== -1) {
        context.character.personality = personality.replace(PERSONALITY_SUFFIX, "");
    }
}
```

**Why this is powerful:** The heavy rules only exist in the prompt while the condition is true. When the scene leaves intimacy, the rules disappear cleanly. No permanent pollution of the character card.

## Pattern 2: Dual Injection (different text to personality vs scenario)

```javascript
if (triggered) {
    context.character.personality += " [behavior modifier]";
    context.character.scenario += " [scene / world rule]";
}
```

## Pattern 3: Message-count gate

```javascript
if (context.chat.message_count >= 40) {
    // unlock deeper content
}
```

## Pattern 4: Weighted random

```javascript
var events = [
    { text: "Event A", weight: 50 },
    { text: "Event B", weight: 30 },
    { text: "Event C", weight: 20 }
];
// roll and inject the chosen text
```

## Detection Best Practices

- Prefer a large, well-curated regex list over a few broad words.
- Always `.toLowerCase()` the message before testing.
- Guard against empty messages.
- When injecting long notes, use a unique marker string so you can reliably find and remove them later.
