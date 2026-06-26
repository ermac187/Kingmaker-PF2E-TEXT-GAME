

---

<!-- merged from KM_Loot_Items_Ref.md (v93.21 file consolidation) -->

# KINGMAKER — LOOT OPTIONS & ITEMS GEAR REFERENCE
## KM_Loot_Items_Ref.md | Companion Give Logic + Give/Identify/Hold Rules
## PAIR-LOAD WITH KM_Loot_Items_Ref.md (tool tiers + gear tables + Ch3–5 vendors)

> **DM:** Load this file when player selects Give/Identify/Hold on loot screen,
> buys tools or alchemical gear, or shops in Ch3+ locations.


## 🎁 OPTION (4) — GIVE TO COMPANION: FULL RULES

### How to Generate the Sub-Menu

When the player selects (4), evaluate every active companion against the item.
⛔ **SCOPE = EVERYONE PRESENT, not just "the group/party" (player directive 2026-06-22).** Poll **ALL companions PRESENT in the scene** who pass the need check for this item type — the full present cast, not only the active party-of-5 or the player's current room-group. Any companion physically here (active party, flipped seekers, planted recruits, a rejoined or dispatched-back group, anyone in the scene) gets to weigh in on which items they want and why. The need check filters by *usability* (can they use this item type), NOT by membership in a core group. Only those genuinely absent from the scene are excluded.
Each present, qualifying companion entry gets: the companion name, the ★/⚠️ marker, a **stat delta line** showing what changes mechanically, and a one-line reason in the companion's voice or as a tactical note.
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
| Heavy armor | Octavia, Linzi, Regongar | *"Arcane spell failure applies"* |
| Heavy armor | Nok-Nok | *"Too large — she can't wear this"* |
| Strength-based weapon (requires Str 14+) | Linzi, Octavia | *"Low Str — attack penalty applies"* |
| Two-handed weapon | Nok-Nok, Linzi | *"Small size — two-handed becomes unusable"* |
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

**⛔ Reaction rule:** One line per qualifying companion — and "qualifying" = **every companion PRESENT in the scene** who can use the item (not just the core group; see § SCOPE above). No speeches. No follow-up unless the player addresses them. Personality still applies — Nok-Nok pumps a fist or sulks visibly; Jaethal says nothing either way (death is a fact to her, not a windfall); Amiri nods once or doesn't. Match the character.

**💡 QUIET-MOMENT LOOT NUDGE:** when the scene is **calm** (combat over, no urgent beat — a lull, downtime, a rest, a march between rooms) AND the loot queue is **sizable (`🎒 Loot` ≥ ~3)**, a **present** companion may **ask, in character, whether the party can look at the loot yet** — a diegetic nudge to run `.loot` (a practical one: *"We've hauled that a while — sort it?"*; Nok-Nok: *"Shinies! Now?"*). **Once per lull, personality-matched** (loot-keen/practical companions ask; the indifferent don't — Jaethal won't). It's a suggestion; "later" defers it until the queue grows or a new lull. Never mid-combat or mid-tension.

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
- Occult scrolls → Linzi, Octavia (Wizard can use some via Arcane)

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
- +Dex → Nok-Nok, Linzi, Octavia, Ekundayo
- +Con → Any companion (everyone benefits from HP)
- +Int → Octavia, Regongar
- +Wis → Tristian, Harrim, Ekundayo
- +Cha → Linzi, Jaethal, Kalikke/Kanerah

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
 see `KM_Loot_Items_Ref.md`**

*KM_Loot_Items_Ref.md 
—
 Kingmaker PF2e Text Adventure | Loot Resolution + Give/Identify/Hold Rules v1.0*
*Source: PF2e Player Core, GM Core (Paizo)*


---

<!-- merged from KM_Loot_Items_Ref.md (v93.21 file consolidation) -->

# KINGMAKER — LOOT OPTIONS & ITEMS GEAR REFERENCE (Part 2)
## KM_Loot_Items_Ref.md | Tool Tiers + Gear Tables + Ch3–5 Vendors
## PAIR-LOAD WITH KM_Loot_Items_Ref.md

> **DM:** Load alongside KM_Loot_Items_Ref.md when the player shops for tools,
> alchemical gear, camping supplies, disguise items, or specialist weapons — and
> when visiting Ch3+ vendor locations not covered in KM_Loot_Merchants.md.

---

## 🔧 TOOL QUALITY TIERS

### Thieves' Tools
| Quality | Bonus | Price | Picks |
|---------|-------|-------|-------|
| Improvised | −2 | — | — |
| Ordinary | +0 | 3 sp | 3 |
| Infiltrator's | +1 | 3 gp | 6 |
| Expanded | +2 | 8 gp | 12 |
| Masterwork | +3 | 25 gp | 20 |

Failed check by 5+ vs hardness 10+ lock: 50% chance pick breaks (d20 ≥ 11). Thievery Expert rank: no flat check needed.

### Climber's Kit
| Quality | Bonus | Price |
|---------|-------|-------|
| Ordinary | +1 | 5 sp |
| Crampons | +2 | 2 gp |
| Superior | +3 | 8 gp |
| Spider Silk | +4 | 40 gp |

Ice/wet stone/glass: require Crampons+ or −2 penalty. No rope: DC +4, no catch on fall.

### Healer's Tools
| Quality | Bonus | Price | Special |
|---------|-------|-------|---------|
| Basic | +0 | 5 gp | Required for Medicine |
| Expanded | +1 | 10 gp | Surgical tools |
| Expert's | +2 | 40 gp | −2 Treat Wounds DC |
| Field Surgery | +3 | 200 gp | Treat Wounds in 1 min. Ch4+ |

---

## 🔍 DETECTION AND INVESTIGATION TOOLS

| Item | Effect | Price |
|------|--------|-------|
| Magnifying Glass | +1 circ. Perception (tiny objects/text) | 3 gp |
| Compass | +1 Survival (navigation); can't get lost | 1 gp |
| Spyglass | Perception range +500 ft | 25 gp |
| Map-maker's Kit | +1 Survival (mapped terrain) | 8 gp |
| Darkvision Goggles | 60 ft darkvision, 1 hr, single use | 25 gp |
| Signal Lantern | 120 ft beam, invisible from sides | 5 gp |
| Chalk ×10 | Mark paths in dungeons | 1 cp |
| Mirror (steel) | See around corners | 1 gp |
| Skeleton Key | +4 Thievery vs standard locks, single use | 20 gp |

---

## 🧪 ALCHEMICAL ADVENTURING GEAR

| Item | Effect | Dur | Price |
|------|--------|-----|-------|
| Antitoxin (Lesser/Mod) | +2/+4 circ. Fort vs poison | 1 hr | 3/15 gp |
| Antiplague (Lesser/Mod) | +2/+4 circ. Fort vs disease | 1 hr | 3/15 gp |
| Darkvision Elixir (L/M) | 60 ft darkvision | 10m/1h | 10/25 gp |
| Comprehension Elixir | +2 circ. one Knowledge skill | 10 min | 15 gp |
| Quicksilver Mutagen (L/M) | +2/+3 Dex/Perception, −2 Str | 10m/1h | 4/25 gp |
| Brewer's Slipstone | 10 sq ft — DC 15 Acro or prone | 1 hr | 5 gp |
| Phosphorescent Powder | Target glows; no Stealth | 1 hr | 8 gp |
| Liquid Ice | +1d4 cold on next hit | 1 hit | 6 gp |
| Tanglefoot Bag | Flat-Footed + Spd −10 (Ref DC 17) | 1 min | 3 gp |
| Thunderstone | 10 ft Deafened 1 rd (Fort DC 15) | Instant | 4 gp |
| Sunrod | Bright 20 ft, dim 40 ft | 6 hrs | 8 sp |
| Everburning Torch | Bright 20 ft | Perm | 18 gp |
| Glowing Eye | +2 Intimidation vs darkvision | 1 hr | 2 gp |
| Ghostlight Candle | 5 ft, visible only to user | 8 hrs | 3 gp |

---

## 🏕️ CAMPING AND SURVIVAL GEAR

| Item | Effect | Bulk | Price |
|------|--------|------|-------|
| Tent (standard) | Shelter for 2; reduce cold penalty | 2 | 8 sp |
| Tent (pavilion) | Shelter for 6; +1 camp activity checks | 3 | 10 gp |
| Bedroll | +1 circ. sleep quality (−1 hr Fatigued recovery) | L | 2 cp |
| Cooking Kit | Required for Cook Meal | 2 | 4 sp |
| Expanded Rations (3 days) | No Survival check for nourishment | L | 1 gp |
| Water Purification Kit | Purify contaminated water; 20 uses | L | 8 gp |
| Cold-weather gear | Negate cold weather damage | 1 | 5 gp |
| Fireproof Blanket | Resist fire 5; extinguish persistent fire | 1 | 15 gp |

---

## 🎭 DISGUISE AND SOCIAL TOOLS

