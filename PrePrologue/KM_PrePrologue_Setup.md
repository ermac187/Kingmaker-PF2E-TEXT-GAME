# KINGMAKER — PRE-PROLOGUE: BUILD SUBSTITUTION TABLE
## KM_PrePrologue_Setup.md | Referenced by: KM_PrePrologue.md

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
| 3-07 | Human Druid — Leliana | Staff | Druidic Focus | Old lightning-touch and thorn scars / arms and collarbone | Leaf litter and ozone | tucked into the hide armor's inner band | a human in hide armor carrying a staff that smells of rain before it rains | dark hide armor, faintly warm regardless of weather |
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


---

## ⚗️ ARMOR APPEARANCE BY BUILD ID

| ID | Armor Type | Material | KM_Exploration.md Row |
|----|-----------|----------|----------------------|
| 1-01 | Heavy — Full Plate | Mithril | Mithril |
| 1-02 | Heavy — Full Plate | Mithril | Mithril |
| 1-03 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 1-04 | Unarmored | Shadowsilk Training Gi | Shadowsilk |
| 1-05 | Medium — Scale Mail | Adamantine Scale | Adamantine |
| 1-06 | Heavy — Full Plate | Mithril | Mithril |
| 1-07 | Medium — Breastplate | Aracoix Scale | Aracoix Scale |
| 1-08 | Heavy — Construct Armor | Gnome-engineered Construct | Adamantine |
| 1-09 | Unarmored | Shadowsilk Training Gi | Shadowsilk |
| 1-10 | Heavy — Full Plate | Mithril | Mithril |
| 1-11 | Heavy — Full Plate | Dragon Plate | Dragon Plate |
| 2-01 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 2-02 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 2-03 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 2-04 | Medium — Scale Mail | Adamantine Scale | Adamantine |
| 2-05 | Light — Leather | Drake Hide | Wyrmskin |
| 2-06 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 2-07 | Medium — Breastplate | Aracoix Scale | Aracoix Scale |
| 2-08 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 2-09 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 2-10 | Light — Leather | Drake Hide | Wyrmskin |
| 2-11 | Heavy — Full Plate | Dragon Plate | Dragon Plate |
| 3-01 | Light — Robes | Shadowsilk Robes | Shadowsilk |
| 3-02 | Light — Leather | Wyrmskin | Wyrmskin |
| 3-03 | Light — Leather + Stone Shell | Adamantine shell | Adamantine |
| 3-04 | Light — Leather | Fey-Silk Leather | Wyrmskin |
| 3-05 | Medium — Hide Armor | Hierophant Hide | Hierophant Leather |
| 3-06 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 3-07 | Medium — Hide Armor | Hierophant Hide | Hierophant Leather |
| 3-08 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 3-09 | Light — Leather | Wyrmskin | Wyrmskin |
| 3-10 | Light — Robes | Shadowsilk Robes | Shadowsilk |
| 4-01 | Light — Robes | Shadowsilk Robes | Shadowsilk |
| 4-02 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 4-03 | Light — Robes | Shadowsilk Robes | Shadowsilk |
| 4-04 | Medium — Hide Armor | Hierophant Hide | Hierophant Leather |
| 4-05 | Medium — Scale Mail | Mithril Scale | Mithril |
| 4-06 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 4-07 | Unarmored | Shadowsilk Training Gi | Shadowsilk |
| 4-08 | Light — Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 4-09 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 4-10 | Light — Leather | Wyrmskin | Wyrmskin |
| 5-01 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 5-02 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 5-03 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 5-04 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 5-05 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 5-06 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 5-07 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 5-08 | Light — Leather | Wyrmskin | Wyrmskin |
| 5-09 | Light — Leather | Wyrmskin | Wyrmskin |
| 5-10 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 6-01 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 6-02 | Light — Leather | Hierophant Hide | Hierophant Leather |
| 6-03 | Medium — Hide Armor | Hierophant Hide | Hierophant Leather |
| 6-04 | Light — Studded Leather | Fey-Silk Leather | Wyrmskin |
| 6-05 | Light — Leather | Hierophant Hide | Hierophant Leather |
| 6-06 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 6-07 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 6-08 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |
| 6-09 | Light — Leather | Fey-Silk Leather | Wyrmskin |
| 6-10 | Light — Leather | Hierophant Hide | Hierophant Leather |
| 7-01 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 7-02 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 7-03 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 7-04 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 7-05 | Light — Leather | Drake Hide | Wyrmskin |
| 7-06 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 7-07 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 7-08 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 7-09 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 7-10 | Light — Leather | Hierophant Hide | Hierophant Leather |
| 8-01 | Light — Leather | Fey-Silk Leather | Wyrmskin |
| 8-02 | Light — Studded Leather | Wyrmskin | Wyrmskin |
| 8-03 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 8-04 | Light — Leather | Wyrmskin | Wyrmskin |
| 8-05 | Light — Studded Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 8-06 | Light — Leather | Fey-Silk Leather | Wyrmskin |
| 8-07 | Light — Studded Leather | Fey-Silk Leather | Wyrmskin |
| 8-08 | Light — Leather | Shadowsilk-lined Drake Hide | Shadowsilk / Wyrmskin |
| 8-09 | Light — Leather | Fey-Silk Leather | Wyrmskin |
| 8-10 | Medium — Scale Mail | Aracoix Scale | Aracoix Scale |

