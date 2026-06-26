# KINGMAKER — MOBILE BASE (CARAVAN / RIVER BARGE)
## KM_MobileBase.md | Active from: Chapter 2 (unlocked via Kingdom investment) | Referenced by: KM_Exploration.md, KM_Kingdom.md

> **DM:** The Mobile Base is a kingdom-funded caravan or river barge that serves as a mobile camp with upgradeable features. It makes wilderness exploration more strategic by providing persistent bonuses, storage, and facilities. Unlocked mid-Ch2 via kingdom investment (10 RP). The player chooses caravan (land) or barge (river) — each has different terrain advantages.

---

## 🚀 ACQUISITION

**Kingdom Activity:** Commission Mobile Base (10 RP, 1 kingdom turn build time)
```
[KINGDOM ACTIVITY — Commission Mobile Base]
Your kingdom is large enough to support a permanent expedition force.
Choose your mobile base type:

 [C] CARAVAN — Wagon train with draft horses. Travels all land hexes.
     Advantage: No terrain restriction on land. Carries more supplies.
     Disadvantage: Slower on roads (land speed). Cannot cross deep water.

 [B] RIVER BARGE — Flat-bottomed vessel for Stolen Lands waterways.
     Advantage: Fastest travel on river hexes (−1 day per river hex).
     Disadvantage: Cannot leave river network. Must dock to explore inland.
```

---

## 📊 BASE STATS

| Stat | Caravan | Barge |
|------|---------|-------|
| **Speed** | 2 hexes/day (road), 1 hex/day (off-road) | 3 hexes/day (river), N/A (land) |
| **Cargo Capacity** | 50 Bulk | 80 Bulk |
| **Ration Storage** | 30 days | 45 days |
| **Defense** | AC 15, HP 60 | AC 12, HP 80 |
| **Crew** | 2 drivers + guards | 4 crew + guards |
| **Camp bonus** | +2 to Prepare Campsite | +2 to Prepare Campsite, no ground hazards |

---

## 🔧 UPGRADES

Purchased with RP during Kingdom Turns. Each upgrade takes 1 turn to install.

| Upgrade | RP Cost | Effect |
|---------|---------|--------|
| **Crafting Bench** | 6 RP | Craft items during travel (KM_Crafting.md). −1 day crafting time. |
| **War Room** | 8 RP | `.wartable` accessible during travel. +1 to army command checks. |
| **Companion Quarters** | 4 RP | Companions in reserve gain +1 to next combat check (rested). Camp morale events fire more frequently. |
| **Expanded Storage** | 4 RP | Cargo +20 Bulk. Ration storage +15 days. |
| **Armored Hull** | 6 RP | Defense: AC +3, HP +20. Resists ambush damage. |
| **Cooking Station** | 4 RP | Special Meal recipes available during travel (KM_Weather_Camping.md). +1 to meal quality. |
| **Medical Bay** | 6 RP | Treat Wounds during travel (no downtime needed). +2 to Medicine checks on the base. |
| **Signal Tower** (Caravan) | 4 RP | Visual signal to nearest watchtower. Early warning system extends 1 hex. |
| **Sail Rig** (Barge) | 6 RP | Speed +1 hex/day on river when wind is favorable (50% of days). |

---

## 🗺️ TRAVEL WITH MOBILE BASE

### Movement
- **Caravan:** Follows road network at 2 hexes/day. Off-road: 1 hex/day. Cannot enter mountain or deep water hexes.
- **Barge:** Follows river hexes at 3 hexes/day. Must dock at river-adjacent land hexes to explore inland. Docking = free action.

### Encounters While Traveling
- Mobile Base **does not prevent** random encounters. Encounter chance as normal.
- If attacked: party fights from/near the base. Base provides cover (+2 AC while behind it).
- **Ambush protection** (if Armored Hull): Perception DC to detect ambush reduced by 2 (easier to spot).

### Camping in the Mobile Base
- All camp activities available. +2 circumstance bonus to Prepare Campsite (built-in shelter).
- Night attacks: base provides walls. Attackers must breach (Athletics DC 14 for caravan, DC 12 for barge).
- **Weather protection:** Moderate weather hazards (rain, wind) negated while in the base. Severe (storm, tornado) still apply.

---

## 💥 MOBILE BASE DAMAGE

The base can be damaged by combat, environmental hazards, or story events.

| HP Remaining | Status | Effect |
|-------------|--------|--------|
| 100–61% | Intact | All bonuses active |
| 60–31% | Damaged | Speed −1 hex/day. One upgrade offline (DM picks least critical). |
| 30–1% | Critical | Speed halved. Two upgrades offline. Camp bonus lost. |
| 0 | Destroyed | Base lost. Must commission new one (full RP cost). Cargo dumped in current hex. |

**Repair:** 2 RP per 25% HP restored. Takes 1 kingdom turn. Cannot repair while traveling — must be at a settlement.

