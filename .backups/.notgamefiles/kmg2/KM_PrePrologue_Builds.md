# KINGMAKER — PRE-PROLOGUE: BUILD SUBSTITUTION TABLE
## KM_PrePrologue_Builds.md | Referenced by: KM_PrePrologue.md

---

> **⛔ DM — BEFORE READING THIS FILE:** Check `tutorial_pickpocket_resolved` in the save block. If it equals `""` AND `current_scene` equals `"restov_gate"` → load `KM_PrePrologue_NPCs.md` and run **§ TUTORIAL BATTLE** NOW, before any narration, before any armor lookup, before Malak. This file is always loaded for the gate scene — this check fires on EVERY entry path.

---

> **DM:** Load alongside `KM_PrePrologue.md`. Look up the player's build ID in the tables below and fill every bracketed variable. For `[Weapon description]` and `[distinguishing feature]`, use the primary weapon's ⚗️ Exotic Materials entry from `KM_Exploration.md`. Do not fabricate any value not listed here.

---

## 📋 NARRATION BRACKET REFERENCE

```
[Ancestry] [Class] — [Subclass/Archetype]
[primary weapon]
[secondary weapon or tool]
[Weapon description] — [primary weapon] with [distinguishing feature]
[Physical scars or marks] / [body locations]
[Environmental wear]
[location on person]
[search description]   ← what the riders asked about at waystations
[armor description]    ← Malak's line: "[primary weapon], [armor description], that dead-man stare"
```

**Armor appearance:** Use the ⚗️ Exotic Materials column in `KM_Exploration.md`. Do not add armor flavor beyond what that table provides.

---

## ⚠️ ANCESTRY WEAPON SUBSTITUTION RULE

If the player's ancestry does not match the row, check the primary weapon first. These are ancestry-locked — a non-matching ancestry cannot use them:
- **Dwarven Waraxe** — Dwarf only → **Battleaxe**
- **Gnome Flickmace** — Gnome only → **Morningstar**
- **Elven Curve Blade** — Elf/Aelfborn only → **Bastard Sword**
- **Orc Necksplitter** — Orc/Half-Orc only → **Falchion**

Check other rows in the same category for an ancestry match first. Use the substitution above only if none exists. Always update the search description to name the correct weapon and ancestry.

---

## 🗣️ MALAK DIALOGUE VARIABLES

> *"Halt, stranger. Hands clear of that **[primary weapon]** and **[secondary weapon/tool]**."*