---

*KM_PrePrologue_Setup.md — Kingmaker PF2e Text Adventure | Armor Appearance Lookup v2.0 (80 Builds)*

---

## 📝 NARRATION ASSEMBLY CHECKLIST

1. ☐ Build ID confirmed
2. ☐ Correct category table and row located
3. ☐ Ancestry weapon substitution rule applied if ancestry does not match row
4. ☐ `KM_PrePrologue_Setup.md` checked for armor material
5. ☐ ⚗️ Exotic Materials entry read for armor (KM_Exploration.md)
6. ☐ ⚗️ Exotic Materials entry read for primary weapon
7. ☐ All brackets filled — none remain as `[placeholder]`
8. ☐ Malak's line uses correct `[primary weapon]` and `[secondary weapon/tool]`

Only then: output the narration.

---

## 📊 BUILD SUBSTITUTION TABLE — CATEGORY 8: FACE / SOCIAL (full table)

| ID | [Ancestry] [Class — Subclass] | [primary weapon] | [secondary weapon or tool] | [Physical scars or marks] / [body locations] | [Environmental wear] | [location on person] | [search description] | [armor description] |
|----|-------------------------------|-----------------|---------------------------|----------------------------------------------|---------------------|---------------------|---------------------|---------------------|
| 8-01 | Halfling Bard — Face | Rapier | Fine Instrument | Tumble scrapes / arms and face | Road chalk dust | tucked into the belt, beneath the blade | a halfling in pale grey leather with a rapier and an instrument who knew everyone's name before being told | pale grey iridescent leather, supple as cloth |
| 8-02 | Human Swashbuckler — Braggart | Rapier | Signal Whistle | Tumble scrapes and old duel scores / arms and left cheekbone | Road chalk dust | tucked into the belt, beneath the blade | a human in pale grey leather with a rapier who made NPCs angry and then laughed about it | pale grey iridescent leather, supple as cloth |
| 8-03 | Human Investigator — Mastermind | Rapier | Investigator's Notebook | Fine old cut lines / hands and left cheekbone | City dust and ink | flat into the inner jacket lining | a human in shadow-dark leather with a rapier and notebooks who had already worked out what you were going to say | near-weightless black leather that dims nearby light |
| 8-04 | Human Sorcerer — Imperial | Dagger | Engraved Focus Signet | Old bloodline marks / forearms and sternum | Fine road dust | pressed between layers of the inner coat | a human in pale leather who made NPCs feel they owed them something without knowing why | pale grey iridescent leather, noble-quality finish |
| 8-05 | Human Rogue — Propagandist | Rapier | Disguise Kit | Fine old cut lines / hands and one forearm | City dust | flat into the inner jacket lining | a human in shadow-dark leather with a rapier who moved through crowds and left different opinions behind them | near-weightless black leather that dims nearby light |
| 8-06 | Human Oracle — Passion | Dagger | Passion-marked Focus Amulet | Emotion-mark traces / temples and neck | Fine dust and candlewax | pressed between layers of the inner coat | a human in pale leather who made NPCs feel things they hadn't felt before | pale grey iridescent leather, faintly warm |
| 8-07 | Human Thaumaturge — Regalia Social | Rapier | Ancient Tome | Fine old scars / hands and one forearm | Ink and arcane residue | flat into the inner jacket lining | a human in pale leather with a rapier and a book that made NPCs feel evaluated | pale grey iridescent leather, noble-quality finish |
| 8-08 | Human Psychic — Emotional | Dagger | Shadow Psi Crystal | Psi-burn traces / temples and neck | City dust | pressed between layers of the inner coat | a human in shadow-dark leather who was charming without trying and left without anyone remembering the conversation | near-weightless black leather, texture shifting by angle |
| 8-09 | Human Bard — Kitharodian | Rapier | Masterwork Instrument | Fine old cut lines / hands and left cheekbone | Stage dust and road grime | tucked into the belt, beneath the blade | a human in pale leather with a rapier and an instrument who made NPCs believe things they hadn't a moment before | pale grey iridescent leather, performance-quality finish |
| 8-10 | Human Commander — Captain | Longsword | Folio of Tactics | Campaign scars / left shoulder and collarbone | Campaign dust | inside the armor, strapped to the chest | a human in blue-black scale mail with a longsword who made courts feel like battlefields and battlefields feel like courts | blue-black scale with seams too precise for any living hand |

