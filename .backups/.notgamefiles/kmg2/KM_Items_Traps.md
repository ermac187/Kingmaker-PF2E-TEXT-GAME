# KINGMAKER — TRAPS CATALOG
## KM_Items_Traps.md | Mundane Traps, Mechanical Hazards, Magical Traps, Snares

> **DM:** Load when the scene contains a trap, the player attempts Disable Device / Craft a Snare / set an ambush, or a dungeon room contains hazards. All traps follow PF2e hazard rules: Stealth DC to notice, Disable DC to remove, trigger conditions, effect on failure.
>
> **Related:** KM_Loot_Items_Ref.md § SPECIALIST COMBAT TOOLS · KM_DungeonPuzzles.md · KM_Actions.md · KM_Crafting.md

---

## 🪤 HOW TRAPS WORK (Quick Reference)

```
┌──────────────────────────────────────────────────────────┐
│ 4 STATS DEFINE EVERY TRAP:                                │
│   1. Stealth DC  — Perception check to notice unsprung    │
│   2. Disable DC  — Thievery (mundane) or Arcana (magical) │
│   3. Trigger     — what sets it off (step, weight, touch) │
│   4. Effect      — damage/condition; save DC & type       │
└──────────────────────────────────────────────────────────┘

DETECTION:
 · Passive Perception (walking through) vs Stealth DC = pass by safely
 · Active Search (1 min) grants +2 circ. to Perception
 · Trap-Spotter's Candle / Detect Anathema Censer / Detect Magic reveal
   within their range; see KM_Items_Expanded.md § Detection

DISABLE:
 · Thievery (mechanical traps)
 · Arcana / Occultism / Nature (magical traps — match tradition)
 · Crafting (complex mechanisms)
 · Critical success = disabled, reusable (if salvageable)
 · Success = disabled
 · Failure = trap still armed
 · Critical failure = trap triggers immediately on you

DEPLOY (player-set trap):
 · Crafting check (Snare) OR Thievery (mechanical) OR spell (magical)
 · Uses trap components from this file
 · Deploy time: 1 min basic, 10 min complex, 1 hour elaborate
 · Limited uses per day: (trained 4) / (expert 6) / (master 8) / (legendary 10)

SALVAGE:
 · Critical success on Disable → recover 50% component cost (round down)
 · Magical traps never salvaged (spell is expended)
```

---

## 🪤 MUNDANE TRAPS — ENCOUNTERED (found in dungeons, ruins, fort traps)

### Level 1 Traps

| Trap | Stealth DC | Disable DC | Trigger | Effect |
|------|-----------|-----------|---------|--------|
| **Hidden Pit (Shallow)** | 18 | 17 (Thievery/Athletics) | Step on false floor | 1d6 B fall; Ref DC 17 or fall into 10-ft pit |
| **Tripwire + Bell** | 20 (Perception) | 15 | Cross wire | No damage; alarm sounds 60 ft; +8 initiative for guards |
| **Caltrop Trap (Scattered)** | 16 | 12 | Walk into square | 1 piercing + 1d4 per sq moved; DC 15 Acrobatics or Slowed 1 |
| **Swinging Log (Passage)** | 19 | 17 | Pressure plate mid-corridor | 2d6 B; Ref DC 17 or Knocked Prone + 5 ft shove |
| **Poison Dart (Wall)** | 21 (hidden seam) | 18 | Wire stretch | Dart: +8 atk, 1d4 P + Black Adder Venom (Fort DC 14) |
| **Deadfall (Loose Stones)** | 17 | 16 (Thievery/Crafting) | Step on rigged stone | 2d6 B on 1 sq; Ref DC 16 half; Knocked Prone on fail |
| **Snare Loop (Foot)** | 18 | 14 | Step in | Immobilized; Athletics DC 16 or Acrobatics DC 18 to Escape |
| **Spike Board (Stepped)** | 15 | — (visible, avoid) | Step on | 1d6 P; DC 14 Fort or persistent 1d4 bleed (infected) |

### Level 3 Traps

