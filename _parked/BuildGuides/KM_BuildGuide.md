# KINGMAKER — BuildGuide (CONSOLIDATED)
## KM_BuildGuide.md | v1.0 (2026-05-22): Merged from related files.



---

<!-- merged from KM_BuildGuide.md (v93.21 file consolidation) -->

# KINGMAKER — BUILD SELECTION SCREEN
## KM_BuildGuide.md | Referenced by: KM.txt, KM_Companions_Behaviors.md

> **DM:** Mechanical reference. Load KM_CharCreate.md first. This file handles Step 2 builds and Step 2.5 weapons. Do NOT generate builds from memory. Skipped step = `.fail 9`.
>
> **⛔ After player selects a build:** Load `KM_CharCreate.md` and run all 8 prompts (Ancestry → Heritage → Stat → Weapon → Armor → Deity → Background → Skills) IN ORDER before Step 3 companion selection.

---

## STEP 2 — PICK A CLASS

```
KINGMAKER — CHARACTER SELECT. PF2e Remaster plus Battlecry.

Choose your class, then pick a build within it.

  [1]  Alchemist      (10 builds)
  [2]  Animist        (10 builds)
  [3]  Barbarian      (10 builds)
  [4]  Bard           (10 builds)
  [5]  Champion       (10 builds)
  [6]  Cleric         (10 builds)
  [7]  Commander      (10 builds)
  [8]  Druid          (10 builds)
  [9]  Exemplar       (10 builds)
  [10] Fighter        (10 builds)
  [11] Guardian       (10 builds)
  [12] Gunslinger     (10 builds)
  [13] Inventor       (10 builds)
  [14] Investigator   (10 builds)
  [15] Kineticist     (10 builds)
  [16] Magus          (10 builds)
  [17] Monk           (10 builds)
  [18] Oracle         (10 builds)
  [19] Psychic        (10 builds)
  [20] Ranger         (10 builds)
  [21] Rogue          (10 builds)
  [22] Sorcerer       (10 builds)
  [23] Summoner       (10 builds)
  [24] Swashbuckler   (10 builds)
  [25] Thaumaturge    (10 builds)
  [26] Witch          (10 builds)
  [27] Wizard         (10 builds)

Type a number from 1 to 27, or CUSTOM to build from scratch.
```

---

## STEP 2 — BUILD LISTS

> **DM:** After player picks a class, load `KM_BuildGuide.md` (classes 1–13) or `KM_BuildGuide.md` (classes 14–27) and display ONLY that class's block. One display, one pick — do NOT load a separate file or ask twice. Proceed directly to KM_CharCreate.md after pick.

> ⛔ **BUILD LIST SOURCE LOCK — mandatory before displaying any build list.**
> Output this line verbatim BEFORE showing the class build block:
> `BUILD LIST SOURCE: [KM_BuildGuide.md or KM_BuildGuide.md] | class = [ClassName] | build 1 = [exact Build 1 name from file]`
> Then copy-paste ONLY that class's block from the file verbatim. Do NOT generate build names or descriptions from training data.
> Build 1 sentinel: if your Build 1 name does not exactly match the file, you are fabricating — stop, re-read, re-output.
> Fabricated build name at any position = `.fail 9`. Skipping source line = `.fail 41`.
>
> ⛔ **NUMERIC ORDER — ALWAYS.** Output builds exactly as numbered in the file: 1, 2, 3 … 10.
> Do NOT reorder. Do NOT group by type, theme, or role. Do NOT move ★ builds to the top.
> Do NOT sort by rating, difficulty, or any other criterion. The file order is the display order.
> Reordering or renumbering = `.fail 9`.
>
> **Barbarian sentinel (class 3):** Build 1 = `Tactical Reach King` — any other name at position 1 = fabrication.
> **Fighter sentinel (class 10):** Build 1 = check KM_BuildGuide.md [10] FIGHTER block.
> **All other classes:** Build 1 is authoritative from the guide file — training data is not a substitute.

---

## STEP 2.5 — STARTING WEAPON

> **DM:** After class + build are confirmed, find the class/build in the table below,
> **copy-paste that category's weapon list verbatim from this file**, and wait for the player's pick.
> Do NOT generate weapon lists from memory. Generating from memory = missing entries = `.fail 9`.
> Record as `player.weapon` in save block. This replaces `[primary weapon]` everywhere
> in pre-prologue narration. Ancestry weapon substitution rule (KM_PrePrologue_Setup.md) still applies.

### FIXED BUILDS — display weapon, skip selection:
```
Kineticist (any)  → Elemental Blast (unarmed)
Monk (any)        → Fists / Handwraps (Monastic Archer = Composite Shortbow; Wild Shape = form jaws)
Magus (any)       → set by build stat block (H.md / H2.md)
Gunslinger (any)  → set by KM_PrePrologue_Setup.md build row
Inventor (any)    → set by KM_PrePrologue_Setup.md build row
```

### CLASS → WEAPON CATEGORY

| Class / Build | Category |
|---|---|
| Rogue (all), Swashbuckler (all), Investigator (all) | A |
| Bard (all), Alchemist (all) | A |
| Champion (all), Guardian (all), Commander (all) | B |
| Cleric — Warpriest | B |
| Fighter — Shield Dual Slice, Power Attack | B |
| Oracle — Battle Mystery | B |
| Barbarian (all), Exemplar (all) | C |
| Fighter — Two-Handed | C |
| Fighter — Dual Slice, Two-Weapon | H |
| Ranger (all), Fighter — Archer | D |
| Fighter — Reach Controller | E |
| Gunslinger — Drifter | B + D (one-handed weapon + pistol) |
| Gunslinger — Sniper | D |
| Wizard (all), Sorcerer (all), Witch (all), Druid (all) | F |
| Psychic (all), Animist (all), Summoner (all) | F |
| Cleric — Cloistered, Oracle (caster mysteries) | F |
| Thaumaturge (all) | G |

### WEAPON CATEGORIES

```
CATEGORY A — Light / Finesse  (pick 1–17)
  1  Rapier              7  Starknife          13  Light Hammer
  2  Shortsword          8  Main Gauche        14  Hatchet
  3  Dagger              9  Light Mace         15  Wakizashi
  4  Sap                10  Sickle             16  Sai
  5  Hand Crossbow      11  Filcher's Fork     17  Butterfly Sword
  6  Kukri              12  Light Pick

CATEGORY B — Martial One-Handed  (pick 1–18)
  1  Longsword           7  Mace              13  Hatchet
  2  Battleaxe           8  Pick              14  Khopesh
  3  Warhammer           9  Trident           15  Flickmace (10 ft reach)
  4  Scimitar           10  Rapier            16  Aklys (reach 10 ft, trip)
  5  Flail              11  Shortsword        17  Bastard Sword (1H d8 / 2H d12)
  6  Morningstar        12  Katana            18  Falcata
 ★ Fighter Shield builds: chosen weapon is paired with Steel Shield
 ★ eRmaC signature: Flickmace pairs with Steel Shield (Bodyguard build)

CATEGORY C — Martial Two-Handed  (pick 1–18)
  1  Greatsword          7  Greatpick         13  Spiked Chain
  2  Greataxe            8  Bastard Sword     14  Naginata
  3  Maul                9  Greatclub         15  Bo Staff
  4  Glaive             10  Earthbreaker      16  Fauchard
  5  Halberd            11  Horsechopper      17  Guisarme
  6  Falchion           12  Longspear         18  Scythe
 ★ Barbarian Giant Instinct: chosen weapon is OVERSIZED (add prefix)
 ★ eRmaC signature: Guisarme (Tactical Reach King, reach 10 ft, trip)

CATEGORY D — Ranged  (pick 1–17)
  1  Longbow             7  Sling             13  Repeating Crossbow
  2  Composite Bow       8  Halfling Sling    14  Arbalest
  3  Shortbow               Staff             15  Throwing Knife
  4  Light Crossbow      9  Javelin           16  Boomerang
  5  Hand Crossbow      10  Shuriken          17  Daikyū (Composite Longbow)
  6  Heavy Crossbow     11  Blowgun
                        12  Hornbow
 ★ Ranger Flurry: also pick a secondary melee — Shortsword / Dagger / Handaxe
 ★ Composite bows scale STR damage; flat bows do not

CATEGORY E — Reach / Polearm  (pick 1–17)
  1  Halberd             7  Naginata          13  Spiked Chain
  2  Glaive              8  Lance             14  Whip
  3  Spear (thrown)      9  Horsechopper      15  Flickmace (10 ft, 1H)
  4  Ranseur            10  Pike              16  Aklys (10 ft, trip)
  5  Longspear          11  Fauchard          17  Tetsubo
  6  Guisarme           12  Bec de Corbin
 ★ All entries reach 10 ft except where noted; flickmace is 1H reach
 ★ Scythe / Bec de Corbin: deadly d10 critical specialization

CATEGORY F — Simple / Implement  (pick 1–16)
  1  Staff (Quarterstaff)    7  Light Crossbow     13  Bo Staff
  2  Dagger                  8  Hand Crossbow      14  Whip
  3  Spear                   9  Heavy Crossbow     15  Javelin
  4  Club                   10  Light Mace         16  Sap
  5  Sling                  11  Mace
  6  Sickle                 12  Morningstar
 ★ Casters: implement weapon doubles as spell focus
 ★ Staff is the universal default; advanced casters often pick Crossbow for backup

CATEGORY G — Thaumaturge  (pick 1–17)
  1  Rapier              7  Pick              13  Hatchet
  2  Shortsword          8  Morningstar       14  Trident
  3  Dagger              9  Flail             15  Starknife
  4  Warhammer          10  Scimitar          16  Hand Crossbow
  5  Sling              11  Mace              17  Light Mace
  6  Longsword          12  Kukri
 ★ Implement-bonded weapon — used 1H with implement in off-hand
 ★ Battleaxe / Sap also legal — type CUSTOM to pick

⛔ CATEGORY H — COPY-PASTE THIS BLOCK EXACTLY. DO NOT GENERATE FROM MEMORY. Count = 13. "Type a number (1–12)" = .fail 9.

CATEGORY H — Dual Wield (Dual Slice / Two-Weapon Fighter)
Pick a main + off-hand combo:

  1   Longsword + Shortsword      slashing all-rounder
  2   Rapier + Shortsword         finesse / DEX build
  3   Rapier + Main Gauche        finesse + parry (AC boost off-hand)
  4   Longsword + Main Gauche     STR + parry defense
  5   Warhammer + Light Hammer    bludgeoning focus (less resisted)
  6   Battleaxe + Hatchet         axe sweep + throwable off-hand
  7   Katana + Wakizashi          DEX/STR hybrid (Advanced Weaponry)
  8   Shortsword + Shortsword     pure agile, maximum attack chains
  9   Dagger + Dagger             pure finesse, concealable
 10   Flail + Shortsword          trip/prone main + agile follow-up
 11   Scimitar + Kukri            slashing + deadly crit off-hand
 12   CUSTOM                      type your own main + off-hand pair
 13   Pick + Light Pick           piercing crit focus (deadly d10 main + agile off-hand)

Type a number (1–13).
```

---

## STEP 2.6 — STARTING ARMOR

> **⛔ DM:** COPY-PASTE THE ARMOR TABLE BELOW EXACTLY. DO NOT GENERATE FROM MEMORY OR PF2E TRAINING DATA.
> Stats in this file differ from core PF2e. Fabricating entries, omitting Dragon Plate, or using
> wrong AC values = `.fail 9`. Entry count = 11 (0–10). "Type a number (0–9)" = `.fail 9`.
> Record as `player.armor` in save block. This replaces `[armor description]` in all pre-prologue narration.

```
LIGHT ARMOR (recommended if DEX +3 or higher)
  1  Leather Armor      +1 AC  Dex cap +4  No speed penalty
  2  Studded Leather    +2 AC  Dex cap +3  No speed penalty

MEDIUM ARMOR (balanced protection)
  3  Hide Armor         +3 AC  Dex cap +2  −5 ft speed
  4  Scale Mail         +4 AC  Dex cap +2  −5 ft speed
  5  Breastplate        +4 AC  Dex cap +2  −5 ft speed
  6  Chain Mail         +4 AC  Dex cap +1  −5 ft speed

HEAVY ARMOR (max AC — best if DEX +0 or fighter with Armor Expertise)
  7  Splint Mail        +5 AC  Dex cap +1  −10 ft speed
  8  Banded Mail        +6 AC  Dex cap +0  −10 ft speed
  9  Full Plate         +6 AC  Dex cap +0  −10 ft speed
 10  Dragon Plate       +6 AC  Dex cap +0  −5 ft speed   [Bulwark] [Resist fire 5] [Aerynth-origin — triggers world-reaction] [PC-LOCKED: eRmaC wears it regardless of class armor proficiency — see DRAGON PLATE NOTE below]

UNARMORED (Monk, some Druids — skip if wearing armor)
  0  Unarmored          Dex + Wis + Prof to AC

SPECIAL MATERIAL — add to any armor type after picking base:
  + Aracoix Scale    Medium (Mail) only; ACP 0, no speed penalty
  + Wyrmskin         Leather/Hide (Light) only; Resist fire 5
  + Shadowsilk       Cloth/Unarmored only; worn over clothes; +2 circ. Stealth

NOTE: Mithril and Adamantine are weapon/blade materials only — not available for armor.
NOTE: Dragonhide is the flex-zone component of Dragon Plate (option 10) — not a standalone add-on.

⚠️ DEX CAP NOTE: If player DEX mod exceeds armor's Dex Cap, the excess is lost.
   Flag this whenever DEX mod > Dex Cap — not only DEX +3 or higher.
   Example: DEX 14 (+2) with Dragon Plate (cap 0) — you lose 2 DEX.

⚠️ DRAGON PLATE NOTE: Same protection as Full Plate. Has Bulwark trait — on a failed Reflex
   save against an area effect, treat it as a success instead. Grants Resist fire 5
   (intrinsic to the dragonscale outer layer — does not stack with other fire resist sources;
   take the higher value). Appearance and NPC reactions pulled from KM_Exploration.md —
   Dragon Plate row. Cannot be combined with special materials.

   **PC-LOCKED PROFICIENCY OVERRIDE (eRmaC only):** Dragon Plate is alien-origin
   (Aerynth) and was fitted, shaped, and worn-in for eRmaC across the campaigns that
   preceded the Aldori invitation. It is **always available to eRmaC regardless of
   his class's armor proficiency**. A Wizard eRmaC, a Sorcerer eRmaC, a Rogue eRmaC,
   a Monk eRmaC — all may select Dragon Plate. The armor effectively grants its own
   trained-Heavy proficiency to eRmaC as a personal artifact. AC is computed normally
   (10 + 6 + DEX capped 0 + L + trained 2). DEX cap 0 still applies — a high-DEX
   caster loses DEX bonus to AC while wearing it. Speed penalty −5 ft still applies.
   No other character (companion, NPC, future PC) can wear it — race/PC-locked.

   **DM:** Do NOT hide option 10 from the player based on class. Dragon Plate appears
   on EVERY armor menu shown to eRmaC, regardless of whether the class normally has
   heavy proficiency. Hiding it from a non-Heavy class = `.fail 9` (false omission).
   The PC-LOCKED tag is what makes this legal — it is eRmaC's signature item, not a
   generic heavy armor purchase.

⚠️ AC FORMULA — compute and output in the status panel:
   AC = 10 + armor bonus + DEX mod (capped by Dex Cap) + proficiency
   L1 trained proficiency: +3 (proficiency rank 2 + level 1)
   Do NOT stop at "10 + armor bonus" — always add DEX (capped) + proficiency.
   Examples: Breastplate, DEX 18 default   = 10 + 4 + 2 + 3 = AC 19
             Dragon Plate, STR-swap DEX 14  = 10 + 6 + 0 + 3 = AC 19
             Dragon Plate speed: 25 − 5 = 20 ft

Type a number (0–10), then specify special material if desired (not valid for option 10).
```

