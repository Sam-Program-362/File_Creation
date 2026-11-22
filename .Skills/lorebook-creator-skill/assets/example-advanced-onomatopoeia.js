/**
 * EXAMPLE ADVANCED SCRIPT — Onomatopoeia / Intimacy Sound Injector
 * 
 * Description (for Janitor Description field):
 * Detects intimacy keywords in the last message and injects detailed rules that force 
 * balanced dialogue + onomatopoeic sounds during sex. Automatically cleans up when 
 * the scene leaves intimacy. Keeps the AI crude, explicit, and in-character.
 */

(function () {
    'use strict';

    var PERSONALITY_SUFFIX = " Currently engaged in intimate activity.";
    var NOTE_MARKER = "[SYSTEM NOTE: When the scene contains intimacy";

    var triggerPatterns = [
        /\bcocks?\b/i, /\bdicks?\b/i, /\bpenis\b/i, /\bshafts?\b/i, /\bballs?\b/i,
        /\bpuss(?:y|ies)\b/i, /\bcunts?\b/i, /\bclits?\b/i, /\bfolds?\b/i, /\bslits?\b/i, /\bholes?\b/i,
        /\bnipples?\b/i, /\bnips?\b/i, /\btits?\b/i, /\bbreasts?\b/i, /\bboobs?\b/i,
        /\bass(?:es)?\b/i, /\bbutts?\b/i, /\bthighs?\b/i,
        /\bcum(?:s|ming|med)?\b/i, /\bprecum\b/i, /\bcreampie\b/i, /\bloads?\b/i,
        /\bwet(?:ter|ness)?\b/i, /\bdrip(?:ping|s)?\b/i, /\bsoaked\b/i, /\bslick\b/i,
        /\bhard(?:er)?\b/i, /\bthrobbing\b/i, /\baching\b/i, /\bswollen\b/i,
        /\bfuck(?:s|ing|ed|er)?\b/i, /\bthrust(?:s|ing|ed)?\b/i, /\bpound(?:s|ing|ed)?\b/i,
        /\bride[sd]?\b/i, /\briding\b/i, /\bslam(?:s|ming|med)?\b/i, /\bgrind(?:s|ing|ed)?\b/i,
        /\bsuck(?:s|ing|ed)?\b/i, /\blick(?:s|ing|ed)?\b/i, /\bkiss(?:es|ing|ed)?\b/i,
        /\bstroke[sd]?\b/i, /\bstroking\b/i, /\brub(?:s|bing|bed)?\b/i,
        /\bpenetrat(?:e|es|ing|ed|ion)\b/i, /\bimpale[sd]?\b/i,
        /\bmoan(?:s|ing|ed)?\b/i, /\bgroan(?:s|ing|ed)?\b/i, /\bgasp(?:s|ing|ed)?\b/i,
        /\bwhimper(?:s|ing|ed)?\b/i, /\bpant(?:s|ing|ed)?\b/i,
        /\bgrab(?:s|bing|bed)?\b/i, /\bsqueeze[sd]?\b/i, /\bsqueezing\b/i,
        /\bejaculat(?:e|es|ing|ed|ion)\b/i, /\borgasm(?:s|ing|ed)?\b/i, /\bclimax(?:es|ing|ed)?\b/i,
        /\bslide[sd]?\b/i, /\bsliding\b/i, /\bpush(?:es|ing|ed)?\b/i, /\bpull(?:s|ing|ed)?\b/i,
        /\bmake love\b/i, /\blovemaking\b/i, /\bhave sex\b/i, /\bfuck each other\b/i, /\bgo down on\b/i,
        /\boral sex\b/i, /\bgive head\b/i, /\beat (?:me|her|him) out\b/i,
        /\bride you\b/i, /\byou ride\b/i,
        /\bagainst the wall\b/i, /\bon the bed\b/i, /\bon the floor\b/i, /\bbent over\b/i,
        /\bfrom behind\b/i, /\bdoggy style\b/i, /\bmissionary\b/i, /\bcowgirl\b/i, /\breverse cowgirl\b/i,
        /\bsixty[\s-]?nine\b/i, /\b69\b/i,
        /\bforeplay\b/i, /\bafterplay\b/i, /\bpillow talk\b/i,
        /\bblowjob\b/i, /\bhandjob\b/i, /\brimjob\b/i,
        /\binside (?:me|you|her|him)\b/i, /\bbetween (?:my|her|his) (?:legs|thighs)\b/i,
        /\bdeeper\b/i, /\bharder\b/i, /\bfaster\b/i, /\brougher\b/i,
        /\bpinned\b/i, /\bon top\b/i, /\bnaked\b/i, /\bnude\b/i, /\bstripped?\b/i, /\bundress(?:ed|ing)?\b/i,
        /\bhorny\b/i, /\baroused\b/i, /\bedge(?:d|s|ing)?\b/i,
        /\bfuck (?:me|you|her|him)\b/i, /\bsuck (?:my|your|her|his)\b/i
    ];

    var SYSTEM_NOTE = "[SYSTEM NOTE: When the scene contains intimacy, sex, or explicit content, you MUST balance descriptive dialogue with onomatopoeic sounds. Dialogue carries thoughts, commands, reactions; onomatopoeia carries breath, pleasure, involuntary sound. Neither may dominate, and both are used during intimacy or sex.\n" +
        "❌ AVOID: *He moaned sharply.* / *She made a choked sound.* / pure sound spam without speech.\n" +
        "✅ DO: *\"Don't stop,\" he gasped, the words breaking into a soft \"nnh...!\"* / *\"More—right there,\" she managed, a shuddering \"haahh~\" escaping.* / *\"Fuck, you feel so good♥\" he whined, voice cracking on a wet \"mmh~\".*\n" +
        "SOUND LIBRARY (vary, never repeat back-to-back):\n" +
        "• Sucking/oral: mmm, slurp, ssslurp, sssweep, glurk, glrk, guhnn, nghn, mmhf, emff, schlick, schlrp, gulp, mmwah, smooch, chu, mwah, and combinations.\n" +
        "• Muffled/mouth-full: mmh, nngh, hangh, hhng, mhm, mmph, mmmpf, hmmrn, ngk, ksshh, and combinations.\n" +
        "• Panting/breathless: aah, hahhh, haaa, hah, grr, agh, ugh, gasp, huff, wheeze, sigh, gasp, grrh, hrrngh, ghh, nnrgh, eergh, errh, and combinations.\n" +
        "• Climax/overwhelm: aahn, ahhn~, haaa♥, nnah♥, cumming♥\n" +
        "SYMBOLS: Use \"~\" to elongate blissful/teasing sounds. Use \"♥\" for deep affection/overwhelming pleasure. Use \"♡\" (heart outline) to show tenderness, soft love, or affectionate warmth. Use \"♪\" (music note) to add a playful, sing-song, or teasing lilt in the voice. Apply them inside dialogue and onomatopoeia, not as decoration.\n" +
        "Stay crude, explicit, and in character. Describe sensation (heat, tightness, friction, taste). Onomatopoeia must support the dialogue, never replace it.]";

    if (typeof context === "undefined" || !context.chat || !context.character) {
        return;
    }

    var lastMsg = (context.chat.last_message || "").toLowerCase().trim();
    if (lastMsg.length === 0) return;

    var triggered = false;
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
})();