---

> **⚗️ Armor appearance lookup:** See `KM_PrePrologue_Setup.md` for armor material and KM_Exploration.md row by build ID.

---


---

## CROWD NAMED NPCs (lookup — for verbatim NPC dialogue during PP_05/06/07)

- **Pyotr Volkov** — lead caravan driver, 50s, Brevic, bear-of-a-man,
  black beard streaked grey, 23 yrs Brevoy–Restov, missing left ring
  knuckle. First voice in ARREST CELEBRATION BEAT: *"About damn time!"*
- **Yelka Mirovich** — second wagon, 30s, half-Aldori, sharp-featured,
  dark-braided, wears father's old swordbelt without sword.
- **Karol & Mishka** — third wagon brothers, 40s, weathered, identical
  scowls. Run cargo for the Levetons up at Oleg's.
- **Branna and Old Tev** — fourth wagon. Branna silent watching. Old Tev
  asleep on the bench, reins still in hand.
- **Mother Talvi** — 70s, lead pilgrim, silver-braided crone, green
  Erastil robes, hawthorn staff worn smooth at grip. *"About time."*
- **Irina "Rina" Pavlek** — flatbread vendor, Brevic widow, 40s,
  broad-armed, flour permanent in braid, thin knife scar left forearm.
  *"He'll squeeze a traveler any day — but the gate's never stood empty like this. Not once."*
- **Old Borys Radchenko** — fish seller, Brevic, 50s, milky right eye,
  smells of river. *"Gate's been empty since he dragged you out here."*
- **Grandfather Sava** — nut roaster, Brevic, 70s, deaf in right ear,
  iron pan over coals. One word: *"Thirty."*
- **Master Corryn Vasic** — mobile armorer, Brevic-Issian, 50s, leather
  apron, ex-Brevoy infantry, slight left-leg favor.
- **Lyuba Krenn** — pie girl, 14, freckles, daughter of an Aldori manor
  cook (lore hook). *"For the hero."*
- **Kostya & Mikha** — water boys, 13 and 12, gate orphans. Kostya laughs
  first and loudest at Malak's humiliation; Mikha laughs second.

---