| Trap | Stealth DC | Disable DC | Trigger | Effect |
|------|-----------|-----------|---------|--------|
| **Pit Trap (Deep)** | 19 | 19 | False floor | 3d6 B; 30-ft drop; Ref DC 19 or fall |
| **Spiked Pit** | 19 | 19 | False floor | 3d6 B fall + 2d6 P from spikes; Ref DC 19 |
| **Dart Volley (Ceiling)** | 22 | 20 | Pressure plate | 3 darts, +10 atk each, 1d4+2 P each |
| **Crossbow Trap (Wall)** | 21 | 19 | Tripwire | +11 atk, 1d8+3 P; range 60 ft |
| **Gas Jet (Poison Smoke)** | 22 | 20 | Tile pressure | 15-ft cone, Fort DC 18 or Sickened 2 + Slowed 1 for 1 min |
| **Collapsing Ceiling (Section)** | 20 | 22 (Crafting) | Trigger plate | 4d6 B in 10x10 area; Ref DC 20 half; difficult terrain after |
| **Rolling Boulder** | 22 | 21 | Weight trigger | 5d6 B in 5-ft corridor; Ref DC 20 flat half; must Stride 25 ft to escape |
| **Arrow Slit Volley** | 19 | 18 | Guard pull | 4 arrows, +9 atk, 1d6+2 P each; from murder hole |

### Level 5 Traps

| Trap | Stealth DC | Disable DC | Trigger | Effect |
|------|-----------|-----------|---------|--------|
| **Scything Blade (Floor Slot)** | 23 | 22 | Plate trigger | +14 atk, 2d12 S; Reach 10 ft; may Strike 3 consecutive targets |
| **Falling Portcullis** | 22 | 23 (Crafting) | Mid-room pressure | 3d8 B Knocked Prone + 5-ft sq separation; Hardness 12 HP 60 |
| **Flame Jet Array** | 24 | 22 | Stepping stone | 4d6 fire 10-ft burst; Ref DC 22 half; persistent 1d6 fire on crit fail |
| **Spiked Pit (Poisoned)** | 22 | 21 | False floor | 4d6 B + 3d6 P + Spider Venom (Fort DC 20) |
| **Cave-In (Triggered)** | 23 | 24 | Vibration/noise | 6d6 B in 15-ft radius; Ref DC 22 half; Buried (see KM_EnvironmentalCombat.md) |
| **Whirling Razor-Wire** | 23 | 21 | Step through archway | 3d6 S; persistent 1d4 bleed; difficult terrain 5 ft around |
| **Sticky Resin Floor** | 24 (smell) | 20 (solvent) | Step on | Immobilized; Athletics DC 22 Escape; 5-ft sq affected per dose |

### Level 7+ Traps (dungeon boss rooms)

| Trap | Level | Stealth DC | Disable DC | Effect |
|------|-------|-----------|-----------|--------|
| **Rigged Collapse Corridor** | 7 | 26 | 26 | 8d6 B corridor-wide; Ref DC 24 half; blocks passage 1 hr to clear |
| **Giant Swinging Axe** | 7 | 25 | 24 | +18 atk, 3d12 S; range 10-ft arc; 2 strikes per round |
| **Twin Blade Floor (Maze)** | 9 | 28 | 27 | +20 atk, 4d10 S; activates every 3 rounds moving through |
| **Murder Hole Battery** | 9 | 26 | 25 | 4× crossbow bolts +17 atk, 2d8 P; boiling oil option 4d6 fire |
| **Vault Gas (Lethal)** | 10 | 28 | 26 | Fort DC 26 or Drained 2 + Unconscious 10 min; Dragon Bile poison ticks |
| **Dragon-Wire Room** | 11 | 29 | 28 | Whole 20-ft room trigger; 6d8 S + persistent 2d6 bleed; Ref DC 27 half |

---

## 🪄 MAGICAL TRAPS — ENCOUNTERED

### Level 1–3 Magical Traps

| Trap | Level | Stealth DC | Disable DC (Arcana/Occ/Nat) | Effect |
|------|-------|-----------|----------------------------|--------|
| **Glyph of Warding (Minor)** | 1 | 18 (Detect Magic) | 17 | On trigger: 2d6 force; Ref DC 17 half; single-use |
| **Alarm Rune** | 2 | 19 | 17 | Silent telepathic alarm to caster within 1 mile; no damage |
| **Flaming Sphere Sigil** | 3 | 20 | 19 | Summon Flaming Sphere (2d6 fire) rolls toward nearest creature; 1 min |
| **Magic Missile Glyph** | 3 | 20 | 19 | 3× Magic Missiles (1d4+1 force each) at triggerer |
| **Web Runes (Floor)** | 3 | 20 | 18 | 10-ft burst Web; Ref DC 19 Immobilized; 5 min |
| **Fear Ward (Threshold)** | 3 | 20 | 18 | Will DC 19 or Frightened 2 + Fleeing 1 rnd |

