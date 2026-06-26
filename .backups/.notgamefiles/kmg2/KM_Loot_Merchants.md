# KINGMAKER — MERCHANT INVENTORIES
## KM_Loot_Merchants.md | Referenced by: KM_Exploration.md, KM_Ch1.md–KM_Ch4.md, KM_Vendors.md

> **DM:** Merchant inventory file. Holds shop format, named-vendor stock lists, and vendor availability by chapter. Pair-load with `KM_Loot_Merchants_B.md` whenever random loot rolls are also needed (Common / Magic / Rare / Epic / Legendary tier d100 / d20 rollable tables live in part B).

---


> **DM:** Use this file whenever the player visits a vendor. Show the full shop
> screen using the format below. Every vendor has: a base stock list with prices,
> restock rules, and a build-relevant callout so the DM can flag items useful to
> the player's specific build without inventing anything.
>
> **Price rule:** Buy at listed price. Sell back at 50% unless noted.
> **Discount rule:** Apply discounts after reputation/quest triggers (noted per vendor).
> **Out of stock:** Mark items as [SOLD] in your session notes. Restock on the schedule listed.

---

## 🛒 SHOP SCREEN FORMAT

```
╔══════════════════════════════════════════════════════════╗
║  🏪 [VENDOR NAME] — [Location]                           ║
║  Relationship: [Neutral/Friendly/Hostile]                ║
╠══════════════════════════════════════════════════════════╣
║  CONSUMABLES                                             ║
║  [Item]...........................[Price]  [Stock]        ║
╠══════════════════════════════════════════════════════════╣
║  EQUIPMENT                                               ║
║  [Item]...........................[Price]  [Stock]        ║
╠══════════════════════════════════════════════════════════╣
║  SERVICES                                                ║
║  [Service]........................[Price]                ║
╠══════════════════════════════════════════════════════════╣
║  YOUR GOLD: [X] gp   ║  SELL (50% value): [list items]  ║
╚══════════════════════════════════════════════════════════╝
```

---

## OLEG'S TRADING POST
**Location:** Hex (1,0) | **Available:** Chapter 1 onward
**Relationship base:** Friendly (Oleg trusts adventurers; Svetlana is warmer)
**Restock:** Weekly (every 7 in-game days). Rare items rotate monthly.

### Base Stock (Ch1 — always available)

**CONSUMABLES**
| Item | Effect | Price | Stock |
|------|--------|-------|-------|
| Healing Potion (Minor) | 1d8 HP | 4 gp | 5 |
| Antitoxin (Lesser) | +2 vs poison 1 hr | 3 gp | 3 |
| Alchemist's Fire (Lesser) | 1d8 fire + splash | 3 gp | 4 |
| Torch ×10 | Light, 1 hr each | 1 sp | Unlimited |
| Rations (1 week) | Trail food | 5 sp | Unlimited |
| Rope (50 ft, hemp) | Climb/tie | 1 sp | 5 |
| Antiplague | +2 vs disease 1 hr | 3 gp | 2 |
| Smokestick (Lesser) | Concealment cloud | 2 gp | 2 |

**EQUIPMENT**
| Item | Stats | Price | Stock |
|------|-------|-------|-------|
| Shortsword | 1d6 P/S, agile, finesse | 9 gp | 2 |
| Handaxe | 1d6 S, agile, thrown 10 | 6 gp | 2 |
| Dagger ×3 | 1d4 P/S, agile, thrown | 6 gp | 10 |
| Light Crossbow | 1d8 P, range 80 ft | 3 gp | 2 |
| Crossbow bolts ×20 | — | 2 sp | Unlimited |
| Leather Armor | AC+1, Dex cap 4 | 2 gp | 2 |
| Studded Leather | AC+2, Dex cap 3 | 3 gp | 1 |
| Wooden Shield | AC+2, Hard 3, HP 12 | 1 gp | 2 |
| Steel Shield | AC+2, Hard 5, HP 20 | 2 gp | 1 |
| Healer's Tools | For Medicine checks | 5 gp | 2 |
| Adventurer's Pack | Rope, torch, bedroll, rations | 7 gp | 3 |
| Crowbar | +2 Athletics (pry) | 5 sp | 2 |
| Grappling Hook | Required for some climbs | 1 sp | 2 |