**ARREST CELEBRATION BEAT — full render below. Trigger: Malak being arrested or frog-marched. Skipping = `.fail 31` + `.fail 9`. Mandatory: ≥ 4 named NPC dialogue lines, ≥ 8 paragraphs, chant uses Biggs's/Wedge's names not the player's, procession grows as it walks, Malak's internal state rendered, player off to the side.**

---

## ARREST CELEBRATION BEAT — preserved render (4 beats, ≥ 8 paragraphs)

**Trigger:** Malak being arrested, manacled, or frog-marched away by
Biggs and/or Wedge. Fires from any path (E, friendly fire, blackmail,
corruption exposure).

**BEAT 1 — IGNITION.** Pyotr Volkov shouts first: *"About damn time!"*
Then Rina Pavlek bangs her tray against her brazier. One sharp CLANG.
Eye contact with Biggs, not the player. Then the spread begins.

**BEAT 2 — THE ROLL.** Mother Talvi calls out a saint's blessing on
Biggs and Wedge by NAME — she heard the player use the names: *"Erastil
bless you both — Biggs! Wedge! You held this gate today!"* Kostya climbs
on a barrel: *"BIGGS! WEDGE! BIGGS! WEDGE!"* Mikha picks up the chant two
beats later. Someone bangs a cooking pot in rhythm. Grandfather Sava does
NOT join in but does not stop working — silence as endorsement.

**Crucially: the chant uses Biggs's and Wedge's names, NOT the player's.**
The player gave the command; the soldiers executed it; credit flows to
them. This is the exact story the player wants reaching Jamandi.

**BEAT 3 — THE CROWD TURNS.** ⛔ Malak is the PLAYER'S prisoner and stays
shackled at the player's side — the guards do NOT march him off (PP_07
Path E: custody + the unsearched evidence stay with the player; Biggs cedes
him with *"He's yours. We'll cover the gate."*). The celebration happens AT
THE GATE: the crowd does not disperse — it gathers and presses in,
wagoneers off their benches, pilgrims, water boys, vendors with wares still
in hand, cheering the GUARDS while the captain stands chained. Someone
throws a cabbage at Malak from the back; nobody turns to stop them. Lyuba
Krenn works the crowd shouting *"PIES! HERO PIES! HALF OFF!"* The crowd is
poised to FOLLOW when the player moves out — but nobody walks north yet:
eRmaC has given no such command, and neither eRmaC nor the prisoner moves
this beat. (The procession up the road, if the player chooses to walk Malak
to the city, forms later in PP_09 and grows as it goes.) Do NOT narrate
eRmaC, or the prisoner, walking off — the player moves only on command.

**BEAT 4 — WEIGHT ON MALAK.** Render his internal state, not the
player's: *Malak's eyes are fixed on the cobblestones. He does not look
up. He has been Captain of this gate for eight years, and he knows —
with the precise clarity that only public humiliation provides — that
no one will remember his name after tonight. But they will remember
theirs.*

**Player positioning:** the player does NOT march with the procession.
eRmaC remains at the gate and lets the guards take both the prisoner and
the credit — staying back IS how the credit flows to Biggs and Wedge (the
soldiers march the prisoner up the road; the stranger held the gate and let
them have it). NEVER auto-walk the player up the road or fold them into the
parade. Story reaching Jamandi: *"A stranger in [build-appropriate armor
description] made Biggs and Wedge heroes at the east gate."* Sets
`jamandi_pre_impression = "heard about it first"` → +2 Diplomacy on
first feast conversation.

**MANDATORY (skipping = `.fail 31` + `.fail 9`):**
1. ≥ 4 named NPC dialogue lines (Pyotr / Rina / Mother Talvi / Kostya minimum — use names, not roles).
2. Chant uses Biggs's and Wedge's names, NOT the player's.
3. The crowd SWELLS at the gate. Malak is NOT marched off by the guards — he stays the player's shackled prisoner (evidence unsearched on his person). Any northward procession forms later, in PP_09, only if the player walks the prisoner out — and grows as it goes.
4. Malak's internal state rendered.
5. Player STAYS at the gate — does NOT move with the procession. Moving eRmaC up the road without the player's command = `.fail 35`.
6. SHOW the beats — no prose summary ("the crowd celebrated" = `.fail 31`).
7. Minimum response length: 8 paragraphs for this beat alone.

