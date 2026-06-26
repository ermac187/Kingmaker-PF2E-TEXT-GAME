# KINGMAKER — EXPLORATION SYSTEMS
## KM_Exploration.md | Active from: Chapter 1 | Referenced by: All chapter files
## PAIR-LOAD WITH KM_Exploration_B.md (exotic materials flavor + armor reaction rule)

---

> **DM:** Load this file from Chapter 1 onward. It covers four systems that run across the entire campaign: the Storyteller/Relic Fragment quest, random encounter tables by terrain, weather and season rules, and the camping recipe system. All four operate in the background of every chapter.
> For full weather hazard stat blocks (Fog, Blizzard, Flash Flood, Tornado, etc.) and the complete camping activity ruleset, search **KM_Weather_Camping.md** in project knowledge.

---

## 📖 THE STORYTELLER & RELIC FRAGMENTS

### Who Is the Storyteller

An ancient, ageless man who appears in your capital once it is founded. He sits in the same spot every day — a corner of the market, or a bench near the throne room steps — and waits. He does not ask for anything. He does not explain himself. He simply says: *"Bring me pieces of the old world. I will tell you what they mean."*

`storyteller_available = TRUE` from Ch1 kingdom founding onward.

He accepts **Relic Fragments** and **Ancient Cyclops Coins**. Each delivery earns gold, XP, and lore that advances understanding of Nyrissa's curse and the campaign's hidden history.

---

### Relic Fragment Locations (All Chapters)

| # | Name | Location | Chapter |
|---|------|----------|---------|
| 1 | Token of the Dryad | Old Sycamore — Tartuccio's sanctum loot | Ch1 |
| 2 | Fallen Warrior's Buckle | Valley of the Dead — Ancient Cemetery | Ch3 |
| 3 | Feather of the Peryton | Narlmarches — Peryton nest encounter | Ch2 |
| 4 | Scale of the Wyvern Queen | Dire Narlmarches — wyvern matriarch | Ch2 |
| 5 | Vordakai's Eye Fragment | Vordakai's Chamber — post-boss loot | Ch3 |
| 6 | Tiger Lord War-Mask | Armag's Tomb — trophy room | Ch4 |
| 7 | Irovetti's Songbird Cage | Pitax Palace — private collection | Ch5 |
| 8 | Bloom-Touched Crown | Thousandbreaths — Nyrissa's sanctum | Ch6 |
| 9 | First Kingdom Stone | House at Edge of Time — entry hall | Ch7 |
| 10 | Lantern King's Tear | House at Edge of Time — true ending reward | Ch7 |

**Note:** Fragments 9 and 10 are only obtainable on the true ending path. Delivering all 10 to the Storyteller before entering Ch7 is one of the four conditions for the optional Linzi save.

---

### Ancient Cyclops Coins

Scattered throughout Ch1–Ch3 locations. The Storyteller accepts up to 12 coins total across the campaign. Each coin gives:
- **1–4 coins:** 200 gp + *"The cyclops empire was old when Thassilon was young."*
- **5–8 coins:** 600 gp + lore about Vordakai's origins (useful in Ch3)
- **9–12 coins:** 1,200 gp + *"The eye that drinks souls was bound by one who loved what it became. That love became the prison. That prison became her curse."* — `nyrissa_origin_hint = TRUE`

---

### Storyteller Rewards Per Relic Fragment

When a Relic Fragment is delivered, the Storyteller examines it and tells a story:

