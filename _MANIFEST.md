# KINGMAKER — UPLOAD MANIFEST
_Folder organization for claude.ai Project capacity. Last reorg: 2026-06-15._

The claude.ai DM reads uploaded files **by filename** — folder location on disk does
NOT matter to it. Folders exist only so YOU can choose which set to upload and keep the
project under capacity. Upload the folders for your current phase; leave the rest off.

> ⚠️ `_MANIFEST.md`, `.backups\`, `.saves\`, `.claude\` are NOT game files — never upload them.
> The system prompt (`.backups\.notgamefiles\KM_ClaudeInstructions.md`) is pasted into the
> Project's custom-instructions box, not uploaded as a document.

---

## WHAT TO UPLOAD, BY PHASE

| Phase | Upload | ≈ % of cap |
|---|---|---|
| **Character creation / respec** | Core + PrePrologue + _parked\BuildGuides | ~88% |
| **Pre-Prologue + Prologue (the Opening)** | Core + PrePrologue + Prologue | ~75% |
| **Chapter 1 and everything after** | **Core + the one chapter folder you're in** (`Ch1/`…`Ch7/`); drop PrePrologue + Prologue forever | ~45–55% |
| **Mid-game respec** | re-add _parked\BuildGuides for that session, then drop it | — |

**Routine level-ups need NO extra upload** once a compact leveling reference lives in Core.
**Full build guides are only for creating a character or a full respec.**

---

## CHAPTER FOLDERS — Ch1/ … Ch7/ (added 2026-06-19)

Chapter narrative is split one file per chapter, each in its own folder, so you upload ONLY
the chapter you're playing:

```
Ch1/KM_Ch1.md — Stolen Land             Ch5/KM_Ch5.md — War of the River Kings
Ch2/KM_Ch2.md — Troll Trouble / Bloom   Ch6/KM_Ch6.md — Sound of a Thousand Screams
Ch3/KM_Ch3.md — Varnhold Vanishing      Ch7/KM_Ch7.md — The Final Act
Ch4/KM_Ch4.md — Twice-Born Warlord
```

Split **verbatim** (byte-identical) from the old `KM_Chapters.md` (Ch1–2) and `KM_Chapters_B.md`
(Ch3–7) bundles, which now live in `.backups\.chapters_consolidated_premerge_2026-06-19\` and are
NOT uploaded. Every cross-chapter SYSTEM (Kingdom, War, Mythic, Bestiary, Items, Loot, Map,
Quests…) still lives in **Core** — only the per-chapter narrative moved out. All in-file pointers
were repointed from `KM_Chapters*.md` to the `KM_Ch#.md` names (0 stale references remain).

---

## CORE (always uploaded — 52 files; chapter narrative moved to Ch1/…Ch7/)
Engine + rules: KM.txt, KM_B.txt, KM_P2.txt, KM_DMRules.md, KM_DMRules_B.md, KM_LoadRules.md,
KM_LoadRules_B.md, KM_SceneFiles.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md,
KM_Combat_Systems.md, KM_CombatTurn.txt, KM_Conditions_Skills.md, KM_Glossary.md, KM_FailCodes.md,
KM_SaveBlock_Template.md, KM_PlayerDialogue_Render.md, KM_PlayerHelp.md, KM_ChapterSelect.md
Companions/NPCs: KM_Companions.md, KM_CompanionIndex.md, KM_Companions_Behaviors.md,
KM_Companions_Behaviors_B.md, KM_Companions_StateVoice.md, KM_Companions_Titles.md,
KM_Companion_Bonds.md, KM_Companion_Dynamics.md, KM_CompanionVoices.md, KM_CompanionQuests.md,
KM_Backstories.md, KM_Romance.md, KM_Signatures.md, KM_NPCs.md, KM_Leliana_Ballads.md
Cross-chapter systems: KM_Kingdom.md, KM_War_Systems.md, KM_Mythic_Systems.md,
KM_World_Systems.md, KM_Game_Subsystems.md, KM_Bestiary.md, KM_Items.md, KM_Items_B.md,
KM_Loot.md, KM_Map.md, KM_Exploration.md, KM_Spells.md, KM_Documents.md,
KM_MissionResolution.md, KM_Rearguard.md, KM_SilkRoad.md, KM_Endings.md
> ⬆️ Chapter narrative (KM_Ch1.md–KM_Ch7.md) is NO LONGER in Core — see § CHAPTER FOLDERS above; upload only the current chapter's folder.

## PREPROLOGUE (Opening only — 11 files)
KM_PP_01..09, KM_PrePrologue_Setup.md, KM_CharCreate.md

## PROLOGUE (Opening only — 15 files)
KM_PR_01..09, KM_PR_03_Openers.md, KM_PR_03_feast_circuit.md, KM_PR_BRANCH_WALKOUT.md,
KM_Prologue_Systems.md, KM_Tartuccio_Strategic.md, KM_DMRules_C.md, KM_Malak_Jail.md
> During the Opening, upload PrePrologue AND Prologue together — it's one continuous act
> and KM_Malak_Jail.md is referenced from both PP_05 and the Prologue.

## _parked\BuildGuides (creation / respec only — 16 files)
KM_BuildGuide.md, KM_Builds.md, KM_Builds_*.md (13 class files), KM_Ancestries.md
