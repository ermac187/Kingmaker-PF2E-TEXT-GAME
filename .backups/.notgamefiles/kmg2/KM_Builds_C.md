# KINGMAKER — BUILDS: CHAMPION (1–6)
## KM_Builds_C.md | Referenced by: KM_BuildScreen.md, KM_Companions_Builds.md

> **DM:** Load this file when player or companion selects any Champion build (1–6). Cleric: KM_Builds_C4.md.
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
# CHAMPION
# ══════════════════════════════════════

## BUILD — RADIANT REACH CHAMPION
**Human (Versatile Heritage) | Champion (Paladin) | Background: Warrior**
*Reach tank / force multiplier / reaction DPS. Guisarme (reach + trip) lets the Paladin sit in the second rank and still punish anyone who hits the frontline. Retributive Strike feeds the Maestro Bard's accuracy buffs; Weight of Guilt enfeebles on reaction; Divine Wall later turns the threat zone into difficult terrain so enemies eat Reactive Strikes from the Fighter and Barbarian when they try to leave. Designed for a 7-player team with a Reach Fighter (Knockdown), a Giant Barbarian, and a Maestro Bard — the Paladin is the layered second-rank threat that converts ally reactions into a Reach Wall.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 10 | 16 | 10 | 12 | 16 |
| Mod | +4 | +0 | +3 | +0 | +1 | +3 |

**HP** 21 | **AC** 19 (Full Plate, Bulwark) | **Init** +1 | **Perc** +4 | **Speed** 25 ft
**Fort** +8 | **Ref** +5 (Bulwark vs Reflex DC) | **Will** +6
**Weapon:** Guisarme (2H S, 1d10+4, **Reach**, **Trip**) | **Shield:** Steel Shield strapped to off-arm (for Shield of Reckoning at L10 — wielded only when reaction fires) | **Armor:** Full Plate (Bulwark)
**Skills:** Athletics +6, Religion +3, Intimidation +5, Warfare Lore +2
**Focus Spells:** Lay on Hands (1d6+CHA heal), Litany Against Wrath (later)
**Class Features:** Retributive Strike (reaction: ally damaged within **15 ft** → Strike + 2 damage to attacker — at reach 10 ft this covers an enormous threat zone), Shield Block, Divine Ally
**Key Feats:** L1 Natural Ambition + **Ranged Reprisal** (Step into reach OR fire a ranged Strike as part of Retributive Strike — extends the threat envelope further)
**Boost Priority:** STR → CHA → CON → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Versatile (Natural Ambition) | STR 18/CHA 16 needs both Ranged Reprisal AND a flex L1 feat — Natural Ambition delivers both at once and keeps the build at 30 ft speed despite Full Plate. |
| 2 | Aasimar | Angelkin | +2 Diplomacy/Intimidation pads CHA 16 skills; positive-energy resist syncs with the holy-aura paladin frame and keeps the reach tank standing in undead aoe. |
| 3 | Dwarf | Mountain's Stoutness | +2 HP/level turns the STR 18 reach tank into a near-unkillable wall — pairs with Bulwark Full Plate for a 26-HP-at-L1 baseline. Speed 20 ft is the only cost. |
| 4 | Half-Orc | Hold-Scarred | Diehard for free on a 21-HP reach tank means one extra full turn at 0 HP — a turn where Retributive Strike still fires and Weight of Guilt still enfeebles. |
| 5 | Orc | Hold-Scarred | STR 18 bruiser base lines up perfectly; Ferocity keeps the reaction economy live a round longer than any other option when the frontline collapses. |
| 6 | Halfling | Gutsy | Immune to frightened crit-fail protects Aura of Courage from being negated by a single fear crit — the Barbarian's morale stays load-bearing. |
| 7 | Lizardfolk | Cliffscale | Natural armor gives an alternative AC floor if Full Plate is unavailable early; STR 18 athletics syncs with reach Trip rolls. |
| 8 | Half-Elf | Elf Atavism | Grants Elven Weapon Familiarity (some elven polearms qualify) and keeps stat flexibility for the STR/CHA split. |
| 9 | Goblin | Unbreakable | +4 max HP and Unbreakable pair with Retributive Strike's zero-action requirement at exactly 1 HP — fires one more reaction before going down. |
| 10 | Tiefling | Grimspawn | Void resist 5 shores up the gap against negative-energy undead casters — Vordakai (Ch3) chews through unprotected paladins. |

