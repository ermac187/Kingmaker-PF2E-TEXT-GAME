# KINGMAKER — KINGDOM MANAGEMENT
## KM_Kingdom.md | Active from: Chapter 1 (Kingdom Founding) | Referenced by: KM_Ch1.md-KM_Ch7.md
## PAIR-LOAD WITH KM_Kingdom.md (faction reputation tracks)

---

> **DM:** Load this file from Ch1 onward. The first Kingdom Turn runs immediately after the player founds their capital. Use the hex system from KM_Map.md alongside this file. Track all kingdom state in the JSON Save Block under `kingdom{}`.
> For the complete settlement building catalogue (all 68 structures, RP costs, Commodity costs, Construction DCs, upgrade chains), search **KM_Kingdom.md** in project knowledge.

---

## 🏰 KINGDOM STATS

```
CULTURE   : Arts, education, morale. Affects spell research, artisan quality, feasts.
ECONOMY   : Trade, production, income. Affects treasury income, building costs.
LOYALTY   : Military morale, citizen happiness. Affects army quality, unrest recovery.
STABILITY : Law, order, infrastructure. Affects event resistance, expansion success.

Each stat: range 0–100. Most actions target one stat with a skill check.
Critical Success (+2), Success (+1), Failure (0), Critical Failure (−1 + Unrest)

UNREST    : 0–20. Tracks civil stability. Increases from failed checks, unpaid consumption,
            crises. Decreases from Celebrate Holiday, temples, player actions.

  Unrest 0–4   : Stable. No automatic effects.
  Unrest 5–7   : Loyalty checks at −1 per turn. Minor civil unrest.
  Unrest 8–10  : All kingdom checks at −2. Desertion possible.
  Unrest 11–14 : −2 all stats per turn. Random hex abandonment each turn.
                 Crisis event mandatory this turn (roll KM_Bestiary.md (kingdom events section)).
  Unrest 15–19 : KINGDOM IN CRISIS. See Kingdom Failure State below.
  Unrest 20    : REVOLT — immediate reckoning. See Kingdom Failure State below.
FAME      : Public reputation. Affects diplomacy and trade agreements.
INFAMY    : Notorious reputation. Affects intimidation and criminal enterprises.
```

---

## 📅 KINGDOM TURN SEQUENCE

One Kingdom Turn = approximately 1 month in-game. Run at the end of each month.

```
PHASE 1 — UPKEEP
  Step 1: Assign Leadership (if any roles empty or changed)
  Step 2: Pay Consumption (see Consumption table below)
  Step 3: Check Unrest (if Stability fails, Unrest +1)

PHASE 2 — COMMERCE
  Step 4: Collect Taxes (automatic — Economy ÷ 5 = gp earned, round down)
  Step 5: Optional commerce activities (Trade, Lifestyle, etc.)

PHASE 3 — ACTIVITIES
  Step 6: Leadership Activities (1 per filled role; Ruler gets 2)
  Step 7: Region Activities (1 at Size 1–10 | 2 at Size 11–25 | 3 at Size 26+)
  Step 8: Civic Activities (1 per settlement)
  Step 9: Army Activities (if armies exist)

PHASE 4 — EVENT
  Step 10: Roll 1d20. On 1–8, a kingdom event occurs (see Event Table)
           Some events are scripted (Ch2 trolls, Ch6 Bloom)
```

---

## 👑 LEADERSHIP ROLES

> Each role requires a character (PC or named NPC) assigned to it. Empty roles impose a −2 penalty to the associated stat per turn. Fill roles as companions and NPCs become available.

| Role | Stat | Skill Used | Best Candidates |
|------|------|-----------|----------------|
| **Ruler** | All (−2 if empty) | Varies | Player character |
| **Councilor** | Loyalty | Diplomacy or Society | Linzi, Tristian |
| **General** | Stability | Athletics or Warfare | Amiri, Kassil Aldori |
| **Grand Diplomat** | Stability | Diplomacy | Linzi, Valerie |
| **High Priest** | Stability | Religion | Harrim, Tristian, Jaethal |
| **Magister** | Culture | Arcana or Occultism | Octavia |
| **Marshal** | Economy | Survival or Scouting | Kesten Garess, Ekundayo |
| **Royal Enforcer** | Loyalty | Intimidation or Law | Regongar, Jaethal |
| **Spymaster** | Economy | Deception or Stealth | Nok-Nok, Octavia |
| **Treasurer** | Economy | Society or Crafting | Oleg (NPC) |
| **Warden** | Loyalty | Athletics or Warfare | Kesten Garess, Akiros |