| Fragments Delivered | Reward | Lore Unlocked |
|--------------------|--------|---------------|
| 1 | 500 gp, +300 XP | "This was left by someone who knew what was coming." |
| 2 | 800 gp, +400 XP | "The curse is not Nyrissa's creation. It was done to her." |
| 3 | 1,200 gp, +500 XP | "The Lantern King plays games with lives. He has done this before." |
| 4 | 1,600 gp, +600 XP | "She was given a heart. Hearts are levers." — `nyrissa_backstory_partial = TRUE` |
| 5 | 2,000 gp, +700 XP | "She loved a kingdom once. She destroyed it. She was made to." |
| 6 | 2,800 gp, +800 XP | "The Lantern King fears one thing: being seen clearly." |
| 7 | 3,500 gp, +900 XP | "Every kingdom she has destroyed has had a ruler who could have saved her. None did." — `nyrissa_can_be_saved_hint = TRUE` |
| 8 | 4,500 gp, +1,000 XP | Full Nyrissa backstory. `nyrissa_backstory_known = TRUE` |
| 9 | 6,000 gp, +1,200 XP | "There is a way to end the Lantern King's game. It requires truth." |
| 10 | 10,000 gp, +2,000 XP | The Storyteller reveals he is one of the Eldest — an ancient being who has watched this cycle repeat. He gives the player a token that grants +2 to all checks against the Lantern King in Ch7. |

**LINZI SAVE CONDITION:** `storyteller_collection = COMPLETE` requires all 10 fragments delivered before Linzi dies or before entering Thousandbreaths. This is the hardest of the four conditions.

---

## 🎲 RANDOM ENCOUNTER TABLES

> **DM:** When the party enters a new hex, roll d20. On a result ≤ the terrain's encounter threshold, roll on the appropriate encounter table. Each hex has one scripted fixed encounter (see KM_Map.md) that triggers on first entry only.

### Random Encounter Loot (by enemy type)

> **DM:** Every triggered random encounter that results in combat produces loot. Roll or select from the appropriate row based on the enemy type encountered. Award loot at end of combat, before travel resumes.

