# KINGMAKER — CRAFTING SYSTEM
## KM_Crafting.md | Active from: Chapter 1 | Referenced by: KM_Actions.md, KM_Kingdom.md

> **DM:** Recipes are found as loot during exploration (on bodies, in chests, purchased from merchants, or discovered via `.examine`). The player crafts items during Downtime using materials + a Crafting check. Recipes are permanent once learned. Materials are consumable. The Mobile Base (KM_MobileBase.md) provides a crafting bench bonus when available.

---

## 📋 COMMANDS

`.craft` — Display known recipes, available materials, and start a crafting attempt.
`.recipes` — List all known recipes with material requirements.

---

## 📊 CRAFTING PROCEDURE

### Step 1 — Choose a Recipe
Player selects from known recipes (`.recipes`).

### Step 2 — Check Materials
Recipe lists required materials. Player must have all in inventory.

### Step 3 — Crafting Check
```
Roll: d20 + Crafting modifier vs Recipe DC
Crit Success: Item crafted + bonus property (DM generates — extra charge, improved quality)
Success:      Item crafted as described
Failure:      Materials consumed, item not created. 50% of material cost refunded as scrap.
Crit Failure: Materials consumed, item not created. Crafting mishap: 1d6 fire/acid damage.
```

### Step 4 — Time Cost
- **Simple recipes:** 1 Downtime day
- **Moderate recipes:** 2 Downtime days
- **Complex recipes:** 4 Downtime days
- **Crafting bench bonus** (Mobile Base upgrade): −1 day (min 1)

---

## 📦 MATERIAL TYPES

| Material | Found In | Common Sources |
|----------|---------|---------------|
| **Iron Ore** | Mining hexes, cave loot | Purchased from smiths (2 gp) |
| **Rare Wood** | Forest hexes, lumber camps | Old Sycamore, Narlmarches |
| **Monster Parts** | Combat loot (beasts, magical creatures) | Troll blood, wyvern scales, dire bear hide |
| **Alchemical Reagents** | Purchased, found in labs, herb gathering | Bokken, Jubilost, apothecaries |
| **Arcane Dust** | Disenchanting magic items, magical locations | Spell-touched ruins, ley line hexes |
| **Rare Herbs** | Herb gathering (Nature DC 14), specific hexes | Fangberry bushes, moon radish patches |
| **Gemstones** | Mining, treasure hoards, purchased | Diamond, ruby, sapphire (for enchantments) |
| **Exotic Hide** | Combat loot (specific creatures) | Wyrmskin, troll hide, basilisk scales |

---

## 📜 RECIPE LIST

### WEAPONS — TIER 1 (Ch1-2, Crafting DC 14-16)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Cold Iron Blade** | Iron Ore ×3 | 16 | 2 days | Cold Iron weapon (bypass DR/cold iron) |
| **Flaming Weapon Oil** | Alchemical Reagents ×2, Arcane Dust ×1 | 18 | 1 day | Apply: +1d6 fire for 1 hour |
| **Troll-Bane Arrow (×10)** | Iron Ore ×1, Alchemical Reagents ×1 | 14 | 1 day | Acid-coated, prevent troll regen 1 round |
| **Silversheen Coating** | Iron Ore ×1, Gemstones ×1 | 16 | 1 day | Apply: counts as silver for 1 hour |
| **Weighted Throwing Hammer (×3)** | Iron Ore ×2 | 14 | 1 day | Returning thrown weapon, 1d6+Str B, range 20 ft |

### WEAPONS — TIER 2 (Ch3-4, Crafting DC 18-20)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Wyvern Venom Blade** | Monster Parts (wyvern) ×2, Alchemical Reagents ×1 | 20 | 2 days | Poison: Fort DC 18 or Enfeebled 1 + Clumsy 1 |
| **Frost-Forged Weapon** | Iron Ore ×2, Rare Herbs ×1, Arcane Dust ×1 | 18 | 2 days | +1d6 cold. Creatures hit: Slowed 1 on crit |
| **Giant-Bane Oil** | Monster Parts (giant) ×2, Alchemical Reagents ×2 | 18 | 1 day | Apply: +2d6 damage vs Large+ creatures, 1 hour |
| **Thunderstone Arrow (×5)** | Iron Ore ×1, Arcane Dust ×1, Gemstones ×1 | 18 | 1 day | On hit: Fort DC 18 or Deafened 1 round + 1d6 sonic |
| **Barbed Net** | Iron Ore ×1, Exotic Hide ×1 | 16 | 1 day | Thrown: Immobilized (Escape DC 18), 1d4 piercing/round |

