# KINGMAKER — STARTING GEAR SELECTION
## KM_StartingGear.md | Referenced by: KM_Builds.md

> **DM:** Run this AFTER build selection, BEFORE companion selection (Pick-10).
> Output the gear screen exactly as written. Player picks A or B.
> Write result to save block `inventory.gear[]` before continuing.
> Weapons and armor are already defined by the build — this covers mundane gear only.

---

## ⚙️ WHEN TO RUN

**After:** Build confirmed, character sheet displayed.
**Before:** Pick-10 companion selection.

---

## 📦 GEAR SELECTION SCREEN

> ⛔ **Output this screen exactly. Do not paraphrase or summarize.**

```
════════════════════════════════════════════════════════════
STARTING GEAR
Your weapons and armor are already set. Now choose what you carry.

[A] CLASS KIT — Standard adventuring kit for your class. Free.
    Fully equipped. Nothing to decide. Start immediately.

[B] BUY YOUR OWN — Spend your 15 gp however you like.
    DM confirms your list and totals before continuing.

[C] PRESET PACK — Pick one named pack (P1–P12). Bundle price
    deducted from 15 gp; any remainder carries over.
    See KM_Items_Mundane.md § PRESET ADVENTURING PACKS.

Type A for class kit, B to buy your own, or C for a preset pack.
════════════════════════════════════════════════════════════
```

---

## 🎒 CLASS KITS (Option A)

All kits include the **Adventurer's Pack:**
```
Backpack | Bedroll | Chalk ×10 | Flint & Steel
Rope 50 ft | Rations ×14 | Torch ×5 | Waterskin
```

Plus class-specific additions:

