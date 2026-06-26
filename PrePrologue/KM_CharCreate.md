# KINGMAKER — GUIDED CHARACTER CREATION
## KM_CharCreate.md | Referenced by: KM_BuildGuide.md, KM_Ancestries.md

> **DM:** Load this file at session start, before KM_BuildGuide.md. Walk the player
> through each step in order. Display guidance text to help them choose — these are
> player-facing, not DM-only. After class + build are confirmed, return here for
> ancestry and background. Weapon selection runs through KM_BuildGuide.md Step 2.5.

---

## ⛔ CREATION ORDER

> **Authoritative sequence — must match KM_BuildGuide.md STEP 3. Any deviation = `.fail 9`.**

```
1. Class       → This file (guidance) → KM_BuildGuide.md (build lists)
2. Build       → KM_BuildGuide.md (10 presets per class) → record player.build,
                 player.build_source, player.leveling_mode
3. Ancestry    → This file (guidance + full list) → KM_Ancestries.md class block
4. Heritage    → KM_Ancestries.md (core + uncommon + Goliath) + KM_Ancestries.md (rare + 8 versatile heritages)
5. Background  → This file (summary) → KM_Ancestries.md (full text, 1–7) +
                 KM_Ancestries.md (8–42)
5.5 Boosts+Feats → This file STEP 5.5 (stat assembly, L1 ancestry/background/class feats)
6. Deity       → This file STEP 6 (divine classes mandatory, others optional)
7. Skills      → This file STEP 7 (class-fixed + N + INT mod player picks)
8. Weapon      → KM_BuildGuide.md Step 2.5 → STAT-WEAPON CHECK (Step 5.5)
9. Armor       → KM_BuildGuide.md Step 2.6  ⚠️ flag DEX cap for DEX +3 or higher
10. Confirm    → This file STEP 10 (.status: HP/AC/languages/feats/skills) → Pick-10
```

> **Why ancestry/background precede weapon/armor:** Ancestry bonuses can shift stat spreads, which affects the STAT-WEAPON CHECK (Step 5.5 in KM_BuildGuide.md). Running weapon selection before ancestry is resolved can force a second pass. Background may also grant weapon proficiencies (e.g., Sword Scion) that widen the weapon menu.

---

## STEP 1 — CLASS SELECTION

> **DM:** Display the class menu below. Offer to answer questions before the player
> commits. After they pick a class number, load KM_BuildGuide.md and display that
> class's build list.

```
══════════════════════════════════════════════════════════════
KINGMAKER — CHOOSE YOUR CLASS
══════════════════════════════════════════════════════════════
Not sure? Each class has a role, difficulty, and note below.
★ = New player recommended

MARTIAL
  [1]  Alchemist      Bombs + potions. High utility, complex action economy.
  [3]  Barbarian    ★ Rage and hit things. Simple, enormous damage output.
  [10] Fighter      ★ Best weapon mastery in the game. No resource limits.
  [11] Guardian     ★ Dedicated tank. Keep allies alive by drawing fire.
  [12] Gunslinger     Reload and shoot. High burst, fun mechanics.
  [17] Monk           Unarmed mastery + ki. Mobile and hard to pin down.
  [21] Rogue          Sneak attack + skills. Best utility outside combat.
  [24] Swashbuckler   Panache and finishers. High crits, mobile, stylish.

MARTIAL + MAGIC HYBRID
  [16] Magus          Spellstrike melee. Complex ceiling, massive payoff.
  [13] Inventor       Build gadgets and constructs. Creative and unusual.
  [25] Thaumaturge    Exploit monster weaknesses via implements. Unique.

DIVINE / OCCULT
  [5]  Champion     ★ Holy warrior + protector. Lay on hands. Easy to play.
  [6]  Cleric       ★ Heal or fight — choose a doctrine. Most versatile support.
  [9]  Exemplar       Divine ikon warrior. New class, ikon-based abilities.
  [18] Oracle         Cursed divine caster. Power comes with a price.
  [26] Witch          Hexes and patron magic. Debuff + control specialist.

ARCANE / PRIMAL
  [8]  Druid          Wildshape or summon or storm. Versatile primal caster.
  [15] Kineticist      Elemental blasting, no daily limits. Sustained output.
  [19] Psychic         Amped cantrips. Mental blasting and control.
  [22] Sorcerer        Bloodline magic. Spontaneous, easier than Wizard.
  [27] Wizard          Most spell options. Preparation mastery. High ceiling.

SUPPORT / HYBRID
  [2]  Animist        Spirit channeling. Flexible support or striker.
  [4]  Bard          ★ Inspire allies. Best party buffer in the game.
  [7]  Commander       Lead through orders. Powerful, complex action economy.
  [14] Investigator    Devise Stratagem + skills. Precision striker/face.
  [20] Ranger        ★ Hunter's Edge + quarry. Excellent damage, simple system.
  [23] Summoner        Shared actions with eidolon. Unique, moderately complex.

Type a number (1–27). Type ? [class name] for a full description before committing.
══════════════════════════════════════════════════════════════
```

### CLASS GUIDANCE — FULL DESCRIPTIONS

> **DM:** If the player types ? before a class name, read the entry below and display it.

**Alchemist** — You craft bombs, mutagens, and elixirs. Perpetual Infusions give you
unlimited basic items at no cost. Every fight you're managing what to throw, when to
mutate, and what your allies need. High skill ceiling. Excellent utility.
*Difficulty: ★★★★ | Best ancestries: Gnome, Human, Halfling*

**Animist** — You channel spirits — battle spirits, ancestral echoes, ghost domain.
Flexible between support, striker, and debuffer. Your spirits shift based on
which you're channeling. Moderate complexity, high flavor.
*Difficulty: ★★★ | Best ancestries: Human, Elf, Leshy*

**Barbarian** — You rage. Your damage goes up, you take hits, you end fights fast.
Giant Instinct gives you an oversized weapon with massive reach and damage.
Easiest entry point for a player who wants to feel powerful immediately.
*Difficulty: ★★ | Best ancestries: Orc, Human, Dwarf*

**Bard** — You inspire your allies. Inspire Courage alone makes every fighter in the
party hit harder. You also have strong occult spells for control and support. One of
the most impactful classes even at low optimization.
*Difficulty: ★★★ | Best ancestries: Halfling, Human, Gnome*

**Champion** — You stand between your allies and harm. Lay on Hands heals as a free
action. Your Champion Reaction punishes enemies for hitting your friends. Durable,
protective, and forgiving to play.
*Difficulty: ★★ | Best ancestries: Human, Dwarf, Aasimar*

**Cleric** — Two doctrines, two completely different characters. Warpriest wears armor
and fights. Cloistered stays back and floods the party with healing font. Both are
excellent. Best class if you want to feel essential to the party.
*Difficulty: ★★ | Best ancestries: Human, Dwarf, Gnome*

**Commander** — You issue orders that give allies extra actions and attacks. High
party impact, but your own action economy takes practice. The best class for a
player who wants to orchestrate rather than execute.
*Difficulty: ★★★★ | Best ancestries: Human, Halfling, Dwarf*

**Druid** — Three strong paths: Wild Shape into predator forms, summon animal hordes,
or call lightning storms. All three work. Wild Shape is the most tactile.
*Difficulty: ★★★ | Best ancestries: Elf, Gnome, Leshy, Human*

**Exemplar** — Divine warrior who channels power through ikons (weapon, body, worn item).
Newer class with unique flavor and strong martial+divine mix.
*Difficulty: ★★★ | Best ancestries: Human, Orc, Dwarf*

**Fighter** — The most reliable martial. Your weapon proficiency is one tier above
every other class. You have no daily resources — every ability works all day.
If you want to hit things effectively without worrying about resource management,
this is the class.
*Difficulty: ★ | Best ancestries: Dwarf, Orc, Human, Goblin*

**Guardian** — You exist to protect. Provoke enemies into targeting you, then absorb
damage with shield blocks and resistances. Simple, effective, and the party
thanks you for it.
*Difficulty: ★★ | Best ancestries: Dwarf, Orc, Human*

**Gunslinger** — Reload, aim, shoot. Pistolero delivers high-crit ranged bursts.
Spellshot adds magic. Managing reload actions takes practice but becomes fluid.
*Difficulty: ★★★ | Best ancestries: Gnome, Human, Goblin*

**Inventor** — Your innovation is your identity: construct companion, megaweapon, or
armor. Creative problem-solving class. Unstable actions add risk and reward.
*Difficulty: ★★★★ | Best ancestries: Gnome, Human, Kobold*

**Investigator** — Devise Stratagem lets you use INT instead of STR/DEX for attack
rolls on your hunted target. Excellent face, excellent skills, solid precision damage.
*Difficulty: ★★★ | Best ancestries: Elf, Human, Gnome*

**Kineticist** — Elemental blasting with no spell slots, no daily limits. Pick your
gate (fire, earth, air, water, wood, metal) and blast all day. One of the most
beginner-friendly casters because you never run out.
*Difficulty: ★★ | Best ancestries: Dwarf, Gnome, Human, Orc*

**Magus** — You cast a spell through your weapon strike. Shocking Grasp + Spellstrike
= one massive hit. Laughing Shadow teleports you before striking. High learning
curve, but the payoff per level is enormous.
*Difficulty: ★★★★ | Best ancestries: Elf, Human, Fetchling*

**Monk** — Unarmed mastery, stances, and ki. Flurry of Blows at level 1 is already
two attacks. Extremely mobile. One of the best unarmored survivability options.
*Difficulty: ★★★ | Best ancestries: Human, Catfolk, Tengu*

**Oracle** — Your mystery grants power; your curse is the cost. Life Mystery makes
you a healer who gets stronger as the curse worsens. Battle Mystery makes you a
fighter. Powerful and flavorful.
*Difficulty: ★★★ | Best ancestries: Human, Aasimar, Gnome*

