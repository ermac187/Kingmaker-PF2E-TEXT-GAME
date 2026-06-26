# KINGMAKER — BUILDS: FIGHTER
## KM_Builds_E2.md | Referenced by: KM_BuildScreen.md, KM_Builds_E.md

> **DM:** Load this file for Fighter builds 1–6. Builds 7–10 are in KM_Builds_E4.md.
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
# FIGHTER (builds 1–6)
# ══════════════════════════════════════

## BUILD — TWO-HANDED STRIKER FIGHTER
**Human (Versatile Heritage) | Fighter (Two-Handed) | Background: Warrior**
*Power Attack + Exacting Strike — high-damage two-handed nova, MAP managed by Exacting Strike miss-recovery.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 14 | 14 | 10 | 12 | 10 |
| Mod | +4 | +2 | +2 | +0 | +1 | +0 |

**HP** 20 | **AC** 18 (Scale Mail) | **Fort** +6 | **Ref** +6 | **Will** +5 | **Speed** 25 ft
**Weapon:** Greatsword (2H S, 1d12+4, Versatile P) | **Armor:** Scale Mail
**Skills:** Athletics +6, Intimidation +3, Warfare Lore +2, Survival +4
**Features:** Attack of Opportunity, Expert martial L1
**L1 Feats:** Natural Ambition + Power Attack | **Boost:** STR → CON → DEX → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Orc | Hold-Scarred | STR 18 base is already maxed; Hold-Scarred's Diehard keeps this high-damage nova build alive through Power Attack crit-fishing rounds where adjacent enemies retaliate hard. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition grabs both Power Attack and a positioning feat at L1, front-loading the two-handed nova combo a full level ahead of schedule. |
| 3 | Dwarf | Dwarven Weapon Familiarity | Dwarven Waraxe (d10 + Forceful + Sweep) out-damages the Greatsword on multi-target swings; Familiarity makes it a martial weapon for Fighter's expert proficiency. |
| 4 | Half-Orc | Hold-Scarred | Orc Blood accesses Hold-Scarred while Human stat flexibility preserves STR 18 + CON 14, hitting the same nova ceiling without sacrificing survivability. |
| 5 | Lizardfolk | Frilled | Frilled's Intimidation demoralize syncs with Intimidating Strike L3 — a Frightened 1 debuff on the Power Attack target turns already-high damage into reliably hitting through AC. |
| 6 | Tiefling | Pitborn | Pitborn grants Athletics bonus and fire resist 5 plus a STR-boosting path — fire resist 5 is the most common AoE damage type facing a front-line melee nova build. |
| 7 | Goblin | Unbreakable | Unbreakable +4 max HP offsets the Goblin's lower base — a two-handed Fighter that swings first and hard can afford to eat one hit in return. |
| 8 | Half-Elf | Elf Atavism | Elf Atavism's Ancient Elf gives a free dedication — Champion for shield or Barbarian for Rage extra damage stacks on Power Attack's doubled dice. |
| 9 | Halfling | Halfling Luck | Halfling Luck rerolls a Power Attack attack roll that missed once per day — with 2× damage dice on the line, that reroll is worth more than any passive bonus. |
| 10 | Catfolk | Clawed | Clawed natural claw acts as a free off-hand for a Trip or Grapple attempt after a Power Attack, extending the two-handed striker into light control at no weapon cost. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Attack of Opportunity, Expert martial | Natural Ambition + Power Attack (2× damage dice) |
| 2 | 12 | — | Exacting Strike |
| 3 | 12 | Bravery | Toughness (+max HP per level — L3 is a General feat slot, not class feat) |
| 4 | 12 | — | Knockdown (Trip on hit) |
| 5 | 12 | Ability Boost (STR/CON+2), Weapon Master | Weapon Specialization + Brutal Finish |
| 6 | 12 | — | Shatter Defenses |
| 7 | 12 | — | Whirlwind Strike |
| 8 | 12 | — | Improved Knockdown |
| 9 | 12 | Combat Flexibility, Master Will | Devastator (ignore resistances) |
| 10 | 12 | Ability Boost | Greater Weapon Specialization |
| 11 | 12 | — | Overwhelming Blow |
| 12 | 12 | — | Weapon Surge |
| 13 | 12 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 12 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 12 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 12 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** STR+2 first. Power Attack (L1) + Exacting Strike (L2) — if Exacting Strike misses it doesn't increment MAP, so Power Attack follows at MAP 0 or −5 instead of −10.