| Enemy Type | Guaranteed Loot | Perception DC (bonus loot) | Bonus Loot (if found) |
|------------|----------------|----------------------------|-----------------------|
| Bandits (2–4) | 1d6×5 gp, leather armor per body, basic weapons | 13 | Wanted poster (lore), 1d4×3 gp extra, 1 dose Antitoxin |
| Wolves / Worgs | Pelt ×1d3 (5 gp each at Oleg's), meat (Camp ingredient) | 15 | Worg: additionally 1 Worg Pelt (15 gp, Bartho wants these) |
| Giant Spiders | Spider Silk Rope 20 ft (2 gp), venom gland (Craft DC 14 → Spider Venom 1 dose) | 16 | Clutch of spider eggs (Old Beldame pays 8 gp each) |
| Kobolds (3–6) | 1d4×2 gp, crude shortbows, javelins ×3 | 12 | Kobold idol (story item — Sootscale recognizes it), 5 gp |
| Mites (3–5) | 1d3 gp in scattered coin, crude daggers | 11 | Thimble-sized mite treasure box: 8 gp, moonstone gem (3 gp) |
| Trolls (1–2) | Troll Flesh ×2 (alchemy ingredient — Bokken pays 4 gp each) | 14 | Crude iron ring (5 gp), stolen food stores (rations ×1d6) |
| Owlbear | Owlbear Claw ×2 (trophy, 10 gp each), feathers (Camp ingredient) | 15 | Owlbear Egg (if nest nearby — 50 gp to right buyer; Ekundayo knows who) |
| Fey (Pixies/Sprites) | Pixie Dust ×1 (Magic ingredient — Bokken or Old Beldame, 12 gp) | 17 | Fey Honey ×1 (Camp recipe ingredient), tiny silver coin (2 gp) |
| Undead (skeletons/zombies) | Bone fragment (story item in cursed areas), no coin | 14 | Corroded medallion (ID with Society DC 13 — identifies former noble, 15 gp) |
| Giant Frogs | Frog Legs ×3 (Camp ingredient — Hearty Porridge), mucus gland (2 gp, alchemical) | 13 | Giant Frog Tongue (Old Beldame, 6 gp) |
| Boars | Boar Meat ×3 (Camp ingredient — Venison Roast substitute), Boar Tusk ×2 (5 gp each) | 12 | Boar Fat ×1 (Camp ingredient — Kellid War-Bread) |
| Bandits (named lieutenant) | As Bandits + Masterwork weapon (type varies), 2d6×5 gp | 14 | Orders from Stag Lord (Ch1) or Pitax (Ch2+), Potion of Cure Light Wounds |

> **DM:** Loot delivery rule — do not summarize loot in one line after combat. Narrate the search briefly: *"You go through their packs / you check the body / you search the area."* Then list what is found. This is the moment items feel real to the player.

---

### Encounter Thresholds by Terrain

```
Plains/Roads : 1–3  (15%)    Hills   : 1–4  (20%)
Forest       : 1–5  (25%)    River   : 1–4  (20%)
Mountains    : 1–6  (30%)    Swamp   : 1–6  (30%)
Night travel : +2 to all thresholds
Roads built  : −1 to threshold in that hex
```

---

### Plains/Grassland Encounters (d12)

| d12 | Encounter | CR | Notes |
|-----|-----------|-----|-------|
| 1 | Thylacine Pack ×4 | 3 | Marsupial predators. Fast. |
| 2 | Bandit Patrol ×5 | 3 | Armed, hostile unless cowed |
| 3 | Wild Boar ×3 | 2 | Tuskgutter's cousins |
| 4 | Wandering Merchant | — | Sells random item (d6: 1–2 potion, 3–4 gear, 5 magic item, 6 nothing useful) |
| 5 | Kellid Outriders ×4 | 4 | Neutral if Amiri present; hostile otherwise |
| 6 | Giant Eagle | 4 | Non-hostile unless attacked; Perception DC 18 — it's watching |
| 7 | Zombie Horde ×8 | 2 | Remnant of Bloom corruption. Fire works well. |
| 8 | Stranded Traveler | — | Skill challenge: Medicine/Diplomacy. Reward: minor item, quest hook |
| 9 | Dire Wolf ×2 | 4 | Territorial. Retreat if 1 is killed. |
| 10 | Mite Scouting Party ×6 | 2 | From Old Sycamore remnants (Ch1) |
| 11 | Tax Dispute (NPC) | — | Two farmers argue over a fence. Resolution: Diplomacy/Society DC 14. Reward: +1 Loyalty |
| 12 | Nothing | — | Clear passage. +25 XP for successful Survival Scout check. |

---

### Forest Encounters (d12)

| d12 | Encounter | CR | Notes |
|-----|-----------|-----|-------|
| 1 | Owlbear | 6 | Bloom-touched in Ch2+. Fire does double. |
| 2 | Fey Pranksters ×4 | 3 | Pixies. Steal items if ignored. Bargain with them (Diplomacy DC 16). |
| 3 | Giant Spider Nest ×6 | 3 | Webbed terrain (difficult). Torch clears webs. |
| 4 | Treant | 6 | Neutral unless forest is damaged. Arcana/Nature DC 17 to parley. |
| 5 | Bandit Ambush ×6 | 4 | Have high ground. Archers in trees. |
| 6 | Lost Patrol | — | Kesten's missing soldiers. Rescue: +Stability, +500 gp |
| 7 | Mandragora Swarm | 5 | Will DC 16 or Confused 1 from their shriek |
| 8 | Dryad (Distressed) | — | Her tree is dying. Help (Nature DC 15): she gives rare herb. |
| 9 | Troll Scout | 5 | Ch2+ only. If trolls defeated: roll again. |
| 10 | Giant Mantis ×2 | 4 | Ambush predators. Reach 15 ft. |
| 11 | Herbalist's Cache | — | Hidden stash. Perception DC 19: find 4 Healing Potions + 2 rare herbs. |
| 12 | Peaceful Glade | — | Rest here: free Camp activity, no random encounter this rest. |

---

### Hills Encounters (d12)

| d12 | Encounter | CR | Notes |
|-----|-----------|-----|-------|
| 1 | Wyvern | 7 | Territorial. Has a lair on the ridge. |
| 2 | Giant Scorpion ×3 | 4 | Poison: Fort DC 16, Enfeebled 1 |
| 3 | Hobgoblin Warband ×8 | 4 | Disciplined. Retreat at 50% losses. |
| 4 | Rock Troll (lone) | 8 | Regeneration 20 (fire/acid). Dangerous alone. |
| 5 | Abandoned Fort | — | Skill challenge: clear rubble (Athletics DC 14). Inside: 300 gp, old weapon cache |
| 6 | Sinkhole | — | Perception DC 17 to spot. Fall in: 3d6 damage, Grabbed. Escape Athletics DC 16 |
| 7 | Griffon (adult) | 7 | Neutral if fed (use raw meat). Hostile if startled. |
| 8 | Giant Centipede Swarm | 5 | Fire clears them faster |
| 9 | Hermit's Shrine | — | Forgotten god. Pray (Religion DC 13): +1 to saves for 1 day |
| 10 | Bandit Lookout Post | 4 | 3 archers, pre-positioned. Perception DC 20 to spot before ambush. |
| 11 | Landslide (hazard) | — | Reflex DC 16 or 4d6 damage + Slowed 1 |
| 12 | Ridge View | — | Perception DC 12: see into adjacent hex. Auto-discover it. |

---

### River/Swamp Encounters (d12)

| d12 | Encounter | CR | Notes |
|-----|-----------|-----|-------|
| 1 | Hydra | 8 | 5 heads. Each head cut off → 2 grow back unless cauterized (fire immediately) |
| 2 | Giant Crocodile ×2 | 6 | Grab + Death Roll: automatic 2d8+10 per round while Grabbed |
| 3 | Will-o'-Wisp ×3 | 6 | Immune to most physical attacks. Lightning/magic only. |
| 4 | Boggard Tribe ×8 | 3 | Territorial. Negotiate with Diplomacy DC 18 (they speak broken Common) |
| 5 | Quicksand | — | Perception DC 20 to spot. Sink: Athletics DC 15/round to escape |
| 6 | Giant Frogs ×4 | 3 | Tongue grab: 15 ft range, Grabbed |
| 7 | Plague Zombie Horde ×10 | 2 | Disease on hit: Fort DC 14 or Sickened 1 |
| 8 | Lizardfolk Scouts ×5 | 3 | Neutral if approached calmly. Hostile if surprised. |
| 9 | Diseased Water | — | Drink without Purify Food/Water: Fort DC 14 or Sickened 1d4 days |
| 10 | Water Elemental (Large) | 7 | Guarding a sunken cache (300 gp, Potion of Water Breathing) |
| 11 | Fog Bank | — | Visibility 10 ft. All Perception checks at −4 until fog clears (2d4 rounds) |
| 12 | Fordable Crossing | — | Short cut: saves 1 day travel. Athletics DC 12 to cross safely. |

---

### Mountain Encounters (d12)

| d12 | Encounter | CR | Notes |
|-----|-----------|-----|-------|
| 1 | Roc (juvenile) | 9 | Will attack if it sees horses/mounts. Avoid: Stealth DC 22 |
| 2 | Stone Giant ×2 | 9 | Rock Throw 120 ft. Parley if Bardic/Diplomacy DC 24 |
| 3 | White Dragon (young) | 8 | Breath weapon: 30 ft cone, 8d6 cold, Reflex DC 22 half |
| 4 | Numerian Barbarians ×6 | 5 | Come from the north. Hostile to outsiders. |
| 5 | Avalanche | — | Athletics DC 18 to outrun. Fail: 6d6 damage + Immobilized |
| 6 | Cave Bear ×2 | 6 | Maternal. Will not pursue if retreated from. |
| 7 | Abandoned Dwarven Outpost | — | Perception DC 22: hidden cache (500 gp, Dwarven weapon) |
| 8 | Harpy Flock ×4 | 5 | Song: Will DC 17 or Fascinated (walk toward them) |
| 9 | Basilisk | 7 | Gaze: Fort DC 18 or Slowed 2. Crit fail: Petrified. Mirror shields help. |
| 10 | Ice Elemental ×3 | 6 | Fire weakness (double damage). Cold immunity. |
| 11 | Thin Air | — | High altitude: Fortitude DC 14 or Fatigued. Persists until lower elevation. |
| 12 | Mountain Pass | — | Shortcut found. Navigation DC 16: halve mountain travel time through this hex. |

---

## 🌦️ WEATHER & SEASON SYSTEM

### Seasons in the Stolen Lands

```
Spring  : Gozran–Sarenith (months 4–6)   — mild, wet, occasional storms
Summer  : Erastus–Arodus (months 7–8)    — hot and dry, clear skies
Autumn  : Rova–Lamashan (months 9–10)    — cool, windy, heavy rains begin
Winter  : Neth–Calistril (months 11–2)   — cold, snow possible, blizzards rare
```

### ⚠️ DAILY WEATHER PROCEDURE — MANDATORY

> **DM:** Run this EVERY morning before the daily travel block, without exception.
> Weather is not optional flavor — it affects travel time, combat, and camping.
> Full hazard stat blocks (Fog, Blizzard, Flash Flood, Tornado, etc.) and camping
> DC modifiers are in **KM_Weather_Camping.md**.

```
EACH MORNING — resolve in this order:

STEP 1 — PRECIPITATION
  Flat check DC (by current season):
    Summer: DC 20  |  Spring/Autumn: DC 15  |  Winter: DC 8
  Success → light rain (or snow if cold snap active)
  Effect: −1 visual Perception; fatigue threshold 4 hrs travel (not 8)

STEP 2 — TEMPERATURE (Winter only)
  Flat check DC:
    Kuthona/Calistril (deep winter): DC 18
    Abadius (mid-winter): DC 16
  Success → cold snap: fatigue after 4 hrs activity;
            light precipitation becomes snow

STEP 3 — WEATHER EVENT
  Flat check DC 17
  Success → roll d20 on the Random Weather Events table (KM_Weather_Camping.md)
  Natural 20 on flat check → roll again for possible linked second event
  If rolled event level exceeds party level + 4: reroll once

STEP 4 — ANNOUNCE WEATHER
  Open the day's travel block with the weather result. Example:
  "Weather: Heavy Rain — ranged attacks at −2, travel slowed"
  or "Weather: Clear — no effect"
  Then proceed to the daily travel format below.
```

**Quick weather effects (for common results — full stat blocks in KM_Weather_Camping.md):**

| Condition | Travel Effect | Combat Effect | Camp DC |
|-----------|--------------|---------------|---------|
| Clear/Overcast | Normal | None | DC 14 |
| Light Rain/Snow | Normal | Ranged −1 | DC 14 |
| Heavy Rain | +1 day per hex | Ranged −2, impossible 60+ ft | DC 18 |
| Storm | +2 days per hex, Fort DC 13 or Fatigued | Ranged impossible, verbal spells DC 15 Concentration | DC 22 or no rest benefits |
| Blizzard (winter) | Impassable without roads | All checks −4, 1d6 cold/hr without shelter | DC 26 or 2d6 cold overnight |

---

## 🍳 CAMPING RECIPE SYSTEM

> **DM:** When the party camps, one character may attempt to Cook a meal if they have the required ingredients. A successful meal grants the listed bonus to all party members the following day. Ingredients are found during exploration (Survival or Perception DC varies) or purchased at vendors.

### Cooking Check
```
Cook's roll: Survival + Wisdom modifier vs Recipe DC
Critical Success: bonus effect + extra benefit listed
Success: standard bonus listed
Failure: food is edible but no bonus
Critical Failure: food is inedible (waste ingredients)
```

### Recipes & Bonuses

| Recipe | Ingredients | DC | Bonus (next day) | Crit Bonus |
|--------|-------------|-----|------------------|------------|
| **Camp Stew** | Meat ×2 + Root Vegetable ×1 | 12 | +2 HP per level at next rest | +4 HP per level |
| **Mushroom Soup** | Mushroom ×3 (any safe variety) | 13 | +1 to Will saves | +2 to Will saves |
| **Berry Tart** | Fangberries or Moonberries ×3 | 14 | +1 to Perception checks | +2 to Perception + Low-Light Vision (1 day) |
| **Hearty Porridge** | Grain ×2 + Milk or Cream ×1 | 12 | Ignore first Fatigued condition | Ignore Fatigued, +5 ft speed |
| **River Fish Fry** | Fresh Fish ×2 + Lemon ×1 | 15 | +1 to Reflex saves | +2 Reflex + Evasion (1 encounter) |
| **Venison Roast** | Venison ×3 + Herbs ×1 | 16 | +2 to Fort saves | +2 Fort + ignore first Drained |
| **Spiced Wine** | Wine ×1 + Spice ×1 + Honey ×1 | 14 | +1 to all social Charisma checks | +2 social + reduce enemy attitude by 1 step easier |
| **Swamp Witch's Brew** | Rattlecaps ×1 + Toadstool ×1 (Old Beldame's recipes) | 20 | +1 to spell attack and DC | +2 spell attack/DC + +1 Focus Point |
| **Kellid War-Bread** | Rye ×2 + Bear Fat ×1 + Salt ×1 | 17 | +4 temp HP per character | +4 temp HP + +2 to Intimidation |
| **Fey Honey Cake** | Fey Honey ×2 + Flour ×1 | 18 | Recover 1 extra spell slot (lowest level) | Recover 2 spell slots |