| Class | Class Addition |
|-------|----------------|
| Alchemist | Alchemist's Tools, Formula Book (2 starter formulas) |
| Animist | Holy Symbol, Writing Kit |
| Barbarian | — |
| Bard | Musical Instrument (lute, horn, or drum — player's choice) |
| Champion | Holy Symbol, Religious Text |
| Cleric | Holy Symbol, Religious Text |
| Commander | — |
| Druid | Druidic Focus (Holly & Mistletoe) |
| Exemplar | — |
| Fighter | Healer's Tools |
| Guardian | — |
| Gunslinger | Cleaning Kit, Ammunition ×20 (extra) |
| Inventor | Crafting Tools |
| Investigator | Writing Kit, Magnifying Glass |
| Kineticist | — |
| Magus | Writing Kit |
| Monk | — |
| Oracle | Holy Symbol |
| Psychic | Writing Kit |
| Ranger | Hunting Trap ×2, Survival Toolkit |
| Rogue | Thieves' Tools |
| Sorcerer | — |
| Summoner | — |
| Swashbuckler | — |
| Thaumaturge | — |
| Witch | — |
| Wizard | Spellbook (4 cantrips + 2 spells), Writing Kit |

> **Gold:** Class kit is standard issue — no charge. Your 15 gp carries over.

---

## 🛒 BUY YOUR OWN (Option B)

⛔ **INPUT FORMAT LOCK — ENFORCEMENT GATE**
Numbered shopping-cart menu only. Player types ONE item number per turn (or `D` for done, `R` for remove, `★` for build-default cart).
BANNED INPUT FORMATS (any of these = `.fail 38`):
  ✗ "List what you want and the DM will total it up"
  ✗ "List items → DM totals → confirm"
  ✗ Asking the player to free-text item names in any form
  ✗ Asking for all picks in a single message

REQUIRED FORMAT: Output the numbered menu below verbatim. After each pick, output the
updated cart with running total + menu again. Continue until player types `D` (Done).

```
════════════════════════════════════════════════════════════
BUY YOUR OWN — pick ONE item per turn (cart mode)
Budget: 15 gp 0 sp | Spent: 0 gp 0 sp | Remaining: 15 gp 0 sp

 [1]  Adventurer's Pack (full bundle)         1 gp 5 sp
 [2]  Healer's Tools                          5 gp     ← Medicine in combat
 [3]  Thieves' Tools                          3 gp
 [4]  Alchemist's Tools                       3 gp
 [5]  Crafting Tools                          4 gp
 [6]  Writing Kit                             1 gp
 [7]  Magnifying Glass                        2 gp
 [8]  Musical Instrument (common, lute)       5 gp
 [9]  Holy Symbol (wooden)                    1 sp
 [10] Holy Symbol (silver)                    2 gp
 [11] Hunting Trap (each)                     2 sp
 [12] Rope 50 ft (hemp)                       1 sp
 [13] Rope 50 ft (silk)                       1 gp
 [14] Rations (1 week)                        4 sp
 [15] Torch (each)                            1 cp
 [16] Lantern (hooded)                        7 sp
 [17] Oil (per flask)                         1 cp
 [18] Compass                                 1 gp
 [19] Bedroll                                 1 sp
 [20] Waterskin                               5 cp
 [21] Crowbar                                 5 sp
 [22] Grappling Hook                          1 sp
 [23] Flint & Steel                           5 cp
 [24] Chalk (10 pieces)                       1 cp
 [25] Alchemical Fire (each)                  1 gp     ← trolls, Ch2
 [26] Acid Flask (each)                       1 gp
 [27] Minor Healing Potion                    4 gp

 ★ BUILD DEFAULT (one-press cart) — picks the build's recommended kit
   for this class from the build file's "Starting Gear (15 gp)" line.
   Type ★ to fill the cart with the default, then `D` to confirm.

 [R] Remove last item    [D] Done — finalize cart
════════════════════════════════════════════════════════════
```

**DM workflow for Option B (cart mode):**
1. Output menu verbatim. Cart starts empty.
2. Player types one number `1`–`27`, or `★`, or `R`, or `D`.
3. Add/remove from cart. Recompute spent/remaining (auto-deny if pick > remaining).
4. Re-output the menu with updated header line + cart contents below it:
   ```
   CART:
     • Adventurer's Pack    1 gp 5 sp
     • Healer's Tools       5 gp
   ```
5. Repeat until player types `D`. Then write `inventory.gear[]` and adjust `gold`.

> Quantities: items marked `each` may be picked multiple times — each press adds one.
> Over-budget pick: DM rejects with `Cannot afford [item] (need X gp, have Y gp).`

---

## 🎁 PRESET PACKS (Option C)

Twelve named bundles from `KM_Items_Mundane.md § PRESET ADVENTURING PACKS`.
Price is deducted from the 15 gp starting budget; remainder carries over.
Display the screen below verbatim, then wait for the player's pick.

```
════════════════════════════════════════════════════════════
PRESET PACKS — pick ONE (price comes out of your 15 gp)

 [P1]  Adventurer's Pack       — 7 gp   | 2 Bulk | baseline
 [P2]  Scholar's Pack          — 12 gp  | 1 Bulk | caster/investigator
 [P3]  Entertainer's Pack      — 9 gp   | 1 Bulk | bard/swash/rogue
 [P4]  Healer's Pack           — 15 gp  | 2 Bulk | cleric/druid/alchemist
 [P5]  Explorer's Pack         — 10 gp  | 2 Bulk | ranger/druid/wilderness
 [P6]  Infiltrator's Pack      — 18 gp  | 1 Bulk | rogue/investigator (−3 gp credit)
 [P7]  Hunter's Pack           — 13 gp  | 2 Bulk | ranger/barbarian/druid
 [P8]  Diplomat's Pack         — 22 gp  | 1 Bulk | noble/commander/bard (−7 gp credit)
 [P9]  Dungeoneer's Pack       — 14 gp  | 3 Bulk | fighter/champion/rogue
 [P10] Survivalist's Pack      — 16 gp  | 3 Bulk | long overland travel (−1 gp credit)
 [P11] Alchemist's Pack        — 20 gp  | 2 Bulk | alchemist/investigator (−5 gp credit)
 [P12] Siege/Soldier's Pack    — 11 gp  | 4 Bulk | fighter/champion/commander

 ⛔ Over-budget packs deduct the balance from future loot as an equipment
    advance. Player can still pick them. (Deficit tracked in save block.)

Type P1 – P12 to pick, or type BACK to return to A/B/C menu.
════════════════════════════════════════════════════════════
```

**DM workflow for Option C:**
1. Player types `P#`. Look up pack contents in `KM_Items_Mundane.md`.
2. Output the pack contents verbatim as a confirmation block.
3. Deduct price from 15 gp. If pack costs > 15 gp, create `equipment_advance` debt in save block (tracked below).
4. Write pack items to `inventory.gear[]` as individual items (expand the bundle).
5. Proceed to Pick-10.

**Equipment advance debt (packs > 15 gp):**
```json
"equipment_advance_gp": 5,  // e.g., P8 Diplomat's Pack (22 gp) - 15 gp = 7 gp debt
"advance_source": "starting_gear_preset_pack",
"advance_reclaim": "first_loot_pool"
```
Debt is reclaimed from the first kingdom-turn / first chapter loot. No interest. Player can pay off voluntarily by selling gear or donating from own stash.

---

## 💾 SAVE BLOCK — WRITE RESULT

After the player confirms their gear, update the save block before continuing:

```json
"inventory": {
  "weapons": ["(from build)"],
  "armor":   ["(from build)"],
  "gear":    ["list items here"],
  "consumables": [],
  "magic_items": [],
  "quest_items": ["Jamandi Aldori's Letter (sealed)"]
},
"gold": { "gp": 15, "sp": 0, "cp": 0 }
```

> Adjust `gold` if player spent from 15 gp (Option B purchases).
> The letter is always present — it is how eRmaC was invited.

---

*KM_StartingGear.md — Kingmaker PF2e Text Adventure | Starting Gear v1.0*
