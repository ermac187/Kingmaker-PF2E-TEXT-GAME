# KINGMAKER — REARGUARD & QUEST MANAGER SYSTEM
## KM_Rearguard.md | Referenced by: KM_Commands_P3.md, KM_Ch1.md

> **DM:** This file defines Kesten Garess's role as Quest Manager, the rearguard
> scouting system, and companion quest delegation. Load this file when:
> — Player types `.quests`, `.scout`, `.delegate`, or `.rearguard`
> — Kesten Garess is in the party's current location
> — A ??? area is mentioned or scouted
>
> **Also load:** `KM_MissionResolution.md` when resolving any scout or delegate mission return.
> That file handles skill pools, DCs, outcome tiers, injuries, gear loss, and mission costs.
> The class-based Delegation Skill Table and ★/★★/★★★ scout ratings below are superseded by it.

---

## 🗂️ KESTEN GARESS — QUEST MANAGER

**Arrives:** After Happs Bydon raid is repelled at Oleg's Trading Post.
**Role:** Intelligence officer and quest clearinghouse for the expedition.

**Flavor:** Kesten is a disgraced Brevic noble running a mercenary squad to rebuild his
name. He has the organizational mind of a soldier and the contacts of someone who used to
be somebody. He collects bounties from Restov, rumors from travelers, and reports from his
own scouts. Every quest that exists in the region passes through him eventually. He does
not post things on boards. He briefs you in person.

**What he tracks:**
- All available quests at the current chapter's active locations
- Bounties from Restov and the Swordlords
- ??? areas: locations rumored to exist but not yet explored by the party
- Rearguard status: who is away and what they are doing

---

## 📋 `.quests` — KESTEN'S BOARD

> **DM:** When player types `.quests`, output this panel. Pull active quests from
> `quests_active` and `story_flags`. Filter out completed quests. ??? entries come
> from `unknown_areas` in the save block. Rearguard entries come from `rearguard_active`.

```
╔═════════════════════════════════════════════════════════════╗
║  KESTEN'S BOARD — [CURRENT LOCATION]           [DATE/DAY]  ║
╠═════════════════════════════════════════════════════════════╣
║  QUESTS AVAILABLE                                           ║
╠═════════════════════════════════════════════════════════════╣
║  ▸ [Quest Name]              [DELEGATE OK] or [PARTY REQD] ║
║    Source: [NPC]  |  Reward: [reward]                       ║
║    Note:   [one-line summary]                               ║
╠═════════════════════════════════════════════════════════════╣
║  ▸ [Next quest...]                                          ║
╠═════════════════════════════════════════════════════════════╣
║  UNKNOWN AREAS                              [X] unscanned   ║
╠═════════════════════════════════════════════════════════════╣
║  ??? [Area hint]           ~[X] days travel  [INTEL: NONE] ║
║    Rumor: [one-line hint Kesten has heard]                   ║
║    → .scout [area] to send rearguard                        ║
╠═════════════════════════════════════════════════════════════╣
║  ??? [Area hint, partially scouted]          [INTEL: BASIC] ║
║    [One-line intel summary from prior scout]                 ║
║    → .scout [area] for full intel or enter yourself         ║
╠═════════════════════════════════════════════════════════════╣
║  REARGUARD AWAY                                             ║
╠═════════════════════════════════════════════════════════════╣
║  [Companion] → [Mission] — returns Day [X]                  ║
╚═════════════════════════════════════════════════════════════╝
```

**Delegation tag rules:**
- `[DELEGATE OK]` — gathering, delivery, simple patrol, weak beast clearance
- `[PARTY REQUIRED]` — named enemy, narrative-critical, dungeon, boss, companion quest

**DM rules:**
- Do NOT show quests in `quests_completed`
- Do NOT invent quests not in the location file or companion files
- ??? entries: only show if an `unknown_areas` entry exists in save block
- Rearguard section: only show if `rearguard_active` is non-empty

---

## ❓ ??? UNKNOWN AREAS SYSTEM

**What creates a ??? entry:**

| Trigger | ??? Added |
|---------|-----------|
| Happs Bydon surrenders | Thorn River camp (Kressle), Stag Lord fort |
| Merchant/traveler rumor | As narrated per chapter |
| NPC quest mention | Location of quest target if not yet visited |
| Map fragment found | Whatever the fragment indicates |
| Adjacent hex explored | Adjacent unexplored hex (general direction only) |

