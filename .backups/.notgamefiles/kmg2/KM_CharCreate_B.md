# KINGMAKER — GUIDED CHARACTER CREATION (PART B)
## KM_CharCreate_B.md | Pair-load with KM_CharCreate.md

> **DM:** Part B of guided character creation (Mode B). Always pair-load with `KM_CharCreate.md` (Part A covers the creation order, Step 1 Class Selection, and Step 2 Build Selection). This file covers Steps 3 (Ancestry), 4 (Heritage), 5 (Background), 5.5 (Ability Boosts + L1 Feats), 6 (Deity), 7 (Skills), Tips for New Players, and Step 10 (Final Confirmation).

---

## STEP 3 — ANCESTRY SELECTION

> **DM:** After class + build + weapon are confirmed, display the ancestry menu below.
> Player picks a number. Record `player.ancestry` in save block.
> Ancestry weapon substitution rule applies (KM_PrePrologue_Builds.md).
> Also record `player.languages[]`: Common + ancestry language + INT mod bonus languages (INT mod > 0 only).
>
> **If player types `? [ancestry]` or asks for more detail:** load `KM_Ancestries_Detailed.md` and display that ancestry's full entry (stats, size, heritages, L1 feats, culture, lifespan, build synergy).

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

> **DM:** ⛔ Load BOTH `KM_Heritages.md` (core + uncommon + Goliath) AND `KM_Heritages_B.md` (rare + versatile). Find the player's ancestry section in whichever file it lives in. Copy-paste the full heritage block verbatim — do NOT skip heritages or describe them from memory. Every listed heritage is a legal pick. Offer Versatile Heritage (`versatile` → KM_Heritages_B.md § VERSATILE HERITAGES) as an alternative. Wait for player pick, record `player.heritage` + `player.heritage_source` + `player.heritage_granted_features[]` in the save block. Missing the step entirely = `.fail 9`. Fabricating a heritage name or effect = `.fail 9`.

**Player input forms:**
- A number from the ancestry's heritage list (e.g., `3` under Elf = Cavern Elf)
- `versatile` → display the 8 Versatile Heritage options, wait for pick
- Typing a heritage name directly (e.g., `Ancient Elf`, `Nephilim Celestial`) — accept if valid

**After pick:** confirm the heritage effect in one sentence, then proceed to Step 5.

---

## STEP 5 — BACKGROUND SELECTION

> **DM:** ⛔ Load `KM_Backgrounds.md`. Copy-paste the compact screen exactly (42 entries, numbered 1–42). Wait for player pick, record `background`. Do NOT display from memory or generate from system knowledge. Missing entries = `.fail 9`.

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

**L1 Feats** (after stats): Ancestry feat → load `KM_AncestryGuide.md` L1 list, wait, record `player.ancestry_feat`. Background skill feat → auto-granted by background, state it, record `player.background_skill_feat`. Class feat (L1) → preset = build file L1 row (SWAP to override); custom = present options; record `player.class_feat_1`.

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
*27 classes | 28 ancestries | 42 backgrounds (KM_Backgrounds.md) | Tips included*

*KM_CharCreate_B.md — Kingmaker PF2e Text Adventure | Char Create Part B v1.0*