---

## BUILD FILE ROUTING

> **DM:** Load the file listed here for the player's chosen class to get the full stat block.

```
(v3.0 — per-class consolidation 2026-05-22: each per-letter file holds all 10 presets for every class assigned to that letter)

Alchemist (1–10)        → KM_Builds_Alch_Animist.md
Animist (1–10)          → KM_Builds_Alch_Animist.md
Barbarian (1–10)        → KM_Builds_Barb_Bard.md
Bard (1–10)             → KM_Builds_Barb_Bard.md
Champion (1–10)         → KM_Builds_Champ_Cleric.md
Cleric (1–10)           → KM_Builds_Champ_Cleric.md
Commander (1–10)        → KM_Builds_Cmdr_Druid.md
Druid (1–10)            → KM_Builds_Cmdr_Druid.md
Exemplar (1–10)         → KM_Builds_Exemplar_Fighter.md
Fighter (1–10)          → KM_Builds_Exemplar_Fighter.md
Guardian (1–10)         → KM_Builds_Guard_Gun_Inv.md
Gunslinger (1–10)       → KM_Builds_Guard_Gun_Inv.md
Inventor (1–10)         → KM_Builds_Guard_Gun_Inv.md
Investigator (1–10)     → KM_Builds_Invest_Kineticist.md
Kineticist (1–10)       → KM_Builds_Invest_Kineticist.md
Magus (1–10)            → KM_Builds_Magus_Monk.md
Monk (1–10)             → KM_Builds_Magus_Monk.md
Oracle (1–10)           → KM_Builds_Oracle_Psychic_Ranger.md
Psychic (1–10)          → KM_Builds_Oracle_Psychic_Ranger.md
Ranger (1–10)           → KM_Builds_Oracle_Psychic_Ranger.md
Rogue (1–10)            → KM_Builds_Rogue_Sorcerer.md
Sorcerer (1–10)         → KM_Builds_Rogue_Sorcerer.md
Summoner (1–10)         → KM_Builds_Summon_Swash.md
Swashbuckler (1–10)     → KM_Builds_Summon_Swash.md
Thaumaturge (1–10)      → KM_Builds_Thaum_Witch.md
Witch (1–10)            → KM_Builds_Thaum_Witch.md
Wizard (1–10)           → KM_Builds_Wizard.md
```

---

## STEP 3 — AFTER BUILD SELECTED

> **DM:** After class + build confirmed, proceed IN ORDER — **do NOT skip any step:**
>
> 1. Record `player.class` + `player.build` + `player.build_source` + `player.leveling_mode`.
> 2. Ancestry — display `KM_Ancestries.md` class block (★/2-5/OK/AVOID + exceptions). Record `player.ancestry`.
> 3. ⛔ **HERITAGE — load BOTH `KM_Ancestries.md` (core/uncommon/Goliath) AND `KM_Ancestries.md` (rare/versatile), find the player's ancestry section, copy-paste the heritage block verbatim. Offer `versatile` as alternate (KM_Ancestries.md). Record `player.heritage` + `heritage_source` + `heritage_granted_features[]`. Skipped or fabricated = `.fail 9`.**
> 4. ⛔ **BACKGROUND — load `KM_Ancestries.md`, copy-paste the compact screen exactly, record `player.background`. Skipped = `.fail 9`.**
> 5. Weapon (Step 2.5). Record `player.weapon`.
> 5.5. ⛔ **STAT-WEAPON CHECK** — if weapon is STR-based (pick, warhammer, battleaxe, etc.) but build defaults to DEX-primary, display swap prompt `[1] Keep DEX 18 / STR 16` / `[2] Swap to STR 18 / DEX 14`. Record player's confirmation. Silently using DEX-default stats when a STR weapon was picked = `.fail 9`.
> 6. Armor (Step 2.6). Record `player.armor`.
> 7. Output `.status` panel before any scene content.
> 8. ⛔ **COMPANION SELECTION — load `KM_Companions_Behaviors.md`, copy-paste the COMPACT PICK-6/DROP-1 SELECTION SCREEN verbatim. Player drops 1 of 6 cross-IP (Pick-5 result). Manor 5 join via Prologue alignment. Quest-Locked 7 join at quest triggers. Seekers 5 hardcoded to Tartuccio's 5. Announcing "proceeding" without showing the list = `.fail 9`.**
>
> **Save block** (all fields REQUIRED; `leveling_mode`: auto|ask|manual; player default = `manual`, companions auto-level via `game_options.companion_leveling_mode`):
> ```json
> "player": { "class": "Fighter", "build": "Dual Slice Fighter",
>   "build_source": "KM_Builds_Guard_Gun_Inv.md", "leveling_mode": "manual",
>   "ancestry": "Human", "heritage": "Versatile Human",
>   "heritage_source": "ancestry-specific",
>   "background": "Sword Scion", "weapon": "Pick + Light Pick",
>   "armor": "Dragon Plate" }
> ```
>
> **⛔ DM RULE:** Do not begin Pre-Prologue until class, build, ancestry, **heritage**, background, weapon, armor are all confirmed AND `.status` displayed. Skipped step = `.fail 9`.

---

## COMPANION BUILD ASSIGNMENT