**After first kingdom turn — added stock:**
| Item | Stats | Price | Stock |
|------|-------|-------|-------|
| Healer's Tools (Expert) | +1 item to Medicine | 50 gp | 1 |
| +1 weapon (rotates weekly) | DM rolls d6: 1 Shortsword, 2 Handaxe, 3 Longsword, 4 Spear, 5 Crossbow, 6 Morningstar | 20 gp | 1 |
| Healing Potion (Lesser) | 2d8+5 HP | 12 gp | 3 |

**Discounts:**
- Svetlana's Ring returned: 10% off all purchases permanently
- Bandits dealt with: Oleg adds 2 extra minor potions to stock weekly

**Build callouts:**
- Build 1/3/4: Steel Shield in stock at launch. +1 weapon rotation may hit Waraxe or Morningstar.
- Build 10: Healer's Tools Expert is a priority buy at kingdom turn.
- Build 6: Crossbow + bolts available for backup ranged.

---

## BOKKEN'S HUT
**Location:** Hex (1,−1) | **Available:** Chapter 1 onward
**Relationship base:** Neutral (eccentric, wary of strangers)
**Restock:** Every 5 in-game days. Limited supply — he brews himself.

### Base Stock

**CONSUMABLES**
| Item | Effect | Price | Stock |
|------|--------|-------|-------|
| Healing Potion (Minor) | 1d8 HP | 4 gp | 3 |
| Healing Potion (Lesser) | 2d8+5 HP | 12 gp | 2 |
| Antitoxin (Lesser) | +2 vs poison | 3 gp | 3 |
| Alchemist's Fire (Lesser) | 1d8 fire + splash | 3 gp | 4 |
| Liquid Ice (Lesser) | 1d6 cold + splash, extinguish fire | 3 gp | 2 |
| Tanglefoot Bag | Immobilized (Athletics DC 14 to escape) | 3 gp | 2 |
| Bottled Lightning | 1d6 electricity + splash, Dazzled | 3 gp | 2 |

**After Fangberries delivered — 25% discount on all items permanently.**
**After Moon Radishes delivered — free 1 Minor Healing Potion per day for 30 days.**
**After Bokken's Brother quest — adds:**
| Item | Effect | Price | Stock |
|------|--------|-------|-------|
| Elixir of Life (Lesser) | 3d6+6 HP + resist disease | 25 gp | 1 |
| Darkvision Elixir (Lesser) | Darkvision 1 hr | 13 gp | 2 |
| Smokestick (Lesser) | Concealment cloud | 2 gp | 3 |

**Build callouts:**
- All builds: Tanglefoot Bag is excellent utility early game.
- Build 9 (Kineticist): Liquid Ice = his specialty. Builds 11/14: No key items — he's mundane alchemy only.

---

## OLD BELDAME (SWAMP WITCH HUT)
**Location:** Hex (−2,−1) | **Available:** Chapter 1+ after quest or DC 14 Diplomacy
**Relationship base:** Hostile → Neutral (quest complete) → Friendly (mushrooms first)
**Restock:** Monthly. Rare items do not restock unless she finds materials.

### Base Stock (after quest)

**CONSUMABLES & SCROLLS**
| Item | Effect | Price | Stock |
|------|--------|-------|-------|
| Potion of Invisibility | Invisible 5 min | 80 gp | 1 |
| Darkvision Elixir (Greater) | Darkvision 8 hr | 45 gp | 1 |
| Scroll of Fear (L1) | Frightened 2, Will DC 17 | 4 gp | 2 |
| Scroll of Slow (L3) | Slowed 1, Will DC 19 | 30 gp | 1 |
| Scroll of Vampiric Touch (L3) | 6d6 neg, you gain HP | 30 gp | 1 |
| Scroll of Confusion (L4) | Random actions, Will DC 21 | 70 gp | 1 |
| Swamp Witch's Brew recipe | Camp recipe (rare healing stew) | 15 gp | 1 |

