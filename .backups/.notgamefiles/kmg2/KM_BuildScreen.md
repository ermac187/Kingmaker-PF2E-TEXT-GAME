# KINGMAKER — BUILD SELECTION SCREEN
## KM_BuildScreen.md | Referenced by: KM.txt, KM_Companions_Builds.md

> **DM:** Mechanical reference. Load KM_CharCreate.md first. This file handles Step 2 builds and Step 2.5 weapons. Do NOT generate builds from memory. Skipped step = `.fail 9`.
>
> **⛔ After player selects a build:** Load `KM_BuildSetup.md` and run all 8 prompts (Ancestry → Heritage → Stat → Weapon → Armor → Deity → Background → Skills) IN ORDER before Step 3 companion selection.

---

## STEP 2 — PICK A CLASS

```
KINGMAKER — CHARACTER SELECT | PF2e Remaster + Battlecry!
══════════════════════════════════════════════════════════
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

Type a number (1–27) or CUSTOM to build from scratch.
══════════════════════════════════════════════════════════
```

---

## STEP 2 — BUILD LISTS

> **DM:** After player picks a class, load `KM_BuildGuide_A.md` (classes 1–13) or `KM_BuildGuide_B.md` (classes 14–27) and display ONLY that class's block. One display, one pick — do NOT load a separate file or ask twice. Proceed directly to KM_BuildSetup.md after pick.

> ⛔ **BUILD LIST SOURCE LOCK — mandatory before displaying any build list.**
> Output this line verbatim BEFORE showing the class build block:
> `BUILD LIST SOURCE: [KM_BuildGuide_A.md or KM_BuildGuide_B.md] | class = [ClassName] | build 1 = [exact Build 1 name from file]`
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
> **Fighter sentinel (class 10):** Build 1 = check KM_BuildGuide_A.md [10] FIGHTER block.
> **All other classes:** Build 1 is authoritative from the guide file — training data is not a substitute.

---

## STEP 2.5 — STARTING WEAPON

> **DM:** After class + build are confirmed, find the class/build in the table below,
> **copy-paste that category's weapon list verbatim from this file**, and wait for the player's pick.
> Do NOT generate weapon lists from memory. Generating from memory = missing entries = `.fail 9`.
> Record as `player.weapon` in save block. This replaces `[primary weapon]` everywhere
> in pre-prologue narration. Ancestry weapon substitution rule (KM_PrePrologue_Builds.md) still applies.

### FIXED BUILDS — display weapon, skip selection:
```
Kineticist (any)  → Elemental Blast (unarmed)
Monk (any)        → Fists / Handwraps (Monastic Archer = Composite Shortbow; Wild Shape = form jaws)
Magus (any)       → set by build stat block (H.md / H2.md)
Gunslinger (any)  → set by KM_PrePrologue_Builds.md build row
Inventor (any)    → set by KM_PrePrologue_Builds.md build row
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
Alchemist 1–3                       → KM_Builds_A.md
Alchemist 4–8                       → KM_Builds_A2.md
Alchemist 9–10                      → KM_Builds_A5.md
Animist 1–5                         → KM_Builds_A4.md
Animist 6–10                        → KM_Builds_A3.md
Barbarian 1–6                       → KM_Builds_B.md
Barbarian 7–10                      → KM_Builds_B2.md
Bard 1–5                            → KM_Builds_B4.md
Bard 6–10                           → KM_Builds_B3.md
Champion 1–6                        → KM_Builds_C.md
Champion 7–10                       → KM_Builds_C2.md
Cleric 1–6                          → KM_Builds_C4.md
Cleric 7–10                         → KM_Builds_C3.md
Commander 1–6                       → KM_Builds_D.md
Commander 7–10                      → KM_Builds_D2.md
Druid 1–6                           → KM_Builds_D4.md
Druid 7–10                          → KM_Builds_D3.md
Exemplar 1–6                        → KM_Builds_E.md
Exemplar 7–10                       → KM_Builds_E3.md
Fighter 1–6                         → KM_Builds_E2.md
Fighter 7–10                        → KM_Builds_E4.md
Guardian 1–6                        → KM_Builds_F.md
Guardian 7–10                       → KM_Builds_F3.md
Gunslinger 1–6                      → KM_Builds_F6.md
Gunslinger 7–10                     → KM_Builds_F4.md
Inventor 1–6                        → KM_Builds_F2.md
Inventor 7–10                       → KM_Builds_F5.md
Investigator 1–6                    → KM_Builds_G.md
Investigator 7–10                   → KM_Builds_G2.md
Kineticist 1–6                      → KM_Builds_G3.md
Kineticist 7–10                     → KM_Builds_G4.md
Magus 1–6                           → KM_Builds_H.md
Magus 7–10                          → KM_Builds_H2.md
Monk 1–6                            → KM_Builds_H3.md
Monk 7–10                           → KM_Builds_H4.md
Oracle 1–6                          → KM_Builds_I.md
Oracle 7–10                         → KM_Builds_I2.md
Psychic 1–6                         → KM_Builds_I4.md
Psychic 7–10                        → KM_Builds_I5.md
Ranger 1–6                          → KM_Builds_I3.md
Ranger 7–10                         → KM_Builds_I6.md
Rogue 1–6                           → KM_Builds_J2.md
Rogue 7–10                          → KM_Builds_J3.md
Sorcerer 1–6                        → KM_Builds_J.md
Sorcerer 7–10                       → KM_Builds_J4.md
Summoner 1–6                        → KM_Builds_K2.md
Summoner 7–10                       → KM_Builds_K3.md
Swashbuckler 1–6                    → KM_Builds_K.md
Swashbuckler 7–10                   → KM_Builds_K4.md
Thaumaturge 1–6                     → KM_Builds_L.md
Thaumaturge 7–10                    → KM_Builds_L3.md
Witch 1–6                           → KM_Builds_L4.md
Witch 7–10                          → KM_Builds_L2.md
Wizard 1–6                          → KM_Builds_M.md
Wizard 7–10                         → KM_Builds_M2.md
```