Fill from the same row. Rest of Malak's dialogue is fixed — do not alter it.

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 1: DEFENDER / TANK

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 1-01 | Dwarf Guardian — Disruption | Dwarven Waraxe | Tower Shield | Deep gouges / forearms and jaw | Trail dust | inside the breastplate, against the chest | a dwarf in armor that looked like nothing anyone had seen before | silver-white plate that catches light wrong |
| 1-02 | Human Champion — Bastion | Longsword | Steel Shield | Old blade scars / forearms and neck | Travel dust | inside the breastplate, over the heart | a human in silver-white plate with a longsword and a holy symbol | silver-white plate impossibly light for its size |
| 1-03 | Human Fighter — Shield Wall | Longsword | Steel Shield | Lance scars / left shoulder and collarbone | Campaign dust | inside the armor, at the chest | a human in blue-black scale mail with a longsword and a shield that looked bolted there | blue-black scale with seams too precise for any living hand |
| 1-04 | Human Monk — Mountain Stance | Fists | Handwraps | Knuckle callus and joint scars / hands, elbows, and shins | Sweat and road dust | tucked inside the outfit at the chest | a human in shadow-dark training clothes moving with uncomfortable precision | near-weightless black training clothes that dim nearby light |
| 1-05 | Orc Barbarian — Shield Rage | Orc Necksplitter | Steel Shield | Brand scars and deep gash lines / arms, chest, and jaw | Sweat and dirt | under the shield's inner strap | an orc in pitch-black scale mail carrying a blade and shield like the shield was part of the weapon | pitch-black scale armor that absorbs light at the surface |
| 1-06 | Human Champion — Redeemer | Longsword | Steel Shield | Old blade scars / forearms and neck | Travel dust | inside the breastplate, over the heart | a human in silver-white plate with a longsword and something in their face that made NPCs step back | silver-white plate impossibly light for its size |
| 1-07 | Human Thaumaturge — Regalia | Warhammer | Steel Shield | Ritual marks / right forearm and sternum | Road dust | inside the armor at the chest | a human in blue-black scale mail carrying a warhammer and something carved at their belt | blue-black scale armor with tolerances no human hand achieves |
| 1-08 | Gnome Inventor — Armor | Gnome Flickmace | Gadget Bandolier | Burn marks and tool scars / hands and forearms | Metal filings and oil | inside the construct armor's chest panel | a gnome in armor that moved on its own and smelled of something burning | self-built construct plate with glowing joints, no smith's mark |
| 1-09 | Human Monk — Wrestler | Fists | Handwraps | Grapple callus and mat burns / hands, wrists, and neck | Sweat and road dust | tucked inside the outfit at the chest | a human in shadow-dark training clothes whose hands made people uncomfortable | near-weightless black training clothes that dim nearby light |
| 1-10 | Human Champion — Reclaimant | Longsword | Steel Shield | Divine-burn marks / right hand and sternum | Incense ash | inside the breastplate, over the heart | a human in silver-white plate carrying a longsword that glowed faintly in the wrong places | silver-white plate, radiant at the edges, rings like a struck bell |
| 1-11 | Human Guardian — Provoke | Adamantine Warhammer | Vorgrim Shield | Campaign scars / left shoulder and jaw | Campaign dust | inside the breastplate, against the chest | a human in blood-red plate with a black warhammer who parted the road | blood-red plate with black accents, dragon-hide texture |

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 2: STRIKER / DPS

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 2-01 | Human Fighter — Two-Handed | Greatsword | Signal Whistle | Old campaign scars / left shoulder and hip | Campaign dust | inside the armor, strapped to the chest | a human with a greatsword in blue-black scale mail who hit like the weapon knew the fight | blue-black scale with seams too precise for any living hand |
| 2-02 | Elf Magus — Starlit Span | Elven Curve Blade | Spell Component Pouch | Fine blade scars / hands and forearms | Arcane residue | flat into the inner jacket lining | an elf in shadow-dark leather carrying a curve blade who kept appearing in the wrong place | near-weightless black leather that dims nearby light |
| 2-03 | Human Ranger — Flurry | Shortbow | Shortsword | Old animal-track scars / forearms and shins | Trail dust and leaf litter | inside the quiver's inner band | a human in pale leather carrying a shortbow who moved through crowds like they weren't there | pale grey iridescent leather, supple as cloth |
| 2-04 | Human Barbarian — Tactical Reach King (Giant Instinct) | Guisarme | Adventurer's Pack (worn) | Old polearm-haft callus and deep blade-wound scars / hands, forearms, chest, and jaw | Road dust and dried sweat under the plate joints | strapped flat against the chest beneath the breastplate | a human in blood-red plate carrying a long-hafted polearm with a hooked head, walking like the road owed him space | blood-red plate with black accents, dragon-hide texture, impossibly fitted at the joints |
| 2-05 | Human Gunslinger — Pistolero | Dueling Pistol | Leather Bandolier | Powder-burn scars / right hand and forearm | Ash and black powder | in the bandolier's inner pouch | a human carrying a pistol with a barrel that doesn't oxidize and eyes that tracked everyone | dark leather with iridescent shimmer, faintly smelling of ash |
| 2-06 | Human Swashbuckler — Fencer | Rapier | Signal Whistle | Tumble scrapes and old duel scores / arms and left cheekbone | Road chalk dust | tucked into the belt, beneath the blade | a human in pale grey leather with a rapier who moved through a crowd like a current | pale grey iridescent leather, supple as cloth |
| 2-07 | Human Thaumaturge — Weapon | Bastard Sword | Esoterica Pouch | Old gladiatorial scar lines / torso and right arm | Arena dust | under the breastplate's inner strap | a human in blue-black scale carrying a bastard sword who seemed to know something about everyone they looked at | blue-black scale armor with tolerances no human hand achieves |
| 2-08 | Human Fighter — Crit Hybrid | Falchion | Spell Component Pouch | Old crit wounds / forearms and right shoulder | Arena dust and arcane residue | inside the armor, at the sternum | a human in blue-black scale with a crescent blade who made every hit feel like a right guess | blue-black scale with seams too precise for any living hand |
| 2-09 | Halfling Rogue — Thief | Shortsword | Thieves' Tools | Old knife scores / ribs and left palm | Street grime | slipped into the inner jacket lining | a halfling in pale grey leather with a short blade moving like they knew where the guards weren't | pale grey leather that catches light with an iridescent shimmer |
| 2-10 | Talos Gunslinger — Sniper | Arquebus | Leather Bandolier | Powder-burn scars / right hand and forearm | Ash and black powder | in the bandolier's inner pouch | something with horns carrying an arquebus that made the air feel smaller | dark leather with iridescent shimmer, faintly smelling of ash |
| 2-11 | Human Fighter — Dual Slice (Pick) | Pick | Light Pick | Campaign scars / left shoulder and jaw | Road dust | inside the breastplate, against the chest | a human in blood-red plate carrying two picks who parted the road | blood-red plate with black accents, dragon-hide texture |

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 3: BLASTER

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 3-01 | Elf Wizard — Evoker | Staff | Spellbook | Burn scars / both hands and left forearm | Scorch residue | folded inside the robe's inner pocket | an elf in dark robes with a staff that smells of lightning | near-weightless black robes, warm regardless of weather |
| 3-02 | Human Sorcerer — Elemental | Dagger | Elemental Focus Crystal | Burn scars and elemental-touch marks / forearms and neck | Ozone and heat shimmer | pressed between layers of the inner coat | a human in pale leather who made the air change when they breathed | pale grey leather with warmth and cold cycling at its surface |
| 3-03 | Dwarf Kineticist — Fire/Earth | (Elemental Blast — no weapon drawn) | Leather (worn under stone shell) | Fire-kiss scars and stone-chip marks / forearms and knuckles | Ash and underground grit | wrapped inside the outer stone-shell | a dwarf in armor that looked like hardened lava | dark plate with a surface like compressed stone, warm to the touch |
| 3-04 | Gnome Witch — Winter/Cackle | Staff | Familiar (perched) | Hex-burn marks / fingers and temples | Frost residue and candle wax | folded into the front robe pocket | a gnome in pale leather with something on their shoulder that watched you back and left frost on the stones | pale grey leather that catches light with an iridescent shimmer, cold to touch |
| 3-05 | Human Oracle — Animist | Staff | Healer's Satchel | Spirit-mark traces / temples and sternum | Ash and herb dust | inside the hide armor's inner band | a human in dark hide carrying a staff that glowed faintly without a source | dark hide armor, faintly warm regardless of weather |
| 3-06 | Human Thaumaturge — Elemental | Sling | Void-glass Lantern | Burn marks and elemental-touch scars / right hand and forearm | Ozone residue | in the lantern's inner casing | a human in pale leather carrying a lantern that showed things in the wrong kind of light | pale grey iridescent leather, supple as cloth |
| 3-07 | Human Druid — Storm | Staff | Druidic Focus | Old lightning-touch and thorn scars / arms and collarbone | Leaf litter and ozone | tucked into the hide armor's inner band | a human in hide armor carrying a staff that smells of rain before it rains | dark hide armor, faintly warm regardless of weather |
| 3-08 | Human Psychic — Oscillating Wave | Dagger | Focus Wand | Psi-burn traces / temples and neck | Heat shimmer and frost residue | pressed between layers of the inner coat | a human in pale grey leather who made the air change temperature | pale grey leather with warmth and cold cycling at its surface |
| 3-09 | Human Sorcerer — Dragon | Dagger | Dragon-bone Focus Staff | Scale-marks and burn scars / forearms and neck | Ozone and heat | pressed between layers of the inner coat | a human in pale leather who made NPCs feel watched by something larger | pale grey iridescent leather, warm regardless of weather |
| 3-10 | Human Wizard — Elements | Staff | Spellbook | Elemental-touch scars / both hands and forearms | Scorch and frost residue | folded inside the robe's inner pocket | a human in dark robes with a staff that flickered the wrong color depending on the light | near-weightless black robes, warm regardless of weather |

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 4: CONTROLLER

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 4-01 | Elf Wizard — Illusion | Staff | Spellbook | Fine old cut lines / hands and left cheekbone | City dust and arcane residue | folded inside the robe's inner pocket | an elf in dark robes with a staff who was never quite where they appeared to be | near-weightless black robes, texture shifting by angle |
| 4-02 | Halfling Bard — Maestro | Rapier | Instrument Case | Tumble scrapes / arms and face | Road chalk dust | tucked into the belt, beneath the blade | a halfling in pale grey leather with a rapier and an instrument that made NPCs stand straighter | pale grey iridescent leather, supple as cloth |
| 4-03 | Human Wizard — Universalist | Staff | Spellbook | Fine old burn and cut lines / hands and forearms | Arcane residue | folded inside the robe's inner pocket | a human in dark robes with a staff and too many prepared answers | near-weightless black robes, warm regardless of weather |
| 4-04 | Human Druid — Plant | Staff | Druidic Focus | Old thorn marks / arms and collarbone | Leaf litter and bark dust | tucked into the hide armor's inner band | a human in hide armor carrying a staff that had moss growing on it | dark hide armor, faintly warm, smells of earth |
| 4-05 | Human Oracle — Battle | Longsword | Steel Shield | Divine-burn marks / right hand and sternum | Incense ash | strapped inside the scale mail | a human in silver-white scale with a longsword and a glow that came and went | silver-white scale, impossibly light, rings like a struck bell |
| 4-06 | Human Bard/Marshal — Fear | Longsword | Campaign Banner | Old lance scars / left shoulder and collarbone | Campaign dust | inside the armor, strapped to the chest | a human with a longsword in blue-black scale who made allies fight better and enemies fight worse | blue-black scale with seams too precise for any living hand |
| 4-07 | Human Monk — Wrestler | Fists | Handwraps | Grapple callus and mat burns / hands, wrists, and neck | Sweat and road dust | tucked inside the outfit at the chest | a human in shadow-dark training clothes who looked at everyone's center of gravity first | near-weightless black training clothes that dim nearby light |
| 4-08 | Human Psychic — Subconscious | Dagger | Psi Crystal | Psi-burn traces / temples and neck | City dust | pressed between layers of the inner coat | a human in shadow-dark leather who was never where they were a moment ago and never spoke | near-weightless black leather, texture shifting by angle |
| 4-09 | Human Thaumaturge — Tome/Bell | Rapier | Ancient Tome | Fine old scars / hands and one forearm | Ink and arcane residue | flat into the inner jacket lining | a human in pale leather with a rapier and a book that knew something about everyone in the room | pale grey iridescent leather, supple as cloth |
| 4-10 | Human Summoner — Controller | Dagger | Phantom Bond Crystal | Eidolon-merge bruising / forearms and collarbone | Ectoplasm residue | inside the robe, over the heart | a human in pale leather accompanied by something that wasn't quite there | pale grey iridescent leather, faintly glowing at the seams |

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 5: SUPPORT / BUFFER

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 5-01 | Human Commander — Tactics | Longsword | Folio of Tactics | Campaign scars / left shoulder and collarbone | Campaign dust | inside the armor, strapped to the chest | a human in blue-black scale with a longsword and a folder that made people around them move differently | blue-black scale with seams too precise for any living hand |
| 5-02 | Halfling Bard — Inspire | Rapier | Instrument Case | Tumble scrapes / arms and face | Road chalk dust | tucked into the belt, beneath the blade | a halfling in pale grey leather with a rapier and an instrument that made NPCs fight harder without knowing why | pale grey iridescent leather, supple as cloth |
| 5-03 | Human Bard — Warrior Muse | Bastard Sword | Instrument (worn at back) | Old campaign scars / left shoulder and hip | Campaign dust | inside the armor, strapped to the chest | a human in blue-black scale carrying a blade who sang before every fight | blue-black scale with seams too precise for any living hand |
| 5-04 | Human Fighter — Propagandist | Halberd | Campaign Banner | Old lance scars / left shoulder and hip | Campaign dust | inside the armor, strapped to the chest | a human with a halberd in blue-black scale who made everyone around them louder | blue-black scale with seams too precise for any living hand |
| 5-05 | Human Fighter — Captain | Longsword | Steel Shield | Old campaign scars / left shoulder and collarbone | Campaign dust | inside the armor, strapped to the chest | a human in blue-black scale with a longsword who made NPCs stand straighter | blue-black scale with seams too precise for any living hand |
| 5-06 | Human Bard — Songblade | Greatsword | Instrument (worn at back) | Old campaign scars / left shoulder and hip | Campaign dust | inside the armor, strapped to the chest | a human with a greatsword who hummed before swinging it | blue-black scale with seams too precise for any living hand |
| 5-07 | Human Fighter — Marshal | Longsword | Campaign Banner | Old lance scars / left shoulder and collarbone | Campaign dust | inside the armor, strapped to the chest | a human in blue-black scale with a longsword and a banner that made people adjust their footing | blue-black scale with seams too precise for any living hand |
| 5-08 | Human Bard — Enchanter | Dagger | Focus Staff | Fine old cut lines / hands and left cheekbone | City dust | pressed between layers of the inner coat | a human in pale leather who made NPCs cooperative without appearing to try | pale grey iridescent leather, supple as cloth |
| 5-09 | Human Psychic — Buffer | Dagger | Psi Crystal | Psi-burn traces / temples | City dust | pressed between layers of the inner coat | a human in pale leather who made the people around them faster | pale grey leather with warmth cycling at its surface |
| 5-10 | Human Swashbuckler — Marshal | Rapier | Campaign Banner | Tumble scrapes and old duel scores / arms and cheekbone | Road chalk dust | tucked into the belt, beneath the blade | a human in pale grey leather with a rapier and a banner who moved like the fight had started | pale grey iridescent leather, supple as cloth |

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 6: HEALER

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 6-01 | Human Cleric — Warpriest | Flail | Steel Shield | Ritual brands / shoulders and sternum | Road mud | tucked into the shield strap | a human in blue-black scale mail carrying a flail and a holy symbol | blue-black scale armor with tolerances no human hand achieves |
| 6-02 | Human Oracle — Life | Staff | Healer's Satchel | Spirit-mark traces / temples and sternum | Herb dust and candlewax | inside the leather's inner band | a human in dark leather carrying a staff that glowed when someone nearby was hurt | dark leather, faintly warm regardless of weather |
| 6-03 | Human Druid — Leaf | Staff | Healer's Tools | Old thorn marks / arms and collarbone | Leaf litter and antiseptic | tucked into the hide armor's inner band | a human in hide armor carrying a staff that grew new leaves every morning | dark hide armor, bark-textured at the shoulders |
| 6-04 | Gnome Alchemist — Chirurgeon | Dagger | Gnome-engineered Bandolier | Tool scars and chemical burns / hands and forearms | Alchemical residue and herbs | inside the bandolier's inner pouch | a gnome in pale leather with a bandolier of labeled vials who moved through injured people like they had a map | pale grey iridescent leather, faint chemical smell |
| 6-05 | Human Kineticist — Water | (Water Blast — no weapon drawn) | Herbalism Kit | Water-mark traces / forearms and palms | Perpetual dampness at the cuffs | wrapped inside the herbalism kit | a human in dark leather who smelled of rain and left the ground dry when they bled | dark leather, cool to touch at the edges |
| 6-06 | Human Oracle — Battle/Champion | Longsword | Steel Shield | Divine-burn marks / right hand and sternum | Incense ash | strapped inside the scale mail | a human in blue-black scale with a longsword who healed allies without looking away from the fight | blue-black scale armor with tolerances no human hand achieves |
| 6-07 | Human Cleric — Necrologist | Scythe | Holy Symbol (skull-marked) | Ritual brands and bone-mark traces / shoulders and sternum | Grave dust | tucked into the scythe's wrapping | a human in dark scale mail carrying a scythe and a symbol that made NPCs look away | dark scale armor, cold to touch regardless of weather |
| 6-08 | Human Fighter — Blessed One | Longsword | Steel Shield | Old campaign scars / left shoulder and right hand | Campaign dust | inside the armor, strapped to the chest | a human in blue-black scale with a longsword whose hands glowed faintly when they touched someone injured | blue-black scale with seams too precise for any living hand |
| 6-09 | Gnome Witch — Life Patron | Staff | Familiar (perched) | Hex-burn marks / fingers and temples | Herb dust and warm light residue | folded into the front robe pocket | a gnome in pale leather with something on their shoulder that watched injured people with specific interest | pale grey leather that catches light with an iridescent warm shimmer |
| 6-10 | Human Sorcerer — Medic | Dagger | Healer's Satchel | Old bloodline marks / forearms and sternum | Herb dust and road grime | pressed between layers of the inner coat | a human in pale leather who carried a satchel and made people feel better by standing near them | pale grey iridescent leather, faintly warm |

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 7: SCOUT / SKILL MONKEY

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 7-01 | Human Rogue — Mastermind | Rapier | Investigator's Notebook | Fine old cut lines / hands and left cheekbone | City dust | flat into the inner jacket lining | a human in shadow-dark leather carrying a rapier and notebooks who seemed to already know your name | near-weightless black leather that dims nearby light |
| 7-02 | Human Ranger — Precision | Longbow | Shortsword | Old animal-track scars / forearms and shins | Trail dust and leaf litter | inside the quiver's inner band | a human in pale leather with a longbow who looked at everyone like they were the prey | pale grey iridescent leather, supple as cloth |
| 7-03 | Halfling Rogue — Thief Scout | Shortsword | Thieves' Tools | Old knife scores / ribs and left palm | Street grime | slipped into the inner jacket lining | a halfling in pale grey leather with a short blade who moved like they knew where the traps were | pale grey leather that catches light with an iridescent shimmer |
| 7-04 | Elf Investigator — Empiricist | Rapier | Investigator's Notebook | Fine old cut lines / hands and left cheekbone | City dust | flat into the inner jacket lining | an elf in shadow-dark leather carrying a rapier and too many notebooks | near-weightless black leather that dims nearby light |
| 7-05 | Human Fighter — Infiltrator | Hand Crossbow | Shortsword | Old scar lines from bolts / forearms and right shoulder | Crossbow oil and road grime | inside the leather's inner strap | a human in dark leather with a hand crossbow who was always in a position they hadn't appeared to move to | dark leather with iridescent shimmer, matte finish |
| 7-06 | Halfling Rogue — Acrobat | Shortsword | Thieves' Tools | Old tumble scars / forearms and knees | Street grime and chalk | slipped into the inner jacket lining | a halfling in pale grey leather with a short blade who used the walls as much as the floor | pale grey leather that catches light with an iridescent shimmer |
| 7-07 | Human Ranger — Scout | Shortbow | Shortsword | Old animal-track scars / forearms and shins | Trail dust and leaf litter | inside the quiver's inner band | a human in pale leather with a shortbow who arrived at places before anyone knew they'd left | pale grey iridescent leather, supple as cloth |
| 7-08 | Human Swashbuckler — Gymnast | Rapier | Signal Whistle | Tumble scrapes and old duel scores / arms and left cheekbone | Road chalk dust | tucked into the belt, beneath the blade | a human in pale grey leather with a rapier who moved through a crowd and ended up somewhere else | pale grey iridescent leather, supple as cloth |
| 7-09 | Elf Rogue — Shadowdancer | Rapier | Dagger (off-hand) | Fine old cut lines / hands and left cheekbone | Shadow-residue and city dust | flat into the inner jacket lining | an elf in shadow-dark leather with a rapier who was harder to see in dim light than in dark | near-weightless black leather that dims nearby light |
| 7-10 | Gnome Kineticist — Air/Wood | (Elemental Blast — no weapon drawn) | Herbalism Kit | Nature-mark traces / forearms and palms | Perpetual leaf litter | wrapped inside the herbalism kit | a gnome in dark leather who moved faster than gnomes moved and left plants pointing the wrong direction | dark leather, rustles faintly without wind |

---


## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 8: FACE / SOCIAL

> **See `KM_PrePrologue_Builds_B.md`.**

---

*KM_PrePrologue_Builds.md — Kingmaker PF2e | Pre-Prologue Build Table v1.0*
