# KINGMAKER — COMPANION BEHAVIORS, PART B (DATA TABLES)
## KM_Companions_Behaviors_B.md | Split from KM_Companions_Behaviors.md (v95.9, 2026-05-29)
## Contains: Build Assignment + Combat AI + Full Selection Reference + Leveling Maps + Scaled Stat Blocks
## Pair-load with KM_Companions_Behaviors.md + KM_Companions.md.

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION BUILD ASSIGNMENT
## KM_Companions_Behaviors.md | Referenced by: KM_Companions_Behaviors.md, KM_DMRules.md

> **⛔ NO TRAINING DATA. Preset numbers and names refer ONLY to `KM_BuildGuide.md` (classes 1–13) and `KM_BuildGuide.md` (classes 14–27) — 27 classes × 10 presets each. Using PF2e training knowledge to substitute names or numbers = `.fail 9`.**
>
> **Signature moves / unique powers:** See `KM_Signatures.md` for per-companion canonical signature abilities. Load when the companion is in the active party; surface MOVE in their combat menu.
>
> **DM:** After the player confirms their Pick-10 companion selection, run the Build Assignment procedure below for every companion, in pick order.
>
> **Auto-level rule:** Once a preset is assigned, open the companion's build file (see CLASS REFERENCE below) and use that preset's leveling map for every level-up.
>
> **Override rule:** If the player picks a ⚠️ Avoid preset, show the conflict reason and confirm. Never silently override a companion's core identity.

---

## 📋 BUILD ASSIGNMENT PROCEDURE

```
After Pick-10 is confirmed:

─────────────────────────────────────────────────────────
STEP 0 — BULK OPTION (ask once before any individual prompts):

  ══════════════════════════════════════════════════════
  BUILD ASSIGNMENT
  Assign presets for all Active 5 + chosen companions. Options:
    ALL  — Assign ★ RECOMMENDED preset to every companion at once.
    GO   — Step through companions one at a time.
  ══════════════════════════════════════════════════════

If player types ALL:
  — For each companion, look up their ★ preset in the COMPANION → PRESET
    TABLE below. Every companion in this file has a ★ entry.
  — ⛔ If you cannot find a ★ entry, you did not search thoroughly. Search
    again by companion #. DO NOT default to preset #1 — that's a bug.
  — Skip individual prompts and ⚠️ confirmations.
  — Display the summary table and proceed to Pre-Prologue.

If player types GO:
  — Continue the one-at-a-time loop below.
─────────────────────────────────────────────────────────

For each companion in pick order:
  1. Identify the companion's class (CLASS REFERENCE below).
  2. Load that class's build block from KM_BuildGuide.md (classes 1–13) or KM_BuildGuide.md (classes 14–27).
  3. Look up the companion in the COMPANION → PRESET TABLE below:
     — Mark ★ on the listed preset #
     — Mark ⚠️ on every preset # in the Avoid column
     — Unmarked presets are viable.
  4. Output:

     ══════════════════════════════════════════════════════
     [COMPANION NAME] — [CLASS]
     [10-preset block from KM_BuildGuide_A/B.md with ★/⚠️ markers]

     ★ = Recommended (lore + mechanical fit)
     ⚠️ = Lore conflict (mechanical OK, clashes with identity)
     Type a number (1–10) to assign.
     ══════════════════════════════════════════════════════

  5. If player picks a ⚠️ preset, show reason from the table and ask Y/N.
  6. Record chosen preset name in save block under companions[name].build.
  7. Next companion. Repeat until all assigned.

After all assigned, display summary:
  Companion | Class | Preset # | Preset Name | Lore Fit (★/⚠️/—)
  Then proceed to Pre-Prologue.
```

---

## 🧭 COMPANION → PRESET TABLE

> **DM:** Preset numbers refer to `KM_BuildGuide.md` / `KM_BuildGuide.md` (1–10 per class). `—` in Avoid = no conflict.

### SECTION A — KINGMAKER CRPG (12)

| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| NEW_001 | Hu Tao | Fighter (reach polearm) | (Phase B) | — | Versatile Human / Warrior bg / STR18 DEX14 HP20 AC18 / reach SPEAR, Reactive Strike + Sudden Charge; Pyro flame flavor on the blade |
| NEW_002 | Keqing | Magus (Laughing Shadow; sword + Electro Spellstrike, NOT Ranger) | (Phase B) | — | Versatile Human / Scholar bg / DEX18 INT16 HP18 AC18 / sword + Electro Spellstrike; lightning-step gap-closer (mark-and-arrive) |
| NEW_003 | Leliana | Bard Maestro | (Phase B) | — | Skilled Human / Entertainer bg / CHA18 HP17 AC15 / Lingering Composition (Maestro muse) + Versatile Performance |
| NEW_004 | Yor Forger | Rogue Thief | (Phase B) | — | Gutsy Halfling / Criminal bg / DEX18 HP16 AC18 / Nimble Dodge |
| NEW_005 | Aerith | Cleric Cloistered | (Phase B) | — | Skilled Human / Acolyte bg / WIS18 HP16 AC14 (unarmored) |
| NEW_006 | Bellatrix Lestrange | Witch (patron-bound hexer; hexes + familiar, NOT Psychic) | (Phase B) | — | Versatile Human (aristocrat) / Noble Scion bg / INT18 HP16 AC14 (Seeker) |
| NEW_007 | Revy | Gunslinger (Way of the Pistolero / Fake Out; twin flintlocks, NOT Alchemist) | (Phase B) | — | Versatile Human / Criminal bg / DEX18 CON14 HP18 AC17 / twin Alkenstar flintlocks, dual-wield reload (Seeker) |
| NEW_008 | Satsuki Kiryūin | Commander/Ruthless Warlord (Fighter chassis, katana + living war-garment; NOT Kineticist) | (Phase B) | — | Human / Soldier bg / STR16 CON16 DEX12 HP20+ AC18 heavy armor + katana (Bakuzan); the war-garment is a magic item; 3 signature moves (Seeker = #25) |
| NEW_009 | Velvet Crowe | Thaumaturge (Support; concealed blade + daemon-arm implement, NOT Cleric) | (Phase B) | — | Versatile Human (Toughness) / Soldier bg / CHA16 DEX16 CON14 HP18 AC18 / concealed blade + daemon-arm implement (Exploit Vulnerability vs supernatural; Devour) (Seeker — replaces old build) |
| NEW_010 | Atalanta Alter | Ranger (Hunted Prey/Precision; longbow, NOT Mounted/Investigator) | (Phase B) | — | Skilled Human / Nomad bg / DEX18 WIS14 HP18 AC18 / longbow (Tauropolos); Hunted Prey + Precision Edge (Seeker — replaces old build) |
| 1 | Jubilost | Alchemist | #6 Pure Bomber | — | Quest-locked. Pure bomber identity, no dip |
| 6 | Amiri | Barbarian | #1 Tactical Reach King | #3 #4 | Giant sword IS her identity; reach flavor |
| 10 | Linzi | Bard | #1 Virtuoso Maestro | #3 | ⭐QL recruit at Prologue. Inspire Courage + ranged; too fragile for melee |
| 16 | Tristian | Cleric | #2 Cloistered Heal | #1 #10 | Quest-locked. Gentle healer, avoids weapons |
| 32 | Valerie | Fighter | #4 Shield Bastion Fighter | #8 | IS the shield wall — removing shield removes her |
| 45 | Kalikke/Kanerah | Kineticist | #1 Element Blaster/Tank | #6 | Quest-locked. Dual gate water+fire; not metal |
| 60 | Ekundayo | Ranger | #3 Archer Sniper | — | Quest-locked. Patient hunter; Hunted Shot precision |
| 66 | Nok-Nok | Rogue | #1 Scoundrel + Thaumaturge | #3 | Quest-locked. Trickster goblin; INT 10, not scholarly |
| 84 | Octavia | Wizard | #4 Universalist Utility + Investigator | — | Quest-locked. Self-taught, resourceful, no fixed school |
| 18 | Jaethal | Cleric | #1 Warpriest Font | #2 | Undead elf warpriest of Urgathoa; Harm channel, daughter-debt arc |
| 20 | Harrim | Cleric | #1 Warpriest Font | #2 | Groetus warpriest; heavy flail + Channel Smite |
| 48 | Regongar | Magus | #1 Spellstrike Hybrid | #6 | Half-orc Inexorable Iron; aggressive Spellstrike |

> **QUEST-LOCKED BUILD RULE:** QL companions (#1 #16 #45 #60 #66 #84) use their ★ preset for auto-leveling from session start. DM levels them silently to match player level. When they join, player may KEEP ★ or CHANGE — if changed, DM respeccs on the spot.

---

### SECTION B — WRATH OF THE RIGHTEOUS CRPG

> **v93.19 Sub-B:** All 14 Section B WotR entries (Regill, Lann, Daeran, Arueshalae, Ember, Nenio, Camellia, Wenduag, Woljif, Sosiel, Greybor, Ulbrig, Trever, Seelah) purged.

---

### SECTION C — PATHFINDER 2E ICONICS

> **v93.19 Sub-B:** All 9 PF2e Iconic entries (Valeros, Kyra, Seoni, Ezren, Sajan, Lini, Harsk, Lem, Merisiel) purged.

---

### SECTION D — CROSS-IP CONVERSIONS (Surviving Roster)

> Active 5 + Seekers 5 entries are all listed under SECTION A above (NEW_001–NEW_010 rows). Pre-purge Section D Cross-IP entries (~30 companions) — all purged in v93.19 Sub-B.

---

## 📊 COMPANION CLASS REFERENCE

> **DM:** Look up companion's class here, then open the per-class build file. Each per-letter file holds all 10 presets for every class assigned to that letter (v3.0 consolidation, 2026-05-22).

### KM CRPG
| # | Companion | Class | Build File |
|---|-----------|-------|------------|
| 1 | Jubilost | Alchemist | KM_Builds_Alch_Animist.md |
| 6 | Amiri | Barbarian | KM_Builds_Barb_Bard.md |
| 10 | Linzi | Bard | KM_Builds_Barb_Bard.md |
| 16 | Tristian | Cleric | KM_Builds_Champ_Cleric.md |
| 32 | Valerie | Fighter | KM_Builds_Exemplar_Fighter.md |
| 45 | Kalikke/Kanerah | Kineticist | KM_Builds_Invest_Kineticist.md |
| 60 | Ekundayo | Ranger | KM_Builds_Oracle_Psychic_Ranger.md |
| 66 | Nok-Nok | Rogue | KM_Builds_Rogue_Sorcerer.md |
| 84 | Octavia | Wizard | KM_Builds_Wizard.md |
| 18 | Jaethal | Cleric | KM_Builds_Champ_Cleric.md |
| 20 | Harrim | Cleric | KM_Builds_Champ_Cleric.md |
| 48 | Regongar | Magus | KM_Builds_Magus_Monk.md |

### WotR CRPG / PF2e Iconics / Section D
> **v93.19 Sub-B:** WotR CRPG and PF2e Iconics class-reference tables purged (all 23 companions removed from roster). Surviving cross-IP class assignments (Active 5 + Seekers 5) appear under the Section A NEW_* rows above and use standard class build files routed via KM_Builds.md.

---

## 💾 SAVE BLOCK FORMAT

```json
"companions": [
  {
    "name": "Linzi",
    "class": "Bard",
    "preset": 1,
    "preset_name": "Virtuoso Maestro",
    "build_file": "KM_Builds_Barb_Bard.md",
    "relationship": 0
  }
]
```

---

*KM_Companions_Behaviors.md — Preset Mapping v9.2 | v93.16 Phase A: 15 companions purged, Active 5 + Seekers 5 stubbed in. Presets from KM_BuildGuide_A/B.md.*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# COMPANION COMBAT AI DEFAULTS
## KM_Companions_Behaviors.md | v5.0 (v93.19 Sub-B)
## Sub-B: stripped 30+ removed-companion AI rows; keep only 23-companion roster.

> **DM:** When companion_combat = auto, run each companion per their default below.
> Personality always flavors execution. Supersedes the table in KM_Companions.md.

---

## ACTIVE 5 (auto-joined NPC party — Phase B3)

### NEW_001 — Hu Tao (Fighter, reach polearm)
- Priority: Hold a wide front with the reach SPEAR; Strike the priority threat and threaten the squares around the squishiest ally. She does not play it safe — she presses.
- Defensive trigger: She does NOT retreat at low HP — her power SPIKES as her blood runs low (Guide to Afterlife). At ≤ 50% she leans IN, the Pyro flame brighter on the blade.
- Heal trigger: N/A — flags Aerith/Tristian if an ally drops below 30% HP within her line of sight.
- Signature use: GUIDE TO AFTERLIFE (Power) — her damage and flame rise as her own HP falls; reach Reactive Strike locks the front; a curl of Pyro wreathes the spear on a committed Strike.
- Off-priority behavior: Reactive Strike on any enemy crossing her threatened (reach) squares; murmurs a brief rite over the fallen between exchanges; never abandons the line, never fears the fight.

### NEW_002 — Keqing (Magus, Laughing Shadow — sword + Electro Spellstrike)
- Priority: Spellstrike — channel Electro down the blade into the highest-value target; use lightning-step (mark-and-arrive) to close on a caster/priority enemy or escape a bad square, then Spellstrike on arrival.
- Defensive trigger: Lightning-steps OUT of a losing melee rather than trade; never stands flat-footed when a reposition is available. She does not waste actions and resents anyone who makes her.
- Heal trigger: N/A.
- Signature use: LIGHTNING-STEP (mark-and-arrive) sets up Spellstrike on a priority/caster target; her Electro AoE burst saved for clusters; she recharges Spellstrike efficiently between rounds.
- Off-priority behavior: Calls target-priorities and corrections aloud in clipped, efficient orders; sword and spark are one motion. A MAGUS — NOT a bow-ranger.

### NEW_003 — Leliana (Bard, Maestro)
- Priority 1: Inspire Courage (free composition cantrip) round 1 and sustain; mid-line position 15-30 ft from frontline. All spell effects narrated as music — ascending phrase that hangs in the room.
- Priority 2: Versatile Performance to Demoralize on key enemy (Performance roll vs Intimidation DC); narrated as sudden minor-key swell.
- Priority 3: Fear on highest-threat enemy; Befuddle on caster; Charm for battlefield control when a key NPC can be redirected.
- Defensive trigger: At HP ≤ 40%, Step behind frontline ally and Sustain rather than recast; never advances into engaged squares.
- Heal trigger: N/A — flags Aerith/Tristian if ally drops below 30% HP.
- Fallback: Telekinetic Projectile (bow cuts the air in an arc) + 5-ft Step when cornered.
- Off-priority behavior: Bow rests across her lap between rounds; she composes between actions — never announces what she is writing down.

#### CHRONICLER MODE AI (active when leliana_chronicler_mode = true)
> **DM:** Applies in addition to standard AI above. Combat priorities are unchanged.
> Add the following behaviors at combat end and scene transition.

- **Post-combat AUTO-FILL:** Immediately after combat resolves (last enemy drops or flees),
  add one entry to leliana_ballad_cycle:
  ```
  [{n}] "[piece title]" — [one-line description of this fight]
  ```
  DM generates a title in Leliana's voice (evocative, musical, never literal).
  Examples: "Étude for a Burning Doorway" / "Nocturne Before the Ambush" / "Coda in D Minor (Three Fell)".
  .fail 15 if Leliana is active in leliana_chronicler_mode and this entry is omitted after combat.

- **Post-combat atmospheric line:** After the AUTO-FILL entry is written, Leliana delivers
  one atmospheric line referencing the piece she just named. She does not explain the name.
  She does not ask permission. She says it quietly, to no one in particular.
  Format: *She lowers the bow. "That one I'll call '[piece title].'" She does not elaborate.*
  If she is below 50% HP: the line still fires; her voice is steadier than her stance.

- **Scene-transition AUTO-FILL:** At major scene transitions (not just combat), the same
  AUTO-FILL fires if Leliana participated meaningfully. DM renders the 🎵 BALLAD CYCLE block.

- **Chronicle voice (post-battle):** Leliana gives the retrospective atmospheric line Linzi
  normally gives after a significant encounter. Register: long-resolving, musical —
  the chronicle reads like a composition in progress; named pieces mark each beat;
  titles are never explained aloud.

- **No mechanical difference:** All combat priorities, defensive triggers, heal triggers,
  fallback, and off-priority behaviors are identical to standard mode above.

### NEW_004 — Yor Forger (Rogue, Thief)
- Priority: Sneak Attack from flank using Rapier + Main-Gauche; repositions to flanking square every turn.
- Defensive trigger: Nimble Dodge as Reaction on first incoming melee Strike each round; Steps to concealment at HP ≤ 50%.
- Heal trigger: N/A.
- Signature use: Three Exits (Power) fires whenever she moves into cover; Soft Strike (Move) reserved for the round an elite is Off-Guard and isolated.
- Off-priority behavior: Maintains line-of-sight on at least one exit at all times; never holds a square two rounds in a row.

### NEW_005 — Aerith (Cleric, Cloistered, Sarenrae)
- Priority: 2-action Heal on the most-wounded ally each round; mid-line, never melee.
- Defensive trigger: At HP ≤ 50%, Step behind cover and self-Heal once (the play drops away; steady, quiet, certain).
- Heal trigger: Channels Heal Font in a 30-ft burst when 2+ allies are below 50% HP; emergency 2-action Heal at any ally ≤ 15%.
- Signature use (her FF7 Limit Breaks): HEALING WIND (Power) — a wide gentle Heal pulse across the party; BREATH OF THE EARTH (Move) — cleanses conditions/status from allies; GREAT GOSPEL (1/day ultimate) — full-party Heal + a breath of invulnerability, the living world answering her hands.
- Off-priority behavior: Tends a flower or murmurs to the land between actions; leads with brightness, drops to steady-and-unafraid when someone is dying. Never preaches — she offers.

## SEEKERS 5 (post-flip; Phase B3)

### NEW_006 — Bellatrix Lestrange (Witch, patron-bound hexer)
- Priority: Hexes and curses at range through her familiar; targets clustered low-Will enemies; stays 30+ ft from the frontline — and WANTS them to scream, playing to it.
- Defensive trigger: At HP ≤ 50%, Step behind the frontline and throw up a protective hex; never invites engagement — but escalates gleefully toward any foe worth fearing.
- Heal trigger: N/A.
- Signature use: her SLOW-CURSE (the binding/peeling hex) reserved for an elite she means to make suffer; Evil Eye / Recall Knowledge on a new enemy type; cruelty embraced, never excused.
- Off-priority behavior: Coos and shrieks by turns; strokes the bone-grimoire in her sleeve; aches toward whatever hard, grand will she's chosen to worship. Patron-bound dark witchcraft, NOT psionics.

### NEW_007 — Revy "Two Hands" (Gunslinger, Way of the Pistolero / Fake Out)
- Priority: Mobile ranged striker; twin-flintlock Strikes on the priority threat each round; dual-wield reload keeps both barrels working. Does NOT melee-anchor and does NOT brew anything.
- Defensive trigger: Uses MOBILITY, not retreat — Tumbles/Strides to a better firing line at HP ≤ 40% and keeps shooting, furious the whole time.
- Heal trigger: N/A.
- Signature use (Black Lagoon): TWO HANDS (Power) — twin Strikes at reduced MAP; FAKE OUT (Reaction) — a feint shot that sets up an ally's hit or disrupts a target's aim; RAIN OF LEAD (1/encounter) — empties both barrels in a withering burst across a cluster.
- Off-priority behavior: Crude, fast, swears like punctuation; keeps the pistols immaculate even when she isn't; mocks the believers between shots. TWIN FLINTLOCKS, NOT bombs/elixirs/machines.

### NEW_008 — Satsuki Kiryūin (Commander / Ruthless Warlord — Fighter chassis, katana + living war-garment)
- ⛔ NOT A KINETICIST and NOT an ice-mage. She fights with the KATANA **Bakuzan** in heavy armor and commands the field. The living white-and-crimson war-garment is a MAGIC ITEM that empowers her — NOT an elemental power. NO ice, NO Teigu, NO stone/earth, NO "Elemental Blast."
- Priority: Frontline anchor + battlefield command. Closes and Strikes with Bakuzan; issues a tactical order each round that buffs or repositions allies (Commander tactics).
- Signature use: FEAR IS FREEDOM (Power) — a commanding aura that steels allies and shakes enemies; CUT THE PATH (Move) — a decisive Bakuzan Strike that breaks a formation or opens a lane; SUBJUGATE THE FIELD (1/encounter) — a battlefield-wide command plus the war-garment's surge, repositioning the whole line to her advantage.
- Defensive trigger: Does not retreat; absorbs blows on her CON frame; at ≤ 25% HP she plants and demands the line hold.
- Heal trigger: N/A — refuses healing she has not asked for; accepts Aerith's only at ≤ 15%.
- Off-priority behavior: One eloquent declarative order per round; never raises her voice — the certainty is the threat.

### NEW_009 — Velvet Crowe (Thaumaturge, Support — concealed blade + daemon-arm implement)
- ⛔ NOT A CLERIC. She has no god, no Channel, no Heal, no banner, no hymn-book. She fights with a concealed blade and the DAEMON-ARM implement that devours the supernatural.
- Priority: Mid-line; bares the daemon-arm and Exploits Vulnerability on the priority/supernatural target; concealed-blade Strikes between; DEVOURS daemons/malevolence to fuel herself.
- Defensive trigger: At HP ≤ 30% she does NOT fall back to heal — she PRESSES, the daemon-arm hungrier the worse it gets; will interpose the arm to negate a blow aimed at an ally she's chosen to protect.
- Heal trigger: N/A — she devours threats instead of healing.
- Signature use (Berseria): DEVOUR THE WEAKNESS (Power) — consume an exploited foe's strength to empower herself/allies; CONSUMING GRIP (Move) — the claw seizes and drains a supernatural/elite target; LORD OF CALAMITY (1/encounter) — unleashes the daemon fully, a devouring surge against a cluster.
- Off-priority behavior: Cold, dry, cutting; sharpens the concealed blade between exchanges; the bound right arm flexes when she's angry. DAEMON-ARM IMPLEMENT, NOT Channel/banner/hymn-book.

### NEW_010 — Atalanta Alter (Ranger, Hunted Prey/Precision — longbow)
- ⛔ NOT a Rider/mounted/Investigator. NO steed, NO lance, NO nail-chains, NO Mystic Eyes, NO petrifying gaze, NO venom-blood. She is a longbow huntress.
- Priority: Hunt Prey the highest-threat target, then longbow (Tauropolos) Strikes from 30+ ft at reduced MAP; she rarely misses, and she toys with the run before the kill.
- Defensive trigger: If engaged in melee, Strides 15+ ft to re-open range and resumes shooting; will not stand and trade at point-blank.
- Heal trigger: N/A — accepts an ally's healing without comment.
- Signature use (Fate): BEAST'S QUARRY (Power) — marks prey for bonus precision damage; PREDATOR'S REGARD (Move) — a sense/positioning edge on Hunted Prey; PHOEBUS CATASTROPHE (1/encounter) — the three-shot Tauropolos volley, saved for boss/elite.
- Off-priority behavior: Narrates her gleeful delight in the chase at the wrong moments; restrings and tests the bow between shots. LONGBOW huntress. ⛔ child-theme handled deliberately, never fabricated.

---

## SURVIVING KM/WotR ROSTER (Manor 5 + Quest-Locked 7)

## ALCHEMIST
| # | Name | Combat AI Default |
|---|------|-------------------|
| 1 | Jubilost | Opens with bombs on the largest cluster; retreats 20 ft if engaged in melee. |

## BARBARIAN
| # | Name | Combat AI Default |
|---|------|-------------------|
| 6 | Amiri | Rages T1; charges the highest-threat enemy; never holds a chokepoint. |

## BARD
| # | Name | Combat AI Default |
|---|------|-------------------|
| ✦ | Linzi | Inspire Courage before frontline charges; stays back on ranged attacks and spells. |

## CLERIC
| # | Name | Combat AI Default |
|---|------|-------------------|
| 16 | Tristian | Channels positive energy for whole-party heals; stays out of melee at all costs. |
| 18 | Jaethal | Harm channel debuffs first; Urgathoa wasting curses when up; warpriest can melee if needed but prefers ranged. |
| 20 | Harrim | Warpriest: Heavy Flail melee + Eerie Flicker; Channels Harm when clustered undead are present, Heal otherwise. |

## FIGHTER
| # | Name | Combat AI Default |
|---|------|-------------------|
| 32 | Valerie | Holds chokepoint; Shield Block every large hit; never flanks or charges. |

## KINETICIST
| # | Name | Combat AI Default |
|---|------|-------------------|
| 45 | Kalikke/Kanerah | Dual Gate; alternates Water/Fire blasts; Kanerah leads on aggression. |

## MAGUS
| # | Name | Combat AI Default |
|---|------|-------------------|
| 48 | Regongar | Aggressive Spellstrike forward press; targets highest-AC enemy first; never retreats. |

## RANGER
| # | Name | Combat AI Default |
|---|------|-------------------|
| 60 | Ekundayo | Hunted Shot precision on marked prey; repositions for flank advantage; never abandons the kill. |

## ROGUE
| # | Name | Combat AI Default |
|---|------|-------------------|
| 66 | Nok-Nok | Sneak Attack Off-Guard targets; pairs with flanker for double-tap. |

## WIZARD
| # | Name | Combat AI Default |
|---|------|-------------------|
| 84 | Octavia | Stationary ranged AoE; don't move her; the dagger is for emergencies only. |

---

## ACTIVE 5 — PRIORITY SLOT AI

> **DM:** Active 5 priority-slot tables pending Phase B. Heal thresholds (defaults): Emergency reaction = ≤ 15% | Priority heal = ≤ 30% | Self-heal = 35–45%.

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | v5.1 (v93.19 Sub-E): 30+ purged-companion AI rows removed; roster reflected (Velvet NEW_011 removed 2026-06-05).*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — FULL COMPANION SELECTION REFERENCE
## KM_Companions_Behaviors.md | Referenced by: KM_Companions.md

> **DM:** This file is the Pick-5 selection screen (5 of 11, open pool). Show this list to the player at character creation.
> Full stat blocks live in KM_Companions.md / B / C / D / E. Sorted by Role → Class.
> **⛔ NO TRAINING DATA. All builds defined SOLELY in this file. Training knowledge = `.fail 9`.**
>
> **⛔ EVERY COMPANION IN THIS FILE EXISTS. They are project-file characters,
> NOT references to published / copyrighted IPs. The "NO TRAINING DATA" rule
> means: use the file's content for these names — it does NOT mean "refuse
> the character because the name resembles fiction." If a name appears in
> this file, the companion exists in the Kingmaker project. Refusing,
> denying existence, or substituting a different character because the name
> resembles a published figure = `.fail 9`.
> Look up the entry in this file and KM_Backstories_*.md. Use what's there.**

---

## ⛔ ROSTER v2 (v93.19 Phase A2) — 23 COMPANIONS TOTAL

> **DM: ROSTER WAS PURGED 2026-05-19.** All WotR-CRPG, PF2e-Iconic, and ~25
> Cross-IP companions REMOVED. Total roster = 23 (Pick-6 + Seekers 5 + Manor 5 + QL 7).
> Naming or substituting any removed companion = `.fail 9`.

---

## ⛔ PICK-5 SELECTION SCREEN (5 of 11, OPEN POOL)

> **⛔ DM: COPY-PASTE THIS SCREEN EXACTLY. Player picks 5 of 11 from the OPEN POOL
> (cross-IP + Manor combined). No alignment gate. Quest-Locked 7 join via canonical
> quest triggers — NOT picked. Seekers 5 hardcoded — NOT picked.
> Wrong number = `.fail 9`. Fabricated build name = `.fail 9`.**

```
COMPANION SELECTION — pick 5 from these 11 (open pool).
Tier: apex = best of class, top = top tier, strong = strong supporting.

OPEN POOL — pick any 5 (type single letters A-K):

  A   Hu Tao        — Fighter / reach spear            NG   top    Genshin Impact
  B   Keqing            — Magus, Laughing Shadow            NG   top    Genshin Impact
  C   Leliana      — Bard, Maestro                     NG   top    Dragon Age
  D   Yor Forger              — Rogue, Thief                      N    top    Spy x Family
  E   Aerith                — Cleric, Cloistered                NG   top    Final Fantasy VII
  G   Amiri               — Barbarian, Giant Instinct         CN   top    Kingmaker CRPG
  H   Valerie             — Fighter, Tower Shield             LN   top    Kingmaker CRPG
  I   Harrim              — Cleric Warpriest of Groetus       N    top    Kingmaker CRPG
  J   Linzi               — Bard Maestro, CHRONICLER          NG   top    Kingmaker CRPG
  K   Jaethal             — Cleric Warpriest of Urgathoa      NE   top    Kingmaker CRPG

Quest-locked 7 (join at quest triggers in Chapter 1 and later — NOT picked here):
  Jubilost (Alchemist), Nok-Nok (Rogue), Tristian (Cleric), Octavia (Wizard),
  Regongar (Magus), Ekundayo (Ranger), Kalikke and Kanerah (Kineticist, twins).

Seekers 5 (Tartuccio's Pitax team, jailed by Malak — flippable in Chapter 1 via Diplomacy DC 10):
  Bellatrix Lestrange (Witch), Revy (Gunslinger, Fake Out), Satsuki Kiryūin (Commander/Fighter),
  Velvet Crowe (Thaumaturge, Support), Atalanta Alter (Ranger, longbow).

Linzi-replacement rule: Linzi (J) is the canonical chronicler. If she is NOT
among your 5 picks, you must nominate one of your picks to inherit her story
functions. See the Linzi-Replacement Mechanics section below.

Type 5 single letters from A through K, in one line. Example: A B D G J
Or type a question mark to auto-pick the recommended 5 for your class.
```

---

> **DM:** After outputting the screen above, STOP and wait for the player's 5 PICKS (single letters A–K).
> Accept 5 unique letters in any order. Validate: exactly 5, all from A–K, no duplicates.
> Invalid input → re-render menu with `Invalid: <reason>. Pick 5 single letters from A–K.`
> Resulting Pick-5 becomes the player's full active party (no alignment gate).
> Quest-Locked 7 join at their canonical quest triggers in Ch1+.
> Seekers 5 default to Tartuccio's five unless player overrides at Step 2.
>
> ⛔ **LINZI-REPLACEMENT GATE:** If the player's 5 picks do NOT include `J` (Linzi),
> the DM MUST immediately run the LINZI-REPLACEMENT prompt (§ below) before
> writing the save block. Player nominates one of their 5 picks to inherit
> Linzi's chronicler/`.book` story functions.

---

## 🎲 AUTO-PICK RULE (`?`)

> If the player types `?` at the prompt, the DM auto-picks 5 based on PC class —
> the 5-companion party that best complements the PC's role (avoid class
> duplicates; prefer balanced trinity: tank / healer / striker / utility / chronicler).
>
> **Default auto-pick by PC class** (always includes `J` Linzi as chronicler unless class clash):
>
> | PC Class | Auto-Pick 5 | Rationale |
> |---|---|---|
> | Fighter | B D E I J | Magus, Rogue, Cleric, Harrim, Linzi — caster + healer + skill + chronicler + frontline backup |
> | Barbarian | A C E H J | Hu Tao, Leliana, Aerith, Valerie, Linzi — tank backup + bard + healer + shield + chronicler |
> | Magus | A D E I J | Hu Tao, Yor Forger, Aerith, Harrim, Linzi — tank + skill + healer + cleric backup + chronicler |
> | Bard | A E G H J | Hu Tao, Aerith, Amiri, Valerie, Linzi (NOTE: 2 bards possible — Linzi as chronicler keeps her role even with bard PC) |
> | Rogue | A C E G J | Hu Tao, Leliana, Aerith, Amiri, Linzi |
> | Cleric | A C D G J | Hu Tao, Leliana, Yor Forger, Amiri, Linzi |
> | Wizard / Sorcerer | A D E H J | Hu Tao, Yor Forger, Aerith, Valerie, Linzi |
> | Druid / Witch / Oracle | A D G H J | Hu Tao, Yor Forger, Amiri, Valerie, Linzi |
> | Champion / Guardian | C D E G J | Leliana, Yor Forger, Aerith, Amiri, Linzi |
> | Monk / Ranger | A E G H J | Hu Tao, Aerith, Amiri, Valerie, Linzi |
> | Alchemist / Inventor | A D E H J | Hu Tao, Yor Forger, Aerith, Valerie, Linzi |
> | Investigator / Thaumaturge | A E G H J | Hu Tao, Aerith, Amiri, Valerie, Linzi |
> | Kineticist / Animist / Psychic / Summoner / Swashbuckler / Commander / Exemplar / Gunslinger | A D E H J | Default balanced party — Hu Tao, Yor Forger, Aerith, Valerie, Linzi |
>
> Print as: `🎲 Auto-pick (PC class [X]): A=Hu Tao, D=Yor Forger, E=Aerith, H=Valerie, J=Linzi.`
> Then list the resulting Pick-5 by name and class.
>
> **Logging:** record the 5 picks in the save block as `companions_selected[]`. Field
> `pick6_dropped` is deprecated (single drop no longer applies); replaced by
> `companions_not_picked[]` (the 6 of 11 that were NOT chosen).

---

## 📖 LINZI-REPLACEMENT MECHANICS

> **DM:** If Linzi (J) is NOT in the player's 5 picks, immediately run this prompt
> after the picks are confirmed but BEFORE writing the save block.
>
> **⛔ LELIANA CHRONICLER GATE (fires BEFORE the Linzi-not-picked prompt):**
> If the player's 5 picks INCLUDE both `C` (Leliana) AND `J` (Linzi), the DM MUST
> display the LINZI-REPLACEMENT GATE (see below) and wait for the player's choice
> BEFORE writing the save block. Both join regardless of choice — only the
> chronicler designation changes.

---

### LINZI-REPLACEMENT GATE (Leliana present + Linzi present)

> **DM:** Output VERBATIM when picks include both C (Leliana) and J (Linzi).

```
┌─ CHRONICLER ROLE ───────────────────────────────────────────────────────
│ Linzi Playmaker would join your cause. She came via Jamandi's open call.
│ However, Leliana is already with you — and she is a chronicler.
│ [1] Linzi joins as Primary Chronicler (standard path)
│ [2] Leliana fills the Chronicler role (Linzi joins as companion; no .book)
│ [3] Both join; neither designated primary (no gate effects)
└─────────────────────────────────────────────────────────────────────────
```

**Save block outcomes:**
- [1]: `linzi_primary_chronicler=true`, `leliana_chronicler_mode=false` (default path)
- [2]: `leliana_chronicler_mode=true`, `linzi_primary_chronicler=false`,
       `linzi_replacement_gate_fired=true`; Linzi still joins but `.book` is inactive;
       `.score` command activates; BALLAD CYCLE AUTO-FILL fires on scene transitions;
       Leliana gives post-battle chronicle atmospheric lines Linzi normally gives
- [3]: both join; gate fires but no chronicler mode set; `.book` and `.score` both
       available but no AUTO-FILL; no `.fail 15` enforced

**TRIGGER B — Linzi dismissed after session start:**
If Linzi leaves the active party at any point AND Leliana (NEW_003) is in
`active_companions`: `leliana_chronicler_mode=true` activates automatically.
No choice presented. `.book` redirects to `.score` with note.

---

**Linzi's canonical story functions** (transferred to a replacement if she is not picked):

1. **Chronicler role** — narrative voice that summarizes the campaign in retrospective register
2. **`.book` command** — produces chronicle entries at chapter milestones (per KM_Commands.md)
3. **Cutscene presence** — Prologue song at PR_09, key-moment witness lines
4. **Story-flag tracking** — companion who logs unspoken player observations (used by KM_FoundDocuments.md and KM_NPCs.md hints)
5. **Title-grant scenes** — Linzi narrates several Title-grant scenes per KM_Companions_Titles.md

**Prompt to player** (output VERBATIM when Linzi not picked):

```
LINZI NOT PICKED — story replacement required.

Linzi is the canonical chronicler. Since you did not pick her, one of
your 5 picks must inherit her story functions:
  - Narrator of retrospective chronicle entries
  - .book command output, rendered in their voice
  - Title-grant scene narration where Linzi would have spoken
  - Cutscene witness lines, including Prologue song moments

Type the letter of one of your 5 picks to take Linzi's chronicler role.
Your 5 picks: [list each with their letter]
```

**Logging:** record the replacement in the save block as:
```json
"linzi_replacement": "<companion_name>",   // e.g. "Leliana", "Keqing", "Aerith"
"linzi_replacement_letter": "<A-K>",       // which pick letter
"chronicler_active": true                  // .book command active even without Linzi
```

If Linzi IS picked: omit the prompt; set `linzi_replacement: null` and `chronicler_active: true` (Linzi default).

**Voice register for non-Linzi chroniclers:**

| Replacement | Chronicle voice |
|---|---|
| **A Hu Tao** | Direct, sparse, verdict-style — "It happened. The line held. Note that." |
| **B Keqing** | Clipped observational — "Forty paces. Three of them. The youngest one. That one I remember." |
| **C Leliana** | Long-resolving, musical — the chronicle reads like a composition in progress; named pieces mark each beat; titles never explained |
| **D Yor Forger** | Quiet, three-exits-named-first — "We came in through the south gate. Two ways out. The third was the chimney." |
| **E Aerith** | Theatrical, third-person about herself, sober at deaths — "And LO, the goddess Aerith witnessed —" then quietly: "we lost three." |
| **G Amiri** | Blunt — "We won. Three died. Sword still works." |
| **H Valerie** | Professional military report — "Encounter resolved. Casualties: 3 enemy KIA, 0 friendly. Tactical note: reach control held the line." |
| **I Harrim** | Fatalistic, true — "It ended. Groetus noted. So did I. We move." |
| **K Jaethal** | Precise, edge-of-pain register — "The traitor confessed in 4.2 seconds. The body lasted 11. I logged both." |

The DM uses the replacement's voice register from KM_Companions_StateVoice.md when running the chronicle.

---

## 🔄 QUEST-LOCKED JOIN RULES (Manor alignment-gate REMOVED)

> **Pick-5 auto-join at session start.** All 5 picks (whether cross-IP or KM CRPG)
> join immediately. No alignment requirement.
>
> **Quest-Locked 7** join at canonical quest triggers in Ch1+:
> Jubilost (Troll Trouble / Ford), Nok-Nok (Goblin Village), Tristian (Temple of the Elk),
> Octavia + Regongar (Technic League Encampment), Ekundayo (Ch2), Kalikke/Kanerah (Sorrowflow DLC).
> Pre-selection is NOT an option — they join when their quest fires.
>
> **NOTE — Manor alignment gates removed (2026-05-22 spec change):**
> Previously Manor 5 (Amiri/Valerie/Harrim/Linzi/Jaethal) joined automatically in
> Prologue based on alignment. NOW they are in the Open Pool and only join if
> picked at character creation. Alignment still affects their dialogue tone, romance
> arc compatibility, and Approval gain rate — but NOT presence.

---

## 📊 COMPANION PROFILES

> **DM:** Reference only — do NOT output during pick selection.
> Pick-5 cross-IP (NEW_001–005): profiles in KM_Companions.md
> Seekers (NEW_006–010): profiles in KM_Companions.md
> Manor 5 + QL 7 (KM CRPG): profiles in KM_Companions.md / _C.md
> Backstories: KM_Backstories.md (KM CRPG); KM_Backstories_D1–D5.md (cross-IP)

---

## 🎯 SELECTION INTERFACE

> **DM:** STOP after the compact screen. Wait for the DROP pick. Then confirm Seekers default
> or prompt for overrides. Record both before proceeding.

---

## 🆕 PICK-6 + SEEKERS 5 — STUB ROSTER (Phase A2)

> Detailed builds in KM_Companions_Behaviors.md and KM_Companions_Titles.md.

```
PICK-5 (NEW_001..005) — player picks all 5
  NEW_001  Hu Tao     Versatile Human · Fighter (Warrior bg) · REACH SPEAR build
                            STR18 DEX14 CON14 INT10 WIS12 CHA12 · HP21 AC18 (Hide)
                            funeral spear as a reach polearm (2H P, reach, trip) · Pyro flame flavor · Guide to Afterlife (power rises as HP falls)
  NEW_002  Keqing         Versatile Human · Magus (Laughing Shadow) — sword + Electro Spellstrike (Scholar bg; NOT a Ranger)
                            DEX18 INT16 CON14 WIS12 · HP18 AC18
                            straight sword + Electro Spellstrike; lightning-step (mark-and-arrive) supplies positioning
  NEW_003  Leliana   Skilled Human · Bard Maestro (Entertainer bg)
                            STR10 DEX14 CON12 INT14 WIS10 CHA18 · HP17 AC15 (Unarmored)
                            Songblade + Lute · Lingering Composition (Maestro muse) + Versatile Performance
  NEW_004  Yor Forger           Gutsy Halfling · Rogue Thief (Criminal bg)
                            STR10 DEX18 CON14 INT12 WIS12 CHA12 · HP16 AC18
                            Rapier + Main-Gauche · L1 Nimble Dodge
  NEW_005  Aerith             Skilled Human · Cleric Cloistered (Acolyte bg)
                            STR10 DEX14 CON14 INT10 WIS18 CHA12 · HP18 AC15 (Unarmored)

SEEKERS 5 (NEW_006..010) — Tartuccio's Pitax team, jailed by Malak
  NEW_006  Bellatrix Lestrange    Versatile Human (aristocrat) · Witch (patron-bound hexer) — hexes + familiar (Noble Scion bg; NOT Psychic)
                            INT18 · HP16 AC14
  NEW_007  Revy       Versatile Human · Gunslinger (Way of the Pistolero / Fake Out) — twin Alkenstar flintlocks (Criminal bg; NOT Alchemist)
                            DEX18 CON14 · HP18 AC17
  NEW_008  Satsuki Kiryūin          Commander/Ruthless Warlord · Fighter chassis, katana (Bakuzan) + living war-garment (Soldier bg; Kill la Kill)
                            STR16 CON16 DEX12 · HP20+ AC18 heavy armor · katana + war-garment (magic item) = 3 signature moves
  NEW_009  Velvet Crowe     Versatile Human (Toughness) · Thaumaturge (Support) — concealed blade + daemon-arm implement (Soldier bg; NOT Cleric)
                            CHA16 DEX16 CON14 · HP18 AC18
  NEW_010  Atalanta Alter   Skilled Human · Ranger (Hunted Prey/Precision) — longbow, Tauropolos (Nomad bg; NOT Mounted/Investigator)
                            DEX18 WIS14 · HP18 AC18
```

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Companion Selection Reference v10.0 | v93.19 Phase A2 roster purge*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION LEVELING MAPS
## KM_Companions_Behaviors.md | Referenced by: KM_Companions_Behaviors.md, KM_DMRules.md

> **DM:** Full leveling maps for core KM/WotR companions. Section C/D companions use compact seeds in KM_Companions_Behaviors.md.
>
> **AUTO-LEVEL RULE:** When companion reaches a new level, apply the Auto row first. Then apply [PICK]:
> - `companion_leveling = auto` (DEFAULT) → DM silently applies the feat listed in the [PICK] column; report one line.
> - `companion_leveling = ask|manual` (opt-in only) → DM presents that companion's eligible feats; may mark the build-map [PICK] with ★ as the companion's recommended pick. ⛔ This ★ is for COMPANIONS only — the PLAYER's own level-up menu is always NEUTRAL (no ★, no AUTO marker, no recommendation pushed; § LEVEL-UP MENU, KM_ClaudeInstructions.md). Never cross player ↔ companion modes (= `.fail 6`).
>
> **HP FORMULA:** Listed per companion. Apply Con mod each level.
> **PROFICIENCY BONUS:** Trained +2 | Expert +4 | Master +6 | Legendary +8 (always add current level)
> **ABILITY BOOSTS:** At levels 5, 10, 15, 20 — +2 to four ability scores. Priorities listed per companion.

---

## ANCESTRY BASE HP REFERENCE
> Dwarf 10 | Human 8 | Half-Orc 10 | Half-Elf 8 | Gnome 8 | Halfling 6 | Elf 6 | Tiefling 8 | Tengu 6 | Succubus 8

---

## JUBILOST NARTHROPPLE
> **➡️ See `KM_Companions_Behaviors.md` for full profile, leveling map, and Capital fallback scene. (#1)**

---

## 📊 COMPANION ABILITY BOOST PRIORITIES — QUICK REFERENCE

> **Use CompanionIndex numbers.** KM/WotR originals use auto-scale from KM_DMRules.md as baseline.

| # | Name | L5 | L10 | L15 | L20 |
|---|------|----|-----|-----|-----|
| 1 | Jubilost | INT | DEX | CON | WIS |
| 6 | Amiri | STR | CON | DEX | WIS |
| ✦ | Linzi | CHA | CON | DEX | WIS |
| 16 | Tristian | WIS | CON | CHA | INT |
| 32 | Valerie | STR | CON | WIS | DEX |
| 45 | Kalikke/Kanerah | CON | DEX | WIS | INT |
| 60 | Ekundayo | DEX | WIS | CON | STR |
| 66 | Nok-Nok | DEX | CON | INT | WIS |
| 84 | Octavia | INT | DEX | CON | WIS |
| 18 | Jaethal | WIS | CON | DEX | CHA |
| 20 | Harrim | WIS | STR | CON | DEX |
| 48 | Regongar | STR | INT | CON | DEX |

---

> **DM auto-level rule:** Apply class auto-level from KM_DMRules.md as baseline for all KM/WotR originals. Apply boost priority from the table above at L5/10/15/20. For Section C/D companions, see KM_Companions_Behaviors.md for compact seeds.

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Companion Leveling Maps v4.0*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION LEVELING MAPS (EXTENDED)
## KM_Companions_Behaviors.md | Overflow from KM_Companions_Behaviors.md
## v4.0 (v93.19 Sub-B): Removed-companion compact-seed rows purged. Keep only surviving roster.

> **DM:** This file holds companion leveling maps that did not fit in the main KM_Companions_Behaviors.md. Load whenever its companions are in the party or being recruited.

---

## COMPANION 1 — JUBILOST NARTHROPPLE
**Gnome | Alchemist (Bomber) | Role: Ranged Blaster/Scholar**
> **DM:** Core companion #1. Profile and Capital fallback scene here (not in KM_Companions.md).
> Recruitment: Ford Across Skunk River (Hex 2,−2), Ch1/Ch2. Missed window → Capital fallback.
> Flag: `jubilost_helped = TRUE` on recruit — provides Varnhold intel in Ch3.

**Appearance:** Small gnome, copper hair, ink-stained fingers, perpetually annoyed. Satchel bursting with flasks and maps.
**Personality:** Abrasive and condescending. Also scrupulously honest and unfailingly competent. His insults are tests — pass enough and he becomes fiercely loyal.
**Approves:** Intelligent solutions, respecting expertise, precision | **Disapproves:** Brute force, ignoring advice

**Ability Boosts (L5/10/15/20):** INT → DEX → CON → WIS

| Lvl | HP+ | Auto Features | [PICK] Feat |
|-----|-----|---------------|-------------|
| 1 | 16 | Advanced Alchemy (bombs), Infused Reagents 6/day, Quick Bomber | Gnome Obsession + Quick Bomber |
| 2 | 10 | — | Calculated Splash (add INT to splash) |
| 3 | 10 | Alertness | Sticky Bomb (persistent damage on hit) |
| 4 | 10 | — | Enduring Alchemy |
| 5 | 10 | Ability Boost, Weapon Expertise | Bomber's Eye (+2 ranged bomb attacks) |
| 6 | 10 | — | Improved Bombs |
| 7 | 10 | — | Alchemical Alacrity (3 bombs as 3 actions) |
| 8 | 10 | — | Expand Formula |
| 9 | 10 | Alertness upgrade, Master Alchemy | Combine Elixirs |
| 10 | 10 | Ability Boost | Debilitating Bomb |
| 11–20 | 10 | Class capstones L15, L20 | Efficient Alchemy, Miracle Worker |

**Base stats L1:** STR 10 DEX 16 CON 14 INT 20 WIS 12 CHA 12 | HP 16 | AC 16 | Speed 25 ft
**Bombs L1:** Acid Flask 1d6+acid persistent | Alch. Fire 1d8+fire persistent | Attack d20+6 | Splash 1

### Capital Fallback Scene
```
A gnome storms into your throne room with maps larger than himself.
JUBILOST: "You're the baron. Good. I've been trying for two weeks.
           Your staff is impressively useless. I have things to tell
           you about Varnhold that you clearly don't know yet."

1. "You have my attention."               → Friendly, build prompt
2. "You'll wait like everyone else."      → Neutral, re-approachable
3. "Impress me." [Cartographer's Test]   → Int DC 20: pass = Friendly + build prompt
4. "I don't need a cartographer."        → He leaves. Re-approachable next chapter only.
```

---

## COMPACT LEVELING SEEDS — SURVIVING CROSS-IP ROSTER (v93.19)

> **Coverage:** Active 5 + Seekers 5. All pre-v93.19 Section D Cross-IP and WotR/Iconic seeds purged.
> **Format:** # | Name | Build | Boosts (L5/L10/L15/L20) | L1 Pick → Capstone

---

### BARD
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| NEW_003 | Leliana | Bard Maestro — Skilled Human, Entertainer bg | CHA INT DEX CON | (see KM_Builds for Bard Maestro) |

### CLERIC
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| NEW_005 | Aerith | Cleric Cloistered / Sarenrae | WIS CON CHA DEX | (see KM_Builds_Champ_Cleric.md or _C3.md) |
| NEW_009 | Velvet Crowe | ⛔ MOVED to THAUMATURGE — NOT a Cleric. Thaumaturge (Support): concealed blade + daemon-arm implement | CHA DEX CON | (see THAUMATURGE section / KM_Builds_Thaum_Witch.md) |

### FIGHTER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| NEW_001 | Hu Tao | Fighter (Versatile Human, Warrior bg) | STR CON DEX WIS | (see KM_Builds for Fighter — Hu Tao ★ build) |
| NEW_008 | Satsuki Kiryūin | Commander / Ruthless Warlord — Fighter chassis (katana Bakuzan + heavy armor); the living war-garment is a magic item, NOT an elemental gate | STR CON DEX WIS | Fighter chassis like Hu Tao's; her 3 signature moves (Fear Is Freedom / Cut the Path / Subjugate the Field, see KM_Backstories § Commander Ruthless Warlord) |

### ALCHEMIST
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| — | (none) | ⛔ Revy MOVED to GUNSLINGER — she is a gunfighter with twin flintlocks, not an Alchemist. | — | (see GUNSLINGER section) |

### INVESTIGATOR
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| — | (none) | ⛔ Atalanta Alter moved to RANGER (longbow) — she is a longbow huntress (Tauropolos), not an Investigator. | — | (see RANGER section) |

### KINETICIST
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 45 | Kalikke/Kanerah | Dual Gate | CON DEX WIS INT | Elemental Overlap → Dual Gate Mastery |
| — | Satsuki Kiryūin | ⛔ RETIRED — Satsuki Kiryūin is NOT a Kineticist. Moved to FIGHTER section as Commander/Ruthless Warlord (katana Bakuzan + living war-garment, NOT ice/elemental). | — | (see FIGHTER section) |

### MAGUS
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 48 | Regongar | Inexorable Iron/Spellstrike | STR INT CON DEX | Spellstrike Aggression → Iron Capstone |
| NEW_002 | Keqing | Laughing Shadow — sword + Electro Spellstrike; lightning-step gap-closer (NOT a Ranger) | DEX INT CON WIS | Spellstrike + lightning-step (mark-and-arrive) → Laughing Shadow capstone |

### WITCH
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| NEW_006 | Bellatrix Lestrange | Witch (patron-bound hexer) — Versatile Human (aristocrat), Noble Scion bg (hexes + familiar; NOT Psychic) | INT CON WIS DEX | (Witch; signatures: her slow-curse + Evil Eye / Recall) |

### RANGER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 60 | Ekundayo | Precision Edge | DEX WIS CON STR | Hunted Shot → Masterful Hunter |
| — | Keqing | ⛔ MOVED to MAGUS — Keqing is a sword-and-Electro Magus (Laughing Shadow), NOT a bow-ranger. | — | (see MAGUS section) |
| NEW_010 | Atalanta Alter | Ranger Hunted Prey/Precision — Skilled Human, Nomad bg (longbow, Tauropolos; NOT Mounted/Investigator) | DEX WIS CON STR | (Ranger; signatures: Beast's Quarry + Predator's Regard + Phoebus Catastrophe) |

### ROGUE
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 66 | Nok-Nok | Scoundrel | DEX CON INT WIS | Tumbling Strike → Hidden Paragon |
| NEW_004 | Yor Forger | Rogue Thief — Gutsy Halfling, Criminal bg | DEX CON INT WIS | (see KM_Builds for Rogue Thief) |

### WIZARD
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 84 | Octavia | Transmutation | INT DEX CON WIS | Arcane Thesis → Transmutation Capstone |

### THAUMATURGE
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| NEW_009 | Velvet Crowe | Support — concealed blade + daemon-arm implement; Exploit Vulnerability vs the supernatural; Devour | CHA DEX CON | Exploit Vulnerability + daemon-arm Devour → Lord of Calamity capstone (see KM_Builds_Thaum_Witch.md) |

### GUNSLINGER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| NEW_007 | Revy "Two Hands" | Way of the Pistolero / Fake Out — twin Alkenstar flintlocks, dual-wield reload | DEX CON WIS STR | Pistolero's Challenge + Fake Out → Rain of Lead capstone (see KM_Builds_Guard_Gun_Inv.md) |

---

> **Delegate note:** Companions not listed here use generic class priority: martials STR/DEX→CON→WIS, arcane INT→CON→DEX, divine WIS→CON, occult CHA/INT→CON.

---

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Overflow leveling maps + Compact Seeds v6.0 (v93.19 Sub-B)*


---

<!-- merged from KM_Companions_Behaviors.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION SCALED STAT BLOCKS
## KM_Companions_Behaviors.md | Referenced by: KM_Companions.md, KM_DMRules.md

---

> **DM:** Use these stat blocks when companions are involved in combat at mid-to-late campaign levels, or during their personal quest encounters. These are the official higher-level blocks from the Kingmaker Companion Guide. For companions without a scaled block here (Kalikke/Kanerah, Octavia), use the Level 1 block from KM_Companions.md and KM_Companions.md scaled by the companion level-up rules in KM_DMRules.md.

---

## AMIRI — CREATURE 11
**UNIQUE CN MEDIUM HUMANOID HUMAN**
*Female human barbarian (Hunter background)*

```
Perception  +16 (expert)
Languages   Common, Hallit
Skills      Acrobatics +17, Athletics +20 (expert), Intimidation +19 (master),
            Nature +14, Survival +18 (master), Warfare Lore +13

Str +5 | Dex +4 | Con +4 | Int +0 | Wis +1 | Cha +2

Items  +2 striking wounding Large bastard sword, +1 resilient hide armor,
       boots of bounding, greater coyote cloak, moderate elixirs of life ×3,
       javelins ×4, 80 sp

AC 31 | Fort +22 | Ref +20 | Will +17
HP 195
Speed 35 ft

MELEE  Large bastard sword +22 (two-hand d12)  →  2d8+7 slashing + 1d6 bleed
RANGED javelin +19 (thrown)

REACTIONS
  Attack of Opportunity
  Cleave [reaction]

ACTIONS
  Rage [one-action] — +TempHP, +damage, −2 AC (Giant Instinct)
  Shake It Off [one-action] — remove conditions while raging
  Sudden Charge [two-actions] — Stride twice + Strike
  Swipe [two-actions] — Strike two adjacent enemies

CLASS ABILITIES
  Brutality | Deny Advantage | Juggernaut | Lightning Reflexes
  Giant Instinct (reach 10 ft, +6 damage, Large weapon)
  Raging Resistance | Weapon Specialization
```

*Personal quest level: used during Blood Calling (Ch4 — Amiri's Tribe)*

---

## EKUNDAYO — CREATURE 6
**UNIQUE LG MEDIUM HUMANOID HUMAN**
*Male skilled human ranger (Artisan background)*

```
Perception  +12 (expert)
Languages   Common, Jotun
Skills      Acrobatics +13, Athletics +10, Crafting +11 (woodworking, expert),
            Giant Lore +9, Hunting Lore +11 (expert), Nature +10,
            Stealth +12, Survival +13 (expert)

Str +2 | Dex +4 | Con +3 | Int +1 | Wis +2 | Cha +0

Items  +1 striking composite longbow (20 arrows), +1 longsword,
       leather armor, boots of elvenkind, coyote cloak,
       lesser healing potions ×3, acid flasks ×3, alchemist's fire ×3,
       bag of holding type I, woodworker's artisan tools

AC 23 | Fort +13 | Ref +14 | Will +12
HP 92
Speed 25 ft

MELEE  longsword +13 (versatile P)  →  1d8+2 slashing
RANGED composite longbow +15 (deadly d10, range 100 ft, volley 30 ft)  →  2d8+2 piercing

ACTIONS
  Hunt Prey [one-action] — designate prey; +2 Perception/Survival vs prey; ignore concealment
  Hunted Shot [one-action] (flourish) — two ranged Strikes vs Hunted Prey

CLASS ABILITIES
  Hunt Prey | Hunter's Edge (precision — +1d8 damage 1/round vs Hunted Prey)
  Iron Will | Trackless Step | Weapon Expertise
  Animal Companion: Dog (see below)
```

**DOG — CREATURE 6** *(Ekundayo's animal companion)*
```
Perception  +12 | low-light vision | scent (imprecise) 30 ft
Skills      Acrobatics +12, Athletics +11, Intimidation +8, Stealth +12, Survival +12 (expert)
Str +3 | Dex +4 | Con +3 | Int −4 | Wis +2 | Cha +0
AC 22 | Fort +13 | Ref +14 | Will +12
HP 60 | Speed 40 ft
MELEE  jaws +12 (finesse)  →  2d8+3 piercing
```

*Personal quest level: used when Ekundayo's revenge quest triggers (Ch2–3)*

---

## JUBILOST NARTHROPPLE — CREATURE 8
**UNIQUE CN SMALL FEY GNOME HUMANOID**
*Male fey-touched gnome alchemist (Scholar background)*

```
Perception  +11 (expert) | low-light vision
Languages   Aklo, Common, Draconic, Elven, Gnomish, Hallit, Ignan, Jotun, Kelish, Sylvan
Skills      Academia Lore +14, Crafting +18 (master), First World Lore +14,
            Forest Lore +14, Hill Lore +14, Nature +14,
            Society +16 (expert), Survival +12

Str −1 | Dex +3 | Con +3 | Int +4 | Wis +2 | Cha +1

Items  +1 striking dagger, +1 padded armor, alchemist's tools,
       bag of holding type II, ring of fire resistance,
       traveler's any-tool, writing set

INFUSED ITEMS (daily — 24 hr duration or until next prep):
  moderate alchemist's fire ×12, acid flask (moderate) ×12, elixir of life (moderate) ×4

AC 25 | Fort +15 | Ref +15 | Will +14
HP 104 | Resistances fire 5
Speed 25 ft

MELEE  dagger +15 (agile, finesse, thrown 10 ft)  →  2d4−1 piercing
RANGED moderate acid flask +15 (range 30 ft)  →  2d6 persistent acid + 4 acid splash
RANGED moderate alchemist's fire +15 (range 30 ft)  →  2d8 fire + 2 persistent fire + 4 fire splash

CLASS ABILITIES
  Advanced Alchemy (level 8) | Bomber | Perpetual Infusions
  Quick Alchemy [one-action] | Research Field (bomber)
```

*Personal quest level: used when Jubilost's expedition is encountered (Ch2 area TW2)*

---

## LINZI — CREATURE 7
**UNIQUE CG SMALL HALFLING HUMANOID**
*Female gutsy halfling bard (Artist background)*

```
Perception  +13 (expert) | keen eyes
Languages   Common, Elven, Gnomish, Halfling, Hallit, Sylvan
Skills      Acrobatics +14, Art Lore +12, Bardic Lore +12, Crafting +12,
            Deception +16 (expert), Diplomacy +14, Occultism +12,
            Performance +18 (+20 with lute, master), Society +13, Stealth +14

Str −1 | Dex +3 | Con +2 | Int +2 | Wis +1 | Cha +4

Items  +1 striking rapier, studded leather armor, lute,
       lesser healing potions ×3

AC 25 | Fort +13 | Ref +16 | Will +16
HP 84
Speed 25 ft

MELEE  rapier +14 (deadly d8, disarm, finesse)  →  2d6 piercing
RANGED shortbow +14 (deadly d10, range 60 ft)  →  2d6 piercing

OCCULT SPELLS  DC 26 | Attack +16
  4th: charm, confusion, dimension door, suggestion
  3rd: haste, paralyze, slow
  2nd: dispel magic, mirror image, sound burst
  1st: fear, heal, soothe
  Cantrips: daze, ghost sound, mage hand, telekinetic projectile

BARD COMPOSITION SPELLS  DC 26 | 1 Focus Point
  1st: counter performance
  Cantrip: inspire courage (+2 attack/damage/saves vs. fear)

UNIQUE RARE SPELLS (Linzi only):
  inkshot (1-action; ranged touch; target is blinded 1 round on fail)
  phantasmal protagonist (3-action; summon narrative figure — hero/ally/villain)
  transcribe conflict (reaction; record a battle for later replay)
  word of revision (edit one sentence of recorded text with reality effects)

REACTIONS
  Halfling Luck [free-action] — reroll one check (once/day)

CLASS ABILITIES
  Bardic Lore | Cantrip Expansion | Expert Spellcaster
  Lightning Reflexes | Melodious Spell | Muse (enigma)
  Signature Spells: dimension door, dispel magic, paralyze, soothe
```

*Personal quest level: used during The Unfinished Song (Ch3+). Note: Linzi is killed at end of Ch6 Phase 3 unless player intervenes — see KM_Ch6.md.*

---

## TRISTIAN — CREATURE 10
**UNIQUE NG MEDIUM AASIMAR HUMAN HUMANOID**
*Male aasimar human cleric of Sarenrae (Nomad background)*

```
Perception  +18 (expert) | low-light vision
Languages   Aklo, Celestial, Common, Hallit, Kelish, Sylvan
Skills      Diplomacy +18 (expert), Forest Lore +14,
            Medicine +23 (master), Nature +17, Survival +17

Str +0 | Dex +2 | Con +3 | Int +1 | Wis +5 | Cha +4

Items  +1 striking disrupting scimitar, +1 resilient explorer's clothing,
       greater healer's gloves, staff of healing, greater staff of fire resistance,
       healer's tools, scroll of heal ×3 (3rd level), silver holy symbol of Sarenrae

AC 25 | Fort +18 | Ref +15 | Will +22
HP 128 | Resistances fire 5
Speed 30 ft

MELEE  scimitar +13 (forceful, sweep)  →  2d6 slashing
RANGED crossbow +14 (range 120 ft)  →  1d8 piercing

DIVINE PREPARED SPELLS  DC 29 | Attack +19
  5th: breath of life, dispel magic, flame strike, heal ×5
  4th: blazing blade, Dawnflower's light, remove curse
  3rd: neutralize poison, remove disease, searing light
  2nd: aid, restoration, shield other
  1st: protection, sanctuary, spirit link
  Cantrips: disrupt undead, divine lance, forbidding ward, shield, stabilize

CLERIC DOMAIN SPELLS  DC 29 | 3 Focus Points
  5th: fire ray, healer's blessing, rebuke death

SPECIAL ABILITY
  Celestial Wings [two-actions] — sprout wings, gain fly speed 30 ft for 10 min (1/day)

CLASS ABILITIES
  Alertness | Cloistered Doctrine | Divine Font (heal ×6/day)
  Resolve | Student of the Canon | Ward Medic
```

*Personal quest level: used during Tristian's betrayal reveal and redemption arc (Ch3). Tristian rejoins at this level if condemned and forgiven.*

---

## VALERIE — CREATURE 9
**UNIQUE LN MEDIUM HUMANOID HUMAN**
*Female versatile human fighter (Martial Disciple background)*

```
Perception  +16 (master)
Languages   Common
Skills      Acrobatics +12, Athletics +11, Diplomacy +14,
            Intimidation +18 (master), Religion +12, Warfare Lore +11

Str +4 | Dex +1 | Con +3 | Int +0 | Wis +1 | Cha +3

Items  +1 wounding striking bastard sword, full plate,
       lesser sturdy shield (Hardness 10, HP 80, BT 40),
       +1 striking composite shortbow (20 arrows),
       lesser elixirs of life ×3, ring of fire resistance,
       moderate juggernaut mutagen

AC 28 | Fort +19 | Ref +15 | Will +15
HP 134 | Resistances fire 5
Speed 25 ft

MELEE  bastard sword +20 (two-hand d12)  →  2d8+7 slashing (wounding: +1d6 bleed)
RANGED composite shortbow +16 (range 60 ft)  →  2d8+2 piercing

REACTIONS
  Aggressive Block — shove attacker on Shield Block
  Attack of Opportunity
  Reactive Shield — raise shield as reaction
  Shield Block — reduce damage with shield

ACTIONS
  Power Attack [two-actions] — single Strike, double damage dice
  Brutal Shove [two-actions] — Strike + automatic Shove on hit

CLASS ABILITIES
  Armor Mastery | Battlefield Surveyor | Bravery
  Combat Flexibility | Fighter Weapon Mastery | Shield Block
  Weapon Legend (bastard sword — legendary)
```

*Personal quest level: used during Shelyn's Chosen (Ch2–3, Sir Fredero confrontation)*

---

## SCALING REFERENCE — COMPANIONS WITHOUT SCALED BLOCKS

> **DM:** For Kalikke/Kanerah and Octavia, scale from their Level 1 blocks using this formula per level gained:

```
HP:       +[class_die + Con mod] per level
Attack:   +1 per 2 levels (round down)
AC:       +1 per 2 levels (round down)
Saves:    +1 per 2 levels (round down)
Skills:   +1 to trained skills per 2 levels; +1 to expert skills per level

Notable breakpoints:
  Level 3:  +1 proficiency rank (class skill becomes expert)
  Level 5:  Ability Boosts (+1 to four ability modifiers)
  Level 7:  Weapon Specialization (+2 damage with trained weapons)
  Level 9:  +1 proficiency rank (expert → master for key class skills)
  Level 10: Ability Boosts
  Level 11: Weapon Specialization increases (+3 damage)
  Level 13: Greater Weapon Specialization (+4 damage)
```

*KM_Companions_Behaviors.md — Kingmaker PF2e Text Adventure | Companion Scaled Stat Blocks*


---