### Finding Ingredients

| Ingredient | How to Find | DC |
|------------|------------|-----|
| Meat (generic) | Hunt during travel (Survival) | 12 |
| Venison | Hunt deer in forest hex (Survival) | 16 |
| Fresh Fish | River/swamp hex + 1 hour (Survival or Athletics) | 13 |
| Root Vegetables | Plains/forest exploration (Perception) | 14 |
| Mushrooms (safe) | Forest hex (Survival — Nature knowledge required) | 15 |
| Fangberries | Old Sycamore area (Ch1) / scattered forest | 16 |
| Moonberries | Night-blooming berry — nocturnal Perception check | 19 |
| Grain | Purchase (Oleg's, vendors) or farmland hex | — |
| Spices | Purchase only (vendors) | — |
| Wine | Purchase only | — |
| Fey Honey | Tiressia's glade (if allied) or fey encounter | — |
| Rattlecaps | Old Beldame's quest reward / swamp hex | 22 |
| Bear Fat | Kill a bear (Cave Bear or Forest Bear) | — |

---

## 🛒 VENDOR REFERENCE

### Capital Shops (available after building)

| Building Required | Items Available | Price Range |
|------------------|-----------------|-------------|
| Smithy | Basic weapons, ammunition, repair kits | Standard PF2e |
| Market | All mundane equipment, rations, tools | −10% vs standard |
| Temple (any) | Healing Potions, holy water, scrolls (L1–2) | Standard |
| Caster's Tower | Magic items (L1–8), scrolls, wands | +20% premium |
| Tannery | Leather armor, cloaks, bags | −15% |

### Vendors by Chapter

**Bokken (Ch1–2, Stolen Lands):**
Potions: Minor Healing 4 gp, Lesser Healing 12 gp, Antitoxin 3 gp, Alchemist's Fire 3 gp
Discount: 25% off if Fangberries delivered. Free potions for 1 month if Moon Radishes delivered.

**Old Beldame (Ch1+, Swamp):**
Scrolls (L1–4), Potion of Invisibility, Darkvision Elixir, Swamp Witch's Brew recipe
Requires: her quest complete or Perception DC 14 to approach safely.

**Bartholomew Delbin (Ch2, Secluded Lodge):**
Potion of Fire Breath ×3 (50 gp each), Scroll of Burning Hands ×4, Wand of Produce Flame
Available after Nature of the Beast quest.

**Oleg's Trading Post (Ch1–3):**
See KM_Ch1.md for full table. Stock expands after the first kingdom turn:
Adds: Healer's Tools upgrade, Antiplague, +1 weapons (one type, rotates weekly).

**Pitax Black Market (Ch5, infiltration path):**
Available if infiltrating Pitax. Illegal goods: Potion of Invisibility ×5, Poisoned Blades,
Scroll of Dominate, stolen magic items (flagged — if recognized, causes incident).

---

## 💾 EXPLORATION FLAGS (Save Block)

```json
"exploration": {
  "storyteller": {
    "fragments_delivered": 0,
    "coins_delivered": 0,
    "nyrissa_backstory_partial": false,
    "nyrissa_can_be_saved_hint": false,
    "nyrissa_backstory_known": false,
    "collection_complete": false,
    "storyteller_token_received": false
  },
  "recipes_known": [],
  "ingredients_in_camp_stores": {},
  "weather_today": "clear",
  "current_season": "spring"
}
```

---

## 🗺️ DAY-BY-DAY TRAVEL SYSTEM

**DM RULE:** Multi-day journeys are NEVER summarized in one paragraph. Each day is its own scene with player input before advancing. Do not skip to the destination.

### Daily Travel Format

```
BEFORE displaying the status block each morning:
  → Run the 4-step weather procedure above (Precipitation → Temperature → Event → Announce)
  → Record result in weather_today field of the save block
  → Apply travel time penalties immediately if Heavy Rain or worse

╔══════════════════════════════════════════════════════╗
║  JOURNEY — DAY [X] OF [Y] TO [DESTINATION]          ║
║  Mode: Exploration | Time: [Morning/Noon/Afternoon]  ║
╠══════════════════════════════════════════════════════╣
║  Progress : ~[X] miles from origin / [Y] miles left  ║
║  Resources: Rations [X] days | Water [status]        ║
║  Weather  : [Result from this morning's weather roll]║
║  Terrain  : [Current hex terrain type]               ║
╚══════════════════════════════════════════════════════╝
```

After displaying the status block, provide 2–3 paragraphs of atmospheric narration for the day's travel — include the weather condition in the narration, not just the stat block. Then present the daily choice menu.

### Daily Travel Choice Menu (minimum 10 options)

```
What do you do on Day [X]?
 1. Press on — maximum distance before nightfall
 2. Scout ahead — check next hex before entering [Survival DC 14]
 3. Investigate a point of interest along the route
 4. Forage for supplies [Survival DC 14 — success: 1d4 rations]
 5. Set up camp early — recover resources, rest fully
 6. Track signs of activity — bandits, monsters, settlements [Survival DC 12]
 7. Hunt for fresh game [Survival DC 13 — success: meat for 2d4 rations]
 8. Move at stealth pace — avoid detection [Stealth DC 14, half speed]
 9. Hustle — double distance, party gains Fatigued at day end
10. Engage companion conversation during travel
11. Treat wounds while walking [Medicine DC 15, companion required]
12. Custom action — describe what you do
```

**WAIT FOR PLAYER INPUT. Do NOT advance to the next day until the player makes a choice and that choice is resolved.**

### End-of-Day Camp Phase

After resolving the day's choice, present the camp setup. Then STOP and ask:

*"Day [X] complete. Camp is set. Do you want to take any camp activities before resting, or pass straight to sleep?"*

Only after the player's camp activities are resolved, advance to the next day's morning. Show the updated journey status block at the top of that response.

### Encounter During Travel

If the daily encounter roll triggers (see Random Encounter Tables above), interrupt the travel narration:

*"[Terrain encounter triggers mid-travel. Display encounter map, roll initiative.]*"

After the encounter resolves, return to the travel sequence at the point it was interrupted.


---

> **➡️ Exotic materials descriptions, NPC reactions, and the Armor Reaction rule → see `KM_Exploration_B.md`**

*KM_Exploration.md | Villain offscreen behavior → KM_DMRules.md*
