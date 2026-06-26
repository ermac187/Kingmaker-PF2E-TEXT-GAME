# KINGMAKER — GUIDED CHARACTER CREATION
## KM_CharCreate.md | Referenced by: KM_BuildScreen.md, KM_Backgrounds.md

> **DM:** Load this file at session start, before KM_BuildScreen.md. Walk the player
> through each step in order. Display guidance text to help them choose — these are
> player-facing, not DM-only. After class + build are confirmed, return here for
> ancestry and background. Weapon selection runs through KM_BuildScreen.md Step 2.5.

---

## ⛔ CREATION ORDER

> **Authoritative sequence — must match KM_BuildScreen.md STEP 3. Any deviation = `.fail 9`.**

```
1. Class       → This file (guidance) → KM_BuildScreen.md (build lists)
2. Build       → KM_BuildScreen.md (10 presets per class) → record player.build,
                 player.build_source, player.leveling_mode
3. Ancestry    → This file (guidance + full list) → KM_AncestryGuide.md class block
4. Heritage    → KM_Heritages.md (core + uncommon + Goliath) + KM_Heritages_B.md (rare + 8 versatile heritages)
5. Background  → This file (summary) → KM_Backgrounds.md (full text, 1–7) +
                 KM_Backgrounds_CRB.md (8–42)
5.5 Boosts+Feats → This file STEP 5.5 (stat assembly, L1 ancestry/background/class feats)
6. Deity       → This file STEP 6 (divine classes mandatory, others optional)
7. Skills      → This file STEP 7 (class-fixed + N + INT mod player picks)
8. Weapon      → KM_BuildScreen.md Step 2.5 → STAT-WEAPON CHECK (Step 5.5)
9. Armor       → KM_BuildScreen.md Step 2.6  ⚠️ flag DEX cap for DEX +3 or higher
10. Confirm    → This file STEP 10 (.status: HP/AC/languages/feats/skills) → Pick-10
```

> **Why ancestry/background precede weapon/armor:** Ancestry bonuses can shift stat spreads, which affects the STAT-WEAPON CHECK (Step 5.5 in KM_BuildScreen.md). Running weapon selection before ancestry is resolved can force a second pass. Background may also grant weapon proficiencies (e.g., Sword Scion) that widen the weapon menu.

---

## STEP 1 — CLASS SELECTION

> **DM:** Display the class menu below. Offer to answer questions before the player
> commits. After they pick a class number, load KM_BuildScreen.md and display that
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

> **DM:** Load `KM_BuildScreen.md` and display the 10-preset block for the player's chosen class.
> Mark the ★ recommended preset. After the player picks a number (1–10), record the build name
> and source file in the save block and set leveling mode to AUTO (default for preset builds).
> Inform the player that level-up feat picks will be applied automatically unless they switch modes.

**Script (player-facing):**
```
Here are your 10 preset builds for [Class]. Each includes a full L1–20 leveling map.
By default I'll apply the recommended feat automatically each time you level up (AUTO mode).
Type ASK if you want to choose your own feats instead.

[BUILD LIST — display from KM_BuildScreen.md for this class]
```

**After build pick — record in save block:**
```
player.build         = [Build Name e.g. "Giant Reach"]
player.build_source  = KM_Builds_[file].md  (look up in KM_Builds.md router)
player.leveling_mode = MANUAL               ← default; change to AUTO or ASK anytime
```

> ⚠️ Player leveling defaults to `MANUAL` (player picks every option, with ★ build-map
> recommendation marked). Companion leveling is governed by
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

> **➡️ STEPS 3 (Ancestry), 4 (Heritage), 5 (Background), 5.5 (Ability Boosts + L1 Feats), 6 (Deity), 7 (Skills), TIPS FOR NEW PLAYERS, and STEP 10 (Final Confirmation) — see `KM_CharCreate_B.md`. Pair-load both files for any guided creation session.**

---

*KM_CharCreate.md — Kingmaker PF2e Text Adventure | Char Create v2.0 (split — pair-load with KM_CharCreate_B.md)*
