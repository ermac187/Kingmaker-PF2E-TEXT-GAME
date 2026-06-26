# KINGMAKER — LOOT OPTIONS & ITEMS GEAR REFERENCE
## KM_Loot_Items_Ref.md | Companion Give Logic + Give/Identify/Hold Rules
## PAIR-LOAD WITH KM_Loot_Items_Ref_B.md (tool tiers + gear tables + Ch3–5 vendors)

> **DM:** Load this file when player selects Give/Identify/Hold on loot screen,
> buys tools or alchemical gear, or shops in Ch3+ locations.


## 🎁 OPTION (4) — GIVE TO COMPANION: FULL RULES

### How to Generate the Sub-Menu

When the player selects (4), evaluate every active companion against the item.
Show only companions who pass the need check for this item type.
Each entry gets: the companion name, the ★/⚠️ marker, a **stat delta line** showing what changes mechanically, and a one-line reason in the companion's voice or as a tactical note.
Apply ★ and ⚠️ markers using the rules below before displaying the menu.

```
GIVE TO — [Item Name] ([Type] — [X gp])
  Companions who can use this:
  (4a) ★ [Name]  [stat delta]
       "[Reason]"
  (4b)   [Name]  [stat delta]
       "[Reason]"
  (4c) ⚠️ [Name]  [stat delta] — [Warning]
       "[Reason]"
  (4x) Cancel — return to main options

  ★ = Best fit — highest stat gain or strongest build synergy
  ⚠️ = Poor fit — item type conflicts with this companion's build or nature
```

### Stat Delta Line — Format Rules

The stat delta line shows **exactly what changes** if this companion equips the item. Compare the item's stats against the companion's currently equipped item in the same slot. Show only stats that change. Use green arrow (↑) for improvements, red arrow (↓) for downgrades.

```
STAT DELTA FORMAT:
  [Stat] [current] → [new]  |  [Stat] [current] → [new]

WEAPON EXAMPLE:
  (4a) ★ Valerie  Atk +12→+14 | Dmg 1d8+3→1d8+5 | Traits: +Shove
       "Sidearm. Shove trait pairs with her shield positioning."

ARMOR EXAMPLE:
  (4a) ★ Harrim   AC 20→22 | Dex Cap +1→+0 | Spd 25→20 | Chk −2→−3
       "Heavier plate. He doesn't move fast anyway."

WONDROUS EXAMPLE:
  (4b)   Linzi    Replaces: Cloak of Resistance +1 | Saves +1→+2
       "Better protection. She's always in range."

NO CURRENT ITEM (empty slot):
  (4a) ★ Tristian  New: Ring slot | +1 AC
       "Nothing in that slot. Anything helps."
```

**Stats to show per item type:**

| Item Type | Always Show | Show If Changed |
|-----------|-------------|-----------------|
| Weapon | Attack bonus, damage dice + modifier | Traits gained/lost, reach, MAP |
| Armor | AC bonus, Dex Cap | Speed penalty, Check penalty, Bulk |
| Shield | AC (raised), Hardness, HP | Shield Block damage absorbed |
| Wondrous | Primary effect | What it replaces (if slot occupied) |
| Consumable | Effect summary | — |
| Rune | Bonus granted | Stacks with or replaces |

**DM rule:** Never show a companion on the Give menu without their stat delta. The reason line is flavor — the delta is information. If you cannot calculate the delta, state `[stats not compared — check sheet]` instead of omitting.

**★ BEST FIT — award to exactly one companion per menu.** The companion who gains the largest mechanical benefit from this specific item relative to their current gear and build. Ties go to the companion with the lower current stat (they benefit more from the delta). If only one companion qualifies, they automatically receive ★.

**⚠️ POOR FIT — apply when the item is technically usable but conflicts with the companion's build, class, or nature.** The warning text is one short phrase appended after the reason line. See Poor Fit Trigger Table below. A companion can appear on the menu and still carry a ⚠️ — the player may give it anyway. The warning is information, not a lock.

---

### ⚠️ Poor Fit Trigger Table

