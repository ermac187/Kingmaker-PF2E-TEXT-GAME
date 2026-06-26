# KINGMAKER — BUILDS: FIGHTER 7–10
## KM_Builds_E4.md | Referenced by: KM_BuildScreen.md, KM_Builds_E2.md

> **DM:** Load this file for Fighter builds 7–10. Builds 1–6 are in KM_Builds_E2.md.
> Each entry: stat block at L1 + full leveling map L1–20 + race options.
> After confirming ancestry, output full `.status` panel before any scene content.
>
> **ANCESTRY HEIGHT — NON-NEGOTIABLE:**
> Dwarf 4–4½ ft | Halfling 2½–3 ft | Gnome 3–3½ ft | Human/Half-Elf/Half-Orc 5–6 ft | Elf 5½–6½ ft | Orc 6–7 ft
>
> **ANCESTRY BASE HP:**
> Dwarf 10 | Orc 10 | Half-Orc 10 | Human 8 | Aasimar 8 | Gnome 8 | Elf 6 | Halfling 6
>
> **HP CORRECTION:** New L1 HP = Listed HP − Default Ancestry HP + Chosen Ancestry HP
>
> **SPEED:** Dwarf 20 ft | Human 30 ft | Elf 30 ft | Halfling 25 ft | Gnome 25 ft | Orc 25 ft | Half-Orc 25 ft

---

## ANCESTRY CONFIRMATION PROMPT
> **⛔ Do NOT use A/B/C. Present the Race Options table (10 rows) from the build.**
> See KM_BuildSetup.md PROMPT 1 for the exact output format. Player picks by
> number (1–10) or types any PF2e ancestry name. Table is guidance, not a gate.

---

# ══════════════════════════════════════
# FIGHTER (builds 7–10)
# ══════════════════════════════════════

## BUILD — TRIP GRAPPLE FIGHTER
**Human (Versatile Heritage) | Fighter (Grapple) | Background: Warrior**
*Knockdown + Combat Grab — Trip and Grapple on the same Strike, pin enemies in reach for free AoO bait.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 12 | 16 | 10 | 14 | 8 |
| Mod | +4 | +1 | +3 | +0 | +2 | -1 |

**HP** 21 | **AC** 17 (Scale Mail) | **Fort** +7 | **Ref** +5 | **Will** +6 | **Speed** 25 ft
**Weapon:** Flail (1H B, 1d6+4, disarm, sweep) + free hand for Grapple | **Armor:** Scale Mail
**Skills:** Athletics +8, Intimidation +3, Warfare Lore +2, Survival +4
**Features:** Attack of Opportunity, Expert martial L1
**L1 Feats:** Natural Ambition + Knockdown | **Boost:** STR → CON → WIS → DEX

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Orc | Hold-Scarred | STR 18 + Diehard makes this grappler the hardest target to put down; a Wrestler who gets knocked out loses its free-hand Grapple and the entire control engine collapses. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition grabs Knockdown and Combat Grab at L1+L2 without any feat sacrifice, front-loading the prone+grabbed combo a full level earlier than Orc can. |
| 3 | Half-Orc | Hold-Scarred | Orc Blood + Human stat flexibility preserves STR 18 + CON 16 while still accessing Diehard, the same Diehard effect as full Orc with better stat array coverage. |
| 4 | Dwarf | Mountain's Stoutness | Mountain's Stoutness +1 HP/level on CON 16 stacks to the highest HP total at every level — a grappler who holds enemies in place gets attacked more, and raw HP absorbs the punishment. |
| 5 | Lizardfolk | Frilled | Frilled's demoralize syncs with Knockdown; applying Frightened 1 on a Trip-on-hit means the prone target has −1 to saves and attacks while the Grapple holds. |
| 6 | Tiefling | Pitborn | Pitborn Athletics bonus stacks directly with STR 18 for Trip/Grapple checks — the most reliable way to improve contested Athletics rolls against large/powerful enemies. |
| 7 | Goblin | Unbreakable | Unbreakable +4 max HP on a Grapple build that voluntarily spends its free hand means it can't use a shield — free HP compensates for the lost Shield Block defense. |
| 8 | Halfling | Gutsy | Gutsy prevents the Frightened critical failure that would force a Grappler to release its hold on the worst possible moment during a boss fight. |
| 9 | Half-Elf | Elf Atavism | Ancient Elf opens Monk Dedication at L1 for free — Monk's Grab gives automatic Grapple on a successful Strike, turning every Knockdown into a free Grapple with zero action cost. |
| 10 | Catfolk | Clawed | Clawed natural attack is a free action-agnostic Strike usable while both hands hold a Grapple or after the Flail + free-hand combo, maintaining pressure between Pin Down reactions. |