---

## BUILD — GREAT PICK FATAL CRIT FIGHTER
**Human (Versatile Heritage) | Fighter (Two-Handed) | Background: Gladiator**
*Fatal d12 crit engine + debuff chain — Intimidating Strike → Shatter Defenses converts every landed hit into flat-footed, maximizing the Fatal damage multiplier.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 14 | 14 | 10 | 12 | 10 |
| Mod | +4 | +2 | +2 | +0 | +1 | +0 |

**HP** 20 | **AC** 18 (Scale Mail) | **Fort** +6 | **Ref** +6 | **Will** +5 | **Speed** 25 ft
**Weapon:** Greatpick (2H P, 1d10+4, Fatal d12) | **Armor:** Scale Mail
**Skills:** Athletics +6, Intimidation +3, Warfare Lore +2, Survival +3
**Features:** Attack of Opportunity, Expert martial L1
**L1 Feats:** Natural Ambition + Power Attack | **Boost:** STR → CON → DEX → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Orc | Hold-Scarred | Fatal d12 crits invite immediate counter-retaliation; Hold-Scarred keeps the crit engine running through the first enemy counter-swing without a trip to dying 2. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition takes Power Attack AND Exacting Strike at L1 — both pieces of the miss-recovery chain are online before session one, no delaying to L2. |
| 3 | Lizardfolk | Frilled | Frilled Heritage Demoralize + Intimidating Strike stacks Frightened faster than any other ancestry; Shatter Defenses converts every Frightened 1 into flat-footed, directly raising Fatal d12 crit chances. |
| 4 | Half-Orc | Hold-Scarred | Orc Blood gives Diehard while Human stat flexibility keeps STR 18 + CON 14 — same crit-engine survivability as a pure Orc without sacrificing the secondary defensive stat. |
| 5 | Dwarf | Mountain's Stoutness | Mountain's Stoutness adds +1 HP/level — a Great Pick Fighter deliberately eats AoOs every round while swinging, so compounding HP is more valuable than any one-time defensive trait. |
| 6 | Tiefling | Pitborn | Free Athletics training sharpens Knockdown trip DCs; prone from Knockdown stacks with flat-footed from Shatter Defenses on the same target, producing back-to-back crit-range turns. |
| 7 | Halfling | Halfling Luck | 1/day reroll on any failed check; a missed Power Attack on a Fatal d12 build costs more DPR than almost any other class — that reroll turns the worst turn into a normal one. |
| 8 | Half-Elf | Elf Atavism | Elf Atavism's Ancient Elf option gives a free dedication at L1 — Champion's Retributive Strike or Exemplar's Ikon stacks a second damage source on top of every Fatal crit turn. |
| 9 | Catfolk | Nimble | 35 ft base speed executes Stride → Knockdown → Follow-up Strike in 3 actions without burning an action just to reach targets that retreated after being knocked prone. |
| 10 | Goblin | Unbreakable | +4 max HP patches the CON 14 durability floor on a fighter that never backs away from melee contact and draws full enemy action economy each round. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Attack of Opportunity, Expert martial | Natural Ambition + Power Attack (2× damage dice) |
| 2 | 12 | — | Exacting Strike (no MAP on second Strike if first misses) |
| 3 | 12 | Bravery | Toughness (+max HP per level) |
| 4 | 12 | — | Knockdown (Trip on hit → prone → flat-footed) |
| 5 | 12 | Ability Boost (STR/CON+2), Weapon Master | Weapon Specialization + Intimidating Strike (Strike + Frighten 1) |
| 6 | 12 | — | Shatter Defenses (flat-footed vs Frightened — crit chain online) |
| 7 | 12 | — | Whirlwind Strike (AoE Fatal crits vs clustered flat-footed enemies) |
| 8 | 12 | — | Improved Knockdown (free Trip on any Strike hit) |
| 9 | 12 | Combat Flexibility, Master Will | Devastator (ignore resistances) |
| 10 | 12 | Ability Boost | Greater Weapon Specialization |
| 11 | 12 | — | Overwhelming Blow |
| 12 | 12 | — | Weapon Surge |
| 13 | 12 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 12 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 12 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 12 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** STR+2 first. Intimidating Strike (L5) → Shatter Defenses (L6) is the core damage multiplier. Every turn: Intimidating Strike to apply Frightened, all subsequent Strikes land on a flat-footed target. Fatal d12 crit on a flat-footed enemy is maximum DPR output.