### WEAPONS — TIER 3 (Ch5+, Crafting DC 22+)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Bloom-Warded Blade** | Arcane Dust ×3, Rare Herbs ×2, Gemstones ×1 | 22 | 4 days | +2d6 vs fey/Bloom creatures. Immune to Bloom weapon corrosion |
| **Siege Bolt (×3)** | Iron Ore ×3, Alchemical Reagents ×2 | 20 | 2 days | Crossbow bolt that deals damage to structures/walls (2d12 to objects) |
| **Vorpal Oil** | Arcane Dust ×4, Gemstones ×2, Monster Parts ×2 | 24 | 4 days | Apply: on nat 20, Fort DC 22 or decapitated (kill). 1 use. |

### ARMOR & SHIELDS (Crafting DC 16-22)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Reinforced Shield** | Iron Ore ×2, Rare Wood ×1 | 18 | 2 days | Shield Hardness +2 |
| **Fire-Resistant Cloak** | Exotic Hide ×1, Alchemical Reagents ×1 | 16 | 1 day | Fire Resistance 5 for 1 day |
| **Troll-Hide Armor Patch** | Monster Parts (troll) ×2 | 18 | 2 days | Fast Healing 1 (wearer) for 1 combat/day |
| **Spell-Deflecting Buckler** | Iron Ore ×2, Arcane Dust ×2 | 20 | 3 days | Shield Block absorbs spell damage (not just physical) |
| **Camouflage Cloak** | Exotic Hide ×2, Rare Herbs ×1 | 16 | 2 days | +2 Stealth in wilderness hexes. Advantage on ambush checks |
| **Bloom-Ward Armor Oil** | Alchemical Reagents ×3, Rare Herbs ×2 | 22 | 2 days | Apply: Resist 5 to Bloom damage for 1 day |

### CONSUMABLES — TIER 1 (Ch1-2, Crafting DC 12-16)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Healing Salve (×3)** | Rare Herbs ×2 | 12 | 1 day | Heal 2d8+4 HP (applied, not spell) |
| **Antidote (×3)** | Rare Herbs ×1, Alchemical Reagents ×1 | 14 | 1 day | Counteract poison (counteract +10) |
| **Blast Bomb** | Alchemical Reagents ×3 | 16 | 1 day | Thrown: 4d6 fire, 10-ft burst, Ref DC 16 half |
| **Smoke Bomb (×3)** | Alchemical Reagents ×1 | 12 | 1 day | 10-ft concealment cloud, 3 rounds |
| **Darkvision Elixir** | Rare Herbs ×1, Arcane Dust ×1 | 14 | 1 day | Darkvision 1 hour |
| **Alchemist's Kindness (×5)** | Rare Herbs ×1 | 12 | 1 day | Remove Sickened, nausea, hangover. Popular at feasts |
| **Tanglefoot Bag (×3)** | Alchemical Reagents ×2 | 14 | 1 day | Thrown: Immobilized 1 round, Ref DC 14 half |

### CONSUMABLES — TIER 2 (Ch3-4, Crafting DC 16-20)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Greater Healing Salve (×3)** | Rare Herbs ×3, Alchemical Reagents ×1 | 18 | 2 days | Heal 4d8+8 HP |
| **Elixir of Life** | Rare Herbs ×2, Gemstones ×1, Arcane Dust ×1 | 20 | 2 days | Heal 5d8+12 HP + remove 1 condition |
| **Frost Bomb** | Alchemical Reagents ×3, Rare Herbs ×1 | 18 | 1 day | Thrown: 4d6 cold, 10-ft burst, Slowed 1 on fail |
| **Invisibility Potion** | Arcane Dust ×2, Alchemical Reagents ×1 | 18 | 2 days | Invisible 10 min (breaks on attack) |
| **Thunderstone (×3)** | Iron Ore ×1, Alchemical Reagents ×2 | 16 | 1 day | 15-ft burst: Fort DC 16 or Deafened + Stunned 1 |