**Companion Role Availability:**
- Kesten Garess → available after Prologue (arrives at Oleg's Day 3)
- Linzi → available after Prologue (if recruited)
- Oleg Leveton → available immediately (Treasurer only)
- Jhod Kavken → available after Temple of the Elk quest
- Akiros Ismort → available if turned at Thorn Ford (Warden or General)
- Others become available as chapters progress

---

## 📊 KINGDOM TURN — DETAILED MECHANICS

### Phase 1: Upkeep

**Consumption:**
```
Base consumption = 1 RP per claimed hex (CRPG canon) — NOT Size ÷ 4
Each settlement adds its Consumption value (see settlement table)
Each army unit adds its Consumption value
Food commodities can offset up to 50% of base consumption (see Commodities below)

If Treasury RP < Consumption:
  Cannot pay → Unrest +2
  Settlers begin leaving → Population −5%
  If 3 consecutive failures → Kingdom collapses (game over — soft: Jamandi intervenes)
```

**Unrest Check (Stability):**
```
Roll: d20 + Stability bonus + Leadership bonuses
DC: 15

Critical Success: Unrest −2 (minimum 0)
Success         : Unrest unchanged
Failure         : Unrest +1
Critical Failure : Unrest +2, random minor event triggers
```

### Phase 2: Commerce

**Tax Collection (automatic):**
```
Income per turn = Economy ÷ 5 gp (round down)
Example: Economy 25 → +5 gp per turn
```

**Optional Commerce Actions:**
```
Tap Treasury   : Withdraw personal gold (Economy check DC 15; fail = −1 Economy)
Trade Agreement: +2 Economy for 3 turns (Diplomacy check, requires allied faction)
Improve Lifestyle: Player gains bonuses (costs 1 RP)
```

### Phase 3A: Leadership Activities

Each filled leadership role provides **1 activity slot** per turn. The Ruler gets **2 slots** per turn.
> **Canon note:** This matches both PF2e Remaster and CRPG — 1 activity per role, Ruler is the exception at 2.

**Most Common Leadership Activities:**

| Activity | Stat | DC | Effect |
|----------|------|----|--------|
| Celebrate Holiday | Culture | 15 | Unrest −1, Loyalty +1 for 1 turn |
| Quell Unrest | Loyalty | 15 | Unrest −1d4 on success |
| Hire Adventurers | Economy | 15 | +1d4 to next Exploration or Combat check |
| Send Diplomatic Envoy | Stability | 16 | Opens trade/alliance with target faction |
| Issue Proclamation | Loyalty | varies | Declare policy — effects per proclamation |
| Provide Care | Culture | 14 | −1 Unrest, heal sick citizens |
| Recruit Army | Warfare | 16 | Raise 1 army unit (costs RP) |
| Repair Reputation | Diplomacy | 15 | −1 Infamy or +1 Fame |
| Clandestine Business | Intrigue | 16 | +2 Economy, risk of +1 Unrest on fail |
| Prognostication | Religion/Arcana | 14 | Preview next kingdom event |
| Rest and Relax | — | — | Restore 1 used activity slot next turn |

### Phase 3B: Region Activities (scales with kingdom size)

> **Canon rule (TTRPG + CRPG):** Region activity count scales with kingdom Size.
> Size 1–10: **1** Region Activity per turn | Size 11–25: **2** | Size 26+: **3**
> Track current allowance in the kingdom JSON as `region_activity_slots`.

| Activity | DC | Cost | Effect |
|----------|----|------|--------|
| Claim Hex | Stability 14 | 0 | Add a **Discovered** hex to kingdom. **Cannot claim unexplored hexes.** |
| Clear Hex | Varies (combat) | 0 | Remove threats from hex |
| Establish Settlement | Stability 16 | 4 RP | Found new settlement in claimed hex |
| Build Roads | Engineering 14 | 2 RP/hex | Connect hexes, halve travel time |
| Establish Farmland | Agriculture 13 | 1 RP | −1 Consumption per turn |
| Establish Work Site | Engineering 15 | 2 RP | +Economy per turn (mine/lumber) |
| Fortify Hex | Warfare 15 | 3 RP | +Defense to that hex |

### Phase 3C: Civic Activities (1 per settlement per turn)

| Activity | DC | Cost | Effect |
|----------|----|------|--------|
| Build Structure | Engineering 15 | Varies | Construct building (see Building Table) |
| Upgrade Structure | Engineering 16 | ½ original cost | Improve building tier |
| Repair Structure | Engineering 13 | ¼ original cost | Restore damaged building |
| Demolish Structure | — | 0 | Remove building, recover ¼ cost |

### Phase 4: Kingdom Events

**Roll d20 at end of each turn:**
- 1–8: Kingdom event triggers (roll on Event Table below, or use scripted event)
- 9–20: No event this turn

> **DM:** For random event resolution, also see `KM_Exploration.md` — the Random Event Table (d12) there applies directly to kingdom events when no scripted event overrides.

**Random Event Table (d12):**

| Roll | Event | Stat | Effect |
|------|-------|------|--------|
| 1 | Bandit Activity | Stability DC 14 | Fail: −1 Economy, random hex threatened |
| 2 | Crop Failure | Economy DC 15 | Fail: +1 Consumption this turn |
| 3 | Visiting Celebrity | Culture DC 13 | Success: +1 Culture, +1 Fame |
| 4 | Political Scandal | Loyalty DC 15 | Fail: +1 Unrest, −1 Fame |
| 5 | Monster Threat | Stability DC 14 | Fail: hex becomes Hostile until cleared |
| 6 | Trade Opportunity | Economy DC 14 | Success: +3 gp this turn |
| 7 | Natural Disaster | Stability DC 16 | Fail: random building damaged |
| 8 | Diplomatic Overture | Diplomacy DC 14 | Success: +1 ally faction relationship |
| 9 | Citizen Unrest | Loyalty DC 15 | Fail: +2 Unrest |
| 10 | Bountiful Harvest | — | +2 Economy this turn (free) |
| 11 | Religious Festival | Culture DC 13 | Success: −1 Unrest, +1 Culture |
| 12 | Military Desertion | Loyalty DC 16 | Fail: lose 1 army unit morale |

**Scripted Events (override random table):**
```
Ch2 Turn 1–3   : Troll Raids (Stability DC 16 — fail = border hex threatened)
Ch2 Turn 4+    : Season of Bloom begins (scripted, cannot be rolled away)
Ch3             : Varnhold Vanishing (scripted — Varnhold stops responding)
Ch4             : Tiger Lord Pressure (Loyalty DC 16)
Ch5             : Pitax Trade Embargo (Economy −3 until Ch5 resolved)
Ch6             : Bloom Events (escalating, scripted sequence)
```

### ⏳ EVENT EXPIRY RULE

> **DM:** Applies to **random Event Table rolls only**. Scripted events never expire — they escalate by their own rules.

**How it works:**
When a random event triggers, record it in `kingdom.pending_events[]`:
```json
{ "event": "Monster Threat", "hex": "SW-2", "fired_turn": 4, "expires_turn": 6 }
```

**Expiry window: 2 kingdom turns.** If the event is not addressed before `expires_turn`, the DM applies the **auto-resolution penalty** without a check — the worst-case outcome happens automatically.

| Event | Auto-Resolution Penalty (if expired) |
|-------|--------------------------------------|
| Bandit Activity | −2 Economy; that hex's Controlled status suspended 1 turn |
| Crop Failure | +2 Consumption next turn (stacks with current) |
| Political Scandal | +2 Unrest; −1 Loyalty |
| Monster Threat | Hex becomes Hostile; requires full Clear Hex activity to reclaim |
| Natural Disaster | Building damaged **and** +1 Unrest (citizens blame the crown) |
| Diplomatic Overture | Faction relationship −1 (they found someone else to talk to) |
| Citizen Unrest | +3 Unrest instead of +2 |
| Military Desertion | Lose 1 army unit morale **and** −1 Loyalty |

**No expiry penalty:** Bountiful Harvest (free benefit), Visiting Celebrity (missed opportunity only), Trade Opportunity (missed gold only).

**Announce at turn start:** List all open events with expiry turns. *"The Monster Threat in hex SW-2 expires Turn 6."*

**Save block:** `kingdom.pending_events[]` — array of active events. Clear on resolution. Add `auto_resolved: true` when expiry fires.

---

## 📦 COMMODITIES (Abstracted Canon Layer)

> **Canon source:** PF2e Remaster and CRPG both use commodity resources for construction and consumption. This is a simplified version that preserves the feel without full accounting overhead.

```
COMMODITIES TRACKED:
  Food   — Offsets Consumption. 1 Food = −1 Consumption this turn. Max offset: 50% of base.
  Lumber — Required for roads and wooden structures. 1 Lumber per road hex; 1 per wooden build.
  Stone  — Required for stone structures and fortifications. 1 Stone per fortification or stone build.
  Ore    — Required for smithies, garrisons, castles, army equipment.

HOW COMMODITIES ARE GAINED:
  Work Site (Lumber Camp) → +1 Lumber per turn
  Work Site (Mine)        → +1 Ore per turn
  Work Site (Quarry)      → +1 Stone per turn
  Farmland hex            → +1 Food per turn
  Trade Agreement         → +1 of agreed commodity per turn

COMMODITY COSTS (added to RP cost):
  Road hex      : 1 Lumber (no Lumber = cannot build roads)
  Barracks      : 1 Ore
  Garrison      : 2 Ore
  Castle        : 4 Stone + 2 Ore
  Watchtower    : 1 Stone
  Courthouse    : 2 Stone
  All others    : No commodity cost (RP only)

TRACKING: Add commodity counts to kingdom JSON under "commodities": {food, lumber, stone, ore}
```

---



> Buildings are constructed in settlements via Civic Activities. Each building provides ongoing bonuses. Maximum 36 buildings per settlement.

| Building | Cost (RP) | Bonus | Notes |
|----------|-----------|-------|-------|
| House | 1 | +1 Stability, +50 pop | Basic residential |
| Mansion | 3 | +2 Stability, +100 pop, +1 Fame | Wealthy residential |
| Tavern | 1 | +1 Economy, −1 Unrest | |
| Inn | 2 | +1 Economy, +1 Loyalty | Travelers welcome |
| Market | 4 | +2 Economy | Enables full vendor stock |
| Smithy | 2 | +1 Economy | Weapons/armor at discount |
| Tannery | 1 | +1 Economy | Requires farmland hex |
| Mill | 2 | +1 Economy, −1 Consumption | |
| Temple (minor) | 2 | +1 Culture, +1 Loyalty | Any deity |
| Temple (major) | 6 | +2 Culture, +2 Loyalty | Requires minor temple |
| Library | 3 | +1 Culture, +1 Magic research | |
| Caster's Tower | 8 | +2 Culture, magic items available | Requires Library |
| Academy | 12 | +3 Culture | Requires Library |
| Barracks | 2 | +1 Stability, −1 Unrest | |
| Garrison | 4 | +2 Stability, enables army training | Requires Barracks |
| Watchtower | 2 | +1 Stability, +1 defense AC | |
| Castle | 16 | +3 Stability, +4 defense AC/HP | Requires Garrison |
| Dump | 1 | −1 Unrest, −1 Culture | Necessary evil |
| Graveyard | 1 | −1 Unrest | Reduces plague risk |
| Park | 2 | +1 Culture, −1 Unrest | |
| Town Square | 3 | −2 Unrest, +1 Loyalty | |
| Monument | 3 | +1 Culture, +1 Fame | |
| Pier | 2 | +1 Economy | Requires river/water hex |
| Waterfront | 6 | +2 Economy | Requires Pier |
| Jail | 3 | +1 Stability, −1 Unrest | |
| Courthouse | 6 | +2 Stability, −2 Unrest | Requires Jail |

---

## ⚔️ ARMY SYSTEM

> Armies become available and relevant from Ch2 onward. Ch5 (War of River Kings) heavily uses armies.

### Raising Armies

```
Recruit Army activity (Leadership Phase):
  Warfare check DC 16 → Success: 1 new army unit raised
  Cost: 2 RP per unit + 1 RP Consumption per turn per unit
  Time: 1 kingdom turn to raise
```

### Army Stats

| Stat | Description |
|------|-------------|
| **Size** | 1 (skirmish) to 10 (legion). Affects combat power. |
| **Morale** | 1–20. At 0 = disbanded. Recover via Leadership activities. |
| **Offense** | Attack bonus for army combat. |
| **Defense** | AC equivalent for army combat. |
| **Tactics** | Special abilities (Darkvision, Mounted, Spellcasting, etc.) |

**Army Combat (simplified):**
```
Each side rolls d20 + Offense modifier
Higher roll deals Morale damage = difference ÷ 2 (round up)
Combat continues until one army reaches 0 Morale
Winner may: Rout (enemy retreats), Capture (take prisoners), Destroy (permanent loss)
```

**Starting Army Types:**

| Unit | Offense | Defense | Morale | Cost | Notes |
|------|---------|---------|--------|------|-------|
| Levy | +2 | 12 | 10 | 1 RP | Conscript farmers |
| Infantry | +4 | 14 | 12 | 2 RP | Basic trained soldiers |
| Cavalry | +6 | 15 | 14 | 3 RP | Fast, high offense |
| Archers | +3 | 12 | 12 | 2 RP | Ranged, good vs cavalry |
| Elite Guard | +8 | 17 | 16 | 5 RP | Best personal unit |

---

## 📋 SETTLEMENT GROWTH TABLE

| Size | Population | Max Buildings | Defense Bonus |
|------|-----------|---------------|---------------|
| Hamlet | 1–200 | 4 | +0 |
| Village | 201–600 | 9 | +1 |
| Small Town | 601–2,000 | 18 | +2 |
| Large Town | 2,001–5,000 | 27 | +3 |
| Small City | 5,001–10,000 | 36 | +4 |
| Large City | 10,001–25,000 | 36 (dense) | +5 |
| Metropolis | 25,001+ | 36 (layered) | +6 |

Population grows +10% per turn if Loyalty > 50 and Unrest < 5.

---

## 🗓️ FIRST KINGDOM TURN (Ch1 — Founding Turn)

> **DM:** Run this immediately after capital location is chosen. It is a guided turn — most things are pre-set.

```
PHASE 1 UPKEEP:
  Assign Leadership:
    Ruler    = Player character (assigned automatically)
    Warden   = Kesten Garess (if kesten_respect = TRUE, offered immediately)
    Treasurer= Oleg Leveton (if Oleg relationship ≥ Friendly)
    Councilor= Linzi (if in party and relationship ≥ Friendly)
    All others = vacant (−2 penalty each to relevant stat next turn)

  Pay Consumption: Kingdom Size 1, no settlements yet = 1 RP Consumption
  Starting Treasury: 10 RP (from Jamandi's charter grant) + kingdom founding resources

  Unrest Check: Stability d20 + 0 = DC 15
    Starting Stability = 10 (base) + any bonuses from prologue flags
    On success: Stable. On failure: Unrest 1.

PHASE 2 COMMERCE:
  Tax Collection: Economy 5 ÷ 5 = 1 gp (tiny, as expected for a new kingdom)

PHASE 3 ACTIVITIES:
  Player gets 1 Region Activity (Size 1–10 = 1 slot): Claim Hex (capital hex is claimed automatically)
  Ruler gets 2 Leadership Activities: recommend Celebrate Holiday + Quell Unrest or Build prep
  Player gets 1 Civic Activity: Build first structure in capital settlement
    Recommended first build: Barracks (2 RP) or Town Square (3 RP, −2 Unrest)

PHASE 4 EVENT:
  First turn: No random event. Scripted message from Jamandi instead.
  She sends congratulations and the first political request (flavor only).

STARTING KINGDOM STATE:
  Name     : [Player names it]
  Capital  : [Selected location]
  Size     : 1 hex
  Culture  : 5  Economy: 5  Loyalty: 5  Stability: 10
  Unrest   : 0
  Fame     : 1  Infamy: 0
  Treasury : 10 RP
  Turn     : 1
```

---

## 💾 KINGDOM JSON TRACKING FORMAT

```json
"kingdom": {
  "name": "Stolen Lands",
  "capital_location": "River Confluence",
  "capital_coords": [0, 0],
  "founded_date": "Desnus 1, 4710 AR",
  "turn": 1,
  "size": 1,
  "region_activity_slots": 1,
  "culture": 5,
  "economy": 5,
  "loyalty": 5,
  "stability": 10,
  "unrest": 0,
  "fame": 1,
  "infamy": 0,
  "treasury_rp": 10,
  "consumption": 1,
  "commodities": {
    "food": 0,
    "lumber": 0,
    "stone": 0,
    "ore": 0
  },
  "leadership_roles": {
    "ruler": "player",
    "councilor": "Linzi",
    "general": "",
    "grand_diplomat": "",
    "high_priest": "",
    "magister": "",
    "marshal": "",
    "royal_enforcer": "",
    "spymaster": "",
    "treasurer": "Oleg Leveton",
    "warden": "Kesten Garess"
  },
  "settlements": [
    {
      "name": "",
      "coords": [0, 0],
      "size": "Hamlet",
      "population": 50,
      "buildings": ["Town Square"],
      "defense_ac": 15,
      "defense_hp": 20,
      "morale": 50,
      "consumption": 1
    }
  ],
  "armies": [],
  "claimed_hexes": [[0,0], [1,0]],
  "roads": [],
  "work_sites": [],
  "farmlands": []
}
```

---

## 📜 .kingdom COMMAND — DISPLAY FORMAT

> Full panel format in KM_Commands_Maps.md. Quick reference:

```
╔══════════════════════════════════════════════════════════╗
║  KINGDOM: [Name]  Size:[X]  Turn:[X]  Unrest:[X]         ║
╠══════════════════════════════════════════════════════════╣
║  Culture  [▮▮▮▮▮░░░░░]  [X]  Economy [▮▮▮▮▮▮░░░░]  [X] ║
║  Loyalty  [▮▮▮▮░░░░░░]  [X]  Stability[▮▮▮▮▮▮▮░░░]  [X]║
║  Fame [X]  Infamy [X]  Treasury [X] RP  Consumption [X]  ║
╠══════════════════════════════════════════════════════════╣
║  LEADERSHIP  (empty roles: -2 per stat per turn)          ║
║  Ruler:[name] Councilor:[name] General:[name]            ║
║  ... (all 11 roles)                                       ║
╠══════════════════════════════════════════════════════════╣
║  SETTLEMENTS  [Name] [Size] Pop:[X] Def:[X]/[X]          ║
╠══════════════════════════════════════════════════════════╣
║  TERRITORY  Controlled:[X]  Discovered:[X]  Armies:[X]   ║
╚══════════════════════════════════════════════════════════╝
```

---

## 🔥 KINGDOM FAILURE STATE

> **DM:** This section defines what actually happens when Unrest reaches 15+.
> It is not game over — it is a crisis arc. The player has a path forward.
> Reference this section whenever the Unrest table says "Kingdom in Crisis."

### Unrest 15–19 — Kingdom in Crisis

The kingdom is visibly unraveling. Every kingdom turn at this level:

```
AUTOMATIC EFFECTS (each turn):
  −2 to ALL kingdom stats (Culture, Economy, Loyalty, Stability)
  One random claimed hex reverts to Hostile (DM chooses narratively)
  One leadership role becomes functionally empty (rebellion, desertion, or fear)
  Consumption doubles (chaos disrupts supply chains)

CRISIS EVENTS (mandatory — roll on KM_Bestiary.md crisis table (kingdom events section)):
  Ch1: Stag Lord's Legacy or Bandit Resurgence (escalated version)
  Ch2: Troll Incursion or Bloom Cult crisis
  Ch3+: DM selects most narratively appropriate from chapter table

JAMANDI ALDORI INTERVENTION:
  If Unrest reaches 17 and the player has not responded to the crisis:
  Jamandi sends a representative with a warning — not help, a warning.
  "You have two turns to show the charter was not a mistake."
  Her letter arrives as a scripted event. It does not reduce Unrest.
  If Unrest hits 19: she arrives personally (see below).
```

**Recovery path from 15–19:**
The player must actively reduce Unrest — it will not drop on its own at this level.

| Action | Unrest Reduction | Cost |
|--------|-----------------|------|
| Celebrate Holiday (grand) | −1d6 | 4 RP + 500 gp |
| Player addresses crowd publicly (Diplomacy DC 22) | −2 | Player action (1 day) |
| Build Temple (any deity) | −1 permanent per temple | 6 RP + 3 turns |
| Suppress Rebellion (Loyalty DC 20) | −2 if success, +1 if fail | Leadership activity |
| Resolve active crisis event (success) | −2 to −4 | Varies by event |
| Player personally leads army (present in battle) | −1 per victory | Combat |

---

### Unrest 20 — Revolt

At Unrest 20 the kingdom does not simply continue declining. A Revolt Event fires immediately — this turn, before any other kingdom actions.

```
REVOLT EVENT SEQUENCE:

Step 1 — The Capital Rises
  A faction in the capital has organized. They have a leader.
  DM selects: Bandit remnants / Disillusioned nobles / Cult of the Bloom /
              Pitax-funded agitators (if Ch4+) / Nyrissa's influence (if Ch5+)
  The faction seizes ONE building in the capital. It is now under their control.
  Guards loyal to the player: roll Loyalty check DC 18. Fail: 25% desert.

Step 2 — Settlement Abandonment
  One non-capital settlement (DM chooses smallest/weakest) declares independence.
  It becomes Hostile territory. The player loses its tax income and buildings.
  To reclaim it: military action OR Diplomacy DC 26.

Step 3 — Jamandi's Ultimatum
  Jamandi Aldori arrives. Not as an enemy — as the original charter-giver.
  She does not attack. She gives the player one kingdom turn to restore order.
  Her exact words: "The charter was issued on the assumption that you could hold
  what you claimed. I am beginning to question that assumption."

  If player resolves Revolt within 1 turn: Jamandi departs satisfied.
    Unrest drops to 14. No further consequence.
  If player fails to resolve within 1 turn: see Collapse below.
```

---

### Kingdom Collapse (Unrest 20 + failed Revolt response)

This is the hard game over state. It is documented here so the DM knows what to narrate — not to prevent it, but to make it meaningful.

```
COLLAPSE SEQUENCE:

The capital building seized by rebels becomes their stronghold.
Jamandi formally revokes the charter. The Stolen Lands revert to unclaimed territory.
Your companions make individual choices — some stay, some leave.
  Amiri: stays ("I don't follow charters. I follow you.")
  Linzi: stays ("This is the best chapter yet.")
  Valerie: leaves ("My oath was to the kingdom. There is no kingdom.")
  Others: alignment-dependent.

THE PLAYER HAS TWO OPTIONS:
  A. Accept the collapse. Epilogue plays — what happened to the Stolen Lands,
     to each companion, to the player character who tried and failed.
     Not a bad ending. A real ending.

  B. Reclaim from zero. The player mounts a rebellion against whoever now controls
     the capital. Treat as a dungeon assault (KM_Ch1 Stag Lord's Fort rules apply —
     same structure, different occupants). Victory returns Unrest to 10 and restores
     the charter. Jamandi acknowledges the reclamation grudgingly.
     This path requires: defeating the Revolt leader (Level = current party level +2)
     + a successful Loyalty DC 24 address to the people after victory.
```

**The DM never fast-forwards to collapse.** If the player is approaching this state, the DM warns clearly — Jamandi's letters, companion dialogue, event descriptions all escalate. Collapse should feel earned, not sudden.

---

## ⚖️ ALIGNMENT → KINGDOM STATS

> Check these modifiers at the start of each kingdom turn alongside normal upkeep.
> Both axes apply simultaneously.

| Alignment | Automatic Effect per Turn |
|-----------|--------------------------|
| Lawful (+7 to +10) | +1 Stability |
| Slightly Lawful (+4 to +6) | None |
| Neutral (−3 to +3) | None |
| Slightly Chaotic (−4 to −6) | Loyalty −1 |
| Chaotic (−7 to −10) | Loyalty −1 and Unrest +1 |
| Good (+7 to +10) | Fame +1 per chapter; +1 to all Religion checks |
| Slightly Good (+4 to +6) | None |
| Neutral (−3 to +3) | None |
| Slightly Evil (−4 to −6) | Infamy +1 per chapter |
| Evil (−7 to −10) | Unrest +1 per turn; Tristian leaves if not resolved |

**Stacking:** A Chaotic Evil ruler (both axes at −7) faces Loyalty −1 + Unrest +2 per turn — a kingdom that collapses in roughly 8 turns without active intervention.

**Companion reactions:**
- Valerie: Loyalty below 10 → she comments. Below 5 → formal objection.
- Tristian: Evil axis −5 → private conversation about the kingdom's direction.
- Amiri: Chaotic axis +5 → approves openly.

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Kingdom Management v1.0*
*Source: Pathfinder Kingmaker AP (Paizo) | PF2e rules: 2e.aonprd.com*

> **
➡
️
 Faction reputation tracks 
→
 see `KM_Kingdom.md`**


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — KINGDOM MANAGEMENT (Part 2)
## KM_Kingdom.md | Faction Reputation Tracks
## PAIR-LOAD WITH KM_Kingdom.md

> **DM:** Load alongside KM_Kingdom.md. This file contains all 8 faction
> reputation tracks. Track scores in save block under `"faction_reputation": {}`.

---

## 🏛️ FACTION REPUTATION TRACKS
> **Faction tracks and villain offscreen behavior** — consolidated below.

> Each faction has a Reputation score from −10 (hostile) to +10 (allied).
> Starting values and change triggers are documented here.
> Track in save block under `"faction_reputation": {}`.

### Save Block Format

```json
"faction_reputation": {
  "aldori_swordlords": 0,
  "house_surtova": 0,
  "nomen_centaurs": -2,
  "river_kingdoms": 0,
  "pitax": -5,
  "brevoy_crown": 0,
  "tiger_lords": -3,
  "first_world_fey": 0
}
```

---

### ALDORI SWORDLORDS

**Starting value:** +2 (Jamandi gave the charter — baseline goodwill)
**Allied threshold:** +7 | **Hostile threshold:** −5

| Action | Change |
|--------|--------|
| Completing the charter (Stag Lord defeated) | +2 |
| Siding with Aldori at coronation | +3 |
| Siding with Surtova at coronation | −4 |
| Declaring independence at coronation | −1 |
| Kassil Aldori in a leadership role | +1/turn |
| Player publicly credits Jamandi | +1 |
| Player insults or defies Jamandi | −2 |
| Kingdom Unrest 15+ for 2+ turns | −2 (embarrassment) |

**At +7 (Allied):** Jamandi sends 2 Aldori duelists as personal guard (Fighters L8, free). Trade agreement: +2 Economy per turn.
**At −5 (Hostile):** Charter formally reviewed. If below −7: charter revoked (see Kingdom Failure State).

---

### HOUSE SURTOVA

**Starting value:** −1 (they wanted this territory for themselves)
**Allied threshold:** +6 | **Hostile threshold:** −6

| Action | Change |
|--------|--------|
| Siding with Natala Surtova at coronation | +4 |
| Siding with Aldori at coronation | −2 |
| Exposing Surtova involvement in any plot | −3 |
| Keeping Surtova's role quiet (discretion) | +1 |
| Sending tribute to Brevoy crown | +2 |
| Kingdom reaches Size 15+ | −1 (they're watching) |

**At +6 (Allied):** Natala offers a marriage alliance (narrative, player choice). Trade route through Brevoy: +3 Economy.
**At −6 (Hostile):** Surtova begins actively funding rivals — Unrest +1/turn (scripted event, cannot be rolled away).

**Note:** Aldori and Surtova are mutually exclusive above +5. If both reach +5, the player must choose — the other drops to +3 automatically. They cannot both be full allies.

---

### NOMEN CENTAURS

**Starting value:** −2 (territorial, suspicious of human expansion)
**Allied threshold:** +5 | **Hostile threshold:** −6

| Action | Change |
|--------|--------|
| Helping Xamanthe (Ch3) | +3 |
| Solving Vordakai without centaur casualties | +2 |
| Centaur deaths during player's campaign | −1 per named centaur |
| Claiming a hex bordering centaur territory without negotiating | −2 |
| Offering centaurs a formal treaty | +2 (Diplomacy DC 22 to present) |
| Kellid War-Bread purchased from Kellid camp | +1 (word spreads) |

**At +5 (Allied):** Centaur scouts reveal 3 hidden hexes on the map. Horse trade: mounted movement +1 hex/day. Nomen warriors available as army unit.
**At −6 (Hostile):** Centaur raids begin. Treat as Ch2-level Troll Incursion events per turn until resolved.

---

### RIVER KINGDOMS

**Starting value:** 0 (neutral — you're new, they're watching)
**Allied threshold:** +6 | **Hostile threshold:** −5

| Action | Change |
|--------|--------|
| Defeating Irovetti (Ch5) | +3 |
| Allowing Irovetti to invade without resistance | −3 |
| Player kingdom reaches Size 20+ | −1 (concern about dominance) |
| Winning River Kingdom Summit (Ch4) | +2 |
| Providing military aid to a River Kingdom | +2 |
| Annexing a River Kingdom settlement | −4 |

**At +6 (Allied):** River Kingdoms recognize the player's kingdom as a legitimate River Kingdom. +1 to all Diplomacy checks in the region. 2 ally armies available in Ch5 war.
**At −5 (Hostile):** River Kingdoms coordinate with Pitax. Irovetti's Ch5 army gets +2 Attack and +10 HP.

---

### PITAX

**Starting value:** −3 (Irovetti funded Malak's bribe attempt at Restov)
**Allied threshold:** N/A (cannot be fully allied while Irovetti lives)
**Hostile threshold:** −8 (triggers early war)

| Action | Change |
|--------|--------|
| Accepting Irovetti's protectorate offer (Ch2) | +3 (temporary) |
| Refusing Stefano Moskoni politely (Ch2) | +1 |
| Exposing Pitax involvement in Malak bribe | −2 |
| Each chapter that passes without conflict | −1 (inevitable drift) |
| Defeating Pitax armies in field | −2 each |

**At −8:** Irovetti invades early — Ch5 begins regardless of chapter. Player is not ready. Army stats unchanged but player has fewer resources.

**Post-Irovetti:** Pitax can be integrated as a vassal (+5 Economy per turn) or left independent (neutral relationship, no bonuses).

---

### BREVOY CROWN

**Starting value:** 0 (they granted the charter via Jamandi — officially neutral)

| Action | Change |
|--------|--------|
| Sending annual tribute (500 gp) | +1/year |
| Kingdom reaches Size 30+ | +1 (impressive) |
| Public scandal (Unrest 15+ reported) | −2 |
| Aldori faction at +7 | +1 (reflected glory) |
| Surtova faction at −6 | −2 (their noble house embarrassed) |

**At +6:** Crown officially endorses the kingdom. Bardic tales spread — Public Reputation +10.
**At −5:** Crown begins questioning charter legality. Jamandi must defend the player.

---

### TIGER LORDS

**Starting value:** −3 (hostile to kingdom expansion into their traditional territory)
**Allied threshold:** +5 | **Hostile threshold:** −7

| Action | Change |
|--------|--------|
| Defeating Armag (Ch4) | +1 (respect for strength) |
| Negotiating with Armag rather than fighting | +3 (rare path) |
| Claiming Tiger Lord ancestral hex without diplomacy | −2 |
| Allowing Tiger Lord raids without retaliation | −1/turn |
| Warrior champion of the kingdom defeats Tiger Lord champion | +2 |

**At +5 (Allied):** Tiger Lords pledge warriors — 1 Cavalry army unit joins (free). Hunting rights in eastern hexes granted.
**At −7 (Hostile):** Armag leads a united warband assault. Treat as Ch4 boss encounter with full army backing.

---

### FIRST WORLD FEY

**Starting value:** 0 (Nyrissa's influence — unstable, watching)
**Allied threshold:** +6 | **Hostile threshold:** −6

| Action | Change |
|--------|--------|
| Returning items to Tiressia and fey allies | +1 each |
| Protecting fey groves from settlement expansion | +1 per grove |
| Cutting down a fey grove for farmland | −3 |
| Completing Nyrissa's true ending (saving her) | +5 (permanent) |
| Killing Nyrissa without pursuing the true ending | −5 |
| Bloom corruption spreading unchecked | −1/chapter |

**At +6 (Allied):** Fey blessing on the kingdom — Culture +3 permanent, one hex per turn auto-discovers. Nyrissa (if saved) becomes a kingdom advisor (Culture +5, prevents fey events).
**At −6 (Hostile):** Bloom events intensify. Fey raids add +1 Unrest/turn and cannot be resolved by normal kingdom activities — require a personal confrontation scene.

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Faction Reputation Tracks v1.0*


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — SETTLEMENT BUILDING CATALOGUE
## KM_Kingdom.md | Active from: Chapter 2 (Kingdom Founded) | Referenced by: KM_Kingdom.md

---

> **DM:** Use this file during the Civic Activities step of each Kingdom Turn when the player issues Build Structure commands. Cross-reference KM_Kingdom.md for the turn sequence and DC rules. All costs are in Resource Points (RP) unless otherwise noted. Lumber, Stone, Ore, Luxuries are Commodity costs paid separately.

---

## 📐 BUILD STRUCTURE RULES

```
BUILD STRUCTURE — Civic Activity (1 per settlement per Kingdom Turn)
  Skill check required (varies by building — see Construction column)
  DC set by building level and required proficiency
  Critical Success: built, recover 10% RP cost
  Success: built
  Failure: RP/Commodities spent, not built (try again next turn)
  Critical Failure: RP/Commodities spent, Unrest +1

Lots: number of Urban Grid slots the building occupies
Infrastructure buildings (Lots —): apply to whole settlement, no lot needed
Residential buildings: required to avoid Overcrowded penalty
  Overcrowded: Unrest +1 per turn until resolved

Upgrade: pay (new cost − old cost), check at new DC
```

---

## 🏗️ COMPLETE BUILDING LIST

### Level 0–1 (Village-tier)

| Building | Lots | Cost (RP + Commodities) | Construction | Key Bonus / Effect |
|----------|------|------------------------|--------------|-------------------|
| **Tenement** | 1 | 1 RP, 1 Lumber | Industry DC 13 | Residential. Overcrowded risk reduced. Upgrade → Houses |
| **Brewery** | 1 | 6 RP, 2 Lumber | Agriculture DC 15 | +1 Establish Trade Agreement. First brewery built: Unrest −1 |
| **Cemetery** | 1 | 4 RP, 1 Stone | Folklore DC 15 | Dangerous settlement events: Unrest −1 (max −4 for 4 cemeteries) |
| **General Store** | 1 | 8 RP, 1 Lumber | Trade DC 15 | Without one: settlement effective level −2 for item availability. Upgrade → Luxury Store, Marketplace |
| **Granary** | 1 | 12 RP, 2 Lumber | Agriculture DC 15 | Each granary +1 max Food Commodity capacity |
| **Herbalist** | 1 | 10 RP, 1 Lumber | Wilderness DC 15 | +1 Provide Care. Upgrade → Hospital |
| **Houses** | 1 | 3 RP, 1 Lumber | Industry DC 15 | Residential. First built each turn: Unrest −1. Upgrade → Mansion or Orphanage |
| **Inn** | 1 | 10 RP, 2 Lumber | Trade DC 15 | +1 Hire Adventurers. Travelers rest here; +1 Gather Information in settlement |
| **Shrine** | 1 | 8 RP, 2 Lumber, 1 Stone | Folklore DC 15 | +1 Celebrate Holiday, Provide Care. Upgrade → Temple |
| **Wooden Wall** | — | 2 RP, 4 Lumber | Defense DC 15 | Infrastructure. +1 settlement Defense. Upgrade → Stone Wall |

---

### Level 2 (Village expanding)

| Building | Lots | Cost (RP + Commodities) | Construction | Key Bonus / Effect |
|----------|------|------------------------|--------------|-------------------|
| **Bridge** | — | 6 RP, 1 Lumber or 1 Stone | Engineering DC 16 | Infrastructure. Enables island settlement influence; negates Trade penalty for island settlements |
| **Dump** | 1 | 4 RP | Industry DC 16 | +1 Demolish. Required to avoid penalties in some events. Cannot share block with Residential |
| **Jail** | 1 | 14 RP, 4 Lumber, 2 Ore, 4 Stone | Defense DC 16 | +1 Quell Unrest. First built each turn: Crime −1 |
| **Library** | 1 | 6 RP, 4 Lumber, 2 Stone | Scholarship (trained) DC 16 | +1 Rest and Relax (Scholarship). +1 Lore Recall Knowledge, Research checks in settlement. Upgrade → Academy |
| **Mill** | 1 | 10 RP, 4 Lumber | Industry (trained) DC 16 | +1 Establish Work Site (lumber). Each mill +1 max Lumber Commodity capacity |
| **Orphanage** | 1 | 6 RP, 2 Lumber | Folklore DC 16 | Residential. First built each turn: Unrest −1 |
| **Town Hall** | 2 | 22 RP, 4 Lumber, 4 Stone | Statecraft (trained) DC 16 | +1 New Leadership, Pledge of Fealty. Leaders may take 2 Leadership activities/turn (instead of default). Upgrade → Castle |

---

### Level 3 (Town-tier)

| Building | Lots | Cost (RP + Commodities) | Construction | Key Bonus / Effect |
|----------|------|------------------------|--------------|-------------------|
| **Alchemy Laboratory** | 1 | 18 RP, 2 Ore, 5 Stone | Industry (trained) DC 16 | +1 Demolish. Settlement level +1 for alchemical item availability (stacks ×3). +1 Identify Alchemy |
| **Barracks** | 1 | 6 RP, 2 Lumber, 1 Stone | Defense DC 16 | Residential. +1 Garrison Army, Recover Army, Recruit Army. Upgrade → Garrison |
| **Festival Hall** | 1 | 7 RP, 3 Lumber | Arts DC 18 | +1 Celebrate Holiday. Upgrade → Theater |
| **Foundry** | 2 | 16 RP, 5 Lumber, 2 Ore, 3 Stone | Industry (trained) DC 18 | +1 Establish Work Site (mine). Each foundry +1 max Ore Commodity capacity. Cannot share block with Residential |
| **Keep** | 2 | 32 RP, 8 Lumber, 8 Stone | Defense (trained) DC 18 | +1 Deploy Army, Garrison Army, Train Army. First built each turn: Unrest −1. Upgrade → Castle |
| **Lumberyard** | 2 | 16 RP, 5 Lumber, 1 Ore | Industry DC 18 | +1 Establish Work Site (lumber). Each lumberyard +1 max Lumber Commodity capacity |
| **Monument** | 1 | 6 RP, 1 Stone | Arts DC 16 | +1 Celebrate Holiday, Repair Reputation (Decay or Strife). Reduce Unrest by 1 when built (once/turn) |
| **Park** | 1 | 5 RP | Wilderness DC 15 | +1 Quell Unrest. First built each turn: Unrest −1 |
| **Pier** | 1 | 8 RP, 2 Lumber, 1 Stone | Boating DC 16 | +1 Go Fishing, Establish Trade Agreement. Upgrade → Waterfront |
| **Smithy** | 1 | 8 RP, 2 Lumber, 1 Ore, 1 Stone | Industry DC 16 | +1 Establish Work Site, Outfit Army. Treat settlement 1 level higher for martial item availability |
| **Stable** | 1 | 10 RP, 2 Lumber | Wilderness DC 16 | +1 Cavalry army actions, Hire Adventurers. Reduces overland travel time from settlement |
| **Stockyard** | 4 | 20 RP, 4 Lumber | Agriculture DC 16 | +1 Establish Work Site (ranch). Each stockyard +1 max Food Commodity capacity |
| **Stonemason** | 2 | 16 RP, 2 Lumber | Industry DC 18 | +1 Build Structure. Each stonemason +1 max Stone Commodity capacity |
| **Trade Shop** | 1 | 10 RP, 2 Lumber | Trade DC 16 | +1 Earn Income. Specialize in one trade. Upgrade → Guildhall |
| **Watchtower** | 1 | 12 RP, 4 Lumber or 4 Stone | Defense DC 16 | +1 Hire Adventurers, Reconnoiter Hex. Reduces ambush chance in settlement hex |
| **Stone Wall** | — | 4 RP, 8 Stone | Defense DC 16 | Infrastructure. +2 settlement Defense (replaces Wooden Wall bonus). |

---

### Level 4–6 (Town growing)

| Building | Lots | Cost (RP + Commodities) | Construction | Key Bonus / Effect |
|----------|------|------------------------|--------------|-------------------|
| **Marketplace** | 2 | 48 RP, 8 Lumber | Trade (trained) DC 20 | +1 Establish Trade Agreement, Collect Taxes. Treat settlement 1 level higher for item availability. Upgrade From: General Store |
| **Paved Streets** | — | 24 RP, 8 Stone | Engineering DC 20 | Infrastructure. +1 all Civic activities in settlement. Reduces travel time within settlement |
| **Specialized Artisan** | 1 | 10 RP, 4 Lumber, 1 Luxury | Arts or Industry DC 20 | +1 Earn Income checks for specific craft. +1 to one specific Commodity production |
| **Arcanist's Tower** | 1 | 30 RP, 6 Stone | Magic (trained) DC 20 | +1 Quell Unrest (Magic). Settlement level +1 for arcane item availability (stacks ×3) |
| **Bank** | 1 | 28 RP, 4 Ore, 6 Stone | Trade (trained) DC 20 | +1 Establish Trade Agreement. Capital Investment activity only usable in settlements with a bank |
| **Garrison** | 2 | 28 RP, 6 Lumber, 3 Stone | Warfare (trained) DC 20 | +1 Outfit Army, Train Army. Upgrade From: Barracks |
| **Guildhall** | 2 | 34 RP, 8 Lumber | Trade (expert) DC 20 | +1 Economy skill checks for the guild's trade focus. First built: Crime −1, Unrest −1 |
| **Magical Streetlamps** | — | 20 RP | Magic DC 20 | Infrastructure. +1 Quell Unrest. Reduces crime events in settlement |
| **Mansion** | 1 | 24 RP, 6 Lumber, 6 Luxuries, 3 Stone | Industry DC 20 | Residential. +1 Improve Lifestyle. Upgrade From: Houses |
| **Museum** | 2 | 40 RP, 6 Lumber, 4 Luxuries | Arts (trained) DC 22 | +2 Celebrate Holiday, Repair Reputation. Donated items grant Culture XP |
| **Sacred Grove** | 1 | 36 RP | Wilderness (trained) DC 22 | +1 Primal magic item availability. +1 Provide Care using Folklore |
| **Illicit Market** | 1 | 50 RP, 5 Lumber | Intrigue (trained) DC 22 | +1 Clandestine Business. Ruin: +1 Crime. Settlement level +1 for illicit item availability |
| **Luxury Store** | 1 | 28 RP, 10 Lumber, 6 Luxuries | Trade DC 22 | +2 Establish Trade Agreement. Upgrade From: General Store |
| **Secure Warehouse** | 2 | 24 RP, 6 Lumber, 4 Ore, 6 Stone | Industry DC 22 | +1 Stockpile. Increases max Commodity storage by 1 for all Commodity types |

---

### Level 7–9 (City-tier)

| Building | Lots | Cost (RP + Commodities) | Construction | Key Bonus / Effect |
|----------|------|------------------------|--------------|-------------------|
| **Sewer System** | — | 36 RP | Engineering DC 24 | Infrastructure. Reduces disease events. +1 Demolish. Required for some advanced buildings |
| **Temple** | 2 | 32 RP, 8 Lumber, 6 Stone | Folklore (trained) DC 22 | +2 Celebrate Holiday, Provide Care, Repair Reputation. Unrest −2 first built. Upgrade From: Shrine → Upgrade To: Cathedral |
| **Embassy** | 2 | 26 RP, 10 Lumber, 6 Luxuries, 4 Stone | Politics DC 24 | +1 Send Diplomatic Envoy, Request Foreign Aid |
| **Magic Shop** | 1 | 26 RP, 2 Lumber, 2 Luxuries, 4 Stone | Magic (trained) DC 24 | +2 Arcane and Occult magic item availability. Settlement level +1 for all magic item availability |
| **Waterfront** | 4 | 90 RP, 10 Lumber | Boating (expert) DC 24 | +2 Go Fishing, Establish Trade Agreement. Trade routes may begin/end here. Upgrade From: Pier |
| **Arena** | 4 | 40 RP, 6 Lumber, 12 Stone | Warfare (expert) DC 26 | +2 Celebrate Holiday, Warfare checks. Combat feat retraining: 5 days (not 1 week) |
| **Castle** | 4 | 54 RP, 12 Lumber, 12 Stone | Defense/Industry/Magic/Statecraft (expert) DC 26 | +2 New Leadership, Pledge of Fealty, Send Diplomatic Envoy, Garrison/Recover/Recruit Army. Unrest −1d4 first built. Ruler: 3 Leadership activities/turn. Upgrade From: Town Hall or Keep |
| **Hospital** | 2 | 30 RP, 10 Lumber, 6 Stone | Defense (expert) DC 26 | +1 Provide Care, Quell Unrest. +2 Medicine checks to Treat Disease/Wounds in settlement. Upgrade From: Herbalist |
| **Noble Villa** | 1 | 24 RP, 10 Lumber, 8 Luxuries, 6 Stone | Industry DC 26 | Residential (luxury). +1 Improve Lifestyle, New Leadership |
| **Theater** | 4 | 78 RP, 18 Lumber, 18 Luxuries, 18 Stone | Arts (expert) DC 26 | +2 Celebrate Holiday, Recruit Army, Repair Reputation. Famous. Upgrade From: Festival Hall |

---

### Level 10–13 (Large City)

| Building | Lots | Cost (RP + Commodities) | Construction | Key Bonus / Effect |
|----------|------|------------------------|--------------|-------------------|
| **Academy** | 2 | 52 RP, 12 Lumber, 6 Luxuries, 12 Stone | Scholarship (expert) DC 27 | +2 Creative Solution. +2 Lore/Recall Knowledge (Investigate), Research checks, Decipher Writing in settlement. Upgrade From: Library |
| **Construction Yard** | 4 | 40 RP, 10 Lumber, 10 Stone | Engineering DC 27 | +1 Build Structure, Repair Reputation (Decay) |
| **Menagerie** | 4 | 40 RP, 10 Lumber, 6 Luxuries, 6 Stone | Wilderness (expert) DC 29 | Famous. +2 Celebrate Holiday. Grants access to rare creature lore checks |
| **Military Academy** | 2 | 36 RP, 12 Lumber, 6 Ore, 10 Stone | Warfare (expert) DC 29 | +2 Train Army, Recruit Army. Upgrade From: Academy |
| **Occult Shop** | 1 | 68 RP, 12 Lumber, 12 Luxuries, 6 Stone | Magic (expert) DC 30 | +2 Occult magic item availability. +2 Occultism checks in settlement |

---

### Level 15 (Metropolis-tier)

| Building | Lots | Cost (RP + Commodities) | Construction | Key Bonus / Effect |
|----------|------|------------------------|--------------|-------------------|
| **Cathedral** | 4 | 58 RP, 20 Lumber, 20 Stone | Folklore (master) DC 34 | +3 Celebrate Holiday, Provide Care, Repair Reputation. Unrest −4 first built. Settlement level +3 for divine items. Upgrade From: Temple |
| **Mint** | 2 | 30 RP, 10 Ore, 10 Stone | Trade (master) DC 34 | +3 Collect Taxes, Establish Trade Agreement. Kingdom earns bonus RP each turn equal to Economy ÷ 10 |
| **Opera House** | 4 | 78 RP, 18 Lumber, 18 Luxuries, 18 Stone | Arts (master) DC 34 | Famous. +3 Celebrate Holiday, Recruit Army, Repair Reputation. +3 Performance checks in settlement. Upgrade From: Theater |
| **Palace** | 4 | 108 RP, 20 Lumber, 20 Luxuries, 20 Stone | Defense/Statecraft (master) DC 34 | +3 all Statecraft and Politics checks. Ruler gains 4 Leadership activities/turn. Upgrade From: Castle |
| **University** | 4 | 78 RP, 18 Lumber, 10 Luxuries, 18 Stone | Scholarship (master) DC 34 | Famous. +3 Research, Recall Knowledge, all Scholarship checks. Upgrade From: Academy |

---

## 🔗 UPGRADE CHAINS

```
Tenement → Houses → Mansion → Noble Villa
Shrine → Temple → Cathedral
General Store → Marketplace / Luxury Store
Festival Hall → Theater → Opera House
Library → Academy → Military Academy / University
Barracks → Garrison
Herbalist → Hospital
Pier → Waterfront
Town Hall → Castle → Palace
Trade Shop → Guildhall
```

---

## 📦 COMMODITY QUICK REFERENCE

```
Lumber   — from forests, Lumberyards add +1 max storage each
Stone    — from hills/mountains, Stonemasons add +1 max storage each
Ore      — from mines, Foundries add +1 max storage each
Food     — from farms/fishing, Granaries/Stockyards add +1 max storage each
Luxuries — from trade, no storage building (unlimited)

Base max storage per Commodity type: 4
Each relevant building adds +1 (see table above)
```

---

## 🛏️ PERSONAL CHAMBERS — THE RULER'S QUARTERS

> **DM:** The Personal Chambers are the player's private space in the capital —
> separate from the Throne Room and council functions. They become available once
> a Castle or Palace is built. The player furnishes them over time through
> purchases, quest rewards, and crafting. Furnishings provide passive mechanical
> benefits and serve as a social space where companions comment and interact.
> This is the Sims layer of the kingdom — small, personal, yours.

### Unlocking Personal Chambers

Personal Chambers unlock automatically when the capital contains a **Castle** or
**Palace**. No additional build action required — the space exists; it just needs
furnishing. An unfurnished Chambers is narratively present but provides no benefits.

---

### Furnishing Slots

Each Chambers has **6 furnishing slots**. Slots are filled by purchasing, finding,
or crafting furnishing items. Only one item per slot category. Replacing a furnishing
costs nothing — the old item is stored, not lost.

| Slot | Category | Description |
|------|----------|-------------|
| 1 | **Desk & Study** | Writing surface, research tools, maps |
| 2 | **Display** | Trophy wall, weapons rack, portrait, shelf of curiosities |
| 3 | **Rest** | Bed quality, linens, bedside items |
| 4 | **Comfort** | Seating, fireplace, rugs, ambient furnishings |
| 5 | **Personal** | Items tied to the player's backstory or companions |
| 6 | **Arcane / Sacred** | Ritual space, shrine, spell focus display (optional) |

---

### Furnishing Items & Effects

#### Slot 1 — Desk & Study

| Item | Source | Cost | Effect |
|------|--------|------|--------|
| **Field Commander's Desk** | Merchant (Ch2+) | 80 gp | +1 to all Kingdom Research checks |
| **Cartographer's Table** | Merchant or craft | 120 gp | Hex exploration reveals one adjacent hex terrain type automatically |
| **Scholar's Escritoire** | Quest reward or Jubilost | — | +2 to Recall Knowledge checks made during Downtime |
| **War Council Map** | Craft (Society DC 20) | 60 gp | +1 to army Warfare checks for 1 turn after reviewing it (1/turn) |

#### Slot 2 — Display

| Item | Source | Cost | Effect |
|------|--------|------|--------|
| **Trophy Wall** | Craft (Crafting DC 16) | 30 gp base | Each significant monster trophy mounted: +1 Morale bonus to party on first combat of a session (max +3) |
| **Weapons Rack** | Merchant (Ch1+) | 40 gp | Spare weapon stored here is always considered *drawn* at start of combat if player is in the capital |
| **Painted Portrait** | Commission (Linzi quest link) | 200 gp | +1 Culture per Kingdom Turn. Companions comment on it. |
| **Shelf of Curiosities** | Assembled from found items | — | Each Relic Fragment or Storyteller item displayed: +1 to Lore checks related to that fragment's origin |

#### Slot 3 — Rest

| Item | Source | Cost | Effect |
|------|--------|------|--------|
| **Standard Bed** | Default (free) | — | No effect |
| **Featherdown Bed** | Merchant (Ch2+) | 60 gp | Recovery during capital rest: +2 HP per level healed overnight |
| **Enchanted Linens** | Magic Shop (Ch3+) | 300 gp | Sleep in capital: automatically lose Fatigued condition; +1 to Will saves next session |
| **War Cot** | Craft (Industry DC 14) | 15 gp | Deliberately Spartan. +1 to Fortitude saves next session; Amiri approves (+1 Morale if she's in party) |

#### Slot 4 — Comfort

| Item | Source | Cost | Effect |
|------|--------|------|--------|
| **Hearthfire Setup** | Merchant or craft | 50 gp | Camp Interlude scenes that occur in the capital gain +1 to all relationship checks (warmth effect) |
| **Fine Rugs** | Merchant (Luxuries) | 80 gp | +1 to Diplomacy checks made in the Chambers (private meetings) |
| **Velvet Seating** | Merchant (Ch3+) | 100 gp | Companions who visit recover 1 additional Mood step (Troubled → Steady faster) |
| **Bare Stone** | Default (free) | — | No effect. Some companions respect it. Regongar respects it. |

#### Slot 5 — Personal

| Item | Source | Cost | Effect |
|------|--------|------|--------|
| **Companion Gift Display** | Assembled from gifted items | — | Each meaningful gift received from a companion and displayed: that companion's Bond History DC −1 (permanent) |
| **Homeland Memento** | Player backstory item | — | +1 to Will saves vs fear and despair; Tristian asks about it once |
| **Fallen Ally Memorial** | Placed after a companion death | — | Party Morale does not drop below 2 while this is present (grief is held, not lost) |
| **Nyrissa's Gift** | Story flag: specific Ch6 event | — | Arcane resonance. +1 to saves vs enchantment. Companions are unsettled by it. |

#### Slot 6 — Arcane / Sacred (optional)

| Item | Source | Cost | Effect |
|------|--------|------|--------|
| **Travel Shrine** | Merchant (religious) or Tristian | 60 gp | Refocus in the Chambers takes 5 minutes instead of 10 |
| **Spell Focus Shelf** | Craft (Arcana DC 18) | 90 gp | Identify Magic checks made in the Chambers: +2 to roll |
| **Ritual Circle** | Craft (Occultism DC 20) | 150 gp | Once per session, may reroll one failed spell attack or save DC check (in capital only) |
| **Empty** | — | — | No effect. Valid choice. |

---

### Companion Reactions to the Chambers

When a companion visits the player's Chambers for the first time, or when a new
furnishing is added, the DM runs a brief ambient reaction (1–2 lines, not a
choice menu). These fire once per furnishing change, not repeatedly.

| Companion | What they notice | What they say (or don't) |
|-----------|-----------------|--------------------------|
| **Valerie** | Whether it's ordered or chaotic | If ordered: says nothing, but doesn't leave immediately. If chaotic: *"This is how you think."* |
| **Linzi** | Everything. Takes notes. | *"Can I describe this in the chronicle? The desk especially."* |
| **Amiri** | The weapons rack or war cot | Touches the weapons without asking. Approves if they're real and used. |
| **Tristian** | The sacred slot | If shrine present: kneels briefly. If empty: *"You haven't decided yet."* |
| **Harrim** | The memorials | If a Fallen Ally Memorial is placed: stands there a long time. Says nothing. |
| **Nok-Nok** | The trophy wall | *"Nok-Nok's trophies should be here. Nok-Nok has MANY trophies."* |
| **Octavia** | The books and desk | Picks one up without asking. Returns it. Has opinions about the selection. |
| **Regongar** | Size of the room | *"Smaller than I expected."* (This is a compliment.) |
| **Jaethal** | The portrait if present | Studies it. *"A good likeness. The painter understood something."* Doesn't say what. |
| **Ekundayo** | The window and its view | Stands at it. His hound sits beside him. Quiet. |

---

### Chambers Commands

| Command | Output |
|---------|--------|
| `.chambers` | Current furnishing layout, all 6 slots, active effects |
| `.chambers [slot]` | Detail on one slot and available alternatives |
| `.furnish [item]` | Place an item in its slot (DM confirms availability) |
| `.chambers effects` | All active passive bonuses from current furnishings |

---

### Chambers Save Block Addition

Add to the capital settlement entry in the save block:

```json
"personal_chambers": {
  "unlocked": false,
  "furnishings": {
    "desk_study": null,
    "display": null,
    "rest": "Standard Bed",
    "comfort": null,
    "personal": null,
    "arcane_sacred": null
  },
  "companion_reactions_fired": []
}
```

---

## 💾 BUILDING SAVE BLOCK FORMAT

> **DM:** Track buildings in the save block under each settlement's `buildings[]` array. Use the exact building names from this file.

```json
"settlements": [
  {
    "name": "Capital Name",
    "size": "village",
    "blocks": 1,
    "lots_used": 3,
    "lots_total": 9,
    "overcrowded": false,
    "buildings": ["Shrine", "Barracks", "Houses", "Town Hall"],
    "defense_bonus": 1,
    "item_bonus_cap": 1
  }
]
```

---

## 🏗️ HEX FORTIFICATIONS (Built on hex map, NOT in settlements)

> **DM:** Hex fortifications are kingdom investments placed on specific hexes to control territory. They affect army movement, border defense (KM_Kingdom.md), and provide defensive bonuses during hex encounters. Built via kingdom activity during Kingdom Turn Phase 3.

| Fortification | RP Cost | Build Time | Defense Bonus | Special |
|---------------|---------|-----------|---------------|---------|
| **Watchtower** | 6 RP | 1 turn | +2 to detect incoming raids/armies in adjacent hexes | Garrison: 1 guard unit. Spotting range: 2 hexes. |
| **Palisade** | 4 RP | 1 turn | +1 AC to all defenders in hex combat | Blocks cavalry charges. Attackers must breach (Athletics DC 16) or go around. |
| **Trapped Approach** | 8 RP | 2 turns | Attackers take 2d6 damage entering hex (Ref DC 18 half) | Requires Crafting DC 14 to construct. Hidden until triggered. Rearms in 1 turn. |
| **Fort** | 16 RP | 3 turns | +4 AC to defenders, provides cover, arrow slits | Garrison: 1 army unit. Supplies for 30 days siege. Can anchor defense line. |
| **Moat** | 10 RP | 2 turns | Attackers need 2 actions to cross (difficult terrain + Athletics DC 14) | Must be adjacent to Fort. Blocks siege equipment approach from that hex side. |

### Rules
- Max 1 fortification per hex (except Moat, which adds to an existing Fort)
- Fortifications can be destroyed by enemy armies (Siege rules — KM_War_Systems.md)
- Watchtowers grant early warning: player learns about border raids 1 turn earlier
- **Save block per hex:** `"fortifications": [{"hex": [x,y], "type": "watchtower", "garrison": "guard_unit_1"}]`

---

## 🏛️ ADVENTURER'S GUILD (Settlement Building)

| Field | Value |
|-------|-------|
| **RP Cost** | 12 RP |
| **Build Time** | 2 turns |
| **Requires** | Tavern in same settlement |
| **Kingdom Bonus** | Economy +1, Stability +1 |
| **Special** | Unlocks `.board` command (KM_Kingdom.md). Hired adventurer parties become available. |
| **Description** | A stone-and-timber hall with a bounty board, contract desk, and lodging for transient adventurers. The guild master takes a 10% cut of all posted bounties. |

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Settlement Building Catalogue v2.0*
*New: Hex Fortifications (5 types), Adventurer's Guild building*


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — LIVING WORLD SYSTEMS
## KM_Kingdom.md | Active from: Chapter 1 | Referenced by: KM_Companions.md, KM_Actions.md, KM_Kingdom.md

> **DM:** Load this file every session alongside KM_Companions.md. It adds three
> ambient systems that run in the background without requiring player attention:
> Party Morale, Companion Mood States, and the Bond History Log. None of these
> systems replace existing mechanics — they layer texture on top of them. All
> three are tracked in the JSON Save Block.

---

## 🔥 SYSTEM 1 — PARTY MORALE

> **What it is:** A shared emotional weather system for the party. Not individual
> companion approval — the collective spirit of the group. High morale means
> the party moves, jokes, argues, and fights like a unit. Low morale means
> they're quiet in the wrong way, short with each other, looking at the horizon
> too long.

### The Morale Track

```
Morale 10 — BLAZING   : The party is alive. Banter is constant. Someone is
                         always starting something. Combat feels inevitable
                         and welcome. +1 bonus die to one party skill check
                         per session (player chooses when to spend it).

Morale 7–9 — HIGH     : Good energy. Companions volunteer opinions. Camp is
                         comfortable. No mechanical effect — just good days.

Morale 4–6 — STEADY   : The default. Professional. They're doing the work.
                         Functionally fine. Narratively quiet.

Morale 2–3 — LOW      : Tension in the silences. Companions speak less.
                         Approval gains from positive actions are halved
                         (round down) until Morale reaches 4+.

Morale 1 — FRACTURED  : Someone is going to say something they can't take back.
                         DM triggers a mandatory Fracture Scene this session —
                         a short confrontation between two companions or between
                         a companion and the player. Approval gains suspended
                         entirely until the scene resolves.

Morale 0 — BROKEN     : The party is not a party. They are individuals sharing
                         a road. Companion combat cooperation reduced (no Aid
                         actions between companions). DM runs a Morale Crisis
                         scene — player must address it or lose one companion
                         to temporary departure (1d3 sessions, returns after).
```

**Starting value:** 5 (Steady). Track as `party_morale` in save block.

---

### Morale Gain Triggers (+1 unless noted)

**Camp actions that build morale:**
- C16 Storytelling activity succeeds → +1
- C10 Cook Special Meal (success or better) → +1
- Player spends a Camp Interlude on a companion (any companion, not just romance) → +1
- Party completes a significant quest and takes time to acknowledge it → +1
- Player initiates any non-tactical conversation with a companion at camp → +1 (once per session)

**In the field:**
- Party wins a combat against a significantly dangerous enemy (CR = party level +2 or higher) → +1
- Player makes a choice that benefits the group at personal cost → +1
- A companion's personal quest advances → +1
- Party reaches a new major location for the first time → +1 (wonder effect)
- Player calls out a companion specifically for doing something well → +1

**Kingdom events:**
- Successful Celebrate Holiday action → +1
- Player hosts a Gathering (see KM_Kingdom.md System 4) → +2
- Kingdom achieves a milestone (new settlement founded, army victory, major building complete) → +1

**+2 triggers (rare):**
- Party survives a near-total-wipe encounter → +2 (shared danger bonds)
- A companion's personal quest completes → +2
- Player remembers a detail from an old conversation and acts on it in front of the group → +2

---

### Morale Loss Triggers (−1 unless noted)

**Neglect:**
- Party rests with no social activity at all (no C16, no interlude, no conversation) → −1
- Player skips 3 consecutive rest scenes without any companion interaction → −1 additional
- Player dismisses a companion's concern with no acknowledgment → −1

**Events:**
- A companion dies in combat (even if raised) → −2
- Party is ambushed while asleep (watch failed) → −1
- Party is forced to retreat from an encounter → −1
- Player makes a kingdom decision that multiple companions oppose → −1
- Extended travel with no discoveries, no events, no rests with activity → −1 per 3 days

**−2 triggers:**
- Player commits a capital crime witnessed by the party → −2
- A companion leaves the party (for any reason) → −2
- Player betrays or publicly humiliates a companion → −2

---

### Morale Ceiling & Floor Rules

- **Ceiling:** Morale cannot exceed 10. At 10, the +1 bonus die refreshes each session automatically.
- **Floor:** Morale cannot go below 0 through passive decay. It reaches 0 only through an active negative trigger at Morale 1.
- **Natural recovery:** If no loss triggers fire for a full session, Morale recovers +1 at session end (the party breathes).
- **Morale and Kingdom:** Morale 7+ adds +1 to one Kingdom skill check per turn (player declares before rolling). Morale 2 or below: −1 to all Kingdom skill checks (the ruler is distracted and it shows).

---

### Fracture Scene (fires at Morale 1)

The DM selects two companions with the most opposing values currently in the party and runs a short (3–5 exchange) scene. The player can intervene or observe.

**If player intervenes:** Diplomacy or Intimidation DC 16.
- Success: Morale → 3. Both companions cool down. One says something honest that wasn't mean.
- Failure: Morale stays at 1. Scene ends unresolved. Comes back next session.
- Critical Success: Morale → 4. The argument cleared something. Relationship between those two companions +1.

**If player does not intervene:** The companions resolve it themselves, imperfectly. Morale → 2. One companion's relationship with the player drops −1 (they noticed the player said nothing).

---

## 😶 SYSTEM 2 — COMPANION MOOD STATES

> **What it is:** Each companion carries a current Mood State that colors how they
> speak, act, and react — separate from Relationship score. Relationship is the
> long arc. Mood is today. A Devoted companion can be Troubled. A Neutral companion
> can be Inspired. Mood shifts are temporary; they fade or resolve within 1–3
> sessions unless a new trigger extends them.

### The Five Mood States

```
INSPIRED  : Something happened that lit them up. They're sharper, warmer,
             more present. Volunteers opinions. Easier to talk to. +1 to
             Assist actions from this companion this session.

STEADY    : Default. They're fine. Doing the job. No modifier.

TROUBLED  : Something is weighing on them. Quieter than usual. Distracted
             at the wrong moments. −1 to Assist actions. May decline small
             talk. Not hostile — just carrying something.

WITHDRAWN : They've gone inward. Brief answers. Won't initiate. Still
             functional in combat. Approval gains from positive actions
             don't fire for this companion until mood lifts.

VOLATILE  : Something cracked. They're reactive — too loud, too sharp, too
             quick to take offense or too quick to laugh. Unpredictable.
             DM rolls d6 secretly each scene: 1–2 they say something they
             shouldn't; 3–6 they hold it together.
```

---

### Mood Triggers by Companion

**AMIRI**
- → Inspired: Won a hard fight; player acknowledged her strength without conditions; tribal memory invoked positively
- → Troubled: Her quest thread is stalled; player chose diplomacy over fighting when she wanted to fight; someone called her a savage and the player didn't respond
- → Volatile: Her quest involves her tribe; player sided against Kellid culture; she's been sidelined from combat for 2+ sessions

**LINZI**
- → Inspired: Got a great quote; witnessed something genuinely historic; player told her the chronicle matters
- → Troubled: The kingdom is doing badly; she witnessed something she can't write honestly; someone died she cared about
- → Withdrawn: Player dismissed the chronicle; she wrote something and showed the player and player ignored it
- → Volatile: Someone threatened to destroy her writing or the chronicle

**VALERIE**
- → Inspired: Upheld a principle under pressure; player backed her formal objection; someone needed protecting and she did it
- → Troubled: The kingdom is lawless or unjust; player did something she considers dishonorable; her faith in structure is shaken
- → Withdrawn: Player has been making chaotic decisions consistently; she's reassessing
- → Volatile: Player attacked a surrendered enemy; an innocent was punished; her shield oath was mocked

**TRISTIAN**
- → Inspired: Healed someone who asked for nothing; witnessed genuine goodness; player made a merciful choice
- → Troubled: His past was referenced; the party did something morally grey he couldn't stop; he's praying more than usual
- → Withdrawn: Player committed a crime he witnessed; his faith is quiet (not gone, quiet)
- → Volatile: Sarenrae directly relevant and things went wrong; undead were created unnecessarily

**HARRIM**
- → Inspired: (rare) Something failed so completely it loops back to beautiful; the end felt close; Groetus was mentioned
- → Troubled: Things are going too well; he's suspicious of hope
- → Steady: Almost always. Harrim is the most emotionally consistent companion. Doom is a stable condition.
- → Volatile: Someone sincerely told him things will be okay and seemed to mean it

**REGONGAR**
- → Inspired: Violence solved a problem cleanly; player let him intimidate someone; he won something through raw power
- → Troubled: Octavia is in danger; he was made to feel weak or controlled
- → Volatile: Someone tried to give him orders like he's property; old slavery wounds touched

**OCTAVIA**
- → Inspired: Clever solution; player let her run a scheme; she outsmarted something
- → Troubled: Regongar is struggling; she's managing something she won't explain
- → Withdrawn: She's running a plan she hasn't told the party about yet
- → Volatile: Someone referenced her slave history as a joke or leverage

**JAETHAL**
- → Inspired: (her version) Something interesting happened to a mortal soul; she learned something
- → Troubled: Her undeath is relevant and unwelcome; someone treated her as a monster without engaging with her
- → Volatile: Urgathoa insulted directly; her personhood denied by someone she respected

**NOK-NOK**
- → Inspired: He did something brave and everyone noticed; a big thing died; he got to be the hero
- → Troubled: He feels small again; someone laughed at him without it being a good joke
- → Volatile: He was genuinely scared and won't admit it; a goblin thing went badly

**EKUNDAYO**
- → Inspired: Justice was done; a family was protected; his hound is acknowledged
- → Troubled: His quest thread is unresolved; someone reminded him of loss without care
- → Withdrawn: He's tracking something and the party keeps interrupting

---

### Mood Duration & Resolution

```
Mood states last:
  Inspired:   1 session (fades naturally; can be extended by continued positive triggers)
  Troubled:   1–2 sessions (resolves when the source is addressed or time passes)
  Withdrawn:  2–3 sessions (requires player acknowledgment to resolve faster)
  Volatile:   1 session (resolves after the session ends; may leave aftermath)

RESOLVING MOOD EARLY:
  Player can attempt to address a companion's mood during a Camp Interlude or
  quiet scene. No roll required — just genuine engagement with the right topic.
  DM judges if the player's approach fits the companion's current state.
  If it fits: mood resolves immediately or steps toward Steady.
  If it misses: mood continues. The companion appreciates that you tried.
```

---

### How Mood Affects Narration

The DM uses Mood to color ambient behavior — not to flag it mechanically.

- **Never announce mood state to the player.** Show it through behavior.
- Inspired Linzi: writing faster, more questions, physically closer to the action.
- Troubled Valerie: armor checked twice before sleep, briefer answers, the careful way she sets her shield.
- Withdrawn Ekundayo: his hound is closer to him than usual. He isn't ignoring you — he's somewhere else.
- Volatile Regongar: everything lands slightly wrong. He's too agreeable or too sharp, never calibrated.

---

## 📖 SYSTEM 3 — BOND HISTORY LOG

> **What it is:** A running record of meaningful moments between the player and
> each companion. Not stats — flagged narrative beats that the DM references
> in later scenes. The campaign has memory. Companions remember what happened.
> So does the world.

### What Gets Logged

The DM logs a Bond Moment when:
- A companion's personal quest advances or completes
- Player makes a choice specifically for or against a companion's stated value
- A Camp Interlude resolves with a meaningful outcome (not every interlude — the ones that land)
- Player says something a companion will not forget (in either direction)
- Player defends, risks for, or sacrifices something for a specific companion
- A crime or serious act is witnessed by a companion
- Romance reaches a new stage
- Brotherhood reaches a new stage
- A companion nearly dies and the player's action was decisive

### Log Format

Each entry is one sentence in the companion's implied voice — what they are still carrying from that moment.

```
BOND HISTORY LOG — [Companion Name]
[Chapter] [Brief moment tag] — "[One sentence in companion's implied voice]"
```

**Example entries:**

```
BOND HISTORY LOG — Valerie
Ch1 Nettles Crossing — "You paid the ferryman's debt without asking why it mattered."
Ch2 Troll attack — "You put yourself between me and it. You didn't have to."
Ch2 Kingdom vote — "You chose the law when everyone wanted you to bend it. I noted that."

BOND HISTORY LOG — Nok-Nok
Ch1 Sootscale — "You let Nok-Nok go first. Into the scary cave. Nok-Nok went first."
Ch2 Big troll — "Nok-Nok killed the big one. Commander saw. Commander said so."

BOND HISTORY LOG — Harrim
Ch1 Shrine — "You didn't try to fix it. You sat with it. That was unexpected."
Ch3 Near-death — "You carried me out. I told you not to bother. You didn't listen."
```

---

### How the DM Uses the Log

**Reference in ambient dialogue:** Companions occasionally reference logged moments unprompted. Not constantly — rarely. When it lands, it lands hard.

**Use in relationship checks:** When a player attempts a Diplomacy check with a companion, if there are 3+ positive Bond Moments logged, the DC reduces by 2. If there are 2+ negative moments (crimes witnessed, choices that hurt the companion), DC increases by 2.

**Use in crisis scenes:** When a companion is at Hostile relationship or considering leaving, the Bond History Log is the DM's reference for what the player can invoke. You cannot invoke a moment that isn't logged.

**Use in death/farewell scenes:** If a companion dies or permanently departs, the DM reads back one logged Bond Moment as part of the scene. Just one. The right one.

---

### Bond History Save Block Format

```json
"bond_history": {
  "Amiri": [
    { "chapter": 1, "tag": "troll_fight", "memory": "You hit harder than the troll. I was watching." }
  ],
  "Linzi": [
    { "chapter": 1, "tag": "chronicle_read", "memory": "You asked to read it. You didn't have to ask." }
  ],
  "Valerie": [],
  "Tristian": [],
  "Harrim": [],
  "Jaethal": [],
  "Octavia": [],
  "Regongar": [],
  "Nok-Nok": [],
  "Ekundayo": [],
  "Kalikke": []
}
```

---

## 💾 FULL LIVING WORLD SAVE BLOCK

```json
"living_world": {
  "party_morale": 5,
  "morale_bonus_die_available": false,
  "fracture_scene_pending": false,
  "morale_crisis_pending": false,
  "sessions_without_social": 0,

  "companion_moods": {
    "Amiri":     { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Linzi":     { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Valerie":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Tristian":  { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Harrim":    { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Regongar":  { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Octavia":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Jaethal":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Nok-Nok":   { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Ekundayo":  { "mood": "Steady",  "sessions_remaining": null, "source": null },
    "Kalikke":   { "mood": "Steady",  "sessions_remaining": null, "source": null }
  },

  "bond_history": {
    "Amiri": [], "Linzi": [], "Valerie": [], "Tristian": [],
    "Harrim": [], "Regongar": [], "Octavia": [], "Jaethal": [],
    "Nok-Nok": [], "Ekundayo": [], "Kalikke": []
  }
}
```

---

## 🖥️ LIVING WORLD COMMANDS

| Command | Output |
|---------|--------|
| `.morale` | Current Morale score, stage name, active modifiers |
| `.mood` | All companions: current mood state and sessions remaining |
| `.mood [name]` | One companion's mood, source, and how it's showing |
| `.bond` | Bond History Log — all companions, all logged moments |
| `.bond [name]` | Bond History Log for one companion only |
| `.bond add [name] [tag] [memory]` | DM tool: manually log a Bond Moment |

---

## ⚠️ DESIGN RULES FOR THE DM

1. **Morale is weather, not punishment.** A Morale 2 session isn't a bad session — it's a cold morning before something happens. Don't play it as failure.
2. **Mood is shown, never told.** If Linzi is Troubled, she doesn't say "I am troubled." She's quieter. She forgets to take notes for a bit. She goes to sleep before the fire dies.
3. **The Bond Log earns its weight in late chapters.** Log faithfully from Ch1. By Ch5 and Ch6, the DM has a library of things that matter. Use it.
4. **Don't over-trigger.** Not every rest needs a Morale event. Not every scene needs a mood beat. These systems live in the gaps — they make the gaps mean something.
5. **Volatile is not the same as Hostile.** A Volatile companion is reactive, not adversarial. They're at the edge of themselves. Play the edge, not the fall.

---

---

## 🏷️ DISPOSITION TAGS — BEHAVIORAL TRACKING

> **DM:** Track silently. Five tags accumulate from player choices. At threshold 3+, NPCs reference the tag in dialogue. Tags are NOT alignment — a Good character can be Ruthless (efficient violence), a Chaotic character can be Scholarly (curious mind).

### The Five Tags

| Tag | Gains From | NPCs Say (at 3+) |
|-----|-----------|-------------------|
| **Merciful** | Sparing enemies, healing prisoners, offering second chances | "They say you let the bandit captain walk." / "A ruler who spares is either wise or naive." |
| **Ruthless** | Executing prisoners, choosing lethal solutions, intimidation kills | "I heard what happened to the last one who defied you." / Merchants lower prices unprompted. |
| **Cunning** | Deception successes, spotting traps/lies, outmaneuvering NPCs | "You see things before they happen, don't you?" / Rogues and spies approach first. |
| **Blunt** | Direct confrontation, refusing subterfuge, saying what others won't | "At least with you I know where I stand." / Soldiers respect it. Diplomats wince. |
| **Scholarly** | Knowledge checks, examining objects, asking follow-up questions, reading documents | "You ask the questions nobody else thinks to ask." / Sages seek you out. |

### Accumulation Rules
- **+1 tag** when player makes a choice that clearly fits the tag (DM judgment, do not announce)
- **Max 10 per tag.** Tags are not mutually exclusive — a player can be Merciful 5 AND Cunning 7
- **Visibility threshold: 3.** Below 3, NPCs don't reference it. At 3+, it colors dialogue
- **Dominant tag** = highest value. If tied, both are dominant. NPCs reference dominant tag first
- **Save block:** `"dispositions": { "merciful": 0, "ruthless": 0, "cunning": 0, "blunt": 0, "scholarly": 0 }`
- **Full NPC reaction tables by tag + settlement type → see `KM_Mythic_Systems.md`**

---

## 📊 MORALE EXPANSION — SUB-THRESHOLDS

> **DM:** These expand the existing 0–10 Morale scale with behavioral triggers at specific values.

| Morale | Stage | New Behavioral Trigger |
|--------|-------|----------------------|
| 10 | Blazing | Companions volunteer for dangerous tasks without being asked. One offers a personal item as a gift. |
| 8–9 | High | Companions offer tactical suggestions before combat ("I could flank left if you draw them out"). |
| 6–7 | Steady | Normal behavior. No additional triggers. |
| 4–5 | Low | Companions question risky orders once before complying. Watch shifts have awkward silences. |
| 2–3 | Fractured | One companion per rest refuses a camp activity ("I'm not in the mood"). Banter stops. |
| 1 | Near-Broken | Companions voice doubt about the mission. One threatens to leave if things don't improve. |
| 0 | Broken | Fracture Scene fires (existing rule). Add: one companion refuses to enter the next combat encounter. |

### Vanguard / Rearguard Morale Split
When the party splits into vanguard and rearguard (KM_Combat_Systems.md), track morale separately:
- **Vanguard morale** = base party_morale + modifiers from combat outcomes experienced by vanguard
- **Rearguard morale** = base party_morale + modifiers from rearguard-specific events
- Morale **reunifies** when groups rejoin: average of both, rounded down
- Save block: `"vanguard_morale": null, "rearguard_morale": null` (null when party is together)

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Living World Systems v2.0*
*Systems: Party Morale Track, Companion Mood States, Bond History Log, Disposition Tags, Morale Expansion*


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — WEATHER HAZARDS & CAMPING ACTIVITIES
## KM_Kingdom.md | Referenced by: KM_Exploration.md

---

> **DM:** This file covers two systems from the Kingmaker Companion Guide. **Weather Hazards** are full stat-block events that replace the basic weather table in KM_Exploration.md when a weather event is triggered. **Camping Activities** are the complete rules for what characters can do at camp each session. Both systems are optional depth layers — run the basic tables in KM_Exploration.md for quick play, use these for detailed wilderness sessions.

---

## 🌦️ DAILY WEATHER PROCEDURE

```
Each morning during daily preparations, resolve in order:

STEP 1 — PRECIPITATION
  Flat check DC (by season):
    Summer: DC 20   |   Spring/Autumn: DC 15   |   Winter: DC 8
  Success: light rain (or snow if winter cold snap is active)
  Effect: −1 to visual Perception checks; overland fatigue threshold 4 hrs (not 8)

STEP 2 — TEMPERATURE (Winter only)
  Flat check DC:
    Kuthona or Calistril (deep winter): DC 18
    Abadius (mid-winter): DC 16
  Success: cold snap — fatigue after 4 hrs activity; light precipitation becomes snow

STEP 3 — WEATHER EVENT
  Flat check DC 17
  Success: roll d20 on the Random Weather Events table below
  Natural 20 on flat check: roll again for possible second event (secondary thematically linked)
  If rolled event level exceeds party level + 4: reroll
```

### Random Weather Events Table

| d20 | Event | Hazard Level |
|-----|-------|-------------|
| 1–3 | Fog | 0 |
| 4–7 | Heavy Downpour | 0 |
| 8–9 | Cold Snap | 1 |
| 10–12 | Windstorm | 1 |
| 13 | Hailstorm (severe) | 2 |
| 14 | Blizzard | 6 |
| 15 | Supernatural Storm | 6+ |
| 16 | Flash Flood | 7 |
| 17 | Wildfire | 4 or 10 |
| 18 | Subsidence | 5 or 12 |
| 19 | Thunderstorm | 7 or 13 |
| 20 | Tornado | 12 or 17 |

**Weather XP:** Equal to a simple hazard of the event's level. Awarded whether the party endures, avoids, or shelters — not awarded if they shelter in a total-protection structure.

**Predict Weather (Feat 2 — Uncommon General Skill):**
Prerequisites: trained in Survival. Spend 10 min outdoors; attempt DC 20 Survival (DC 15 with commanding view; DC 30 with impaired visibility).
- **Critical Success:** Know precipitation, temperature, wind, and exact weather event (type + timing). +2 to Survival checks to prepare.
- **Success:** Know precipitation, temperature, wind. Know if event occurs but not what/when. +1 to prepare checks.
- **Critical Failure:** GM gives false critical-success info.

---

## ⛈️ WEATHER HAZARD STAT BLOCKS

### FOG — Hazard 0
**Environmental**
*Survival DC 12 (trained) to notice within 1 hour*
**Prepare:** Survival DC 12 — find high ground or landmark to navigate by.
**Routine (4 hours+):** Concealed condition for all creatures. −4 to visual Perception. Characters who Stride more than 30 ft must succeed DC 12 Survival or become lost (off course by 1d4 × 10 ft per hour). Fog disperses on its own after 4 hours or with any significant wind.

---

### HEAVY DOWNPOUR — Hazard 0
**Environmental**
*Survival DC 12 (trained)*
**Prepare:** Survival DC 12 — find or construct shelter.
**Routine (3 hours):** Difficult terrain in open areas. −2 to visual Perception and ranged attack rolls. Unprotected fire extinguished. Tracking impossible. Overland fatigue threshold 4 hrs. Flat check DC 11 to continue — on success, downpour continues another 3 hours.

---

### COLD SNAP — Hazard 1
**Environmental**
*Survival DC 14 (trained)*
**Prepare:** Survival DC 14 — layer clothing and build insulated shelter.
**Requirements:** Winter season.
**Routine (8 hours):** Mild cold environment (Core Rulebook 517). Characters without cold-weather gear must succeed DC 13 Fortitude each hour or become fatigued. Fatigue threshold 2 hours. Water sources may freeze (Survival DC 14 to find unfrozen water).

---

### WINDSTORM — Hazard 1
**Environmental**
*Survival DC 15 (trained)*
**Prepare:** Survival DC 15 — find shelter and secure equipment.
**Routine (2 hours+):** Ranged attacks at −2; ranged attacks beyond 30 ft at −4. Flying creatures must succeed DC 16 Athletics or be pushed back 10 ft. Open flames extinguished. Tents and light structures may be damaged (flat check DC 13 per hour; fail = structure damaged). Flat check DC 11 to continue each 2 hours.

---

### HAILSTORM (SEVERE) — Hazard 2
**Environmental**
*Survival DC 16 (trained)*
**Prepare:** Survival DC 16 — find overhead cover.
**Requirements:** Cold temperatures (spring, autumn, or winter).
**Routine (1 hour):** 2d6 bludgeoning damage to unprotected creatures each 10 minutes (DC 16 basic Fortitude halves). −4 to visual Perception. Difficult terrain outdoors. Light structures take 1d6 damage per 10 minutes.

---

### BLIZZARD — Hazard 6
**Environmental**
*Survival DC 22 (expert)*
**Prepare:** Survival DC 22 — construct or reach substantial shelter.
**Requirements:** Winter season.
**Routine (6 hours):** Blinded condition outdoors. All terrain is difficult and hazardous terrain. Exposed creatures must succeed DC 20 Fortitude each hour or gain fatigued (+1 each failure). Navigation impossible without landmarks. Shelter reduces all effects to Cold Snap level. Flat check DC 11 each 6 hours to continue.
**Escalation (Supernatural Blizzard):** As Blizzard but includes Supernatural Storm effects.

---

### SUPERNATURAL STORM — Hazard 6+
**Environmental · Magical**
*Survival DC 22 (expert) or Occultism DC 20*
**Prepare:** Survival DC 22 (find shelter) or Occultism DC 20 (identify nature + reduce effects).
**Requirements:** Near First World bleed-through zones (Narlmarches, Thousand Voices, any hex with fey activity).
**Routine (4 hours):** All Blizzard effects, plus: random magical effects each hour (roll d6: 1 — enlarge or shrink a creature for 1 hour; 2 — random colors; 3 — one character polymorphed into fey creature for 10 min; 4 — spontaneous plant growth creates hazardous terrain; 5 — Nyrissa's laughter on the wind, all Perception −2; 6 — no effect). Spell DCs in the area +1.

---

### FLASH FLOOD — Hazard 7
**Environmental**
*Survival DC 23 (expert)*
**Prepare:** Survival DC 23 — reach high ground (20+ ft elevation).
**Requirements:** Near river, stream, or low-lying area. Most dangerous in Greenbelt, Tuskwater, Hooktongue zones.
**Routine (Immediate onset):** All creatures in low-lying area must succeed DC 22 Reflex or be swept 30 ft downstream, taking 4d6 bludgeoning. Each round in water: DC 20 Athletics or take 2d6 bludgeoning and be pushed another 20 ft. Difficult terrain in shallow flood; Swimming required in deep flood. Flood subsides after 1 hour. Kills campfires; may destroy unanchored equipment.

---

### WILDFIRE — Hazard 4 (forest) or 10 (dry plains)
**Environmental**
*Survival DC 20/26 (trained/expert by tier)*
**Prepare:** Survival DC 20/26 — identify wind direction, create firebreak, flee upwind.
**Requirements:** Forest (level 4) or dry grassland in summer (level 10).
**Routine:** Fire spreads 1d4 × 10 ft per round downwind. Creatures in fire: 2d6/4d8 fire damage per round (DC 20/26 basic Reflex). Smoke: concealed within 60 ft, creatures without smoke protection must succeed DC 16 Fortitude each minute or become sickened 1. Fire suppression: DC 20 Athletics to beat out (5-ft patch per success).

---

### SUBSIDENCE — Hazard 5 (minor) or 12 (major)
**Environmental**
*Survival DC 21/28 (trained/expert)*
**Prepare:** Survival DC 21/28 — spot unstable ground, route around.
**Requirements:** Boggy or unstable terrain (Hooktongue, Sorrow Marshes, areas with recent heavy rain).
**Routine:** Ground collapses under a creature. Minor: DC 19 Reflex or fall 10 ft (2d6 bludgeoning), difficult terrain. Major: DC 25 Reflex or fall into sinkhole (4d6 bludgeoning, restrained — DC 22 Athletics to escape each round).

---

### THUNDERSTORM — Hazard 7 (standard) or 13 (severe)
**Environmental**
*Survival DC 23/29 (expert)*
**Prepare:** Survival DC 23/29 — avoid tall objects and open ground.
**Routine (2 hours+):** Heavy downpour effects (see above). Lightning: each 10 minutes outdoors, one random creature must succeed DC 22/28 basic Reflex or take 6d12/10d12 electricity damage. Metal armor doubles as a lightning rod — wearer is targeted first. Shelter negates lightning risk. Flat check DC 11 each 2 hours to continue.

---

### TORNADO — Hazard 12 (distant) or 17 (direct path)
**Environmental**
*Survival DC 28/34 (expert/master)*
**Prepare:** Survival DC 28/34 — find underground shelter or low depression.
**Requirements:** Open plains or grasslands. Spring/summer most common.
**Routine:** Creatures outdoors within 1 mile of path must succeed DC 26 Fortitude or be knocked prone. Creatures within 300 ft: DC 28 Fortitude or be lifted (flying speed 60 ft, uncontrolled) taking 6d6 bludgeoning per round. Structures take 10d10 bludgeoning per round. Only underground or stone shelter provides full protection.

---

## 🏕️ CAMPING ACTIVITIES

```
CAMPING SESSION STRUCTURE
  Step 1 — Make Camp:       Prepare Campsite activity (1 hr, or 30 min if returning to used site)
  Step 2 — Activities:      Each character chooses 1 Camping activity
  Step 3 — Eating:          Characters eat their meal for the session
  Step 4 — Rest:            8-hour rest; recover HP, spell slots, focus points
  Step 5 — Daily Prep:      30-minute daily preparations; zone Encounter DC resets

Zone Encounter DC: varies by zone level (see KM_Exploration.md encounter tables)
  Low zones (1–3): DC 16   |   Mid zones (4–7): DC 18   |   High zones (8–12): DC 20
  Dangerous zones (13+): DC 22
```

### Core Camping Activities

**PREPARE CAMPSITE** *(required first activity)*
*Camping, Manipulate*
Spend 1 hour (30 min for previously used campsite). Attempt Survival vs zone DC.
- **Crit Success:** Zone Encounter DC +2 for session; party recovers +1d8 additional HP when resting.
- **Success:** Functional campsite established. Can proceed with other activities.
- **Failure:** Camp is established but uncomfortable; all Camping activities this session at −2.
- **Crit Failure:** Poorly chosen site. Zone Encounter DC −2 for session.

---

**CAMOUFLAGE CAMPSITE**
*Camping, Manipulate, Secret | Req: trained in Stealth*
Spend 1 hour hiding the camp. Attempt Stealth vs zone DC. Only once per session.
- **Crit Success:** Zone Encounter DC +2; first flat check that would trigger encounter is treated as a failure instead.
- **Success:** Zone Encounter DC +1.
- **Crit Failure:** Zone Encounter DC −2; flat checks on 19–20 also trigger encounters.

---

**COOK BASIC MEAL**
*Camping, Manipulate*
Spend 2 hours. Expend 2 basic ingredients + 1 day's rations per serving.
Attempt Survival DC 22 or Cooking Lore DC 18.
- **Crit Success:** Eating character recovers HP equal to Con mod × (level × 2) during rest instead of normal. +1 status to all saves until next daily prep.
- **Success:** +1 status bonus to all saves until next daily prep.
- **Failure:** Meal fills bellies, no other effect.
- **Crit Failure:** Sickened 1 until after rest and daily prep.

---

**COOK SPECIAL MEAL**
*Camping, Manipulate | Req: knowledge of the recipe*
Spend 2 hours. Expend basic + special ingredients per recipe. Attempt recipe's Cooking Lore DC.
Can be attempted multiple times per session using different recipes. Sickened characters cannot benefit.
Results vary by recipe (see recipes below).

---

**DISCOVER SPECIAL MEAL**
*Camping, Manipulate | Req: trained in Cooking Lore*
Spend 2 hours. Choose a common recipe ≤ zone level. Expend twice normal ingredients. Attempt recipe's Cooking Lore DC.
- **Crit Success:** Learn the recipe; recover half expended ingredients.
- **Success:** Learn the recipe.
- **Failure:** Ingredients lost; no recipe learned.
- **Crit Failure:** Ingredients lost; suffer critical failure effect from unwise taste test.

---

**HUNT AND GATHER**
*Camping, Move*
Spend 2 hours ranging the area. Attempt Survival vs zone DC.
- **Crit Success:** 2d4 basic ingredients + 1 special ingredient.
- **Success:** 2d4 basic ingredients.
- **Failure:** 1d4 basic ingredients.
- **Crit Failure:** No ingredients; may trigger an encounter (GM's discretion).

---

**ORGANIZE WATCH**
*Camping, Concentrate*
Spend 1 hour organizing the night watch schedule. Attempt Perception vs zone DC.
- **Crit Success:** No flat checks for encounters during rest; automatic notice of any approach.
- **Success:** Flat checks for rest encounters made at +2.
- **Failure:** Normal flat checks.
- **Crit Failure:** First watch rotation: one random watcher falls asleep; Encounter DC −2 during that period.

---

**PROVIDE AID**
*Camping, Manipulate*
Spend 1 hour assisting another character's recovery. Attempt Medicine DC 15.
- **Crit Success:** Target recovers additional HP equal to your Medicine modifier × 2 during rest.
- **Success:** Target recovers additional HP equal to your Medicine modifier.
- **Failure:** No effect.
- **Crit Failure:** Target's rest is disturbed; recovers 2 fewer HP per die.

---

**TELL CAMPFIRE STORY**
*Camping, Concentrate*
Spend 1 hour telling a story of past victory. Attempt Performance vs zone DC.
- **Crit Success:** All allies gain a +1 status bonus to saves vs fear for the next day.
- **Success:** Morale lifted; one ally of your choice gains a +1 status bonus to initiative for the next day.
- **Failure:** Enjoyable but no mechanical benefit.

---

**RELAX**
*Camping*
Rest without performing other activities. Recover an additional Focus Point (if you have a focus pool) and remove the fatigued condition if present.

---

**SET ALARMS**
*Camping, Manipulate | Req: trained in Crafting or Survival*
Spend 1 hour setting tripwires, snares, or noise-makers. Attempt Crafting or Survival DC 18.
- **Crit Success:** Zone Encounter DC +2; first encounter this session: initiative +4 for whole party.
- **Success:** Zone Encounter DC +1.
- **Failure:** No effect; materials used.

---

**BLEND INTO THE NIGHT** *(Harrim — req: trained in Religion, worships Groetus)*
*Camping, Concentrate*
Harrim meditates on the void. Attempt Religion vs zone DC.
- **Crit Success:** Party is treated as if underground; all visual Perception checks vs the party at −4.
- **Success:** Zone Encounter DC +1 for rest period.

---

**BOLSTER CONFIDENCE** *(Linzi — req: expert in Performance)*
*Camping, Concentrate*
Linzi performs an uplifting tale. Attempt Performance DC 20.
- **Success:** One ally removes the frightened or rattled condition and gains +1 morale to saves vs fear next day.
- **Crit Success:** All allies gain the above benefit.

---

**CAMP MANAGEMENT** *(Jubilost — req: expert in Survival)*
*Camping, Concentrate*
Jubilost optimizes camp logistics. Attempt Survival DC 20.
- **Crit Success:** Daily preparations take 15 min instead of 30; zone Encounter DC +1.
- **Success:** Daily preparations take 15 min instead of 30.

---

**ENHANCE CAMPFIRE** *(Kanerah — req: any)*
*Camping, Concentration*
Kanerah infuses the campfire with elemental warmth. No check required.
Effect: Cold snap and blizzard effects are negated for the camp. Party recovers +1 HP per level during rest. Lasts until camp is broken.

---

**ENHANCE WEAPONS** *(Amiri — req: any)*
*Camping, Manipulate*
Amiri teaches weapon maintenance. Attempt Athletics DC 18.
- **Success:** Up to 4 party weapons deal +1 damage for the next day (once per session).
- **Crit Success:** All party weapons +1 damage for next day.

---

**RULING WITH [COMPANION]** — Kingdom Activity (once per Kingdom Turn)
Each companion with a "Ruling With" entry unlocks a special Kingdom Activity when they hold a Leadership role. See KM_Kingdom.md for their assigned roles.

| Companion | Activity | Effect |
|-----------|----------|--------|
| Harrim | Evangelize the End | Spend 1 RP → convert Unrest to Stability (+1) |
| Jaethal | Decadent Feasts | Spend 2 RP → Fame +1, Loyalty +1, Crime +1 |
| Kalikke | Deliberate Planning | Reroll one failed kingdom skill check (1/turn) |
| Regongar | Show of Force | Loyalty +2, Stability +1 — Unrest +1 |
| Linzi | Read All About It | Print propaganda — +2 to next Diplomatic Envoy |

---

## 🍽️ SPECIAL MEAL RECIPES

> **DM:** Recipes are found during play (quest rewards, vendor purchases, Discover Special Meal). Common recipes are available via Discover Special Meal at appropriate zone levels.

| Recipe | Level | Ingredient | Cook DC | Success Effect | Crit Success |
|--------|-------|------------|---------|----------------|--------------|
| Moon Radish Soup | 1 | Moon radishes ×2 | Cooking Lore 15 | +1 Fortitude saves all day | +1 Fortitude + recover Con mod × level extra HP |
| Fey Pepper Stew | 2 | Fey pepper ×1 | Cooking Lore 16 | +1 Reflex saves all day | +1 Reflex + ignore difficult terrain 1 hr |
| Aged Tatzlwyrm | 3 | Tatzlwyrm meat ×1 | Cooking Lore 18 | +1 Will saves all day | +1 Will + +2 vs fear all day |
| Swamp Witch's Brew | 4 | Rattlecaps ×1 + Toadstool ×1 | Cooking Lore 20 | +1 spell attack/DC all day | +1 spell attack/DC + +1 Focus Point (recoverable) |
| Owlbear Egg Scramble | 5 | Owlbear egg ×1 | Cooking Lore 22 | +1 Perception all day | +2 Perception + low-light vision until next camp |
| Nymph's Delight | 6 | Fey honey ×1 + cloudberries ×2 | Cooking Lore 24 | Recover 2 extra HP per die during rest | Recover 2 extra HP per die + remove one condition |
| Kellid Trail Ration | 7 | Dried meat ×3 | Cooking Lore 25 | No fatigue from overland travel next day | Above + Speed +10 ft for day |
| Baked Spider Legs | 8 | Giant spider ×2 | Cooking Lore 26 | +2 Stealth all day | +2 Stealth + ignore darkness concealment for 1 hr |
| Hearty Purple Soup | 9 | Purple mushroom ×2 | Cooking Lore 28 | +10 temporary HP at start of day | +15 temp HP + fast healing 1 for 1 hr after each combat |

---

## 🌙 NIGHTTIME DANGER SCALING

> **DM:** Time of day affects encounter difficulty and skill checks. Track day/night cycle during exploration. Default: sunrise 6:00, sunset 18:00. Adjust by season (KM_Kingdom.md calendar).

### Night Modifiers (sunset to sunrise)

| Category | Modifier | Notes |
|----------|----------|-------|
| **Encounter Level** | +1 effective creature level | Nocturnal predators, undead, bandits with night advantage |
| **Visual Perception** | −2 circumstance penalty | Does NOT apply to: Darkvision, creatures with low-light vision in dim light |
| **Stealth approaches** | +2 circumstance bonus | Darkness helps ambushers and sneakers equally |
| **Ambush DC** | −2 to detect ambush | Combined with Perception penalty = dangerous |
| **Navigation** | Survival DC +2 to avoid getting lost | Familiar hexes exempt |
| **Random encounter chance** | +10% (roll d100, add 10 to encounter threshold) | More creatures hunt at night |

### Camping at Night
- **Watch system unchanged** — Organize Watch activity uses flat checks as normal
- **Night attack on camp:** If random encounter fires during rest, party is Surprised (flat-footed, no weapons drawn) unless watch succeeds on DC 14 Perception
- **Campfire visibility:** A lit campfire is visible 300 ft in darkness. Increases random encounter chance by +5% but provides light (negates Perception penalty within 30 ft)
- **No campfire:** −5% encounter chance but all camp activities requiring light take −2

### Dawn/Dusk (1 hour each)
- **Dim light conditions** — low-light vision works normally, standard vision at −1 Perception
- **No encounter level modifier** — transitional period
- **Best time to break camp or approach a target** — experienced adventurers know this

### Player Choice Point
When the party is traveling and sunset approaches, present:
```
The sun is low. Shadows lengthen across the trail.
 1. Make camp here before dark
 2. Push on — travel through the night  [Fatigue risk: Fort DC 12 or Fatigued]
 3. Travel until full dark, then camp  [1-2 hours of night travel]
```

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Weather Hazards & Camping Activities v2.0*


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — ADVISOR EVENTS & POLITICAL INTRIGUE
## KM_Kingdom.md | Active from: Chapter 2 | Referenced by: KM_Kingdom.md

> **DM:** Load during Kingdom Turns. Each kingdom event now has 2–3 advisor-championed solutions. The player hears each advisor's pitch, then chooses. Choosing an advisor's solution: +1 relationship with that advisor, variable kingdom stat outcomes. Advisors with conflicting interests may sabotage each other's projects (Intrigue system, bottom of file). Use the Debate system (KM_Mythic_Systems.md) if the player wants advisors to argue it out.

---

## 📋 ADVISOR EVENT FORMAT

```
[KINGDOM EVENT — {Event Name}]
{Description of the problem}

ADVISOR SOLUTIONS:
 A. {Advisor Name} ({Role}): "{Their pitch in 1-2 sentences}"
    → Effect: {Kingdom stat changes}
    → Cost: {RP or resource cost}
    → Risk: {What could go wrong}

 B. {Advisor Name} ({Role}): "{Their pitch}"
    → Effect: {Stats}
    → Cost: {Cost}
    → Risk: {Risk}

 C. Player's own solution (describe)
    → DM adjudicates based on skills and resources

Choose A, B, or C. Or use .debate to have the advisors argue.
```

---

## 🏛️ ADVISOR EVENTS — CHAPTER 2

### Event A2-1: The Bandit Resurgence
*Stag Lord loyalists regroup in the Narlmarches. Scouts report a new camp.*

**Councilor:** *"Amnesty. Offer pardons for any who lay down arms before the next moon. Most of these people are desperate farmers, not soldiers."*
→ Loyalty +2, Stability −1. 60% of bandits accept. Remainder hardens.

**General:** *"Send the army. Crush the camp before they organize. Every day we wait, they recruit."*
→ Stability +2, Loyalty −1. Camp destroyed. 1d4 prisoners for interrogation. RP cost: 4.

**Marshal:** *"Blockade. Cut their supply lines. They starve out in two turns without a fight."*
→ Economy −1 (trade disruption), Stability +1. Slow but bloodless. Bandits scatter.

---

### Event A2-2: The Trade Road Dispute
*Two merchant guilds claim exclusive rights to the kingdom's main trade road.*

**Treasurer:** *"Grant the contract to the Restov guild. They pay more and we need the revenue."*
→ Economy +3. Restov faction +1. Local merchants: Reputation −1.

**Councilor:** *"Split the road. Half to each guild. Nobody wins everything, nobody loses everything."*
→ Economy +1, Loyalty +1. Both guilds mildly annoyed. Stable compromise.

**Grand Diplomat:** *"Use this as leverage. Neither guild gets exclusivity — we open the road to all comers and take a crown toll."*
→ Economy +2, Stability +1. Both guilds: faction −1. Commoners: Reputation +1 (lower prices).

---

### Event A2-3: The Temple Petition
*A religious order requests land and tax exemption to build a temple in the capital.*

**High Priest:** *"Grant it. Divine favor brings pilgrims, tithes, and healers. The kingdom needs all three."*
→ Culture +2, Stability +1. Free Temple building (saves 8 RP). High Priest: +1 relationship.

**Treasurer:** *"Tax exemption for a building that generates income? Absolutely not. They can build, but they pay like everyone else."*
→ Economy +1. Clergy faction −1. Commoners neutral.

**Spymaster:** *"Let them build. But I want an observer inside. Religious orders collect secrets along with tithes."*
→ Culture +1, Stability +1. Spymaster network: +1 agent. Clergy faction −1 if discovered (25% chance per turn).

---

### Event A2-4: The Hex Dispute
*Two settlements both claim the same cleared hex for farmland expansion.*

**Councilor:** *"The hamlet that cleared it gets priority. First labor, first claim."*
→ Loyalty +1 in winning hamlet. Loyalty −1 in losing hamlet.

**Warden:** *"Neither. That hex is strategically important — build a fortification, not farms."*
→ Stability +2. Both hamlets: Loyalty −1. Hex becomes eligible for fortification (KM_Kingdom.md).

**Ruler (player):** Can propose a third option. DM adjudicates with appropriate skill check.

---

## 🏛️ ADVISOR EVENTS — CHAPTER 3

### Event A3-1: The Troll Refugees
*Troll Trouble aftermath: displaced trolls seek territory in your borderlands.*

**General:** *"Trolls don't negotiate. Patrol the borders. Kill any that cross."*
→ Stability +2. Kellid faction +1. Culture −1 (brutal reputation). RP cost: 2/turn (patrols).

**Grand Diplomat:** *"Designate a wilderness hex as troll territory. Formal border. They stay out, we stay out."*
→ Stability +1, Loyalty +1. Kellid faction −1 ("You gave land to trolls?"). Saves RP long-term.

**High Priest:** *"The trolls are creatures of the wild. The druids can mediate. Let Jhod try."*
→ Culture +2 if Jhod succeeds (70%). Stability −1 if he fails (30%). No RP cost.

---

### Event A3-2: The Festival Question
*The capital is large enough for an annual festival. What kind?*

**Councilor:** *"A harvest festival. Food, drink, games. The people need joy."*
→ Loyalty +3, Culture +1, Economy −2 (festival costs). Reputation +1 in capital.

**Treasurer:** *"A trade fair. Invite merchants from Restov and the River Kingdoms."*
→ Economy +4, Culture +1. Faction +1 with trade partners. Loyalty +0 (merchants aren't fun).

**Magister:** *"An arcane symposium. Attract scholars and mages. The kingdom needs intellectual depth."*
→ Culture +3, Economy +1. Scholarly NPCs arrive (side quests). Commoners confused (Loyalty +0).

---

### Event A3-3: The Spy Report
*Spymaster reports Pitax has agents in the capital. Three suspects identified.*

**Spymaster:** *"Let me handle this quietly. Arrests, interrogation, expulsion. Nobody needs to know."*
→ Stability +2. Pitax faction −1. 100% success but −1 Loyalty if methods leak (20% chance).

**Marshal:** *"Public arrests. Show everyone that spies face justice."*
→ Loyalty +2 (deterrence), Stability +1. Pitax faction −2 (humiliated). Agents may warn others (50% of remaining network escapes).

**Grand Diplomat:** *"Turn them. Feed false information back to Pitax. A spy you know about is an asset."*
→ Stability +1. Pitax faction unchanged. Long-term: +2 to next Pitax-related intelligence check. 30% chance the double-agent is a triple-agent.

---

### Event A3-4: The Dwarven Miners
*A dwarven mining company offers to set up operations in a resource-rich hex — but they want autonomy.*

**Treasurer:** *"Their operation will triple our ore output. Give them the hex. We tax the output, not the process."*
→ Economy +3, Ore +2/turn. Dwarven faction +1. Loyalty −1 (citizens see foreign control over domestic land).

**Warden:** *"Our miners, our hex, our rules. Offer them contracts, not territory."*
→ Economy +1, Ore +1/turn. Loyalty +1. Dwarven faction −1 (insulted). Slower but sovereign.

**Councilor:** *"Joint venture. They run the mine, we staff it with our people. Both sides learn."*
→ Economy +2, Ore +1/turn, Culture +1. Dwarven faction +0 (acceptable). Build time: 2 turns.

---

### Event A3-5: The River Toll
*A bridge connecting two settlements needs repair. Who pays — the settlements or the crown?*

**Treasurer:** *"Toll bridge. Users pay for repairs. Self-sustaining infrastructure."*
→ Economy +2. Loyalty −1 in both settlements. Trade volume: −10% on that route.

**Councilor:** *"Crown pays. It's our bridge, our kingdom, our responsibility."*
→ Loyalty +2 in both settlements. Economy −2 (repair costs). Reputation +1.

**Marshal:** *"Military priority. Repair it, fortify it, and station guards. Bridges are chokepoints."*
→ Stability +2. Economy −1. Bridge becomes defensible position (KM_Kingdom.md bonus).

---

## 🏛️ ADVISOR EVENTS — CHAPTER 4

### Event A4-1: The Barbarian Alliance
*Tiger Lord scouts approach under flag of truce. They offer non-aggression — for a price.*

**General:** *"It's a trap. The Tiger Lords don't negotiate — they stall while they recruit. Reject and reinforce."*
→ Stability +2. Kellid faction −2. Tiger Lords attack 1 turn sooner. Army preparation: +1 Morale.

**Grand Diplomat:** *"Accept the truce. Buy time. We're not ready for a two-front war."*
→ Stability +1, Economy +1 (no war spending). Kellid faction +1. Tiger Lords delay attack 2 turns. Risk: they use the time too.

**Spymaster:** *"Accept publicly. Use the truce to infiltrate their camp. When the truce breaks, we know their numbers."*
→ Stability +1. Spymaster network: full Tiger Lord army intelligence. 20% chance they detect the spy (truce breaks immediately, faction −3).

---

### Event A4-2: The Refugee Wave
*War with the Tiger Lords displaces hundreds of Kellid civilians. They arrive at your borders.*

**Councilor:** *"Open the gates. These are people, not threats. Feed them, house them, make them citizens."*
→ Loyalty +3, Culture +1. Economy −3 (feeding costs). Population +500. Some refugees have useful skills (1 free building worker).

**Marshal:** *"Screen them first. Tiger Lord spies will be mixed in. Process, then admit."*
→ Stability +2, Loyalty +1. Economy −1 (processing costs). Spymaster detects 1d4 embedded spies.

**Treasurer:** *"We can't afford this. Redirect them to Restov. Brevoy has resources we don't."*
→ Economy stable. Loyalty −2 (cold). Kellid faction −2. Reputation −1. Restov faction +1 (they appreciate the warning).

---

### Event A4-3: The War Profiteers
*Arms dealers offer bulk weapon sales at inflated prices. Your army needs equipment.*

**Treasurer:** *"Haggle. We buy half now at their price, half later at ours, or we commission locally."*
→ Army gets half equipment now. Economy −2. Local smiths begin production (full equipment in 2 turns).

**General:** *"Pay the price. Men die while we negotiate. Equipment now saves lives."*
→ Army fully equipped. Economy −4. Morale +2. General: +1 relationship.

**Magister:** *"Let me examine their stock. I suspect some of these weapons are enchanted — badly. Cursed, even."*
→ Arcana DC 16 check. Success: 30% of stock is cursed — saved the army. Failure: bought cursed weapons, 1 army unit takes −1 Morale.

---

### Event A4-4: The Coronation Debate
*Jamandi and Natala Surtova pressure you to formalize your political alignment before the war.*

**Grand Diplomat:** *"Delay. Neither side gets a commitment until the war is won. We need both."*
→ Both factions: −1. Independence maintained. No alliance bonus but no obligation.

**Councilor:** *"The people should choose. Hold a public declaration ceremony. Let the kingdom decide its identity."*
→ Loyalty +3, Culture +2. Player chooses alignment publicly — all consequences transparent. +1 Blunt disposition.

**Spymaster:** *"Promise both. Privately. When the war ends, we choose the winner."*
→ Both factions: +1 (temporarily). Stability +1. Risk: if discovered (30% per chapter), both factions −3. +1 Cunning disposition.

---

## 🏛️ ADVISOR EVENTS — CHAPTER 5

### Event A5-1: The Pitax Ultimatum
*Irovetti sends a formal demand: surrender the Stolen Lands or face invasion.*

**General:** *"This is not a negotiation. This is a declaration. Mobilize everything."*
→ All armies activated. Stability +2. Economy −3 (war footing). War begins formally.

**Grand Diplomat:** *"Respond with a counter-proposal. We don't want war — but we don't bend either."*
→ Delay Pitax invasion by 1 turn. Diplomacy DC 20. Success: Pitax faction +1, delay 2 turns. Failure: Irovetti insulted, invasion accelerated.

**Spymaster:** *"Ignore the letter. Send assassins. Cut the head off the snake."*
→ Assassination attempt: 40% success. Success: Pitax army in disarray (−3 Morale all units, invasion delayed 3 turns). Failure: Spymaster agent captured, Pitax propaganda victory (Reputation −2).

---

### Event A5-2: The Supply Chain
*War stretches supply lines. Settlements closest to the front are running low.*

**Treasurer:** *"Ration distribution. Central control. Nobody starves, but nobody feasts."*
→ Economy stable. Loyalty −1 (rationing is unpopular). Stability +1. Food commodity: −2/turn but controlled.

**Warden:** *"Local foraging. My rangers can supplement supplies from the wilderness."*
→ Warden Survival DC 16. Success: Food +2/turn, no cost. Failure: rangers encounter enemy scouts, 1d4 casualties.

**Councilor:** *"Ask the people. Volunteer kitchens, community sharing. Make it a cause, not a burden."*
→ Loyalty +2 (community spirit). Food −1/turn (less efficient). Reputation +1. Morale +1 (everyone contributes).

---

### Event A5-3: The Mercenary Company
*A mercenary company offers their services. Professional, expensive, morally flexible.*

**General:** *"Hire them. Our army is stretched thin. Professional soldiers fill the gap."*
→ +1 army unit (Mercenary Company: Off +6, Def 15, Morale 10). Cost: 6 RP/turn. Mercenaries fight well but may loot settlements if unpaid.

**Treasurer:** *"Too expensive. That gold builds fortifications that last longer than hired swords."*
→ No mercenaries. 6 RP invested in fortifications instead: +1 to all hex defense bonuses.

**Marshal:** *"Hire them but assign them to the front line. If they prove loyal, integrate. If not, they absorb the first casualties."*
→ Mercenaries hired at 4 RP/turn (front-line discount). If first battle goes well: Mercenary Morale +2 (they respect competence). If badly: they desert.

---

### Event A5-4: The Siege Preparation
*Intelligence says Pitax will siege the capital within 2 turns.*

**General:** *"Defensive positions. Every building is a strongpoint. Every citizen who can hold a spear gets one."*
→ Capital defense: +4. Militia mobilized (1 temporary army unit, weak but present). Culture −1 (militarization).

**Magister:** *"I can ward the walls. Arcane defenses — detection, shields, counterspells at the gates."*
→ Capital defense: +2 vs magical attacks. Enemy casters: −2 to spell DCs within walls. Cost: 4 RP + Magister unavailable for 1 turn.

**Spymaster:** *"Let me evacuate the non-combatants. If they siege, I want civilians out of the crossfire."*
→ Civilians evacuated. If siege occurs: no civilian casualties. Loyalty +2 (they remember). Economy −1 (disruption). If siege doesn't occur: wasted effort but goodwill earned.

---

## 🏛️ ADVISOR EVENTS — CHAPTER 6

### Event A6-1: The Bloom Ultimatum
*Nyrissa's Bloom is consuming hexes. Three settlements are in its path.*

**Warden:** *"We can't fight the Bloom with swords. Druids and nature magic. Slow it down, buy time."*
→ Bloom advance: −1 hex per turn (slowed). Warden and druids committed for 2 turns. Nature DC 18 per turn to maintain.

**General:** *"Evacuate the settlements. Save the people. We can rebuild later."*
→ Settlements abandoned. Population relocated (Loyalty +1 — people saved). Economy −2 (lost infrastructure). 3 hexes lost to Bloom.

**High Priest:** *"The Bloom is fey corruption. Divine cleansing — coordinated prayer, holy ground, consecration."*
→ Culture +2 if Bloom is slowed. 50% chance per hex of full cleansing. Failure: Bloom accelerates in that hex (+1 hex consumed). Clergy committed for 3 turns.

---

### Event A6-2: The Final Alliance
*Before the final confrontation, choose who stands with you.*

**Grand Diplomat:** *"Call in every favor. Every faction we've helped. This is what alliances are for."*
→ Every faction at Honored+ sends 1 army unit. Total allies = number of factions at Honored or above.

**General:** *"Our army alone. Allies complicate command structure. We trained for this."*
→ Player armies only. +2 Morale (unity). +1 Offense (no coordination overhead). Fewer total troops.

**Councilor:** *"The people themselves. Arm the citizens. Everyone fights."*
→ Militia army units from every settlement (weak: Off +2, Def 12, Morale 8). Many units but fragile. Loyalty +3 (the kingdom fights as one).

---

### Event A6-3: The Nyrissa Question
*If nyrissa_backstory_known ≥ 2, advisors debate what to do about Nyrissa herself.*

**High Priest:** *"She is the source. Destroy her. End the Bloom at its root."*
→ Standard final battle path. Nyrissa destroyed. Bloom ends.

**Grand Diplomat:** *"She was cursed, not born evil. If there's a way to save her, we should try."*
→ True Ending path remains open. +1 Merciful disposition. Requires: nyrissa_saveable flags to complete.

**Spymaster:** *"Neither destroy nor save. Bind her. Use the Bloom as a weapon against our enemies, then contain it."*
→ Dark path. Bloom becomes a kingdom weapon for 1 chapter. Economy +5, Stability −3. Nyrissa: permanently hostile. Lantern King: amused (not good). Unique dark ending flag set.

---

## 🗡️ ADVISOR INTRIGUE SYSTEM

> **DM:** Advisors with opposing goals occasionally sabotage each other's projects. This runs in the background. The player notices when a project underperforms. The Spymaster can detect intrigue. Detecting and confronting an intriguing advisor is a choice point.

### Intrigue Trigger
- **Two advisors with opposing priorities** on a recently resolved event
- The LOSING advisor has a 25% chance per turn to sabotage the WINNING advisor's project
- Sabotage: the winning solution's positive effect is halved for 1 turn

### Intrigue Pairs (most common)
| Pair | Conflict Axis |
|------|--------------|
| Treasurer vs Councilor | Economy vs Loyalty |
| General vs Grand Diplomat | Force vs Diplomacy |
| High Priest vs Spymaster | Transparency vs Secrecy |
| Marshal vs Treasurer | Security spending vs Revenue |

### Detection
- **Spymaster detects intrigue** automatically if assigned "Monitor Advisors" standing order (KM_War_Systems.md)
- **Without Spymaster monitoring:** Player must notice stat underperformance and investigate (Perception DC 16 or Society DC 14)

### Confrontation
When detected, player has 3 options:
1. **Warn** — Advisor stops sabotage for 2 chapters. No relationship penalty. May resume.
2. **Reprimand publicly** — Advisor stops permanently. −2 relationship with that advisor. +1 Stability (order restored).
3. **Use the Debate system** — Force the two advisors to argue it out (KM_Mythic_Systems.md). Loser accepts result. No sabotage, no relationship loss.

**Save block:** `"advisor_intrigue": { "active": [], "detected": [], "resolved": [] }`

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Advisor Events & Political Intrigue v1.0*
*Features #17 (Advisor Disagreements) and #26 (Advisor Intrigue) combined.*
*Inspired by Pathfinder: Kingmaker CRPG advisor system and Shadowbane guild politics.*


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — ADVENTURER BOARD
## KM_Kingdom.md | Active from: Adventurer's Guild built | Referenced by: KM_Kingdom.md, KM_Kingdom.md

> **DM:** The Adventurer Board lets the player post bounties, hire NPC adventurer parties to handle kingdom problems, and receive mission reports. Requires the Adventurer's Guild building (KM_Kingdom.md). This system lets the player delegate tasks they can't or won't handle personally.

---

## 📋 COMMAND

`.board` — Display the Adventurer Board: active bounties, available parties, and mission reports.

---

## 🏛️ BOARD OPERATIONS

### 1. POST A BOUNTY
Player pays RP to post a bounty on a specific problem. NPC adventurers may take it.

| Bounty Type | RP Cost | Time to Complete | Success Chance |
|-------------|---------|-----------------|----------------|
| **Clear a hex** (known enemies) | 4 RP | 1 kingdom turn | 70% + 5% per extra RP spent |
| **Escort a caravan** | 2 RP | Immediate (next trade event) | 85% |
| **Investigate a rumor** | 3 RP | 1 turn | 60% + 10% if Spymaster assists |
| **Retrieve a specific item** | 6 RP | 1-2 turns | 50% + 5% per extra RP |
| **Slay a named creature** | 8 RP | 2 turns | 40% base (dangerous missions) |

### 2. HIRE AN ADVENTURER PARTY
Available parties rotate each kingdom turn. Each has a quality tier affecting success rates.

| Party Tier | Hire Cost | Success Modifier | Availability |
|-----------|-----------|-----------------|-------------|
| **Green** (level 1-3) | 2 RP | −10% to base chance | Always available |
| **Seasoned** (level 4-6) | 5 RP | +0% (uses base chance) | 70% chance available |
| **Veteran** (level 7-9) | 10 RP | +15% | 40% chance available |
| **Elite** (level 10+) | 18 RP | +30% | 20% chance available |

### 3. RECEIVE MISSION REPORTS
When a mission completes, the DM delivers a report at the start of the next Kingdom Turn:

**Success report:**
```
[ADVENTURER BOARD — Mission Complete]
Bounty: {bounty description}
Party: {party name and tier}
Result: SUCCESS
Loot recovered: {items if any — rolled from hex loot table}
XP awarded to kingdom: {50 × party level}
Notes: {1-2 sentence narrative of how they handled it}
```

**Failure report:**
```
[ADVENTURER BOARD — Mission Failed]
Bounty: {bounty description}
Party: {party name and tier}
Result: FAILURE — {party defeated / retreated / disappeared}
Bounty refunded: 50% of posted RP
Notes: {What went wrong. Intel gained about the threat.}
Consequence: {Threat may escalate. Re-posting bounty costs +2 RP.}
```

---

## 🧑‍🤝‍🧑 SAMPLE NPC PARTIES (DM generates new ones each turn)

| Party Name | Tier | Composition | Personality |
|-----------|------|-------------|------------|
| The Copper Crows | Green | Fighter, Rogue, Cleric | Enthusiastic, inexperienced, cheap |
| Ironwood Company | Seasoned | Ranger, Druid, Fighter, Wizard | Professional, reliable, no-nonsense |
| The Red Requiem | Veteran | Champion, Magus, Oracle, Rogue | Expensive, effective, morally flexible |
| Stormbreak | Elite | Fighter/Marshal, Witch, Barbarian, Investigator, Summoner | The real deal. They negotiate terms. |

### Party Personality Effects
- **Enthusiastic/Green:** May over-report success. 10% chance they missed something in the cleared hex.
- **Professional:** Report accurately. No surprises.
- **Morally flexible:** 15% chance they kept the best loot item for themselves. Player can confront.
- **Negotiate terms:** Elite parties demand a share of recovered loot (50% of any magic items found).

---

## 📊 BOARD MANAGEMENT

| Rule | Detail |
|------|--------|
| Max active bounties | 3 (expandable to 5 with Guild upgrade: +6 RP) |
| Max parties hired simultaneously | 2 |
| Party loss | If a party is destroyed (crit failure), that tier becomes unavailable for 2 turns (recruitment drought) |
| Reputation link | Each successful bounty: +1 civilian reputation in nearest settlement |
| Failed bounty | Threat level in target hex increases by 1 (enemies are warned/prepared) |

---

## ⚠️ DM RULES

1. **Generate party names and personalities each turn.** Don't reuse names. These are transient NPCs.
2. **Roll success/failure honestly.** Show the math: "Success chance: 70% base + 15% veteran = 85%. Roll: d100 → 73. SUCCESS."
3. **Failure consequences are real.** A failed "slay named creature" means the creature is now alert and harder to approach.
4. **Player can accompany a party.** If the player joins, auto-success but they spend the time (travel + encounter takes 1-3 days). Converts to a normal encounter played out in full.
5. **The board is NOT a replacement for play.** If a bounty would involve a major story beat or quest objective, the board rejects it: "No party will take a contract this dangerous. This one's yours, Your Majesty."

---

## 📋 BOUNTY SCENARIOS (d12 table, roll per kingdom turn)

| d12 | Bounty | RP Cost | Difficulty | Target Hex |
|-----|--------|---------|-----------|------------|
| 1 | Wolf pack harassing farmstead | 2 | Green | Random settled hex |
| 2 | Bandit camp spotted by patrol | 4 | Seasoned | Random border hex |
| 3 | Missing merchant caravan | 3 | Green | Random road hex |
| 4 | Troll sighting near settlement | 6 | Veteran | Random forest hex |
| 5 | Ancient ruin discovered, needs clearing | 5 | Seasoned | Random unexplored hex |
| 6 | Haunted mine — workers refuse to enter | 4 | Seasoned | Random hill hex |
| 7 | Fey pranksters disrupting a village | 3 | Green | Random settled hex |
| 8 | Escaped prisoner from Pitax spotted | 6 | Veteran | Random border hex |
| 9 | Giant beast tracks near the capital | 8 | Elite | Capital-adjacent hex |
| 10 | Cult activity reported in the Narlmarches | 6 | Veteran | Narlmarches hex |
| 11 | Rival adventurer guild poaching in your territory | 4 | Seasoned | Random hex |
| 12 | Dragon sighting (young, territorial) | 10 | Elite | Random mountain hex |

### Expanded NPC Party Templates (d10 per availability check)

| d10 | Party Name | Tier | Composition | Personality | Quirk |
|-----|-----------|------|-------------|------------|-------|
| 1 | The Copper Crows | Green | Fighter, Rogue, Cleric | Enthusiastic beginners | Over-report success. 10% missed detail. |
| 2 | Mudfoot Company | Green | Ranger, Druid, Barbarian | Smell terrible, work cheap | Track anything. Refuse to enter cities. |
| 3 | Ironwood Company | Seasoned | Ranger, Druid, Fighter, Wizard | Professional, reliable | Write formal reports. Expect formal payment. |
| 4 | The Lantern Bearers | Seasoned | Cleric, Paladin, Rogue, Bard | Religious. Efficient. Judgmental. | Refuse bounties involving undead allies. |
| 5 | Shrike River Runners | Seasoned | Rogue ×2, Ranger, Bard | Fast, flexible, morally gray | 15% kept best loot. Confrontable. |
| 6 | The Red Requiem | Veteran | Champion, Magus, Oracle, Rogue | Expensive, effective, dramatic | Demand an audience with the ruler post-mission. |
| 7 | Blackwater Solutions | Veteran | Fighter, Alchemist, Investigator, Ranger | Cold professionals | No personality. Perfect reports. Unsettling. |
| 8 | Thornwall Irregulars | Veteran | Barbarian, Druid, Monk, Sorcerer | Chaotic but devastating | 20% cause collateral damage. Always succeed. |
| 9 | Stormbreak | Elite | Fighter/Marshal, Witch, Barbarian, Investigator, Summoner | Negotiate terms. Demand respect. | Want 50% of magic items. Worth it. |
| 10 | The Last Company | Elite | Champion, Wizard, Rogue, Cleric, Fighter | Retired legends. One last job. | Automatically succeed on first mission. Disband after. |

### Failure Consequence Chains

When a bounty fails, the threat doesn't just persist — it escalates:

| Original Bounty | Failure → Escalation | Second Failure → Crisis |
|----------------|---------------------|----------------------|
| Wolf pack | Pack grows. +2 wolves. Attacks livestock. Economy −1. | Alpha wolf appears. Named beast. Personal hunt required. |
| Bandit camp | Bandits recruit. Raid fires next turn. Border −1. | Bandit leader emerges. Named NPC. Army engagement. |
| Troll sighting | Troll claims hex. Fortification damaged. | Troll nest established. 3 trolls. Fire required. |
| Ancient ruin | Undead emerge from ruin. Random encounter +1 in area. | Ruin becomes a dungeon (KM_Mythic_Systems.md). |
| Dragon sighting | Dragon attacks a caravan. Economy −2. | Dragon nests. Permanent threat until slain. Personal combat or elite party. |

**Save block:** `"adventurer_board": { "posted_bounties": [], "active_missions": [], "completed_reports": [], "guild_upgraded": false, "failure_escalations": [] }`

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Adventurer Board v2.0*
*Bounty table + 10 party templates + failure escalation chains.*


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — TERRITORIAL RAIDS & BORDER CONFLICTS
## KM_Kingdom.md | Active from: Chapter 2 | Referenced by: KM_Kingdom.md, KM_War_Systems.md

> **DM:** Between-chapter events where rival factions probe the kingdom's borders with raids. These fire automatically based on kingdom turn events and faction hostility. Resolution depends on garrison strength, fortifications (KM_Kingdom.md), and standing orders (KM_War_Systems.md). The player can delegate defense or handle raids personally.

---

## 📊 RAID GENERATION

### When Raids Fire
- **Every 2-3 kingdom turns** starting Chapter 2 (roll d6: raid fires on 5-6)
- **Automatic** if any faction is at Hostile (−6 or below) in KM_World_Systems.md
- **Story-scripted** raids during specific chapter events (Troll Trouble, Pitax War)
- **Random** border encounters when no hex fortifications protect a border hex

### Raid Sources by Chapter

| Chapter | Primary Raider | Secondary Raider | Raid Level Range |
|---------|---------------|-----------------|-----------------|
| Ch2 | Bandit remnants | Kobold/Mite raiders | 2-4 |
| Ch3 | Trolls | Tiger Lord scouts | 4-7 |
| Ch4 | Tiger Lord warbands | Pitax infiltrators | 7-10 |
| Ch5 | Pitax army units | Mercenary companies | 10-14 |
| Ch6 | Nyrissa's fey | Bloom creatures | 12-16 |

---

## ⚔️ RAID RESOLUTION

### Automated Resolution (player delegates)
Used when player assigns standing orders to handle raids or has garrison forces in the target hex.

```
Raid Strength: d20 + Raid Level
Defense Strength: Garrison Offense + Fortification Bonus + Standing Order Bonus

Defense > Raid     = REPELLED. No damage. +1 Stability. Raider faction −1.
Defense = Raid     = STALEMATE. Fortification takes 1 damage tier. Garrison holds.
Defense < Raid     = BREACH. Settlement/hex takes damage:
                     - Unfortified hex: random building destroyed (if settlement)
                     - Fortified hex: fortification reduced 1 tier
                     - Unrest +1. Reputation −1 in nearest settlement.
Defense < Raid −5  = OVERRUN. Garrison routed. Hex control lost until reclaimed.
                     Unrest +2. Reputation −2.
```

### Bonuses to Defense

| Source | Bonus |
|--------|-------|
| Watchtower in hex or adjacent | +2 (early warning) |
| Palisade in hex | +1 AC bonus to garrison |
| Fort in hex | +4 AC, supplies for extended defense |
| Trapped Approach | Raid takes 2d6 damage before engagement |
| Marshal "Patrol Borders" order | +2 to detect, +1 to defense |
| General "Fortify Position" order | +1 defense per turn active |
| Army unit garrisoned | Add army's Offense to defense |

### Personal Resolution (player handles it)
If the player chooses to ride out and meet the raid:
- **Travel time:** Based on hex distance. Early warning from Watchtower = 1 extra day to prepare.
- **Encounter:** Standard combat encounter at Raid Level. DM runs from Bestiary + chapter raider stat blocks.
- **Victory:** +1 Stability, +1 Reputation in nearest settlement. Loot from defeated raiders. XP as normal encounter.
- **Retreat:** Raid succeeds as automated BREACH result.

---

## 📋 RAID EVENT FORMAT

```
[BORDER CONFLICT — {Raid Name}]
RAIDER: {Faction} — {Unit type} — Strength {Raid Level + d20 result}
TARGET: Hex [{x,y}] — {Settlement name or "wilderness hex"}
DEFENSE: {Garrison + Fortification + Orders = total}

RESULT: {REPELLED / STALEMATE / BREACH / OVERRUN}
DAMAGE: {What was lost}
RESPONSE OPTIONS:
 1. Accept result — move on
 2. Send army to pursue  [costs 1 army action]
 3. Ride out personally  [travel + combat encounter]
 4. Post bounty on Adventurer Board  [KM_Kingdom.md]
```

---

## 🗺️ BORDER VULNERABILITY

### Unprotected Borders
A border hex with no fortification AND no patrol order is "exposed." Exposed hexes:
- Raid success chance +20%
- No early warning (player learns about raid AFTER damage)
- If 3+ border hexes are exposed simultaneously: +1 Unrest per turn ("the borders are undefended")

### Border Hardening
Placing 1 fortification every 3 border hexes covers the gap:
- **Chain rule:** A Watchtower covers its hex + 2 adjacent hexes for detection
- **Fort rule:** A Fort covers its hex only but at maximum defense
- **Optimal coverage:** Alternating Watchtowers and Forts along the border

---

## 📊 ESCALATION

If raids go unanswered for 3+ consecutive turns:
1. **Turn 1-2:** Raids are probing. Low strength. Easy to repel.
2. **Turn 3:** Raider faction commits more forces. Raid Level +2.
3. **Turn 4+:** Full incursion. Multiple hexes attacked simultaneously. Army response required.
4. **Turn 6+:** If still unanswered, raider faction claims the hex permanently. Kingdom Size −1.

### De-escalation
- Repel 3 consecutive raids: raider faction backs off for 4 turns
- Destroy raider source (clear the enemy camp/stronghold): raids from that source stop permanently
- Diplomatic solution: use faction reputation to negotiate cease-fire (requires Friendly or better)

---

## ⚠️ DM RULES

1. **Raids should feel like pressure, not punishment.** A well-fortified kingdom handles most raids automatically. The system rewards preparation.
2. **Roll honestly.** Show the raid strength roll and defense calculation. The player should see why they won or lost.
3. **Personal combat raids are OPTIONAL.** The player can always delegate. Never force them to ride out.
4. **Narrative flavor:** Describe the raid briefly even when automated. "Tiger Lord riders tested your eastern watchtower at dawn. The garrison held. They left two dead and retreated into the Kamelands."
5. **Scale with kingdom size.** A large kingdom (Size 20+) faces raids more frequently but has more resources. Small kingdoms face fewer but have less defense.

---

## 🏴 NAMED RAIDER LEADERS

Each chapter's raiders have named leaders. If the leader is captured or killed, raids from that source stop for 2 chapters. If the leader escapes, raids escalate faster.

### Chapter 2 Raiders

**Kressle's Remnants** — Bandit Captain Drelev's Cousin
- If Kressle survived Ch1: she leads the remnants. Raid Level +1 (she knows the terrain).
- If Kressle was killed: a nameless lieutenant leads. Generic stats. Easier to break.
- **Capture reward:** Intel on remaining Stag Lord caches (1d4 × 50 gp loot). Reputation +1.

**Sootscale Renegades** — Chief Mikmek the Bitter (if kobold alliance failed)
- Only fires if `sootscale_alliance = FALSE`.
- Raid style: underground sabotage (mine collapses, road sinkholes). Not direct combat.
- **Resolution:** Negotiate (Diplomacy DC 14) or smoke them out (Athletics DC 16 + 2 days).

### Chapter 3 Raiders

**Troll Marauders** — Hargulka's Lieutenant
- Trolls hit farming hexes. Burn crops. Food commodity: −1 per unanswered raid.
- **Special:** Fire required. Non-fire garrison bonus halved.
- **Capture:** Interrogation reveals Hargulka's camp location (if not yet found).

**Kellid Scouts** — Dugath the Quiet
- Not hostile by default. Testing borders. If kingdom has Kellid faction ≥ Friendly: scouts report to you instead.
- If faction < Neutral: raids escalate to livestock theft (Economy −1/turn).
- **Personal encounter:** Player can meet Dugath at the border (Scripted Interaction). Diplomacy DC 16: alliance option.

### Chapter 4 Raiders

**Tiger Lord Vanguard** — War Chief Zorek
- Professional military raiders. Raid Level 8-10. Target fortified hexes specifically.
- **Strategy:** Zorek tests defenses, reports to Armag. Captured: full Tiger Lord army intelligence.
- **Combat:** If player intercepts personally — War Chief Zorek (Barbarian 8, HP 95, AC 20). Named NPC fight.

**Pitax Infiltrators** — The Masked Agent
- Not military raids — sabotage. Poison wells, burn barns, plant evidence of disloyalty.
- Detection: Spymaster "Counter-Espionage" order. Otherwise: effects appear as random bad luck.
- **Unmasking:** Perception DC 18 at the site of sabotage, or Spymaster investigation (2 turns).

### Chapter 5 Raiders

**Pitax Forward Units** — Captain Stefano
- Full military raids. Raid Level 10-14. Multiple simultaneous hexes.
- **Special:** War footing. These are not probes — this is the invasion's opening move.
- **If captured:** Stefano negotiates. Offers Pitax troop positions in exchange for release. Information is 80% accurate (20% deliberate misdirection).

### Chapter 6 Raiders

**Bloom Incursions** — No leader (the Bloom itself)
- Not intelligent raids. The Bloom spreads into border hexes like infection.
- **Defense:** Nature-based (druids, Warden standing order, fire). Military garrison: half effectiveness.
- **Escalation:** Unlike other raids, Bloom incursions never stop escalating until the source is destroyed.
- **Cleansing:** Cleared hexes require 1 turn + Nature DC 18 or divine cleansing to restore.

---

## 📊 RAID EVENT TABLE (d8 per chapter)

| d8 | Ch2 Raid | Ch3 Raid | Ch4 Raid | Ch5 Raid | Ch6 Raid |
|----|----------|----------|----------|----------|----------|
| 1-2 | Kressle's Remnants | Troll Marauders | Tiger Lord Vanguard | Pitax Forward Units | Bloom Incursion (1 hex) |
| 3-4 | Sootscale Renegades | Kellid Scouts | Pitax Infiltrators | Pitax Forward Units | Bloom Incursion (2 hexes) |
| 5-6 | Kressle's Remnants | Troll Marauders | Tiger Lord Vanguard | Mercenary Raid (hired by Pitax) | Fey Border Test |
| 7 | No raid this turn | Kellid Scouts | Both Tiger + Pitax | Coordinated 3-hex assault | Bloom Incursion (3 hexes) |
| 8 | No raid this turn | No raid this turn | No raid this turn | No raid this turn | No raid — calm before final battle |

**Save block:** `"border_raids": { "pending": [], "resolved": [], "consecutive_unanswered": 0, "last_raid_turn": 0, "named_leaders_captured": [], "named_leaders_killed": [] }`

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Territorial Raids & Border Conflicts v2.0*
*Named raiders, per-chapter tables. Inspired by Shadowbane territorial warfare.*


---

<!-- merged from KM_Kingdom.md (v93.21 file consolidation) -->

# KINGMAKER — CLASS-SPECIFIC STRONGHOLD EVENTS
## KM_Kingdom.md | Active from: Chapter 2 (Kingdom Founded) | Referenced by: KM_Kingdom.md

> **DM:** Once per chapter, the player's class archetype generates a unique throne room event. These are personal to the player's build — a Guardian gets fortress defense petitions, a Witch gets supplicants seeking curses lifted. Events fire during Kingdom Turn Phase 4 (Events), tagged with `[STRONGHOLD EVENT]` to distinguish from generic kingdom events. Each event offers 2-3 solutions, rewards relationship/reputation/kingdom stats, and deepens the player's identity as a class-specific ruler.

---

## 📊 ARCHETYPE MAPPING

| Player Class Category | Archetype | Event Theme |
|-----------------------|-----------|-------------|
| Fighter, Guardian, Champion | **Fortress Lord** | Military petitions, fortress defense, dueling challenges |
| Barbarian, Monk | **Warlord** | Tribal disputes, arena challenges, warrior pilgrimages |
| Rogue, Investigator, Swashbuckler | **Shadow Lord** | Underworld contacts, heist proposals, information trade |
| Wizard, Witch, Psychic | **Arcane Sovereign** | Magical anomalies, apprentice requests, curse-breaking |
| Cleric, Oracle, Champion (divine) | **Divine Steward** | Religious disputes, pilgrim crises, divine omens |
| Druid, Ranger, Kineticist | **Warden** | Wildlife crises, territorial spirits, land corruption |
| Bard, Commander, Summoner | **Court Lord** | Performance challenges, diplomatic games, courtly intrigue |
| Alchemist, Inventor, Thaumaturge | **Artificer Lord** | Invention proposals, resource anomalies, magical item disputes |

---

## 🏰 FORTRESS LORD EVENTS (Fighter/Guardian/Champion)

### FL-1: The Dueling Challenge
A foreign swordsman arrives demanding a duel with the ruler to test the kingdom's martial strength.
```
[STRONGHOLD EVENT — The Dueling Challenge]
A Taldan swordsman in white and gold stands in your throne room.
"I have crossed three kingdoms to find a ruler worth fighting. Will you oblige?"

 A. Accept the duel personally  [Single combat, Fighter vs Fighter]
    → Win: +2 Reputation, +1 Stability, duelist becomes recruitable
    → Lose: −1 Reputation, duelist leaves respectfully

 B. Name a champion  [Companion fights in your stead]
    → Win: +1 Stability, companion +1 relationship
    → Lose: −1 Reputation

 C. Decline  [Diplomacy DC 14 to do so gracefully]
    → Success: No penalty. "A ruler who knows when not to fight."
    → Failure: −1 Reputation, −1 Stability. "Cowardice sits a throne here."
```

### FL-2: The Siege Engineer
A dwarf engineer offers to redesign your fortifications — for a price.
- **Accept (12 RP):** All hex fortifications gain +1 defense permanently. Engineer stays 1 chapter.
- **Negotiate (Diplomacy DC 16):** Half price (6 RP) but +1 defense to capital only.
- **Decline:** No cost, no benefit. Engineer offers services to Pitax instead.

### FL-3: The Veteran's Petition
Retired soldiers request a veterans' home in the capital. They offer their experience in return.
- **Grant (8 RP):** Loyalty +2. Army recruitment quality +1. Veterans advise during siege events.
- **Deny:** Loyalty −1. Veterans leave. Some join bandit groups (border raid chance +10%).
- **Compromise (4 RP):** Small hostel. Loyalty +1. Veterans available for training only.

---

## 🗡️ WARLORD EVENTS (Barbarian/Monk)

### WL-1: The Trial of Strength
Kellid warriors arrive to test the ruler in traditional combat — three rounds, escalating.
- **Accept:** Three opponents in sequence (level −2, level, level +2). Win all three: Kellid faction +2, Party Morale +1.
- **Refuse:** Kellid faction −1. "Soft hands rule here."
- **Substitute a companion:** Kellid accept if companion is martial class. Same rewards, companion +1.

### WL-2: The Arena Proposal
A merchant proposes building a fighting arena in the capital.
- **Accept (14 RP):** Economy +2, Culture +1, Loyalty +1. Arena building constructed. Monthly fight events.
- **Accept but regulate:** Economy +1, Stability +1. No death matches. Kellid faction −1 (soft rules).
- **Reject:** No effect. Merchant builds in rival territory instead.

---

## 🌙 SHADOW LORD EVENTS (Rogue/Investigator/Swashbuckler)

### SL-1: The Thieves' Guild Offer
An underground network proposes a formal arrangement — they operate with limits, you get information.
- **Accept:** Spymaster network +2 agents. Crime rate −10% (organized crime is quieter). Lawful alignment shift −1.
- **Reject publicly:** Crime rate +10% short-term (resentment). Stability +1. Lawful alignment shift +1.
- **Counter-offer (Deception DC 16):** You run the guild. All benefits, no alignment shift. 30% chance of exposure.

### SL-2: The Cold Case
A murder from before your reign surfaces — evidence points to a current advisor.
- **Investigate personally:** 3-step investigation scene (KM_Mythic_Systems.md). Truth revealed.
- **Assign to Spymaster:** Resolved in 1 turn. 80% accurate. 20% wrong person accused.
- **Bury it:** Stability +1 (no scandal). But the real killer is still active (Ch4 consequence).

---

## ✨ ARCANE SOVEREIGN EVENTS (Wizard/Witch/Psychic)

### AS-1: The Magical Anomaly
A ley line under the capital surges. Strange effects in the market district.
- **Study it (Arcana DC 18):** Harness the surge. Magister's research +1. Free spell scroll (level = player level ÷ 2).
- **Contain it (Crafting DC 16):** Surge stopped. Stability +1. No further effects.
- **Let it run:** Unpredictable results. Roll d6: 1-2 = bad (random curse), 3-4 = neutral, 5-6 = good (permanent +1 Culture).

### AS-2: The Apprentice Request
A talented young mage asks to study under you.
- **Accept:** Apprentice assists with kingdom magic. Culture +1/turn for 3 turns. Time cost: 1 downtime day/turn.
- **Refer to Magister:** Culture +1 once. No time cost. Apprentice becomes NPC at court.
- **Refuse:** No effect. Apprentice goes to rival mage (possible future antagonist).

---

## 🙏 DIVINE STEWARD EVENTS (Cleric/Oracle)

### DS-1: The Religious Schism
Two sects of the same deity clash over doctrine. Both want your ruling.
- **Side with Sect A:** Culture +1, Loyalty −1 with Sect B followers. Sect A priest offers services.
- **Side with Sect B:** Same, reversed.
- **Decree tolerance (Diplomacy DC 16):** Both sects accept. Culture +2. No loyalty loss. +1 Merciful disposition.

### DS-2: The Pilgrim Crisis
A flood of pilgrims overwhelms the capital. They seek healing and guidance.
- **Open the temples (4 RP):** Loyalty +2, Culture +1. Pilgrims spread word: Reputation +1 in 3 regions.
- **Limit entry:** Stability +1. Loyalty −1. Some pilgrims camp outside walls (disease risk: 10% plague event).
- **Heal personally:** Time cost: 3 downtime days. Loyalty +3, Reputation +2. Exhaustion (player Fatigued 1 day).

---

## 🌿 WARDEN EVENTS (Druid/Ranger/Kineticist)

### WA-1: The Corrupted Grove
A sacred grove in kingdom territory is dying. Druids request the ruler's intervention.
- **Cleanse personally (Nature DC 16):** Grove restored. Druid faction +2. Free primal scroll.
- **Send the Warden:** Resolved in 1 turn. 70% success. Grove partially restored on failure.
- **Burn it (prevents spread):** Grove destroyed. Druid faction −2. Stability +1 (no corruption spread).

### WA-2: The Beast Treaty
A pack of intelligent wolves offers non-aggression in exchange for a protected hex.
- **Accept:** Designate 1 hex as wildlife preserve. No building/farming there. Animal encounters −50% kingdom-wide. Druid faction +1.
- **Counter-offer (Nature DC 14):** Wolves patrol border. −10% raid chance from that direction. No hex cost.
- **Refuse:** Wolves become hostile. Animal encounters +25% for 2 chapters.

---

## 🎭 COURT LORD EVENTS (Bard/Commander/Summoner)

### CL-1: The Performance Challenge
A rival bard challenges you to a performance duel at court.
- **Accept (Performance DC 16):** Win: Culture +2, bard joins court. Lose: Culture −1, rival mocks you publicly.
- **Hire a champion performer:** Culture +1 regardless. Less personal glory.
- **Turn it political (Diplomacy DC 14):** Redirect into a diplomatic event. Economy +1. Bard confused but impressed.

---

## ⚗️ ARTIFICER LORD EVENTS (Alchemist/Inventor/Thaumaturge)

### AL-1: The Prototype
An inventor offers a revolutionary device — but it needs testing. And materials.
- **Fund it (10 RP, Crafting DC 16):** Success: unique item (DM generates). Failure: explosion (1d6 damage to capital building).
- **Let them test elsewhere:** No cost. Device appears in Pitax market next chapter.
- **Confiscate and study:** Free item. Inventor: −2 relationship. +1 Ruthless disposition.

---

---

## 🛡️ FORTRESS LORD — ADDITIONAL EVENTS

### FL-4: The Border Fort Request
A frontier settlement demands a permanent garrison. They'll contribute labor and food — but want soldiers NOW.
- **Accept (8 RP):** Fort built at that hex. Stability +2. Settlement: Loyalty +2. Standing military cost: 1 RP/turn.
- **Send militia instead (2 RP):** Cheaper but weaker defense (+1 instead of +4). Settlement: Loyalty +1.
- **Refuse:** Settlement begins hiring private guards. Stability −1. Risk: private militia becomes independent.

---

## 🗡️ WARLORD — ADDITIONAL EVENTS

### WL-3: The Monster Trophy
A legendary beast is spotted near the capital. Killing it would cement the ruler's warrior reputation.
- **Hunt it personally:** Combat encounter (CR = player level +1). Victory: Reputation +3, Culture +1 (trophy on display), +1 Blunt.
- **Organize a grand hunt (6 RP):** Festival atmosphere. Economy +1, Loyalty +1. Beast killed by whichever party finds it first.
- **Leave it:** "A ruler who ignores a beast at the gates." Stability −1 until resolved.

---

## 🌙 SHADOW LORD — ADDITIONAL EVENTS

### SL-3: The Blackmail Letter
Someone is blackmailing a kingdom advisor. The letter arrives on your desk.
- **Investigate (Spymaster):** Learn the blackmailer's identity in 1 turn. Confront or use the information.
- **Pay the demand (4 RP):** Problem goes away temporarily. Returns in 2 chapters at double cost.
- **Publish the secret yourself:** Advisor's secret becomes public. Advisor: −2 relationship. Blackmailer: neutralized. +1 Ruthless. Stability +1 (nobody else can be leveraged).

---

## ✨ ARCANE SOVEREIGN — ADDITIONAL EVENTS

### AS-3: The Ley Line Convergence
A rare alignment of ley lines creates a temporary nexus of power beneath the capital. Lasts 3 turns.
- **Harness it (Arcana DC 20):** Free magical building (Mage Tower equivalent). Culture +3. Magister: +1.
- **Study it (2 turns):** Learn 2 new spell recipes (KM_Mythic_Systems.md). +1 Scholarly.
- **Sell access to visiting mages (6 RP profit):** Economy +3. Visiting mages may cause incidents (10% chance: magical accident, Stability −1).

---

## 🎭 COURT LORD — ADDITIONAL EVENTS

### CL-2: The Diplomatic Marriage Proposal
A neighboring noble offers a political marriage. Not to you — to a companion.
- **Accept (companion agrees):** Faction +2 with proposing faction. Companion: Loyalty check (relationship must be Friendly+). If relationship <Friendly: companion refuses publicly (awkward).
- **Decline gracefully (Diplomacy DC 16):** No penalty. Faction +0. Companion: +1 relationship (you respected their autonomy).
- **Counter-propose trade alliance instead:** Economy +2. Faction +1. No marriage, no personal complications.

---

## ⚗️ ARTIFICER LORD — ADDITIONAL EVENTS

### AL-2: The Arms Contract
A foreign power wants to buy weapons manufactured in your kingdom. Large order, excellent price.
- **Accept (Economy +4/turn for 3 turns):** Weapons flow out. If that faction later attacks you, they use YOUR weapons. Oops.
- **Accept but limit quality:** Economy +2/turn. Weapons are functional but not your best. Less risk.
- **Refuse:** Economy +0. Faction: −1 (insulted). But your smiths are free to equip your army instead (army Offense +1).

---

## ⚠️ DM RULES

1. **One stronghold event per chapter.** Roll or select based on narrative fit.
2. **Match to player's archetype.** Never give a Fighter a magical anomaly event.
3. **Results are permanent.** Buildings built, factions shifted, NPCs recruited — all persist.
4. **Player override:** If the player's solution doesn't match any option, adjudicate with skill checks.
5. **Cycle through events.** Don't repeat an event the player already resolved. Each archetype now has 3-4 events — enough for the full campaign.

**Save block:** `"stronghold_events_completed": [{"event_id": "FL-1", "choice": "A", "chapter": 2}]`

---

*KM_Kingdom.md — Kingmaker PF2e Text Adventure | Class-Specific Stronghold Events v2.0*
*3-4 events per archetype. Inspired by BG2 stronghold management events.*