---

## BUILD — AGILE DUAL WIELD FIGHTER
**Human (Versatile Heritage) | Fighter (Dual-Weapon) | Background: Warrior**
*Twin Takedown + Agile Grace — maximum attack volume, MAP −3/−6 means third Strike lands on 14+.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 14 | 18 | 14 | 10 | 12 | 10 |
| Mod | +2 | +4 | +2 | +0 | +1 | +0 |

**HP** 20 | **AC** 18 (Breastplate) | **Fort** +6 | **Ref** +8 | **Will** +5 | **Speed** 25 ft
**Weapon:** Shortsword × 2 (1H P, 1d6+2, agile, finesse, versatile S) | **Armor:** Breastplate
**Skills:** Athletics +4, Acrobatics +6, Intimidation +2, Warfare Lore +2
**Features:** Attack of Opportunity, Expert martial L1
**L1 Feats:** Natural Ambition + Double Slice | **Boost:** DEX → STR → CON → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Versatile (Natural Ambition) | Natural Ambition locks in both Double Slice AND Agile Grace at L1 — MAP −3/−6 is active from session one, not L3, so Twin Takedown's third Strike lands on 14+ before the campaign starts. |
| 2 | Elf | Nimble Elf | 35 ft speed means one Stride + Twin Takedown in 3 actions on most turns; at base 25 ft, a second Stride to chase backline targets eats both attack actions and kills the turn. |
| 3 | Catfolk | Nimble | Same 35 ft as Elf at 8 base HP instead of 6 — identical movement advantage with a 2 HP/level durability premium for a build that takes melee retaliation every round. |
| 4 | Half-Elf | Elf Atavism | Elf Atavism unlocks Elven Accuracy, which rerolls all 1s on DEX 18 finesse Strikes — three attacks per Twin Takedown + bite cycle gives three reroll chances per turn, the highest volume upside of any heritage. |
| 5 | Tengu | Dogtooth | Dogtooth bite is agile; after Twin Takedown (2 Strikes, 2 actions), the bite fires as a third hit at only MAP −3 via Agile Grace — three attacks for 2 action investment, none penalized above −3. |
| 6 | Halfling | Halfling Luck | Twin Takedown commits 2 actions to two Strikes; a rerolled miss 1/day turns a half-wasted turn back into full attack output, worth more than any static bonus at DEX 18. |
| 7 | Goblin | Unbreakable | +4 max HP from Unbreakable patches the DEX 18 / CON 14 durability gap — this build deliberately stands between two enemies to maximize attack access and will eat double melee retaliation until one drops. |
| 8 | Fetchling | Liminal | Shadow Step 1/day repositions when Stride alone can't close both gaps — preserves the 2 attack actions for Twin Takedown on a turn that would otherwise spend 2 actions just reaching targets. |
| 9 | Half-Orc | Hold-Scarred | Diehard from Hold-Scarred lets you survive to dying 5 instead of dying 4 — a Fighter that stands between two melee enemies every turn by design will drop eventually, and one extra wound threshold wins fights. |
| 10 | Gnome | Wellspring | Wellspring grants an extra innate cantrip — on turns where two Strides are needed to reach melee range, the remaining action fires the cantrip instead of ending empty-handed. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Attack of Opportunity, Expert martial | Natural Ambition + Double Slice |
| 2 | 12 | — | Twin Parry (+1 AC while dual-wielding) |
| 3 | 12 | Bravery | Agile Grace (MAP −4/−8 → −3/−6) |
| 4 | 12 | — | Twin Riposte |
| 5 | 12 | Ability Boost (DEX/STR+2), Weapon Master | Weapon Specialization + Twin Takedown |
| 6 | 12 | — | Shatter Defenses |
| 7 | 12 | — | Flensing Slice (persistent bleed on crit) |
| 8 | 12 | — | Improved Twin Riposte |
| 9 | 12 | Combat Flexibility, Master Will | Devastating Strike |
| 10 | 12 | Ability Boost | Greater Weapon Specialization |
| 11 | 12 | — | Dual-Weapon Blitz (3 attacks, 2 actions) |
| 12 | 12 | — | Weapon Surge |
| 13 | 12 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 12 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 12 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 12 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** DEX+2 first. Twin Takedown at L5 — 2 full Strikes in 2 actions, mandatory for action economy.