| Item Type | Companion | Warning Text |
|-----------|-----------|-------------|
| Healing wand / healing scroll / healing potion | Jaethal | *"Undead — healing harms her"* |
| Healing wand / healing scroll / healing potion | Any undead companion | *"Undead — healing harms her/him"* |
| Divine scroll (positive energy) | Jaethal | *"Positive energy scroll — damages undead"* |
| Heavy armor | Octavia, Linzi, Lem, Regongar | *"Arcane spell failure applies"* |
| Heavy armor | Nok-Nok | *"Too large — she can't wear this"* |
| Strength-based weapon (requires Str 14+) | Linzi, Octavia, Lem | *"Low Str — attack penalty applies"* |
| Two-handed weapon | Nok-Nok, Linzi, Lem | *"Small size — two-handed becomes unusable"* |
| Melee weapon | Ekundayo | *"Ranged build — melee weapons rarely fire"* |
| Melee weapon | Octavia | *"Blaster build — melee weapons rarely fire"* |
| Melee weapon | Kalikke, Kanerah | *"Blast build — melee weapons rarely used"* |
| Bow / ranged weapon | Valerie | *"Shield tank — frees neither hand for a bow"* |
| Bow / ranged weapon | Amiri | *"Melee-only build — bow wastes her rage"* |
| Scroll (tradition mismatch) | Any companion | *"Wrong tradition — [Name] cannot cast this"* — suppress entirely if total mismatch; show with ⚠️ only if companion has multiclass access |
| Alchemical bomb | Tristian, Valerie | *"Non-alchemist — no proficiency bonus"* |
| Wondrous item (already has this slot filled) | Any companion | *"Slot occupied — replaces [current item]"* |

**Suppress vs warn:** If an item is *unusable* (wrong size, no tradition access, Jaethal + healing), suppress the companion entirely — they should not appear on the list. ⚠️ is for items that *work mechanically* but are a poor investment. The Jaethal/healing case is the canonical suppress — she takes damage from positive energy, so a healing wand is never a valid give option for her and she never appears on that menu.

After player selects a companion or claims for themselves: the item **auto-equips immediately** if it fills the relevant slot and is a stat upgrade over the currently equipped item (or fills an empty slot). No second confirmation needed.

**Auto-equip rules — apply to player AND all companions:**

```
AUTO-EQUIP CONDITIONS (all must be true):
  1. Item is equipment (weapon, armor, shield, wondrous) — not a consumable
  2. Item fills a slot the character uses (weapon main/off, armor, shield, ring, etc.)
  3. Item is mechanically equal or better than the currently equipped item in that slot
     OR the slot is currently empty

IF AUTO-EQUIP FIRES:
  → Item moves from pending_loot to equipped_items
  → Stat block updates immediately (AC, attack, saves, etc.)
  → DM announces: "[Name] equips [Item]. [stat delta summary]."
  → If the slot was occupied: old item enters UNEQUIP CASCADE (see below)

IF AUTO-EQUIP DOES NOT FIRE (item is a downgrade or sidegrade):
  → Item moves to inventory (carried, not equipped)
  → DM announces: "[Name] takes [Item]. (Not equipped — current gear is better.)"
  → No cascade triggered

CONSUMABLES: Never auto-equip. Always go to inventory.
QUEST ITEMS: Never auto-equip. Always go to inventory.
```

**Player claim auto-equip:** When the player selects (1) Claim, the same logic applies. If the item is better than what they have in that slot, it equips and the old item enters the cascade. If it's worse or a sidegrade, it goes to inventory.

**Companion give auto-equip:** When the player gives via (4), the companion equips automatically if conditions are met. The companion does not refuse to equip a valid upgrade — the player made the decision for them.

**⛔ NO ORIGIN QUESTIONS:** When the player gives an item to a companion, the companion never asks where it came from, how the player obtained it, or why they have it. Items given from the loot queue are accepted without comment on their source. The companion may react to the item itself (what it is, what it does, whether they want it) but the origin is never raised. This applies to all item types — weapons, armor, wondrous items, consumables.

---

### 🔄 UNEQUIP CASCADE — REPLACED ITEMS

When any character (player or companion) equips a new item that replaces an existing equipped item in the same slot, the **replaced item** does not disappear. It enters an immediate redistribution cycle using the same Give logic as new loot.

**Trigger:** Any equip action that displaces a currently equipped item — from loot distribution, gear swaps, purchases, quest rewards, or manual inventory management.

**Cascade steps:**

