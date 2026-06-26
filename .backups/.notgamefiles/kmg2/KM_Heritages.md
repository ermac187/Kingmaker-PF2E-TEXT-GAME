# KINGMAKER — HERITAGE CATALOG (CORE + UNCOMMON + KINGMAKER)
## KM_Heritages.md | Referenced by: KM_CharCreate.md STEP 4, KM_AncestryGuide.md
## ⛔ ALSO LOAD: KM_Heritages_B.md — Rare ancestries + Versatile heritages

> **⛔ DM: Load BOTH files at character-creation Step 4** (after ancestry is confirmed, before Step 5 background). This file covers Core + Uncommon + Goliath. KM_Heritages_B.md covers Rare + Versatile heritages. The player picks ONE heritage — either their ancestry's specific heritage (this file for Core/Uncommon/Goliath, `_B` for Rare) OR a Versatile Heritage (§ VERSATILE HERITAGES in `_B` — works on any ancestry). Heritages are FREE — they do NOT consume ancestry feat slots.

---

## ⛔ STEP 4 HERITAGE FLOW

1. Look up the player's ancestry in this file OR KM_Heritages_B.md. Display the heritage block VERBATIM. Show ALL options — no skipping.
2. Say: *"Heritages are free — they don't cost ancestry feats. Pick a number, or type `versatile` to see cross-ancestry options."*
3. Wait for player input.
4. If player types `versatile`: display § VERSATILE HERITAGES from KM_Heritages_B.md. Wait for pick.
5. Record in the save block:
   - `player.heritage = "<name>"`
   - `player.heritage_source = "ancestry-specific" | "versatile"`
   - Add granted abilities to `player.senses[]`, `player.resistances{}`, `player.immunities[]`, `player.feats.heritage[]`, or `player.class_features[]` as appropriate.
6. Proceed to Step 5 (Background).

**Violations:**
- Skipping the heritage step entirely: `.fail 9`
- Fabricating a heritage not listed in EITHER file: `.fail 9`
- Describing heritage effects from PF2e training data instead of these files: `.fail 9`
- Applying heritage bonuses incorrectly or to the wrong ancestry: `.fail 6`

> **Source:** Heritage names and mechanical effects verified against Archives of Nethys (2e.aonprd.com) Remaster data — Player Core, Player Core 2, Lost Omens: Impossible Lands, Lost Omens: Tian Xia, Lost Omens: Mwangi Expanse, Ancestry Guide, Rage of Elements. Legacy (pre-Remaster) names accepted as input and shown where relevant.

---

## 📊 SCALING REFERENCE

Several heritages grant resistance or bonuses that scale with level.

| Heritage effect | L1–4 | L5–9 | L10–14 | L15+ |
|-----------------|------|------|--------|------|
| Resist (1/2 level, min 1) | 1 | 2–4 | 5–7 | 8+ |
| Innate cantrip | heightened to half your level rounded up |
| Void healing (Dhampir) | categorical — no scaling |
| Damning Strikes (Duskwalker) | +1d4 vs undead → +1d6 at L10 → +1d8 at L15 |

**Rule:** Scaling is automatic. DM does NOT ask the player to track. Use `player.level` at each combat.

---

## 🧬 CORE ANCESTRIES

### HUMAN — Ability Boosts: 2 free
```
[1] Skilled Human       — Trained in 1 skill of your choice; expert at level 5.
[2] Versatile Human     — Gain 1 general feat of your choice you qualify for. *(DM: load KM_GeneralFeats.md and present filtered list — never just say "name any.")*
[3] Wintertouched Human — Cold resist 1/2 level (min 1); environmental cold one step less extreme.
```
**Best for:** Any class. Versatile is the workhorse — enables 1-level multiclass dips without paying the feat slot. Skilled for extra skill breadth. Wintertouched for Stolen Lands winter travel.

---