**Leveling — 13 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 21 | Retributive Strike, Lay on Hands, Shield Block, Paladin's Code | Natural Ambition + **Ranged Reprisal** (Step or ranged-Strike as part of Retributive Strike) |
| 2 | 13 | — | **Weight of Guilt** (Retributive Strike enfeebles on hit — −1 dmg, −1 Athletics; Trip checks easier for the Fighter) |
| 3 | 13 | Divine Ally (weapon: guisarme), Alertness | Mercy |
| 4 | 13 | — | **Aura of Courage** (you and allies within 15 ft reduce Frightened faster — keeps the Giant Barbarian raging) |
| 5 | 13 | Ability Boost (STR/CHA+2), Weapon Expertise | Aura of Faith |
| 6 | 13 | — | **Smite Evil** (extra damage that persists until target dies — focus-fire amplifier in a 7-player team) |
| 7 | 13 | Armor Expertise | Divine Grace |
| 8 | 13 | — | **Greater Radiant Armament** *(or Advanced Deity's Domain if your deity gives a better second-rank option)* |
| 9 | 13 | Juggernaut | Radiant Blade Spirit |
| 10 | 13 | Ability Boost | **Shield of Reckoning** (Shield Block + Retributive Strike in one reaction — this is why the shield stays strapped even with the 2H guisarme) |
| 11 | 13 | — | Litany of Righteousness |
| 12 | 13 | — | **Divine Wall** (your reach zone becomes Difficult Terrain — enemies cannot Step out of the Fighter/Barbarian engagement; they must Stride and eat every Reactive Strike) |
| 13 | 13 | Weapon Mastery | Celestial Form |
| 14 | 13 | — | **Divine Reflexes** (extra reaction every turn for Retributive Strike — in a 7-player party someone is hit every round; this is two reaction-Strikes per round before your turn even starts) |
| 15 | 13 | Ability Boost, Greater Divine Ally | Shining Beacon |
| 16 | — | — | — |
| 17 | 13 | — | Avatar's Grace |
| 18 | — | — | — |
| 19 | 13 | — | Legendary Champion |
| 20 | 13 | Ability Boost | — |

**Auto-level note:** STR+2 first. **Ranged Reprisal at L1 mandatory** (the entire reach-reaction concept depends on it). Crushing Rune on the guisarme (when accessible) procs Clumsy + Enfeebled on crit, layering on top of Weight of Guilt for a Trip-and-stay-down loop with the Reach Fighter. L16/L18 no picks.

**Tactical playbook (DM cues):**
- **Reaction priority:** Retributive Strike fires first when the Barbarian is hit (keeps rage live, Bard's Courageous Anthem boosts the reaction-Strike).
- **Trip from 10 ft:** use the guisarme's Trip trait at reach — Athletics vs Reflex DC. Prone enemy that stands triggers the Fighter's Reactive Strike. Stack with Weight of Guilt's Athletics penalty for higher success.
- **Positioning:** stand 5–10 ft behind the Fighter and Barbarian. Layered threat zone — enemies eat 3+ attacks just to reach the back line (Fighter Reactive Strike → Barbarian opportunity → Paladin Retributive Strike via Ranged Reprisal/Divine Reflexes).
- **L12+ Divine Wall:** announce the difficult-terrain bubble at scene start. Enemies that try to Step out of melee instead Stride, drawing every Reactive Strike on the field.

---

## BUILD — SHIELD ALLY BASTION
**Dwarf (Mountain Stoutness) | Champion (Paladin) + Bastion | Background: Guard**
*Tower shield + Bastion Dedication = fortress mode. Shield of Reckoning fires Shield Block + Retributive Strike simultaneously.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 10 | 18 | 10 | 12 | 14 |
| Mod | +4 | +0 | +4 | +0 | +1 | +2 |

**HP** 24 | **AC** 19 (Mithril Full Plate + Tower Shield) | **Init** +0 | **Perc** +4 | **Speed** 20 ft
**Fort** +9 | **Ref** +4 | **Will** +6
**Weapon:** Dwarven Waraxe (1H S, 1d8+4, Sweep) | **Shield:** Tower Shield (HP 40, Hardness 8) | **Armor:** Mithril Full Plate
**Skills:** Athletics +6, Religion +3, Intimidation +4, Warfare Lore +2
**Focus Spells:** Lay on Hands, Shield of Reckoning (Shield Block + Retributive Strike simultaneously)
**Class Features:** Retributive Strike, Shield Block, Divine Ally (Shield — tower shield upgrades)
**Key Feats:** L1 Dwarven Weapon Familiarity + Mountain Stoutness (heritage, auto)
**Boost Priority:** STR → CON → CHA → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Dwarf | Mountain's Stoutness | HP 26 at L1 plus +1 HP/level makes this the highest-HP tank in the game — tower shield fortress fantasy fulfilled. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition lets this CON 18 build pick up Shield Block AND Dwarven Weapon Familiarity at L1 without the dwarf speed penalty. |
| 3 | Orc | Hold-Scarred | STR 18/CON 18 bruiser frame; Diehard on a tower shield build means the fortress wall literally refuses to fall. |
| 4 | Half-Orc | Hold-Scarred | Orc Blood gives Diehard access with Human's stat flexibility, trading 1 HP base for 10 ft more speed. |
| 5 | Dwarf | Unburdened Iron | No Speed penalty in heavy armor converts the 20 ft Dwarf speed liability to a neutral starting point in full plate. |
| 6 | Halfling | Hillock | Extra HP per rest compounds over a long dungeon crawl for this high-CON build that wants every hit point. |
| 7 | Goblin | Unbreakable | +4 max HP is the simplest possible upside for a tower shield build whose only job is absorbing damage totals. |
| 8 | Lizardfolk | Cliffscale | Natural armor redundancy and STR synergy — a good thematic fit for a slow, immovable fortress Champion. |
| 9 | Aasimar | Angelkin | Angelkin's resist positive/negative adds a secondary layer of damage mitigation on top of the tower shield's hardness. |
| 10 | Tiefling | Pitborn | Athletics +2 means better Shove/Trip action economy on a STR 18 build that sometimes wants to move enemies off-flank. |

**Leveling — 14 HP/level** (+1/level Mountain Stoutness)
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 24 | Retributive Strike, Lay on Hands, Shield Block, Paladin's Code | Dwarven Weapon Familiarity + Mountain Stoutness |
| 2 | 14 | — | Bastion Dedication |
| 3 | 14 | Divine Ally (Shield upgrade), Alertness | Quick Shield Block |
| 4 | 14 | — | Shield Warden |
| 5 | 14 | Ability Boost (STR/CON+2), Weapon Expertise | Shield of Reckoning |
| 6 | 14 | — | Shield Ally (Bastion — adj ally +2 AC) |
| 7 | 14 | Armor Expertise | Tower Shield Specialist |
| 8 | 14 | — | Reflexive Shield |
| 9 | 14 | Juggernaut | Radiant Blade Spirit |
| 10 | 14 | Ability Boost | Holy Avenger |
| 11 | 14 | — | Resurrection Blessing |
| 12 | 14 | — | Invulnerable Juggernaut |
| 13 | 14 | Weapon Mastery | Celestial Form |
| 14 | 14 | — | Sacred Defense |
| 15 | 14 | Ability Boost, Greater Divine Ally | Shining Beacon |
| 16 | — | — | — |
| 17 | 14 | — | Avatar's Grace |
| 18 | — | — | — |
| 19 | 14 | — | Legendary Champion |
| 20 | 14 | Ability Boost | — |

**Auto-level note:** STR+2 first. Bastion Dedication at L2 mandatory. Shield HP L1 40 → L9 80. L16/L18 no picks.

---

## BUILD — PALADIN DUAL FOCUS CHAMPION
**Aasimar (Angelically Blessed) | Champion (Paladin) + Oracle Dedication | Background: Acolyte**
*Two focus pools from L2: Lay on Hands + Oracle Life mystery revelation. Healing nova reaction chain.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 16 | 10 | 14 | 10 | 14 | 18 |
| Mod | +3 | +0 | +2 | +0 | +2 | +4 |

**HP** 20 | **AC** 16 (Scale Mail + Shield) | **Init** +0 | **Perc** +5 | **Speed** 25 ft
**Fort** +7 | **Ref** +4 | **Will** +9
**Weapon:** Longsword (1H S, 1d8+3, Versatile P) | **Shield:** Steel Shield | **Armor:** Scale Mail
**Skills:** Religion +6, Diplomacy +9, Medicine +4, Healing Lore +4
**Focus Spells:** Lay on Hands (1d6+5 heal), Oracle Dedication (Life mystery — Healer's Light)
**Class Features:** Retributive Strike, Shield Block, Divine Ally, Oracle Dedication (L2 — adds focus pool)
**Key Feats:** L1 Natural Ambition + Healing Touch
**Boost Priority:** CHA → WIS → CON → STR

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Aasimar | Angelkin | Angelkin's +2 Diplomacy and positive energy resist directly amplify CHA 20 Lay on Hands output and the dual-focus healing identity. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition secures both Healing Touch AND a second feat at L1 — critical when CHA 20 Oracle dual-pool comes online at L2. |
| 3 | Halfling | Gutsy | Immune to frightened crit-fail protects the WIS 14 Will save gap while this CHA-heavy build invests in the Oracle multiclass. |
| 4 | Kitsune | Celestial | Celestial Kitsune's innate divine cantrip complements the Oracle Life mystery and leans into the divine/celestial thematic identity. |
| 5 | Gnome | Wellspring | Wellspring's free 1st-level spell/day gives an extra healing slot on top of the dual focus pools at no feat investment. |
| 6 | Half-Elf | Elf Atavism | Elf Atavism adds elf feat access for Elven Weapon Familiarity or Ancient Elf multiclass — broadens an already-complex build's ceiling. |
| 7 | Leshy | Gourd | Gourd Leshy's light emission helps a WIS 14/DEX 10 build that lacks darkvision and can't afford night-blind Lay on Hands misses. |
| 8 | Dwarf | Mountain's Stoutness | Offsets the CHA-primary HP trade-off; CON 14 with Mountain's Stoutness pushes HP closer to front-line-sustainable levels. |
| 9 | Elf | Ancient Elf | Ancient Elf grants a free multiclass dedication at L1 — can front-load Oracle Dedication even earlier than L2. |
| 10 | Goblin | Unbreakable | +4 max HP prevents one-shot kills on a CON 14 Aasimar Champion with suboptimal AC from Scale Mail instead of full plate. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Retributive Strike, Lay on Hands, Shield Block, Paladin's Code | Natural Ambition + Healing Touch |
| 2 | 12 | — | Oracle Dedication (Life mystery + Healer's Light) |
| 3 | 12 | Divine Ally, Alertness | Mercy (remove condition with Lay on Hands) |
| 4 | 12 | — | Aura of Courage |
| 5 | 12 | Ability Boost (CHA/WIS+2), Weapon Expertise | Advanced Oracle Spell (Basic Revelation) |
| 6 | 12 | — | Aura of Faith |
| 7 | 12 | Armor Expertise | Greater Mercy |
| 8 | 12 | — | Extend Mercy |
| 9 | 12 | Juggernaut | Radiant Blade Spirit |
| 10 | 12 | Ability Boost | Holy Avenger |
| 11 | 12 | — | Resurrection Blessing |
| 12 | 12 | — | Invulnerable Juggernaut |
| 13 | 12 | Weapon Mastery | Celestial Form |
| 14 | 12 | — | Sacred Defense |
| 15 | 12 | Ability Boost, Greater Divine Ally | Shining Beacon |
| 16 | — | — | — |
| 17 | 12 | — | Avatar's Grace |
| 18 | — | — | — |
| 19 | 12 | — | Legendary Champion |
| 20 | 12 | Ability Boost | — |

**Auto-level note:** CHA+2 first. Oracle Dedication at L2 mandatory — dual focus pool. LoH L1 1d6+5 → L20 10d6+10. L16/L18 no picks.

---

## BUILD — SHIELD OF PURITY
**Human (Versatile Heritage) | Champion (Redeemer, Sarenrae) | Background: Acolyte**
*Glimpse of Redemption + Weight of Guilt: ally hit → attacker takes −2 dmg AND Enfeebled. Shield Warden + Quick Shield Block + Shield of Reckoning create a triple-reaction chain. Divine Reflexes doubles it.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 10 | 14 | 10 | 14 | 14 |
| Mod | +4 | +0 | +2 | +0 | +2 | +2 |

**HP** 20 | **AC** 16 (Scale Mail + Shield) | **Init** +2 | **Perc** +5 | **Speed** 25 ft
**Fort** +7 | **Ref** +5 | **Will** +7
**Weapon:** Longsword — *Caliburn* (1H S, 1d8+4, Versatile P) | **Shield:** Steel Shield — *Avalon* | **Armor:** Scale Mail
**Skills:** Athletics +6, Religion +6, Diplomacy +6, Medicine +4
**Focus Spells:** Lay on Hands (1d6+2 heal), Glimpse of Redemption (−2 all dmg rolls to attacker)
**Class Features:** Glimpse of Redemption (reaction: enemy attacks ally → −2 all damage rolls), Shield Block, Divine Ally, 15 ft Aura
**Key Feats:** Versatile Heritage (heritage, auto) + General Training (ancestry feat) + Healing Touch | L2 Weight of Guilt | L10 Shield of Reckoning | L14 Divine Reflexes
**Boost Priority:** STR → CHA → WIS → CON

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Human | Versatile | Free general feat at L1 alongside Healing Touch — STR 18/CHA 14 Redeemer needs both combat output and healing access from session one. |
| 2 | Aasimar | Angelkin | Sarenrae's iconic ancestry; +2 Diplomacy/Intimidation on CHA 14 adds social utility while positive energy resist compounds the build's healing-heavy playstyle. |
| 3 | Halfling | Gutsy | Frightened crit-fail immunity prevents the single most dangerous counter to a Redeemer whose Shield Block + Glimpse reaction chain requires a clear reaction window. |
| 4 | Dwarf | Mountain's Stoutness | +1 HP/level on a STR-heavy Redeemer who stays in melee; CON 14 base benefits most from per-level HP compounding across 20 levels. |
| 5 | Orc | Hold-Scarred | STR 18 + Diehard keeps the shield-bearer alive through multi-front retaliation — a Champion who dies before Divine Reflexes fires loses the double-reaction payoff. |
| 6 | Half-Orc | Orc Blood | Hold-Scarred via feat + Human stat flexibility; STR 18 + CON 14 preserved with no compromise while adding Diehard for the frontline tank. |
| 7 | Tiefling | Pitborn | Sarenrae's fire theme synergizes with Pitborn fire resist 5; CHA-favoring outsider keeps the Champion charismatic across the long campaign. |
| 8 | Half-Elf | Elf Atavism | Ancient Elf path gets a free dedication at L1 — Bastion Dedication accelerates the Shield Block chain without burning the L2 class feat slot on an archetype. |
| 9 | Goblin | Unbreakable | +4 max HP raises the L1 floor to 24 — a Champion who willingly takes hits to block for allies needs every hit point to outlast the fights. |
| 10 | Kitsune | Celestial | CHA 14 + Celestial Kitsune innate divine cantrip expands action options on turns where all reactions are spent and a free attack cantrip is available. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 20 | Glimpse of Redemption, Lay on Hands, Shield Block, Redeemer's Code | Versatile Heritage (heritage, auto) + General Training (ancestry) + + Healing Touch (Lay on Hands usable on self) |
| 2 | 12 | — | Weight of Guilt (Glimpse also Enfeebles attacker — −2 damage AND Enfeebled 2 simultaneously) |
| 3 | 12 | Divine Ally, Alertness | Mercy (remove condition with Lay on Hands) |
| 4 | 12 | — | Aura of Courage (15 ft aura: allies reduce Frightened by 1 each round end) |
| 5 | 12 | Ability Boost (STR/CHA+2), Weapon Expertise | Shield Warden (share Shield Block reaction with an adjacent ally) |
| 6 | 12 | — | Quick Shield Block (extra Shield Block reaction per round) |
| 7 | 12 | Armor Expertise | Aura of Faith |
| 8 | 12 | — | Extend Mercy |
| 9 | 12 | Juggernaut | Radiant Blade Spirit |
| 10 | 12 | Ability Boost | Shield of Reckoning (use Shield Block + Glimpse of Redemption as a single reaction simultaneously) |
| 11 | 12 | — | Lasting Spirit (Lay on Hands triggers for free once when ally would drop below 0 HP) |
| 12 | 12 | — | Aura of Righteousness |
| 13 | 12 | Weapon Mastery | Celestial Form |
| 14 | 12 | — | Divine Reflexes (extra champion reaction per round — two Glimpse reactions before your own turn) |
| 15 | 12 | Ability Boost, Greater Divine Ally | Instrument of Zeal (Glimpse effects extend to all enemies within the aura who attacked the same ally) |
| 16 | — | — | — |
| 17 | 12 | — | Avatar's Grace |
| 18 | 12 | — | Ultimate Mercy (Lay on Hands can restore life to newly-dead allies) |
| 19 | 12 | — | Legendary Champion |
| 20 | 12 | Ability Boost | Shield of Power (shield bonus to AC also applies to adjacent ally's saving throws) |

**Auto-level note:** STR+2 first. Weight of Guilt at L2 is mandatory — Glimpse of Redemption alone is weak, but Enfeebled stacked simultaneously makes it the strongest per-reaction debuff in the game. Divine Reflexes at L14 doubles the chain. L16 no picks.

---

## BUILD — LIBERATOR MOBILITY CHAMPION
**Elf (Nimble Elf) | Champion (Liberator) | Background: Street Urchin**
*Liberating Step counters grapples as a free reaction. 35 ft speed — fastest Champion.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 16 | 14 | 14 | 10 | 12 | 18 |
| Mod | +3 | +2 | +2 | +0 | +1 | +4 |

**HP** 18 | **AC** 18 (Scale Mail + Shield) | **Init** +2 | **Perc** +4 | **Speed** 35 ft
**Fort** +6 | **Ref** +6 | **Will** +7
**Weapon:** Rapier (1H P, 1d6+3, agile, deadly d8, finesse) | **Shield:** Steel Shield | **Armor:** Scale Mail
**Skills:** Acrobatics +4, Athletics +5, Diplomacy +6, Religion +3
**Focus Spells:** Lay on Hands, Freedom's Call (remove grabbed/restrained/immobilized)
**Class Features:** Liberating Step (reaction: ally grabbed/restrained → ally Steps, +2 AC/saves), Shield Block, Divine Ally
**Key Feats:** L1 Elven Weapon Familiarity + Healing Touch
**Boost Priority:** CHA → STR → DEX → WIS

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Elf | Nimble Elf | 35 ft base speed is the entire identity of this build — Liberating Step into a 35 ft reposition reaches targets no other Champion can. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition picks up Healing Touch free, letting CHA 18 fuel both Lay on Hands heal output and Liberating Step reaction simultaneously. |
| 3 | Aasimar | Angelkin | Angelkin's +2 Diplomacy matches CHA 18 and divine identity; positive energy resist adds a tanky layer to a DEX 14/CON 14 frame. |
| 4 | Half-Elf | Elf Atavism | Elf Atavism unlocks Nimble Elf feat access for +5 ft speed while keeping Human's stat flexibility for the DEX 14/CHA 18 spread. |
| 5 | Catfolk | Nimble | +5 ft speed at 35 ft total matches Elf, plus Cat's Luck reroll on DEX saves shores up the Reflex +6 that this finesse build relies on. |
| 6 | Halfling | Gutsy | Frightened immunity on crit-fail prevents disrupting the reaction chain — a Liberator who can't react to grapples defeats the concept. |
| 7 | Gnome | Wellspring | Wellspring's free innate spell offsets CHA 18 limitation at L1 before Lay on Hands fully scales; thematically odd but mechanically clean. |
| 8 | Tengu | Dogtooth | Natural bite adds a free third attack when Rapier MAP gets too steep; DEX 14 finesse supports identical proficiency scaling. |
| 9 | Half-Orc | Hold-Scarred | Diehard free prevents death on a low-HP Elf base (18 HP) — keeping the fastest Champion alive one extra round is the whole payoff. |
| 10 | Fetchling | Liminal | Shadow step 1/day is a bonus teleport repositioning tool for the mobility-focused Liberator who runs out of Stride budget. |

**Leveling — 12 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 18 | Liberating Step, Lay on Hands, Shield Block, Code | Elven Weapon Familiarity + Healing Touch |
| 2 | 12 | — | Ranged Reprisal |
| 3 | 12 | Divine Ally, Alertness | Aura of Courage |
| 4 | 12 | — | Mercy |
| 5 | 12 | Ability Boost (CHA/STR+2), Weapon Expertise | Aura of Faith |
| 6 | 12 | — | Liberating Stride (ally Strides instead of Steps) |
| 7 | 12 | Armor Expertise | Divine Grace |
| 8 | 12 | — | Extend Mercy |
| 9 | 12 | Juggernaut | Radiant Blade Spirit |
| 10 | 12 | Ability Boost | Affliction Mercy |
| 11 | 12 | — | Litany of Freedom |
| 12 | 12 | — | Aura of Righteousness |
| 13 | 12 | Weapon Mastery | Celestial Form |
| 14 | 12 | — | Sacred Defense |
| 15 | 12 | Ability Boost, Greater Divine Ally | Shining Beacon |
| 16 | — | — | — |
| 17 | 12 | — | Avatar's Grace |
| 18 | — | — | — |
| 19 | 12 | — | Legendary Champion |
| 20 | 12 | Ability Boost | — |

**Auto-level note:** CHA+2 first. Liberating Stride at L6 automatic (Step→Stride). L16/L18 no picks.

---

## BUILD — PALADIN PURE LAY ON HANDS
**Dwarf (Ancient-Blooded) | Champion (Paladin) | Background: Acolyte**
*Maximum Lay on Hands output, no archetype tax. Ancient-Blooded Dwarf: +2 status vs spell saves.*

| | STR | DEX | CON | INT | WIS | CHA |
|-|-----|-----|-----|-----|-----|-----|
| Score | 18 | 10 | 18 | 10 | 12 | 14 |
| Mod | +4 | +0 | +4 | +0 | +1 | +2 |

**HP** 24 | **AC** 19 (Mithril Full Plate + Shield) | **Init** +0 | **Perc** +4 | **Speed** 20 ft
**Fort** +9 | **Ref** +4 | **Will** +7
**Weapon:** Dwarven Waraxe (1H S, 1d8+4, Sweep) | **Shield:** Steel Shield | **Armor:** Mithril Full Plate
**Skills:** Athletics +6, Religion +5, Medicine +3, Warfare Lore +2
**Focus Spells:** Lay on Hands (1d6+CHA heal), Litany Against Wrath
**Class Features:** Retributive Strike, Shield Block, Divine Ally (Blade — holy weapon)
**Key Feats:** L1 Dwarven Weapon Familiarity + Healing Touch
**Boost Priority:** CON → STR → WIS → CHA

**Race Options** *(ranked best-fit — pick any)*

| # | Ancestry | Heritage | Why It Fits |
|---|----------|----------|-------------|
| ★1 | Dwarf | Ancient-Blooded | +2 status to all saves vs spells at CON 18 turns the already-armored Dwarf into an anti-caster fortress with zero feat investment. |
| 2 | Human | Versatile (Natural Ambition) | Natural Ambition at STR 18/CON 18 grabs Healing Touch AND Dwarven-equivalent at L1 without the 20 ft speed drawback. |
| 3 | Aasimar | Angelkin | Angelkin resist positive/negative benefits a Lay on Hands-focused Paladin who channels both positive and negative energy types. |
| 4 | Dwarf | Mountain's Stoutness | Mountain's Stoutness +1 HP/level pushes the CON 18 HP chain to max sustainable frontline totals across a 20-level campaign. |
| 5 | Orc | Hold-Scarred | Diehard at STR 18/CON 18 means the pure LoH build survives long enough to heal the party even after being dropped to 0 HP. |
| 6 | Half-Orc | Hold-Scarred | Same Diehard benefit with Human's stat range for the CON 18 push; 10 ft more speed than Dwarf as a trade-off. |
| 7 | Halfling | Hillock | Extra HP per rest is small but consistent — across a full campaign the HP floor stays higher without consuming any feat slots. |
| 8 | Lizardfolk | Cliffscale | Natural armor floor on a build with no archetype tax means no wasted slots on AC — gear budget goes straight to LoH gear. |
| 9 | Goblin | Unbreakable | +4 max HP is the simplest possible upgrade for a CON 18 build where every HP added extends the Lay on Hands reaction window. |
| 10 | Tiefling | Pitborn | Fire resist 5 and Athletics bonus at STR 18 adds marginal martial coverage to a non-archetype Paladin staying in the fight longer. |

**Leveling — 14 HP/level**
| Lvl | HP | Auto Features | [PICK] Feat |
|-----|----|---------------|-------------|
| 1 | 24 | Retributive Strike, Lay on Hands, Shield Block, Paladin's Code | Dwarven Weapon Familiarity + Healing Touch |
| 2 | 14 | — | Ranged Reprisal |
| 3 | 14 | Divine Ally, Alertness | Mercy (remove condition with Lay on Hands) |
| 4 | 14 | — | Aura of Courage |
| 5 | 14 | Ability Boost (CON/STR+2), Weapon Expertise | Shield of Reckoning |
| 6 | 14 | — | Aura of Faith |
| 7 | 14 | Armor Expertise | Greater Mercy |
| 8 | 14 | — | Extend Mercy |
| 9 | 14 | Juggernaut | Radiant Blade Spirit |
| 10 | 14 | Ability Boost | Affliction Mercy |
| 11 | 14 | — | Resurrection Blessing |
| 12 | 14 | — | Aura of Righteousness |
| 13 | 14 | Weapon Mastery | Celestial Form |
| 14 | 14 | — | Sacred Defense |
| 15 | 14 | Ability Boost, Greater Divine Ally | Shining Beacon |
| 16 | — | — | — |
| 17 | 14 | — | Avatar's Grace |
| 18 | — | — | — |
| 19 | 14 | — | Legendary Champion |
| 20 | 14 | Ability Boost | — |

**Auto-level note:** CON+2 first. No archetype — all feats in Mercy chain. LoH L1 1d6+2 → L20 10d6+6. L16/L18 no picks.

---

> **➡️ Cleric builds 1–6: see `KM_Builds_C4.md`**
> **➡️ Full class index: see `KM_BuildScreen.md`**

*KM_Builds_C.md — Kingmaker PF2e Text Adventure | Builds: Champion (1–6) v2.0*