---

## STEP 3 — AFTER BUILD SELECTED

> **DM:** After class + build confirmed, proceed IN ORDER — **do NOT skip any step:**
>
> 1. Record `player.class` + `player.build` + `player.build_source` + `player.leveling_mode`.
> 2. Ancestry — display `KM_AncestryGuide.md` class block (★/2-5/OK/AVOID + exceptions). Record `player.ancestry`.
> 3. ⛔ **HERITAGE — load BOTH `KM_Heritages.md` (core/uncommon/Goliath) AND `KM_Heritages_B.md` (rare/versatile), find the player's ancestry section, copy-paste the heritage block verbatim. Offer `versatile` as alternate (KM_Heritages_B.md). Record `player.heritage` + `heritage_source` + `heritage_granted_features[]`. Skipped or fabricated = `.fail 9`.**
> 4. ⛔ **BACKGROUND — load `KM_Backgrounds.md`, copy-paste the compact screen exactly, record `player.background`. Skipped = `.fail 9`.**
> 5. Weapon (Step 2.5). Record `player.weapon`.
> 5.5. ⛔ **STAT-WEAPON CHECK** — if weapon is STR-based (pick, warhammer, battleaxe, etc.) but build defaults to DEX-primary, display swap prompt `[1] Keep DEX 18 / STR 16` / `[2] Swap to STR 18 / DEX 14`. Record player's confirmation. Silently using DEX-default stats when a STR weapon was picked = `.fail 9`.
> 6. Armor (Step 2.6). Record `player.armor`.
> 7. Output `.status` panel before any scene content.
> 8. ⛔ **COMPANION SELECTION — load `KM_Companions_Iconics.md`, copy-paste the COMPACT PICK-10 SELECTION SCREEN verbatim. Announcing "proceeding" without showing the list = `.fail 9`.**
>
> **Save block** (all fields REQUIRED; `leveling_mode`: auto|ask|manual; player default = `manual`, companions auto-level via `game_options.companion_leveling_mode`):
> ```json
> "player": { "class": "Fighter", "build": "Dual Slice Fighter",
>   "build_source": "KM_Builds_F.md", "leveling_mode": "manual",
>   "ancestry": "Human", "heritage": "Versatile Human",
>   "heritage_source": "ancestry-specific",
>   "background": "Sword Scion", "weapon": "Pick + Light Pick",
>   "armor": "Dragon Plate" }
> ```
>
> **⛔ DM RULE:** Do not begin Pre-Prologue until class, build, ancestry, **heritage**, background, weapon, armor are all confirmed AND `.status` displayed. Skipped step = `.fail 9`.

---

## COMPANION BUILD ASSIGNMENT

> **DM:** After Pick-10 is complete, open `KM_Companions_Builds.md` and run the
> Build Assignment procedure for each companion. Each companion sees only the build
> list matching their class from this file. The procedure is defined in
> `KM_Companions_Builds.md` — do not improvise it.

---

*KM_BuildScreen.md v6.2 — 270 Builds, 27 Classes | Build lists + advisory merged into KM_BuildGuide_A/B.md*