### ELF — Ability Boosts: +DEX, +INT, free
```
[1] Ancient Elf    — Gain 1 multiclass dedication feat at L1, ignoring class level prerequisites.
[2] Arctic Elf     — Cold resist 1/2 level; environmental cold one step less extreme.
[3] Cavern Elf     — Gain darkvision.
[4] Desert Elf     — Fire resist 1/2 level; environmental heat one step less extreme.
[5] Seer Elf       — Cast *detect magic* at will as a primal innate cantrip.
[6] Whisper Elf    — +2 circumstance to Perception to locate hidden creatures by sound; hearing +30 ft.
[7] Woodland Elf   — Climb speed 10 ft on trees/plants; ignore difficult terrain from plants.
```
**Best for:** Ancient = multiclass fuel (Magus/Wizard/Spellshot). Arctic/Desert = environmental specialist. Seer = caster utility. Whisper = scout. Woodland = Ranger flavor. Cavern = dungeon delver.

---

### DWARF — Ability Boosts: +CON, +WIS, free; flaw −CHA
```
[1] Ancient-Blooded Dwarf  — Reaction 1/day: +1 status to saves vs magic until end of turn.
[2] Anvil Dwarf            — Trained in Crafting; pick 2 specialty areas instead of 1.
[3] Death Warden Dwarf     — Successful saves vs void/undead become critical successes.
[4] Elemental Heart Dwarf  — 1/day: deal 1d6 energy damage to adjacent creatures (scales with level).
[5] Forge Dwarf            — Fire resist 1/2 level; environmental heat one step less extreme.
[6] Forge-Blessed Dwarf    — 1/week: cast a dwarven deity's 1st-level cleric spell as innate.
[7] Oathkeeper Dwarf       — +1 status to Will saves and Sense Motive; penalty when you lie.
[8] Rock Dwarf             — +2 status vs forced movement/prone; halve forced movement distance.
[9] Strong-Blooded Dwarf   — Poison resist 1/2 level; reduce poison stage faster on saves.
```
**Best for:** Rock = tank. Forge = fire-resist frontline. Anvil = crafter. Elemental Heart = element caster. Ancient-Blooded / Death Warden = caster defense / undead hunter. Forge-Blessed = dwarven faith caster. Oathkeeper = Champion / Cavalier.

---

### HALFLING — Ability Boosts: +DEX, +WIS, free; flaw −STR
```
[1] Gutsy Halfling     — Successes on saves vs emotion effects become critical successes.
[2] Hillock Halfling   — Overnight rest and treated wounds restore extra HP equal to your level.
[3] Jinxed Halfling    — Gain the Jinx action to curse a creature with clumsiness (replaces Halfling Luck access).
[4] Nomadic Halfling   — Gain 2 extra languages at creation; +1 language whenever you gain Multilingual.
[5] Observant Halfling — +1 circumstance to Perception when seeking hidden/undetected creatures.
[6] Twilight Halfling  — Gain low-light vision.
[7] Wildwood Halfling  — Ignore difficult terrain caused by plants/fungi (bushes, vines, undergrowth).
```
**Best for:** Gutsy = emotion-save defense (Ch6 Nyrissa fear). Hillock = tanky caster. Observant = Investigator. Twilight = Rogue/Scout. Nomadic = Bard/Face. Wildwood = forest-campaign god (Stolen Lands).

---

### GNOME — Ability Boosts: +CON, +CHA, free
```
[1] Chameleon Gnome    — Change skin/hair colors; +2 circumstance to Stealth when matching surroundings.
[2] Fey-Touched Gnome  — Gain fey trait; cast 1 primal cantrip at will (swap daily in meditation).
[3] Kijimuna Gnome     — Choose: Combat Climber feat with auto-crits on climb, OR 15-ft swim speed.
[4] Sensate Gnome      — Imprecise scent 30 ft; +2 circumstance to locate undetected creatures by scent.
[5] Umbral Gnome       — Gain darkvision.
[6] Vivacious Gnome    — Void resist 1/2 level; reduce the doomed condition by one step.
[7] Wellspring Gnome   — Choose arcane/divine/occult cantrip at will as innate; converts primal innates to that tradition.
```
**Best for:** Fey-Touched = Witch/Druid. Umbral = Shadow Sorcerer / dungeon caster. Wellspring = multiclass caster. Sensate = Investigator. Vivacious = undead/Vordakai hunter (Ch3). Kijimuna = river/climb specialist.

