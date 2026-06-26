# KINGMAKER — MAP & PANEL FORMATS
## KM_Commands_Maps.md | Part of: KM_Commands.md system
## PAIR-LOAD WITH KM_Commands_Maps.md (relationship/companion/recap/build panels)

> **DM:** Load this file alongside KM_Commands.md, KM_Commands.md, and KM_Commands_Maps.md.
> This file contains all ASCII map formats and main info panel formats.

---

### `.map` — All Map Output (combat / scene / world)

⛔ **ONE map system. There is NO map format in this file.** Every map — combat
grids, indoor scenes, the world hex map, every encounter size — is drawn from the
single universal template set in **`KM_Map.md`**:

  - Combat / single room / corridor → `KM_Map.md` § TEMPLATE 1 (+ SCENE-SHAPE RULE for size)
  - Multi-room building / dungeon    → `KM_Map.md` § TEMPLATE 2
  - Overland / hex                   → `KM_Map.md` § TEMPLATE 3

**Rules (all enforced in `KM_Map.md` § TEMPLATE 1 — authoritative; do not restate a
different version here):**
- No UTF-8 BOX-DRAWING borders (`║ ═ ╔ █ ─ ·`) and no `+---+` frames — the code fence
  is the frame. ⛔ EXCEPTION: the block-shade glyphs `▓ ▒ ░` ARE allowed as OUTDOOR
  TERRAIN on wilderness maps (forest/woods/road), never indoors and never as furniture
  (interior furniture = `*`). Interiors are pure ASCII.
- Tight grid: **1 char + 1 SPACE** per cell (not 4 spaces); header letters aligned;
  row numbers right-aligned. **HARD WIDTH CAP = 26 columns (A–Z)**; rows may run longer.
  Prefer a FLOOR SECTION (room + corridor + adjacent rooms, `?` fog) over a lone room.
- Enemies = digits `1`–`9`; companions = their fixed single letter; `C` = rescue. No
  2-char tokens. Furniture = `*` (named in KEY), never a letter.

Do NOT draw a map from memory. Do NOT invent a width or box style here. Copy the
`KM_Map.md` template, size it, fill in symbols. Anything else = `.fail 14`.

**MAP MODE / ARTIFACT COMMANDS (full spec in KM_ClaudeInstructions.md § MAPS):**
- **`.art`** (aliases `.mapart`, `.map art`) — render the emoji ARTIFACT this turn (KM_Map_Artifact.md),
  a one-off, regardless of mode. Output a RENDERED artifact, NEVER pasted HTML text (`.fail 14`).
- **`.maptoggle`** (alias `.mapmode`) — flip `story_flags.map_primary` between `ascii` (default) and
  `artifact`, persist it, confirm in one line. `ascii` = the automatic every-turn map is the ASCII grid
  (always renders); `artifact` = the automatic map is the emoji artifact (for testing it as primary,
  e.g. on Claude Code). Default is `ascii`.

> The old `.map combat` / `.map` / `.map world` blocks (UTF-8 box-drawing borders,
> a fixed 80-char width rule, and an old-cast symbol key) were REMOVED 2026-06-21 —
> they contradicted `KM_Map.md`'s universal ASCII template and were the source of
> the DM fabricating its own grids.

---

### `.time` / `.calendar` — Time Panel

```
╔══════════════════════════════════════════╗
║  TIME & CALENDAR                         ║
╠══════════════════════════════════════════╣
║  Date: [Month] [Day], [Year]             ║
║  Season: [X]  Time: [Dawn/Morning/etc]   ║
╠══════════════════════════════════════════╣
║  Chapter 1 Time Limit                    ║
║  Started: 16 Gozran 4710 AR              ║
║  Deadline: [Date] (90 days)              ║
║  Days Used: [X]/90  Remaining: [X]       ║
║  Progress [████░░░░░░░░░░░░░░░░░░░] [X]%║
╠══════════════════════════════════════════╣
║  Travel Log                              ║
║  Hexes: [X]  Camps: [X]  Town Days: [X] ║
╚══════════════════════════════════════════╝
```

---

### `.quests` — Quest Panel