> **DM:** After Pick-6/Drop-1 is complete (player's Pick-5 cross-IP locked), open
> `KM_Companions_Behaviors.md` and run the Build Assignment procedure for each cross-IP
> companion AND for any Manor 5 / QL 7 companion as they join. Each companion uses
> the build pre-assigned in NEW_001..NEW_010. Manor / QL companions use canonical
> KM CRPG builds. The procedure is defined in `KM_Companions_Behaviors.md` — do not improvise it.

---

*KM_BuildGuide.md v6.2 — 270 Builds, 27 Classes | Build lists + advisory merged into KM_BuildGuide_A/B.md*


---

<!-- merged from KM_BuildGuide.md (v93.21 file consolidation) -->

# KINGMAKER — BUILD GUIDE A (Classes 1–13)
## KM_BuildGuide.md | Referenced by: KM_BuildGuide.md, KM_Companions_Behaviors.md

> **DM:** After the player picks a class number from KM_BuildGuide.md, display ONLY that class's block below. This file is the single source for both build lists and advisory — display the block, prompt once. Do NOT load a separate lists file. Do NOT ask twice. Do NOT generate builds from memory = `.fail 9`.
>
> **Badges:** ★ = recommended (new players or strong overall) · ⚠️ = complex/MAD/niche · no badge = solid pick
> **Format per build:** compact mechanic · preferred ancestry · Alt-build pointer · weakness/caveat

---

## [1] ALCHEMIST

```
ALCHEMIST — Role: consumable-based control, healing, ranged alpha-strike
★ RECOMMENDED: 6 (new players) · 3 (support) · 2 (melee hybrid)
⚠️ AVOID IF NEW: 10 (MAD — INT+CON+DEX) · 9 (complex action chain)

 1  Kineticist Bomber        — Bomber + Kineticist Ded. + Fire Bomb + impulse cycling · Dwarf or Goblin · Alt: 5 · Weak: MAD
 2  Witch Mutagenist       ★ — Mutagenist + Witch Ded. + Evil Eye hex + bestial claws · Orc or Goblin · Alt: 7 · Weak: short mutagen duration
 3  Inventor Chirurgeon    ★ — Chirurgeon + Inventor Ded. + Overdrive + Elixir of Life · Gnome or Dwarf · Alt: 8 · Weak: elixir action economy
 4  Rogue Toxicologist       — Toxicologist + Rogue Ded. + Sneak Attack + poison dagger · Elf or Hobgoblin · Alt: 2 · Weak: poison DC vs bosses
 5  Psychic Bomber           — Bomber + Psychic Ded. + Amped Telekinetic Projectile · Halfling · Alt: 1 · Weak: no self-heal
 6  Pure Bomber            ★ — Bomber + Perpetual Infusions + Explosive Bomb, no dip · Dwarf or Goblin · Alt: 5 · Weak: narrow without archetype
 7  Grand Mutagenic Logistician — Mutagenist + Goblin + INT 18 + party mutagen factory · Goblin or Gnome · Alt: 2 · Weak: own combat output low
 8  Wildshape Chirurgeon     — Chirurgeon + Druid Ded. + Wild Shape + Elixir of Life · Gnome or Goblin · Alt: 3 · Weak: 3 stats matter
 9  Thaumaturge Toxicologist — Toxicologist + Thaumaturge Ded. + Tome implement · Halfling · Alt: 4 · Weak: complex round-to-round
10  Arcane Artificer       ⚠️ — Bomber + Ancient Elf + Wizard Ded. + arcane spells · Ancient Elf required · Alt: 5 · Weak: MAD, slow L1–4

Type a number (1-10). Type BACK to return to classes.
```

---

## [2] ANIMIST

```
ANIMIST — Role: flexible apparition-based caster (battle, heal, or knowledge)
★ RECOMMENDED: 3 (new players, melee) · 4 (support) · 10 (skill player)
⚠️ AVOID IF NEW: 7 (apparition tax — read ruleset first)

 1  Witness of Battles      — Vessel appar. + Oracle Ded. + dual focus pools · Dwarf or Human · Alt: 9 · Weak: dual focus management
 2  Spirit Swapper          — Daily retrain + 3 apparition slots by L6 · Human (Natural Ambition) · Alt: 8 · Weak: analysis paralysis
 3  Spirit Blade Warrior  ★ — STR melee + spirit blade, no oracle tax · Human or Orc · Alt: 9 · Weak: lower spell DC
 4  Wandering Support     ★ — Triple aura (heal + attack + skill) from L6 · Halfling or Gnome · Alt: 10 · Weak: defensive numbers low
 5  Elemental Blaster        — Typed blast 60 ft, Nimble Elf 35 ft · Nimble Elf · Alt: 7 · Weak: single element focus
 6  Spirit Warden            — Guardian appar., DR aura + intercept reaction · Dwarf or Goliath · Alt: 4 · Weak: no nova damage
 7  Apparition Blaster    ⚠️ — All feats blast, no dedication tax · Elf · Alt: 5 · Weak: needs all class feats
 8  Daily Retrain            — Spirit Guide + 4 apparition slots + utility · Human or Elf · Alt: 2 · Weak: overthinks every day
 9  Echoing Hierophant       — Witness appar. + Reactive Strike + multi-apparition support · Human or Orc · Alt: 3 · Weak: feat-intensive setup
10  Knowledge Skill God    ★ — Free RK/round + 20+ trained skills · Human or Elf · Alt: 4 · Weak: combat output average

Type a number (1-10). Type BACK to return to classes.
```

---

## [3] BARBARIAN

```
BARBARIAN — Role: high-damage STR melee, HP sponge, rage engine
★ RECOMMENDED: 1 (new players, reach) · 2 (dual-wield DPR) · 10 (support)
⚠️ AVOID IF NEW: 5 (breath weapon timing) · 6 (anti-magic niche)

 1  Tactical Reach King   ★ — Guisarme + Versatile Human + Full Plate + Titan Wrestler · Versatile Human · Alt: 7 · Weak: polearm-dependent reach
 2  Fury Flurry           ★ — Dual kukri + Double Slice + Two-Weapon Flurry · Orc or Human · Alt: 9 · Weak: vulnerable when disarmed
 3  Animal Mutagen          — Claws/jaws + Alchemist Ded. + Bestial Mutagen · Catfolk or Orc · Alt: 9 · Weak: mutagen duration management
 4  Spirit Oracle           — Ghost-touch strikes + Oracle Ded. + Weapon Surge · Human or Hobgoblin · Alt: 5 · Weak: multiclass action tax
 5  Dragon Blaster        ⚠️ — Breath 1/rage + Sorcerer Ded. + elemental nova · Half-elf (Dragon) · Alt: 4 · Weak: breath economy
 6  Superstition          ⚠️ — Warded Mind + Spell Sunder + anti-magic tank · Dwarf · Alt: 3 · Weak: useless vs non-casters
 7  Titan Mauler            — Giant Instinct + 2d12+4 Bastard Sword + STR 18 · Orc or Human · Alt: 1 · Weak: Clumsy 1 from Giant Instinct
 8  Elemental Rage          — Fury + Kineticist Ded. + typed elemental blast · Human or Elf · Alt: 5 · Weak: split action economy
 9  Frenzy Monk             — Flurry of Blows 1-action + rage flat dmg/strike · Human or Orc · Alt: 2 · Weak: MAD (STR + DEX)
10  Rage Support          ★ — CHA Raging Intimidation + Terrifying Howl AoE fear · Half-orc or Human · Alt: 4 · Weak: lower personal DPR

Type a number (1-10). Type BACK to return to classes.
```

---

## [4] BARD

```
BARD — Role: Inspire Courage buffer, versatile occult caster
★ RECOMMENDED: 6 (new players, pure caster) · 5 (focus spam) · 10 (frontline)
⚠️ AVOID IF NEW: 3 (Spellstrike timing) · 7 (dual tradition complexity)

 1  Virtuoso Maestro        — Elf Whisper + Maestro only + CHA 18 + Shortbow/Whip · Elf (Whisper) · Alt: 5 · Weak: single muse limits flexibility
 2  Warrior Melee           — Medium armor + martial + STR melee + Inspire Courage · Human or Half-orc · Alt: 10 · Weak: lower spell DC
 3  Polymath Spellblade   ⚠️ — Occult + Spellstrike via Magus Ded. + wide access · Elf or Human · Alt: 5 · Weak: action economy complex
 4  Enigma Support          — Bardic Lore all skills + Know-It-All + Dirge debuff · Gnome or Halfling · Alt: 8 · Weak: average combat output
 5  Maestro Amp           ★ — Maestro + Psychic Ded. + amp focus spam · Halfling · Alt: 1 · Weak: focus pool fragile
 6  Dirge Pure            ★ — Frightened 1 all enemies free + Fatal Aria finisher · Gnome or Elf · Alt: 4 · Weak: no Inspire Courage
 7  Polymath Spellbook    ⚠️ — Occult + Arcane via Wizard Ded. + any tradition L11 · Ancient Elf · Alt: 3 · Weak: preparation complexity
 8  Enigma Stratagem        — Bardic Lore + Devise a Stratagem precision · Halfling · Alt: 4 · Weak: MAD
 9  Maestro Summoner        — Inspire Courage + eidolon companion from L2 · Gnome · Alt: 1 · Weak: pet micromanagement
10  Warrior Pure          ★ — Half-Orc frontline + no archetype tax + Orc Ferocity · Half-orc (Orc Ferocity) · Alt: 2 · Weak: no multiclass utility

Type a number (1-10). Type BACK to return to classes.
```

---

## [5] CHAMPION

```
CHAMPION — Role: reactive tank/defender, divine frontline
★ RECOMMENDED: 6 (new players, Pure LoH) · 2 (shield tank) · 4 (redeemer)
⚠️ AVOID IF NEW: 3 (dual focus) · 9 (evil alignment required in-game)

 1  Radiant Reach         ★ — Guisarme reach tank + Retributive Strike + Divine Wall · Human or Dwarf · Alt: 6 · Weak: 2H means no shield
 2  Shield Bastion        ★ — Tower shield + Bastion Ded. + fortress mode · Dwarf or Human · Alt: 10 · Weak: low Speed
 3  Paladin Dual Focus    ⚠️ — Retributive Strike + Oracle Ded. + dual focus · Human · Alt: 6 · Weak: focus pool juggling
 4  Shield of Purity      ★ — Redeemer Sarenrae + Longsword+Shield + STR 18 · Half-elf or Human · Alt: 7 · Weak: no personal nova
 5  Liberator Mobile        — Liberating Step + 35 ft speed + finesse · Nimble Elf · Alt: 8 · Weak: lower AC
 6  Paladin Pure LoH      ★ — Retributive Strike + max Lay on Hands, no arch. · Human or Dwarf · Alt: 1 · Weak: reaction-starved
 7  Redeemer Dual Focus     — Glimpse + Oracle Ded. + curse aura · Human · Alt: 4 · Weak: dual focus
 8  Liberator Ranged        — Liberating Step + Gunslinger Ded. + gun · Human · Alt: 5 · Weak: reload economy
 9  Tyrant Cause          ⚠️ — Selfish Shield + fear aura + Intimidation (evil) · Orc or Hobgoblin · Alt: 4 · Weak: kingdom reputation cost
10  Pure Shield Ally        — Tower shield + shield feats, no archetype · Dwarf · Alt: 2 · Weak: narrow, no offense

Type a number (1-10). Type BACK to return to classes.
```

---

## [6] CLERIC

```
CLERIC — Role: divine caster, font healing or martial Warpriest
★ RECOMMENDED: 2 (new players, Cloistered heal) · 1 (Warpriest melee) · 7 (pure martial)
⚠️ AVOID IF NEW: 4 (Magus action economy) · 9 (Exemplar timing)

 1  Warpriest Font        ★ — Heal font + Channel Smite · Dwarf or Human · Alt: 7 · Weak: lower accuracy
 2  Cloistered Heal       ★ — 2 bonus font slots + max dice · Halfling or Gnome · Alt: 6 · Weak: fragile in melee
 3  Deadly Simplicity       — Deadly Simplicity + Channel Smite · Orc or Human · Alt: 1 · Weak: deity restrictions
 4  Harm-Spammer          ⚠️ — Cloistered + Negative Font + Cast Down (auto-prone) · Human · Alt: 9 · Weak: action economy
 5  Mystery Font Healer     — Oracle Ded. + dual focus · Human · Alt: 3 · Weak: curse management
 6  Inspire Word            — Bard Ded. + Inspire Courage · Halfling · Alt: 2 · Weak: limited font
 7  Warpriest Pure        ★ — Martial chain + no archetype · Human · Alt: 1 · Weak: average DPR
 8  Impulse Font            — Kineticist Ded. + impulse heal · Dwarf (Crimson Shroud) · Alt: 4 · Weak: MAD
 9  Grave-Warden Warpriest  — Warpriest Pharasma + Dwarf + Warhammer + WIS 18 · Dwarf (Strong-Blooded) · Alt: 3 · Weak: deity-locked
10  Firebrand               — Cloistered + Sarenrae + Fireball/Wall of Fire blaster · Human or Elf · Alt: 3 · Weak: fire-immune bosses

Type a number (1-10). Type BACK to return to classes.
```

---

## [7] COMMANDER

```
COMMANDER — Role: tactical buffer, banner-based battlefield control
★ RECOMMENDED: 1 (new players, tactics) · 5 (CHA support) · 9 (frontline)
⚠️ AVOID IF NEW: 3 (archetype complexity) · 6 (steep tactic cost)

 1  Tactical              ★ — Folio of Tactics + Battlefield Coordination · Human or Halfling · Alt: 6 · Weak: action-heavy first round
 2  Retributive Banner      — War Banner + Champion Ded. + Retributive Strike · Human or Dwarf · Alt: 9 · Weak: dual reaction management
 3  Strategist Spellcaster ⚠️ — Wizard Ded. + arcane control · Ancient Elf · Alt: 10 · Weak: prep fragility
 4  Vanguard Melee          — Greatsword frontline + Diehard · Orc or Human · Alt: 9 · Weak: no inspire
 5  Inspirational Support ★ — CHA 20 + morale chain · Human or Half-elf · Alt: 10 · Weak: fragile personal AC
 6  Tactical Overlord     ⚠️ — Hobgoblin Elvenbane + Longsword + Breastplate + INT 18 · Hobgoblin (Elvenbane) · Alt: 1 · Weak: steep learning curve
 7  Rallying Banner         — War Banner + Bard Ded. + Inspire Courage · Halfling · Alt: 2 · Weak: narrow action pool
 8  Strategist Investigator — Devise a Stratagem + precision · Halfling · Alt: 3 · Weak: MAD
 9  Vanguard Fighter      ★ — Fighter Ded. + Attack of Opportunity · Human or Orc · Alt: 4 · Weak: less banner uptime
10  Inspirational Oracle    — Oracle Ded. + Healer's Light · Human · Alt: 5 · Weak: curse pressure

Type a number (1-10). Type BACK to return to classes.
```

---

## [8] DRUID

```
DRUID — Role: primal caster, shape-shifter, companion master
★ RECOMMENDED: 6 (new players, Wild Shape) · 3 (Leaf heal) · 7 (companion)
⚠️ AVOID IF NEW: 1 (Wild Shape+Monk MAD) · 10 (dual fire source)

 1  Wild Shape Ki Strike  ⚠️ — Wild Shape + Monk Ded. + Ki Strike, untouchable melee · Human · Alt: 6 · Weak: MAD (STR/WIS/DEX)
 2  Wild Pet Army           — Wild Shape + Companion + eidolon, three bodies from L3 · Gnome · Alt: 7 · Weak: action overhead
 3  Leaf Healer           ★ — Goodberry + Verdant Burst, best primal support · Halfling or Gnome · Alt: 9 · Weak: Primal heal slower than Divine
 4  Flame Blaster           — Blazing Wave + fire spells, raw elemental output · Elf or Human · Alt: 10 · Weak: fire-immune enemies
 5  Wave Controller         — Tidal Surge push/prone, water battlefield control · Human · Alt: 8 · Weak: needs open terrain
 6  Wild Shape Pure       ★ — No archetype, max form depth, Dragon Shape nova · Human or Orc · Alt: 1 · Weak: narrow without archetype
 7  Animal Companion Pure ★ — No archetype, Specialized companion at L8 · Halfling (Mount) · Alt: 2 · Weak: companion action dependency
 8  Storm Blaster           — Tempest Surge pure lightning, no archetype tax · Elf · Alt: 4 · Weak: one element
 9  Dual Font Leaf          — Goodberry + divine Font, dual healing tradition · Halfling · Alt: 3 · Weak: prep juggling
10  Elemental Channel Flame ⚠️ — Blazing Wave + fire impulse, two fire sources · Dwarf (Crimson) · Alt: 4 · Weak: MAD, one resist kills output

Type a number (1-10). Type BACK to return to classes.
```

---

## [9] EXEMPLAR

```
EXEMPLAR — Role: Transcendence burst hero, ikon-focused champion
★ RECOMMENDED: 1 (new players, Victor's Wreath) · 3 (Sky Chariot mobility) · 7 (pure)
⚠️ AVOID IF NEW: 2 (Monk hybrid MAD) · 10 (ancestor rules complexity)

 1  Victor's Wreath       ★ — Wound-scaling Transcendence, unkillable · Human or Orc · Alt: 6 · Weak: starts soft L1–4
 2  Steel on Steel + Monk ⚠️ — Weapon Ikon + ki fused with Spark · Human · Alt: 9 · Weak: MAD
 3  Sky Chariot           ★ — +10 ft divine speed, 1-action Stride+Strike · Nimble Elf · Alt: 8 · Weak: no tank tools
 4  Gaze Sharp as Steel     — Flat-footed Spark + precision nova · Halfling or Human · Alt: 10 · Weak: relies on flat-foot
 5  Divine Ikon Support     — Triple ikon, Share Transcendence · Human · Alt: 6 · Weak: lower personal output
 6  Ikon of the Eternal     — Dying –1, TempHP per hit, Undying Glory · Dwarf or Human · Alt: 1 · Weak: no mobility
 7  Transcendence Pure    ★ — No archetype, 3 surges/day by L17 · Human · Alt: 1 · Weak: linear progression
 8  Sky Chariot Pure        — No archetype, immune to difficult terrain · Elf · Alt: 3 · Weak: narrow role
 9  Steel Perfection        — No archetype, Master's Spark fires twice · Human · Alt: 2 · Weak: late bloomer
10  Gaze of the Ancestors ⚠️ — Ancestor echoes independent from L5 · Orc or Kobold · Alt: 4 · Weak: rule-heavy

Type a number (1-10). Type BACK to return to classes.
```

---

## [10] FIGHTER

```
FIGHTER — Role: highest weapon accuracy, reaction-heavy martial
★ RECOMMENDED: 1 (new players) · 4 (tank) · 8 (archer)
⚠️ AVOID IF NEW: 3 (Flurry MAD) · 7 (wrestler action chains)

 1  Two-Handed Striker Fighter ★ — Power Attack + Exacting Strike, nova from L3 · Human or Orc · Alt: 10 · Weak: no ranged option
 2  Great Pick Fatal Fighter    — Greatpick Fatal d12 + Shatter Defenses crit-chain · Orc or Human · Alt: 1 · Weak: crit-variance dependent
 3  Agile Dual Wield Fighter ⚠️ — Double Slice + Agile Grace + Twin Takedown · Human or Elf · Alt: 6 · Weak: MAD (STR+DEX)
 4  Shield Bastion Fighter    ★ — Shield Block + Bastion Ded. + reaction chain · Dwarf or Human · Alt: 9 · Weak: low mobility
 5  Polearm Master              — Guisarme reach/trip + Human Skilled + STR 18 + AoO chain · Human (Skilled) · Alt: 10 · Weak: reach weapon required
 6  Rapier Finesse Fighter      — Double Slice + Rapier deadly d8 + Twin Takedown · Human · Alt: 3 · Weak: specific weapon pair
 7  Trip Grapple Fighter     ⚠️ — Knockdown + Combat Grab, pin build · Orc or Goliath · Alt: 5 · Weak: action-chain sensitive
 8  Longbow Archer Fighter   ★ — Longbow + Triple Shot, steady DPR · Elf or Human · Alt: 2 · Weak: no control tools
 9  Intercepting Shield Fighter — Guardian Ded. + Intercepting Shield, redirect hits · Dwarf · Alt: 4 · Weak: lower offense
10  Reach Sentinel Fighter   ★ — Attack of Opportunity + Sentinel + Halberd, max zone · Human · Alt: 5 · Weak: needs enemies to move

Type a number (1-10). Type BACK to return to classes.
```

---

## [11] GUARDIAN

```
GUARDIAN — Role: damage-soaker tank, ally-protector
★ RECOMMENDED: 1 (new players, Hit-Me) · 5 (Shield Wall) · 6 (Mountain HP)
⚠️ AVOID IF NEW: 9 (dual reaction juggling)

 1  Hit-Me Tank           ★ — Toughness + Full Plate + CON 18 · Dwarf · Alt: 6 · Weak: low DPR
 2  Protector + Champion    — Shield Block + Lay on Hands react · Dwarf or Human · Alt: 7 · Weak: MAD (CON+CHA)
 3  Fortress Builder        — Fortress Stance + Halberd reach · Dwarf (Stone) · Alt: 8 · Weak: needs terrain control
 4  Retaliation Striker     — Retaliatory Strike on hit · Orc or Human · Alt: 9 · Weak: reactive only
 5  Party Shield Wall     ★ — Shield Warden + Tower Shield · Dwarf · Alt: 10 · Weak: movement penalty
 6  Mountain Pure HP      ★ — Dwarf Mountain Stoutness + CON 20 · Dwarf (Stone) · Alt: 1 · Weak: narrow
 7  Protector + Bard        — Inspire Courage + Shield Block · Halfling · Alt: 2 · Weak: fragile AC
 8  Fortress Pure Terrain   — Stone Dwarf + Fortress Stance chokepoint · Dwarf · Alt: 3 · Weak: open-field weak
 9  Retaliation + Champion ⚠️ — Strike + Lay on Hands dual react · Dwarf or Human · Alt: 4 · Weak: react-starved
10  Party Wall Pure         — Shieldwall aura · Dwarf · Alt: 5 · Weak: no offense

Type a number (1-10). Type BACK to return to classes.
```

---

## [12] GUNSLINGER

```
GUNSLINGER — Role: ranged DPR with reload economy, alpha-strike
★ RECOMMENDED: 4 (new players, Pistolero) · 2 (fatal sniper) · 6 (Drifter)
⚠️ AVOID IF NEW: 1 (Spellshot MAD) · 5 (AoE positioning + friendly-fire)

 1  Spellshot Hybrid      ⚠️ — Arcane Reloading: spell+bullet 1 action · Ancient Elf · Alt: 10 · Weak: MAD
 2  Sniper Fatal           ★ — Arquebus fatal d12 + Aimed Shot · Elf or Human · Alt: 9 · Weak: no melee backup
 3  Drifter Melee Bypass    — Sword and Pistol: reload+melee 2 actions · Human · Alt: 7 · Weak: reload timing
 4  Pistolero Debuff       ★ — Pistol Twirl free Demoralize · Half-elf or Halfling · Alt: 7 · Weak: fragile
 5  Vanguard Bombardier   ⚠️ — Blunderbuss scatter + Covering Fire · Dwarf or Orc · Alt: 8 · Weak: friendly-fire risk
 6  Drifter Pure Reload     — Vicious Reload chain · Human · Alt: 3 · Weak: narrow role
 7  Pistolero + Swashbuckler — Panache + Finishers · Halfling · Alt: 4 · Weak: MAD (DEX+CHA)
 8  Vanguard Pure AoE      — Scatter Blast + Point-Blank · Dwarf · Alt: 5 · Weak: needs grouped enemies
 9  Fake Out Sniper         — Kobold Strongjaw + Arquebus + Fake Out + Aimed Shot · Kobold (Strongjaw) · Alt: 2 · Weak: ancestry-locked
10  Spellshot Pure          — Spell Volley + Impossible Reload · Ancient Elf · Alt: 1 · Weak: MAD

Type a number (1-10). Type BACK to return to classes.
```

---

## [13] INVENTOR

```
INVENTOR — Role: gadget-based martial or construct master, Overdrive DPR
★ RECOMMENDED: 9 (new players, Weapon+Fighter) · 4 (bomb blaster) · 2 (tank)
⚠️ AVOID IF NEW: 5 (Unstable self-damage risk) · 3 (construct micromanagement)

 1  Weapon Innov + Magus      — Overdrive rapier + Spellstrike nova · Human or Elf · Alt: 9 · Weak: MAD
 2  Armor Tank + Guardian   ★ — Armor mods + Shield Block fortress · Dwarf · Alt: 7 · Weak: low mobility
 3  Construct + Summoner    ⚠️ — Construct + eidolon pet-army · Gnome · Alt: 8 · Weak: action overhead
 4  Explosive Blaster       ★ — Bomb Innov + Explode AoE deletion · Goblin or Gnome · Alt: 10 · Weak: limited uses/day
 5  Unstable Overcharge     ⚠️ — Greataxe + Unstable Overcharge nova · Orc or Human · Alt: 1 · Weak: self-damage risk
 6  Construct Support + Bard  — Construct gadgets + Inspire support · Gnome · Alt: 10 · Weak: fragile
 7  Armor + Champion          — Armor mods + reaction tank · Dwarf · Alt: 2 · Weak: MAD
 8  Construct + Ranger        — Construct + Hunt Prey sniper · Halfling · Alt: 3 · Weak: MAD
 9  Weapon + Fighter        ★ — Weapon Innov + Fighter accuracy · Human or Orc · Alt: 1 · Weak: single-target only
10  Pure Inventor Utility     — Full class kit, crafting god · Gnome or Human · Alt: 4 · Weak: average combat

Type a number (1-10). Type BACK to return to classes.
```

---

*KM_BuildGuide.md v2.0 — 130 builds, classes 1–13*
*See KM_BuildGuide.md for classes 14–27 (Investigator through Wizard)*


---

<!-- merged from KM_BuildGuide.md (v93.21 file consolidation) -->

# KINGMAKER — BUILD GUIDE B (Classes 14–27)
## KM_BuildGuide.md | Referenced by: KM_BuildGuide.md, KM_Companions_Behaviors.md

> **DM:** After the player picks a class number from KM_BuildGuide.md, display ONLY that class's block below. This file is the single source for both build lists and advisory — display the block, prompt once. Do NOT load a separate lists file. Do NOT ask twice. Do NOT generate builds from memory = `.fail 9`.
>
> **Badges:** ★ = recommended (new players or strong overall) · ⚠️ = complex/MAD/niche · no badge = solid pick
> **Format per build:** compact mechanic · preferred ancestry · Alt-build pointer · weakness/caveat
> For classes 1–13 see KM_BuildGuide.md.

---

## [14] INVESTIGATOR

```
INVESTIGATOR — Role: Devise-a-Stratagem precision, skill-rich detective
★ RECOMMENDED: 1 (new players, rogue dip) · 6 (pure support) · 10 (team enabler)
⚠️ AVOID IF NEW: 3 (alchemical action chain) · 9 (thaumaturge layering)

 1  Forensic + Rogue         ★ — Forensic + Rogue Ded. + Sneak Attack crit · Halfling or Human · Alt: 6 · Weak: requires flat-foot
 2  Empiricist + Psychic       — Empiricist + Psychic Ded. + Stratagem + amp cantrips · Ancient Elf · Alt: 7 · Weak: MAD (INT+CHA)
 3  Alchemical + Alchemist   ⚠️ — Bomb-Devise precision hybrid · Goblin or Gnome · Alt: 10 · Weak: action heavy
 4  Stratagem Sniper           — Ranged Stratagem boss killer · Elf · Alt: 7 · Weak: no melee
 5  Strategist + Commander     — Devise + banner tactics · Human · Alt: 10 · Weak: MAD
 6  Forensic Medicine Investigator ★ — Forensic Medicine + Medic Ded. + Battle Medicine doubled · Halfling or Gnome · Alt: 1 · Weak: combat output average
 7  Empiricist + Wizard        — Empiricist + Wizard Ded. + Devise + True Strike combo · Ancient Elf · Alt: 2 · Weak: prep tax
 8  Rogue Dedication Melee     — Gang-up + Twin Feint flat-foot · Human or Halfling · Alt: 1 · Weak: needs ally positioning
 9  Thaumaturge Implement    ⚠️ — Exploit Vulnerability layered · Human · Alt: 2 · Weak: ruleset-heavy
10  Pure Support Investigator ★ — Battle Medicine + Ward Medic · Halfling · Alt: 6 · Weak: low DPR

Type a number (1-10). Type BACK to return to classes.
```

---

## [15] KINETICIST

```
KINETICIST — Role: at-will elemental impulse caster (blaster, tank, or control)
★ RECOMMENDED: 1 (new players, multi-element) · 5 (pure blaster) · 10 (tank)
⚠️ AVOID IF NEW: 7 (Spellstrike timing) · 9 (size rules)

 1  Element Blaster/Tank    ★ — Multi-element impulse DPR god · Dwarf (Crimson Shroud) · Alt: 5 · Weak: gateway decisions matter
 2  Everbloom Bastion         — Wood+Earth + Fresh Produce infinite heal + terrain wall · Halfling or Gnome · Alt: 10 · Weak: low burst damage
 3  Fire/Earth Fortress        — AoE + tank hybrid remaster · Dwarf · Alt: 10 · Weak: slow movement
 4  Water Control + Guardian   — Redirect + impulse tank · Dwarf · Alt: 3 · Weak: fire-immune enemies weaken output
 5  Pure Impulse Blaster     ★ — Consistent elemental king · Dwarf or Gnome · Alt: 1 · Weak: needs element diversity vs resistances
 6  Metal Weapon + Fighter     — Impulse weapon mastery · Human or Orc · Alt: 7 · Weak: split focus
 7  Kinetic + Magus          ⚠️ — Spellstrike impulses · Human · Alt: 6 · Weak: complex action chains
 8  Aura Support + Bard        — Party elemental buffs · Gnome · Alt: 10 · Weak: fragile personal
 9  Jotunborn Size Impulse   ⚠️ — Massive reach blaster · Goliath or Orc · Alt: 1 · Weak: specific ancestry required
10  Pure Tank Kineticist     ★ — Unbreakable elemental wall · Dwarf (Stone) · Alt: 4 · Weak: low offense

Type a number (1-10). Type BACK to return to classes.
```

---

## [16] MAGUS

```
MAGUS — Role: Spellstrike melee/ranged caster, boss-round nova
★ RECOMMENDED: 6 (new players, Pure) · 3 (Twisting Tree reach) · 1 (Iron)
⚠️ AVOID IF NEW: 4 (Psychic amp timing) · 8 (Kineticist impulse chain)

 1  Spellstrike Hybrid      ★ — Inexorable Iron + Force Fang nova · Human or Orc · Alt: 3 · Weak: spell pool fragile
 2  Dimensional Striker       — Starlit Span + Archer Ded. + Expansive AoE + AoO ranged · Nimble Elf · Alt: 9 · Weak: no melee option
 3  Twisting Tree Melee     ★ — Polearm reach Spellstrike · Human · Alt: 1 · Weak: 2-handed only
 4  Psychic Amp + Magus     ⚠️ — Amped Force Fang focus spam · Ancient Elf · Alt: 6 · Weak: MAD
 5  Warpriest Strike + Cleric  — Divine Spellstrike via greataxe · Human · Alt: 6 · Weak: MAD (STR+WIS+INT)
 6  Pure Spellstrike        ★ — Laughing Shadow, no dip, classic king · Human or Half-elf · Alt: 10 · Weak: no archetype safety net
 7  Exemplar Ikon + Magus     — Transcendence surge nova · Human · Alt: 1 · Weak: dual resource pool
 8  Impulse Spellstrike     ⚠️ — Elemental Spellstrike bypass · Human · Alt: 7 · Weak: heavy ruleset
 9  Power Attack Accuracy     — Crit machine, Power Attack + Legendary weapon · Human or Orc · Alt: 6 · Weak: lower spell DC
10  Support Magus             — Laughing Shadow + Bard Ded. + Inspire Courage buff · Half-elf or Human · Alt: 6 · Weak: lower personal DPR

Type a number (1-10). Type BACK to return to classes.
```

---

## [17] MONK

```
MONK — Role: unarmed striker, stance-based battlefield specialist
★ RECOMMENDED: 5 (new players, Pure Flurry) · 4 (Crane/Wolf mobility) · 3 (tank)
⚠️ AVOID IF NEW: 1 (Kineticist action compression) · 7 (Magus ki chain)

 1  Flurry + Kineticist    ⚠️ — Stunning + impulse, action compression · Dwarf or Human · Alt: 8 · Weak: MAD
 2  Wild Shape + Druid       — Untouchable shifter tank · Human or Goliath · Alt: 9 · Weak: form transition action
 3  Stance Master + Guardian ★ — Mountain/Ironblood wall · Dwarf · Alt: 10 · Weak: no ranged
 4  Crane/Wolf Stance Striker ★ — Mobility + Trip control · Nimble Elf or Halfling · Alt: 10 · Weak: AC-reactive stances
 5  Pure Flurry Agile      ★ — 3 hits/action by L15 · Human (Ambition) or Halfling · Alt: 4 · Weak: no AoE
 6  Exemplar Steel + Monk    — Ikon handwraps, martial perfection · Human · Alt: 1 · Weak: dual-resource
 7  Ki Spellblade + Magus  ⚠️ — Spellstrike through Flurry · Human · Alt: 1 · Weak: rules-heavy
 8  Water Stance Control     — Push/Slow battlefield lockdown · Human · Alt: 4 · Weak: needs positioning
 9  Jotunborn Giant Stance   — 20 ft reach Dragon Stance · Goliath or Orc · Alt: 2 · Weak: specific ancestry
10  Pure Support             — Stunning Fist + Wholeness of Body + Ki Blast utility · Human · Alt: 5 · Weak: limited damage output

Type a number (1-10). Type BACK to return to classes.
```

---

## [18] ORACLE

```
ORACLE — Role: curse-fueled caster, mystery-themed specialist
★ RECOMMENDED: 6 (new players, Life heal) · 1 (Battle melee) · 5 (Curse control)
⚠️ AVOID IF NEW: 4 (Animist hybrid) · 10 (flexible mystery)

 1  Battle Mystery + Warpriest ★ — Curse-free striker · Human or Orc · Alt: 8 · Weak: martial chassis modest
 2  Bones Mystery Heal/Tank    — Immortal support (remaster) · Dwarf or Human · Alt: 6 · Weak: curse pressure
 3  Flames Mystery Blaster     — Raw AoE fire nova · Elf · Alt: 7 · Weak: fire-immune bosses
 4  Ancestors Mystery + Animist ⚠️ — Spirit hybrid, dual focus · Orc or Human · Alt: 10 · Weak: ruleset-heavy
 5  Pure Curse Control       ★ — Debuff god, Extreme nova trigger · Human · Alt: 9 · Weak: curse snowball risk
 6  Life Mystery + Cleric    ★ — Infinite healing with Life Link · Halfling or Gnome · Alt: 2 · Weak: fragile personal
 7  Tempest Mystery + Kineticist — Storm synergy, AoE lightning · Human · Alt: 3 · Weak: MAD
 8  Warrior Mystery Melee      — Martial oracle frontline · Human or Orc · Alt: 1 · Weak: low spell DC
 9  Cosmos Mystery Support     — Party buffs + Void aura · Elf · Alt: 5 · Weak: niche
10  Pure Mystery Spellblade  ⚠️ — Flexible caster, any mystery · Human · Alt: 5 · Weak: indecision cost

Type a number (1-10). Type BACK to return to classes.
```

---

## [19] PSYCHIC

```
PSYCHIC — Role: focus-spell amplifier, amped cantrip nova
★ RECOMMENDED: 5 (new players, Pure amp) · 2 (Puppet control) · 3 (blaster)
⚠️ AVOID IF NEW: 7 (Investigator stratagem) · 9 (Magus mindsmith)

 1  Amp Focus Spam + Bard    — Infinite focus nova via Lingering · Halfling · Alt: 5 · Weak: focus-recovery timing
 2  Puppet Master Control  ★ — Dominate king (remaster) · Human or Elf · Alt: 9 · Weak: Will-immune enemies
 3  Oscillating Wave Blaster ★ — Fire/cold alt, bypass resistance · Elf or Human · Alt: 5 · Weak: element-switch action
 4  TK Projectile + Fighter  — Precision ranged hybrid · Human · Alt: 10 · Weak: MAD
 5  Pure Amp Blaster       ★ — Focus-spell monster, max Amps · Human (Ambition) · Alt: 1 · Weak: no archetype utility
 6  Bloodline Amp            — Sorcerer bloodline + amp crossover, dual tradition · Human · Alt: 10 · Weak: prep complexity
 7  Investigator Stratagem ⚠️ — Pre-rolled Amped crits · Halfling · Alt: 4 · Weak: MAD
 8  Support Amp Buffer       — Party-wide Amp auras · Halfling or Gnome · Alt: 1 · Weak: fragile
 9  Mindsmith + Magus      ⚠️ — Psychic Spellstrike weapon · Human · Alt: 4 · Weak: rules-heavy
10  The Chronos Master       — Infinite Eye + Precise Discipline + Human Skilled + INT 18 staff · Human (Skilled) · Alt: 6 · Weak: setup-heavy, niche

Type a number (1-10). Type BACK to return to classes.
```

---

## [20] RANGER

```
RANGER — Role: Hunt Prey precision, dual-weapon or ranged hunter
★ RECOMMENDED: 5 (new players, Pure Flurry) · 3 (Archer) · 8 (Ghost-Wolf)
⚠️ AVOID IF NEW: 4 (Druid dip prep) · 9 (Gunslinger reload)

 1  Flurry Hunter          ★ — Twin Takedown + precision, multi-attack delete · Human or Half-elf · Alt: 5 · Weak: MAD
 2  Animal Companion + Summoner — Pet army, wolf + eidolon · Gnome · Alt: 8 · Weak: action overhead
 3  Archer Sniper          ★ — Fatal + deadly, boss-killer at 100 ft · Elf or Human · Alt: 9 · Weak: no melee fallback
 4  Warden Spells + Druid  ⚠️ — Primal hybrid, dual slot pool · Human · Alt: 10 · Weak: prep-day juggling
 5  Pure Flurry            ★ — No dedication, consistent martial DPR · Human (Ambition) · Alt: 1 · Weak: no archetype
 6  Monster Hunter Debuff    — Precision + Frightened/Flat-Footed · Half-elf · Alt: 10 · Weak: action chain
 7  Guardian Redirect + Ranger — Tank + hunt hybrid · Dwarf · Alt: 8 · Weak: lower mobility
 8  Ghost-Wolf Hunter      ★ — Outwit + Wolf auto-trip + Monster Hunter flanking · Human or Half-elf · Alt: 2 · Weak: companion-dependent
 9  Crossbow Ace + Gunslinger ⚠️ — Gun/ranged hybrid, Aimed Shot · Human · Alt: 3 · Weak: reload timing
10  Support Ranger           — Warden's Boon + Inspire Courage party buff · Half-elf · Alt: 6 · Weak: lower personal DPR

Type a number (1-10). Type BACK to return to classes.
```

---

## [21] ROGUE

```
ROGUE — Role: Sneak Attack precision, skill-monkey specialist
★ RECOMMENDED: 5 (new players, Opportunistic) · 6 (Thief mobility) · 1 (crit)
⚠️ AVOID IF NEW: 4 (cantrip Sneak timing) · 8 (poison chain)

 1  Scoundrel + Thaumaturge ★ — Sneak + Exploit Vulnerability · Half-elf or Human · Alt: 3 · Weak: implement juggling
 2  Ruffian + Magus          — Brutal Spellstrike, heavy hitter · Human or Orc · Alt: 7 · Weak: MAD
 3  Mastermind Precision + Investigator — Stratagem crits · Halfling · Alt: 1 · Weak: pre-roll planning
 4  Eldritch Trickster + Psychic ⚠️ — Sneak Attack on cantrips · Ancient Elf · Alt: 8 · Weak: MAD, timing-sensitive
 5  Opportunistic Thief    ★ — Thief + Trap Finder + Gang Up + Precise Debilitations · Halfling or Human · Alt: 6 · Weak: needs positioning + ally
 6  Thief Dexterity God    ★ — 35 ft + skill god + mobility · Nimble Elf · Alt: 5 · Weak: no weapon versatility
 7  Gang Up + Fighter        — AoO + Opportune Backstab reactions · Human · Alt: 2 · Weak: needs ally positioning
 8  Poison + Alchemist     ⚠️ — Sticky Poison + Brutal Strikes · Goblin or Gnome · Alt: 4 · Weak: poison DC vs boss Fort
 9  Shadowdancer Stealth     — Hide in Plain Sight + Shadow Walk · Elf or Halfling · Alt: 10 · Weak: lighting dependency
10  Support Debuff Rogue     — Methodical Debilitations party enable · Halfling · Alt: 3 · Weak: low personal DPR

Type a number (1-10). Type BACK to return to classes.
```

---

## [22] SORCERER

```
SORCERER — Role: spontaneous caster, bloodline-themed blaster or controller
★ RECOMMENDED: 1 (new players, Draconic) · 5 (Pure flex) · 3 (Psychic)
⚠️ AVOID IF NEW: 7 (Aberrant mental) · 10 (Imperial niche)

 1  Draconic Blaster       ★ — Draconic bloodline, flat damage, highest spell DPR · Human or Orc · Alt: 8 · Weak: element resistance
 2  Elemental + Kineticist   — Elemental bloodline, impulse synergy dual source · Dwarf · Alt: 8 · Weak: MAD
 3  Psychic Bloodline Amp  ★ — Psychic bloodline, focus spell spam via amps · Halfling · Alt: 5 · Weak: focus recovery
 4  Shadow Control          — Shadow bloodline, debuff king, darkness battlefield · Elf · Alt: 9 · Weak: light-based counters
 5  Pure Spontaneous       ★ — No dedication, versatile blaster, broadest access · Human · Alt: 1 · Weak: no archetype safety
 6  Divine + Cleric          — Divine bloodline, heal + damage hybrid Font · Human · Alt: 1 · Weak: prep complexity
 7  Aberrant Support       ⚠️ — Aberrant bloodline, mind control and Dominate · Elf or Human · Alt: 4 · Weak: Will-immune counters
 8  Storm + Druid            — Storm bloodline, primal hybrid, AoE lightning · Elf · Alt: 2 · Weak: indoors weak
 9  Transcendence Sorcerer   — Draconic + Exemplar Ded. + Transcendence nova · Human · Alt: 4 · Weak: dual resource pool
10  Bloodline Buffer       ⚠️ — Party enabler, Imperial bloodline, Inspire substitute · Human · Alt: 3 · Weak: narrow niche

Type a number (1-10). Type BACK to return to classes.
```

---

## [23] SUMMONER

```
SUMMONER — Role: eidolon master, two-body action economy
★ RECOMMENDED: 5 (new players, Pure eidolon) · 4 (Dragon) · 2 (tank)
⚠️ AVOID IF NEW: 1 (Magus Spellstrike through pet) · 9 (construct micromanagement)

 1  Martial Eidolon + Magus ⚠️ — Spellstrike through pet, hybrid army · Human · Alt: 5 · Weak: dual-body action tax
 2  Plant Tank + Guardian  ★ — Evolution eidolon, unkillable pet wall · Dwarf or Human · Alt: 7 · Weak: offense modest
 3  Caster Summoner + Bard   — Composition buffs, pet-army synergy · Halfling · Alt: 10 · Weak: MAD
 4  Dragon Eidolon Blaster ★ — Breath weapon + strikes, aerial frontline · Human or Elf · Alt: 5 · Weak: breath economy
 5  Pure Eidolon Striker   ★ — No dip, consistent pet DPR, max evolutions · Human · Alt: 1 · Weak: linked-HP risk
 6  Incarnate + Exemplar     — Transcendence channeled through eidolon · Human or Orc · Alt: 1 · Weak: dual-resource
 7  Animal Eidolon + Ranger  — Hunt Prey shared, companion synergy · Halfling · Alt: 2 · Weak: specific feat tax
 8  Phantom Support          — Spirit eidolon, Protection Aura, buff focus · Gnome · Alt: 3 · Weak: fragile
 9  Construct + Inventor   ⚠️ — Gadget eidolon, mechanical pet flexibility · Gnome · Alt: 1 · Weak: rules-heavy
10  Utility Summoner         — Flexible pet control, skill + social coverage · Halfling · Alt: 3 · Weak: combat modest

Type a number (1-10). Type BACK to return to classes.
```

---

## [24] SWASHBUCKLER

```
SWASHBUCKLER — Role: Panache mobility striker, Finisher-based DPR
★ RECOMMENDED: 5 (new players, Pure Panache) · 3 (Precision rogue) · 6 (Wit)
⚠️ AVOID IF NEW: 1 (Gunslinger reload) · 2 (grapple chain)

 1  Panache + Gunslinger   ⚠️ — Fencer pistolero, Pistol Twirl free Demoralize → Panache · Halfling or Human · Alt: 4 · Weak: reload timing
 2  Gymnast Grapple + Monk ⚠️ — Flurry compresses Grapple → Strike → Strike · Human or Orc · Alt: 7 · Weak: MAD
 3  Fencer Precision + Rogue ★ — Sneak Attack + Precise Strike crit machine · Half-elf or Human · Alt: 5 · Weak: needs flat-foot
 4  Braggart + Bard          — Demoralize loop + Inspire Courage buff · Half-elf or Halfling · Alt: 6 · Weak: fragile
 5  Pure Panache Striker   ★ — No dip, mobility DPR, Finisher depth · Human or Halfling · Alt: 3 · Weak: no archetype
 6  Wit Support            ★ — Bon Mot Panache + −2 Will/Perception · Gnome or Halfling · Alt: 10 · Weak: low personal DPR
 7  Swash + Fighter          — Legendary weapon + Attack of Opportunity · Human · Alt: 5 · Weak: loses Panache mobility
 8  Pirate + Commander       — Rally banner + Frightened stack · Half-elf · Alt: 4 · Weak: MAD
 9  Battledancer Aura        — Performance Panache + Inspire bubble · Halfling · Alt: 6 · Weak: sustain dependency
10  Pure Support Swash       — Wit + Charmed Life party enabler · Halfling · Alt: 6 · Weak: averaged output

Type a number (1-10). Type BACK to return to classes.
```

---

## [25] THAUMATURGE

```
THAUMATURGE — Role: Exploit Vulnerability specialist, three-implement layered
★ RECOMMENDED: 1 (new players, Regalia) · 5 (Pure) · 6 (Chalice)
⚠️ AVOID IF NEW: 7 (Psychic amp) · 8 (Exemplar surge)

 1  Regalia Thaumaturge    ★ — Regalia implement + Gnome Wellspring + Whip reach + CHA 18 · Human or Half-elf · Alt: 5 · Weak: complex action routine
 2  Weapon Implement + Fighter — Martial hybrid, Legendary weapon ceiling · Human or Orc · Alt: 9 · Weak: lower Exploit uptime
 3  Cursed Saboteur        ★ — Bell+Wand+Mirror Save-Slayer debuff loop · Human · Alt: 1 · Weak: low single-target DPR
 4  Tome Implement + Investigator — Devise + pre-known weakness crits · Halfling · Alt: 9 · Weak: MAD
 5  Pure Implement Exploiter ★ — No dip, three implements passive stack · Human · Alt: 1 · Weak: no archetype
 6  Chalice Implement Support ★ — Regen + Regalia party heal, tanky · Halfling or Gnome · Alt: 1 · Weak: fragile AC
 7  Psychic Amp + Thaumaturge ⚠️ — Amped cantrips + Exploit nova · Human · Alt: 1 · Weak: MAD
 8  Exemplar Ikon Dip      ⚠️ — Transcendence surge through Weapon Implement · Human or Orc · Alt: 2 · Weak: dual-resource
 9  Rogue Sneak + Thaumaturge — Bell flat-foot + Sneak + Exploit triple · Halfling or Human · Alt: 1 · Weak: positioning-heavy
10  Pure Support Thaumaturge  — Bell+Regalia+Tome party force-multiplier · Halfling · Alt: 6 · Weak: combat modest

Type a number (1-10). Type BACK to return to classes.
```

---

## [26] WITCH

```
WITCH — Role: hex-based controller, familiar master, Patron-themed caster
★ RECOMMENDED: 5 (new players, Pure Hex) · 8 (Heal) · 10 (Utility)
⚠️ AVOID IF NEW: 2 (Hex Magus timing) · 7 (Spirit Patron complexity)

 1  Familiar + Alchemist     — Cauldron + bombs, infinite consumables · Gnome or Goblin · Alt: 10 · Weak: MAD
 2  Hex Magus              ⚠️ — Hex through Spellstrike, curse nova · Human or Elf · Alt: 5 · Weak: action-heavy
 3  Patron Spell + Wizard    — Fate Patron + arcane slots, dual tradition · Ancient Elf · Alt: 7 · Weak: prep juggling
 4  Cackle Support + Bard    — Inspire + Evil Eye sustained, party +1/−1 · Halfling · Alt: 5 · Weak: fragile
 5  Pure Hex Debuff        ★ — Evil Eye + Nudge + Misfortune stacked, control king · Gnome or Human · Alt: 4 · Weak: Will-immune counters
 6  Beastbound Familiar + Druid — Familiar + animal companion, pet synergy · Halfling or Gnome · Alt: 1 · Weak: action overhead
 7  Spirit Patron + Animist ⚠️ — Spirit hex, dual focus pool · Human · Alt: 3 · Weak: rules-heavy
 8  Lesson of Life Heal    ★ — Wilding Patron + curative Lessons, support witch · Halfling or Gnome · Alt: 4 · Weak: low personal DPR
 9  Hex-Bound Shepherd       — Resentment patron + Human Changeling + Raven familiar + Enfeeblement chain · Human (Changeling) · Alt: 5 · Weak: specific ancestry + patron required
10  Pure Utility Witch     ★ — Skill + crafting god, Cauldron + Speech familiar · Gnome · Alt: 5 · Weak: combat modest

Type a number (1-10). Type BACK to return to classes.
```

---

## [27] WIZARD

```
WIZARD — Role: prepared arcane caster, thesis-specialized
★ RECOMMENDED: 5 (new players, Pure Prepared) · 1 (Blaster) · 10 (Control)
⚠️ AVOID IF NEW: 2 (Spellstrike timing) · 9 (Ikon dual-resource)

 1  Spellbook Blaster + Psychic ★ — Evoker + Amped cantrips, highest spell DPR · Ancient Elf · Alt: 5 · Weak: focus-pool fragile
 2  School Specialist + Magus ⚠️ — Element school + Spellstrike, crit nova · Human or Elf · Alt: 8 · Weak: dual-pool juggling
 3  Bonded Item + Alchemist    — Recover spell/day + Cauldron, consumable spam · Gnome · Alt: 7 · Weak: MAD
 4  Universalist Utility + Investigator — Flexible Prep + Devise, knowledge god · Halfling · Alt: 10 · Weak: no nova focus
 5  Pure Prepared Blaster   ★ — Spell Blending thesis, no dip, versatile king · Human or Elf · Alt: 1 · Weak: no archetype safety
 6  Staff Specialist + Cleric  — Staff Nexus thesis + Heal Font, dual tradition · Dwarf · Alt: 3 · Weak: prep complexity
 7  Familiar + Witch           — Enhanced Familiar + Conduit, spells from familiar's square · Gnome · Alt: 3 · Weak: action overhead
 8  Battle Magic + Fighter     — Greatsword + arcane slots, front-line caster · Human or Orc · Alt: 2 · Weak: MAD
 9  Ikon Mage               ⚠️ — Evoker + Ikon surge, boss-round nova · Human · Alt: 5 · Weak: dual-resource
10  Support Control Wizard  ★ — Spell Substitution, Slow/Wall/Grease lockdown · Halfling or Gnome · Alt: 4 · Weak: no offensive nova

Type a number (1-10). Type BACK to return to classes.
```

---

*KM_BuildGuide.md v2.0 — 140 builds, classes 14–27*
*See KM_BuildGuide.md for classes 1–13 (Alchemist through Inventor)*


---

<!-- merged from KM_BuildGuide.md (v93.21 file consolidation) -->

# KINGMAKER — STARTING GEAR SELECTION
## KM_BuildGuide.md | Referenced by: KM_Builds.md

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
    See KM_Items.md § PRESET ADVENTURING PACKS.

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

Twelve named bundles from `KM_Items.md § PRESET ADVENTURING PACKS`.
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
1. Player types `P#`. Look up pack contents in `KM_Items.md`.
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

*KM_BuildGuide.md — Kingmaker PF2e Text Adventure | Starting Gear v1.0*


---

<!-- merged from KM_BuildGuide.md (v93.21 file consolidation) -->

# KINGMAKER — LEVEL-UP PROCEDURES
## KM_BuildGuide.md | Referenced by: KM_DMRules.md, KM_Ch1.md-KM_Ch7.md, KM_Commands.md, KM_Commands_Maps.md, KM_Combat_Systems.md, KM_Prologue_Systems.md, KM_Ch1.md-KM_Ch7.md, KM_PlayerHelp.md, KM_Spells.md, KM.txt, KM_P2.txt

> **DM:** This file contains XP thresholds, the player level-up procedure, and routing to companion leveling files. Load every session.

---

## 📊 XP THRESHOLDS (PF2e Standard)

| Level | XP Required | Cumulative XP |
|-------|-------------|---------------|
| 1 → 2 | 1,000 | 1,000 |
| 2 → 3 | 1,000 | 2,000 |
| 3 → 4 | 1,000 | 3,000 |
| 4 → 5 | 1,000 | 4,000 |
| 5 → 6 | 1,000 | 5,000 |
| 6 → 7 | 1,000 | 6,000 |
| 7 → 8 | 1,000 | 7,000 |
| 8 → 9 | 1,000 | 8,000 |
| 9 → 10 | 1,000 | 9,000 |
| 10 → 11 | 1,000 | 10,000 |
| 11 → 12 | 1,000 | 11,000 |
| 12 → 13 | 1,000 | 12,000 |
| 13 → 14 | 1,000 | 13,000 |
| 14 → 15 | 1,000 | 14,000 |
| 15 → 16 | 1,000 | 15,000 |
| 16 → 17 | 1,000 | 16,000 |
| 17 → 18 | 1,000 | 17,000 |
| 18 → 19 | 1,000 | 18,000 |
| 19 → 20 | 1,000 | 19,000 |

> PF2e Remaster uses a flat 1,000 XP per level. XP resets to 0 after each level-up in some tables — this project uses cumulative tracking. Both are valid; the save block uses cumulative.

---

## 🎯 PLAYER LEVEL-UP PROCEDURE

**Trigger:** Player's cumulative XP crosses the next threshold.

**Step 1 — Announce immediately (inline, mid-scene if necessary):**
```
[LEVEL UP — reached Level X!]
  XP    : [current] / [next threshold]
  HP    : +[class HP + Con mod] → [new total]
```

**Step 2 — Apply or present choices based on `player.leveling_mode` (NOT `companion_leveling_mode` — that field governs companions in the procedure below):**

**AUTO mode** (player opted in; preset builds NO LONGER auto-default to AUTO):
```
Apply all choices silently from the build map (KM_Builds_X.md row for this level):
  • Feats      : apply [PICK] feat from build map — announce inline
  • Skill inc  : apply class default signature skill
  • Ability boosts (5/10/15/20): apply in build-map priority order
  • Spell slots: apply per class table automatically
Format: append to the level-up block from Step 1 —
  Feat: [Feat Name] (auto — build map)
  Boost: [Stat] +2 → [new score]  (at L5/10/15/20 only)
Skip Step 3.
```

**ASK mode** (default when CUSTOM build; or player switched with `/mode ask`):
```
Present choices with ★ build-map recommendation marked:
  • Ability boosts (at levels 5, 10, 15, 20): four +2 boosts — list options, mark ★ priority
  • Skill increase: list eligible skills
  • Class feat: present 3–5 options from build file (see KM_Builds.md → sub-file), mark ★ pick
  • General/skill feat: at even levels
  • Ancestry feat: at 1, 5, 9, 13, 17
  • Spell slot increases: if caster, new slots per class table
```

**MANUAL mode** (player-initiated; switched with `/mode manual`):

When the XP threshold is crossed in MANUAL (or ASK) mode, the DM outputs the deferral prompt — NOT the full menu immediately:

```
[LEVEL UP — reached Level X!]
  XP : [current] / [next threshold]  (carry: [remainder])
  HP : +[X] (pending — applied when you confirm)

Level now or save it for later?
  1. Level now — show me the full menu
  2. Later — I'll type .level when I'm ready
```

If player picks **1**: fire the full menu in the next response (all choice points, `[AUTO would pick: …]` annotations on every item).
If player picks **2**: set `level_up_available: true` and continue the scene. Fire the full menu when player types `.level`.

**⛔ .fail 29 fires when:** threshold crossed and DM outputs nothing — no notification, no deferral prompt, just continues narrating. Offering the deferral prompt is correct behavior, not a violation.

Display ALL available options. For every choice point, also surface an inline
`[AUTO would pick: X — reason]` annotation so the player has a default to compare
against or accept. Player may take the auto pick, pick anything else, or ask
for more info. Format:
```
CLASS FEAT (Level 4) — choose one:
  [1] Attack of Opportunity        — Reaction, strike a foe that triggers
  [2] Reactive Shield              — Raise shield as reaction on hit
  [3] Sudden Charge                — Stride + Strike in 1 action  [AUTO ★]
  [4] Double Slice                 — Two Strikes in 1 action
  [AUTO would pick: 3 Sudden Charge — matches Dual Slice Fighter build's mobility priority]
  Type a number, or ASK for more detail on any option.
```
Same `[AUTO would pick: …]` annotation format applies to ability boosts,
skill increases, ancestry feats, and spell prep. Never withhold auto's choice
in MANUAL — the point of the mode is to see every option **and** know which
one auto would take.

**Step 3 — Confirm with player before continuing scene. (ASK/MANUAL only — skip in AUTO.)**

**⛔ The level-up menu fires in the SAME response as the XP-threshold crossing.**
Do not announce *"level-up available"* in one response and then continue the
scene without the menu, intending to fire it later. The menu MUST be in the
same response as the threshold cross. Splitting them = `.fail 29`.

If the player wants to defer the level-up choice, they will say so in their
next input. The DM's job is to present the choices the moment the threshold
is crossed, not to wait for the player to request them.

**Step 4 — Fire ALL companion level-ups simultaneously (see below).**

> **Violation:** `.fail 29` if companions are not leveled in the same response as the player.

---

## 🤖 COMPANION LEVEL-UP PROCEDURE

**Rule:** ALL companions level up simultaneously with the player. No exceptions. See KM_DMRules.md § COMPANION LEVEL-UP.

**Leveling mode source:** Read `game_options.companion_leveling_mode` (NOT `player.leveling_mode`). Default = AUTO. Player and companions ALWAYS use independent fields — applying the player's mode to companions = `.fail 6` (rule applied incorrectly).

**Leveling modes:**
- **AUTO** (default): DM applies choices from build maps silently, announces inline
- **ASK**: DM presents choices to player for each companion
- **MANUAL**: Player makes all choices — same as ASK but player-initiated

**Required output format:**
```
[LEVEL UP — Amiri → Level X]
  HP: +[X] → [total]
  New feature: [auto feature if any]
  Feat: [feat name from build map]
[LEVEL UP — Linzi → Level X]
  HP: +[X] → [total]
  ...
[All active companions listed]
```

---

## 🔗 COMPANION LEVELING FILE ROUTER

| Companions | Source File | Notes |
|------------|-----------|-------|
| 1–12 (CRPG roster) | KM_Companions_Behaviors.md | Scaled stat blocks at key levels |
| 1–12 auto-level rules | KM_DMRules.md | Generic class auto-level procedure |
| 1–12 build file lookup | KM_Companions_Behaviors.md | Maps each companion to KM_Builds.md |
| 13–25 (Wrath companions) | KM_Companions_Behaviors.md (stubs) | Use generic class auto-level from KM_DMRules.md |
| 26–30 (extended) | KM_Companions_Behaviors.md | Build file lookup → KM_Builds.md |
| 31–54 (iconics) | KM_Companions_Behaviors.md | Full L1–20 leveling maps |
| 55–73 (new iconics) | KM_Companions_Behaviors.md (stubs) | Use generic class auto-level from KM_DMRules.md |

---

## 📋 GENERIC CLASS AUTO-LEVEL (for companions without full maps)

When a companion has no full leveling map, apply these defaults at each level:

1. **HP:** Class base HP + Con modifier
2. **Proficiency increases:** Per class table (martial = expert at 5, master at 13; caster = expert at 7, master at 15)
3. **Ability boosts (5/10/15/20):** Primary stat → secondary stat → CON → tertiary stat
4. **Class feat:** Highest-rated feat for the companion's role from the class feat list
5. **Skill increase:** Class's signature skill → Perception → secondary skill
6. **Spell slots (casters):** Per class table, prepare highest-level options available

> **Ability boost priority by archetype:**
> - Martial melee: STR → CON → DEX → WIS
> - Martial ranged: DEX → STR → CON → WIS
> - Full caster (divine/occult): WIS or CHA → CON → DEX → INT
> - Full caster (arcane/primal): INT or WIS → CON → DEX → CHA
> - Skill monkey: DEX → INT → WIS → CHA

---

*KM_BuildGuide.md — Kingmaker PF2e Text Adventure | Level-Up Procedures v1.0*


---

<!-- merged from KM_BuildGuide.md (v93.21 file consolidation) -->

# KINGMAKER — GENERAL FEATS L1 CATALOG (PF2e Remaster)
## KM_BuildGuide.md | Used whenever a general feat slot must be filled

> **⛔ DM: When ANY source grants the player "a general feat of your choice
> you qualify for" (Versatile Human, Skilled Heritage's general-feat option,
> Ancestral Paragon, Natural Ambition's general option, Canny Acumen retake,
> level-up general slots at L3/7/11/15/19), you MUST:**
>
> 1. Read this file
> 2. Filter the catalog by the player's current stats / proficiencies / feats
> 3. Output a numbered list of feats the player qualifies for, with each
>    feat's effect summarized in one line
> 4. Mark feats with `(prereq met: X)` or strike non-qualifying ones
> 5. Include `[N] CUSTOM` as the final option for any general feat (including
>    skill feats) not on this short-list
>
> Never just say "name any general feat you qualify for" without showing the
> filtered list first. That prompt = `.fail 22` (skill check / choice offered
> without the player having visible options).