**??? entry in save block:**
```json
"unknown_areas": [
  {
    "id": "thorn_river_camp",
    "hint": "Bandit camp, Thorn River",
    "travel_days": 1,
    "intel_level": "none",
    "intel_summary": "",
    "source": "Happs Bydon (surrender)"
  }
]
```

**Intel levels:** `none` → `basic` → `full`
- `none` — exists on the board, no details
- `basic` — general danger level + area type (from ★ or ★★ scout)
- `full` — enemy types, count, layout, loot hint (from ★★★ scout)

---

## 🔭 `.scout [area]` — REARGUARD SCOUTING

> **DM:** When player types `.scout [area name]`, run the following procedure.

```
SCOUT PROCEDURE:
  1. Confirm the area exists in unknown_areas (not yet visited).
  2. Display the COMPANION SELECTION PANEL (below).
  3. Player picks 1–2 companions to send.
     — Companions must be currently in the party (not already on rearguard).
  4. Calculate travel time: unknown_area.travel_days × 2 + 1 day observation.
  5. Add entry to rearguard_active in save block.
  6. Mark those companions AWAY (unavailable for combat).
  7. Advance the day counter when the player rests/travels (normal time flow).
  8. When return day arrives, fire the INTEL REPORT (see format below).
```

**Companion selection panel:**
```
══════════════════════════════════════════════
SCOUT MISSION — [AREA HINT]
Estimated time: [X] days round trip
Select 1–2 companions to send.
Available:
  [list companions in party who are not AWAY]
  [show scout rating next to each name]
══════════════════════════════════════════════
```

**Scout ratings:** *(superseded — use Perception modifier pool in KM_MissionResolution.md)*

**Risk of encounter:** Handled by the outcome tier roll in KM_MissionResolution.md.
Failure or Critical Failure = something went wrong. Success+ = clean mission.

---

## 📡 INTEL REPORT FORMAT

> **DM:** When scouts return, deliver this panel in Kesten's voice plus a brief
> quote from the returning companion.

```
╔═════════════════════════════════════════════════════════════╗
║  SCOUT REPORT — [AREA NAME]                    [RETURN DAY] ║
╠═════════════════════════════════════════════════════════════╣
║  Scouts: [Companion names]     Intel level: [BASIC / FULL] ║
╠═════════════════════════════════════════════════════════════╣
║  AREA TYPE    [terrain: forest / ruins / camp / cave etc.]  ║
║  DANGER       [LOW / MODERATE / HIGH / EXTREME]             ║
║  ENEMIES      [types and rough count — FULL only]           ║
║  LAYOUT       [one-line summary — FULL only]                ║
║  LOOT HINT    [general: "gold and gear" / "magical item"…]  ║
║  HAZARDS      [traps, environmental — FULL only if known]   ║
╠═════════════════════════════════════════════════════════════╣
║  "[Returning companion's one-line report in their voice]"   ║
╠═════════════════════════════════════════════════════════════╣
║  → Area upgraded from ??? to [NAME] on Kesten's board       ║
║  → .quests to see updated board                             ║
╚═════════════════════════════════════════════════════════════╝
```

**BASIC intel (★ and solo ★★ scouts):**
Fill: Area Type, Danger. Leave ENEMIES/LAYOUT/HAZARDS as `[NOT OBSERVED]`.

**FULL intel (★★★ or paired ★★ scouts):**
Fill all fields. Enemies = general type + rough count ("~8 bandits, 1 leader-type").
Do NOT give exact stat blocks — that's for when the party arrives.

**Save block update after report:**
```json
"unknown_areas": update intel_level and intel_summary for this area
```

---

## ⚔️ `.delegate [quest]` — REARGUARD QUEST DELEGATION

> **DM:** When player types `.delegate [quest name]`, run the following procedure.

```
DELEGATE PROCEDURE:
  1. Confirm quest is marked [DELEGATE OK] on Kesten's board.
     — If [PARTY REQUIRED]: refuse with reason. Do NOT allow override.
  2. Display the COMPANION SELECTION PANEL for delegation.
  3. Player picks 1–3 companions.
  4. DM checks: does this group have the right skill rating for this quest type?
     — See DELEGATION SKILL TABLE below.
  5. Calculate completion time (see QUEST TIME TABLE below).
  6. Add entry to rearguard_active.
  7. Mark companions AWAY.
  8. On return: fire QUEST RETURN REPORT.
```

**Delegation skill table:** *(superseded — use KM_MissionResolution.md)*

**Quest time table:**