```
╔══════════════════════════════════════════════════════╗
║  QUEST LOG                                           ║
╠══════════════════════════════════════════════════════╣
║  ► MAIN QUEST                                        ║
║  Stolen Land                                         ║
║  Objective: Defeat the Stag Lord                     ║
║  Progress : [Explore] → [Find Stag Lord] → [Defeat]  ║
║  Time Left: [X] days                                 ║
╠══════════════════════════════════════════════════════╣
║  ► ACTIVE SIDE QUESTS                                ║
║  [Quest Name]                                        ║
║    Giver    : [NPC name]                             ║
║    Objective: [Current step]                         ║
║    Reward   : [Known reward or ?]                    ║
╠══════════════════════════════════════════════════════╣
║  ► COMPLETED                                         ║
║  [✓] The First Step — Charter granted by Jamandi     ║
╚══════════════════════════════════════════════════════╝
```

---

### `.npc [name]` — NPC Profile Panel

```
╔═══════════════════════════════════════════════════╗
║  NPC PROFILE — [Full Name]                        ║
╠═══════════════════════════════════════════════════╣
║  Role: [Title]  Location: [Where]  Status: [X]    ║
╠═══════════════════════════════════════════════════╣
║  RELATIONSHIP                                     ║
║  Attitude: [Hostile/Unfriendly/Indifferent/       ║
║             Friendly/Helpful]                     ║
║  Score: [−2 to +2]  Trend: [Improving/Stable/     ║
║                              Declining]           ║
╠═══════════════════════════════════════════════════╣
║  KNOWN INFORMATION                                ║
║  [Bullet list of what player has learned]         ║
╠═══════════════════════════════════════════════════╣
║  INTERACTION HISTORY                              ║
║  [Last 3 meaningful interactions]                 ║
╠═══════════════════════════════════════════════════╣
║  ACTIVE FLAGS                                     ║
║  [Promises, debts, flags related to NPC]          ║
╚═══════════════════════════════════════════════════╝
```

---

### `.kingdom` — Kingdom Status Panel (Ch1+)

```
╔═══════════════════════════════════════════════════╗
║  KINGDOM: [Name]  Size: [X] hexes  Turn: [X]     ║
╠═══════════════════════════════════════════════════╣
║  Culture  [████████░░] [X]/20                     ║
║  Economy  [██████░░░░] [X]/20                     ║
║  Loyalty  [███████░░░] [X]/20                     ║
║  Stability[█████████░] [X]/20                     ║
║  Unrest   [░░░░░░░░░░] [X] (0=Stable,20=Revolt)  ║
║  Fame [X]  Infamy [X]                             ║
╠═══════════════════════════════════════════════════╣
║  Treasury: [X] RP  Food: [X] Consumption/mo      ║
║  Armies: [X] units [list names]                   ║
╠═══════════════════════════════════════════════════╣
║  LEADERSHIP                                       ║
║  Ruler: [Name]  Councilor: [Name]                 ║
║  General: [Name]  Treasurer: [Name]               ║
║  Warden: [Name]  Spymaster: [Name]  [+6 more]    ║
╠═══════════════════════════════════════════════════╣
║  SETTLEMENTS                                      ║
║  [Name] Size:[X] Pop:[X] Buildings:[X] Def:[X]    ║
╚═══════════════════════════════════════════════════╝
```

---

### `.xp` — XP and Level Panel

> **DM:** XP is auto-tracked inline after every trigger (see KM_DMRules.md — XP Award System). This panel always reflects the current running total. Never show stale or estimated XP.

```
╔═══════════════════════════════════════════╗
║  EXPERIENCE                               ║
╠═══════════════════════════════════════════╣
║  Level: [X]  XP: [X]/[Next]              ║
║  Progress: [████████░░░░░░░░░░░░] [X]%   ║
╠═══════════════════════════════════════════╣
║  XP THIS SESSION                          ║
║  [Source] +[X] XP                         ║
║  Session Total: +[X] XP                   ║
╠═══════════════════════════════════════════╣
║  COMPANION LEVELS                         ║
║  [Companion]: Level [X] XP [X]/[next]     ║
╚═══════════════════════════════════════════╝
```

---

### `.conditions` — Conditions Panel

```
╔══════════════════════════════════════════════════════╗
║  ACTIVE CONDITIONS                                   ║
╠══════════════════════════════════════════════════════╣
║  [YOU]                                               ║
║  Frightened 2  → −2 to all checks/DCs               ║
║                   Reduces by 1 at end of each turn   ║
╠══════════════════════════════════════════════════════╣
║  AMIRI                                               ║
║  Raging        → +2 dmg, +6 TempHP, −1 AC           ║
║                   Ends if no Strike this turn        ║
╠══════════════════════════════════════════════════════╣
║  [Enemy E1]                                          ║
║  Grabbed       → Immobilized + Off-Guard             ║
║                   Escape DC [X] to break free        ║
║  Off-Guard     → −2 AC, enables Sneak Attack         ║
╠══════════════════════════════════════════════════════╣
║  NONE: Linzi, Valerie                                ║
╚══════════════════════════════════════════════════════╝
```