**Leveling — 13 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 21 | Attack of Opportunity, Expert martial | Natural Ambition + Knockdown (Trip on hit) |
| 2 | 13 | — | Combat Grab (free Grab on hit) |
| 3 | 13 | Bravery | Slam Down (Strike prone enemy after Trip) |
| 4 | 13 | — | Brutish Shove (push 5 ft on hit) |
| 5 | 13 | Ability Boost (STR/CON+2), Weapon Master | Weapon Specialization + Improved Knockdown |
| 6 | 13 | — | Shatter Defenses |
| 7 | 13 | — | Whirlwind Strike |
| 8 | 13 | — | Pin Down (reaction vs escaping grapples) |
| 9 | 13 | Combat Flexibility, Master Will | Devastator |
| 10 | 13 | Ability Boost | Greater Weapon Specialization |
| 11 | 13 | — | Positioning Strike |
| 12 | 13 | — | Weapon Surge |
| 13 | 13 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 13 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 13 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 13 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** STR+2 first. Combat Grab at L2 — free Grab stacks with Knockdown for prone+grabbed in one action.

---

## BUILD — LONGBOW ARCHER FIGHTER
**Human (Versatile Heritage) | Fighter (Archer) | Background: Hunter**
*Longbow + Triple Shot — consistent mid-range output, no reload penalty, sustainable ranged DPR.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 12 | 18 | 14 | 10 | 14 | 10 |
| Mod | +1 | +4 | +2 | +0 | +2 | +0 |

**HP** 20 | **AC** 18 (Scale Mail) | **Fort** +6 | **Ref** +8 | **Will** +6 | **Speed** 25 ft
**Weapon:** Longbow (2H P, 1d8, 100 ft, deadly d10) | **Armor:** Scale Mail
**Skills:** Athletics +3, Survival +6, Stealth +6, Perception +6
**Features:** Attack of Opportunity, Expert martial L1
**L1 Feats:** Natural Ambition + Point-Blank Shot | **Boost:** DEX → WIS → CON → STR

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Elf | Ancient Elf | Ancient Elf opens a free Ranger Dedication at L1 — Hunt Prey applies a +2 circumstance bonus to the first Longbow Strike each round, stacking on top of Triple Shot's volume. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition grabs Point-Blank Shot and Far Shot at L1, establishing both in-range accuracy and extreme-range reach before the first encounter even begins. |
| 3 | Catfolk | Cat's Luck | Cat's Luck rerolls a DEX or Reflex save 1/day — a stationary longbow archer that fires from the back line still eats AoEs, and the reroll saves a full turn of output. |
| 4 | Half-Elf | Elf Atavism | Elf Atavism unlocks Elven Accuracy for a free reroll of 1s on Longbow attacks — the highest single-feat DPR increase available to any bow Fighter build. |
| 5 | Tengu | Dogtooth | Tengu Weapon Training grants an extra martial weapon proficiency group — opens the Elven Longbow or Gnome Flickmace as backup melee weapons without a feat investment. |
| 6 | Halfling | Halfling Luck | Halfling Luck rerolls any failed check 1/day — at DEX 18 accuracy, the only meaningful threat to this build is a series of unlucky misses on a Triple Shot volley. |
| 7 | Goblin | Irongut | Irongut Goblin resists ingested poison/Fort checks — a Longbow archer in the back row is the first target for alchemical sabotage, and this closes that specific vulnerability. |
| 8 | Fetchling | Liminal | Shadow Step 1/day lets this Longbow build escape a melee pin without using 3 actions to Stride to safety, preserving the full Point-Blank Shot + Triple Shot routine. |
| 9 | Gnome | Umbral | Umbral Gnome darkvision removes the need for a light source that signals position — a Stealth-based archer at 25 ft speed with Stealth +6 thrives in darkness. |
| 10 | Orc | Hold-Scarred | Diehard keeps the DPR anchor alive when a single lucky enemy charge would otherwise remove the party's highest sustained damage source in one action. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Attack of Opportunity, Expert martial | Natural Ambition + Point-Blank Shot |
| 2 | 12 | — | Far Shot |
| 3 | 12 | Bravery | Running Reload |
| 4 | 12 | — | Parting Shot (Step then shoot as reaction) |
| 5 | 12 | Ability Boost (DEX/WIS+2), Weapon Master | Weapon Specialization + Triple Shot |
| 6 | 12 | — | Shatter Defenses |
| 7 | 12 | — | Multishot Stance (2 arrows per Strike) |
| 8 | 12 | — | Incredible Aim |
| 9 | 12 | Combat Flexibility, Master Will | Devastating Strike |
| 10 | 12 | Ability Boost | Greater Weapon Specialization |
| 11 | 12 | — | Mobile Shot Stance |
| 12 | 12 | — | Weapon Surge |
| 13 | 12 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 12 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 12 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 12 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** DEX+2 first. Running Reload at L3 — removes action cost of reloading while moving, essential.