### CONSUMABLES — TIER 3 (Ch5+, Crafting DC 20+)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Breath of Life Scroll** | Arcane Dust ×4, Gemstones ×2 | 24 | 4 days | As Breath of Life spell (reaction, prevent death) |
| **War Paint of the Kellid** | Monster Parts ×2, Rare Herbs ×2 | 20 | 2 days | +2 Intimidation, +1 attack for 1 combat. Kellid tradition |
| **Philosopher's Stone Fragment** | Gemstones ×4, Arcane Dust ×3 | 26 | 4 days | Convert 1 base metal item to gold equivalent (100 gp value) |

### UTILITY (Crafting DC 14-22)

| Recipe | Materials | DC | Time | Result |
|--------|-----------|-----|------|--------|
| **Trap Kit** | Iron Ore ×1, Rare Wood ×1 | 14 | 1 day | 2d6 piercing, DC 16 Perception/Ref |
| **Signal Arrow (×5)** | Rare Wood ×1 | 12 | 1 day | Visible flare 500 ft. Army signals |
| **Feather Token (Tree)** | Rare Wood ×1, Arcane Dust ×2 | 18 | 2 days | Instant tree. Cover, climbing, bridge |
| **Expedition Tent** | Exotic Hide ×2, Rare Wood ×1 | 16 | 4 days | +2 to camp Survival checks |
| **Hex Ward Marker** | Arcane Dust ×2, Gemstones ×1 | 20 | 4 days | −25% random encounter rate in hex, permanent |
| **Portable Bridge** | Rare Wood ×3, Iron Ore ×2 | 18 | 4 days | Spans 30-ft gap. Reusable. 500 lb capacity |
| **Underwater Breathing Helm** | Iron Ore ×2, Arcane Dust ×2 | 20 | 3 days | Breathe underwater 8 hours. Reusable |
| **Compass of True North** | Iron Ore ×1, Gemstones ×1, Arcane Dust ×1 | 16 | 2 days | Never get lost. Navigation Survival DCs: auto-pass |
| **Kingdom Banner** | Rare Wood ×1, Exotic Hide ×1 | 14 | 2 days | Plant in hex: kingdom claim visible. Army Morale +1 if visible during battle |

---

## 📋 RECIPE DISCOVERY

Recipes are NOT automatically known. They must be found:

| Source | How |
|--------|-----|
| **Loot** | Found on bodies, in chests, or in dungeon rooms. DM adds to treasure as appropriate. |
| **Merchants** | Purchased from specialist vendors. Bokken sells alchemical recipes. Smiths sell weapon recipes. |
| **Examination** | Using `.examine` on a crafting bench, smith's tools, or alchemical lab may reveal a recipe (Perception DC 14). |
| **Companion gift** | At Devoted relationship, some companions share a personal recipe (Jubilost: Blast Bomb, Octavia: Darkvision Elixir). |
| **Kingdom event** | Some stronghold events (KM_StrongholdEvents.md) reward recipes. |
| **Quest reward** | Side quests may award unique recipes not available elsewhere. |

---

## ⚠️ DM RULES

1. **Don't flood recipes.** 1-2 per chapter is the right pace. The player should feel each discovery.
2. **Materials are loot.** Add them to treasure tables alongside gold and gear. 1-2 materials per significant encounter.
3. **Crafting is Downtime.** Cannot craft during travel, combat, or active scenes. Requires camp or settlement.
4. **Companion assist:** If a companion has Crafting proficiency, they can Aid (+1 to +4 based on proficiency).
5. **No infinite loops.** Crafted items cannot be disenchanted for more materials than they cost.

**Save block:** `"crafting": { "known_recipes": ["healing_salve", "cold_iron_blade"], "materials": {"iron_ore": 3, "rare_herbs": 2}, "crafting_queue": [] }`

---

*KM_Crafting.md — Kingmaker PF2e Text Adventure | Crafting System v1.0*
*Inspired by NWN2 crafting bench system. Recipes found, not known.*