### Level 4–6 Magical Traps

| Trap | Level | Stealth DC | Disable DC | Effect |
|------|-------|-----------|-----------|--------|
| **Fireball Glyph** | 5 | 23 | 22 | 6d6 fire 20-ft burst; Ref DC 22 half |
| **Phantasmal Killer Sigil** | 6 | 24 | 23 | Will DC 24 or 8d6 mental + Frightened 2; crit fail = die |
| **Lightning Bolt Rune** | 5 | 22 | 22 | 6d12 electricity in 60-ft line; Ref DC 22 half |
| **Hold Person Ward** | 5 | 22 | 21 | Will DC 22 or Paralyzed 1 min (rerolls each rnd) |
| **Stinking Cloud Pit** | 4 | 22 | 20 | 20-ft burst fog; Fort DC 20 or Sickened 2 + Slowed 1 |
| **Summon Elemental Glyph** | 6 | 24 | 22 | Summon CR 4 elemental hostile to triggerer; 10 rnd |

### Level 7+ Magical Traps

| Trap | Level | Stealth DC | Disable DC | Effect |
|------|-------|-----------|-----------|--------|
| **Cloudkill Ward** | 9 | 27 | 26 | 20-ft burst poison cloud; Fort DC 26 or 6d8 poison + Sickened 3 |
| **Disintegrate Sigil** | 11 | 29 | 28 | Ref DC 28 or 12d10 force + target reduced to dust on crit fail |
| **Imprisonment Glyph** | 17 | 37 | 36 | Will DC 37 or target trapped in magical prison until counterspell |
| **Symbol of Insanity** | 13 | 32 | 31 | Will DC 31 or Confused 1 day; 60-ft radius; up to 6 creatures |
| **Soul-Rending Sigil** | 15 | 34 | 33 | Fort DC 33 or Drained 4 + 8d10 void damage; halves on success |

---

## 🏹 PLAYER-DEPLOYABLE SNARES (Ranger, Rogue, any with Snare Crafting)

> **How snares work:** A snare is a trap you Craft in 1 minute (or Prepare Snare for instant deploy). Crafting proficiency and Snare Crafter / Ubiquitous Snares feats affect how many you can prep per day. Snares are consumable — one use.
>
> **Preparation table** (PF2e standard):
> - Trained: 4 prepared snares/day
> - Expert: 6/day
> - Master: 8/day
> - Legendary: 10/day
>
> Feats (Ranger, Alchemist-with-Snares, Rogue-with-Snares) can increase these counts.

### Basic Snares (L1–L3)

| Snare | Level | Formula Cost | Trigger | Effect |
|-------|-------|-------------|---------|--------|
| **Caltrop Snare** | 1 | 3 gp | Step on 5-ft sq | 2d6 piercing; Acrobatics DC 17 or Slowed 1 |
| **Hampering Snare** | 1 | 3 gp | Step into | Immobilized; Athletics DC 17 Escape |
| **Hobbling Snare** | 1 | 3 gp | Step on | Speed reduced 10 ft for 1 min; Fort DC 17 negates |
| **Marking Snare** | 1 | 3 gp | Step | No damage; marks creature with dye (Stealth DC −4 until washed) |
| **Signaling Snare** | 1 | 3 gp | Trip | Loud noise audible 60 ft; no damage |
| **Spike Snare** | 1 | 3 gp | Step | 1d8 piercing + 1d4 persistent bleed; Fort DC 17 no bleed |
| **Warning Snare** | 1 | 3 gp | Step | Signal to you silently (telepathic-feel); lasts 24 hrs |
| **Alarm Snare** | 3 | 10 gp | Step | Caster-level Alarm spell; 20-ft radius, 8 hrs |
| **Bleeding Spines Snare** | 3 | 10 gp | Step | 3d6 P + 2d4 persistent bleed; Fort DC 19 half |
| **Briny Snare (anti-fey)** | 3 | 10 gp | Step | 2d6 force; fey take +1d6; Will DC 19 to resist Confused 1 |
| **Freezing Snare** | 3 | 10 gp | Step | 3d6 cold; Fort DC 19 or Slowed 1 for 1 min |
| **Hobbling Snare (Greater)** | 3 | 10 gp | Step | Speed reduced 15 ft for 10 min; Fort DC 19 negates |
| **Saltpeter Snare** | 3 | 10 gp | Step | 3d6 fire + 1d6 persistent fire; Ref DC 19 half |
| **Scorpion Snare** | 3 | 10 gp | Step | +9 atk, 1d8 P + scorpion venom (Fort DC 18) |
| **Trip Snare** | 3 | 10 gp | Trip | Athletics +11 to Trip; Knocked Prone; +2d6 B fall damage |