| Item | Effect | Price |
|------|--------|-------|
| Disguise Kit (Basic) | +1 circ. Deception (Create Disguise) | 1 gp 5 sp |
| Disguise Kit (Superior) | +2 circ. Deception; voice modulator | 8 gp |
| Noble's Outfit | +2 circ. Diplomacy (formal court); required Pitax noble path | 30 gp |
| Merchant's Outfit | +1 circ. Diplomacy (commerce); pass as trader | 5 gp |
| Guard's Outfit | Pass inspection (Deception DC 12) | 1 gp |
| Courtier's Outfit | Required Pitax court; +1 circ. Diplomacy (River Kingdoms) | 50 gp |
| Forgery Kit | +1 circ. Society (Create Forgery) | 1 gp |

---

## 🗡️ SPECIALIST COMBAT TOOLS

| Item | Effect | Price |
|------|--------|-------|
| Caltrops | 5 sq ft; DC 15 Acrobatics or Slowed 1 | 3 sp |
| Snare Components (Basic) | DC 14 snare; immobilizes Medium | 2 gp |
| Snare Components (Expert) | DC 18 snare; 2d6 P + immobilized | 8 gp |
| Bola | Thrown 20 ft; DC 16 Acrobatics or Prone | 5 sp |
| Manacles (average) | Thievery DC 22 to escape | 2 gp |
| Manacles (superior) | Thievery DC 27 to escape | 15 gp |
| Net (weighted) | Thrown 10 ft; DC 16 Ref or Grabbed; escape Ath DC 18 | 2 gp |
| Grappling Hook | Thrown 30 ft; Athletics DC 12 | 1 sp |
| Smokestick (Lesser) | 10 ft cloud; Concealed 1 min | 2 gp |
| Smokestick (Greater) | 20 ft cloud; Heavily Obscured center | 10 gp |

---

## 🏪 CH3–CH5 VENDOR STOCK

### VARNHOLD TRADING POST (Ch3, after liberation)

**Available after:** `maegar_varn_saved = TRUE` AND Varnhold vassal status.
**Restock:** Weekly. Standard PF2e prices (no discount — remote).

| Category | Available Items |
|----------|----------------|
| Weapons | Standard martial weapons up to +1 (no runes beyond that) |
| Armor | Up to Chain Mail +1; Hide Armor |
| Tools | Climber's Kit (Superior), Thieves' Tools (Expanded), Healer's Tools (Expanded) |
| Alchemical | Antitoxin (Moderate), Darkvision Elixir (Moderate), Tanglefoot Bags ×5 |
| Specialty | Ancient Cyclops Coin (1d3 available — 50 gp each, for Storyteller) |
| Scrolls | Divine L1–L3 (Jhod-sourced) |

---

### KELLID TRADE CAMP (Ch3, after Centaur Alliance)

**Available after:** `kellid_friendly = TRUE`
**Restock:** Each return visit (once per in-game week). Unique Kellid craftwork.

| Item | Effect | Price |
|------|--------|-------|
| Kellid War Paint | +1 circ. Intimidation, 1 hour | 5 gp |
| Bone Fetish (Totem) | +1 circ. Nature vs primal creatures, 24 hrs | 8 gp |
| Steppe Jerky (3 days) | Rations; ignore cold-weather fatigue | 2 gp |
| Woolen Cloak (heavy) | Cold-weather gear + +1 Survival vs weather | 4 gp |
| Kellid Composite Shortbow | 1d6+2 P, Propulsive | 3 gp |
| Ancient Cyclops Coin ×1d2 | For Storyteller | 40 gp ea |

---

### PITAX BLACK MARKET (Ch5 — infiltration path)

**Available after:** Player enters Pitax using infiltration path.
**Restock:** One-time stock. **Access:** Deception DC 18 or Spymaster role.

| Item | Effect | Price |
|------|--------|-------|
| Masterwork Thieves' Tools | +3 item to Thievery | 25 gp |
| Skeleton Key ×3 | +4 Thievery vs standard locks, single use | 20 gp ea |
| Disguise Kit (Superior) ×2 | +2 circ. Deception; voice modulator | 8 gp |
| Courtier's Outfit | Required for Pitax court noble path | 50 gp |
| Potions of Invisibility ×3 | Invisible 5 min or until hostile | 80 gp ea |
| Scroll of Silence ×2 | Silence 20-ft area | 8 gp ea |
| Darkvision Elixir (Mod) ×4 | 1 hour darkvision | 25 gp ea |
| Smokestick (Greater) ×4 | 20-ft smoke cloud | 10 gp ea |
| Pitax Guard Outfit | Pass as guard (Deception DC 14) | 3 gp |
| Irovetti's Map (partial) | −4 Stealth DCs inside Pitax palace | 150 gp |

---

### RIVER KINGDOMS TRAVELING MERCHANT (Ch4–5 random encounter)

**Trigger:** d20 river travel roll ≥ 18 (KM_Game_Subsystems.md). **Restock:** One-time per encounter.

| Category | Available |
|----------|-----------|
| Magic Items | Roll 1d4 from Magic tier loot table (KM_Loot_Merchants.md) |
| Tools | Masterwork versions of any standard tool at 3× price |
| Rare Components | Spell components for L5–L7 spells (300–700 gp each) |
| Information | One piece of regional intelligence per chapter (trade for gold) |

---

### ARMAG'S TOMB CACHE (Ch4 — after clearing)

Fixed treasure cache, not a vendor.

| Item | Notes |
|------|-------|
| Kellid War Supplies ×10 | Smokesticks + Tanglefoot Bags |
| Field Surgery Kit | +3 Medicine; Treat Wounds in 1 min |
| Everburning Torch ×3 | Permanent light |
| Spider Silk Climbing Kit | +4 Athletics (Climb); any surface |
| Ancient Map Fragment | +1 hex revealed on world map |

---

*KM_Loot_Items_Ref.md — Kingmaker PF2e Text Adventure | Gear Reference v1.0*


---

<!-- merged from KM_Loot_Merchants.md (v93.21 file consolidation) -->

# KINGMAKER — MERCHANT INVENTORIES
## KM_Loot_Merchants.md | Referenced by: KM_Exploration.md, KM_Ch1.md-KM_Ch7.md, KM_Loot.md

> **DM:** Merchant inventory file. Holds shop format, named-vendor stock lists, and vendor availability by chapter. Pair-load with `KM_Loot_Merchants.md` whenever random loot rolls are also needed (Common / Magic / Rare / Epic / Legendary tier d100 / d20 rollable tables live in part B).

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

> **DM:** Items from `KM_Items.md` and `KM_Items.md` are
> distributed to vendors by theme. Use this table to decide what a given
> merchant has in stock when the player asks for a specific item type.
> Default: rotate 3–5 items from the listed section per visit.

| Vendor | KM_Items.md sections | KM_Items.md sections |
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
*Updated: Added vendor cross-reference for KM_Items.md and KM_Items.md.*

*KM_Loot_Merchants.md — Kingmaker PF2e Text Adventure | Merchant Inventories v2.0 (split — pair-load with KM_Loot_Merchants.md)*


---

<!-- merged from KM_Loot_Merchants.md (v93.21 file consolidation) -->

# KINGMAKER — LOOT TABLES (PART B)
## KM_Loot_Merchants.md | Pair-load with KM_Loot_Merchants.md