**Psychic** — Amplified cantrips that scale dramatically. No daily limits at low
level; stronger abilities unlock at higher levels. Mental blasting and emotional
control. Unusual and effective.
*Difficulty: ★★★ | Best ancestries: Elf, Human, Fetchling*

**Ranger** — Mark your target, hit it repeatedly, hit it again. Hunter's Edge
(Flurry or Precision) defines your style. Simple to learn, consistently excellent.
*Difficulty: ★★ | Best ancestries: Elf, Human, Halfling*

**Rogue** — Sneak attack triggers on flanking or off-guard enemies. Mastermind
uses INT and Recall Knowledge instead. Best skill coverage of any class.
*Difficulty: ★★★ | Best ancestries: Halfling, Elf, Human, Gnome*

**Sorcerer** — Your bloodline determines your spell list. No preparation needed —
spontaneous casting means you cast what you know, when you want. Easier than
Wizard to play, slightly less flexible.
*Difficulty: ★★ | Best ancestries: Human, Gnome, Elf*

**Summoner** — Your eidolon acts on your turn sharing your action pool. You and
your eidolon together are a two-body problem. Powerful, unusual action economy.
*Difficulty: ★★★★ | Best ancestries: Human, Gnome, Elf*

**Swashbuckler** — Build panache through acrobatics, taunts, or disarms, then spend
it on a Precise Strike finisher. High crit fishing. Extremely mobile. Fun.
*Difficulty: ★★★ | Best ancestries: Human, Elf, Catfolk, Halfling*

**Thaumaturge** — Exploit monster vulnerabilities via implements. Every enemy has a
weakness you can find and press. Unique flavor, strong against bosses.
*Difficulty: ★★★ | Best ancestries: Human, Gnome, Dwarf*

**Witch** — Hexes that linger, cackle to extend them. Patron determines your spell
list. Strong debuffer and controller. Familiar is your spellbook.
*Difficulty: ★★★ | Best ancestries: Gnome, Elf, Human*

**Wizard** — Prepare every spell you know from your spellbook each day. Most
spell variety of any caster. School specialization or Universalist flexibility.
Powerful but demands knowledge of what spells to prepare.
*Difficulty: ★★★★★ | Best ancestries: Elf, Gnome, Human*

---

## STEP 2 — BUILD SELECTION

> **DM:** Load `KM_BuildGuide.md` and display the 10-preset block for the player's chosen class.
> Mark the ★ recommended preset. After the player picks a number (1–10), record the build name
> and source file in the save block and set leveling mode to AUTO (default for preset builds).
> Inform the player that level-up feat picks will be applied automatically unless they switch modes.

**Script (player-facing):**
```
Here are your 10 preset builds for [Class]. Each includes a full L1–20 leveling map.
By default I'll apply the recommended feat automatically each time you level up (AUTO mode).
Type ASK if you want to choose your own feats instead.

[BUILD LIST — display from KM_BuildGuide.md for this class]
```

**After build pick — record in save block:**
```
player.build         = [Build Name e.g. "Giant Reach"]
player.build_source  = KM_Builds_[file].md  (look up in KM_Builds.md router)
player.leveling_mode = MANUAL               ← default; change to AUTO or ASK anytime
```

> ⚠️ Player leveling is `MANUAL` always (player picks every option himself —
> ⛔ NO ★ recommendation marked, NO AUTO pick pre-selected, NO "lock both" shortcut;
> the build map is reference the player may ASK for, never pushed — user directive 2026-06-16).
> Companion leveling is governed by
> `game_options.companion_leveling_mode` (default `AUTO`) — always handled silently
> from build maps unless player switches it.
> ⚠️ If the player declines all 10 presets or says CUSTOM, set `player.leveling_mode = ASK`
> and record `player.build = CUSTOM`. All feat choices will be presented at each level-up.

**Leveling mode reference (player can change anytime with `/mode auto|ask|manual`):**
| Mode   | Behavior |
|--------|----------|
| AUTO   | DM silently applies build-map feat picks; announces inline with level-up block |
| ASK    | DM presents build-map recommendation but player confirms or overrides |
| MANUAL | DM presents all options; player chooses without recommendations |

---

> **➡️ STEPS 3 (Ancestry), 4 (Heritage), 5 (Background), 5.5 (Ability Boosts + L1 Feats), 6 (Deity), 7 (Skills), TIPS FOR NEW PLAYERS, and STEP 10 (Final Confirmation) — see `KM_CharCreate.md`. Pair-load both files for any guided creation session.**

---

*KM_CharCreate.md — Kingmaker PF2e Text Adventure | Char Create v2.0 (split — pair-load with KM_CharCreate.md)*


---

<!-- merged from KM_CharCreate.md (v93.21 file consolidation) -->

# KINGMAKER — GUIDED CHARACTER CREATION (PART B)
## KM_CharCreate.md | Pair-load with KM_CharCreate.md

> **DM:** Part B of guided character creation (Mode B). Always pair-load with `KM_CharCreate.md` (Part A covers the creation order, Step 1 Class Selection, and Step 2 Build Selection). This file covers Steps 3 (Ancestry), 4 (Heritage), 5 (Background), 5.5 (Ability Boosts + L1 Feats), 6 (Deity), 7 (Skills), Tips for New Players, and Step 10 (Final Confirmation).

---

## STEP 3 — ANCESTRY SELECTION

> **DM:** After class + build + weapon are confirmed, display the ancestry menu below.
> Player picks a number. Record `player.ancestry` in save block.
> Ancestry weapon substitution rule applies (KM_PrePrologue_Setup.md).
> Also record `player.languages[]`: Common + ancestry language + INT mod bonus languages (INT mod > 0 only).
>
> **If player types `? [ancestry]` or asks for more detail:** load `KM_Ancestries.md` and display that ancestry's full entry (stats, size, heritages, L1 feats, culture, lifespan, build synergy).

```
══════════════════════════════════════════════════════════════
CHOOSE YOUR ANCESTRY
Type a number. Type ? [name] for full description.
══════════════════════════════════════════════════════════════
COMMON
  [1]  Human       Free boosts, versatile, extra feat at level 1
  [2]  Elf         DEX + INT, low-light vision, long-lived
  [3]  Dwarf       CON + WIS, darkvision, stout and resistant
  [4]  Gnome       CON + INT, low-light vision, small, gnome magic
  [5]  Halfling    DEX + WIS, small, lucky, keen eyes
  [6]  Goblin      DEX + CHA, darkvision, small, goblin lore
  [7]  Hobgoblin   CON + whatever, darkvision, martial discipline
  [8]  Orc         STR + CON, darkvision, ferocious survivability
  [9]  Leshy       CON + WIS, plant form, low-light, nature tied

UNCOMMON
 [10]  Lizardfolk  STR + WIS + CON, cold-blooded, natural armor
 [11]  Tengu       DEX + INT, low-light, beak, sword-trained
 [12]  Catfolk     DEX + CHA, low-light, agile, lucky
 [13]  Kitsune     DEX + CHA, change shape, trickster magic
 [14]  Kobold      DEX + CHA, darkvision, small, clever crafter
 [15]  Ratfolk     DEX + INT, low-light, small, pack tactics
 [16]  Sprite      DEX + INT, flight (at higher levels), tiny
 [17]  Fetchling   DEX + CHA, darkvision, shadow-touched
 [18]  Gnoll       STR + CON, darkvision, Pack Attack
 [19]  Grippli     DEX + WIS, small, frog-tongue, swamp-born
 [20]  Nagaji      STR + CON, low-light, scales, serpent magic

RARE
 [21]  Anadi       DEX + WIS, spider-folk, change shape, web
 [22]  Automaton   STR + CON, construct traits, no sleep/food/air
 [23]  Azarketi    STR + CON, aquatic, gills, amphibious
 [24]  Poppet      CON + CHA, construct, tiny, curious survivor
 [25]  Fleshwarp   STR + CON, aberrant mutation, frightening form
 [26]  Vanara      DEX + WIS, prehensile tail, forest-born
 [27]  Aasimar     CON or CHA + free, darkvision, celestial resist, divine innate spells
 [28]  Tiefling    CON or INT + free, darkvision, resist fire, fiendish innate spells
══════════════════════════════════════════════════════════════
```

### ANCESTRY DETAILS

**[1] Human** — HP +8 | Speed 25 | Normal vision
Two free ability boosts (most flexible in the game). Gain a bonus General feat at
level 1. Best ancestry if you're not sure — humans are never a wrong pick.
Best for: Any class. Especially strong for classes needing multiple stats.

**[2] Elf** — HP +6 | Speed 30 | Low-light vision
+DEX, +INT, −CON. Naturally gifted spellcasters and archers. Elven Weapon
Familiarity gives access to superior elven weapons. Long-lived: bonus lore skill.
Best for: Wizard, Magus, Ranger, Rogue, Investigator, Psychic.

**[3] Dwarf** — HP +10 | Speed 20 | Darkvision
+CON, +WIS, −CHA. Hardiest ancestry in the game. Ancient-Blooded adds saves
vs. magic. Clan Dagger is a free ancestral weapon. Stubborn means more rerolls.
Best for: Fighter, Guardian, Champion, Cleric, Barbarian, Kineticist.

**[4] Gnome** — HP +8 | Speed 25 | Low-light vision
+CON, +INT, −STR. Small size. Gnome magic gives free cantrips even on martials.
Obsessive gives a free skill increase. Excellent for hybrid and caster builds.
Best for: Wizard, Witch, Alchemist, Inventor, Investigator, Gunslinger.

**[5] Halfling** — HP +6 | Speed 25 | Low-light vision
+DEX, +WIS, −STR. Small size. Halfling Luck rerolls critical failures. Keen
Eyes gives bonuses to find concealed creatures. Culturally adaptable.
Best for: Rogue, Ranger, Bard, Cleric, Swashbuckler.