**WONDROUS ITEMS**
| Item | Effect | Price | Stock |
|------|--------|-------|-------|
| Amulet of Natural Armor (+1) | +1 untyped AC | 160 gp | 1 |
| Cloak of Elvenkind | +2 Stealth, dim light advantage | 55 gp | 1 |
| Witch's Familiar Focus | +1 to Witch hex DCs | 50 gp | 1 |
| Bracers of Armor (+1) | +1 AC unarmored | 160 gp | 1 |

**Build callouts:**
- Build 11 (Witch): Witch's Familiar Focus is mandatory buy. Scroll of Slow excellent pick.
- Build 14 (Psychic): Scroll of Confusion extends your control kit.
- Build 7 (Magus): Potion of Invisibility for escape/setup.
- Builds 1–5 (Martials): Amulet of Natural Armor is a meaningful AC boost.

---

## BARTHOLOMEW DELBIN (SECLUDED LODGE)
**Location:** Hex (3,1) | **Available:** Chapter 2, after Nature of the Beast quest
**Relationship base:** Friendly (eccentric noble, loves demonstrations of power)
**Restock:** Does not restock — limited personal collection.

### Stock (one-time purchases)

| Item | Effect | Price | Stock |
|------|--------|-------|-------|
| Potion of Fire Breath | 4d6 fire breath, 15-ft cone, Ref DC 20 | 50 gp | 3 |
| Scroll of Burning Hands (L1) | 2d6 fire, 15-ft cone, Ref DC 17 | 4 gp | 4 |
| Scroll of Fireball (L3) | 6d6 fire, 20-ft burst, Ref DC 19 | 30 gp | 2 |
| Wand of Produce Flame (L1, 10 charges) | Produce Flame per charge | 90 gp | 1 |
| Worg Pelt Cloak | +1 circ. Intimidation vs animals/beasts | 20 gp | 1 |

**Build callouts:**
- Build 7 (Magus): Scroll of Fireball for Spellstrike burst.
- Build 9 (Kineticist): Potion of Fire Breath is excellent action economy for AoE.
- Build 6 (Thaumaturge): Wand of Produce Flame fills ranged slot cheaply.

---

## PITAX BLACK MARKET
**Location:** Pitax (Ch5, infiltration path only)
**Relationship base:** Suspicious (you are a foreigner; wrong move = combat)
**Restock:** Does not restock — underground supply.
**Warning:** If any item is recognized by a guard while in Pitax (Perception DC 18), causes an incident. Flagged items are noted.

### Stock

**CONSUMABLES**
| Item | Effect | Price | Notes |
|------|--------|-------|-------|
| Potion of Invisibility ×5 | Invisible 5 min each | 65 gp each | Flagged if found |
| Potion of Gaseous Form | Become gas 5 min (escape only) | 90 gp | |
| Assassin's Elixir | +2d6 precision on first strike next round | 50 gp | Flagged |
| Black Lotus Extract (poison, 1 dose) | Fort DC 22 or Paralyzed 1 min | 150 gp | Highly flagged |
| Sovereign Glue (1 dose) | Permanently bonds two surfaces | 90 gp | |

**WEAPONS & WONDROUS**
| Item | Stats | Price | Notes |
|------|-------|-------|-------|
| +1 Striking Poisoned Blade (Shortsword) | 2d6+1d4 poison on hit | 220 gp | Flagged |
| Scroll of Dominate (L6) | Dominated, Will DC 24 | 300 gp | Flagged |
| Ring of Feather Falling | Feather Fall at will | 225 gp | |
| Stolen +2 Rapier (no rune, masterwork) | 1d6+2, finesse | 180 gp | Flagged — recognized by Pitax guard captain |
| Portable Disguise Kit (masterwork) | +3 circ. Deception (disguise) | 45 gp | |

**Build callouts:**
- Build 13 (Rogue): Assassin's Elixir + Poisoned Blade is massive opening burst.
- Build 7 (Magus): Scroll of Dominate for Spellstrike control.
- All builds: Potion of Gaseous Form is emergency escape only.