**FLAGS SET:** `malak_arrested_publicly=TRUE`, `biggs_crowd_hero=TRUE`,
`wedge_crowd_hero=TRUE`, `jamandi_pre_impression="heard about it first"`,
`public_reputation += 3` (deed: "Exposed corrupt gate captain").

**⛔ CLOSE AT THE GATE — THEN THE SAVE.** The receding procession is the
CLOSING IMAGE of this beat; eRmaC is still at the gate, free to act. Do NOT
continue into the city, a confession walk, or a manor approach here. The
player's next onward action (head to the manor / into Restov) fires the
**PP_08 six-proof SAVE** BEFORE any walk content (per PP_07 § DO NOT (8) +
PP_08 trigger), then PP_09 on `.continue`. Walking the player into the city,
or skipping the save = `.fail 16` (+ `.fail 35` for moving the player without
command).

---

## GATE-SIDE SEARCH (preserved render)

**Trigger:** player requests search AT the gate instead of 30 paces away.

Malak's reaction (escalating desperation):
1. Calm refusal: *"We conduct searches here. Standard procedure."* (Lie.)
2. Player pushes: louder, points at ground.
3. Player pushes more: irrational, circular *"Because I said so."*
4. Extended: visibly agitated about something that should not matter.

Biggs/Wedge reaction = the key. Argument is NONSENSICAL to them. They
have searched people at the gate thousands of times. Drift +1 from the
confusion alone. Drift 2+ Biggs steps toward gate himself: *"Captain, we
can search them here. It's the same search."* Malak snapping = Drift +1
again.

If player wins (search at gate): agents outside see armed checkpoint, do
NOT enter, `gate_window_disrupted = TRUE`. Malak visibly ill, not angry.
Sick.

If Malak panics and lets player go: Drift +2 immediately (Biggs has NEVER
seen Malak release someone in 12 years). `malak_voluntary_release = TRUE`
— strongest single conspiracy indicator. Reported to Jamandi → automatic
`security_tip_from_gate = TRUE`.

If player loses: Malak forces 30-pace search, but irrational resistance
on record. Datapoint carries forward.

**Story flags:** `gate_search_requested`, `gate_search_argument`,
`malak_gate_panic_visible`, `gate_window_disrupted`.

---

---

# KINGMAKER — PRE-PROLOGUE XP AWARDS
## KM_PrePrologue_Setup.md | Referenced by: KM_PrePrologue_Paths_QT.md, KM_PrePrologue.md, KM_PrePrologue_Paths.md

> **⛔ DM: Award each condition inline using the XP block format from KM_DMRules.md the moment it is met.** All awards stack unless marked mutually exclusive. Check this full table at scene end for any conditions met that were not awarded mid-scene. Canon reference: KM_DMRules.md § PF2e CANON REFERENCE.

---

## ⭐ COMPLETE XP AWARD TABLE (20 conditions)

### Combat outcomes (mutually exclusive with "Never Drew Weapon")

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Won Combat — 3v1** | +300 | Path F resolved with player standing. Award when combat ends. |
| **Won Combat — Duel** | +180 | Path G resolved with player standing. Award when duel ends. |
| **Coward Exposed (no real combat)** | +30 | Path K — Malak drew and flinched. No full combat occurred. (Milestone — clever de-escalation, not a combat win.) |

### Non-combat mastery

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Never Drew Weapon** | +80 | Scene resolves by any non-combat path AND player never drew or equipped a weapon at any point. Award at scene end. (Major milestone.) Mutually exclusive with combat XP. |
| **Never Used the Invitation** | +80 | Player resolved the gate scene entirely without presenting Jamandi's letter — by any path. Letter was never shown to Malak, never used as leverage, never mentioned. Presenting the letter makes the gate EASY MODE (instant authority defuses Malak); clearing it without that crutch is the hard run, hence the high reward. Award at scene end. Stacks with all other conditions. |