**[6] Goblin** — HP +6 | Speed 25 | Darkvision
+DEX, +CHA, −WIS. Small size. Burn It! bonus on fire damage. Junk Tinker
builds useful items from scraps. Fast Movement feat available early.
Best for: Alchemist, Gunslinger, Rogue, Inventor, Kineticist (fire).

**[7] Hobgoblin** — HP +8 | Speed 25 | Darkvision
+CON + free boost, −free flaw. Martial Training ancestry feat gives extra weapon
proficiency. Steelskin provides damage resistance. Disciplined and durable.
Best for: Fighter, Guardian, Ranger, Champion, Barbarian.

**[8] Orc** — HP +10 | Speed 25 | Darkvision
+STR + free boost, −free flaw. Orc Ferocity keeps you alive past 0 HP once per
day. Bloody Blows adds bleed on crits. The hardest-hitting ancestry.
Best for: Barbarian, Fighter, Guardian, Champion, Kineticist.

**[9] Leshy** — HP +8 | Speed 25 | Low-light vision
+CON, +WIS, −INT. Plant creature — immune to poison, no need to breathe.
Leshy families (leaf, gourd, vine, etc.) each add different abilities.
Best for: Druid, Animist, Cleric, Kineticist (wood).

**[10] Lizardfolk** — HP +8 | Speed 25 | Low-light vision
+STR, +WIS, +CON, −INT. Unarmed claws and tail. Hold Breath underwater.
Natural Armor feat adds AC. Excellent for tanky or natural-weapon builds.
Best for: Barbarian, Monk, Champion, Fighter, Guardian.

**[11] Tengu** — HP +6 | Speed 25 | Low-light vision
+DEX, +INT, −CON. Beak as unarmed attack. Tengu Weapon Familiarity: katana
and wakizashi treated as martial. Strong sword-user ancestry.
Best for: Rogue, Fighter, Monk, Swashbuckler, Magus.

**[12] Catfolk** — HP +8 | Speed 25 | Low-light vision
+DEX, +CHA, −WIS. Cat's Luck gives an extra reroll per day. Nimble
Catfolk feat grants free Athletics for movement. Predatory Rush for pouncing.
Best for: Rogue, Swashbuckler, Monk, Ranger, Bard.

**[13] Kitsune** — HP +8 | Speed 25 | Low-light vision
+DEX, +CHA, −free flaw. Change Shape (fox ↔ humanoid or alternate form).
Fox Spark adds free innate cantrips. Excellent for social and arcane builds.
Best for: Sorcerer, Bard, Rogue, Witch, Oracle.

**[14] Kobold** — HP +6 | Speed 25 | Darkvision
+DEX, +CHA, −STR. Small size. Crafter's Instinct bonus to Crafting.
Kobold Breath (once/day) adds elemental damage option. Pack tactics synergy.
Best for: Alchemist, Inventor, Sorcerer, Rogue, Wizard.

**[15] Ratfolk** — HP +6 | Speed 25 | Low-light vision
+DEX, +INT, −STR. Small size. Cheek Pouches carry free extra items. Rat
Familiar grants a familiar. Vicious Incisors for unarmed bite attacks.
Best for: Alchemist, Rogue, Wizard, Investigator, Inventor.

**[16] Sprite** — HP +6 | Speed 20 (fly 20 at higher levels) | Low-light vision
+DEX, +INT, −STR. Tiny size. Sprite Magic gives innate cantrips. Flight
feats unlock early for Sprites. Fragile but mobile and magically gifted.
Best for: Witch, Wizard, Bard, Sorcerer, Rogue.

**[17] Fetchling** — HP +8 | Speed 25 | Darkvision
+DEX, +CHA, −free flaw. Shadow-touched: Fetchling Magic innate spells.
Fetch Step teleport-step ability. Excellent for shadow-flavored or arcane builds.
Best for: Rogue, Magus, Psychic, Sorcerer, Swashbuckler.

**[18] Gnoll (Kholo)** — HP +8 | Speed 25 | Darkvision
+STR, +CON, −free flaw. Jaws unarmed attack (d6 piercing). Pack Attack
bonus damage when flanking. Prey Seeker for tracking. Strong and brutal.
Best for: Barbarian, Fighter, Ranger, Guardian, Monk.

**[19] Grippli** — HP +6 | Speed 25 | Low-light vision
+DEX, +WIS, −STR. Small frog-folk. Tongue attack (reach 10 ft, free action
to grab). Grippli Magic gives innate spells. Sticky tongue for disarming.
Best for: Monk, Ranger, Druid, Rogue, Kineticist.

**[20] Nagaji** — HP +8 | Speed 25 | Low-light vision
+STR, +CON, −INT. Scales provide natural armor. Serpent's Venom adds
poison bite. Hardy against mental effects. Imposing presence.
Best for: Champion, Fighter, Guardian, Barbarian, Oracle.

**[21] Anadi** — HP +8 | Speed 25 | Darkvision
+DEX, +WIS, −CON. Spider-folk who appear human. Change Shape (human form).
Web feat to immobilize targets. Fangs unarmed attack with poison.
Best for: Druid, Ranger, Rogue, Animist, Witch.

**[22] Automaton** — HP +10 | Speed 25 | Darkvision + low-light
+STR, +CON, −free flaw. Construct: immune to death effects, disease,
poison, sleep, and paralysis. No food/water/air needed. Excellent tank base.
Best for: Guardian, Fighter, Champion, Barbarian, Kineticist.

**[23] Azarketi** — HP +8 | Speed 20 (swim 30) | Low-light vision
+STR, +CON, −free flaw. Aquatic and amphibious. Hydraulic Deflection grants
AC bonus. Excellent in any campaign near water; viable anywhere.
Best for: Kineticist (water), Fighter, Guardian, Ranger, Monk.

**[24] Poppet** — HP +6 | Speed 25 | Low-light vision
+CON, +CHA, −STR. Small construct, immune to poison/disease/sleep. Takes
half damage from falling. Stuffed (fire resistance). Cheerful and durable.
Best for: Bard, Sorcerer, Oracle, Witch, Cleric.

**[25] Fleshwarp** — HP +10 | Speed 25 | Darkvision
+STR, +CON, −free flaw. Aberrant Form gives intimidating appearance.
Unusual Anatomy provides natural armor. Strong for horror-flavored builds.
Best for: Barbarian, Guardian, Fighter, Kineticist, Oracle.

**[26] Vanara** — HP +8 | Speed 25 (climb 15) | Low-light vision
+DEX, +WIS, −free flaw. Prehensile tail can hold items. Forest-born gives
Nature proficiency. Brachiation for fast tree movement.
Best for: Monk, Ranger, Druid, Rogue, Swashbuckler.

**[27] Aasimar** — HP +8 | Speed 25 | Darkvision
+CON or +CHA, free boost. Celestial bloodline grants resistance (acid/cold/electricity/fire,
pick one). Scion of Divinity adds innate divine spells. Celestial Eyes for darkvision.
Best for: Champion, Cleric, Oracle, Sorcerer (angelic bloodline), any holy warrior.

**[28] Tiefling** — HP +8 | Speed 25 | Darkvision
+CON or +INT, free boost. Fiendish bloodline grants resist fire 5. Hellfire Breath adds
an innate fire spell. Fiend Eyes for darkvision. Strong for dark or morally complex builds.
Best for: Sorcerer (demonic), Oracle, Witch, Rogue, Warpriest Cleric.

---

## STEP 4 — HERITAGE SELECTION

> **DM:** ⛔ Load BOTH `KM_Ancestries.md` (core + uncommon + Goliath) AND `KM_Ancestries.md` (rare + versatile). Find the player's ancestry section in whichever file it lives in. Copy-paste the full heritage block verbatim — do NOT skip heritages or describe them from memory. Every listed heritage is a legal pick. Offer Versatile Heritage (`versatile` → KM_Ancestries.md § VERSATILE HERITAGES) as an alternative. Wait for player pick, record `player.heritage` + `player.heritage_source` + `player.heritage_granted_features[]` in the save block. Missing the step entirely = `.fail 9`. Fabricating a heritage name or effect = `.fail 9`.

**Player input forms:**
- A number from the ancestry's heritage list (e.g., `3` under Elf = Cavern Elf)
- `versatile` → display the 8 Versatile Heritage options, wait for pick
- Typing a heritage name directly (e.g., `Ancient Elf`, `Nephilim Celestial`) — accept if valid

**After pick:** confirm the heritage effect in one sentence, then proceed to Step 5.

---

## STEP 5 — BACKGROUND SELECTION

> **DM:** ⛔ Load `KM_Ancestries.md`. Copy-paste the compact screen exactly (42 entries, numbered 1–42). Wait for player pick, record `background`. Do NOT display from memory or generate from system knowledge. Missing entries = `.fail 9`.

---

## STEP 5.5 — ABILITY BOOSTS + L1 FEATS

> **DM:** Once ancestry + background + class are confirmed, assemble stats and present L1 feats.

**Boost sources:** Ancestry ×2 | Background ×2 | Class ×1 (key stat) | Free ×4 (no cross-source cap; only restriction: within one source, no double-boosting the same stat)

Output VERBATIM:
```
ABILITY BOOSTS — [Character]
Locked: Ancestry (+[A,B]) | Background (+[C,D]) | Class (+[E])
Free ×4: each free boost must go to a different stat (no repeats within free boosts).
Before free: STR [X] DEX [X] CON [X] INT [X] WIS [X] CHA [X]
Type: ASSIGN [stat] [stat] [stat] [stat]
```
Record `player.stats{}` after confirmation.