```
1. Character equips new item → old item is unequipped
2. DM generates a HAND-ME-DOWN menu for the old item:

   🔄 HAND-ME-DOWN — [Old Item Name] ([Type] — [X gp])
     Unequipped by: [Name who replaced it]
     Companions who can use this:
     (a) ★ [Name]  [stat delta]
          "[Reason]"
     (b)   [Name]  [stat delta]
          "[Reason]"
     (c) ⚠️ [Name]  [stat delta] — [Warning]
     ─────────────────────────────
     (S) Sell (+[X] gp)
     (T) Treasury
     (D) Discard
     (X) Skip — hold in inventory

3. Player selects recipient or disposition
4. If recipient equips the hand-me-down AND it replaces THEIR item →
   cascade repeats for that item (new HAND-ME-DOWN menu)
5. Cascade continues until an item is sold, treasured, discarded,
   skipped, or no one qualifies
```

**Cascade depth:** No limit. A +2 sword replacing a +1 on the player, handed to Valerie, whose old sword goes to Harrim, whose old flail goes to treasury — valid 3-deep cascade. Each step gets its own menu.

**Auto-treasury:** If no companion qualifies (nobody passes need check), skip the menu. Item goes to treasury automatically. DM announces: `[Item] → Treasury (no one needs it). +[X] RP.`

**Player unequips count too.** When the player equips new gear that replaces their own, the old item enters the same cascade. No one is exempt.

**Who is evaluated:** All companions (Vanguard + Rearguard + Reserve). Reserve companions appear with a `[Reserve]` tag.

**Opinion Score effects:** Hand-me-down distribution follows the same 3-scenario scoring as new loot (Scenarios 1–3 below). Getting a hand-me-down still triggers +3 for the recipient. Being the ★ Best Fit and getting skipped still triggers −3. The item's origin as "used" does not reduce the opinion impact — gear is gear.

**Companion reactions to hand-me-downs:** Same reaction tables as new loot. DM may add one beat noting the item was someone else's. Amiri doesn't care. Valerie inspects it. Linzi notes the history. Nok-Nok checks if it's cursed. One line max.

---

### Relationship Effects on Item Distribution

Every time an item is distributed, the DM evaluates the scenario and applies Opinion Score changes to **all active companions** who qualified for the item. The system tracks three scenarios based on the player's choice.

---

#### SCENARIO 1 — ITEM GIVEN TO BEST FIT (★ companion receives)

The player gave the item to the companion the system marked as ★ Best Fit.

| Who | Opinion Change | Notes |
|-----|---------------|-------|
| **Recipient (★)** | **+3** | They got what they needed most. Gratitude is real. |
| **Non-recipients who wanted it mildly** (qualified but not ★) | **0** | No change. Fair is fair — they can see why. |
| **Non-recipients who wanted it badly** (qualified AND item would have been a major upgrade) | **−1** | Mild sting. They understand the logic. Still feels like a miss. |

**"Wanted it badly" definition:** The item would have improved their primary attack, AC, or save by +2 or more, OR replaced a broken/missing slot, OR connected to their personal quest or backstory.

**Romance/Brotherhood effect:** None. Giving to Best Fit is expected — competent, not personal.

---

#### SCENARIO 2 — ITEM GIVEN TO NON-BEST FIT (non-★ companion receives)

The player gave the item to someone who qualified but was NOT the ★ Best Fit. This is a personal choice — favoritism, friendship, or a gut call that overrides optimization.

| Who | Opinion Change | Romance/Brotherhood | Notes |
|-----|---------------|---------------------|-------|
| **Recipient (non-★)** | **+3** | **+1 Romance or Brotherhood** (if eligible and track is active) | They know they weren't the optimal pick. You chose them anyway. That lands. |
| **Non-recipients who wanted it mildly** (qualified, not ★, not recipient) | **−1** | — | Passed over AND it didn't even go to the best person. Friction. |
| **★ Best Fit who did NOT receive** | **−3** | — | They were the right choice and everyone knows it. Being skipped stings hard. |

**DM note:** The +1 Romance/Brotherhood on Scenario 2 only fires if the companion's Romance or Brotherhood track is already at Stage 1+. Giving a gift to someone at Stage 0 does not spontaneously open a track — it takes a personal moment for that.

---

#### SCENARIO 3 — ITEM KEPT, SOLD, OR SENT TO TREASURY