---

## BUILD — SHIELD BASTION FIGHTER
**Human (Versatile Heritage) | Fighter (Shield) + Bastion Dedication | Background: Guard**
*Shield Block + Bastion — Reactive Shield before Quick Shield Block arrives, chain makes you near-unkillable.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 16 | 14 | 16 | 10 | 14 | 10 |
| Mod | +3 | +2 | +3 | +0 | +2 | +0 |

**HP** 21 | **AC** 18 (Scale Mail) | **Fort** +7 | **Ref** +6 | **Will** +6 | **Speed** 25 ft
**Weapon:** Longsword (1H S, 1d8+3, versatile P) + Steel Shield | **Armor:** Scale Mail
**Skills:** Athletics +5, Intimidation +3, Perception +6, Warfare Lore +2
**Features:** Attack of Opportunity, Expert martial L1, Shield Block
**L1 Feats:** Natural Ambition + Shield Block | **Boost:** CON → STR → WIS → DEX

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Dwarf | Unburdened Iron | Unburdened Iron removes the Full Plate speed penalty entirely — this Shield Tank can upgrade to Full Plate at no Speed cost, reaching 25 ft with the best AC in the game. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition grabs Shield Block and Bastion Dedication access at L1, establishing the block-reaction chain one level earlier than any other ancestry. |
| 3 | Orc | Hold-Scarred | CON 16 and Hold-Scarred means this tank requires three knockdowns to stay dead — perfect for the build that exists to absorb every hit the party avoids. |
| 4 | Half-Orc | Hold-Scarred | Orc Blood + Unburdened Iron (via Dwarf heritage feat) isn't available, but Hold-Scarred alone on a STR 16/CON 16 base is top-tier tank synergy. |
| 5 | Goblin | Unbreakable | Unbreakable +4 max HP stacks with CON 16's 13 HP/level — a shield tank that never drops means Quick Shield Block L6 is always available to defend an ally. |
| 6 | Lizardfolk | Frilled | Frilled Lizardfolk lets a shield-wielder Demoralize as a reaction to being struck — enemies wasting turns on a -1 to-hit from Frightened reduces incoming damage further. |
| 7 | Half-Elf | Elf Atavism | Elf Atavism's Ancient Elf dedication opens Champion — the tank adds Lay on Hands to the shield chain, making nearby party members nearly as hard to kill as itself. |
| 8 | Halfling | Hillock | Hillock restores extra HP per rest on a CON 16 build, which maximizes the sleep-healing coefficient — the best short-rest HP recovery option for a frontline tank. |
| 9 | Tiefling | Grimspawn | Grimspawn void resist 5 and free social ancestry feats make the shield tank also the party's face — CHA 10 is low but Grimspawn Intimidation ancestry feats work off CON. |
| 10 | Catfolk | Clawed | Clawed gives a free off-hand natural weapon for a Trip or Grapple attempt after a shield bash, adding control utility without sacrificing the shield in hand. |

**Leveling — 13 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 21 | Attack of Opportunity, Expert martial | Natural Ambition + Shield Block |
| 2 | 13 | — | Bastion Dedication (Reactive Shield reaction) |
| 3 | 13 | Bravery | Aggressive Block (push/trip on block) |
| 4 | 13 | — | Shield Warden (share Shield Block with adjacent ally) |
| 5 | 13 | Ability Boost (CON/STR+2), Weapon Master | Weapon Specialization + Knockdown |
| 6 | 13 | — | Quick Shield Block (extra block reaction/round) |
| 7 | 13 | — | Disruptive Stance |
| 8 | 13 | — | Improved Knockdown |
| 9 | 13 | Combat Flexibility, Master Will | Devastating Strike |
| 10 | 13 | Ability Boost | Greater Weapon Specialization |
| 11 | 13 | — | Fortress Shield (harden shield free action) |
| 12 | 13 | — | Weapon Surge |
| 13 | 13 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 13 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 13 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 13 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** CON+2 first. Bastion Dedication at L2 — Reactive Shield establishes block chain before Quick Shield Block.

---

## BUILD — POLEARM MASTER
**Human (Skilled Heritage) | Fighter (Reach Specialist) | Background: Warrior**
*Guisarme reach + Reactive Strike + Knockdown — every enemy entering the 10 ft zone triggers a free Trip. Combat Reflexes adds a second reaction per round. Whirlwind Strike clears clustered groups.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 14 | 14 | 12 | 12 | 10 |
| Mod | +4 | +2 | +2 | +1 | +1 | +0 |