---

### Action Economy Counter — Real-Time Display

**DM RULE:** After every action the player spends during their turn, output this counter inline before describing the result. Update it in real time — never show a stale count.

```
ERMAC'S TURN — Action Economy
Actions: [●●●] (3/3) | Movement: [━━━━━] 25 ft | Reaction: ◆ available

[After Stride:]  Actions: [●●○] (2/3) | Movement: [━━░░░] 15 ft | Reaction: ◆
[After Strike:]  Actions: [●○○] (1/3) | Movement: [━━░░░] 15 ft | Reaction: ◆
[After Strike:]  Actions: [○○○] (0/3) | Movement: [━━░░░] 15 ft | Reaction: ◆
→ Turn complete. Type CONTINUE for next combatant.
```

**Movement menu must label action cost and terrain:**
```
MOVEMENT OPTIONS (Speed: 25 ft | Actions remaining: 2):
  1. Stride to (7,3) — 15 ft clear  [1 Action | 10 ft left]
  2. Stride to (5,5) — mud ▓        [1 Action | 20 ft DIFFICULT]
  3. Step to adjacent               [1 Action | no AoO]
  ⚠ Path to (9,1) BLOCKED — impassable.
```

---

### Cover Analysis Block — `.cover`

**DM RULE:** Show at start of each round or on `.cover` command.

```
╔══════════════════════════════════════════════════════╗
║  COVER ANALYSIS — Round [X]                          ║
╠══════════════════════════════════════════════════════╣
║  YOUR COVER                                          ║
║  From E1: NONE (open ground)                         ║
║  From E2: ½ cover (+2 AC/Ref) — tree at (3,2)        ║
╠══════════════════════════════════════════════════════╣
║  ENEMY COVER                                         ║
║  E1: NONE  |  E2: ½ cover (+2 AC) — wall at (8,0)    ║
╠══════════════════════════════════════════════════════╣
║  FLANKING                                            ║
║  E1 FLANKED by you + Amiri → Off-Guard (−2 AC) ✓    ║
║  E2 NOT flanked                                      ║
╠══════════════════════════════════════════════════════╣
║  LINE OF SIGHT                                       ║
║  E2 → you: YES  |  You → E2: YES                     ║
╚══════════════════════════════════════════════════════╝
```

Cover values: Lesser +1 | Standard +2 | Greater +4 | Take Cover action: 1A for standard.

---

### Condition Duration — Inline Format Rule

**DM RULE:** Conditions must always show duration and effect. Never display just the condition name.

```
CORRECT:
  Frightened 2  (−1/round at end of turn | now: −2 all checks/DCs)
  Grabbed       (Escape DC 16 | Immobilized + Off-Guard)
  Sickened 1    (Fort DC 14 as 1A to remove | −1 all checks/saves)
  Slowed 1      (1 round | lose 1 action next turn)
  Raging        (until no Strike this turn | +2 dmg, −1 AC, +TempHP)
  Dying 1       (Recovery check DC 11 or worsen)

WRONG: Frightened 2 ✗  Grabbed ✗  Sickened ✗ — never use name alone
```

In `.hp` quick panel, conditions append after HP bar on the same line:
```
[YOU]  [████████░░░░]  18/24  ○○● | Frightened 1 (−1/rnd, −1 checks)
Amiri  [████████████]  24/24  ○○○ | Raging (active, −1 AC +2 dmg)
E1     [░░░░░░░░░░░░]   0/22  ✕   | Dying 1 (recovery DC 11)
```

---

> **
➡
️
 Relationship, companion sheet, recap, and build panels 
→
 see `KM_Commands_Maps.md`**


---

<!-- merged from KM_Commands_Maps.md (v93.21 file consolidation) -->

# KINGMAKER — MAP & PANEL FORMATS (Part 2)
## KM_Commands_Maps.md | Relationship / Companion / Recap / Build Panels
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

> **DM:** Pull from KM_BuildGuide.md and KM_Builds.md → per-class sub-files (KM_Builds_*.md) for the player's build. `.build next` = next level only. `.build` = current +3 future levels + major unlocks to L20.

*KM_Commands_Maps.md — Kingmaker PF2e Text Adventure | Panel Formats (Part 2) v1.0*
