# KINGMAKER — STANDING ORDERS SYSTEM
## KM_StandingOrders.md | Active from: Chapter 2 | Referenced by: KM_Kingdom.md, KM_Commands_P2.md

> **DM:** Standing orders are persistent per-role assignments that run automatically each kingdom turn. The player assigns them once; they repeat until changed. This fills the gap between kingdom turns with ongoing work and generates minor rewards, XP, or reputation.

---

## 📋 COMMAND

`.orders` — Display and modify standing orders for all filled leadership roles.

---

## 📊 STANDING ORDER LIST BY ROLE

### MARSHAL — Military Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Patrol Borders** | +1 Stability. Detect border raids 1 turn early (stacks with Watchtower). | Army unit assigned |
| **Train Militia** | +1 to next army recruitment quality. After 3 turns: unlock Militia army unit. | Barracks in capital |
| **Escort Caravans** | +1 Economy (trade protection). Merchant random encounter chance −10%. | Trade road cleared |
| **Hunt Bandits** | Reduce bandit random encounter chance by 25% in patrolled hexes. | — |

### TREASURER — Economic Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Collect Taxes** | +2 RP income. Loyalty −1 if used 3+ consecutive turns. | — |
| **Audit Settlements** | Detect embezzlement or advisor intrigue (Finance). Stability +1. | — |
| **Negotiate Trade** | +1 Economy. 20% chance per turn of new merchant arrival at capital. | Trade road open |
| **Invest in Infrastructure** | Next building costs −2 RP. Stacks up to −6 over 3 turns, then resets. | Treasury ≥ 20 RP |

### SPYMASTER — Intelligence Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Monitor Advisors** | Auto-detect advisor intrigue (KM_AdvisorEvents.md). | — |
| **Gather Intelligence** | Learn one fact about target faction's current plans. | Target faction specified |
| **Counter-Espionage** | Enemy spy success rate −25%. Foreign agents detected on arrival. | — |
| **Infiltrate Faction** | After 3 turns: +2 to next diplomatic roll with target faction. Risky: 15% chance of exposure (faction −2). | Target faction specified |

### COUNCILOR — Domestic Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Boost Morale** | +1 Loyalty. Reputation +1 in capital (max once per 3 turns). | — |
| **Mediate Disputes** | Prevent 1 random kingdom event from firing (absorb it). | — |
| **Census** | Reveal exact population, growth rate, and immigration trend. Economy +1 (better tax base). | — |
| **Festival Planning** | After 2 turns: free festival event fires (Loyalty +2, Economy −1). | Tavern in capital |

### GENERAL — Military Strategy Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Fortify Position** | +1 Defense to all hex fortifications (KM_Buildings.md). | Fort or Watchtower exists |
| **War Games** | Army Morale +1 per turn (max +3). Offense +1 after 3 turns. | 2+ army units |
| **Recruit Soldiers** | After 2 turns: 1 new army unit available. Quality based on kingdom Stability. | Barracks, Treasury ≥ 8 RP |
| **Scout Enemy** | Reveal enemy army positions and strength in 1 target hex. | Army unit or Watchtower |

### HIGH PRIEST — Spiritual Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Preach** | +1 Loyalty, +1 Culture. 10% chance of religious NPC arrival. | Temple in capital |
| **Bless Fields** | +2 Food commodity. Farmers happy: Loyalty +1 in rural hexes. | — |
| **Tend Wounded** | After any combat/event: automatic healing for kingdom army units. Morale +1. | Temple or Shrine |
| **Consecrate Land** | Target hex: undead encounter rate −50%. After 3 turns: permanently cleansed. | Target hex specified |

### WARDEN — Territory Orders

| Order | Effect Per Turn | Requirement |
|-------|----------------|-------------|
| **Survey Hex** | Reveal all resources, encounters, and points of interest in 1 unexplored hex. | Target hex specified |
| **Maintain Roads** | Travel time between settlements −1 day (min 1). Economy +1 from trade flow. | Road built |
| **Wildlife Management** | Reduce animal/beast encounter rate −25% in settled hexes. | — |
| **Resource Harvest** | +1 of any one commodity (Food, Lumber, Stone, or Ore) per turn from target hex. | Cleared hex specified |

---

## 📊 ORDER MANAGEMENT RULES

1. **One order per filled role per turn.** Empty roles = no order for that function.
2. **Orders persist.** Set once, runs every turn until changed. `.orders` to review/change.
3. **Changing an order:** Free action during Kingdom Turn Phase 3 (Activities). New order takes effect next turn.
4. **Stacking:** Orders that say "after X turns" track progress. Changing the order resets the counter.
5. **Companion-role link:** The companion filling the role uses their skill modifier for any checks. Higher-skilled advisors = better results.
6. **Failure:** Some orders have failure chances noted. On failure, the order still consumed the turn — try again or change strategy.