**HP** 20 | **AC** 18 (Chain Mail) | **Fort** +6 | **Ref** +6 | **Will** +5 | **Speed** 25 ft
**Weapon:** Guisarme (2H S, 1d10+4, reach 10 ft, trip, forceful) | **Armor:** Chain Mail
**Skills:** Athletics +6, Perception +5, Warfare Lore +3, Survival +3
**Features:** Reactive Strike, Expert martial L1
**L1 Feats:** Skilled (heritage, auto) Heritage + Knockdown | **Boost:** STR → CON → DEX → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Skilled | Extra trained skill fills the narrow skill spread; Reactive Strike + Knockdown + Guisarme reach punishes every enemy who enters the 10 ft threat zone from session one. |
| 2 | Orc | Hold-Scarred | STR 18 + Diehard keeps a reach-control Fighter who baits all enemies into the threat zone alive through multi-front retaliation every round. |
| 3 | Half-Orc | Orc Blood | Hold-Scarred via feat + Human flexibility; STR 18 + CON 14 preserved with no stat loss, adding Diehard for the frontline zone-controller who never retreats. |
| 4 | Dwarf | Unburdened Iron | Removes Chain Mail speed penalty entirely — reach Fighter at full 30 ft speed controls the 10 ft threat zone while repositioning to intercept multiple approach vectors. |
| 5 | Lizardfolk | Frilled | Intimidation bonus reinforces Demoralize after a Knockdown — a prone + Frightened enemy in reach takes both penalties on their escape attempt roll. |
| 6 | Tiefling | Pitborn | Athletics + STR 18 synergy; Pitborn bonus improves Knockdown and Shove DCs, making the zone-control web harder to escape via Athletics-resisted maneuvers. |
| 7 | Halfling | Gutsy | Will +5 is already solid; Gutsy's crit-fail Frightened immunity ensures Combat Reflexes reactions always fire — a scared zone-controller who can't react loses everything. |
| 8 | Half-Elf | Elf Atavism | Ancient Elf path gets a free dedication at L1; Sentinel Dedication moves this build to Master armor proficiency one full tier sooner. |
| 9 | Goblin | Unbreakable | +4 max HP raises the L1 floor to 24, compensating for Chain Mail's lower DEX cap vs Scale Mail builds. |
| 10 | Catfolk | Nimble | +5 ft speed offsets Chain Mail penalty — 30 ft full speed widens the Guisarme zone from a static 10 ft ring to a dynamic 20 ft threat area during Stride turns. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Reactive Strike, Expert martial | Skilled Heritage + Knockdown (free Trip on any successful hit) |
| 2 | 12 | — | Powerful Shove (push target 5 ft on any successful melee Strike) |
| 3 | 12 | Bravery | Toughness |
| 4 | 12 | — | Lunging Stance (extend Guisarme reach to 15 ft for one Strike) |
| 5 | 12 | Ability Boost (STR/CON+2), Weapon Master | Weapon Specialization + Combat Reflexes (extra Reactive Strike reaction per round) |
| 6 | 12 | — | Improved Knockdown (Trip applies to all hits, not just first each round) |
| 7 | 12 | — | Disruptive Stance |
| 8 | 12 | — | Whirlwind Strike (Strike all creatures in reach simultaneously) |
| 9 | 12 | Combat Flexibility, Master Will | Devastator |
| 10 | 12 | Ability Boost | Greater Weapon Specialization |
| 11 | 12 | — | Overwhelming Blow |
| 12 | 12 | — | Weapon Surge |
| 13 | 12 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 12 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 12 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 12 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** STR+2 first. Knockdown at L1 — every Reactive Strike and hit trips the target, turning the 10 ft zone into a prone trap. Combat Reflexes at L5 doubles reaction output.

---

## BUILD — RAPIER FINESSE FIGHTER
**Human (Versatile Heritage) | Fighter (Dual-Weapon) | Background: Warrior**
*Double Slice + Rapier deadly d8 — finesse dual-wield with Twin Takedown multi-target at L5 and crit-fishing via Rapier's deadly die.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 16 | 18 | 14 | 10 | 12 | 10 |
| Mod | +3 | +4 | +2 | +0 | +1 | +0 |