---

## BUILD — INTERCEPTING SHIELD FIGHTER
**Human (Versatile Heritage) | Fighter (Shield) + Guardian Dedication | Background: Guard**
*Intercepting Shield + Shield Block — redirect hits to yourself, cover allies without losing offense.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 16 | 14 | 16 | 10 | 12 | 12 |
| Mod | +3 | +2 | +3 | +0 | +1 | +1 |

**HP** 21 | **AC** 18 (Scale Mail) | **Fort** +7 | **Ref** +6 | **Will** +5 | **Speed** 25 ft
**Weapon:** Longsword (1H S, 1d8+3, versatile P) + Steel Shield | **Armor:** Scale Mail
**Skills:** Athletics +5, Intimidation +3, Diplomacy +3, Warfare Lore +2
**Features:** Attack of Opportunity, Expert martial L1, Shield Block
**L1 Feats:** Natural Ambition + Shield Block | **Boost:** CON → STR → CHA → DEX

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Dwarf | Unburdened Iron | Unburdened Iron lets this Guardian Fighter wear Full Plate at 25 ft speed — the highest possible AC while still intercepting adjacent allies requires maximum armor and maximum mobility. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition grabs Shield Block and Intercepting Shield setup at L1, locking the Guardian Dedication reaction chain before L2 without a feat gap. |
| 3 | Orc | Hold-Scarred | CON 16 + Hold-Scarred means a Fighter who deliberately eats redirected hits from Intercepting Shield needs three knockdowns to drop — the tank's tank. |
| 4 | Half-Orc | Hold-Scarred | Orc Blood preserves Human stat flexibility (CON 16 + STR 16 intact) while still accessing Hold-Scarred — best of both ancestries for a redirect-damage build. |
| 5 | Goblin | Unbreakable | Unbreakable +4 max HP directly compensates for every redirected hit absorbed via Intercepting Shield — Guardian's Deflection turns damage into math, and raw HP wins that math. |
| 6 | Halfling | Hillock | Hillock restores extra HP per rest on CON 16 base — a Guardian that absorbs hits for others needs maximum sleep-recovery to show up at full HP each encounter. |
| 7 | Lizardfolk | Frilled | Frilled demoralize on a CON 16/CHA 12 build gives the Guardian Fighter a free Intimidation fear action when hit, creating an AoE debuff from the very hits it absorbs. |
| 8 | Half-Elf | Elf Atavism | Ancient Elf opens Champion Dedication at L1 — Lay on Hands on a Guardian Fighter who can redirect damage AND heal the target afterward is one of the best protective combinations available. |
| 9 | Tiefling | Grimspawn | Grimspawn void resist 5 plugs the most common non-fire magical damage type a frontline Guardian faces; the Intimidation ancestry feat adds demoralize off CHA 12 with proficiency training. |
| 10 | Catfolk | Clawed | Clawed natural attack gives the shield-hand a Strike option on rounds where Shield Warden has been triggered and the one-handed Longsword hasn't swung yet — no weapon swap required. |

**Leveling — 13 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 21 | Attack of Opportunity, Expert martial | Natural Ambition + Shield Block |
| 2 | 13 | — | Guardian Dedication (Intercepting Shield reaction) |
| 3 | 13 | Bravery | Aggressive Block |
| 4 | 13 | — | Shield Warden |
| 5 | 13 | Ability Boost (CON/STR+2), Weapon Master | Weapon Specialization + Knockdown |
| 6 | 13 | — | Quick Shield Block |
| 7 | 13 | — | Disruptive Stance |
| 8 | 13 | — | Guardian's Deflection |
| 9 | 13 | Combat Flexibility, Master Will | Devastating Strike |
| 10 | 13 | Ability Boost | Greater Weapon Specialization |
| 11 | 13 | — | Fortress Shield |
| 12 | 13 | — | Weapon Surge |
| 13 | 13 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 13 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 13 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 13 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** CON+2 first. Guardian Dedication at L2 — Intercepting Shield enables ally protection chain before Quick Shield Block.