**Language Pick** (if ancestry grants a player-chosen bonus language):
> **DM:** Humans always get 1 bonus language beyond Common (PF2e Remaster rule). Present the menu below — do NOT ask an open text question. Record the pick, then proceed to L1 Feats.

```
LANGUAGE SELECTION
════════════════════════════════════════════════
Your ancestry grants 1 bonus language beyond Common.
Choose one (type a number or the name):

 [1]  Hallit       — Kellid warrior tongue; Brevoy and River Kingdoms region
 [2]  Skald        — Old Iobarian; ancient language of the Stolen Lands
 [3]  Sylvan       — Language of fey; essential in the Stolen Lands
 [4]  Jotun        — Language of giants; thematic for Giant Instinct builds
 [5]  Draconic     — Dragon and arcane scholarship language
 [6]  Elven        — Scholarly, arcane, and forest tradition
 [7]  Dwarven      — Underground civilizations and forge tradition
 [8]  Orcish       — Orcish clans and northern barbarian tribes
 [9]  Goblin       — Goblin tribes and some fey-adjacent groups
[10]  Varisian     — Wanderer tongue; widely spoken across Avistan
[11]  Gnomish      — Gnome language; useful for fey interaction
[12]  Undercommon  — Spoken by underground civilizations

Type a number (1–12) or any valid PF2e language name.
════════════════════════════════════════════════
```
Record `player.languages[]`: Common + [chosen] + INT mod additional languages (only if INT mod > 0).

**L1 Feats** (after stats and language): Ancestry feat → load `KM_Ancestries.md` L1 list, wait, record `player.ancestry_feat`. Background skill feat → auto-granted by background, state it, record `player.background_skill_feat`. Class feat (L1) → preset = build file L1 row (SWAP to override); custom = present options; record `player.class_feat_1`.

---

## STEP 6 — DEITY (divine / nature classes only)

> **DM:** Run this step only if the player's class has a deity slot.
> **Mandatory:** Cleric, Champion. **Optional (offer, accept `none`):** Druid, Oracle, Animist, Exemplar, Monk. **Skip entirely:** all other classes.
> After pick, record `player.deity`. For Cleric, also pick **2 domains** from the deity's domain list.

```
══════════════════════════════════════════════════════════════
CHOOSE YOUR DEITY — Kingmaker-relevant patrons
══════════════════════════════════════════════════════════════
 [1]  Erastil        — Huntsman, community, family. Kingmaker's patron saint.
 [2]  Abadar         — Law, cities, wealth. Popular in Restov and Brevoy.
 [3]  Iomedae        — Justice, honor, valor. Aldori noble tradition.
 [4]  Gorum          — War, strength, strife. Sword-arm deity.
 [5]  Sarenrae       — Sun, healing, redemption. Forgiving but firm.
 [6]  Desna          — Stars, travel, luck. Patron of wanderers.
 [7]  Shelyn         — Beauty, love, art. Peaceful path.
 [8]  Torag          — Dwarves, forge, protection. Stronghold guardian.
 [9]  Cayden Cailean — Freedom, ale, bravery. Drunken hero god.
 [10] Pharasma       — Death, fate, birth. Neutral arbiter.
 [11] Gyronna        — Hate, spite (uncommon — GM approves case by case).
 [12] Nethys         — Magic in all forms. Arcane scholar's choice.
Type 1–12, CUSTOM (any Golarion deity), or NONE (optional classes only).
══════════════════════════════════════════════════════════════
```

---

## STEP 7 — SKILL CHOICES

> **DM:** Every class grants trained skills. Some are fixed by the class; the rest are player choice. Present this step AFTER deity (if any) and BEFORE weapon.

```
══════════════════════════════════════════════════════════════
SKILL PICKS — [Class]
══════════════════════════════════════════════════════════════
Your class grants: [list fixed class-granted skills, e.g. "Athletics (Barbarian)"]
You pick [N + INT mod] additional trained skills from the PF2e skill list:
  Acrobatics, Arcana, Athletics, Crafting, Deception, Diplomacy,
  Intimidation, Lore (pick a subject), Medicine, Nature, Occultism,
  Performance, Religion, Society, Stealth, Survival, Thievery

  [K] KEEP build defaults — use the skills listed in your build file
  [S] SWAP — pick your own trained skills
  [?] Show me build recommendations (picks come from ANY PF2e skill — no class restriction)
Type K, S, or ?.
══════════════════════════════════════════════════════════════
```

**Pick counts per class (trained skills beyond class-fixed + INT mod):**
- Rogue: 7  |  Investigator, Bard, Ranger, Thaumaturge: 4
- Most classes: 3  |  Fighter/Champion/Cleric/Guardian: 3
- Wizard/Witch: 2 (INT mod carries them higher)

Record `player.skills_trained[]` in save block.

---

## ★ TIPS FOR NEW PLAYERS

> **DM:** Show this section if the player indicates they are new to PF2e or RPGs.

```
BEFORE YOU PICK — THINGS WORTH KNOWING

1. YOU CAN'T GO WRONG
   Every class has strong builds. There are no trap choices in this system.
   Pick what sounds fun. Mechanical optimization matters less than engagement.

2. ROLE GUIDANCE
   — Want to hit things reliably?     → Fighter, Barbarian, Guardian
   — Want to support your party?      → Bard, Cleric, Commander
   — Want to cast spells + fight?     → Magus, Champion, Oracle
   — Want versatility + skills?       → Rogue, Ranger, Investigator
   — Want to blow things up?          → Kineticist, Sorcerer, Wizard
   — Want something unusual?          → Summoner, Thaumaturge, Animist

3. ANCESTRY DOESN'T MAKE OR BREAK YOU
   The +2 stat boosts matter less than you think at level 1.
   Pick an ancestry that fits the character you want to play.
   Human is never wrong. Orc + Barbarian is deeply satisfying.

4. BACKGROUND MATTERS FOR STORY
   The mechanical difference between backgrounds is small.
   The narrative difference is large — your background shapes how
   NPCs respond to you and which quests feel personal.

5. YOUR WEAPON IS YOUR IDENTITY
   More than almost anything else, players remember their weapon.
   Pick one you'll want to describe in combat. It shows up in narration.

6. YOU CAN CHANGE YOUR MIND
   Builds can be adjusted between sessions if something isn't working.
   The system supports experimentation.
```

---

## STEP 10 — FINAL CONFIRMATION (.status panel)

> **DM:** Output this full block after all choices are confirmed.

```
CHARACTER CONFIRMED — [Name]
CLASS: [class] | Build: [build] | Ancestry: [X] | Heritage: [X] | Background: [X]

ABILITY SCORES: STR [X] DEX [X] CON [X] INT [X] WIS [X] CHA [X]
  Sources: Ancestry (+[X,X]) | Background (+[X,X]) | Class (+[X]) | Free (+[X,X,X,X])

FEATS (L1)
  Ancestry feat:         [name] — [effect]
  Background skill feat: [name] — [effect]
  Class feat (L1):       [name] — [effect]

HP: [base]+[CON mod]+[ancestry] = [total]  |  AC: 10+[armor]+[DEX cap]+3 = [total]
LANGUAGES: Common | [ancestry lang] | [INT bonus langs, if INT mod >0]
TRAINED SKILLS: [Skill] +[rank+mod] = +[total]  (list all trained)
WEAPON: [X] | ARMOR: [X] | DEITY: [X or none]
```
→ Proceed to Pick-10 companion selection (Bootstrap STEP 3).

*KM_CharCreate.md — Kingmaker PF2e Text Adventure | Guided Character Creation v1.1*
*27 classes | 28 ancestries | 42 backgrounds (KM_Ancestries.md) | Tips included*

*KM_CharCreate.md — Kingmaker PF2e Text Adventure | Char Create Part B v1.0*


---

<!-- merged from KM_CharCreate.md (v93.21 file consolidation) -->

﻿# KINGMAKER — BUILD SETUP (8-PROMPT SEQUENCE)
## KM_CharCreate.md | Referenced by: KM.txt Step 2, KM_Builds.md headers

> **⛔ DM: After the player confirms class + build, you MUST run ALL 8 prompts
> below IN STRICT NUMERIC ORDER (1 → 2 → 3 → 4 → 5 → 6 → 7 → 8). Output each
> prompt VERBATIM. STOP after each. WAIT for input. Do NOT combine. Do NOT
> skip. Do NOT auto-select defaults. Do NOT reorder. Skipping or reordering
> any prompt = `.fail 3` (agency violation) + `.fail 9` (file content ignored).**

> **Purpose:** The build file lists defaults for ancestry / heritage / weapon /
> armor / stats / skills / deity / background. Without these prompts, the DM
> treats the default as final and strips the player's right to customize.
> These 8 prompts restore that right — ancestry, heritage, stat, weapon,
> armor, deity, background, and skills.

> **⛔ HERITAGE IS A SEPARATE STEP (Prompt 2).** It is NOT a sub-question of
> Prompt 1 (Ancestry). Even if the Ancestry table suggests a heritage in its
> "Heritage" column, the player must explicitly confirm or choose a heritage
> in Prompt 2. Skipping Prompt 2 = `.fail 3`.

> **⛔ BACKGROUND COMES BEFORE SKILLS (Prompt 7 before Prompt 8).** Background
> grants a fixed trained skill + Lore skill which must be locked before the
> player picks remaining class skills. Running Skills before Background = `.fail 3`.

---

## ⛔ MANDATORY CHECKLIST BLOCK (every BuildSetup response)

Every response that runs a BuildSetup prompt MUST open with this exact
checklist block at the TOP of the response (before the prompt itself):