---

### GOBLIN — Ability Boosts: +DEX, +CHA, free; flaw −WIS
```
[1] Charhide Goblin    — Fire resist 1/2 level (min 1); DC 10 flat check to end persistent fire (was 15).
[2] Dokkaebi Goblin    — Cast *figment* at will as occult innate cantrip; +1 Will vs illusions.
[3] Irongut Goblin     — Eat spoiled food without penalty; +2 saves vs ingested afflictions and sickened.
[4] Razortooth Goblin  — Jaws unarmed attack: 1d6 piercing (finesse, brawling group).
[5] Snow Goblin        — Cold resist 1/2 level (min 1); environmental cold one step less extreme.
[6] Tailed Goblin      — +2 circumstance to Athletics to climb; reduce hands needed to climb/trip by 1.
[7] Treedweller Goblin — +2 circumstance to Stealth and Survival in forests/jungles.
[8] Unbreakable Goblin — Ancestry HP becomes 10 (was 6); halve falling damage.
```
**Best for:** Razortooth = Rogue Ruffian. Irongut = Alchemist. Unbreakable = frontline/Barbarian. Charhide = fire-themed. Dokkaebi = illusion caster. Tailed/Treedweller = mobility/forest scout.

---

## 🧬 UNCOMMON ANCESTRIES

### HOBGOBLIN — Ability Boosts: +CON, +INT, free
```
[1] Elfbane Hobgoblin    — Reaction: +1 (+2 vs arcane) circumstance to a save vs magical effect.
[2] Runtboss Hobgoblin   — Gain Group Coercion feat; improved Intimidation results vs goblins.
[3] Shortshanks Hobgoblin — Gain Ride feat; cannot be off-guard while climbing.
[4] Smokeworker Hobgoblin — Fire resist 1/2 level; auto-succeed flat checks vs smoke-concealed creatures.
[5] Steelskin Hobgoblin   — Persistent-damage recovery DC becomes 13 (was 15), or 8 with assistance.
[6] Warmarch Hobgoblin    — Subsist on poor meals when foraging fails; Hustle twice as long during exploration.
[7] Warrenbred Hobgoblin  — Underground: reduced DCs vs concealed/hidden; auto-crit Acrobatics Squeeze.
```
**Best for:** Elfbane = anti-caster specialist. Warrenbred = dungeon crawler. Warmarch = overland-travel / Commander. Smokeworker = fire-build / Alchemist. Runtboss = Commander / Intimidate. Steelskin = frontline persistent-damage resistance. Shortshanks = mounted / climber.

---

### LESHY — Ability Boosts: +CON, +WIS, free
```
[1] Cactus Leshy       — Spine unarmed attack (1d6 piercing, finesse).
[2] Chrysanthemum Leshy — Poison resist 1/2 level; 1/day create a usable antidote.
[3] Fruit Leshy         — 1/day detach a healing fruit; an ally eating it regains HP equal to your level.
[4] Fungus Leshy        — Gain darkvision; trait changes from plant to fungus.
[5] Gourd Leshy         — Store up to 1 Bulk of objects inside your hollow head.
[6] Leaf Leshy          — Take no damage from falls of any distance.
[7] Lotus Leshy         — Walk on still water surfaces at half Speed.
[8] Peachchild Leshy    — Communicate with and influence domesticated animals.
[9] Pine Leshy          — Gain Combat Climber as bonus feat; +1 Reflex.
[10] Root Leshy         — Extra HP; +2 status vs forced movement and prone.
[11] Seaweed Leshy      — Swim speed; breathe underwater; land Speed reduced.
[12] Vine Leshy         — Climb speed 10 ft; +2 Athletics to climb; climb without free hands.
```
**Best for:** Cactus = reactive grapple punisher. Fruit = party support / Druid. Fungus = dungeon delver. Root/Pine = tank vs CC. Vine = scout / forester. Seaweed = river campaign (Stolen Lands). Chrysanthemum = poison-heavy Ch2 (troll venom). Peachchild = wilderness companion handler.

