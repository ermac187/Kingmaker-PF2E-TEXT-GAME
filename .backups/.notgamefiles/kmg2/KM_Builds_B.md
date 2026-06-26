# KINGMAKER — BUILDS: BARBARIAN (1–3)
## KM_Builds_B.md | Referenced by: KM_BuildScreen.md, KM_Companions_Builds.md

> **DM:** Load this file when player or companion selects Barbarian builds 1–3. Builds 4–6: KM_Builds_B5.md. Builds 7–10: KM_Builds_B2.md. Bard: KM_Builds_B4.md.
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
# BARBARIAN
# ══════════════════════════════════════

## BUILD — TACTICAL REACH KING (GIANT INSTINCT, HEAVY PLATE VARIANT)
**Human (Versatile Human) | Barbarian (Giant Instinct) | Background: Warrior**
*Become Large during Rage. Guisarme + Large rage = 15 ft reach at L1, 20 ft at L7, 25 ft at L13. The "God Combo": Heavy Plate at L1 via Versatile Human → Sentinel Dedication scaling at L2. Battlefield controller, tank, and high-DPR striker.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 10 | 16 | 10 | 14 | 10 |
| Mod | +4 | +0 | +3 | +0 | +2 | +0 |

**HP** 23 | **AC** 19 (Full Plate, DEX cap 0, Trained Heavy) | **Init** +7 | **Perc** +7 | **Speed** 20 ft
**Fort** +8 | **Ref** +3 (Bulwark — treats failed Reflex save vs area as success) | **Will** +7
**Weapon:** Guisarme (2H S, 1d10+4 / +1d10+10 Large+Rage, Reach, Trip) | **Armor:** Dragon Plate (homebrew, Resist fire 5) or Full Plate (Bulwark, Heavy)
*Alt: Maul (1d12 B, Shove, Backswing) — trades 5 ft reach for max single-hit damage.*
**Skills:** Athletics +7 (Trained, → Expert L3), Acrobatics +1, Intimidation +3 (Trained via Warrior bg), Medicine +5, Warfare Lore +3 (Trained via Warrior bg), Crafting +1, Perception +7
**Class Features:** Rage (Giant — Large size, +6 damage, 10 ft reach, TempHP = level+CON), Deny Advantage, Raging Resistance (vs physical from chosen alignment damage type per Instinct rules)
**Key Feats:** L1 Heritage Versatile Human → bonus general feat: Armor Proficiency (Heavy via campaign homebrew armor menu) | L1 Ancestry → Natural Ambition (grants Sudden Charge as bonus class feat) | L1 Class → Raging Intimidation | L1 Skill (Warrior bg auto) → Intimidating Glare | L2 Class → Sentinel Dedication | L3 General → Toughness | L3 Class → Titan Wrestler
**Boost Priority:** STR → CON → WIS → DEX

**The "God Combo" (L1–L3 stack):**
- **Versatile Human** grants Armor Proficiency (Heavy) at L1 → wear Full Plate immediately.
- **Sentinel Dedication (L2)** auto-scales Heavy Armor to Expert at L7, Master at L15.
- **Bulwark trait** (Full Plate) → DEX is irrelevant for Reflex; use +3 flat. Frees the stat to dump.
- **Toughness (L3)** patches Barbarian's mid AC with massive HP pool (16 + level HP, +1/level from Toughness).
- **Titan Wrestler (L3)** lets you Trip/Shove enemies up to TWO sizes larger than you. While Raging Large, that's Gargantuan.

**Race Options** *(this build is locked to Human; Versatile Human heritage required for Heavy Armor at L1. Listing alt heritages for reference only — switching costs the L1 Heavy Plate access.)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Versatile Human | REQUIRED for Heavy Armor proficiency at L1 — the entire build hinges on this. |
| 2 | Human | Natural Ambition | Without Versatile Human you lose Full Plate L1; switch armor to Hide and re-spec ancestry feat to Hold-Scarred analog. |
| 3 | Half-Orc | Orc Blood | Loses L1 Heavy Armor but gains Hold-Scarred Diehard for Giant rage 0-HP drops. |
| 4 | Orc | Hold-Scarred | Original carousel chassis — Diehard free + 10 base HP. Hide Armor instead of Full Plate. AC drops to 18, no Bulwark. |
| 5 | Dwarf | Ancient-Blooded | Already proficient in Heavy Armor as a base ancestry — alternate route to Full Plate without burning Versatile Human. |
| 6 | Dwarf | Mountain's Stoutness | +1 HP/level stacks; trade Bulwark for native dwarf survivability. |
| 7 | Lizardfolk | Cliffscale | Natural armor bonus + STR 18 synergy; Hide Armor variant. |
| 8 | Goblin | Unbreakable | +4 max HP and Goblin Scuttle mobility patch the speed gap from Large size repositions. |
| 9 | Halfling | Hillock | Extra HP per rest matters when Giant Barbarians burn through huge pools. Hide Armor variant. |
| 10 | Catfolk | Clawed | Backup agile claw attack on MAP-3 when Guisarme MAP penalties make a third swing nonviable. |