---

## 📋 DISPLAY FORMAT

```
══════════════════════════════════════════════
STANDING ORDERS — Turn {N}
══════════════════════════════════════════════
Marshal ({Name})      : Patrol Borders    [Stability +1, raid detection]
Treasurer ({Name})    : Negotiate Trade   [Economy +1, merchant chance]
Spymaster ({Name})    : Monitor Advisors  [Intrigue auto-detect]
Councilor ({Name})    : Boost Morale      [Loyalty +1]
General ({Name})      : War Games         [Army Morale +1, turn 2/3]
High Priest ({Name})  : Bless Fields      [Food +2, rural Loyalty +1]
Warden ({Name})       : Survey Hex        [Target: Hex 4,7]

Type .orders to modify. Changes take effect next turn.
══════════════════════════════════════════════
```

---

## 📋 ORDER OUTCOME NARRATION

> **DM:** Each turn, announce standing order results inline during Kingdom Turn Phase 1 (Upkeep). One sentence per active order. Show the effect.

**Narration examples by order:**

| Order | Success Narration | Failure/Complication Narration |
|-------|-------------------|-------------------------------|
| Patrol Borders | *"Marshal reports: borders quiet. One scout patrol spotted Tiger Lord riders watching from a distance. They did not cross."* | *"Marshal reports: patrol encountered resistance. 2 soldiers wounded. Bandits probing the eastern border."* |
| Collect Taxes | *"Treasurer's ledger: revenue up. Citizens grumble but pay."* | *"Treasurer reports: a hamlet refused collection. Marshal dispatched to resolve."* (Loyalty −1 event queued) |
| Monitor Advisors | *"Spymaster's note, sealed: 'All clear.' Or: 'The Treasurer and Councilor had a private meeting. Contents unknown.'"* | N/A (always succeeds if Spymaster assigned) |
| Gather Intelligence | *"Spymaster's report: [1 fact about target faction]. Source reliability: [high/moderate/low]."* | *"Spymaster: 'Source went silent. Either compromised or lying. Working on it.'"* |
| Boost Morale | *"Councilor organized a public works day. Citizens seem lighter. A child painted the kingdom banner on a wall."* | *"Councilor's event rained out. Loyalty unchanged. She's planning a replacement."* |
| Bless Fields | *"High Priest reports: harvest prayers conducted. Farmers optimistic. Two fields yielded double."* | *"High Priest: 'The land resists. Something in the soil is wrong.' Nature DC 16 to investigate."* |
| Survey Hex | *"Warden's map updated: Hex [x,y] — [terrain], [resource], [encounter type]. Point of interest: [description]."* | *"Warden: 'Hex surveyed but my scout didn't return. Sending another.'"* (delayed 1 turn) |
| War Games | *"General reports: troops sharper this month. Formation drills show improvement. Morale +1."* | N/A (War Games always succeed, just take time) |

### Companion-Specific Bonuses

When a companion fills a leadership role, their personality affects order outcomes:

| Companion | Role | Bonus |
|-----------|------|-------|
| **Amiri** as Marshal | Patrol Borders | +1 to detection (she scouts personally). Bandits: "A very large woman with a very large sword told us to leave." |
| **Linzi** as Councilor | Boost Morale | Effect lasts +1 turn (she writes commemorative songs). Citizens request encores. |
| **Regill** as Marshal | Any military order | +1 to all military results. Efficiency up. Soldiers terrified but effective. |
| **Tristian** as High Priest | Bless Fields / Tend Wounded | Healing doubled. Farmers bring him pies. He doesn't know what to do with the pies. |
| **Octavia** as Magister | Any arcane order | +1 to arcane results. Students assist (free labor). Occasional magical accident (5% chance, minor). |
| **Jubilost** as Treasurer | Audit / Negotiate Trade | Detects irregularities +2 bonus. Merchants dislike his tone but respect his numbers. |
| **Nok-Nok** as Spymaster | Any espionage order | Unorthodox methods. +2 to infiltration. Reports are barely legible but accurate. |
| **Harrim** as High Priest | Any spiritual order | Sermons are depressing but strangely effective. Loyalty +0 but Culture +1 (philosophical depth). |

**Save block:** `"standing_orders": { "marshal": "patrol_borders", "treasurer": "negotiate_trade", ... }`

---

*KM_StandingOrders.md — Kingmaker PF2e Text Adventure | Standing Orders System v2.0*
*Orders + outcome narration + companion personality bonuses.*