---

### ORC — Ability Boosts: +STR, +CON, free
```
[1] Badlands Orc     — Hustle twice as long; environmental heat one step less extreme.
[2] Battle-Ready Orc — Trained in Intimidation; gain the Intimidating Glare feat.
[3] Deep Orc         — Gain Terrain Expertise (underground) and Combat Climber feats.
[4] Grave Orc        — Void resist 1/2 level; +1 status to saves vs death and void effects.
[5] Hold-Scarred Orc — Ancestry HP becomes 12 (was 10); gain Diehard feat.
[6] Rainfall Orc     — +2 Athletics to climb/swim; +1 circumstance to saves vs disease.
[7] Winter Orc       — Trained in Survival; environmental cold one step less extreme.
```
**Best for:** Battle-Ready = Barbarian / Commander (Intimidate-scaling). Hold-Scarred = Barbarian (Ferocity + Diehard). Grave = Ch3 Vordakai encounters. Deep = dungeon Fighter. Rainfall = river/swamp campaigns (Hargulka Ch2, Old Beldame). Winter = overland travel. Badlands = desert-speed caravan.

---

### RATFOLK (YSOKI) — Ability Boosts: +DEX, +INT, free
*Remaster note: Heritage names drop the "-folk" suffix (e.g., "Deep Rat" not "Deep Ratfolk").*
```
[1] Deep Rat      — Gain darkvision.
[2] Desert Rat    — Speed 30 ft on all fours; heat one step less extreme; x10 starvation endurance; cold worse.
[3] Longsnout Rat — Imprecise scent 30 ft; +2 Perception to Seek within scent range.
[4] Sewer Rat     — Immune to putrid plague; +1 to disease/poison saves; crit-success ratchet.
[5] Shadow Rat    — Trained in Intimidation; coerce animals; animal attitudes toward you start worse.
[6] Snow Rat      — Cold resist 1/2 level; environmental cold one step less extreme.
[7] Tunnel Rat    — Gain Quick Squeeze feat; ignore difficult terrain from tight (non-squeeze) spaces.
```
**Best for:** Longsnout = Investigator / Ranger-tracker. Sewer = Ch1 bandit-lair resilience. Shadow = Rogue/Swashbuckler infiltrator. Tunnel = dungeon escape artist. Deep = dungeon delver. Desert = overland speed. Snow = Ch6 Bloom cold zones.

---

### TENGU — Ability Boosts: +DEX, +CHA, free
```
[1] Dogtooth Tengu       — Beak unarmed attack gains deadly d8 trait (extra die on crits).
[2] Jinxed Tengu         — Crit-success on curse/misfortune saves; reduce doomed value received.
[3] Mountainkeeper Tengu — Cast *vitality lash* at will (primal or divine, your choice per cast).
[4] Skyborn Tengu        — Take no damage from falls of any distance.
[5] Stormtossed Tengu    — Electricity resist 1/2 level; auto-hit creatures concealed only by rain/fog.
[6] Taloned Tengu        — Talon unarmed attack (1d4 slashing, agile + finesse + versatile piercing).
[7] Wavediver Tengu      — Swim speed 15 ft.
```
**Best for:** Taloned / Dogtooth = Monk / Rogue natural-weapon builds. Mountainkeeper = Oracle / Cleric with primal-divine crossover. Jinxed = Swashbuckler (crit-denial). Stormtossed = Kineticist (air) / rain combat. Skyborn = Gunslinger (high-ground). Wavediver = river campaign.