**LEVELING MAP — TACTICAL REACH KING**
HP per level: 12 + Con mod (+3) = **15 HP/level** (Toughness L3+ adds +1/level retroactively, becomes 16/level)

| Lvl | HP | Auto Features (class progression) | [PICK] Feat slots |
|-----|----|-----------------------------------|--------------------|
| 1 | 23 | Rage (Giant — Large, +6 dmg, 10 ft reach), Deny Advantage, Raging Resistance, Giant Instinct anathema | Class: Raging Intimidation • +Sudden Charge (Natural Ambition bonus class feat) • Heritage general feat: Armor Proficiency • Skill (bg auto): Intimidating Glare |
| 2 | 15 | — | Class: Sentinel Dedication • Skill: Assurance (Athletics) |
| 3 | 16 (+1 Toughness retro) | **Furious Footfalls** (flat +5 status to Speed, unconditional; +10 while raging) | General: Toughness • Class: Titan Wrestler |
| 4 | 15 | — | Class: Swipe • Skill: Powerful Leap |
| 5 | 15 | **Brutal Critical** (extra die on crit), Ability Boost (STR/CON+2) | Ancestry: (open — Human ancestry feat L5) |
| 6 | 15 | — | Class: Giant's Stature (grow to Large via instinct — synergy: Guisarme reach 15→ no change while already Large in Rage, but baseline Large outside Rage) • Skill: Quick Jump |
| 7 | 15 | **Juggernaut** (Expert Fort, success → crit success), **Weapon Specialization**, Sentinel auto-scale → Expert Heavy Armor | General: Sentinel Basic Maneuvers (or hold) |
| 8 | 15 | — | Class: Furious Bully (Athletics maneuvers add STR mod dmg) • Skill: Combat Climber |
| 9 | 15 | **Lightning Reflexes** (Expert Reflex), Raging Resistance increase | Ancestry: (open) |
| 10 | 15 | Ability Boost ×4 | Class: Improved Knockdown • Skill: Cloud Jump |
| 11 | 15 | **Mighty Rage** (Rage 2/day with bonus action, end rage at will) | General: Fleet (or hold) |
| 12 | 15 | — | Class: Come and Get Me • Skill: Battle Medicine (prior entry "Combat Grab" was illegal — Fighter-only class feat in a skill slot; Battle Medicine fits the build's Medicine +5 third-action pattern) |
| 13 | 15 | **Greater Juggernaut** (Master Fort), **Weapon Mastery**, **Medium Armor Expertise** | Ancestry: (open) |
| 14 | 15 | — | Class: Gigantic Stature (Huge — Guisarme reach 25 ft / Maul 20 ft) • Skill: Aerobatics Mastery |
| 15 | 15 | **Greater Weapon Specialization**, **Indomitable Will** (Master Will), Sentinel auto-scale → Master Heavy Armor, Ability Boost ×4 | General: Incredible Initiative |
| 16 | 15 | — | Class: Collateral Thrash • Skill: Sky Strider |
| 17 | 15 | **Quick Rage** (Rage as free action between encounters) | Ancestry: (open) |
| 18 | 15 | — | Class: Unstoppable Juggernaut • Skill: (open) |
| 19 | 15 | **Devastating Strike** (extra dmg on hit) | General: (open) |
| 20 | 15 | Ability Boost ×4 | Class: Rampage • Skill: (open) |

**Key progression (Guisarme):** Reach L1 15 ft (Large in Rage) → L6 baseline Large via Giant's Stature → L14 25 ft (Huge via Gigantic Stature) | Rage dmg L1 +6 → L7 +12 (Weapon Spec) → L15 +18 (GWS)
**Maul alternate:** Reach scales differently (10 ft → 15 ft → 20 ft) — trades 5 ft for 1d12 B + Shove + Backswing.
**Auto-level note:** STR+2 priority. Titan Wrestler (L3) + Guisarme Trip = grapple/prone chain at 15 ft from L3. Note: most "Sentinel scaling" claims depend on archetype rules version; verify against current Player Core 2 archetype text.

**Combat strategy — "The Zone":**
- Maintain 10–25 ft reach bubble; no enemy reaches the backline.
- Combo: **Strike** (huge dmg) → **Trip with Guisarme** (Athletics, Titan Wrestler covers up to Gargantuan) → **Step / Medicine** as third action.
- **Reactive Strike (mid+):** Use Guisarme reach to punish enemies standing from your Trip or moving within threat range.

---

## BUILD — FURY FLURRY BARBARIAN
**Human (Natural Ambition) | Barbarian (Fury Instinct) | Background: Warrior**
*Dual kukri flurry. Agile + deadly d8 crit machine. No instinct restrictions, Double Slice from L1.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 14 | 16 | 10 | 12 | 10 |
| Mod | +4 | +2 | +3 | +0 | +1 | +0 |

**HP** 23 | **AC** 18 (Hide Armor) | **Init** +6 | **Perc** +6 | **Speed** 25 ft
**Fort** +8 | **Ref** +5 | **Will** +4
**Weapon:** Kukri ×2 (1H S, 1d6+4, agile, deadly d8) | **Armor:** Hide Armor
**Skills:** Athletics +7, Intimidation +3 (Trained via Warrior bg), Acrobatics +5, Warfare Lore +3 (Trained via Warrior bg)
**Class Features:** Rage (Fury — no instinct restrictions, +2 damage), Deny Advantage, Raging Resistance
**Key Feats:** L1 Ancestry → Natural Ambition (grants Sudden Charge as bonus class feat) | L1 Class → Power Attack | L1 Skill (Warrior bg auto) → Intimidating Glare
**Boost Priority:** STR → CON → DEX → WIS
> **⚠️ FIX:** Original build listed "Double Slice" as L1 class feat — Double Slice is a Fighter class feat, illegal for Barbarian via Natural Ambition. Replaced with Power Attack (legal L1 Barb feat that works with dual kukris via repeat Strikes). "Two-Weapon Flurry" at L4 is also Fighter-only — removed.

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Natural Ambition | Secures Double Slice at L1 — without Natural Ambition this dual-kukri flurry loses its defining action economy from the start. |
| 2 | Orc | Hold-Scarred | Diehard critical for Fury Barbarian who dives into melee with no instinct damage reduction cushion; 28 HP buffers aggression. |
| 3 | Half-Orc | Orc Blood | Hold-Scarred via ancestry feat + Human-like stat flexibility covers DEX/STR spread this dual-weapon build needs. |
| 4 | Catfolk | Nimble | +5 ft speed to 30 ft patches the mobility gap when flanking with dual kukris requires closing from range. |
| 5 | Halfling | Gutsy | Immunity to Frightened crit-fail keeps Fury Barbarian functional against mass fear effects that would break the flurry rotation. |
| 6 | Goblin | Unbreakable | +4 max HP offsets CON 16 (vs 18 in Giant build) — Fury Barbarian has lower HP floor, so every point matters. |
| 7 | Dwarf | Unburdened Iron | No Speed penalty in heavy armor; less critical here but opens Scale Mail option if DEX investment drops mid-campaign. |
| 8 | Tengu | Dogtooth | Natural bite adds a cheap third attack at MAP-5 during raging flurry when kukri MAP-10 makes the third kukri strike near-useless. |
| 9 | Lizardfolk | Frilled | Intimidation synergy complements Raging Intimidation feats if player pivots to a fear-support Fury variant. |
| 10 | Tiefling | Grimspawn | Deception/Intimidation bonuses + void resist 5 provide soft utility when the build outgrows pure STR flurry around L8+. |

**LEVELING MAP — FURY FLURRY BARBARIAN**
HP per level: 12 + Con mod (+3) = **15 HP/level**

| Lvl | HP | Auto Features (class progression) | [PICK] Feat slots |
|-----|----|-----------------------------------|--------------------|
| 1 | 23 | Rage (Fury, +2 damage, no restrictions), Deny Advantage, Raging Resistance | Class: Power Attack • +Sudden Charge (Natural Ambition bonus) • Skill (bg auto): Intimidating Glare |
| 2 | 15 | — | Class: Raging Intimidation • Skill: Assurance (Athletics) |
| 3 | 15 | **Furious Footfalls** (+5 Speed in light/no armor — applies here, Hide is medium so check ruling) | General: Toughness |
| 4 | 15 | — | Class: Swipe (hit two adjacent enemies, one Strike roll, dual-kukri MAP-aware) • Skill: Cat Fall |
| 5 | 15 | **Brutal Critical**, Ability Boost (STR/CON+2) | Ancestry: (open Human ancestry feat) |
| 6 | 15 | — | Class: Furious Bully • Skill: Combat Climber |
| 7 | 15 | **Juggernaut** (Expert Fort, success→crit), **Weapon Specialization** | General: Fleet |
| 8 | 15 | — | Class: Knockback (or Improved Knockdown) • Skill: Quick Jump |
| 9 | 15 | **Lightning Reflexes** (Expert Ref) | Ancestry: (open) |
| 10 | 15 | Ability Boost ×4 | Class: Improved Knockdown • Skill: Powerful Leap |
| 11 | 15 | **Mighty Rage** | General: Incredible Initiative |
| 12 | 15 | — | Class: Come and Get Me • Skill: (open) |
| 13 | 15 | **Greater Juggernaut** (Master Fort), **Weapon Mastery** | Ancestry: (open) |
| 14 | 15 | — | Class: Furious Sprint • Skill: (open) |
| 15 | 15 | **Greater Weapon Specialization**, **Indomitable Will** (Master Will), Ability Boost ×4 | General: (open) |
| 16 | 15 | — | Class: Collateral Thrash • Skill: (open) |
| 17 | 15 | **Quick Rage** | Ancestry: (open) |
| 18 | 15 | — | Class: Brutal Bully (was L6 earlier; legal at any later level) • Skill: (open) |
| 19 | 15 | **Devastating Strike**, **Armor of Will** | General: (open) |
| 20 | 15 | Ability Boost ×4 | Class: Rampage • Skill: (open) |

**Key progression:** Rage dmg L1 +2 → L7 +4 (Weapon Spec adds +2 with martial) → L15 +6 (Greater Weapon Spec) | Deadly d8 on crit | Power Attack adds extra die per Strike
**Auto-level note:** STR+2 first. With dual kukris MAP runs −0/−4/−8 (agile). Strike→Strike→Sudden Charge or Power Attack→Strike are the standard rotations.

---

## BUILD — ANIMAL INSTINCT MUTAGEN BARBARIAN
**Orc (Hold-Scarred) | Barbarian (Animal Instinct) | Background: Herbalist**
*Natural attacks + Alchemist Dedication for Bestial Mutagen free 3/day. Agile claws flurry, best natural attack build.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 16 | 18 | 14 | 12 | 8 |
| Mod | +4 | +3 | +4 | +2 | +1 | -1 |

**HP** 26 | **AC** 18 (Hide Armor) | **Init** +7 | **Perc** +7 | **Speed** 25 ft
**Fort** +9 | **Ref** +6 | **Will** +5
**Weapon:** Claws (1d6+4, agile) + Jaws (1d8+4) while raging | **Armor:** Hide Armor
**Skills:** Athletics +7, Crafting +5, Survival +4 (Trained via Herbalist bg), Nature +4 (Trained via Herbalist bg)
**Class Features:** Rage (Animal — claws 1d6 agile + jaws 1d8, +2 dmg, nat armor +1), Deny Advantage, Raging Resistance (physical)
**Key Feats:** L1 Heritage: Hold-Scarred (grants Diehard) | L1 Ancestry: Iron Fists (or similar Orc L1) | L1 Class: Animal Skin (Animal Instinct feature) | L1 Skill (Herbalist bg auto): Natural Medicine | L2 Class: Alchemist Dedication (Bestial Mutagen access)
> See **KM_BuildAudit_Barbarian.md** for leveling-map corrections (Juggernaut L7 not L3, Master Fort → L13 Greater Juggernaut, GWS auto L15, "Apex Predator" needs verify).
**Boost Priority:** STR → CON → DEX → INT

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Natural Ambition | Grabs Alchemist Dedication one level earlier than Orc can — but loses 4 HP; best if you want Mutagen online ASAP. |
| 2 | Orc | Hold-Scarred | Diehard + 28 HP is ideal for a build that trades armor for nat armor and depends on regen from rage TempHP each round. |
| 3 | Catfolk | Clawed | Natural claws stack with Animal Instinct claws debate — even without stacking, Catfolk's +5 ft speed and Cat's Luck help agile claw flurry. |
| 4 | Half-Orc | Orc Blood | Hold-Scarred access + Human ancestry feat flexibility covers INT 14 Alchemist Dedication prereq without sacrificing CON. |
| 5 | Elf | Ancient Elf | Free MCdedication at L1 is uniquely powerful here — grabs Alchemist Dedication before the standard L2 slot, freeing L2 for another option. |
| 6 | Tengu | Dogtooth | Natural bite at 1d6+4 adds a second natural attack type alongside Animal Instinct jaws for a three-natural-attack rotation. |
| 7 | Goblin | Unbreakable | +4 max HP compensates for the nat-armor-only defense; Goblin Scuttle frees an action after flanking to avoid AoO repositioning. |
| 8 | Halfling | Hillock | Extra HP per rest is valuable for this no-shield, no-heavy-armor build that absorbs hits on a lower AC floor. |
| 9 | Lizardfolk | Cliffscale | Climb speed from Cliffscale Heritage complements Animal Instinct's nature-predator identity and opens vertical terrain options. |
| 10 | Leshy | Vine | Athletics bonus pairs well with the Titan Wrestler chain this build keeps as a secondary grapple option mid-levels. |

**LEVELING MAP — ANIMAL INSTINCT MUTAGEN BARBARIAN**
HP per level: 12 + Con mod (+4) = **16 HP/level**

| Lvl | HP | Auto Features (class progression) | [PICK] Feat slots |
|-----|----|-----------------------------------|--------------------|
| 1 | 26 | Rage (Animal — claws 1d6 agile + jaws 1d8, +2 dmg, nat armor +1), Deny Advantage, Raging Resistance (physical) | Class: Animal Skin (Animal Instinct feat) • Ancestry: Iron Fists (or open Orc L1) • Heritage: Hold-Scarred (Diehard) • Skill (bg auto): Natural Medicine |
| 2 | 16 | — | Class: Alchemist Dedication (Bestial Mutagen access, INT 14 prereq met) • Skill: Crafting Assurance |
| 3 | 16 | **Furious Footfalls** | General: Toughness |
| 4 | 16 | — | Class: Swipe • Skill: (open) |
| 5 | 16 | **Brutal Critical**, Ability Boost ×4 | Ancestry: (open Orc) |
| 6 | 16 | — | Class: Furious Bully (canon L6) • Skill: (open) |
| 7 | 16 | **Juggernaut**, **Weapon Specialization** | General: (open) |
| 8 | 16 | — | Class: Predator's Pounce (canon L8) • Skill: (open) |
| 9 | 16 | **Lightning Reflexes** | Ancestry: (open) |
| 10 | 16 | Ability Boost ×4 | Class: Brutal Bully (canon L6 — legal at L10) • Skill: (open) |
| 11 | 16 | **Mighty Rage** | General: (open) |
| 12 | 16 | — | Class: Come and Get Me • Skill: (open) |
| 13 | 16 | **Greater Juggernaut**, **Weapon Mastery** | Ancestry: (open) |
| 14 | 16 | — | Class: Vicious Evisceration (canon L14 — bleed on crit) • Skill: (open) |
| 15 | 16 | **Greater Weapon Spec**, **Indomitable Will**, Ability Boost ×4 | General: (open) |
| 16 | 16 | — | Class: Collateral Thrash • Skill: (open) |
| 17 | 16 | **Quick Rage** | Ancestry: (open) |
| 18 | 16 | — | Class: Unstoppable Juggernaut • Skill: (open) |
| 19 | 16 | **Devastating Strike**, **Armor of Will** | General: (open) |
| 20 | 16 | Ability Boost ×4 | Class: Rampage • Skill: (open) |

**Key progression:** Claws/Jaws auto-scale via Animal Instinct Specialization Ability (Player Core canon: L7 Spec, L15 Greater Spec). Bestial Mutagen from L2 archetype = +2 atk/dmg lesser variant, scales per Alchemist archetype rules. "Greater Animalistic Attacks" / "Apex Predator" from original were not canonical — replaced with valid class progression.
**Auto-level note:** STR+2 first. INT 14 meets Alchemist Ded. prereq. HP corrected to 26 (10 Orc + 12 Barb + 4 CON = 26, not 28).

---

> **➡️ Builds 4 (Spirit Instinct), 5 (Dragon Instinct), 6 (Superstition): see `KM_Builds_B5.md`**

<!-- BUILDS 4-6 MOVED TO KM_Builds_B5.md (v2.0 split, 2026-05-14) -->

*Builds 4, 5, 6 relocated to **KM_Builds_B5.md** with full leveling-map corrections applied.*

---

> **➡️ Barbarian builds 7–10: see `KM_Builds_B2.md`**
> **➡️ Bard builds 1–5: see `KM_Builds_B4.md`**

*KM_Builds_B.md — Kingmaker PF2e Text Adventure | Builds: Barbarian (1–3) v3.0 | 2026-05-14 split*
