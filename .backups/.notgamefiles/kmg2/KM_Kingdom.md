# KINGMAKER — KINGDOM MANAGEMENT
## KM_Kingdom.md | Active from: Chapter 1 (Kingdom Founding) | Referenced by: KM_Ch1.md+
## PAIR-LOAD WITH KM_Kingdom_B.md (faction reputation tracks)

---

> **DM:** Load this file from Ch1 onward. The first Kingdom Turn runs immediately after the player founds their capital. Use the hex system from KM_Map.md alongside this file. Track all kingdom state in the JSON Save Block under `kingdom{}`.
> For the complete settlement building catalogue (all 68 structures, RP costs, Commodity costs, Construction DCs, upgrade chains), search **KM_Buildings.md** in project knowledge.

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
                 Crisis event mandatory this turn (roll KM_Bestiary_B.md (kingdom events section)).
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

CRISIS EVENTS (mandatory — roll on KM_Bestiary_B.md crisis table (kingdom events section)):
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
 see `KM_Kingdom_B.md`**