---

## CORE GENERAL FEATS (no skill training required)

| # | Feat | Prereq | Effect |
|---|------|--------|--------|
| 1 | Adopted Ancestry | None | Pick one ancestry; you can take its ancestry feats. Useful for thematic multi-ancestry party builds. |
| 2 | Armor Proficiency | None | Gain trained in next armor tier (light → medium → heavy). MUST be class with martial chassis to be worth it; full casters skip. |
| 3 | Breath Control | None | +1 status to saves vs inhaled, hold breath 25× longer. Niche but free. |
| 4 | Canny Acumen | None | Become expert in one of: Fortitude / Reflex / Will / Perception. Bumps to master at L17. **Always strong** — pick your weakest save. |
| 5 | Diehard | None | Die at dying 5 instead of dying 4. One extra round of life at 0 HP. **Mandatory for melee tanks.** |
| 6 | Fast Recovery | CON 14 | Recover 2× HP from rest, +2 vs ongoing disease/poison. Great for high-CON frontliners. |
| 7 | Feather Step | DEX 14 | Step into difficult terrain. **Mandatory for any DEX class** that fights in dungeons. |
| 8 | Fleet | None | Speed +5 ft permanently. Stacks with everything. **Always strong.** |
| 9 | Incredible Initiative | None | +2 circumstance bonus to initiative rolls. **Top-tier** — going first wins fights. |
| 10 | Ride | None | Mount obeys 1-action commands instead of 2-action. Required for cavalier-style builds. |
| 11 | Shield Block | None | Gain the Shield Block reaction. **Mandatory for any character carrying a shield** (most classes don't get it free until L1 if at all — Fighter/Champion already have it). |
| 12 | Toughness | None | +HP equal to your level, recovery DC −3. **Top-tier durability** — picks every level it stays valid. |
| 13 | Untrained Improvisation | None | +Level/2 to untrained skill checks. Useful for INT-low characters who want to attempt anything. |
| 14 | Weapon Proficiency | None | Gain trained in simple OR martial weapon group. Casters who want a real weapon. |

---

## ADVANCED GENERAL FEATS (require prior feat or proficiency)

| # | Feat | Prereq | Effect |
|---|------|--------|--------|
| 15 | Ancestral Paragon | Lvl 3, ≥1 ancestry feat | Gain another 1st-level ancestry feat. Good if you missed a key ancestry feat at L1/5/9. |
| 16 | Expeditious Search | Master Perception | Search at 2× / 4× speed. L7+ pick. |
| 17 | Incredible Investiture | Lvl 11, CHA 16 | Wear/benefit from 12 invested items instead of 10. Magic-item builds only. |

---

## SKILL FEATS (also count as general feats — show only if matching skill is trained)

Show these ONLY if the player is trained (or higher) in the listed skill.
This list is partial — for any skill feat not below, accept via `[N] CUSTOM`
and verify the prerequisite from the PF2e Remaster skill-feat list.

| # | Feat | Skill Prereq | Effect |
|---|------|--------------|--------|
| S1 | Assurance | Trained in any skill | Take 10 + proficiency on that skill instead of rolling. **Top-tier** — picks the skill at character creation, scales for life. |
| S2 | Cat Fall | Trained Acrobatics | Treat falls as 10/25/50 ft shorter (trained/expert/master). |
| S3 | Quick Jump | Trained Athletics | High Jump / Long Jump as 1 action instead of 2. |
| S4 | Battle Medicine | Trained Medicine | Treat Wounds as 1 action in combat, once per target per day. **Top-tier party-utility.** |
| S5 | Pickpocket | Trained Thievery | Steal from creatures actively watching, no penalty. |
| S6 | Group Coercion | Trained Intimidation | Demoralize multiple targets at once. Scales by proficiency. |
| S7 | Hobnobber | Trained Diplomacy | Gather Information at 2× speed; on success can never crit-fail. |
| S8 | Recognize Spell | Trained in any of Arcana/Nature/Occultism/Religion | ID a spell as it's cast (reaction). Mandatory anti-caster pick. |
| S9 | Trick Magic Item | Trained in any spell tradition skill | Activate a magic item not on your spell list. |
| S10 | Terrain Expertise | Trained Survival | +1 circumstance to Survival in chosen terrain. |

---

## ⛔ DM PROMPT FORMAT

When granting a general feat slot, output VERBATIM:

```
════════════════════════════════════════════════════════════
GENERAL FEAT — [Source: Versatile Human / Natural Ambition / Lvl 3 slot]

You qualify for the following (filtered by your stats: STR [X] DEX [X]
CON [X] INT [X] WIS [X] CHA [X], trained in [skill list]):

Top-tier picks for [your build type — caster / melee / hybrid]:
  [1] [Feat] — [one-line effect]
  [2] [Feat] — [one-line effect]
  [3] [Feat] — [one-line effect]

Other valid options:
  [4] [Feat] — [one-line effect]
  [5] [Feat] — [one-line effect]
  ...

  [N] CUSTOM — name any other general feat (including skill feats not
              listed). DM will verify prerequisite.

Type a number or feat name.
════════════════════════════════════════════════════════════
```

Filter rules:
- DEX < 14 → omit Feather Step
- CON < 14 → omit Fast Recovery
- Already heavy-armor proficient → omit Armor Proficiency
- Already has Shield Block class feature → omit Shield Block
- Skill feats: include only those matching player's trained skills
- Highlight 2–3 "top-tier picks" relevant to the build (e.g. caster builds:
  Canny Acumen, Toughness, Recognize Spell; melee tanks: Diehard, Toughness,
  Shield Block; DEX skirmishers: Feather Step, Fleet, Incredible Initiative)

---

*KM_BuildGuide.md — Kingmaker PF2e | General Feat Catalog v1.0*


---

<!-- merged from KM_BuildGuide.md (v93.21 file consolidation) -->

# KINGMAKER — BUILD AUDIT: BARBARIAN
## KM_BuildGuide.md | Source files: KM_Builds_Barb_Bard.md (1–6), KM_Builds_Barb_Bard.md (7–10)
## Audit date: 2026-05-14 | Canon reference: PF2e Remaster Player Core / Player Core 2

> **Method:** Each build is audited at L1 (statblock math, feat-slot accounting) and across the L1–20 leveling map (feat-level legality, feat-name fabrication, class-feature placement). Deltas shown only — values not listed = correct or unverified.
>
> **PF2e Remaster Barbarian L1 proficiencies (canon reference):**
> Perception: Expert | Fort: Expert | Ref: Trained | Will: Trained | Class DC: Trained
> *(Note: some Player Core 2 sources boost Will to Expert at L1 — entries flagged with [†].)*
>
> **PF2e save formula:** `L + prof_bonus + ability_mod` where Trained = +2, Expert = +4, Master = +6, Legendary = +8.
> **PF2e Init = Perception** in standard play.
>
> **Barbarian class progression milestones (Remaster):**
> L3 Furious Footfalls (+5 Speed) | L5 Brutal Critical | L7 Juggernaut (Expert Fort, success→crit) + Weapon Spec
> L9 Lightning Reflexes (Expert Ref) | L11 Mighty Rage | L13 Greater Juggernaut (Master Fort)
> L15 Indomitable Will (Master Will) + Greater Weapon Spec | L17 Quick Rage | L19 Devastating Strike

---

## SYSTEMIC PATTERNS (apply to all 10 builds)

1. **Saves and Perception are L-short.** Files compute as `prof + mod` without adding character level. At L1 every Expert save/perception reads 1 lower than canon; every Trained reads correctly only by coincidence (some are also short).
2. **Init mis-stated.** Files use a DEX-like number; canon is Init = Perception bonus.
3. **Background skill feat omitted or wrong.** Warrior bg canonically grants Intimidating Glare; multiple builds list Powerful Leap as bg feat (not what Warrior grants).
4. **L1 standard class feat slot empty.** When Natural Ambition is taken, Sudden Charge (or equivalent) is labeled as the Natural Ambition grant — but the standard L1 class feat slot is left unfilled in the leveling map.
5. **Juggernaut placed at L3 (illegal).** Canon: L7. Affects all 10 builds.
6. **Master Fort at L9 (illegal).** Canon: Greater Juggernaut at L13.
7. **Greater Weapon Specialization at L10 (illegal).** Canon: L15.
8. **Indomitable Will at L15** — placement OK (canon L15) but it's a class feature, not a [PICK] feat — should not consume the class-feat slot.
9. **"Brutal Rage" at L5** — canonical name is **Brutal Critical** (extra die on crit). "Brutal Rage" is not a published class feature name.
10. **"Rage of Ruin" at L20** — not a canonical PF2e feat. Suspected fabrication or homebrew rename.

---

## BUILD 1 — TACTICAL REACH KING *(Human Versatile / Giant Instinct / Warrior)* ✅ LIVE
**File:** KM_Builds_Barb_Bard.md:31-104
**Status:** PASS — all audit findings resolved. Canon-compliant against PF2e Remaster (Player Core / Player Core 2).
**Last verified:** 2026-05-17

### Resolution summary
v93.12 mass sweep (2026-05-15) fixed: HP 24→23, Brutal Critical naming, Juggernaut placement L3→L7, Greater Juggernaut L9→L13, Greater Weapon Spec L10→L15, Gigantic Stature L13→L14, background skill feat to Intimidating Glare, removed Reactive Strike fabricated path, removed Rage of Ruin fabrication, removed Titan Mauler/Devastator/Improved Knockdown placement errors.

v93.13 targeted edits (2026-05-17) fixed:
| Issue | Resolution |
|-------|-----------|
| AC 13 (Unarmored) contradicted Full Plate L1 premise | → AC 19 (10 + 6 Full Plate + 3 Trained Heavy, DEX cap 0) |
| Intimidation +1 (labelled Trained, used Untrained math) | → +3 (Trained + CHA 0 + L1) |
| Warfare Lore +1 (same bug) | → +3 (Trained + INT 0 + L1) |
| L3 Furious Footfalls note had outdated "light/no armor" conditional | → "flat +5 status to Speed, unconditional; +10 while raging" |
| L12 Combat Grab (Fighter-only class feat placed in skill slot) | → Battle Medicine (legal skill feat, fits Medicine +5 third-action pattern) |
| L19 "Armor of Will" (Champion-only feature) | Deleted; L19 is Devastating Strike only |
| L20 "Apex Predator" (fabricated name) | Deleted; L20 is Ability Boost ×4 + Rampage |

### Legality verified
- L1 statline: HP 23, AC 19, Init +7, Perception +7, Fort +8, Ref +3, Will +7, all skill bonuses match prof + ability + L1
- L1 feat slots: Heritage general feat (Armor Prof Heavy — legal because Barb starts Trained Medium), Ancestry (Natural Ambition → bonus class feat Sudden Charge), Class (Raging Intimidation), Skill (Intimidating Glare via Warrior bg)
- L1-20 leveling map: every class feature at canon level, every class feat legal at its slot, every skill feat legal, Sentinel archetype chain (L2 Ded → L7 Expert Heavy → L15 Master Heavy) intact
- L18 Unstoppable Juggernaut confirmed canon (Barb L18 class feat — resistance + Con mod + 1 HP stay-alive reaction)

### Live status
This is the live build for the current playthrough character (eRmaC, per save state). Active in `KM_Builds_Barb_Bard.md`. Available on `KM_BuildGuide.md` Barbarian menu as option [1]. Ready for play.

---

## BUILD 2 — FURY FLURRY *(Human Natural Ambition / Fury Instinct / Warrior)*
**File:** KM_Builds_Barb_Bard.md:108-167

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 24 | 23 | **+1** unexplained |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** (Trained: 1+2+2 = +5) |
| Will | +5 | +5 (Trained) / +7 (Expert) | ✓ or **−2** |
| Perception | +4 | +7 | **−3** |
| Init | +2 | +7 | **−5** |
| Athletics | +6 | +7 | **−1** |
| Acrobatics +4 | — | +5 | **−1** |

### L1 feat-slot issues
- **Double Slice picked as L1 Natural Ambition class feat — ILLEGAL.** Double Slice is a L1 **Fighter** class feat. Natural Ambition grants a 1st-level **class feat from your own class**. Barbarians do not have Double Slice in their feat list. **Critical fabrication.**
- Background skill feat: Warrior → Intimidating Glare. Not listed; only "Double Slice" appears at L1.
- L1 standard class feat slot: empty (same pattern).

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal at L3.** |
| 3 | Raging Athlete | L7 class feat. **Illegal at L3.** |
| 4 | Two-Weapon Flurry | **Fighter** L8 feat. Barbarian cannot pick directly. Needs Fighter Dedication chain. **Illegal/fabricated.** |
| 5 | Brutal Rage | Likely Brutal Critical rename. |
| 5 | Power Attack | L1 class feat — legal at L5 but wasted slot. |
| 6 | Improved Knockdown | L8 class feat. **Illegal at L6.** |
| 7 | Knockback Strike | Not canonical PF2e Barbarian feat. **Suspected fabrication.** |
| 8 | Brutal Bully | L6 class feat. Legal at L8 ✓ |
| 9 | Devastator | See Build 1 — likely fabrication. |
| 9 | Master Fort | Should be L13 (Greater Juggernaut). |
| 10 | Greater Weapon Specialization | L15. **Illegal at L10.** |
| 13 | Furious Sprint | L8 class feat. Legal at L13 ✓ |

**Count:** 7 stat deltas, 3 L1 feat issues (1 critical fabrication), 8 leveling issues.

---

## BUILD 3 — ANIMAL INSTINCT MUTAGEN *(Orc Hold-Scarred / Animal Instinct / Herbalist)*
**File:** KM_Builds_Barb_Bard.md:171-230

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 28 | 28 | ✓ (10 Orc + 12 Barb + 4 CON = 26; **off by +2** unless Diehard/Hold-Scarred adds — Hold-Scarred Heritage doesn't add HP at L1, just Diehard. **Δ +2 unexplained**) |
| Fort | +8 | +9 | **−1** (1 + 4 + 4 = 9) |
| Ref | +7 | +6 | **+1** (Trained: 1+2+3 = +6) |
| Will | +5 | +5 (T) / +7 (E) | ✓ or **−2** |
| Perception | +4 | +7 | **−3** |
| Init | +3 | +7 | **−4** |
| Athletics | +6 | +7 | **−1** |
| Crafting +4, Survival +3, Nature +3 | — | +5/+4/+4 | **−1 each** |

### L1 feat-slot issues
- **"Hold-Scarred + Animal Skin"** at L1 — Hold-Scarred is a **heritage**, not a feat slot. Animal Skin is the L1 class feat. The pairing in "Key Feats: L1 Hold-Scarred + Animal Skin" is mislabeled but mechanically OK: heritage + L1 class feat.
- However the leveling map L1 PICK column lists "Hold-Scarred + Animal Skin" — Hold-Scarred is heritage, not a [PICK]. Confused slot labeling.
- L1 ancestry feat: not listed. Orc gets an L1 ancestry feat — missing from the build.
- Herbalist bg skill feat: should grant Natural Medicine. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Raging Athlete | L7. **Illegal at L3.** |
| 4 | Predator's Pounce | L8 class feat. **Illegal at L4.** |
| 5 | Greater Animalistic Attacks | **Not canonical.** Animal Instinct upgrades happen via auto-scale (Specialization Ability at L7). Suspected fabrication. |
| 7 | Vicious Evisceration | L8 class feat. Legal at L7? Edition-check. |
| 9 | Devastator | Fabrication (see Build 1). |
| 10 | Greater Weapon Spec | L15. **Illegal at L10.** |
| 11 | Apex Predator | Not canonical PF2e feat. **Suspected fabrication.** |
| 13 | Furious Sprint | L8 class feat. Legal at L13 ✓ |

**Count:** 7 stat deltas, 3 L1 feat issues, 7 leveling issues (2 suspected fabrications).

---

## BUILD 4 — SPIRIT INSTINCT FORCE DAMAGE *(Human Natural Ambition / Spirit Instinct / Acolyte)*
**File:** KM_Builds_Barb_Bard.md:234-293

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 24 | 23 | **+1** unexplained |
| Fort | +7 | +8 | **−1** |
| Ref | +5 | +4 | **+1** (1+2+1 = 4) |
| Will | +6 | +6 (T) / +8 (E if Remaster) | ✓ or **−2** |
| Perception | +5 | +7 | **−2** |
| Init | +1 | +7 | **−6** |
| Skills | various −1 each | | |

### L1 feat-slot issues
- **"Spirit's Wrath" at L1** — canonical name is **Spirit Rage** (Spirit Instinct's base feature) or **Furious Howl/Howl of Heavens**. "Spirit's Wrath" is not a PF2e feat. **Suspected fabrication.**
- Acolyte bg skill feat: canon = Student of the Canon. Not listed.
- L1 standard class feat slot empty.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Swipe | L4 Barbarian feat. **Illegal at L3.** |
| 4 | Spirit's Vengeance | Not canonical. **Suspected fabrication.** |
| 5 | Basic Oracle Spells | Archetype feat from Oracle Dedication. Legal at L5 if Oracle Ded taken L2 ✓ |
| 6 | Improved Spirit's Vengeance | Built on a fabricated base — fabrication. |
| 11 | Spirit Incarnation | Not canonical. **Suspected fabrication.** |
| Others | Same pattern as builds 1-3 (Juggernaut, Master Fort, GWS placements) | |

**Count:** 6 stat deltas, 2 L1 issues (1 fabrication), 6 leveling issues (3 fabrications).

---

## BUILD 5 — DRAGON INSTINCT ELEMENTAL BLASTER *(Half-Orc Orc Ferocity / Dragon Instinct / Hunter)*
**File:** KM_Builds_Barb_Bard.md:297-356

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 26 | 25 | **+1** (10 Half-Orc + 12 + 3 = 25) |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +5 | +5/+7 | ✓ or **−2** |
| Perception | +4 | +7 | **−3** |
| Init | +2 | +7 | **−5** |
| Skills | −1 each | | |

### L1 feat-slot issues
- **Dragon Roar at L1** — canonical name is **Intimidating Strike** or **Demoralize** + Dragon Instinct flavor. "Dragon Roar" might refer to the **Dragon Instinct anathema/feature**. Not a feat per se. Suspected misclassification.
- Hunter bg skill feat: canon = Survey Wildlife. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Swipe | L4 feat. **Illegal at L3.** |
| 4 | Draconic Arrogance | Not canonical PF2e feat (sounds like APG/Legacy). **Verify.** |
| 6 | Basic Bloodline Spell "Fireball equiv" | Generic — depends on Sorcerer Ded prereqs. Fireball is a 3rd-rank spell; "Basic Bloodline Spell" archetype feat grants 1st-rank bloodline spells only. **Wrong rank claim.** |
| 8 | Improved Dragon Breath | Not canonical Barbarian feat. **Suspected fabrication.** |
| 11 | Dragon Transformation | Sorcerer Draconic Bloodline focus spell at L18 (Form of the Dragon analog). As Barb-archetype access requires very high archetype investment. **Illegal at L11.** |
| Others | Standard Juggernaut/MasterFort/GWS errors | |

**Count:** 6 stat deltas, 2 L1 issues, 6 leveling issues (3 fabrications/wrong).

---

## BUILD 6 — SUPERSTITION ANTI-MAGIC *(Dwarf Stonegate / Superstition Instinct / Warrior)*
**File:** KM_Builds_Barb_Bard.md:360-419

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 26 | 26 | ✓ (10 Dwarf + 12 + 4 = 26) |
| Fort | +8 | +9 | **−1** |
| Ref | +5 | +4 | **+1** |
| Will | +6 | +6/+8 | ✓ or **−2** |
| Perception | +5 | +7 | **−2** |
| Init | +1 | +7 | **−6** |
| Athletics | +8 | +7 | **+1** (1+2+4 = +7) |

### L1 feat-slot issues
- **"Stone Walk" at L1** — Dwarf has **Stonemason's Eye**, **Stonegate** Heritage gives sense, but "Stone Walk" as ancestry feat name is non-canonical. Likely refers to **Stonewalker** L1 ancestry feat. Name mismatch.
- "Superstition Instinct" as L1 [PICK] feat — Superstition Instinct is the chosen Instinct (class feature), not a feat. **Slot mislabel.**
- Warrior bg skill feat (Intimidating Glare): not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 4 | Warded Mind | L12 class feat. **Illegal at L4.** Major error — this is sold as the "L4 identity feature" in build summary. |
| 5 | Terrifying Howl | L8 class feat. **Illegal at L5.** |
| 6 | Spell Sunder | Not a canonical PF2e Barbarian feat. Closest is **Sunder Spell** (Cleric) or **Counter Magic**. **Suspected fabrication.** |
| 11 | "Spell Sunder: Greater" | Built on fabricated base. |
| Others | Standard Juggernaut/MasterFort/GWS errors | |

**Count:** 6 stat deltas, 3 L1 issues, 5 leveling issues (2 fabrications, 1 major level mismatch).

---

## BUILD 7 — TITAN MAULER *(Human Versatile / Giant Instinct / Warrior)*
**File:** KM_Builds_Barb_Bard.md:19-78

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 22 | 22 | ✓ (8 Human + 12 + 2 = 22) |
| Fort | +6 | +7 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +4 | +4/+6 | ✓ or **−2** |
| Perception | +3 | +5 | **−2** |
| Init | +2 | +5 | **−3** |
| Athletics | +6 | +7 | **−1** |

### L1 feat-slot issues
- **"Large Bastard Sword (2d12+4)" at L1** — Bastard Sword 1d8, Large weapon increases damage die size to 1d10 (one step up). **2d12 claim wrong.** Giant Instinct allows Large weapons but die scaling is +1 step, not double dice.
- "Raging Intimidation (free Demoralize on every hit while raging)" L1 — **Free Demoralize on every hit is NOT the canonical effect.** Raging Intimidation (L1 Barbarian feat) lets you Demoralize without spending action AND lets you use Intimidating Glare/Scare to Death while raging. It does NOT give free Demoralize on hit. **Mechanic fabricated.**
- Versatile Human "free general feat at L1" used for Raging Intimidation — Raging Intimidation is a CLASS feat, not a general feat. Versatile Human gives a general feat slot. **Slot type mismatch.** Would need to be the standard L1 class feat slot.
- Warrior bg skill feat (Intimidating Glare): listed at L2 as a [PICK]. But Intimidating Glare should be granted **automatically by Warrior background** at L1, not picked at L2.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 2 | Intimidating Glare | Should be auto-granted by Warrior bg at L1 (free) — not a L2 pick. |
| 3 | Juggernaut | L7. **Illegal.** |
| 3 | Swipe | L4. **Illegal at L3.** |
| 5 | Terrifying Howl | L8. **Illegal at L5.** |
| 6 | Giant's Stature | L6 ✓ — first correct placement |
| 8 | Come and Get Me | L12 class feat. **Illegal at L8.** |
| 11 | Collateral Thrash | L10 ✓ (legal at L11) |
| 12 | Predator's Pounce | L8 ✓ (legal at L12) but wasted slot |
| 16 | Scare to Death | L7 skill feat (Master Intimidation prereq, available ~L7). Skill feat slot consumed. Class feat slot at L16 = wasted? |
| Others | Standard errors | |

**Count:** 7 stat deltas, 4 L1 issues (1 mechanic fabrication, 1 weapon-math error), 7 leveling issues.

---

## BUILD 8 — ELEMENTAL RAGE *(Half-Orc Orc Ferocity / Fury Instinct / Farmhand)*
**File:** KM_Builds_Barb_Bard.md:82-141

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 26 | 25 | **+1** |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +5 | +5/+7 | ✓ or **−2** |
| Perception | +4 | +6 | **−2** |
| Init | +2 | +6 | **−4** |

### L1 feat-slot issues
- "Orc Ferocity" labeled as L1 [PICK] — Orc Ferocity is a **Half-Orc ancestry feat (L1)** ✓ but slot label conflates ancestry feat with class feat in some entries.
- "Raging Intimidation" — mechanic fabrication carried over from Build 7 if used in same flavor.
- Farmhand bg skill feat: canon = Assurance (skill of choice) or Survey Wildlife. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 2 | Kineticist Dedication (elemental blast) | **Kineticist Dedication has Kineticist-specific prereqs (an element + impulse junction). Available L2 if rules support multiclass. Verify Player Core 2 compatibility.** |
| 3 | Juggernaut + Swipe | Both illegal placements. |
| 4 | Basic Kinesis | Archetype feat L4 (Basic Kineticist), legal ✓ |
| 6 | Elemental Blast upgrade (2d6) | Damage die progression for Kineticist scales with class level. Multiclass archetype Kineticist scales slower. **Verify die size.** |
| Others | Standard errors | |

**Count:** 6 stat deltas, 1-2 L1 issues, 5 leveling issues + archetype-scaling verify.

---

## BUILD 9 — RAGING FLURRY STRIKES *(Human Natural Ambition / Fury Instinct / Street Urchin)*
**File:** KM_Builds_Barb_Bard.md:145-204

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 24 | 23 | **+1** |
| Fort | +7 | +8 | **−1** |
| Ref | +6 | +5 | **+1** |
| Will | +6 | +5/+7 | ✓ |
| Perception | +5 | +7 | **−2** |
| Init | +2 | +7 | **−5** |

### L1 feat-slot issues
- "Toughness" at L1 via Natural Ambition — Natural Ambition grants a **class feat**, not a general feat. Toughness is a **general feat**. **Slot type mismatch — illegal.**
- Street Urchin bg skill feat: canon = Pickpocket. Not listed.
- L1 standard class feat slot: empty.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 2 | Monk Dedication (Flurry of Blows, Powerful Fist 1d6) | Monk Dedication archetype feat ✓ L2. **Flurry of Blows is a Monk class feature, NOT granted by Monk Dedication.** Monk Dedication gives Trained in martial weapons + 8 HP + access to Monk archetype feats. Flurry of Blows specifically requires Basic Monk Spellcasting OR the **Monastic Weaponry** chain. **"Flurry of Blows from Monk Ded L2" is fabricated mechanic.** |
| 4 | Basic Unarmed Strike "Monk agile chain upgrades" | Not a canonical archetype feat name. Closest: Basic Kata. **Suspected fabrication.** |
| 6 | Savage Critical | Not canonical PF2e Barbarian feat. **Suspected fabrication.** |
| 3,9,10,15 | Standard errors | |

**Count:** 6 stat deltas, 2 L1 issues (1 illegal slot), 5 leveling issues (2 mechanism fabrications).

---

## BUILD 10 — PURE RAGE SUPPORT *(Human Natural Ambition / Fury Instinct / Street Performer)*
**File:** KM_Builds_Barb_Bard.md:208-267

### L1 statblock deltas
| Stat | File | Canon | Δ |
|---|---|---|---|
| HP | 22 | 22 | ✓ |
| AC | 17 | 18 | **−1** (Hide armor at L1 Trained: 10+2+1+2+3 = 18; file 17 is short) |
| Fort | +6 | +7 | **−1** |
| Ref | +5 | +4 | **+1** |
| Will | +5 | +4/+6 | varies |
| Perception | +4 | +5 | **−1** |
| Init | +1 | +5 | **−4** |
| Performance +5 | — | +6 | **−1** (1+2+3 CHA = +6) |

### L1 feat-slot issues
- "Raging Intimidation" — mechanic fabrication if represented as free-Demoralize-on-hit (see Build 7).
- Street Performer bg skill feat: canon = Fascinating Performance. Not listed.

### Leveling map illegalities
| Lvl | File entry | Issue |
|---|---|---|
| 3 | Juggernaut + Swipe | Both illegal at L3. |
| 5 | Terrifying Howl | L8. **Illegal at L5.** |
| 8 | Come and Get Me | L12. **Illegal at L8.** |
| 12 | Dragon Transformation | Sorcerer focus spell. Not legally accessible to this build (no Sorcerer Ded). **Illegal.** |
| Others | Standard errors | |

**Count:** 7 stat deltas, 1 L1 issue, 6 leveling issues.

---

## CONSOLIDATED FINDINGS

| Build | Stat deltas | L1 issues | Leveling issues | Critical fabrications |
|---|---|---|---|---|
| 1 Tactical Reach King | 6 | 3 | 10 | Titan Mauler-as-feat, Devastator, Rage of Ruin, Reactive Strike path |
| 2 Fury Flurry | 7 | 3 | 8 | **Double Slice illegal for Barb**, Knockback Strike, Devastator |
| 3 Animal Mutagen | 7 | 3 | 7 | Greater Animalistic Attacks, Apex Predator, Devastator |
| 4 Spirit Force | 6 | 2 | 6 | Spirit's Wrath, Spirit's Vengeance, Spirit Incarnation |
| 5 Dragon Blaster | 6 | 2 | 6 | Improved Dragon Breath, Dragon Transformation @ L11, Draconic Arrogance |
| 6 Superstition | 6 | 3 | 5 | Spell Sunder, Warded Mind @ L4 (huge error) |
| 7 Titan Mauler | 7 | 4 | 7 | **Raging Intimidation mechanic fabricated**, 2d12 weapon math |
| 8 Elemental Rage | 6 | 2 | 5 | Kineticist scaling verify |
| 9 Raging Flurry | 6 | 2 | 5 | **Flurry-from-Monk-Ded fabricated**, Savage Critical |
| 10 Pure Rage Support | 7 | 1 | 6 | Dragon Transformation @ L12 illegal |

**Totals across 10 Barbarian builds:**
- 64 L1 statblock math deltas
- 25 L1 feat-slot issues
- 65 L1-20 leveling-map errors
- ~25 distinct fabricated feat names or fabricated mechanics

**Top systemic fixes (one edit pattern, applies to all 10 builds):**
1. Add `L + ` to every save/perception/skill bonus calculation
2. Set `Init = Perception` (or note "see Perception")
3. Move **Juggernaut** from L3 → L7 (auto class feature)
4. Move **Master Fort** from L9 → L13 (Greater Juggernaut)
5. Move **Greater Weapon Specialization** from L10 → L15
6. Rename **Brutal Rage** → **Brutal Critical**
7. Replace or remove **Rage of Ruin** (L20) with a canonical capstone
8. Add **Lightning Reflexes** L9, **Mighty Rage** L11, **Quick Rage** L17, **Devastating Strike** L19 as auto class features
9. Auto-grant **background skill feat** at L1 per background canon (Intimidating Glare for Warrior, etc.) instead of consuming the L1 [PICK]
10. Document each Instinct's L1 anathema/special feature so it's not confused with a feat

---

*KM_BuildGuide.md — Audit v1.0 | 2026-05-14*