### Advanced Snares (L5–L9)

| Snare | Level | Cost | Effect |
|-------|-------|------|--------|
| **Biting Snare (Greater)** | 5 | 25 gp | Bite +14, 3d10 P; Immobilized until Escape DC 22 |
| **Hampering Spine Snare** | 5 | 25 gp | 4d6 P + Immobilized; Escape Athletics DC 22 |
| **Stalker Bane Snare** | 5 | 25 gp | Reveals creature using Stealth; they glow for 10 min |
| **Grasping Snare** | 6 | 40 gp | Athletics +15 to Grapple; Fort DC 22 or Restrained |
| **Grave-Chill Snare** | 7 | 60 gp | 4d6 cold + 2d6 void; Fort DC 23 or Drained 1 |
| **Oil-Slick Snare** | 7 | 60 gp | 20-ft burst; Acrobatics DC 23 or Prone; persistent fire if ignited |
| **Stunning Snare** | 7 | 60 gp | Fort DC 23 or Stunned 1 (1 rnd); +1 rnd on crit fail |
| **Dueling Snare** | 9 | 140 gp | Creature is locked in 5-ft square; may only target you (Will DC 26) |
| **Omnidirectional Snare** | 9 | 140 gp | Affects all creatures within 10 ft; Ref DC 26 or 6d10 P + prone |
| **Terrain Snare (Fey)** | 9 | 140 gp | 30-ft burst difficult terrain; fey take 4d6 cold iron damage |

### Magical / Specialty Snares (L10+)

| Snare | Level | Cost | Effect |
|-------|-------|------|--------|
| **Banishing Snare** | 10 | 200 gp | Outsiders: Will DC 27 or Banished to home plane for 1 min |
| **Bonding Snare** | 11 | 275 gp | Two creatures share damage taken for 1 min; Fort DC 28 negates |
| **Soul-Cage Snare** | 13 | 500 gp | Fort DC 31 or Paralyzed + spirit tethered (re-enter body = 1 action) |
| **Null-Magic Snare** | 15 | 1,000 gp | 20-ft burst Antimagic Zone for 1 min; Will DC 34 to walk through |
| **Petrifying Snare** | 17 | 3,000 gp | Fort DC 37 or Petrified (Slowed 1 → Paralyzed → Petrified over 3 rnd) |

---

## 🎯 TRAP COMPONENTS (Crafting Raw Materials)

> Raw components consumed when crafting snares / setting traps. Stocked by
> hunters, blacksmiths, alchemists. All tiers available at Capital Market Ch2+.