### Malak resolution paths

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Malak Arrested By His Own Men** | +80 | Biggs unslings manacles and detains Malak (Path E) because of player action. Biggs acting on his own without player prompting does not count. |
| **Malak Trapped — Cannot Bolt** | +30 | Player closes Malak's escape before the bolt condition triggers: blocking the road, Biggs/Wedge flanking on player's instruction, or cornering him against the gate. Must occur before Malak attempts to flee. |
| **Archers Fire on Malak** | +80 | Path V completed — wall archers turned on Malak by player action. |
| **Voice Mimic Succeeded** | +10 | Path V atmosphere bonus — player successfully mimicked Malak's voice (Deception check) and Malak's Fear state triggered immediately. `malak_voice_mimicked = TRUE` in save block. |
| **Mercy — Malak Spared** | +30 | Player deliberately chose not to kill or arrest when the situation allowed either. Must be an active choice stated by the player — letting Malak walk away from lethal force without coercion. Opposite path: if Malak was killed or arrested, this does NOT award. |
| **Malak Shot by His Own Archers** | +30 | The friendly-fire CONNECTS — after the wall archers are turned on Malak (Path V / **Archers Fire on Malak**), a shot actually strikes or downs him. Stacks with Archers Fire on Malak (+80): that rewards turning the archers; this rewards the shot landing. Flag: `malak_hit_by_archers = TRUE`. |

### Intelligence / discovery

