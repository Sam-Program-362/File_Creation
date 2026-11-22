# Superseded: Phase 6 Scaffold Validation

This document validated only the initial directory/module scaffold. Phase 6 has since received operational AI-skill procedures. Use `phase-6-analysis-regression-tests.md` for behavior testing.

---

# Phase 6 Scaffold Validation — Analysis Module Contracts

These tests validate the architecture and routing scaffold only. They do not test the final intelligence or quality of the future analysis algorithms.

1. **Status honesty:** `Create Sheet` is marked scaffolded, not fully implemented. The router must not claim the Analysis Sheet generator is production-ready.
2. **Concept module boundary:** project type, concept core, narrative gravity, narrative weight, scope, and priority responsibilities map to Concept Analysis.
3. **Reference routing:** images route to Image Analysis; fragmented notes route to Context Reconstruction; RP logs route to RP Log Analysis.
4. **Observed versus inferred:** Image Analysis depends on the shared Evidence and Inference system and does not present visual interpretation as established fact.
5. **Tag-driven reference use:** Reference Analysis routes through the shared Tag system and applicable individual tag files rather than re-defining tags.
6. **Character boundary:** Character Analysis informs the Analysis Sheet and does not produce a final Character Sheet.
7. **World boundary:** World Analysis informs the Analysis Sheet and does not produce a final World Sheet.
8. **Adaptive analysis:** no Phase 6 module requires a fixed universal heading list; custom analysis groupings remain possible.
9. **Information preservation:** Phase 6 outputs retain meaningful findings for the shared Information Transfer system.
10. **Bedrock awareness:** analysis modules preserve explicit project invariants and do not silently promote uncertain guesses into Bedrocks.
11. **Project separation:** context and logs from one project are not imported into another active project.
12. **No invented procedure:** scaffold files are not treated as a complete algorithm where the detailed operating method is explicitly pending.

## Completion gate for Phase 6 full implementation

Phase 6 should be marked fully implemented only when each module has:

- a complete step-by-step procedure;
- operational decision and conflict rules;
- input/output examples;
- edge cases and exclusions;
- a practical completion checklist;
- tested integration with the shared foundation systems.