> **DM:** This file holds the RANDOM ROLLABLE LOOT TABLES (Common / Magic / Rare / Epic / Legendary tiers, d100 + d20). Pair-load with `KM_Loot_Merchants.md` (which holds the merchant inventories — Oleg's, Bokken, Beldame, Bartholomew, Pitax Black Market, Capital Shops, Hassuf, Dragn, Verdel, vendor availability, expanded stock, SHOP SCREEN FORMAT).

> **Use this file** whenever Step 3 (Quality, d100) produces a loot-table result and you need a specific named item. Use the merchant file for any `.buy` / vendor browsing flow.

---

> **DM:** This file is the authoritative item source for all loot-table rolls.
> When Step 3 (Quality, d100) produces a loot-table result, roll d20 on the
> matching tier table below to get a specific named item. No DM generation.
> No contextual substitution. Roll the die, read the result, award the item.
>
> **DM Created items are ELIMINATED from loot-table rolls.**
> The only DM Created slot remaining is the explicit DM Created column in the
> Step 2 Item Drop table (rolls 18–20 in KM_P2.txt). All other items come
> from this file.
>
> **Context rule (item type only):** If the rolled item is physically impossible
> as loot from this source (e.g., a greatsword from a pixie), reroll once.
> If the second roll is also impossible, take the closest item in the same row.
> Do not substitute a DM-invented item.

---

## ⬜ COMMON TIER (d100: 01–40)

> Mundane weapons, basic armor, standard consumables. No magical properties.
> Value range: 1–20 gp.

| d20 | Category | Item | Stats | Value |
|-----|----------|------|-------|-------|
| 1 | Weapon | Shortsword | 1d6 piercing/slashing, finesse, agile | 9 gp |
| 2 | Weapon | Handaxe | 1d6 slashing, agile, thrown 10 ft | 6 gp |
| 3 | Weapon | Spear | 1d6 piercing, thrown 20 ft | 1 gp |
| 4 | Weapon | Light Crossbow | 1d8 piercing, range 80 ft, reload 1 | 3 gp |
| 5 | Weapon | Dagger | 1d4 piercing/slashing, agile, finesse, thrown 10 ft | 2 gp |
| 6 | Weapon | Morningstar | 1d6 bludgeoning/piercing, versatile | 1 gp |
| 7 | Weapon | Greatclub | 1d10 bludgeoning, backswing, shove | 1 gp |
| 8 | Weapon | Longbow | 1d8 piercing, range 100 ft, volley 30 ft | 6 gp |
| 9 | Armor | Leather Armor | +1 AC, Dex cap +4, ACP 0 | 2 gp |
| 10 | Armor | Studded Leather | +2 AC, Dex cap +3, ACP −1 | 3 gp |
| 11 | Armor | Chain Shirt | +2 AC, Dex cap +3, ACP −1 | 5 gp |
| 12 | Armor | Hide Armor | +3 AC, Dex cap +2, ACP −2 | 2 gp |
| 13 | Shield | Wooden Shield | +2 AC (raised), Hardness 3, HP 12, BT 6 | 1 gp |
| 14 | Shield | Steel Shield | +2 AC (raised), Hardness 5, HP 20, BT 10 | 2 gp |
| 15 | Consumable | Healing Potion (Minor) | Restores 1d8 HP | 4 gp |
| 16 | Consumable | Antitoxin (Lesser) | +2 circ. bonus vs poison for 1 hour | 3 gp |
| 17 | Consumable | Alchemist's Fire (Lesser) | 1d8 fire + 1 persistent fire, splash 5 ft | 3 gp |
| 18 | Consumable | Smokestick (Lesser) | 10-ft smoke cloud, concealment, 1 min | 2 gp |
| 19 | Consumable | Rations (1 week) | Standard trail rations | 5 sp |
| 20 | Gear | Healer's Tools | Required for Medicine checks; 10 uses | 5 gp |

---

## 🟡 MAGIC TIER (d100: 41–70)

> +1 striking weapons, +1 resilient armor, lesser wondrous items, moderate potions.
> Value range: 20–160 gp.

| d20 | Category | Item | Stats | Value |
|-----|----------|------|-------|-------|
| 1 | Weapon | +1 Shortsword | 1d6+1 piercing/slashing, finesse, agile | 20 gp |
| 2 | Weapon | +1 Handaxe | 1d6+1 slashing, agile, thrown 10 ft | 20 gp |
| 3 | Weapon | +1 Striking Dagger | 2d4 piercing/slashing, agile, finesse, thrown | 65 gp |
| 4 | Weapon | +1 Striking Shortbow | 2d6 piercing, range 60 ft | 65 gp |
| 5 | Weapon | Shock Rune Handaxe (+1) | 1d6+1d4 electricity on crit, agile | 30 gp |
| 6 | Weapon | Flaming Rune Dagger (+1) | 1d4+1d6 fire on crit, agile, finesse | 35 gp |
| 7 | Weapon | +1 Light Mace | 1d4+1 bludgeoning, agile, finesse | 20 gp |
| 8 | Weapon | +1 Rapier | 1d6+1 piercing, deadly d8, disarm, finesse | 20 gp |
| 9 | Armor | +1 Leather Armor | +1 AC, Dex cap +4, ACP 0 | 27 gp |
| 10 | Armor | +1 Studded Leather | +2 AC (base), Dex cap +3, +1 item bonus saves | 35 gp |
| 11 | Armor | +1 Chain Mail | +4 AC (base), Dex cap +1, ACP −2 | 37 gp |
| 12 | Armor | +1 Breastplate | +4 AC (base), Dex cap +2, ACP −1 | 40 gp |
| 13 | Shield | Sturdy Shield (Lesser) | +2 AC raised, Hardness 8, HP 32, BT 16 | 30 gp |
| 14 | Wondrous | Cloak of Elvenkind | +2 circ. Stealth; advantage in dim light | 55 gp |
| 15 | Wondrous | Bag of Holding (Type I) | Holds 25 bulk; weighs 1 bulk | 75 gp |
| 16 | Wondrous | Boots of Elvenkind | +2 circ. Acrobatics (balance), ignore difficult terrain | 45 gp |
| 17 | Consumable | Healing Potion (Lesser) | Restores 2d8+5 HP | 12 gp |
| 18 | Consumable | Oil of Potency (+1) | Apply to weapon: +1 item bonus attacks for 1 hour | 25 gp |
| 19 | Consumable | Scroll of Magic Missile (L1) | 1d4+1 force, 3 missiles | 4 gp |
| 20 | Consumable | Elixir of Life (Lesser) | Restores 3d6+6 HP; +1 saves vs disease/poison 10 min | 25 gp |

---

## 🟢 RARE TIER (d100: 71–86)

> +1 striking weapons with property runes, +1 resilient armor with property runes,
> moderate wondrous items. Special materials (Cold Iron, Silver).
> Value range: 160–650 gp.

| d20 | Category | Item | Stats | Value |
|-----|----------|------|-------|-------|
| 1 | Weapon | +1 Striking Frost Shortbow | 2d6+1d6 cold, range 60 ft; Weakness cold on crit | 200 gp |
| 2 | Weapon | +1 Striking Flaming Longsword | 2d8+1d6 fire; persistent fire on crit | 215 gp |
| 3 | Weapon | Cold Iron +1 Striking Dagger | 2d4, agile, finesse; bypasses fey DR | 185 gp |
| 4 | Weapon | Silver +1 Striking Morningstar | 2d6; bypasses lycanthrope/devil DR | 175 gp |
| 5 | Weapon | +1 Striking Shocking Rapier | 2d6+1d4 electricity; Stunned 1 on crit (Fort DC 19) | 210 gp |
| 6 | Weapon | +2 Shortsword | 1d6+2 piercing/slashing, finesse, agile | 200 gp |
| 7 | Weapon | +1 Striking Wounding Handaxe | 2d6; 1d6 persistent bleed on crit | 220 gp |
| 8 | Weapon | +1 Striking Thundering Crossbow | 2d8+1d6 sonic; Deafened on crit (Fort DC 19) | 205 gp |
| 9 | Armor | +1 Resilient Studded Leather | +2 AC, +1 item saves; Dex cap +3 | 160 gp |
| 10 | Armor | +1 Resilient Breastplate | +4 AC, +1 item saves; Dex cap +2 | 200 gp |
| 11 | Armor | +1 Resilient Chain Mail | +4 AC, +1 item saves; Dex cap +1 | 185 gp |
| 12 | Armor | +2 Hide Armor | +3 AC, Dex cap +2; resist physical 2 | 350 gp |
| 13 | Shield | Sturdy Shield (Moderate) | +2 AC raised, Hardness 10, HP 40, BT 20 | 160 gp |
| 14 | Wondrous | Amulet of Natural Armor (+1) | +1 item bonus to AC (untyped, stacks) | 160 gp |
| 15 | Wondrous | Ring of Protection (+1) | +1 circ. bonus to AC and saves | 160 gp |
| 16 | Wondrous | Necklace of Fireballs (Type I) | 3 × Fireball beads (3d6 fire, DC 17 Reflex) | 225 gp |
| 17 | Wondrous | Bracers of Armor (+1) | +1 item AC (unarmored only); counts as armor rune | 160 gp |
| 18 | Consumable | Healing Potion (Moderate) | Restores 3d8+10 HP | 50 gp |
| 19 | Consumable | Potion of Invisibility | Invisible for 5 min or until hostile act | 80 gp |
| 20 | Consumable | Scroll of Fireball (L3) | 6d6 fire, 20-ft burst, DC 19 Reflex | 30 gp |

---

## 🔵 EPIC TIER (d100: 87–94)

> +2 greater striking weapons, +2 resilient armor, major wondrous items.
> Special materials (Mithral, Adamantine). Named weapons from Kingmaker.
> Value range: 650–2,500 gp.

| d20 | Category | Item | Stats | Value |
|-----|----------|------|-------|-------|
| 1 | Weapon | Trollreaper (+2 Acid Greataxe) | 3d12+2d6 acid; persistent acid + sickened 1 on crit | 2,000 gp |
| 2 | Weapon | +2 Greater Striking Flaming Longsword | 3d8+2d6 fire; Stunned 1 on crit (Fort DC 22) | 1,400 gp |
| 3 | Weapon | Mithral +2 Rapier | 3d6+2, finesse, deadly d8; reduces Bulk by 1 | 1,500 gp |
| 4 | Weapon | Adamantine +2 Warhammer | 3d8+2, shove; ignore Hardness ≤ 13 | 1,600 gp |
| 5 | Weapon | +2 Greater Striking Shock Composite Longbow | 3d8+2d4 electricity; range 100 ft | 1,450 gp |
| 6 | Weapon | Assassin's Shortbow (+2 Striking, Vorpal property) | 3d6+2; double crit range; Decapitate on nat 20 | 1,800 gp |
| 7 | Weapon | Cold Iron +2 Greater Striking Dagger | 3d4+2; bypasses fey DR; +2d6 vs fey/fiends | 1,350 gp |
| 8 | Weapon | +2 Greater Striking Thundering Maul | 3d12+2d6 sonic; Deafened 1 min on crit | 1,500 gp |
| 9 | Armor | +2 Resilient Full Plate | +6 AC, +2 item saves; Dex cap +0, ACP −3 | 1,600 gp |
| 10 | Armor | Mithral +2 Resilient Breastplate | +4 AC, +2 item saves; ACP 0; reduces Bulk | 1,800 gp |
| 11 | Armor | Adamantine +2 Resilient Hide | +3 AC, +2 item saves; resist physical 5 | 1,700 gp |
| 12 | Armor | +2 Resilient Studded Leather | +2 AC, +2 item saves; Dex cap +3 | 1,000 gp |
| 13 | Shield | Sturdy Shield (Major) | +2 AC raised, Hardness 15, HP 60, BT 30 | 1,400 gp |
| 14 | Wondrous | Boots of Speed | +10-ft status bonus speed; Haste 1/day (1 min) | 2,000 gp |
| 15 | Wondrous | Ring of Wizardry (Type II) | +2 spell slots of your highest prepared spell level | 1,800 gp |
| 16 | Wondrous | Belt of Giant Strength | +2 item bonus to Athletics; Bulk cap +2 | 1,600 gp |
| 17 | Wondrous | Headband of Inspired Wisdom | +2 item bonus to Will saves and Perception | 1,400 gp |
| 18 | Wondrous | Cloak of Displacement | 20% miss chance (concealment) while worn | 2,000 gp |
| 19 | Consumable | Healing Potion (Greater) | Restores 6d8+20 HP | 300 gp |
| 20 | Consumable | Potion of Heroism | +1 status bonus attack, saves, skills for 10 min | 700 gp |

---

## 🟣 LEGENDARY TIER (d100: 95–100)

> Artifact-level weapons, +3 resilient armor, apex wondrous items.
> Named Kingmaker artifacts and endgame items.
> Value range: 2,500 gp+.

| d20 | Category | Item | Stats | Value |
|-----|----------|------|-------|-------|
| 1 | Weapon | The Vanishing Blade (+3 Striking Rapier) | 4d6+3, finesse; Teleport 30 ft as free action 1/round | 9,000 gp |
| 2 | Weapon | Stag's Fury (+3 Greater Striking Longbow) | 4d8+3; crit auto-trips target (Reflex DC 26) | 8,500 gp |
| 3 | Weapon | Plague Sword (+3 Striking, Wounding, Sickening) | 4d8+3+1d6 bleed; Sickened 2 on crit | 10,000 gp |
| 4 | Weapon | Fey-Bane Glaive (+3, Cold Iron, Holy) | 4d8+3; +3d6 vs fey/fiend; Blinded on crit (Will DC 27) | 11,000 gp |
| 5 | Weapon | Hurtling Hammer (+3 Striking, Returning, Ghost Touch) | 4d8+3; returns after throw; hits incorporeal | 9,500 gp |
| 6 | Weapon | Ovinrbaane, Enemy of All Enemies | 4d6+5, +2d6 vs all creature types; Dominated on crit (Will DC 28) — cursed | 14,000 gp |
| 7 | Weapon | Briar (Artifact — First World Shortsword) | 4d6+5 piercing+cold; crit auto-Grabbed; Stunned 1d4 on nat 20 | Priceless |
| 8 | Weapon | Nyrissa's Sting (Artifact — Poisoned Dagger) | 4d4+5; Fort DC 30 or Paralyzed 1 min on any hit | Priceless |
| 9 | Armor | +3 Resilient Full Plate | +6 AC, +3 item saves; Dex cap +0, ACP −2 | 4,500 gp |
| 10 | Armor | Mithral +3 Resilient Breastplate | +4 AC, +3 item saves; Bulk 1; ACP 0 | 5,000 gp |
| 11 | Armor | Adamantine +3 Resilient Full Plate | +6 AC, +3 item saves; resist physical 10 | 6,000 gp |
| 12 | Armor | Armor of the Pitax King (+3 Resilient Scale, Fortification) | +5 AC, +3 saves; 25% chance crit becomes normal hit | 7,000 gp |
| 13 | Shield | Stonewall Shield (Artifact) | +3 AC raised; Hardness 25, HP 100, BT 50; immune to Sunder | Priceless |
| 14 | Wondrous | Amulet of Mighty Fists (+3) | +3 item bonus to unarmed attack/damage rolls | 3,000 gp |
| 15 | Wondrous | Tome of Clear Thought (+4) | +4 permanent Intelligence on read; single use | 27,500 gp |
| 16 | Wondrous | Manual of Bodily Health (+4) | +4 permanent Constitution on read; single use | 27,500 gp |
| 17 | Wondrous | Ioun Stone (Pale Green Prism) | +1 competence bonus all checks; orbits head | 30,000 gp |
| 18 | Wondrous | Rod of Lordly Might | Transforms (6 weapon forms); Suggestion 3/day (DC 28) | 12,000 gp |
| 19 | Wondrous | Portable Hole | 10-ft diameter extradimensional space; holds any Bulk | 20,000 gp |
| 20 | Wondrous | Sphere of Annihilation | Destroys anything it touches; Will DC 30 to control | Priceless |

---

## 🎲 HOW TO USE THIS FILE

**Full roll sequence for a loot-table item:**

```
Step 1 — Roll d100 → Quality Tier (from KM_P2.txt table)
Step 2 — Roll d20  → Specific item from matching tier table above
Step 3 — Apply context filter: can this item physically exist on this enemy?
          If yes → award it. If no → reroll d20 once. If still no → take nearest row.
Step 4 — Record item in pending_loot with name, tier, effects, and value
Step 5 — Output loot block in standard format
```

**Context filter examples:**
- Bandit → any weapon, armor, consumable ✓ | Sphere of Annihilation ✗ (reroll)
- Wolf/Worg/beast/vermin/ooze → Trophy/material ONLY (use Random Encounter table) — ⛔ **HARD GATE: no hands, no concept of loot → CANNOT carry/wield ANY crafted item at any tier, no exception** (this is the real prevention; see GATE 1 below)
- Kobold → light weapons, crude items typical; ⛔ but a kobold HAS hands and covets shiny things, so it CAN carry any tier it acquired — reroll an 🔵 Epic / 🟣 Legendary weapon ONLY when it's an **unexplained RANDOM-roll spike on a faceless mook** (GATE 2), never when the fiction gave it one
- Fey → wondrous items, consumables ✓ | heavy armor, greatweapons ✗ (reroll)
- Undead (skeletal) → weapons, no armor, no consumables (reroll if consumable)
- Cultist → scrolls, wondrous items, light weapons ✓ | heavy armor ✗

⛔ **TWO DIFFERENT GATES — DON'T CONFUSE THEM (user-flagged 2026-06-23).** The thing that "prevents a kobold from having a legendary blade" was framed wrong. The real axis is **ACQUISITION CAPABILITY, not power tier.** Split it:

  **GATE 1 — CAPABILITY (HARD, real in-world prevention).** Can the creature **pick up, carry, covet, or wield a crafted object** at all? Only creatures that can drop crafted gear.
  - ⛔ **Animals / beasts / vermin / oozes / mindless non-handed things → NO manufactured items, EVER, at any tier.** A wolf has no hands and no concept of loot — it physically cannot have a legendary blade. They drop **natural** things only: pelt, fang, hide, ichor, trophy, raw material (Random Encounter / trophy tables). **This is the genuine prevention** — and it has **no story exception** (a wolf can't "steal" a sword).
  - ✅ **Handed / sapient creatures (humanoids, kobolds, goblins, cultists, bandits, intelligent monsters) → CAN have any tier they could have ACQUIRED.** Hands + intent = they can loot a corpse, steal, be gifted, hoard, or guard a blade. **No power-tier prevention applies to them.**

  **GATE 2 — RANDOM-SPIKE PLAUSIBILITY (SOFT, RNG-only).** This applies *only* to GATE-1-capable creatures, and *only* to the **auto-roll dice**: so the d100 doesn't hand a **faceless mook** gear wildly above its station from nothing (a random kobold doesn't *conjure* a legendary sword from a die). Reroll the **unexplained random spike** on a generic mook. ⛔ It does **NOT** apply — award as-is, no reroll — when there's a **REASON**:
  - the enemy is **named / a notable / a captain** (not a generic mook),
  - the item is **story-placed or flagged** for this encounter (scene file, quest, plant),
  - the fiction establishes the enemy **stole / looted / was gifted / guards** it,
  - the player **forced/rerolled it via Hero-Point overflow** (manufacturing currency overrides source-gating entirely — see KM_Commands.md).

  So: **a wolf with a legendary blade = impossible (Gate 1).** **A kobold with a legendary blade = fine if the fiction gave it one; rerolled only as a bare random spike (Gate 2).** When a handed mook legitimately carries something above its tier, lean into the hook (*where did a kobold get THIS?*) — don't sand it off. Never reroll an item the story put there.

**DM Created is no longer a loot-table result.**
The only remaining DM Created slot is the explicit DM Created column in Step 2
of the Item Drop table (KM_P2.txt). All other results use this file.

---

*KM_Loot_Merchants.md — Loot Tables Section v1.0*

*KM_Loot_Merchants.md — Kingmaker PF2e Text Adventure | Loot Tables (rollable) v1.0*


---

<!-- merged from KM_Loot.md (v93.21 file consolidation) -->

# KINGMAKER — VENDOR NPC ROSTER & DIALOGUE RULE
## KM_Loot.md | Referenced by: KM_DMRules.md, KM_Commands.md, KM_Loot_Merchants.md
## **PAIR-LOAD WITH KM_Loot.md** (extended roster + quality-tier gate table)

> **DM:** This file is the authoritative roster of every vendor NPC in the game.
> All vendors named here are project-canon (no `.fail 9`). It also defines the
> universal `[Buy]` menu rule that applies to ALL vendor dialogue.
> **Extended vendors (Issili, Mim Wobblegander, The Bonewright, Storyteller-as-trader)
> and the AUTHORITATIVE quality-tier gate table live in `KM_Loot.md` — load both.**

---

## ⛔ UNIVERSAL VENDOR DIALOGUE RULE

**When the player is in dialogue with any vendor NPC listed in this file, the
choice menu MUST include `[Buy] Browse <Vendor>'s wares` as the FINAL option
(slot N — last in the menu). This is in addition to the normal 10–30 option
menu requirement.**

- The Buy option is always present whenever a vendor is the active speaker.
- The Buy option is always the LAST listed option (after travel, depart, etc.).
- Selecting `[Buy]` opens the vendor's shop screen using the format from
  `KM_Loot_Merchants.md` § SHOP SCREEN FORMAT.
- After the player closes the shop (`.shop close` or selects `Done`), the
  conversation resumes at the same dialogue node. The Buy option remains
  available on the next menu.
- Player may also force-open with `.buy` while a vendor is in scene.

**Violations:**
- Vendor dialogue menu missing `[Buy]` last option = `.fail 3` (menu < 10
  options or required option absent).
- DM closing a vendor scene before player chooses to leave = `.fail 35`.

**Format example:**

```
[1] Ask about the bandit raids
[2] Ask about Svetlana
[3] Ask about Restov politics
...
[9] Travel — leave the trading post
[10] Buy — Browse Oleg's wares     ← always last, always present
```

If the menu would otherwise have 10 options, append Buy as #11. If it has 30,
Buy is #30. The Buy slot is reserved.

---

## 📋 NAMED VENDOR NPC ROSTER

> **DM:** Every NPC below is project-canon. When the player encounters a
> shop in any chapter and wants to talk to the shopkeeper, use the name,
> personality, voice, and hooks below. Do not invent new shopkeeper names.
> Already-defined NPCs (Oleg, Svetlana, Bokken, Old Beldame, Hassuf,
> Bartholomew Delbin) — see `KM_NPCs.md` and `KM_Loot_Merchants.md` for
> their full writeups; they are listed here only as a quick reference.

### QUICK REFERENCE — ALREADY DEFINED ELSEWHERE

| NPC | Shop | Location | Full writeup in |
|-----|------|----------|-----------------|
| Oleg Leveton | Oleg's Trading Post | Hex (1,0) | KM_NPCs.md |
| Svetlana Leveton | Oleg's Trading Post (co) | Hex (1,0) | KM_NPCs.md |
| Bokken | Bokken's Hut | Hex (1,−1) | KM_NPCs.md, KM_Loot_Merchants.md |
| Old Beldame | Swamp Witch's Hut | Hex (−2,−1) | KM_Loot_Merchants.md |
| Hassuf | Wandering Caravan | Appears at Oleg's, every 14d | KM_Loot_Merchants.md |
| Bartholomew Delbin | Secluded Lodge | Hex (3,1) | KM_Loot_Merchants.md |

---

### NEW VENDOR NPCs — FULL WRITEUPS

The following vendors were previously anonymous in `KM_Loot_Merchants.md`.
Each is now project-canon with a full profile. Use these names, voices, and
quirks; do not improvise replacements.

---

#### DRAGN STONEWARD
- **Role:** Dwarven smith. Capital smithy district, his own forge separate from the kingdom-stamped Capital Smithy.
- **Available:** Chapter 2+ after Trobold cleared.
- **Appearance:** Five Kings dwarf, late middle-aged, beard plaited in three braids that he chews when thinking. Burn scars up both forearms. Wears a leather apron over chain. Hammer-hand calluses thick enough to take a sparking ember without flinching.
- **Personality:** Bluff and direct. Trusts work over words — if you bring him a broken weapon, he'll respect you more than any speech. Hates ornament-for-its-own-sake, distrusts elven smithing on principle, and refuses to discuss what made him leave the Five Kings (a guild dispute he lost). Jokes are rare and dry.
- **Voice:** Short sentences. No contractions when angry. Calls everyone "smith" until they prove they're something else.
- **Hooks:**
  - **Quest — A Proper Anvil:** Dragn's Five Kings anvil was lost on the road south. He pays well if anyone recovers it from the bandit camp that took it. Reward: 15% lifetime discount + first crack at any Adamantine restock.
  - **Lore:** If asked about his past three times across separate visits (gated by trust), he'll mention the guild dispute. Fourth time: names the rival who set him up. Never the fifth time.
- **Disposition shift:** Player who brings him a Dwarven-craft weapon to admire (not sell) gains +1 Dragn opinion permanently.

---

#### VERDEL OF BREVOY
- **Role:** Wondrous-goods specialist. Capital market district, signed-and-sealed wares only.
- **Available:** Chapter 2+ after Market building.
- **Appearance:** Issian human, slight, mid-40s, dressed Brevic-style: stiff high collar, dark fitted coat, gloves indoors. Spectacles on a fine chain. Hands fastidiously clean — he wipes them between every transaction. A small ledger never leaves his belt.
- **Personality:** Fastidious almost to the point of comedy. Every item in his shop is appraised, signed, dated, and accounted for in his ledger; he resents being made to look anything up he hasn't already memorized. Quotes prices to two decimal places ("Sixty gold and four silver, plus four copper for the certificate"). Genuinely respects craftsmanship and will spend twenty minutes on the provenance of a ring if asked. Mildly snobby about Rostlandic customers.
- **Voice:** Formal, precise, occasionally condescending. Calls the player "patron" once trust is established; "customer" if not.
- **Hooks:**
  - **Service — Authentication:** For 20 gp, Verdel will authenticate any wondrous item the party brings in (Arcana DC 18 done by him). Reveals cursed, fake, or stolen status.
  - **Quest — The Provenance Ledger:** A ledger of his was stolen during a market disturbance. Recover it, and he opens his back-room stock (one rare-tier item per chapter, otherwise unavailable).
  - **Refusal:** Will not buy items he suspects are stolen. If the party offers Pitax-flagged goods, he asks them politely to leave and remembers them next visit (−1 disposition).

---

#### MASTER SMITH KELDEN
- **Role:** Operator of the kingdom-stamped Capital Smithy. Standard arms for the standing kingdom guard and adventurers.
- **Available:** Chapter 2+ after Smithy built.
- **Appearance:** Restov-trained human, broad-shouldered, late 30s. Forge-darkened skin, soot at the cuffs of his rolled sleeves, kingdom sigil branded on his apron. Two apprentices visible in the background.
- **Personality:** Professional. Treats the smithy like a sworn duty — he took the kingdom-stamp oath when the building was raised and considers shoddy work a betrayal of it. Has no time for haggling but will work overtime for a paying noble. Was a Restov militia armorer before the kingdom drew him south.
- **Voice:** Curt. Asks two questions: "What do you need?" and "When?" Doesn't speak unless answering.
- **Hooks:**
  - **Quest — Iron from the South:** Restov shipments are being intercepted. If the party clears the bandits responsible, Kelden discounts +1 weapons by 25% permanently.
  - **Service — Armor Repair:** Same-day repair of any non-magical armor for half PF2e standard cost.
- **Disposition shift:** +1 if the player commissions kingdom guard equipment (visible patriotism).

---

#### MARKETEER THESSILY
- **Role:** Operator of the Capital Market. Daily restock and price-board manager.
- **Available:** Chapter 2+ after Market built.
- **Appearance:** Halfling woman, late 20s, perpetual half-smile, hair pinned up with a charcoal pencil she also uses to update prices. A bandolier of ledger-strips across her chest. Always moving.
- **Personality:** Brisk and organized to a fault. Knows every stallholder by name and every customer's standing balance. Has zero patience for nobles who think their title gets them priority — first-come-first-served, and she enforces it. Privately runs a small loan operation for new settlers (1% above Restov rates, hates being called a moneylender).
- **Voice:** Quick, friendly, transactional. Punctuates with "next" when she's done with you. Calls everyone "settler" — the highest compliment she has.
- **Hooks:**
  - **Service — Loan:** First chapter at the capital, Thessily offers a 100 gp short-term loan to the founding party (no interest if repaid within one kingdom turn). Refusing offends her; she remembers.
  - **Rumor mill:** She hears everything. For 2 gp she'll point at the right vendor for any item type. For 10 gp she'll tell you which noble is having an affair with which advisor (consistent with KM_NPC_Relations).
- **Disposition shift:** Repaying the loan early grants a 5% market discount permanently.

---

#### FATHER ALDRIC (ERASTIL TEMPLE)
- **Role:** Cleric-vendor at the Capital Temple if the temple is dedicated to Erastil.
- **Available:** Chapter 2+ after the temple is built AND dedicated to Erastil. Mutually exclusive with Ilenne (only one temple deity per kingdom unless the player builds a second temple).
- **Appearance:** Late-50s human, weather-beaten, calloused hands of someone who farmed before he tended a chapel. Plain green-and-brown vestments, an antler-tipped staff. Small dog at his feet — not his, just one that follows him.
- **Personality:** Calm, devotional, slow to anger and slower to praise. Considers his role at the temple a continuation of Jhod's work (KM_NPCs.md), and will defer to Jhod on Erastil matters if Jhod is present. Disapproves of waste — if the party buys more potions than they can carry, he asks why.
- **Voice:** Quiet. Quotes Erastil verses occasionally and means them. Calls the player "settler" or "founder," never by title.
- **Hooks:**
  - **Service — Free Tier-1 Healing:** Once per visit, free casting of Heal (level 1) for any party member who shows respect to Erastil's altar.
  - **Quest — A Wolf at the Gate:** A dire wolf has been sighted near outlying farms. Aldric does not want it killed if it can be relocated. Reward: free Tier-2 healing for life if returned alive; nothing if killed.
- **Disposition shift:** −1 to all temple-related opinions (Aldric, Jhod) for casual desecration of altars. Permanent.

---

#### HIGH SISTER ILENNE (SARENRAE TEMPLE)
- **Role:** Cleric-vendor at the Capital Temple if the temple is dedicated to Sarenrae.
- **Available:** Chapter 2+ after the temple is built AND dedicated to Sarenrae. Mutually exclusive with Aldric.
- **Appearance:** Mid-30s human, golden-brown skin, hair the color of dark honey braided down her back. Wears the layered amber-and-white of a Sarenite high sister. Open palms, no jewelry. Smiles often, but it does not always reach her eyes.
- **Personality:** Warm in surface, steel underneath. She came from Qadira and has not forgotten what redemption costs. Believes Sarenrae's mercy is for the genuinely repentant, not the conveniently sorry — and will refuse to bless an item or person she judges unrepentant. Genuinely happy to help the lost; quietly furious with the willfully cruel.
- **Voice:** Gentle, melodic, with a faint Qadiran accent. Calls the player "child of the Dawnflower" once they've earned it; "friend" until then.
- **Hooks:**
  - **Service — Atonement:** For party members who've committed Evil acts, Ilenne will perform Atonement (full PF2e ritual) for 50 gp materials cost. A wholly corrupt soul — an unrepentant worshipper of Rovagug, a devil-bound tyrant, a willing servant of the Whispering Tyrant — cannot be Atoned (anathema).
  - **Quest — The Lost Caravan:** A Sarenite caravan from Qadira went silent in the southern hexes. Recover survivors or remains. Reward: Sun-blessed Greater Healing Potion.
- **Disposition shift:** +1 for sparing a defeated foe (canonical alignment ledger).

---

#### TANNERY MASTER BORSK
- **Role:** Operator of the Capital Tannery. Leather goods, mounts barding, and saddles.
- **Available:** Chapter 2+ after Tannery built.
- **Appearance:** Half-orc, large, perpetually cheerful despite the smell of his trade. Tusk-broken-and-recapped, leather-stained hands he doesn't bother washing for customers because everyone here knows what tanning is. Wears the simplest possible clothes under a heavy tanner's apron.
- **Personality:** Tirelessly cheerful — genuinely loves the work. Discusses leather provenance the way Verdel discusses gemstones, and expects the listener to be interested. A founder of the early kingdom (he was one of the first non-noble settlers) and offers a discount to the founding party out of sentiment.
- **Voice:** Booming. Laughs often. Calls the player "boss" if they're a founder; "friend" otherwise.
- **Hooks:**
  - **Service — Founder's Discount:** Permanent 15% off all leather goods for any party member present at the kingdom's founding.
  - **Quest — Hide of the Beast:** If the party kills a notable beast (Tuskgutter, the Beast of Malar, etc.), Borsk will craft custom barding or armor from the hide. Custom items use the item's tier as base + appropriate flavor (e.g., Tuskgutter Hide Armor = +3 AC, fear-resist).
- **Disposition shift:** Bringing him any unique beast hide (even unpaid) = +1 permanently.

---

#### MAGISTER VELLEX
- **Role:** Master of the Caster's Tower. Scrolls, wands, identifications.
- **Available:** Chapter 3+ after Caster's Tower built (Ch3 unlock per KM_Loot_Merchants.md).
- **Appearance:** Half-elf, age uncertain (looks 35, is closer to 90), slim, formally dressed in scholar-blue robes with silver trim. Reading glasses he doesn't actually need (an affectation he kept). Always seated when first encountered, surrounded by stacked tomes; rises only for serious customers.
- **Personality:** Scholarly, mildly arrogant, deeply curious. Charges premium for stock (+20%) but identifies unknown items for ten gold flat — he genuinely enjoys the puzzle and considers the fee a courtesy. Dismissive of non-casters until they prove they understand magical theory. Has a soft spot for Octavia (#37) and will discount her purchases personally if she's in the party.
- **Voice:** Precise, occasionally pedantic. Will correct your pronunciation of arcane terms. Calls the player "patron" or "novice" depending on demonstrated knowledge.
- **Hooks:**
  - **Service — Identification:** 10 gp flat fee, no exceptions.
  - **Quest — A Volume Long Sought:** Vellex has been searching for a specific spellbook (Wand of Wonder formula) lost during the Restov-Brevoy schism. If the party recovers it from a Pitax noble's library, Vellex grants permanent 25% off all scrolls and one free L5 scroll of the player's choice.
  - **Special:** If Octavia is in the party, Vellex offers her a Caster's Tower position post-campaign (KM_Mythic_Systems.md flag).
- **Disposition shift:** +1 to Vellex opinion for any successful Arcana check made in his presence at DC 22 or higher.

---

#### QUARTERMASTER GENNRIK
- **Role:** Sole survivor running the Varnhold Stockade salvage shop after the Vanishing.
- **Available:** Chapter 3 only. Disappears (or dies) when Varnhold's fate resolves at chapter end.
- **Appearance:** Human male, gaunt, grey-bearded, half his uniform still kingdom-stamped Varnhold colors and half stitched-together rags. One eye twitches. Carries a notched short sword he never quite puts down. Sleeps in the stockade's old armory.
- **Personality:** Half-mad with survivor's guilt. Watched the Vanishing happen — his memory of it is fragmented, contradictory, and he'll tell three different versions across three visits. Sells salvage at half PF2e standard because he genuinely doesn't think he'll need the gold, but flares into terror or rage if anyone implies the missing villagers are dead. Asks the party every visit if they've found his daughter (Nessa). She is gone.
- **Voice:** Tangents. Drops mid-sentence into a different memory. Calls the player "stranger" until they bring him news of Varnhold, then by their actual name.
- **Hooks:**
  - **Quest — Find Nessa:** Mostly closed-off. If the party finds Nessa's body or her name in Vordakai's records (KM_Ch3.md), bringing the truth to Gennrik triggers either: (a) his peaceful death the next dawn, +5 reputation, or (b) refusal to believe and a final stand defending the empty stockade. Player choice: tell him, lie, or stay silent.
  - **Service — Salvage:** Common+Magic tier loot rolls from KM_Loot_Merchants.md at half-price; weapons and armor only, no consumables.
- **Disposition shift:** None — he doesn't track it. The Nessa moment is the only meaningful interaction.

---

#### MOTHER HALISA
- **Role:** Fence and contraband-broker of the Pitax Black Market.
- **Available:** Chapter 5 only, infiltration path. Inaccessible without Pitax cover identity established.
- **Appearance:** Mwangi human, age impossible to guess (older), face fully veiled with a charcoal-and-amber wrap that leaves only the eyes visible. Hands ringed with cheap brass and one extremely real ruby. Always seated behind a small brass table in a back-of-stall booth. Smells of cardamom and gun-oil.
- **Personality:** Assumes betrayal as the baseline state of every customer; works backward from there. Will not sell to anyone who hasn't named her a price they shouldn't be able to afford. Has informants in the Pitax court and will sell their reports for staggering sums. Considers Mother a trade title, not an honorific — she has children, but the title precedes them.
- **Voice:** Quiet, slow, with a Mwangi southern lilt. Calls the player "stranger" the entire time, even after multiple visits. Ends every transaction with "You did not see this stall."
- **Hooks:**
  - **Service — Flagged Goods:** Per KM_Loot_Merchants.md § PITAX BLACK MARKET. Risk: each flagged item carries a Perception DC 18 detection check by Pitax guards on exit.
  - **Quest — A Letter to a King:** Halisa offers the party an Irovetti-court informant report (unsealed) for 500 gp. Reading it reveals Tartuccio's spy contact (consistent with KM_P2.txt Tartuccio Protocol — does NOT reveal Tartuccio is the spy unless that flag is already tripped). Buying it triggers no fail; reading the contents and acting on them is up to the player.
  - **Special:** Halisa will not sell to any party member with a visible Brevic or Restov sigil. They must remove or hide identifying marks before approaching.
- **Disposition shift:** None tracked. Halisa is purely transactional; goodwill is meaningless to her.

---

> **➡️ EXTENDED VENDORS** (Issili, Mim Wobblegander, The Bonewright, Storyteller-as-trader) **and the AUTHORITATIVE QUALITY-TIER GATE TABLE moved to `KM_Loot.md` — load both files together.**

---

## 🛒 BUY-OPTION SYNTAX (MENU ENTRY)

The DM uses one of these forms in the menu, matched to vendor:

```
[N] Buy — Browse Oleg's wares
[N] Buy — Browse Bokken's potions
[N] Buy — Browse the Old Beldame's curiosities
[N] Buy — Browse Hassuf's caravan stock
[N] Buy — Browse Bartholomew's collection
[N] Buy — Browse Dragn's smithy
[N] Buy — Browse Verdel's wondrous goods
[N] Buy — Browse the Capital Smithy
[N] Buy — Browse the Capital Market
[N] Buy — Browse the Capital Temple offerings
[N] Buy — Browse the Tannery
[N] Buy — Browse the Caster's Tower
[N] Buy — Browse Gennrik's salvage
[N] Buy — Browse Mother Halisa's contraband (Pitax — risk: flagged goods)
```

> **➡️ Extended buy/trade options for Issili, Mim, Bonewright, Storyteller → see `KM_Loot.md`**

When multiple vendor NPCs share a location (Oleg + Svetlana, e.g.), Buy uses
the active speaker's wares. If neither has unique stock, default to the
location's primary inventory (Oleg).

---

## 🔁 CROSS-REFERENCE TO INVENTORIES

| NPC | Inventory section in `KM_Loot_Merchants.md` |
|-----|--------------------------------------------|
| Oleg Leveton | OLEG'S TRADING POST |
| Svetlana Leveton | OLEG'S TRADING POST (shared) |
| Bokken | BOKKEN'S HUT |
| Old Beldame | OLD BELDAME (SWAMP WITCH HUT) |
| Hassuf | HASSUF — WANDERING MERCHANT |
| Bartholomew Delbin | BARTHOLOMEW DELBIN (SECLUDED LODGE) |
| Dragn Stoneward | DRAGN — DWARVEN SMITH |
| Verdel of Brevoy | VERDEL — CAPITAL WONDROUS GOODS |
| Master Smith Kelden | CAPITAL SHOPS § Smithy |
| Marketeer Thessily | CAPITAL SHOPS § Market |
| Father Aldric / High Sister Ilenne | CAPITAL SHOPS § Temple |
| Tannery Master Borsk | CAPITAL SHOPS § Tannery |
| Magister Vellex | CAPITAL SHOPS § Caster's Tower |
| Quartermaster Gennrik | (Ch3 stockade — see KM_Ch3.md; uses Common+Magic tier rolls from KM_Loot_Merchants.md) |
| Mother Halisa | PITAX BLACK MARKET |

> **➡️ Extended vendor inventory cross-refs (Issili, Mim, Bonewright, Storyteller) → see `KM_Loot.md`**

---

## 🗣️ DIALOGUE OPENER LINES (1 per NPC, DM may use verbatim)

```
Oleg        : "If you're here to talk, talk. If you're here to buy, gold's gold."
Svetlana    : "Sit down. There's tea on. Whatever you need — we'll find it."
Bokken      : "Don't touch the green vials. Those are not for selling. Today."
Old Beldame : "You came here. So you know what you want. Say it plain or leave."
Hassuf      : "Welcome, friend. Today's wares are different. Tomorrow's wares are not yet."
Bartholomew : "Marvelous timing. I've just acquired something that BURNS things. Care to see?"
Dragn       : "If it's dwarven and it's mine, you can buy it. If it's elven, get out."
Verdel      : "Each piece is appraised, signed, and accounted. Browse — but slowly."
Kelden      : "Standard arms, kingdom-stamped. What do you need."
Thessily    : "Daily prices on the board. Restock at dawn. You're third in line."
Aldric      : "The Elk Father provides what is needful. Coin offerings welcome."
Ilenne      : "Light brought you here. Let's see what you're meant to leave with."
Borsk       : "Leather is patient work. So am I. What're we making for you today?"
Vellex      : "Identifications: ten gold flat. Anything else: we negotiate."
Gennrik     : "Half-price on most of it. Other half — well. You'd be surprised what survived."
Halisa      : "You did not see this stall. Now: what did you not come for?"
```

> **➡️ Extended opener lines for Issili, Mim, Bonewright, Storyteller → see `KM_Loot.md`**

---

## ⚠️ DM ENFORCEMENT NOTES

- A scene with a vendor present but not yet engaged in dialogue does NOT require
  the Buy option (e.g., walking past Oleg in a busy room). The Buy option is
  required once the vendor is the active dialogue partner OR the player
  explicitly addresses them by name.
- `.buy` may also be used by the player at any time a vendor is in scene to
  open the shop screen directly without clicking through a menu.
- Vendors in capital shops are addressable individually OR collectively
  ("I want to visit the smithy"); both open the same shop screen.
- If a vendor is dead, captured, or otherwise absent (e.g., Halisa during
  a Pitax incident), the shop is closed and the Buy option is replaced with
  `[N] (Shop closed — <reason>)` and is not selectable.

---

*KM_Loot.md — Kingmaker PF2e Text Adventure | Vendor NPC Roster & Buy-Option Rule v1.0 | 2026-05-01*


---

<!-- merged from KM_Loot.md (v93.21 file consolidation) -->

# KINGMAKER — VENDOR ROSTER (EXTENDED) + QUALITY-TIER GATE
## KM_Loot.md | **PAIR-LOAD WITH KM_Loot.md** (load both)

> **DM:** This sibling holds the four extended vendors added post-v15.1
> (Issili, Mim Wobblegander, The Bonewright, Storyteller-as-trader) and the
> AUTHORITATIVE quality-tier gate table the DM checks before allowing any
> Magic+ item purchase. Main file `KM_Loot.md` holds the universal `[Buy]`
> rule, the original 9 named vendors, and the dialogue opener lines.

---

## 📋 EXTENDED VENDOR ROSTER

The following four vendors are project-canon. They expand the kingdom's
quality ceiling and copy the CRPG model of vendors that gatekeep Rare/Epic
loot. Use these names, voices, and quirks; do not improvise replacements.

---

#### ISSILI (TOWER OF KNOWLEDGE)
- **Role:** Historian-archivist of the Capital Tower of Knowledge. Wondrous-item gatekeeper for the kingdom — sells items the lesser shops cannot stock.
- **Available:** Chapter 3+ after Tower of Knowledge built. Mutually compatible with Verdel (Issili stocks rare-tier wondrous; Verdel stocks magic-tier).
- **Appearance:** Issian human woman, mid-30s, raven hair pinned back severely, dark-blue scholar robes with silver clasps shaped like open books. Ink-stained fingertips she does not bother to clean. Reads two books at once (one in each hand) and somehow loses neither place.
- **Personality:** Brilliant, impatient with idiocy, generous with knowledge. Believes the Tower exists to preserve what would otherwise be lost — she'll spend an hour explaining a relic's provenance for free, then charge full price for the relic itself. Treats merchants like Verdel as colleagues, peasant-tier traders as background noise. Mildly obsessed with Old Sarkorian artifacts.
- **Voice:** Crisp, fast, faintly Brevic-aristocratic. Calls the player "Founder" once they've impressed her; "you" until then. Ends explanations with "— do you understand, or shall I repeat it?" and is genuine about both options.
- **Hooks:**
  - **Service — Rare Wondrous Stock:** Issili is the ONLY vendor who carries Rare-tier wondrous items in standard rotation (rings, cloaks, staves, headbands above +2 bonus). Stock rotates per kingdom turn.
  - **Quest — The Sarkorian Index:** A fragmented index of pre-Worldwound Sarkorian relics is rumored intact in Varnhold's old library (Ch3). Recover it. Reward: 30% lifetime discount + Issili will identify any cursed item for free thereafter.
  - **Lore:** Knows three lore tiers about the Stolen Lands' First World incursion history. Each tier costs 100 gp to unlock OR can be earned by delivering Storyteller relic fragments she hasn't seen.
- **Disposition shift:** +1 for any successful Arcana / Occultism / Society check in her presence at DC 22 or higher. Stacks with Vellex disposition (separate ledger).

---

#### MIM WOBBLEGANDER
- **Role:** Gnome jeweler and gemstone broker. Capital market, smaller booth tucked between Thessily's stalls and the Tannery.
- **Available:** Chapter 2+ after Market built. Earlier than most quality-gate vendors — a stepping-stone between Common and Rare tiers.
- **Appearance:** Gnome woman, perhaps 80 (gnomes age strangely), wild copper-orange hair held back with three jeweler's loupes. Apron pockets bristling with calipers, a magnifying glass, and a small hammer she swears is for jewelry but uses on customers' knuckles when they touch the merchandise. Stands on a stool to see over her own counter.
- **Personality:** Encyclopedic about gemstones, dismissive of sentiment ("a tear-shaped sapphire is just a sapphire that got cut wrong"). Charges fair prices but will never lower them — haggling offends her professional standards. Genuinely delighted by uncut stones brought in from the field; pays premium for any gem the party recovers from a dungeon.
- **Voice:** High, fast, gnome-cadenced. Calls everyone "dearie" regardless of rank. Punctuates appraisals with "mm, yes, mm" while peering through her loupe.
- **Hooks:**
  - **Service — Gem Appraisal:** Free identification of any gemstone, +5% sale value if the player sells the gem to her instead of any other vendor.
  - **Service — Gemstone-Set Wondrous:** Magic-tier wondrous items that key off gemstones (Ioun Stones, Gem of Brightness, Rings with set stones, Goggles of Night). Price tier: Magic only — she does not stock Rare.
  - **Quest — The Wobblegander Vault:** A family vault in Five Kings holds her grandmother's collection. Recover the deed (held by a Pitax noble per Ch4 hooks). Reward: she opens the vault and offers ONE Rare-tier gemstone wondrous to the party at half price.
- **Disposition shift:** Bringing her any uncut gemstone (even unsold) for appraisal = +1 permanently.

---

#### THE BONEWRIGHT (RANDOM HEX VENDOR)
- **Role:** Wandering skeleton merchant. Appears at random in unmarked hexes during exploration. Carries one item only — never the same item twice.
- **Available:** Any chapter from Ch1 onward. **Encounter trigger:** while exploring an empty hex, roll d20 — on a natural 20, OR on Perception DC 22 if the party has the *Storyteller's Token* (KM_Exploration.md:66), the Bonewright appears at the next short rest. Appears at most once per kingdom turn. The DM does NOT pre-announce the trigger; the encounter narration begins with a campfire glint of bone in the dark.
- **Appearance:** A skeleton in a moth-eaten merchant's coat over rusted half-plate, neck wrapped in a faded scarf no body needs. One eye-socket holds a single working mechanical lens that whirrs and refocuses. Pulls a small two-wheeled cart that creaks louder than any cart should. Speaks without a tongue, voice arriving from somewhere just behind the listener's left ear.
- **Personality:** Polite, patient, deeply odd. Does not negotiate. Does not haggle. Names a price; the price is what the item is worth; the player either pays or does not. Will not sell the same item twice — even across kingdom turns, even across campaigns, even on NG+. If asked who he was alive, says: *"I forget. The cart remembers. That is enough."*
- **Voice:** Soft, slow, slightly out of sync with his jaw movements. Calls the player "traveler" always. Ends each visit with "Until the road brings us together again — or it does not."
- **Hooks:**
  - **Service — One Item Per Encounter:** The cart contains exactly one item, rolled by the DM from the **Rare** or **Epic** tier in `KM_Loot_Merchants.md` (50/50). Never a duplicate of any item the party has bought from him before. Price: standard market value × 1.5 (luck premium).
  - **Refusal:** If the player declines to buy, the Bonewright bows, the cart creaks, and he is gone before the next narrative sentence finishes. The same item does NOT return next encounter — it is lost permanently.
  - **Quest — The Cart's Ledger:** On the player's 5th Bonewright encounter, his cart includes a ledger written in a dead language. Translating it (Occultism DC 30 OR delivering it to the Storyteller) reveals the Bonewright's name in life — and resolves whether his next appearance is hostile (he is owed something) or final (he says goodbye, and the cart rolls into the dark forever).
- **Disposition shift:** None tracked. The Bonewright neither remembers nor forgets — except via the ledger.

---

#### THE STORYTELLER (TRADER, NOT VENDOR)
- **Role:** Lore-trader and unique-item gatekeeper for relic fragments and cyclops coins. **NOT a standard vendor — does NOT use the `[Buy]` menu rule.**
- **Available:** Chapter 2+ once the capital is founded. Full writeup in `KM_Exploration.md` § THE STORYTELLER & RELIC FRAGMENTS.
- **Why he's listed here:** Players will often try to "buy" from him. Reject the `[Buy]` framing — the Storyteller exchanges items for items (relic fragments → unique rewards) or items for lore. Gold is meaningless to him. Replace the standard Buy option with `[N] Trade — Offer relics to the Storyteller` and route to his exchange table in KM_Exploration.md.
- **Quality gate:** Unique narrative-tier rewards (Storyteller's Token, +2 vs Lantern King checks, etc.) — these items appear nowhere else in the game and are not on the Common→Legendary tier scale.

---

## 📊 VENDOR QUALITY-TIER GATE TABLE

> **DM:** This is the AUTHORITATIVE table for which vendor stocks which loot tier.
> When the player asks for an item, check the player's currently-unlocked vendors against the item's tier. If no unlocked vendor stocks that tier, the item is not buyable yet — the DM may say so and (optionally) hint at which vendor would carry it.
> Tiers from `KM_Loot_Merchants.md`: **Common · Magic · Rare · Epic · Legendary**

| Vendor | Common | Magic | Rare | Epic | Legendary | Unlocks | Notes |
|--------|:------:|:-----:|:----:|:----:|:---------:|---------|-------|
| Oleg / Svetlana | ✅ | — | — | — | — | Ch1 | Mundane gear floor |
| Bokken | ✅ | ✅ (alch) | — | — | — | Ch1 | Alchemical / potions only |
| Old Beldame | — | ✅ | ✅ | — | — | Ch1 | Curiosities, herbs, swamp-rare |
| Hassuf | — | ✅ | ✅ | — | — | Ch1, every 14d | Caravan rotation |
| Bartholomew | — | ✅ | ✅ | ✅ (1/visit) | — | Ch1 (Lodge) | One explosive Epic per visit |
| Dragn | — | ✅ | ✅ (Adamantine post-quest) | — | — | Ch2 | Smithwork specialist |
| Verdel | — | ✅ | — | ✅ (back-room post-quest) | — | Ch2 (Market) | Wondrous-magic, Epic if Provenance Ledger returned |
| Kelden (Capital Smithy) | ✅ | ✅ | — | — | — | Ch2 | Standard arms, kingdom-stamped |
| Thessily (Capital Market) | ✅ | ✅ | — | — | — | Ch2 | Daily mundane + minor magic |
| **Mim Wobblegander** | — | ✅ (gem-set) | ✅ (Vault unlock only) | — | — | Ch2 | Gemstone wondrous, Magic-tier; Rare via vault quest |
| Aldric / Ilenne (Temple) | ✅ | ✅ (divine) | ✅ (blessed-ritual) | — | — | Ch2 | Divine consumables, Atonement service |
| Borsk (Tannery) | ✅ | ✅ | ✅ (unique hide only) | — | — | Ch2 | Custom barding from named-beast hides |
| Vellex (Caster's Tower) | — | ✅ (scrolls) | ✅ (scrolls L5+) | ✅ (1 scroll if Wand-of-Wonder quest done) | — | Ch3 | Scrolls, wands, identification |
| **Issili (Tower of Knowledge)** | — | — | ✅ (rotation) | ✅ (Sarkorian Index quest) | — | Ch3 | **Sole standard-rotation Rare-wondrous source** |
| Gennrik (Varnhold) | ✅ | ✅ | — | — | — | Ch3 only | Half-price salvage; Ch3 only, expires |
| **The Bonewright** | — | — | ✅ (50%) | ✅ (50%) | — | Any (random) | One item per encounter; never duplicates; +50% price |
| Halisa (Pitax Black Market) | — | — | ✅ | ✅ | ✅ (flagged) | Ch5 (infiltration) | Contraband risk: Perception DC 18 on exit |
| Storyteller (TRADER) | — | — | — | — | Unique narrative | Ch2 | Trades relics/coins for unique rewards; NOT a [Buy] vendor |

**Quality-gate enforcement:**
- If player requests a Rare item before Ch3, the only sources are Old Beldame, Hassuf, Bartholomew, Dragn (Adamantine post-quest), Borsk (unique hide), or a Bonewright encounter. No others.
- If player requests an Epic item before Ch3, the only sources are Bartholomew (1/visit) or a Bonewright encounter. Rare for the early game, by design.
- Legendary items are Halisa-only (Ch5) — there is no Legendary vendor before then. The Bonewright caps at Epic.
- Pitax-flagged items from Halisa cannot be openly used in the kingdom — see KM_Loot_Merchants.md § PITAX BLACK MARKET.

---

## 🔁 EXTENDED CROSS-REFERENCE TO INVENTORIES

| NPC | Inventory section |
|-----|-------------------|
| Issili | (Add to KM_Loot_Merchants.md § ISSILI — Rare-wondrous rotation; rolls from KM_Loot_Merchants.md Rare table) |
| Mim Wobblegander | (Add to KM_Loot_Merchants.md § MIM WOBBLEGANDER — Magic-tier gemstone wondrous) |
| The Bonewright | KM_Loot_Merchants.md (random Rare/Epic single-item draw, +50% price; never duplicates) |
| The Storyteller | KM_Exploration.md § STORYTELLER REWARDS (item-for-item trade, NOT [Buy]) |

---

## 🛒 EXTENDED BUY/TRADE OPTIONS (append to main syntax)

```
[N] Buy — Browse Issili's archive stock
[N] Buy — Browse Mim Wobblegander's gemstones
[N] Buy — Examine the Bonewright's cart
[N] Trade — Offer relics to the Storyteller   ← NOT [Buy]; routes to KM_Exploration.md
```

---

## 🗣️ EXTENDED OPENER LINES (append to main)

```
Issili      : "Founder. The archive is open. State your interest precisely — I do not guess."
Mim         : "Mm. Yes. Mm. Bring it closer, dearie — the loupe doesn't walk to you."
Bonewright  : "Traveler. The cart has one thing. The cart will not have it again. Look — or do not look."
Storyteller : "Bring me pieces of the old world. I will tell you what they mean."
```

---

*KM_Loot.md — Kingmaker PF2e Text Adventure | Extended Vendor Roster + Quality-Tier Gate v1.0 | 2026-05-03*
