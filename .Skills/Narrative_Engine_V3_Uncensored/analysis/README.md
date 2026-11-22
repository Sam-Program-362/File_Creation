# Phase 6 — Analysis Subsystem

**Status:** Operational AI-skill procedures implemented in this stage.  
**Purpose:** Convert supplied project material into a faithful, inspectable Analysis Sheet that can be approved before creation.

Phase 6 is a coordinated analysis system, not a single template. The Analysis Sheet is its user-facing synthesis. The specialist modules perform distinct work and return structured findings to the coordinator.

## Module map

| Module | Responsibility | Invoke when |
|---|---|---|
| `analysis-sheet/SKILL.md` | Orchestrates the analysis and writes the Analysis Sheet | New concept / `Create Sheet` |
| `concept-analysis/SKILL.md` | Understands concept, type, scope, appeal, gravity and narrative structure | Every substantive analysis |
| `reference-analysis/SKILL.md` | Selects and coordinates source-specific analysis | Images, references, fragmented notes or RP logs are supplied |
| `reference-analysis/image-analysis.md` | Extracts visual evidence and bounded interpretations | One or more images are supplied |
| `reference-analysis/context-reconstruction.md` | Reconstructs scattered or incomplete material | Notes or context are fragmented, inconsistent or disordered |
| `reference-analysis/rp-log-analysis.md` | Extracts project-relevant information from roleplay transcripts | RP logs or interaction excerpts are supplied |
| `character-analysis/SKILL.md` | Analyzes character traits, psychology, behavior and relationships | Characters or interactions matter to the project |
| `world-analysis/SKILL.md` | Analyzes setting, systems, rules and world implications | A world or setting materially matters |

## Analysis execution order

1. Read `analysis-sheet/SKILL.md` as the coordinator.
2. Read `concept-analysis/SKILL.md` for every project.
3. Read `reference-analysis/SKILL.md` when there are references, images, fragmented notes or logs. Load only the relevant specialist submodules.
4. Read `character-analysis/SKILL.md` only when character or relationship analysis is needed.
5. Read `world-analysis/SKILL.md` only when a setting or world structure is materially relevant.
6. Use shared dependencies named by each skill: evidence and inference, tags, Bedrocks, adaptive sections and information transfer.
7. Synthesize all relevant findings through the Analysis Sheet coordinator. Do not expose an unnecessary module-by-module dump.

## Specialist output contract

Specialist modules return compact, clearly classified findings to the coordinator. They do not independently generate a separate user-facing document unless the user directly asks for that analysis. The coordinator decides what belongs in the Analysis Sheet and which information needs to be carried to later deliverables.

Each finding should preserve:
- the information itself;
- its source or source group;
- its information status (established, supported, inferred, proposed or unknown);
- its scope (project, character, relationship, world, plot, scenario or other relevant unit);
- any relevant tag or Bedrock association;
- any ambiguity or conflict that could change the interpretation.

## Non-goals

Phase 6 does not create Character Sheets, World Sheets, Context Sheets, Descriptions, Lorebook Plans or Scenario openings. Those are separate deliverables. Analysis may plan or identify what they will need, but must not silently generate them.

## Shared invariants

- The user's explicit information remains authoritative.
- A candidate interpretation is not silently promoted to canon.
- Explicit Bedrocks are captured and preserved; suspected Bedrocks remain candidates.
- Tags are applied at the narrowest appropriate scope.
- Adaptive sections govern the Analysis Sheet: no universal fixed list of headings.
- Approved meaningful findings must be passed through the Information Transfer system so they do not disappear during creation.
- Final creation documents must later remove analysis-only language; the Analysis Sheet itself may show evidence and interpretation.

## Completion standard

Phase 6 is complete for a project when the coordinator can explain the concept accurately, show the evidence and uncertainty that materially affect interpretation, identify the project's narrative center, capture constraints and tags, and provide an actionable generation direction without producing final assets prematurely.