---

## 📋 DISPLAY FORMAT

```
══════════════════════════════════════════════
MOBILE BASE — {Caravan/Barge} "{Name}"
══════════════════════════════════════════════
HP: {current}/{max} | Status: {Intact/Damaged/Critical}
Speed: {X} hexes/day | Cargo: {used}/{max} Bulk
Rations: {current}/{max} days
Upgrades: {list of installed upgrades}
Current Location: Hex [{x,y}] — {description}
══════════════════════════════════════════════
```

**Save block:** `"mobile_base": { "type": "caravan", "name": "The Iron Road", "hp": 60, "hp_max": 60, "upgrades": ["crafting_bench", "companion_quarters"], "cargo_used": 12, "rations": 30, "location": [4,7] }`

---

## ⚠️ DM RULES

1. **The base is a home.** Companions comment on it. They decorate their quarters. It's not just a stat block — it's a place.
2. **Name it.** The player names their caravan/barge. Use the name in narration.
3. **Upgrades are visible.** When the crafting bench is installed, describe the tools bolted to the wagon bed. When the war room is added, describe the map table.
4. **Destruction is dramatic.** If the base is destroyed, it's a scene — cargo scattered, upgrades lost, companions salvaging what they can.
5. **One base at a time.** Cannot have both caravan and barge. Can switch by commissioning a new one (old one decommissioned, upgrades do not transfer).

---

## 🎲 MOBILE BASE EVENTS (d8, roll per 3 hexes traveled)

| d8 | Event | Resolution |
|----|-------|-----------|
| 1 | **Wheel breaks** (caravan) / **Hull scrapes** (barge) | Crafting DC 14 to repair (1 hour). No repair: Speed −1 until settlement. |
| 2 | **Ambush on the road/river** | Combat encounter. Base provides cover (+2 AC). If Armored Hull: attackers take 1d6 approaching. |
| 3 | **Merchant encounter** | Traveling merchant offers 3 random items at 120% price. Rare materials available (1 per encounter). |
| 4 | **Refugee request** | Family asks for a ride to the capital. Accept: Loyalty +1, 1 day slower. Refuse: no penalty. |
| 5 | **Weather damage** | Severe weather hits the base. Fort DC 14 or base takes 10 HP damage. Expedition Tent negates. |
| 6 | **Companion moment** | Random companion has a scene triggered by the travel. Bond Moment opportunity. +1 if engaged. |
| 7 | **Discovery** | Warden spots something from the base: hidden trail, animal den, mineral deposit. Free hex intel. |
| 8 | **Nothing** | Quiet travel. Good time to craft, rest, or talk. |

### Named Caravan Events (story-specific)

**"The Painted Wagon" (Ch2):** A traveling theater troupe asks to join your caravan for protection. Accept: they perform at your next settlement (Culture +1, Loyalty +1). Refuse: they're attacked 1 hex later (guilt moment — player can rescue).

**"The River Ghost" (Ch3, barge only):** At night on the river, something bumps the hull. Perception DC 16: a body, face-down. Investigation reveals a murdered Pitax courier carrying intelligence. Free intel + quest hook.

**"The Broken Axle" (Ch4):** The caravan master reports the axle was sabotaged — cut partway through. Someone in the caravan or a recent visitor did this. Investigation scene (KM_Examination.md format). Spymaster: auto-detect if present.

**"The Bloom on the Water" (Ch6, barge only):** Roses growing on the river surface. The barge can push through (hull takes 2d6 damage) or detour (adds 1 day). Nature DC 18: the roses part if you play music. Hakon or Linzi: auto-success.

### Upgrade Narration

When an upgrade is installed, the DM describes it in one sentence:

| Upgrade | Installation Narration |
|---------|----------------------|
| Crafting Bench | *"A heavy wooden bench bolted to the wagon bed, tools hanging from pegs. It smells of iron filings and possibility."* |
| War Room | *"A map table that folds out from the wall. Pins and string. The kingdom's borders drawn in charcoal. It makes the caravan feel like a command post."* |
| Companion Quarters | *"Curtained sections. Not privacy — the illusion of it. Enough for people who've been sleeping on the ground to remember what a personal space feels like."* |
| Medical Bay | *"Clean cloth, boiled instruments, a folding cot. Tristian called it 'adequate.' From him, that's a compliment."* |
| Cooking Station | *"A proper fire pit with a wind shield and hanging pots. The first meal cooked here makes the caravan smell like a home."* |

**Save block:** `"mobile_base": { "type": "caravan", "name": "The Iron Road", "hp": 60, "hp_max": 60, "upgrades": ["crafting_bench"], "cargo_used": 12, "rations": 30, "location": [4,7] }`

---

*KM_MobileBase.md — Kingmaker PF2e Text Adventure | Mobile Base System v2.0*
*Travel events + named story events + upgrade narration.*