---

## CAPITAL SHOPS (after kingdom buildings)

### Smithy
**Restock:** Weekly. Scales with kingdom Economy rank.

| Item | Stats | Price |
|------|-------|-------|
| Any martial weapon (common) | Standard stats | PF2e standard |
| Ammunition (arrows/bolts/bullets ×20) | — | 2 sp |
| Repair Kit | Restore weapon/armor HP | 2 gp |
| Masterwork weapon (+1 to hit, no rune) | +1 circumstance to attack | 35 gp |
| +1 weapon (single type, see Economy) | +1 item bonus attack | 20 gp |
| Scale Mail | AC+4, Dex cap 2 | 4 gp |
| Chain Mail | AC+4, Dex cap 1 | 6 gp |
| Full Plate | AC+6, Dex cap 0 | 30 gp |

### Market
**Restock:** Daily. −10% vs standard PF2e.

All mundane equipment from PF2e Player Core at −10%:
Tools, rope, lanterns, instruments, thieves' tools, climbing gear, camping equipment, disguise kits.

### Temple (any deity)
**Restock:** Weekly.

| Item | Effect | Price |
|------|--------|-------|
| Healing Potion (Minor) | 1d8 HP | 4 gp |
| Healing Potion (Lesser) | 2d8+5 HP | 12 gp |
| Healing Potion (Moderate) | 3d8+10 HP | 50 gp |
| Holy Water (Lesser) | 1d6 good vs undead/fiend | 3 gp |
| Scroll (L1, deity-appropriate) | DM selects from tradition | 4 gp |
| Scroll (L2, deity-appropriate) | DM selects from tradition | 8 gp |

### Caster's Tower (if built)
**Restock:** Monthly. +20% premium over standard.

| Item | Price |
|------|-------|
| Scrolls L1–L8 (any tradition, on request) | 4/8/16/30/70/140/300/650 gp |
| Wands (L1–L4, common spells) | 90/360/1440/5760 gp |
| +1 magic item (type: DM rolls on loot table Magic tier) | 20–55 gp |
| +2 magic item (type: DM rolls on loot table Rare tier) | 160–650 gp |
| Identifying unknown magic items (Arcana DC 20) | 10 gp flat fee |

### Tannery (if built)
**Restock:** Weekly. −15% on leather goods.

| Item | Stats | Price |
|------|-------|-------|
| Leather Armor | AC+1, Dex cap 4 | 1 gp 7 sp |
| Studded Leather | AC+2, Dex cap 3 | 2 gp 5 sp |
| Hide Armor | AC+3, Dex cap 2 | 1 gp 7 sp |
| Cloak (traveling) | Cold weather resist | 1 gp |
| Backpack (large) | +2 Bulk capacity | 2 gp |
| Bandolier | 8 item slots, quick draw | 1 sp |

---

## HASSUF — WANDERING MERCHANT
**Location:** Appears at Oleg's. First visit Day 10–14, then every 14 in-game days.
**Relationship base:** Neutral — sells to anyone, no loyalty
**Restock:** Full rotation each visit. Previous stock is gone.

| Item | Stats | Price | Notes |
|------|-------|-------|-------|
| Kukri ×2 | 1d6 S, agile, finesse | 6 gp | Nok-Nok's preferred weapon |
| Composite Longbow | 1d8 P, range 100 ft, propulsive | 20 gp | Upgrade over Oleg's longbow |
| Falchion | 1d10 S, forceful, sweep | 3 gp | Two-handed martial |
| Chain Mail | AC+4, Dex cap +1, ACP −2 | 6 gp | Best heavy armor available Ch1 |
| Elixir of Life (Lesser) | 3d6+6 HP + resist disease 10 min | 25 gp | 50% chance per visit |
| Potion of Invisibility | Invisible 5 min | 80 gp | 25% chance per visit |
| Tanglefoot Bag (Moderate) | Immobilized DC 17 | 8 gp | — |
| Thieves' Tools (Infiltrator) | +2 item Thievery (pick locks) | 35 gp | 1 per visit |