```
═══ BUILDSETUP CHECKLIST ═══
[✓]  1. Ancestry          → recorded: [value or "—"]
[✓]  2. Heritage          → recorded: [value or "—"]
[✓]  3. Stat Priority     → recorded: [value or "N/A locked" or "—"]
[→]  4. Weapon            → IN PROGRESS (this prompt)
[ ]  5. Armor             → pending
[ ]  6. Deity             → pending (or "N/A — no deity slot")
[ ]  7. Background        → pending
[ ]  8. Skills            → pending
─── post-prompt sequence (MUST run before save block) ───
[ ]  9. Setup Assembly    → boosts, feats, HP/AC, languages, skill mods
[ ] 10. Starting Gear     → KM_BuildGuide.md screen (A/B/C). Skipping = .fail 41
[ ] 11. Pick-5 OPEN POOL → Pick 5 of 10 candidates (A–E + G–K: Hu Tao/Keqing/Leliana/Yor Forger/Aerith / Amiri/Valerie/Harrim/Linzi/Jaethal; slot F retired — Velvet removed). No alignment gate. If Linzi (J) not picked → run LINZI-REPLACEMENT prompt. QL 7 join at quest triggers
         NOTE — C (Leliana NEW_003): can fill Linzi's chronicler role — see Good-alignment gate at Manor arrival (KM_PR_01_manor_arrival.md)
[ ] 12. Seekers (HARDCODED)      → Bellatrix Lestrange, Revy, Satsuki Kiryūin, Velvet Crowe, Atalanta Alter (no pick; flip via Diplomacy DC 10 in Ch1)
[ ] 13. Save Block               → USE KM_SaveBlock_Template.md (EXHAUSTIVE MODE) — ONLY AFTER 11 recorded
[ ] 14. Chapter Select           → KM_ChapterSelect.md screen
════════════════════════════
```

**Marker rules:**
- `[✓]` = prompt complete, value locked. Show recorded value after `→`.
- `[→]` = the prompt this response is running RIGHT NOW. Exactly one per response.
- `[ ]` = pending. Show "pending" or "N/A — [reason]" if skip-applicable.
- `[✗]` = explicitly skipped per spec (e.g. Prompt 3 on STR-locked Barbarian, Prompt 6 on non-divine class). Show reason.

**STOP footer (also mandatory at END of every prompt response):**
```
⛔ STOP — DO NOT ADVANCE. Awaiting player input for Step [M].
⛔ DO NOT auto-select. DO NOT skip ahead.
⛔ Steps remaining after this one: [list, e.g. 5-Armor, 6-Deity, 7-Background, 8-Skills, 9-Assembly, 10-Pick10, 11-Pick5, 12-SaveBlock, 13-Chapter]
⛔ Save Block does NOT generate until Step 11 (Pick-5 open pool + Linzi-replacement gate if needed) is recorded.
⛔ Prologue does NOT begin until Step 13 (Chapter Select) is chosen.
```

**Why this exists:** the DM has historically jumped from Prompt 3 directly to
companion selection or save block, skipping Weapon/Armor/Deity/Background.
A visible checklist at the top of every response forces the DM to track
every step. If the checklist shows `[ ] 5. Armor → pending` but the next
response narrates the prologue, the skip is immediately visible.

**Violations:**
- Missing checklist block at top of response = `.fail 41`
- Missing STOP footer = `.fail 41`
- More than one `[→]` marker, or no `[→]` marker = `.fail 41`
- Marking a step `[✓]` that was never actually run = `.fail 41` + `.fail 3`
- Advancing past the `[→]` step without recording player input = `.fail 41` + `.fail 3`
- Jumping the `[→]` marker forward by more than 1 (e.g. from 3 to 7) = `.fail 41` + `.fail 3`
- Outputting Save Block (Step 12) before Steps 10 + 11 are `[✓]` = `.fail 9` (broken-seed save) + `.fail 41`
- Beginning prologue narration before Step 13 is `[✓]` = `.fail 3` + `.fail 41`

**Recovery:** reprint the earliest unfinished prompt with corrected checklist.
Never combine prompts. Never shorten. Corrections are additive.

**Player override:** type `.checklist` to force the DM to reprint the
checklist block showing current state.

---

## 🔤 INPUT MATCHING (applies to every numbered list in this file)

For any prompt that shows a numbered list (ancestry, heritage, weapon, armor,
background, skill, deity), the DM accepts ALL of the following as valid input:

1. **Numbers** — `1`, `2`, `3`, …
2. **Full names** — `Versatile Human`, `Ancient-Blooded`, `Whipfang`
3. **Unique prefixes** (case-insensitive) — the shortest input that
   uniquely identifies one option in the **current menu**:
   - `V` → Versatile Human (if no other "V" option is on the menu)
   - `Anc` → Ancient-Blooded
   - `Conr` → Conrasu
   - `Whip` → Whipfang
4. **Ambiguous prefixes** — DM lists the matches and re-asks; never
   auto-picks. Example: `H` with both "Human" and "Halfling" on the menu →
   *"Did you mean Human or Halfling?"*

⛔ **Never expand a prefix to an option not on the current menu.** `V` →
Versatile Human is correct when Versatile Human is listed; `V` → Vanara
(when Vanara is not on the current menu) = `.fail 9` (fabricated selection).

⛔ **Capitalization is irrelevant.** `v`, `V`, `vers`, `Versatile`,
`VERSATILE HUMAN` all match Versatile Human.

---

## ⛔ PROMPT 1 — ANCESTRY CONFIRMATION

**⛔ IGNORE the A/B/C template in the build file header — it is outdated.**
Use the **Race Options table** in the current build (the 10-row numbered table
below the stat block). Output VERBATIM:

```
════════════════════════════════════════════
ANCESTRY — [Build Name]
Default: [★1 row from Race Options table]

All options (pick any — ranked by fit, not restricted to this list):
  [copy Race Options table rows 1–10 verbatim, # | Ancestry | Heritage | Why]

INPUT — accept ANY of these:
  • Number 1–10 from the list above
  • Full ancestry name (e.g. `Goliath`, `Human`)
  • Unique prefix, case-insensitive (e.g. `Hum` → Human; `G` → Goliath if no
    other "G" ancestry is on the list; `Conr` → Conrasu)
  • Any PF2e ancestry name not on the list (table is guidance, not restriction)

⛔ DM MUST resolve unique prefixes. Rejecting `Hum` when only "Human" starts
   with H on the current list = `.fail 3` + `.fail 9`. The match is required.
════════════════════════════════════════════
```
STOP. Wait for input. Player may pick any ancestry — the table is ranked
guidance, not a restriction. Apply the HP / speed adjustments from the build
file header (ANCESTRY BASE HP, SPEED, HEIGHT). **Heritage is NOT chosen here
— proceed to PROMPT 2.**

---

## ⛔ PROMPT 2 — HERITAGE

**RUN THIS PROMPT FOR EVERY ANCESTRY.** Heritage is a discrete PF2e character
creation step — never bundle into Prompt 1, never auto-select the table's
suggested heritage, never skip. Look up the chosen ancestry's heritage list
in `KM_Ancestries.md` and output the canonical heritage table verbatim.

Output VERBATIM:
```
════════════════════════════════════════════════════════════
HERITAGE — [Ancestry] ([Build Name])
The Race Options table suggested: [Heritage from P1 table row, if any] (★)

All [Ancestry] heritages (pick any — the suggestion is guidance only):
  [copy the ancestry's full heritage list from KM_Ancestries.md verbatim,
   numbered. Each row: # | Heritage | Effect (one line)]

INPUT — accept ANY of these:
  • Number from the list above (e.g. `2`)
  • Full heritage name (e.g. `Versatile Human`)
  • Unique prefix, case-insensitive (e.g. `V` → Versatile Human if no other "V"
    heritage is on the list; `Skil` → Skilled Human; `Anc` → Ancient-Blooded)
  • `?` for more detail on a heritage
  • `VERSATILE` (uppercase) to see cross-ancestry Versatile Heritages submenu

⛔ DM MUST resolve unique prefixes. Rejecting `V` when only "Versatile Human"
   starts with V on the current list = `.fail 3` (forced verbose input) +
   `.fail 9` (ignored explicit input rule). The match is required, not optional.
════════════════════════════════════════════════════════════
```
STOP. Wait for input. Record `player.heritage`. Apply heritage effects
(extra feat, extra skill, vision change, resistance, etc.) — most heritages
do NOT change HP / speed / stat array, but a few do (e.g. Hill Dwarf +1 HP
already included in dwarf base; Half-Elf grants Low-Light Vision; Versatile
Human grants 1 extra general feat at L1; Skilled Human grants 1 extra
trained skill at L1). Update the stat block accordingly.

⛔ **HERITAGE VERIFY — MANDATORY before advancing to Prompt 3.**
Output this line verbatim (values from KM_Ancestries.md — NOT from training data):
`HERITAGE CONFIRMED: [Ancestry] → [Heritage Name] | [one-line effect]`
Wrong or fabricated heritage = `.fail 9`. Skipping this line = `.fail 41`.

Proceed to PROMPT 3.

---

## ⛔ PROMPT 3 — STAT PRIORITY (primary attack stat)

**RUN THIS PROMPT ONLY IF the build's class supports both STR and DEX as
primary attack stats.** Classes where swap is legal:
  Fighter, Ranger, Magus, Monk, Rogue, Swashbuckler, Investigator,
  Champion (Liberator/Redeemer DEX viable), Thaumaturge, Inventor.

For STR-locked (Barbarian, Guardian) or DEX-locked (Gunslinger) or
casting-stat-locked (full casters) builds, **SKIP this prompt and say:**
*"This build's primary stat is locked to [X]. Proceeding to Prompt 4."*

Otherwise output VERBATIM:
```
════════════════════════════════════════════
STAT PRIORITY — [Build Name]
Default primary: [STR or DEX]
  [S] STR primary — [one-line effect, e.g. "heavy armor, maul 1d12"]
  [D] DEX primary — [one-line effect, e.g. "light armor, rapier 1d6 finesse"]
Type S or D.
════════════════════════════════════════════
```
STOP. Wait for S or D. Swap the stat array (primary ↔ secondary attack stat)
if player chose the non-default. Proceed to PROMPT 4.

