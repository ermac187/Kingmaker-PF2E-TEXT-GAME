# KINGMAKER — MAP & PANEL FORMATS
## KM_Commands_Maps.md | Part of: KM_Commands.md system
## PAIR-LOAD WITH KM_Commands_Maps_B.md (relationship/companion/recap/build panels)

> **DM:** Load this file alongside KM_Commands.md, KM_Commands_P2.md, and KM_Commands_Maps_B.md.
> This file contains all ASCII map formats and main info panel formats.

---

### `.map combat` — Combat Tactical Grid

**⚠️ MAP WIDTH RULE — MANDATORY:**
All maps must use **maximum width — target 80+ characters wide.** Never draw narrow maps. This applies to combat, scene, and world maps.

**DM rules for ASCII combat maps:**
- Draw at start of every combat encounter; update on any move, door, terrain change, or `.map combat`
- Grid squares = 5 feet each — draw each cell as 4 characters wide
- Use column headers (A B C D...) and row numbers (1 2 3...) on every combat map
- Show every creature, wall, cover, hazard; show range rings when relevant
- Label must match combatant list below the map
- Grid minimum 10 columns × 8 rows; scale up for larger rooms

**Symbol key:**
```
@  = Player character (you)
A  = Amiri       L = Linzi      V = Valerie
H  = Harrim      J = Jaethal    N = Nok-Nok
E1 E2 E3 ...     = Enemies (numbered by initiative order)
T  = Tartuccio (when present)
█  = Solid wall / impassable
▓  = Difficult terrain (costs 2 movement)
░  = Rubble / light difficult terrain (costs 2 movement first time)
─  ─  = Low wall / half cover (+2 AC)
═  ═  = Full wall cover
|  = Door (closed)
/  = Door (open)
≈  = Water / liquid
^  = Elevated terrain
⁎  = Hazard / trap location
★  = Objective / quest item
+  = Ally (non-companion NPC)
?  = Unknown/hidden creature (DM shows if player spotted them)
·  = Empty floor / passable terrain
```

**Combat map example — Manor Corridor:**
```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  CORRIDOR — Manor East Wing                                  Each square = 5 ft ║
║  Round: 1  |  Initiative: E2 → You → Tartuccio → E1                            ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║       A    B    C    D    E    F    G    H    I    J    K    L    M    N         ║
║  1    █    █    █    █    █    █    █    █    █    █    █    █    █    █         ║
║  2    █    ·    ·    ·    ·    ·    ·    ·    ·    ·    ·    ·    ·    █         ║
║  3    █    ·    T    ·    ·    ░    ░    ·    ·    ·    ·    E2   ·    █         ║
║  4    █    ·    ·    ·    ·    ·    ·    ·    ─    ─    ─    ·    ·    █         ║
║  5    █    ·    @    ·    ·    ·    ·    ·    ·    ·    ·    ·    ·    █         ║
║  6    █    ·    ·    ·    ·    ·    ·    E1   ·    ·    ·    ·    ·    █         ║
║  7    █    ·    ·    ·    ·    ▓    ▓    ▓    ·    ·    ·    ·    ·    █         ║
║  8    █    █    █    █    |    █    █    █    █    █    █    |    █    █         ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  ID   Name          HP       AC   Status              Distance from @           ║
║  @    [You]         18/24    19   —                   —                          ║
║  T    Tartuccio     16/16    17   —                   Adjacent (B3, 5 ft)        ║
║  E1   Assassin      22/22    17   —                   25 ft (H6)                ║
║  E2   Archer        14/14    14   ½ Cover (+2 AC)     45 ft (L3) behind wall    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  TERRAIN: ░=Rubble (difficult)  ▓=Mud (difficult)  ─=Low wall (½ cover)        ║
║  DOORS: D8=closed  L8=closed  |  Flank E1 with Tartuccio = Off-Guard           ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```
⛔ A narrow box with names and distances IS NOT a map. Draw the grid.

**DM: Redraw the map any time:**
- A creature moves
- A door opens or closes
- Cover changes
- Terrain is destroyed or created
- Player types `.map combat`
- Start of each round (in strict mode)

---

### `.map` — Scene Map (Exploration)

**For indoor locations (rooms, dungeons):**
```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  JAMANDI'S MANOR — Ground Floor                                  [@] = You      ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║                                                                                 ║
║  ┌───────────────────┐       ┌───────────────────┐       ┌──────────────────┐   ║
║  │     LIBRARY       │       │     ARMORY         │       │  SERVANTS'       │   ║
║  │     [cleared]     │───────│     [looted]  ★    │───────│  QUARTERS        │   ║
║  │  Bookshelves,desk │       │  Weapon racks      │       │  [unexplored]    │   ║
║  └─────────┬─────────┘       └─────────┬──────────┘       └────────┬─────────┘  ║
║            │                           │                           │             ║
║  ┌─────────┴───────────────────────────┴───────────────────────────┴──────────┐  ║
║  │                           MAIN CORRIDOR                                    │  ║
║  │     ⁎              ⁎              ⁎        [3 traps — Perception DC 14]    │  ║
║  └─────────┬──────────────────────────────────────────────┬──────────────────┘  ║
║            │                                              │                     ║
║  ┌─────────┴─────────┐    ┌──────────────┐    ┌──────────┴──────────────────┐   ║
║  │   BANQUET HALL    │    │  WINE CELLAR │    │       COURTYARD             │   ║
║  │   [!] Active      │────│  [locked]    │    │       [@current]            │   ║
║  │  Long tables,fire │    │  DC 18 Pick  │    │    Open sky, fountain       │   ║
║  └───────────────────┘    └──────────────┘    └─────────────────────────────┘   ║
║                                                                                 ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  [@]=You  [!]=Active event  [★]=Loot  [⁎]=Trap  [cleared]=Defeated  [locked]=DC ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

---

### `.map world` — World Hex Map

```
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  THE STOLEN LANDS — Hex Map                                                     ║
║  Discovered: [X] hexes  |  Claimed: [X] hexes  |  Season: [X]  |  Day: [X]     ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║        A       B       C       D       E       F       G       H       I       J║
║  1   [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  2   [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  3   [Rst ] [ ?  ] [OTP●] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  4   [ ?  ] [ ?  ] [ ▒  ] [ ♣  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  5   [ ?  ] [ ?  ] [ ♣  ] [ ♣  ] [Slc ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  6   [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  7   [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  8   [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  9   [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
║  10  [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ] [ ?  ]    ║
╠═══════════════════════════════════════════════════════════════════════════════════╣
║  [@]=You  [?]=Undiscovered  ●=Controlled  ○=Discovered  Rst=Restov             ║
║  OTP=Oleg's Trading Post  Slc=Sootscale  [▒]=Hills  [♣]=Forest  [∿]=River     ║
║  [.]=Plains  [█]=Mountain  [≈]=Swamp  [★]=Settlement  [■]=Claimed  [+]=Road   ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
```

> **DM:** Update the world map every time the player enters a new hex. Replace `?` with terrain symbol + status. Add location abbreviation if named. Each hex cell is 7 characters wide. Example: `[ ♣○ ]` or `[ToE✦]`.

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
 see `KM_Commands_Maps_B.md`**