| Component | Use | Price |
|-----------|-----|-------|
| Trip Wire (50 ft spool) | Tripwire, alarm, snare linkage | 1 gp |
| Spring Mechanism (Small) | Dart, crossbow, snap traps | 2 gp |
| Spring Mechanism (Large) | Pit covers, log-swings | 5 gp |
| Pressure Plate (Wood) | Mounted trigger | 8 sp |
| Pressure Plate (Stone) | Concealed floor trigger | 3 gp |
| Trap Spikes (×10) | Pit trap, spike board | 5 sp |
| Iron Teeth (Jaw Trap) | Leg-hold trap; reuses as component | 2 gp |
| Poison Vial (Empty) | Coat darts/spikes | 2 sp |
| Dart (Barbed, ×10) | Ranged traps ammo | 1 gp |
| Bolt (Heavy, ×10) | Crossbow trap ammo | 4 sp |
| Alchemical Fuse (1 hour) | Delayed triggers | 1 gp |
| Alchemical Fuse (Instant) | Tripwire triggers | 1 sp |
| Glyph Ink (1 scroll's worth) | Magical sigil base | 15 gp |
| Runic Paper | Single-use glyph base | 3 gp |
| Binding Wax (1 lb) | Affixes scrolls/glyphs to surface | 1 gp |
| Cold Iron Nails (×20) | Fey-targeting traps | 4 sp |
| Silver Wire (per ft) | Lycanthrope/fiend traps | 5 sp |

---

## 🎯 PLAYER-DEPLOYABLE MECHANICAL TRAPS (non-snare, downtime-built)

> These are set during Exploration downtime (1 hour per trap), not combat. Useful for kingdom fortification, camping ambushes, and preparing known battlefields.

| Trap | Set Time | Cost | Disarm DC | Effect |
|------|---------|------|-----------|--------|
| **Trip Wire + Bell Alarm** | 10 min | 1 gp | 15 | Alarm only; 60-ft audible |
| **Concealed Caltrops** | 5 min | 3 sp | 12 | Caltrops field; same as mundane |
| **Leg-Hold Trap (Jaw)** | 10 min | 5 gp | 18 | 2d6 P; Immobilized; Escape Athletics DC 20 |
| **Spring-Dart (Wall-Mount)** | 30 min | 15 gp | 18 | +10 atk, 1d4+2 P; may coat with poison (buyer supplies) |
| **Pit Trap (5-ft Square)** | 1 hr | 5 gp | 16 | 1d6 B fall + 10-ft pit |
| **Spike Pit (5-ft)** | 2 hrs | 20 gp | 17 | 2d6 B + 2d6 P |
| **Falling Net** | 30 min | 10 gp | 17 | 10-ft sq; Ref DC 18 or Restrained; Escape DC 20 |
| **Log Deadfall** | 1 hr | 5 gp | 18 | 2d6 B in 5-ft sq; Knocked Prone on fail |
| **Crossbow Arbalest (Emplaced)** | 2 hrs | 30 gp | 19 | +12 atk, 2d8 P; range 80 ft; one-shot |
| **Gas Censer (Sleeping Smoke)** | 30 min + 1 alch component | 25 gp | 20 | 10-ft burst; Fort DC 20 or Unconscious 10 min |
| **Bear Trap (Heavy Jaw)** | 15 min | 10 gp | 20 | 2d8 P + Immobilized; Escape Athletics DC 22 |
| **Tar Pit (Sticky, Concealed)** | 2 hrs | 15 gp | 18 | 10-ft sq; Immobilized; Escape DC 20 |
| **Stone Pressure Mine** | 30 min + 50 gp powder | 50 gp | 22 | 4d6 B 15-ft burst; Ref DC 20 half |

**Deploy checks:**
- Thievery DC = trap disarm DC − 2 (deploy is easier than disarm)
- Crafting DC for alchemical/gas traps = same as disarm
- Set on a known path / choke point: +2 circ. to any Perception DC

**Kingdom-scale defenses:** Kingdom Turn can place permanent traps in fortified hexes at 1 BP per minor trap / 2 BP per major trap. See [KM_Kingdom.md](KM_Kingdom.md) § Defense spending.

---

## 🕷️ NYRISSA / FEY-THEMED TRAPS (Kingmaker-specific)

> Found in Thousandbreaths (Ch6), fey-blighted hexes, Bloom events, First World incursions. May be deployed by Nyrissa's agents against the player, or learned / captured for player use.

| Trap | Level | Effect | Disarm |
|------|-------|--------|--------|
| **Thorn Circle (Binding)** | 5 | 20-ft Wall of Thorns; Ref DC 22 or 4d4 P + Immobilized; 10 min | Arcana/Nature DC 22 |
| **Dreamroot Patch** | 6 | Step on 5-ft sq: Will DC 22 or Unconscious (prophetic dream) 10 min | Nature DC 22 |
| **Bloom-Bloom (Fruiting Spore)** | 7 | 30-ft cone on disturbance; Fort DC 23 or Poisoned + Confused 1 min | Nature DC 23 |
| **Nyrissa's Thorn Sigil** | 9 | On touch: Will DC 26 or compelled 1 rnd to speak Nyrissa's riddle | Occultism DC 26 |
| **First World Doorway (False)** | 10 | Step through: Will DC 27 or Banished to First World 1 min | Occultism DC 27 |
| **Heartbriar Circle (Protective)** | 11 | 20-ft radius ward; fey allies cannot leave; enemy fey take 4d6 cold iron | Nature DC 28 |
| **Whispering Mistfalls** | 13 | 60-ft radius fog; Will DC 30 or Stupefied 2 + hallucinating | Occultism DC 30 |

---

## 🪤 HAZARDS — ENVIRONMENTAL (not traps, but trap-adjacent)

> Terrain-based dangers. Not "set" — they exist. Documented here for DM
> reference when building encounters. Use alongside [KM_EnvironmentalCombat.md](KM_EnvironmentalCombat.md).

| Hazard | Effect | Save |
|--------|--------|------|
| Quicksand (Shallow) | Speed 5 ft; Athletics DC 15 or sink 1 ft/rnd | Fort ongoing |
| Quicksand (Deep) | Sink fully in 3 rnd; Athletics DC 20 to escape | Fort DC 20 |
| Acid Pool (Kingmaker swamps) | 2d6 acid/rnd in pool; persistent 1d6 after exit | Ref DC 17 |
| Thornwall (Dense) | Difficult terrain + 1d4 P per 5 ft moved | — |
| Mire (Troll Swamp) | Slowed 1; drops held items on 1-in-6 per rnd | Ref DC 16 |
| Bramble Maze (Bloom) | Difficult terrain + 1d4 P + Will DC 18 or lost | Will DC 18 |
| Bone Pile (Vordakai) | Slowed 1; 1d6 void when stepped on | Fort DC 20 |
| Cold Spring (Freezing) | 1d6 cold/rnd exposed; Fort DC 18 or Clumsy 1 | Fort DC 18 |
| Lava Vent (Rare) | 6d6 fire; persistent 2d6 fire | Ref DC 25 |
| Sinkhole (Sudden) | 4d6 B fall 20 ft; detected 1 rnd before | Ref DC 20 |

---

## 📋 DM NOTES

**Trap placement by chapter:**
- **Pre-Prologue / Prologue:** no mechanical traps (social tone); Malak's parchment is a "trap" in a narrative sense only
- **Ch1 Stolen Lands:** L1–3 traps in bandit camps (Kressle, Stag Lord fort); simple pits, dart traps, tripwire alarms
- **Ch2 Troll/Bloom:** L3–5 traps in troll caves; magical Bloom traps start appearing in fey-blighted hexes
- **Ch3 Varnhold:** L5–7 traps in Vordakai's tomb; ancient cyclopean mechanical + necromantic sigils
- **Ch4–5 Pitax/Armag:** L7–9 traps in palace + tomb; Irovetti's paranoid security (mundane heavy)
- **Ch6 Thousandbreaths:** L9–13 fey traps; Nyrissa's riddles encoded as ward sigils
- **Ch7 Finale:** L13+ soul-binding traps around Nyrissa's heart tree

**Player-deployable snares / mechanical traps as ROGUE/RANGER REWARD:**
- Ranger (Build 3, Sniper & Flurry variants): Snare Crafter at L4
- Alchemist: Can prep alchemical snares instead of bombs
- Rogue: Trap Finder feat (L1) reduces Stealth DC by 2 to find traps; Mechanical Expertise (L9) lets them set mechanical traps in half the time
- Rogue Thief: Treat Disarm as Master at L7

**Salvage rules:**
- Mechanical traps: 50% material cost recovered on crit success Disable
- Magical traps: cannot be salvaged; spell is expended regardless of outcome
- Snares: single-use; cannot recover unless feat explicitly allows (Stealthy Sniper feat, some Alchemist discoveries)

**Loot placement (found traps):**
- Bandit fort boss rooms: 2–3 minor traps at Ch1 tier
- Cyclops tomb boss rooms (Ch3): 4–6 magical + mechanical
- Pitax palace (Ch5): 3–4 high-tier mechanical, no magical (Pitax distrusts magic)
- Nyrissa's lair (Ch6+): 4–6 fey/magical traps scaling to L15

**Tone fit:** All traps here fit Kingmaker — no Numerian tech, no clockwork-city traps, no Alkenstar firearm artillery. Stolen Lands aesthetic: pit traps, deadfalls, fey compulsions, necromantic wards.

---

*KM_Items_Traps.md — Kingmaker PF2e Text Adventure | Traps Catalog v1.0*
*Source: PF2e GM Core, Player Core, Treasure Vault (Snares), Kingmaker AP (Paizo), Book of the Dead (magical traps)*