The player chose not to give the item to any companion. They kept it for themselves, sold it, or banked it as kingdom resources.

| Who | Opinion Change | Notes |
|-----|---------------|-------|
| **Companions who wanted it mildly** (qualified, not ★) | **−1** | Item existed, they could have used it, player chose gold or self over them. |
| **Companions who wanted it badly** (qualified AND major upgrade) | **−2** | Real need denied. Not a betrayal — but remembered. |
| **★ Best Fit denied** | **−3** | Maximum sting. They needed it, they were the right call, and the player chose the treasury. This is the loot decision that companions carry. |

**No Romance/Brotherhood effect.** Keeping loot for yourself is neutral on personal tracks — it's a strategic call, not a personal slight. But Opinion Score tracks it.

---

### Companion Reactions After Distribution

After the item transfer (or keep/sell) is logged, output **one short reaction line per companion** who qualified for the item. Tone scales with **both** their current Opinion Score **and** the scenario that just played out.

#### SCENARIO 1 — Best Fit Receives

**RECIPIENT (★, +3) reactions — scale by current score:**

| Score | Tone | Example |
|-------|------|---------|
| ≤ 5 | Professional relief | *"Good. I needed that."* |
| 6–10 | Practical warmth | *"Right call. I'll put it to work."* |
| 11–15 | Genuine, brief | *"You always know where things belong. Thanks."* |
| ≥ 16 | Personal, quiet weight | *"You pay attention. Don't think I don't notice."* |

**NON-RECIPIENT (0 or −1) reactions — scale by current score:**