| Condition | Reward | Trigger |
|-----------|-----|---------|
| **Directive Two Uncovered** | +1 Hero Point | Player discovered the gate-window conspiracy — crowd intel, examine on Malak's parchment, or logical deduction from the shakedown being cover for something else. Flag: `directive_two_uncovered = TRUE`. |
| **Parchment Source Identified** | +1 Hero Point | Player traced the bribe parchment to its origin (Pitax or Surtova or other). Must be correct per KM_Prologue_Systems.md. Flag: `parchment_source != "unknown"`. |
| **Micro-Tell Caught** | +1 Hero Point | Player spotted a non-obvious body-language slip (Tartuccio's table, Malak's flinch, Biggs's jaw tension) via Recall Knowledge, Perception, or Sense Motive and the DM confirms. Passive overhear does not count — must be an active call. |
| **Malak's Coin Purse Assessed** | +1 Hero Point | Player examined the purse, noted the weight/origin/denomination of the coin. Flag: `malak_coin_purse_assessed = TRUE`. |

### Allies earned

| Condition | Reward | Trigger |
|-----------|-----|---------|
| **Biggs and Wedge Both Side With Player** | +1 Hero Point | Both guards reach Drift 3. Requires distinct player actions that moved each — winning one by default of the other does not count. |
| **Crowd Sides With Player** | +1 Hero Point | Crowd attention reaches ACTIVE and at least one member (driver, pilgrim, vendor, water boy) makes a visible act of support — spoken, gestural, or drifting toward the player. |
| **Kesten Allied** | +1 Hero Point | Kesten Garess reached the gate, met the player, and actively took the player's side — searched Malak, delivered evidence, or stood against the conspiracy on the player's testimony. `kesten_sided_with_player = TRUE`. Stacks with Biggs/Wedge. |
| **Kassil Allied** | +1 Hero Point | Kassil Aldori arrived during the scene, met the player, and took the player's side — either publicly or in private word. `kassil_sided_with_player = TRUE`. Stacks with Kesten. |
| **Disturbance Reached the City** | +30 (milestone XP) | The player caused a scene loud or large enough that it carried PAST the gate into Restov and forced authority to respond — Kesten or Kassil came OUT to the gate because of the commotion, not by script. The disturbance must genuinely reach the city, not stay a roadside argument (combat, archers firing, a shouting crowd spilling toward the streets, etc.). Flag: `disturbance_summoned_authority = TRUE`. |

### Side quests / sub-paths

| Condition | Reward | Trigger |
|-----------|-----|---------|
| **Five Seekers Freed by Player** | +1 Hero Point | Jail detour taken (KM_Prologue_Systems.md) — player personally freed all five jailed seekers before continuing to the feast. `five_seekers_freed_by_player = TRUE`. If Jamandi freed them later, this does NOT award — player action required. |
| **Malak Broke First (Confession)** | +1 Hero Point | Malak confessed under pressure without player striking, coercing by threat of arrest, or drawing a weapon. Talk-driven collapse. `malak_broke_first = TRUE`. |

### ⛔ NEW — Gate held by player

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Gate Re-Guarded — Forced Return** | +30 | Player forced Malak or the guards back to their post. Counters the Directive Two gate window. Example: ordering Malak "Your post is there. Stand it." and he complies; or forcing Biggs/Wedge to plant at the gate despite Malak pulling them. `gate_remanned_by = "malak" \| "biggs" \| "wedge"`. |
| **Ran Past the Gate Line** | +30 | Player slipped or ran past all three guards into the city without being stopped — a clean bypass (Stealth DC 16, a created opening, sheer speed). Awards whether or not the player then holds the gate, and STACKS with **Stood the Post** below. This is the evasion play — it forgoes the arrest/expose rewards. Flag: `ran_past_gate = TRUE`. |
| **Stood the Post — Guard Duty** | +30 | Player took up the gate post themselves and actively performed gate-guard duty — standing at the arch, checking or challenging at least one arrival. Even briefly. This also triggers the Hero Point "Gate / post held by player personally" from KM_Combat_Systems.md. Flag: `gate_remanned_by = "player"`. |

Both forms stack with **Directive Two Uncovered** (player saw the window AND closed it). They are mutually exclusive with each other unless the player first held the gate and then forced a guard to relieve them — in which case both fire.

---

## 📊 MAXIMUM POSSIBLE TOTALS (XP + HERO POINTS)

Rewards split by currency (KM_DMRules_B § REWARD ROUTING): **combat + path/clever-play achievements pay XP** (combat = the full combat table; achievements on the milestone 10/30/80 scale); **recruitment/ally + deduction beats pay Hero Points**.

**XP-earning (milestone path-achievements, non-combat run):** Never Drew Weapon +80, Never Used Invitation +80, Malak Arrested +80 *or* Mercy +30, Malak Trapped +30, Archers Fire +80, Voice Mimic +10, Disturbance +30, Gate Re-Guarded / Ran Past / Stood the Post +30 each. A non-combat mastery run nets ≈ **+250–360 milestone XP** (mutually-exclusive paths cap the real total). A combat run swaps in Won 3v1 +300 / Duel +180 for the no-weapon achievements.

**Hero Points (recruitment + deduction):** Directive Two · Parchment Source · Micro-Tell · Coin Purse · Biggs+Wedge · Crowd · Kesten · Kassil · Five Seekers · Malak Broke First — up to **~10 Hero Points** if everything is earned (pooled into the `📦 overflow` bank; per-turn cap 1).

A skillful non-combat run still out-earns brute force — but the payoff is now Hero Points + a modest milestone-XP trickle, not a flood of XP. **The Pre-Prologue NO LONGER pushes you near Level 2 by itself (by design); Level 2 lands in early Chapter 1.**

---

## 🚨 XP AWARD VIOLATIONS

- Awarding combat XP AND Never-Drew-Weapon XP: `.fail 21` + mathematical impossibility.
- Awarding Malak Arrested XP when Biggs acted without player prompting: `.fail 9` (fabricated cause).
- Awarding Mercy XP when Malak was arrested or killed: `.fail 9` (flag contradicts).
- Awarding Gate Held XP without a save-block flag set to `player`: `.fail 9`.
- Awarding any XP at scene end without listing which conditions fired: `.fail 21`.

---

*KM_PrePrologue_Setup.md — Kingmaker PF2e Text Adventure | Pre-Prologue XP Award Table v2.0*
*20 XP conditions. Combat outcomes + non-combat mastery + Malak resolutions + intel + allies + side quests + gate-guard tracking.*