---

## BUILD — REACH SENTINEL FIGHTER
**Human (Versatile Heritage) | Fighter (Reaction) + Sentinel Dedication | Background: Warrior**
*Knockdown + Sentinel Dedication — Trip on every AoO hit, maximum reach zone control.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 12 | 16 | 10 | 14 | 8 |
| Mod | +4 | +1 | +3 | +0 | +2 | -1 |

**HP** 21 | **AC** 19 (Full Plate) | **Fort** +7 | **Ref** +5 | **Will** +6 | **Speed** 20 ft
**Weapon:** Halberd (2H P, 1d10+4, reach 10 ft, versatile S) | **Armor:** Full Plate
**Skills:** Athletics +6, Intimidation +3, Warfare Lore +2, Survival +6
**Features:** Attack of Opportunity, Expert martial L1
**L1 Feats:** Natural Ambition + Knockdown | **Boost:** STR → WIS → CON → DEX

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Dwarf | Unburdened Iron | Unburdened Iron removes the Full Plate speed penalty entirely — this build starts in Full Plate at 20 ft; Unburdened Iron makes the reach-zone control happen at no mobility cost. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition secures Knockdown and Lunge at L1+L2, giving Trip-on-hit at 15 ft reach immediately — enemies entering the zone risk going prone from the first encounter. |
| 3 | Half-Orc | Hold-Scarred | A pure-AoO build in Full Plate that never retreats needs Diehard; Half-Orc keeps STR 18 + CON 16 intact while Hold-Scarred extends the inevitable final stand. |
| 4 | Orc | Hold-Scarred | Pure Orc's Hold-Scarred at STR 18 base with 2 extra max HP over Half-Orc is the optimal choice when staying alive longer than anyone expects is the entire point. |
| 5 | Goblin | Unbreakable | Unbreakable +4 max HP on a Full Plate build that never Strides means every HP matters — the pure AoO build must survive every hit it baits, and raw HP is the most honest defense. |
| 6 | Tiefling | Pitborn | Pitborn fire resist 5 + Athletics syncs with STR 18 Halberd Knockdown attempts — Frightened 1 from fire-adjacent flavor is the weakest link in this build, and Pitborn's resist covers it. |
| 7 | Lizardfolk | Frilled | Frilled demoralize on a hit means every AoO simultaneously deals damage and applies Frightened 1 — consecutive AoOs each round stack fear on incoming enemies without extra actions. |
| 8 | Halfling | Gutsy | Gutsy prevents a Frightened critical failure that would ruin a Disruptive Stance + AoO turn by forcing the build to spend its reaction on a fear reroll instead of a Strike. |
| 9 | Half-Elf | Elf Atavism | Ancient Elf opens Sentinel Dedication for free at L1 — advanced armor expertise arrives earlier, letting the build reach maximum AC long before Weapon Legend unlocks. |
| 10 | Leshy | Vine | Vine Leshy Athletics in natural terrain boosts Combat Grab and Knockdown checks — a reach AoO build that also forces grabs on every entry makes the entire zone a grapple trap. |

**Leveling — 13 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 21 | Attack of Opportunity, Expert martial | Natural Ambition + Knockdown (Trip on hit) |
| 2 | 13 | — | Sentinel Dedication (armor expertise earlier) |
| 3 | 13 | Bravery | Lunge (reach 15 ft for 1 Strike) |
| 4 | 13 | — | Combat Grab |
| 5 | 13 | Ability Boost (STR/WIS+2), Weapon Master | Weapon Specialization + Improved Knockdown |
| 6 | 13 | — | Shatter Defenses |
| 7 | 13 | — | Disruptive Stance |
| 8 | 13 | — | Positioning Strike |
| 9 | 13 | Combat Flexibility, Master Will | Devastator |
| 10 | 13 | Ability Boost | Greater Weapon Specialization |
| 11 | 13 | — | Positioning Strike |
| 12 | 13 | — | Weapon Surge |
| 13 | 13 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 13 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 13 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 13 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** STR+2 first. Knockdown at L1 — Trip on every AoO hit, foundation of the zone control strategy.

---

> **➡️ Fighter builds 1–6: see `KM_Builds_E2.md`**
> **➡️ Full class index: see `KM_BuildScreen.md`**

*KM_Builds_E4.md — Kingmaker PF2e Text Adventure | Fighter Builds 7–10 v1.0*