**Build callouts:** Build 13 (Rogue): Kukri pair + Infiltrator Tools. Build 3 (Ranger): Composite Longbow. Builds 1–5: Chain Mail is the only non-capital heavy armor in Ch1.

---

## DRAGN — DWARVEN SMITH
**Location:** Capital (near smithy district). **Available:** Ch2+ after Trobold cleared.
**Relationship base:** Friendly. **Restock:** Monthly. Dwarven-craft only.

| Item | Stats | Price |
|------|-------|-------|
| Dwarven Waraxe +1 | 1d8+1 S, sweep, versatile P | 35 gp |
| Warhammer +1 | 1d8+1 B, shove | 30 gp |
| Full Plate (Dwarven-forged) | AC+6, ACP −2 (reduced from standard) | 45 gp |
| Adamantine Shield (Lesser) | Hardness 10, HP 40 | 160 gp |
| Dwarven Ale (restorative) | Remove Fatigued condition | 5 gp |
| Repair Kit (Dwarven) | Restore 10 Hardness to any item | 8 gp |

**Build callout:** Build 5 (Champion): Adamantine Shield — Shield Block becomes near-invincible. Builds 1/2/4: Dwarven Full Plate is the best non-magical heavy armor until Ch3+.

---

## VERDEL — CAPITAL WONDROUS GOODS
**Location:** Capital (market district). **Available:** Ch2+ after Market building.
**Relationship base:** Neutral. **Restock:** Monthly. Wondrous items only.

| Item | Effect | Price |
|------|--------|-------|
| Cloak of Resistance (+1) | +1 item bonus all saves | 80 gp |
| Amulet of Natural Armor (+1) | +1 untyped AC | 160 gp |
| Ring of Protection (+1) | +1 circ. AC and saves | 160 gp |
| Hat of Disguise | Cast Illusory Disguise 1/day | 160 gp |
| Gloves of Storing | Store 1 item (1 Bulk); free action retrieve | 90 gp |
| Bag of Holding (Type I) | Holds 25 Bulk, weighs 1 Bulk | 75 gp |
| Bracers of Armor (+1) | +1 item AC (unarmored only) | 160 gp |

**Build callout:** All builds: Cloak of Resistance is a universal priority. Build 9 (Kineticist): Bracers of Armor stack with unarmored kineticist. Build 11 (Witch): Hat of Disguise extends infiltration options.

---

## 📋 VENDOR AVAILABILITY BY CHAPTER

| Vendor | Ch1 | Ch2 | Ch3 | Ch4 | Ch5 |
|--------|-----|-----|-----|-----|-----|
| Oleg's Trading Post | ✓ | ✓ | ✓ | — | — |
| Bokken | ✓ | ✓ | — | — | — |
| Old Beldame | ✓* | ✓ | ✓ | — | — |
| Hassuf (wandering) | ✓ | ✓ | ✓ | ✓ | — |
| Bartholomew Delbin | — | ✓* | ✓ | — | — |
| Dragn (dwarven smith) | — | ✓* | ✓ | ✓ | — |
| Verdel (wondrous goods) | — | ✓* | ✓ | ✓ | — |
| Varnhold Stockade | — | — | ✓* | — | — |
| Pitax Black Market | — | — | — | — | ✓* |
| Capital Smithy | — | ✓* | ✓ | ✓ | ✓ |
| Capital Market | — | ✓* | ✓ | ✓ | ✓ |
| Capital Temple | — | ✓* | ✓ | ✓ | ✓ |
| Caster's Tower | — | — | ✓* | ✓ | ✓ |
| Tannery | — | ✓* | ✓ | ✓ | ✓ |

*= available after quest/building unlock. Varnhold Stockade = one-time only.

*= available after quest/building unlock. See chapter files for triggers.

---

## 📚 EXPANDED ITEM STOCK — WHO SELLS WHAT

