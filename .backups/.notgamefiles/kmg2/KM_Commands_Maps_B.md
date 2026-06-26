# KINGMAKER — MAP & PANEL FORMATS (Part 2)
## KM_Commands_Maps_B.md | Relationship / Companion / Recap / Build Panels
## PAIR-LOAD WITH KM_Commands_Maps.md

> **DM:** Load alongside KM_Commands_Maps.md. This file contains the companion
> relationship panel, full companion sheet, session recap panel, and build
> progression panel formats.

---

### `.relationship` — Companion Relationship Panel

```
╔═══════════════════════════════════════════════════╗
║  COMPANION RELATIONSHIPS                          ║
╠═══════════════════════════════════════════════════╣
║  [Name]  [Hostile──Strained──Neutral──Friendly──Devoted]
║          Score: [−2/−1/0/+1/+2]  Quest: [status] ║
╠═══════════════════════════════════════════════════╣
║  Amiri   ●●●●○ Friendly (+1)  Quest: incomplete  ║
║  Linzi   ●●●●● Devoted  (+2)  Quest: complete    ║
║  Valerie ●●●○○ Neutral  (0)   Quest: inactive    ║
║  ...                                              ║
╠═══════════════════════════════════════════════════╣
║  Next threshold: [Name] needs [X] to reach [lvl] ║
║  At risk: [Name] at [level] — [reason]            ║
╚═══════════════════════════════════════════════════╝
```

---

### `.companion [name]` — Full Companion Sheet

```
╔═══════════════════════════════════════════════════╗
║  [NAME] — [Class] Level [X]                       ║
╠═══════════════════════════════════════════════════╣
║  HP [bar] [X]/[X]  AC [X]  Speed [X]ft            ║
║  Fort +[X]  Ref +[X]  Will +[X]  Init +[X]        ║
║  STR [X] DEX [X] CON [X] INT [X] WIS [X] CHA [X] ║
╠═══════════════════════════════════════════════════╣
║  ATTACKS                                          ║
║  [Weapon]: d20+[X] ([dice]+[X] [type]) MAP −5/−10║
╠═══════════════════════════════════════════════════╣
║  SKILLS (Trained+)                                ║
║  [Skill] +[X]  [Skill] +[X]  [Skill] +[X]        ║
╠═══════════════════════════════════════════════════╣
║  KEY FEATS: [Feat — one line each]                ║
║  EQUIPPED: [Item — effect]                        ║
╠═══════════════════════════════════════════════════╣
║  Relationship: [score/level]  Quest: [status]     ║
║  Thread: "[current thread in their voice]"        ║
╚═══════════════════════════════════════════════════╝
```

---

### `.recap` — Session/Chapter Summary Panel

```
╔══════════════════════════════════════════════════════╗
║  PREVIOUSLY ON KINGMAKER...                          ║
╠══════════════════════════════════════════════════════╣
║  [2–4 sentence narrative recap in DM voice,          ║
║   covering the most dramatic/consequential events.   ║
║   Written as story, not bullet points.]              ║
╠══════════════════════════════════════════════════════╣
║  KEY DECISIONS MADE                                  ║
║  ▸ [Decision — consequence]                          ║
║  ▸ [Decision — consequence]                          ║
╠══════════════════════════════════════════════════════╣
║  WHERE YOU ARE NOW                                   ║
║  Location : [current hex/scene]                      ║
║  Date     : [in-game date]                           ║
║  Active   : [quests + time limits if any]            ║
╚══════════════════════════════════════════════════════╝
```

> **DM:** Reconstruct recap from save block flags, quest_log, npc_threads, world_state. Write narrative as a GM opening a session — present tense, specific, dramatic. Translate flags to story, don't list them.

---

### `.build` — Class Progression Panel

```
╔══════════════════════════════════════════════════════╗
║  BUILD [#] — [Class] PROGRESSION                     ║
╠══════════════════════════════════════════════════════╣
║  CURRENT LEVEL [X]                                   ║
║  ▸ [Feature you have — one line]                     ║
║  ▸ [Feature you have — one line]                     ║
╠══════════════════════════════════════════════════════╣
║  LEVEL [X+1] — [X XP needed]                         ║
║  ▸ [Feature you gain]                                ║
║  ▸ [Feat slot — choose from: X, Y, Z]                ║
╠══════════════════════════════════════════════════════╣
║  LEVEL [X+2]                                         ║
║  ▸ [Feature you gain]                                ║
╠══════════════════════════════════════════════════════╣
║  MAJOR UNLOCKS AHEAD                                 ║
║  L[X]: [Significant ability name — brief description]║
║  L[X]: [Significant ability name — brief description]║
╚══════════════════════════════════════════════════════╝
```

> **DM:** Pull from KM_Leveling.md and KM_Builds.md → sub-files (KM_Builds_A–M.md) for the player's build. `.build next` = next level only. `.build` = current +3 future levels + major unlocks to L20.

*KM_Commands_Maps_B.md — Kingmaker PF2e Text Adventure | Panel Formats (Part 2) v1.0*