---

## ⛔ PROMPT 4 — WEAPON CHOICE

Look up the build's class/build row in KM_BuildGuide.md CLASS → WEAPON CATEGORY table
to find its category (A–H). Then display that category's FULL weapon list verbatim from
KM_BuildGuide.md WEAPON CATEGORIES. Do NOT generate a truncated subset.

⛔ **WEAPON CATEGORY VERIFY — MANDATORY before showing the weapon list.**
Output this line verbatim (values from KM_BuildGuide.md CLASS → WEAPON CATEGORY table):
`WEAPON CATEGORY: [Class/Build] → Category [X] | [N] weapons in category | source: KM_BuildGuide.md`
Wrong category = `.fail 9`. Skipping this line = `.fail 41`.

Place the build's default weapon at [1] (marked ★ BUILD DEFAULT). Remaining entries are
the category list in order. Add a Custom option as the final numbered entry.

⛔ **THE BUILD DEFAULT IS ALWAYS [1]. It is NEVER outside the numbered list. It is NEVER
presented as a typed-input option ("type GUISARME", "type the weapon name", etc.).
It is entry [1] in the numbered menu. Full stop. No exceptions.**

⛔ **WEAPON MENU FORMAT LOCK — numbered list only. Every entry must be:**
`[N] Weapon Name — [dice] [type] [traits]`
No sub-headers, no unnumbered bullets, no prose lists, no mixed format.
"Type the weapon name" prompts = `.fail 3`. Any non-numbered weapon entry = `.fail 3`.
Build default outside the numbered list = `.fail 3`.
If the player types a name instead of a number, treat it as Custom and confirm.

After player picks, update the build's Weapon line in the stat block.
Proceed to PROMPT 5.

## ⛔ PROMPT 5 — ARMOR CHOICE

COPY-PASTE the armor table from KM_BuildGuide.md STEP 2.6 EXACTLY AS WRITTEN.
DO NOT generate from PF2e training data — stats differ from core rules.
Omitting Dragon Plate, using wrong AC values, or fabricating entries = .fail 9.
Entry count = 11 (options 0–10). Showing fewer = .fail 9.