**HP** 20 | **AC** 18 (Breastplate) | **Fort** +6 | **Ref** +8 | **Will** +5 | **Speed** 25 ft
**Weapon:** Rapier (1H P, 1d6+3, agile, deadly d8, finesse) + Shortsword (1H P, 1d6+3, agile, finesse) | **Armor:** Breastplate
**Skills:** Athletics +5, Acrobatics +6, Intimidation +3, Warfare Lore +2
**Features:** Attack of Opportunity, Expert martial L1, Double Slice
**L1 Feats:** Natural Ambition + Double Slice | **Boost:** DEX → STR → CON → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Versatile (Natural Ambition) | Natural Ambition grabs Double Slice and Agile Grace at L1 — the MAP −3/−6 reduction means both Rapier + Shortsword hits land reliably before Agile Grace is normally available at L3. |
| 2 | Elf | Nimble Elf | Nimble Elf's 35 ft speed lets this Rapier + Shortsword Fighter reach two separated enemies in one Stride, making Twin Takedown's two-target Strike achievable almost every turn. |
| 3 | Catfolk | Nimble | Nimble Catfolk hits 35 ft at 8 base HP instead of Elf's 6, a straight upgrade when the speed threshold is all that matters for Twin Takedown target access. |
| 4 | Half-Elf | Elf Atavism | Elf Atavism (Ancient Elf) opens Swashbuckler Dedication for free at L1 — Panache adds +2 to both Double Slice hits while style is active, boosting the Rapier's deadly d8 crit threshold. |
| 5 | Tengu | Dogtooth | Dogtooth bite provides a third natural strike that doesn't share a MAP category with Rapier + Shortsword, functioning as a free third hit after Double Slice when an adjacent target remains. |
| 6 | Halfling | Halfling Luck | Halfling Luck rerolls a failed Double Slice or Twin Takedown attack 1/day — the build commits 2 actions to Twin Takedown at L5+, making a miss on either target costly. |
| 7 | Goblin | Unbreakable | Unbreakable +4 max HP gives a DEX-primary Breastplate wearer the same HP cushion as a CON-primary build, covering the main weakness of this finesse-first choice. |
| 8 | Fetchling | Liminal | Shadow Step repositions between two clustered enemies 1/day when Stride alone can't close both gaps, ensuring Twin Takedown's 2-target requirement is always satisfiable. |
| 9 | Half-Orc | Hold-Scarred | Hold-Scarred protects a DEX 18/STR 16 melee build that stands between two targets every turn from the inevitable double-retaliation those adjacent enemies make. |
| 10 | Gnome | Obsessive | Obsessive's +2 Lore pairs with STR 16 to cover an off-turn skill action when Dual Slice's targets are dead — the build has dead rounds between fights that benefit from skilled utility. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Attack of Opportunity, Expert martial | Natural Ambition + Double Slice (both weapons, 1 action) |
| 2 | 12 | — | Twin Parry |
| 3 | 12 | Bravery | Agile Grace (MAP −4/−8 → −3/−6) |
| 4 | 12 | — | Twin Riposte |
| 5 | 12 | Ability Boost (DEX/STR+2), Weapon Master | Weapon Specialization + Twin Takedown |
| 6 | 12 | — | Shatter Defenses |
| 7 | 12 | — | Flensing Slice |
| 8 | 12 | — | Improved Twin Riposte |
| 9 | 12 | Combat Flexibility, Master Will | Devastating Strike |
| 10 | 12 | Ability Boost | Greater Weapon Specialization |
| 11 | 12 | — | Dual-Weapon Blitz |
| 12 | 12 | — | Weapon Surge |
| 13 | 12 | Weapon Legend | Boundless Reprisals |
| 14 | — | — | — |
| 15 | 12 | Ability Boost, Greater Bravery | Twinned Defense |
| 16 | — | — | — |
| 17 | 12 | — | Savage Critical |
| 18 | — | — | — |
| 19 | — | — | — |
| 20 | 12 | Ability Boost | Weapon Legend capstone |

**Auto-level note:** DEX+2 first. Twin Takedown at L5 — 2-action Strike against two different targets; Rapier's deadly d8 fires on every crit from L1.

---

> **➡️ Fighter builds 7–10: see `KM_Builds_E4.md`**
> **➡️ Full class index: see `KM_BuildScreen.md`**

*KM_Builds_E2.md — Kingmaker PF2e Text Adventure | Fighter Builds 1–6 v2.0*