| Score | Scenario | Tone | Example |
|-------|----------|------|---------|
| Any | 0 (didn't want it badly) | Neutral shrug | *"Makes sense."* — or nothing at all. |
| ≤ 5 | −1 (wanted it badly) | Flat, brief | *"Could've used that."* Then nothing. |
| 6–10 | −1 (wanted it badly) | Wry, accepts it | *"Next one's mine, yeah?"* |
| ≥ 11 | −1 (wanted it badly) | Good-natured | *"Fair enough. You know what you're doing."* |

#### SCENARIO 2 — Non-Best Fit Receives

**RECIPIENT (non-★, +3, +1 Romance/Brotherhood) reactions — scale by current score:**

| Score | Tone | Example |
|-------|------|---------|
| ≤ 5 | Surprised, cautious | *"...really? Alright then."* A beat of confusion that settles into something. |
| 6–10 | Surprised, warm | *"I wasn't expecting that. Thanks."* They hold it differently. |
| 11–15 | Touched, brief | *"You didn't have to do that."* They know exactly what it cost. |
| ≥ 16 | Quiet, personal | *"You chose me."* One sentence. It stays in the air. |

**★ BEST FIT DENIED (−3) reactions — scale by current score:**

| Score | Tone | Example |
|-------|------|---------|
| ≤ 5 | Cold, contained | *"Interesting choice."* They walk away. |
| 6–10 | Pointed, controlled | *"I would have used that better. You know that."* |
| 11–15 | Hurt under composure | *"Alright."* One word. The wrong weight. |
| ≥ 16 | Quiet wound | *"I thought—"* They stop. *"Never mind. It's fine."* It is not fine. |

**OTHER NON-RECIPIENTS (−1) reactions:**

| Score | Tone | Example |
|-------|------|---------|
| ≤ 5 | Mutters | *"Didn't even go to the right person."* |
| 6–10 | Dry observation | *"Bold choice."* They mean: wrong choice. |
| ≥ 11 | Shrug with an edge | *"Your call, Commander."* |

#### SCENARIO 3 — Kept / Sold / Treasury

**BEST FIT DENIED (−3) reactions — scale by current score:**

| Score | Tone | Example |
|-------|------|---------|
| ≤ 5 | Flat hostility | *"Sold it. Right."* They leave the room. |
| 6–10 | Pointed | *"I needed that and you know it."* No follow-up. |
| 11–15 | Controlled hurt | *"I suppose the treasury needed it more than I did."* |
| ≥ 16 | Disappointed | *"I wouldn't have asked. But I hoped you'd see."* |

**WANTED BADLY DENIED (−2) reactions:**

| Score | Tone | Example |
|-------|------|---------|
| ≤ 5 | Bitter | *"Another one for the pile."* |
| 6–10 | Resigned | *"Could've been useful. Guess not."* |
| ≥ 11 | Understanding but stung | *"Treasury it is. I get it."* They don't entirely get it. |

**WANTED MILDLY DENIED (−1) reactions:**

| Score | Tone | Example |
|-------|------|---------|
| Any | Minimal | *"Fair enough."* — or nothing. This is background friction, not drama. |

**⛔ Reaction rule:** One line per qualifying companion. No speeches. No follow-up unless the player addresses them. Personality still applies — Nok-Nok pumps a fist or sulks visibly; Jaethal says nothing either way; Amiri nods once or doesn't. Match the character.

---

### Need Check by Item Type

**WEAPON**
Show companion if: their primary weapon's base damage dice < this weapon's base damage dice
OR their attack bonus is more than 2 lower than this weapon would provide.
Do NOT show if: they already have this weapon type at equal or better stats.

| Companion | Primary Weapon | Notes |
|-----------|---------------|-------|
| Amiri | Bastard Sword (1d12) | Show only if weapon ≥ 2d8 or has special property she lacks |
| Linzi | Rapier (1d6) | Show for any better finesse weapon or shortbow upgrade |
| Tristian | Staff/Mace (1d4/1d6) | Show for any martial weapon (he rarely uses melee) |
| Valerie | Bastard Sword (1d8) | Show for higher damage or better crit profile |
| Harrim | Flail (1d6) | Show for better reach or damage |
| Jaethal | Scythe (1d10) | Show only if significantly better |
| Nok-Nok | Kukri ×2 (1d6 agile) | Show for agile weapons with better damage |
| Octavia | Longbow/Dagger | Show for arcane focus or better ranged |
| Regongar | Longsword/Spell | Show for Spellstrike-compatible weapon |
| Ekundayo | Composite Longbow (1d8) | Show for better bow or ranged weapon |
| Lem | Rapier/Sling | Show for better finesse or ranged |
| Kalikke | Elemental blasts (no weapon) | Almost never; only wondrous focus items |
| Kanerah | Elemental blasts (no weapon) | Same |

**ARMOR / SHIELD**
Show companion if: their current AC (base) is lower than what this item would provide.
Check: current armor AC bonus vs item AC bonus. If item is strictly better → show.

| Companion | Current Armor | AC Bonus |
|-----------|--------------|----------|
| Amiri | Scale Mail / Full Plate (L2) | +4/+6 |
| Linzi | Studded Leather | +2 |
| Tristian | None / Light | +1 or less |
| Valerie | Scale Mail / Tower Shield | +4+2 raised |
| Harrim | Chain Mail | +4 |
| Jaethal | Full Plate | +6 |
| Nok-Nok | Leather | +1 |
| Octavia | Studded Leather | +2 |
| Regongar | Scale Mail | +4 |
| Ekundayo | Leather Armor +1 | +2 |
| Lem | Studded Leather | +2 |

**CONSUMABLE — HEALING POTION / ELIXIR OF LIFE**
Show companions currently below 75% of their max HP.
Show companions with the Wounded condition (they need it most).
Priority display: most injured companion listed first.

**CONSUMABLE — ALCHEMICAL (bomb, tool, reagent)**
Show companions with Crafting trained or Alchemist class.
Show if the item counters a condition a companion currently has
(e.g., Antitoxin → show any companion with a poison condition).

**CONSUMABLE — SCROLL**
Show companions who have that spell on their tradition's list.
Check: spell tradition of the scroll vs each companion's casting tradition.
- Divine scrolls → Tristian, Harrim, Jaethal (if Cleric/Champion)
- Arcane scrolls → Octavia, Regongar
- Primal scrolls → Ekundayo (Ranger minor spells), Kalikke/Kanerah
- Occult scrolls → Linzi, Lem, Octavia (Wizard can use some via Arcane)

**WONDROUS ITEM — by slot**
| Slot | Show companions who… |
|------|---------------------|
| Head | Any companion without a head-slot item |
| Neck/Cloak | Any companion without neck-slot; prioritize squishier companions for Cloak of Resistance |
| Hands/Bracers | Unarmored companions (Bracers of Armor); or any without gloves |
| Feet | Any companion without feet-slot item |
| Ring | Any companion with a free ring slot (max 2 rings) |
| Belt | Martial companions (Str-based) for Belt of Giant Strength; any for Belt of Dex |
| Held | Companions who use that implement type (staff → spellcasters; rod → casters) |

**WONDROUS ITEM — stat/skill bonus**
Show companions who use the boosted stat or skill as primary:
- +Str → Amiri, Valerie, Harrim, Regongar, Ekundayo
- +Dex → Nok-Nok, Linzi, Octavia, Lem, Ekundayo
- +Con → Any companion (everyone benefits from HP)
- +Int → Octavia, Regongar, Lem
- +Wis → Tristian, Harrim, Ekundayo
- +Cha → Linzi, Lem, Jaethal, Kalikke/Kanerah

---

### Reason Line Examples by Companion

> **DM:** Generate the reason line in the companion's voice. Keep it one sentence.
> It should be specific to the item and their current stats — not generic.

**DM guidance:** Reason lines should reference the stat delta specifically — not generic. Examples: Amiri on a weapon: *"Better damage than my sword. More things die."* Valerie on a shield: *"Hardness [X]→[Y]. Numbers matter."* Nok-Nok on anything: enthusiastic. Jaethal on anything: measured. Tristian on healing gear: *"I can stretch this further than you can."* Match personality to mechanic — one sentence.

---

## 🔍 OPTION (6) — IDENTIFY: FULL RULES

### In the Field
- **Time:** 10 minutes (counts as a camp activity if at camp)
- **Check:** Arcana (arcane/occult items) or Occultism (occult/divine items) or Nature (primal items)
- **DC:** 15 (Common) | 20 (Uncommon/Magic tier) | 25 (Rare) | 30 (Epic) | 35 (Legendary)
- **Success:** Full stats revealed. Item card updates. Choose fate normally.
- **Failure:** No information revealed. Can try again after the next rest.
- **Critical Failure:** False information — DM provides one wrong stat (does not penalize player; item is flagged as `unreliably_identified` until confirmed by Caster's Tower)
- **Assurance:** A character with Assurance (Arcana) can auto-identify items up to DC = 10 + their proficiency bonus, with no roll needed.

### At the Caster's Tower (Capital)
- **Cost:** 10 gp per item
- **Time:** Instant
- **Result:** Always succeeds. No false information possible.
- **Available:** Ch2 onward (after Caster's Tower is built)

### Unidentified Item Display
```
[❓ UNIDENTIFIED — Weapon / Armor / Wondrous / Consumable]
  Estimated Value : [X gp range based on visual quality tier]
  Apparent Type   : [what it looks like — based on physical description]
  "[Flavor: what it looks like, feels like, smells like]"
  Source: [same as identified items]

  → Type .identify or select (6) to examine this item
```

### What Arrives Unidentified
- **Always pre-identified:** Items from documented chapter loot (stat block already in chapter file)
- **DM's discretion:** Procedural loot from d100 rolls — DM may choose to present Magic tier and above as unidentified for tension
- **Always unidentified:** Epic (🔵) and Legendary (🟣) procedural loot — player must identify before choosing fate

---

## 📌 OPTION (5) — HOLD: FULL RULES

Items on Hold remain in `pending_loot` indefinitely.

**What "Hold" means:**
- Item stays in the queue
- `📦 N item(s) waiting` counter includes held items
- On next `.loot` call: held items appear again with full stats and the same DECIDE FATE menu
- No time limit — held items persist across sessions as long as they are in the save block

**When to use Hold:**
- Player wants to compare item against shop stock before deciding
- Waiting to see if a companion's quest outcome changes what they need
- Saving a decision until the party reaches a vendor to check sell prices
- Deferring an Epic/Legendary item until it's identified

**Held item flag in save block:**
```json
{
  "name": "Unidentified Greataxe",
  "tier": "epic",
  "status": "held",
  "identified": false,
  "source": "Hero Point — defeated named boss"
}
```


> **
➡
️
 Tool quality tiers, gear tables, alchemical items, and Ch3
–
5 vendor stock 
→
 see `KM_Loot_Items_Ref_B.md`**

*KM_Loot_Items_Ref.md 
—
 Kingmaker PF2e Text Adventure | Loot Resolution + Give/Identify/Hold Rules v1.0*
*Source: PF2e Player Core, GM Core (Paizo)*