Filter by class proficiency (Dragon Plate #10 ALWAYS shown — see ⚠️ below):
- Light-only (Rogue/Bard): show 0–6, 10
- Medium (Barbarian/Ranger/Druid): show 0–6, 10
- Heavy (Fighter/Champion/Guardian): show 0–10
- Unarmored (Monk/Sorcerer/Wizard): show 0, 10, Custom only

⚠️ **DRAGON PLATE (#10) is PC-LOCKED to eRmaC and OVERRIDES class armor proficiency.** Shown to every class, no exceptions. Hiding it = `.fail 9`. Aerynth-origin artifact grants its own trained-Heavy proficiency to eRmaC. Full rule: KM_BuildGuide.md § DRAGON PLATE NOTE.

⛔ **ARMOR VERIFY — MANDATORY after player picks.**
Output this line verbatim (values from KM_BuildGuide.md STEP 2.6 — NOT from training data):
`ARMOR CONFIRMED: [Armor Name] | AC bonus +[X] | DEX cap [Y or "—"] | Check penalty [Z or "—"] | source: KM_BuildGuide.md`
Wrong stats = `.fail 9`. Skipping = `.fail 41`.

After player picks, recompute AC: 10 + armor bonus + DEX (capped) + proficiency (+3 at L1: rank 2 + level 1).
Update the stat block. Proceed to PROMPT 6.

## ⛔ PROMPT 6 — DEITY (divine/nature classes only)

**RUN THIS PROMPT ONLY IF the build's class is in the Mandatory or Optional list below.**
- **Mandatory** for: Cleric, Champion, Warpriest Cleric, Paladin (Champion: Iomedae/etc.)
- **Optional** for: Druid, Oracle, Animist, Exemplar, Monk
- **SKIP for ALL other classes** — including Barbarian, Fighter, Ranger, Rogue,
  Wizard, Sorcerer, Bard, Magus, Gunslinger, Inventor, Investigator, Kineticist,
  Psychic, Summoner, Swashbuckler, Thaumaturge, Witch, Commander, Guardian.
  Say *"No deity slot for [class]. Skipping to Prompt 7."* and PROCEED IMMEDIATELY.
  Do NOT show a deity menu with an optional/none option. Do NOT offer flavor picks.
  Showing a deity menu for a skip-class = `.fail 41`.

Output VERBATIM:
```
════════════════════════════════════════════════════════════
DEITY — [Build Name]
Kingmaker-relevant deities (pick one or type CUSTOM for any other):
  [1]  Erastil        — Huntsman, community, family. Kingmaker's patron saint.
  [2]  Abadar         — Law, cities, wealth. Popular in Restov and Brevoy.
  [3]  Iomedae        — Justice, honor, valor. Aldori noble tradition.
  [4]  Gorum          — War, strength, strife. Sword-arm deity.
  [5]  Sarenrae       — Sun, healing, redemption. Forgiving but firm.
  [6]  Desna          — Stars, travel, luck. Patron of wanderers.
  [7]  Shelyn         — Beauty, love, art. Peaceful path.
  [8]  Torag          — Dwarves, forge, protection. Stronghold guardian.
  [9]  Cayden Cailean — Freedom, ale, bravery. Drunken hero god.
  [10] Pharasma       — Death, fate, birth. Neutral arbiter.
  [11] Gyronna        — Hate, spite (uncommon — GM approves case by case).
  [12] Nethys         — Magic in all forms. Arcane scholar's choice.
Type 1–12 or CUSTOM.
════════════════════════════════════════════════════════════
```
STOP. Wait for selection. Record `player.deity`. For Cleric: also load the
deity's **domain list** (2 picks) from AoN or KM_Spells.md.
For Champion: also record the Cause (Paladin/Redeemer/Liberator) — this
may already be in the build file; if not, ask. Proceed to PROMPT 7.

---

## ⛔ PROMPT 7 — BACKGROUND

⛔ READ KM_Ancestries.md DIRECTLY BY FILENAME. OUTPUT ITS TABLE VERBATIM.
Do NOT search by content keywords — search truncates and you will fabricate
the gaps. Do NOT reconstruct from training data. Use the Read tool with the
exact filename. Paste the table. Mark the build's default entry with ★.

⛔ SENTINEL CHECK before posting your output:
   Entry [ 1] must be: Borderlands Pioneer  (NOT Acolyte — that's CRB-order
                                              fabrication)
   Entry [ 8] must be: Acolyte               (first CRB entry)
   Entry [22] must be: Field Medic
   Entry [42] must be: Warrior               (final entry — if your table does
                                              NOT end here, you fabricated)
   All four sentinels must match. Wrong boosts, missing entries, fabricated
   names, "..." or "etc.", or skipped numbers = .fail 9. Re-Read and re-post.

After player picks, look up full entry in KM_Ancestries.md or KM_Ancestries.md.
Record player.background, player.background_skills[], player.background_skill_feat.

⛔ **BACKGROUND SKILL VERIFY — MANDATORY before advancing to Prompt 8.**
Output this line verbatim (values from KM_Ancestries.md — NOT from training data):
`BACKGROUND CONFIRMED: [Background Name] = [Stat1]/[Stat2] | [Skill] + [Lore] | [Skill Feat]`
If training data and the file disagree, the file is authoritative.
Wrong or fabricated skills = `.fail 9`. Skipping this line = `.fail 41`.

Proceed to PROMPT 8 (Skills).

**Every background grants:** 2 ability boosts | 1 trained skill + 1 Lore skill | 1 skill feat

---

## ⛔ PROMPT 8 — SKILL CHOICES

Every class auto-trains the player in 1 fixed skill (sometimes 2). The
player then picks N additional trained skills, where N = class base + INT
mod. **Those N picks come from ANY skill in PF2e — not a "class list".**
Background grants 1 trained skill + 1 Lore skill on top of that. The build
file shows DEFAULT picks. Ask whether to keep or swap.

⛔ **NO CLASS SKILL LIST RESTRICTION (PF2e Remaster).** Not PF1. Free picks
come from ANY PF2e skill — Medicine, Thievery, Religion, Performance, etc.
are legal for any class. Per-class list below = AUTO-TRAINED only, not a
pick restriction. Rejecting "Medicine not on Fighter list" = `.fail 9` + `.fail 38`.

⛔ **SKILL COUNT VERIFY — output this line BEFORE presenting the skill menu:**
`SKILL COUNT: [class] base [N] + INT [±X] = [Y] | [background] [skill] overlap → [+1 or none] | free picks = [total] | Warfare/other Lore = locked separately`
Wrong free pick count = `.fail 6`. Skipping this line = `.fail 41`.
Example (Barbarian + Warrior, INT +0): `SKILL COUNT: Barbarian base 3 + INT 0 = 3 | Warrior Athletics overlap → +1 | free picks = 4 | Warfare Lore = locked`

**Skill count formula:**
  Total trained skills = (class base + INT mod) + 1 background skill + 1 background Lore skill
  Example: Fighter INT +0 with Warrior background = 3 + 0 + 1 (Athletics) + 1 (Warfare Lore) = 5

⛔ **OVERLAP RULE — MANDATORY (apply BEFORE counting free picks):**
If the background's trained skill duplicates a class-LOCKED skill, the redundant
grant **converts to +1 free class pick**. The Lore skill is unaffected (always
granted on top). DM must apply this every time — silently dropping the bonus
pick = `.fail 6`. "Already covered, no bonus" is the wrong answer.

  ► Barbarian + Warrior (Athletics overlap): Barbarian locks Athletics;
    Warrior grants Athletics + Warfare Lore. Athletics overlap → +1 free pick.
    INT +0: Athletics (locked) + **4 free class picks** + Warfare Lore = 6 trained.
    Free picks = 3 (base) + 1 (overlap) = **4, not 3.**
    Asking for only 3 free picks here = `.fail 6`.

  ► Magus + Scholar/Arcana: Arcana overlap → +1 free pick (4 total at INT +0).
  ► Cleric + Acolyte: Religion overlap → +1 free pick.
  ► Ranger + Hunter: Nature overlap → +1 free pick.
  ► Wizard + Scholar/Arcana: Arcana overlap → +1 free pick.
  ► Champion + Acolyte: Religion overlap → +1 free pick.

⛔ **DM ANTI-FLIP RULE:** Once the player commits to N free picks based on the
overlap formula, do NOT recount mid-prompt and demand a different N. If you need
to recount, explain the math first; don't silently flip the number. Flipping
the skill count back-and-forth across turns = `.fail 6` + `.fail 33`.

Output VERBATIM:
```
════════════════════════════════════════════════════════════
SKILLS — [Build Name]
Class auto-trains:  [fixed-grant skill(s), e.g. "Athletics (Fighter)"]
Free picks:         [N + INT mod] from ANY PF2e skill (see list below)
Background grants:  1 trained skill + 1 Lore skill ([Background] = [Skill] + [Lore])
Total trained:      [N + INT mod + 2 + class auto-grant]
Build's default:    [list from build file]

All PF2e skills (pick freely from this list for the [N + INT mod] free picks):
  Acrobatics · Arcana · Athletics · Crafting · Deception · Diplomacy
  Intimidation · Lore (any subject) · Medicine · Nature · Occultism
  Performance · Religion · Society · Stealth · Survival · Thievery
(Perception is auto-trained for everyone — not a pick.)

  [K] KEEP defaults — proceed with the skills above
  [S] SWAP — pick your own [N + INT mod] free skills from ANY skill above
  [?] Show me build recommendations before deciding
Type K, S, or ?.
════════════════════════════════════════════════════════════
```
STOP. Wait for selection.
- **K:** record the build's default skills in `player.skills_trained[]`. Proceed.
- **S:** wait for player to name [N + INT mod] skills FROM ANY PF2e SKILL.
  Do NOT reject picks for being "not on the class list" — no such list exists.
  Background-granted skills and class auto-grants are already locked. Record all.
- **?:** display the build file's recommendations + rationale, then re-present K/S.

**Background skill grants (common backgrounds):**
- Warrior: Athletics (or Intimidation) + Warfare Lore
- Scholar: choose from Arcana/Nature/Occultism/Religion/Society + Lore of field
- Guard: Intimidation + Legal Lore or Guild Lore
- Acolyte: Religion + a deity-appropriate Lore
- Criminal: Stealth + Underworld Lore
- Hunter: Nature + Terrain Lore (chosen)
- (other backgrounds: check KM_Ancestries.md for skill grants)

**Class AUTO-TRAINED skills (fixed-grant only — NOT a restriction on free picks):**
- Alchemist: Crafting  |  Barbarian: Athletics  |  Bard: Occultism, Performance
- Champion: Religion  |  Cleric: Religion + domain  |  Druid: Nature (+order)
- Fighter: Acrobatics OR Athletics  |  Gunslinger: Stealth, Crafting
- Guardian: Athletics  |  Investigator: methodology  |  Magus: Arcana, Athletics
- Monk: (none)  |  Ranger: Nature, Survival  |  Rogue: Stealth (7 free picks)
- Sorcerer: bloodline  |  Thaumaturge: Occultism  |  Witch: Occultism (+patron)
- Wizard: Arcana  |  (other classes: see KM_Builds.md)

Free pick count = **3 + INT mod** most classes; **7 + INT** Rogue;
**2 + INT** Wizard/Witch. Skill proficiencies auto-advance per leveling map.

---

## ⛔ AFTER ALL 8 PROMPTS — SETUP ASSEMBLY

Output ALL of the following in a single response:

**① ABILITY BOOSTS — L1 STAT ASSEMBLY**

Total boosts at L1 = 9, each +2 (below 18). Sources:
  Class key: 1 fixed.
  Background: 2 (1 from 2-stat menu + 1 free — MUST be different stats).
  Ancestry: 2 (Human/Half-Elf/Half-Orc/Versatile = both free; others = 2 fixed or 1 fixed + 1 flaw + 1 free). Both ancestry boosts MUST be different stats.
  Standard free: 4 — **MUST go to 4 DIFFERENT attributes.** Cannot stack 2+ standard free into same stat. `.fail 6` if accepted.
No double-boost within a single source. Each boost = +2 (NOT +1). 10→12→14→16→18.
**HARD 18 CAP at L1.** No stat exceeds 18 at creation. Boost above 18 = REJECTED at validation; player re-picks. Not capped to +1.
+1 per boost = `.fail 6`. STR 19+ at L1 = `.fail 6` + `.fail 38`.

⛔ **COMPUTE N BEFORE OUTPUT.** N = bg menu pick (1) + bg free + ancestry free + standard 4. Human + flex-bg classes: N=7–8. Locking to 4 = `.fail 38`.

⛔ **FREE BOOSTS = PLAYER CHOICE.** Auto-assign / working-backwards / pre-applied "FREE BOOST 1: STR (14→16)" = `.fail 39`. Build array is ★ SUGGESTION.

⛔ **INPUT FORMAT — PER-PROMPT MANDATORY.**
DM outputs ONE `FREE BOOST [k] of [N]:` menu at a time. Wait for player input. After each pick, render the running stat array showing the boost applied (e.g. `Applied: CON +2 → CON 14`). THEN the next prompt. Each prompt shows: which source this boost is from (bg free / ancestry free 1 / ancestry free 2 / standard 1-4), what stats are still legal (excluding already-picked within same source), and ★ Suggested per build.
Opening with "type N numbers" / batch-first menu = `.fail 38`. Skipping the running array between prompts = `.fail 39`.
PLAYER MAY OPT INTO BATCH by typing all N picks in one message. DM accepts batch only if player initiates. Validate: (a) within-source uniqueness; (b) 4 standard free MUST be 4 DIFFERENT stats; (c) no stat > 18 after summing. Illegal batch = `Invalid: <rule>. Re-pick per-prompt.` Refusing VALID batch with theater = `.fail 35`.

Banned formats (`.fail 38`): ASSIGN / DEFAULT / SWAP commands, combined menu, working-backwards derivation, free-count locked to 4.

⛔ **HARD STOP — SELF-CHECK BEFORE POSTING.** Scan your draft. ALL must hold:
  (1) Response contains literal text `FREE BOOST 1 of ` (count-agnostic — number that follows must equal N you computed).
  (2) Response does NOT contain any of: `FINAL STATS`, `Fort +`, `Ref +`, `Will +`, `HP:`, `AC:`, `Speed:`. These appear only AFTER all picks recorded.
  (3) Response ends at the active menu. No derivation, no final array, no feat list past this point.
Any fail → delete from `FREE BOOST 1 of` onward, re-post stopping at the menu. `.fail 39` + `.fail 41`.

```
LOCKED BOOSTS:
  Class key: +[stat]
  Background pool: [A] or [B] (pick below; 2nd bg boost is free)
  Ancestry fixed: [stat(s) or "none — all free"]

BACKGROUND FIXED PICK (if 2-stat menu):  [1] [A]   [2] [B]

FREE BOOST 1 of [N]:
  [1] STR  [2] DEX  [3] CON  [4] INT  [5] WIS  [6] CHA
  ★ Suggested: [stat] — [reason from build file]
```
After ALL picks recorded, output the final stat array:
```
Boosts: Ancestry (+[..]) | Background (+[..]) | Class (+[..]) | Free (+[..])
STR [X] DEX [X] CON [X] INT [X] WIS [X] CHA [X]
```

⛔ **BOOST MATH SELF-CHECK** — before posting final array:
  stat = 10 + (2 × count of boosts to that stat from all sources, class key included). 18 cap hard. Any DM-suggested batch's claimed array MUST match the counted boosts in the batch. Example: batch "1 1 3 3 5 2 6" has STR×2 in free picks + class key = 3 STR boosts = STR 16, NOT 18. Claim-math mismatch = .fail 4 + .fail 9.

**② FEATS — L1 (NUMBERED MENU REQUIRED — NEVER AUTO-FILL)**

⛔ **FEAT SOURCE LOCK — output before any feat menu:**
`FEAT SOURCES: Heritage = KM_Ancestries.md | Ancestry feat = KM_Ancestries.md | Background skill feat = KM_Ancestries.md | Class feat = [build file]`
Fabricated feat not in named file = `.fail 9`. Skipping source line = `.fail 41`.

L1 feat slots (compute per character):
  Heritage: confirm from Step 2 (no menu).
  Background skill feat: AUTO-granted (announce, no menu).
  Ancestry feat: 1 menu from KM_Ancestries.md.
  L1 class feat: 1 menu from build file.
  Heritage bonus (if applicable): Natural Ambition → +1 class feat menu (same source, minus used pick); Versatile Human → +1 general feat menu (KM_BuildGuide.md); Skilled Human → +1 trained skill (class skill list).

⛔ **EVERY non-auto slot = NUMBERED MENU.** Build default = ★ marker only, NOT pre-filled. Listing feats as filled values without preceding numbered menu = `.fail 39`.

⛔ **HARD STOP — SELF-CHECK BEFORE POSTING (feats phase).** ALL must hold:
  (1) Each non-auto feat slot output as: `[SLOT NAME] (slot k of M):` + numbered list `[1] FeatName — effect` ... drawn from the named source file.
  (2) No feat slot shows a single filled value without its menu first.
  (3) Response ends at the active feat menu, waiting for input.
Fail → delete and re-post with menus. `.fail 39`.

Player may swap with: SWAP ANCESTRY / SWAP SKILL / SWAP CLASS + feat name.

**③ HIT POINTS + ARMOR CLASS**
```
HP: [class base HP] + [CON mod] + [ancestry HP] = [total]
AC: 10 + [armor bonus] + [DEX mod capped] + 3 (trained = proficiency rank 2 + level 1) = [total]
```

**④ LANGUAGES**
```
Starting: Common + [ancestry language, e.g. Elven / Dwarven / Orcish]
Bonus: +[INT mod] additional languages if INT mod > 0 (player names them)
```

**⑤ FINAL TRAINED SKILLS (with modifiers)**
List every trained skill:
```
[Skill]: +2 (trained) + [ability mod] = +[total]
```

Then output: *"Setup confirmed. Ancestry [X], Heritage [H], Background [Y],
Weapon [Z], Armor [W], Deity [D or none]. HP [X] | AC [Y]. Generating save block."*
Heritage missing from confirmation line = `.fail 3` (heritage step skipped).
⛔ **DO NOT OUTPUT THE SAVE BLOCK YET. Starting Gear runs NEXT, then companion selection.**

⛔ **STARTING GEAR — STEP 10 — MANDATORY.**
Open `KM_BuildGuide.md`. Output the gear selection screen verbatim. Wait for player to pick A, B, or C.
Record result in `inventory.gear[]` and adjust `gold` if player spent from 15 gp.
Skipping this step = `.fail 41`. Moving to companions before gear is confirmed = `.fail 41`.

⛔ **COMPANION SELECTION — STEP 11 — MANDATORY. RUNS AFTER GEAR, BEFORE THE SAVE BLOCK.**

**Exact sequence — no deviations:**
1. READ `KM_Companions_Behaviors.md` DIRECTLY BY FILENAME and copy-paste the
   COMPANION SELECTION SCREEN verbatim (OPEN POOL: 11 candidates, single-letter codes A–K).
2. STOP. Wait for the player to type 5 SINGLE LETTERS (A–K) in any order — e.g. "A B D G J" — or `?` for auto-pick.
   Validate: exactly 5 unique letters, all from A–K. Invalid input → re-render menu with reason.
   Manor companions (G–K Amiri/Valerie/Harrim/Linzi/Jaethal) are NOW in the open pool — picked here, NOT alignment-gated.
   Quest-Locked 7 are NOT picked here — they join at quest triggers in Ch1+.
   ⛔ **PICK-5 VERIFY — MANDATORY before recording picks.**
   Open `KM_CompanionIndex.md`. Output the SENTINEL CHECK first, then the 5 picks:
   `INDEX SENTINEL v7.0: A = Hu Tao | F = (retired — Velvet removed) | J = Linzi | Q1 = Jubilost | S1 = Bellatrix Lestrange`
   Then for each of the 5 picks, output:
   `PICK [X] LOCKED: [X] = [Name] ([Class]) — CONFIRMED`
   Build defaults: A=Hu Tao NEW_001, B=Keqing NEW_002, C=Leliana NEW_003, D=Yor Forger NEW_004, E=Aerith NEW_005, G=Amiri, H=Valerie, I=Harrim, J=Linzi, K=Jaethal. (F retired — Velvet/NEW_011 removed.)
   ⛔ **C (Leliana) and J (Linzi) are the SAME chronicler-bard slot — MUTUALLY EXCLUSIVE; pick AT MOST ONE.** If the player's 5 include BOTH C and J, REJECT and have them swap one out — they are the one-or-the-other chronicler-bard (Leliana = book of ballads/songs; Linzi = book of stories; NEVER both, per KM_Companions_Behaviors.md § LINZI-REPLACEMENT GATE). Pick C → Leliana is the chronicler-bard, Linzi NEVER appears in the run, the Manor Linzi-offer is skipped. Pick neither → Linzi is offered at the Manor and may be declined → Leliana walks in (Route 2). A run with both in `companions_selected` = `.fail 9`.
   Using training data = `.fail 9`. Skipping verify = `.fail 41`.
   Record `companions_selected[]` (the 5 picked) + `companions_not_picked[]` (the 6 not picked) only after sentinel + all lines output.
2.5. ⛔ **LINZI-REPLACEMENT GATE — MANDATORY if J (Linzi) NOT in picks.**
    If the player did not pick J, run the LINZI-REPLACEMENT prompt from
    `KM_Companions_Behaviors.md § LINZI-REPLACEMENT MECHANICS` verbatim.
    Wait for player to nominate one of their 5 picks (single letter) as chronicler.
    Record `linzi_replacement` + `linzi_replacement_letter` + `chronicler_active: true` in save block.
    If Linzi IS picked: set `linzi_replacement: null` and `chronicler_active: true`. Skip prompt.
    Skipping the gate when Linzi not picked = `.fail 41`.
    NOTE — LINZI / LELIANA ARE ONE SLOT, NEVER BOTH: Linzi (J) and Leliana (C) are
    mutually exclusive — exactly ONE chronicler-bard per run. Pick C → Linzi never
    appears (`leliana_chronicler_mode=true`, `linzi_primary_chronicler=false`, Linzi
    absent from companions[] and the recruitable pool). Pick J → Linzi is the
    chronicler-bard. Pick NEITHER → Linzi is offered at Manor arrival, where declining
    her brings Leliana in (Route 2). Leliana = Linzi with the MEDIUM swapped (music/songs,
    a book of ballads) — she inherits ALL of Linzi's mechanics AND story roles,
    including the Ch6 Thousandbreaths death + resurrection. Full rule:
    KM_Companions_Behaviors.md § LINZI-REPLACEMENT GATE + MASTER TRANSFORMATION RULE;
    gate fires at KM_PR_01_manor_arrival.md. Record `linzi_replacement_gate_fired`,
    `leliana_chronicler_mode`, `linzi_primary_chronicler` accordingly.
3. SEEKERS ARE HARDCODED — no player pick. Auto-record:
   `seeker_1 = "Bellatrix Lestrange"` | `seeker_2 = "Revy"` | `seeker_3 = "Satsuki Kiryūin"` | `seeker_4 = "Velvet Crowe"` | `seeker_5 = "Atalanta Alter"`
   They are Tartuccio's five and flip via Diplomacy DC 10 in Ch1. Do NOT show a Pick-5 screen.
4. ⛔ **SAVE BLOCK SCHEMA LOCK — output BOTH lines below before generating save block:**
   Line A — schema sentinel:
   `SCHEMA CHECK: save_version = "1.9" | source = KM_SaveBlock_Template.md EXHAUSTIVE MODE | top-level keys = 53`
   Line B — template fingerprint (first 6 root keys, verbatim, in order):
   `FINGERPRINT: save_version | chapter_completed | save_timestamp | save_label | turns_elapsed | dm_resume_note`

   Then re-open `KM_SaveBlock_Template.md` and copy its structure verbatim.
   ⛔ DO NOT generate the save block from memory, training data, or inference.
   ⛔ DO NOT use `"schema_version"` or any version other than `"1.9"`.
   ⛔ DO NOT invent, rename, reorder, or drop keys. All 53 top-level keys present.
   ⛔ DO NOT omit `turns_elapsed` — required at root position 5 (between save_label and dm_resume_note).
   ⛔ DO NOT skip `pick6_dropped`, `manor_companions_joined`, `quest_locked_joined`,
      `passive_jealousy`, `companion_rivalry`, `companion_fights`, `date_log`,
      `dates_this_chapter`, `dispositions`, `marriage` (inside player), or
      `game_options.companion_leveling_mode` — common omissions.

   Wrong version / fingerprint / key count = `.fail 9`. Missing sentinel = `.fail 41`.

   NOW output the COMPLETE save block using `KM_SaveBlock_Template.md`
   (EXHAUSTIVE MODE — every field present, 53 top-level keys, all 8 log
   blocks populated) with `companions_selected[]` (Pick-5), `pick6_dropped`,
   `manor_companions_joined: []`, `quest_locked_joined: []`, and
   `seeker_1`–`seeker_5` already populated. Custom structure / omitted fields = `.fail 9`.
5. ONLY THEN proceed to the prologue.

**⛔ PROHIBITED until step 4 is complete:** scene narration, NPC dialogue,
location flavor, "you arrive at Jamandi's manor" or equivalent, announcing
the screen without showing it, assuming a default companion roster from
training data, outputting a save block before companions AND seekers are recorded.

Skipping the Pick-6 screen = `.fail 9`. Save block before Pick-6 drop + Seekers default = `.fail 9`.
Prologue before `companions_selected[]` confirmed = `.fail 3`.

**If DM skipped any prompt:** player types `.fail 3 — prompt [N] skipped`.
DM reprints prompt [N] and continues.

---

## 📋 DM NOTES

- These prompts are the ONLY way the player chooses weapon/armor/stat/deity/skills.
  Build file defaults are SUGGESTIONS, not decisions.
- Never combine prompts into one menu. One prompt per response. Wait between.
- If the build file has a richer alternatives table, USE IT instead of the
  generic fallback lists above. Generic fallbacks are last-resort only.
- Chosen values override the build file's stat block. If player picks a
  Finesse weapon on a STR-locked build, reject the choice and re-prompt.
- Companion builds (Pick-5 cross-IP + Manor 5 + QL 7): these 4 prompts do NOT run for companions.
  Companion builds use pre-assigned NEW_001..NEW_010 (cross-IP/Seekers) or canonical KM CRPG builds (Manor/QL).
  Only the player character gets setup prompts.

---

*KM_CharCreate.md — Kingmaker PF2e | 8-prompt build customization*