> **DM:** Items from `KM_Items_Expanded.md` and `KM_Items_Wilderness.md` are
> distributed to vendors by theme. Use this table to decide what a given
> merchant has in stock when the player asks for a specific item type.
> Default: rotate 3–5 items from the listed section per visit.

| Vendor | KM_Items_Expanded.md sections | KM_Items_Wilderness.md sections |
|--------|-------------------------------|-------------------------------|
| Oleg's Trading Post | Utility (Travel, Survival); Bandolier basics | River/Travel; Bandolier/Quiver; Herbalism (common) |
| Bokken (Ch1+) | — | Herbalism (formulas + stock L1–3) |
| Old Beldame (Ch1+) | Cursed items identification; low-level spellhearts | Herbalism (rare); Fey Charms; Dreaming Moss |
| Hassuf (wandering) | Eye slot items (L3–5); low rods | Bandolier (enchanted); Potion Bandolier |
| Bartholomew Delbin (Ch2+) | Magical Utility (Communication, Detection) | — |
| Dragn (dwarven smith, Ch2+) | Expanded rods (weapon-form); bandolier gear | Mount barding; bridle/horseshoes |
| Verdel (wondrous, Ch2+) | Spellhearts (full range); Eye slot; Magical Utility | Noble/Ceremonial; Festival Mask |
| Caster's Tower (Ch2+) | Staves (expanded); Rods (expanded); Spellhearts | Fey Charms (cold iron, salt-iron coin) |
| Capital Market (Ch2+) | Magical Utility (Crafting, Downtime) | Mount/Familiar gear; Bandolier (deluxe) |
| Capital Temple (Ch2+) | Magical Utility (Detection — Anathema Censer, Bloodhound's Whistle) | Herbalism (blessed); Cold Iron Circlet |
| Tannery (Ch2+) | — | Mount barding (leather/chain); saddles |
| Varnhold Stockade (Ch3 only) | Cursed items (1–2 genuine); rare staff | River/travel gear (worn-out but functional, discounted) |
| Pitax Black Market (Ch5) | Cursed items; Dust of Sneezing; Tyrant's Seal | Fey-Blooded Wine; Nightshade Dust |
| Kingdom Advisor Rewards | — | Kingdom & Stronghold Gear (earned, not bought) |

**v1.2 — new item files:** KM_Items_Mundane (QoL/tools/food/packs), KM_Items_Traps (traps + snares), KM_Items_APPulls (Stolen Fate/Sky King/etc). Each has a DM NOTES § PLACEMENT listing vendor stock. Starting gear Option C = KM_Items_Mundane § PRESET ADVENTURING PACKS.

### Stock Rotation Rules

- **Common tier items** (price ≤ 50 gp): always in stock at listed vendors
- **Magic tier** (50–500 gp): 50% chance per visit; rotates monthly
- **Rare tier** (500–5000 gp): 25% chance per visit; rotates per chapter
- **Cursed items:** Never in friendly merchant stock. Found in tombs, evil
  NPC possessions, haunted locations, or sold only by Pitax Black Market
  (and the seller may or may not know the item is cursed)
- **Kingdom & Stronghold Gear:** Most items are built during Kingdom turns
  using BP, not purchased. See KM_Kingdom.md for build costs.

### Formula Availability (for Crafting)

| Formula Type | Source |
|--------------|--------|
| Herbalism (poultices, salves) | Bokken, Old Beldame, any druid circle |
| Spellhearts | Caster's Tower, magical theorists, fey archives |
| Noble/Ceremonial | Court tailors in Restov, Mivon, New Stetven |
| Mount/Familiar | Dragn (barding), Capital stables (saddles), Verdel (collars) |
| River/Travel | Oleg's, Capital Market, any boatwright |
| Fey Charms | Old Beldame, First World caches, Nyrissa's territory |

---

*KM_Loot_Merchants.md — Merchant Inventories Section v1.1*
*Updated: Added vendor cross-reference for KM_Items_Expanded.md and KM_Items_Wilderness.md.*

*KM_Loot_Merchants.md — Kingmaker PF2e Text Adventure | Merchant Inventories v2.0 (split — pair-load with KM_Loot_Merchants_B.md)*