---

## 🧬 KINGMAKER-ADDED ANCESTRY

### GOLIATH — Ability Boosts: +STR, +CON, free; flaw −DEX
*Source: Kingmaker-curated from Howl of the Wild + Travelers Anthology. **Not verified against Archives of Nethys** — DM should treat this block as authoritative for Kingmaker play. If the player cites a Paizo source that differs, accept their cite.*
```
[1] Cloud Goliath       — Slow fall: take half damage from falls; land upright.
[2] Cragborn Goliath    — Ignore difficult terrain from rocks, rubble, or loose stone.
[3] Great Goliath       — Access to Large-size Giant Instinct synergy feats; reach-weapon optimization.
[4] Soaring Goliath     — Glide 10 ft horizontally per 5 ft fallen; treat falls as 20 ft shorter.
[5] Stonemauler Goliath — Reduce the Hardness of inanimate objects by 2 when you Strike them.
[6] Sunbaked Goliath    — Fire resist 1/2 level; environmental heat one step less extreme.
[7] Thunderborn Goliath — Sonic resist 1/2 level.
```
**Best for:** Cragborn = Barbarian/Guardian frontline. Great = Giant Instinct (BUILD EXCEPTION in KM_AncestryGuide.md). Soaring = mobility-focused builds. Stonemauler = sundering/siege. Thunderborn = Bard/Kineticist counter.

---

## 📋 DM NOTES

**Heritage vs ancestry feat distinction.** Heritages apply automatically at L1 (no feat slot cost). Ancestry feats are taken at L1, 5, 9, 13, 17 and consume ancestry feat slots. SEPARATE: heritage is free, ancestry feats cost slots.

**Stacking.** Most heritage effects stack with ancestry feats of similar type (e.g., Forge Dwarf fire resist + a fire-resist ancestry feat compound). Two heritage-granted resistances of the same type do NOT stack — use the higher.

**Save block entry format:**
```json
"player": {
  "ancestry": "Elf",
  "heritage": "Ancient Elf",
  "heritage_source": "ancestry-specific",
  "heritage_granted_features": [
    "Multiclass Dedication Feat at L1 ignoring level prereq"
  ]
}
```
If versatile: `"heritage_source": "versatile"`.

**Heritage is locked at creation.** No retraining heritage mid-campaign. Ancestry/heritage change is a full rebuild event — see KM_Leveling.md retraining rules.

**Kingmaker setting note.** The Stolen Lands accept all ancestries. Brevoy-culture NPCs (Restov nobles, Aldori guards) react most familiarly to Human, Dromaar (Half-Orc), Dwarf, and Aiuvarin (Half-Elf). Rare ancestries draw curious looks in noble courts and warm greetings in wilderness hexes. No mechanical penalty — flavor only.

**If a player picks an ancestry not listed in EITHER heritage file:** accept it, ask them to cite a Paizo source. Load that source's heritage list and let them pick. Do NOT invent a heritage. `.fail 9` for any fabricated heritage effect.

**⛔ DM: For RARE ancestries (Kobold, Catfolk, Lizardfolk, Shoony, Fetchling, Strix, Conrasu, Nagaji, Vanara, Azarketi, Kashrishi, Fleshwarp, Ghoran, Goloma) AND for VERSATILE HERITAGES (Nephilim, Changeling, Dhampir, Duskwalker, Beastkin, Aiuvarin, Dromaar): SEE `KM_Heritages_B.md`.**

---

*KM_Heritages.md — Kingmaker PF2e Text Adventure | Heritage Catalog Part 1 (Core + Uncommon + Goliath)*
*12 ancestries | Continues in KM_Heritages_B.md*
