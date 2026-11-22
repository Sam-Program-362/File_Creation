# Foundation Regression Tests — Phases 1–5

Run these after any change to the starter foundation. The complete project test suite will be expanded when the creation modules are implemented.

## Phase 1 — Orchestrator and index

1. Ask for a normal project start. The system routes to the Analysis-first workflow and does not claim that character creation is already implemented.
2. Ask Help about an installed shared system. The system locates the relevant file and explains it briefly.
3. Ask Help about a future reserved module. The system says it is planned but not installed.

## Phase 2 — Commands, workflow, isolation

4. Submit `Create Character [only Akari for now]`. The command router treats the bracketed text as local to this generation.
5. Submit `New Project` after an active project. A separate namespace is created without erasing the first.
6. Submit `Switch Project [name]`. The active namespace changes without carrying over unrelated facts.
7. Generate an output. No fixed command footer is appended.
8. Ask the engine to continue a roleplay. It explains that V3 creates starting messages but does not continue RP.

## Phase 3 — Bedrocks

9. Establish `The king must never kill any citizen.` The engine records it as a Bedrock only when the user establishes it as a core rule.
10. Ask for an opening that implies the king kills a citizen. The Bedrock validator flags and prevents the contradiction.
11. Provide a new instruction that may contradict the Bedrock but is not clearly a revision. The engine asks whether the user intends to revise the Bedrock.
12. Confirm a Bedrock revision. The engine updates the project-level rule rather than leaving both conflicting versions active.

## Phase 4 — Adaptive sections, transfer, evidence

13. Supply a strange hybrid character concept with information that does not fit standard headings. The section system creates custom headings.
14. Put an important detail in the Analysis Sheet that has no standard destination. The transfer process assigns it a custom section in the correct final artifact.
15. Supply an image and a temporary expression. The system distinguishes observed expression from stable personality.
16. Supply a user-provided fact that conflicts with a visual guess. The user-provided fact is preserved.
17. Apply Improvise. The engine proactively completes relevant gaps but does not contradict explicit facts or Bedrocks.

## Phase 5 — Tags

18. Supply `character_description`. The system normalizes it to `Full Physical Description`.
19. Apply Full Physical Description to a full-body reference. The output covers supported upper body, hips, thighs, lower body, face, frame, posture, and other relevant physical details.
20. Apply Detailed as a tag. High-detail mode activates. Merely saying “make the title detailed” does not activate the global tag.
21. Apply Uncensored to one sharp-tongued character. That character's voice retains appropriate profanity; unrelated characters are unaffected.
22. Apply Open Interaction without Open World. Additional participants may appear, but the setting is not automatically unrestricted.
23. Apply Open World without Open Interaction. New locations may appear, but the cast is not automatically unrestricted.
24. Apply Focus and Exclude together. Focus increases priority while Exclude removes the named material from the scoped reference analysis.
25. Auto-detect Uncensored from strong character evidence. The tag is shown as auto-applied, character-scoped, and correctable by the user.