| Quest Type | Days |
|------------|------|
| Gather (local, < 1 day travel) | 1–2 |
| Gather (distant, 1–2 days travel) | 2–4 |
| Deliver (local) | 1 |
| Deliver (distant) | 2–3 |
| Patrol / beast hunt | 2–5 |

**XP split on successful delegation:**
- Rearguard companions: 50% of base quest XP (divided among them)
- Player character: 25% of base quest XP
- 25% lost (not there personally)

**Non-delegatable quests (always [PARTY REQUIRED]):**
- Any quest with a named enemy (Stag Lord, Kressle, Tartuk, Tuskgutter, etc.)
- Any companion's personal quest chain
- Any quest with narrative choices or dialogue outcomes
- Any dungeon with more than one room
- Any quest where the reward depends on player decisions

---

## 📦 QUEST RETURN REPORT FORMAT

> **DM:** When rearguard returns from a completed delegation, deliver in Kesten's voice.

```
╔═════════════════════════════════════════════════════════════╗
║  MISSION COMPLETE — [QUEST NAME]               [RETURN DAY] ║
╠═════════════════════════════════════════════════════════════╣
║  Sent: [Companion names]                                    ║
╠═════════════════════════════════════════════════════════════╣
║  OUTCOME:   [SUCCESS / PARTIAL / FAILURE]                   ║
║  REWARD:    [Items / gold / service — as defined by quest]  ║
║  XP:        [Amount — Player: X | Rearguard: Y each]        ║
╠═════════════════════════════════════════════════════════════╣
║  "[Returning companion's one-line report in their voice]"   ║
╠═════════════════════════════════════════════════════════════╣
║  → Quest marked complete. Turn in to: [NPC name if needed]  ║
╚═════════════════════════════════════════════════════════════╝
```

**Turn-in rule:** Some rewards require the player to speak to the quest-giver in person
(e.g., Bokken's potion discount activates when player visits him). Kesten notes this.

---

## 📊 `.rearguard` — STATUS PANEL

> **DM:** When player types `.rearguard`, output this panel.
> Pull from `rearguard_active` in save block. If empty, say so in one line.

```
╔═════════════════════════════════════════════════════════════╗
║  REARGUARD STATUS                              [CURRENT DAY] ║
╠═════════════════════════════════════════════════════════════╣
║  [Companion]  →  [Mission type + target]  — Day [X] of [Y]  ║
║  [Companion]  →  [Mission type + target]  — Day [X] of [Y]  ║
╠═════════════════════════════════════════════════════════════╣
║  [X] companion(s) away.  [Y] companion(s) available.        ║
╚═════════════════════════════════════════════════════════════╝
```

**Save block format for rearguard_active:**
```json
"rearguard_active": [
  {
    "companion": "Ekundayo",
    "mission_type": "scout",
    "target": "thorn_river_camp",
    "depart_day": 4,
    "return_day": 7,
    "status": "away"
  },
  {
    "companion": "Reiko",
    "mission_type": "delegate",
    "target": "Fangberries for Bokken",
    "depart_day": 4,
    "return_day": 6,
    "status": "away"
  }
]
```

---

## ⏱️ TIME TRACKING RULES

- Day counter lives in save block: `current_day` (Day 1 = first morning at Oleg's)
- Day advances when: the party rests overnight, travels between locations, or explicitly camps
- Rearguard return day is fixed at departure: `depart_day + travel_time`
- **DM:** At the start of each new day, check `rearguard_active` for any entry where
  `return_day ≤ current_day`. If found, fire the appropriate report (intel or quest return).
- Multiple rearguard missions run simultaneously — they do not block each other
- A companion cannot be sent on a new mission until their current one completes
- The player can always ask `.rearguard` to check status mid-session

---

## ⛔ REARGUARD RULES

- **Companions marked AWAY cannot join combat.** If an encounter triggers while they
  are away, they are simply not present. Do not invent a reason — just note they are
  on mission. `.fail 9` if an AWAY companion participates in combat.
- **The player cannot send all companions away** — minimum 2 companions must remain
  in the active party at all times (plus the player character).
- **QL companions are available for rearguard once they join** — their QL status
  only affects when they first appear, not rearguard eligibility afterward.
- **If a rearguard companion would be needed for a companion quest trigger:** delay
  the trigger until they return. Do not fire companion quests while the companion is away.

---

*KM_Rearguard.md — Kingmaker PF2e Text Adventure | Rearguard & Quest Manager v1.0*
*Commands: .quests | .scout [area] | .delegate [quest] | .rearguard*
