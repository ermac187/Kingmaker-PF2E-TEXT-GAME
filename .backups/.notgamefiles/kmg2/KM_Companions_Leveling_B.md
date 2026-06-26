# KINGMAKER — COMPANION LEVELING MAPS (EXTENDED)
## KM_Companions_Leveling_B.md | Overflow from KM_Companions_Leveling.md

> **DM:** This file holds companion leveling maps that did not fit in the main KM_Companions_Leveling.md. Load whenever its companions are in the party or being recruited.

---

## COMPANION 1 — JUBILOST NARTHROPPLE
**Gnome | Alchemist (Bomber) | Role: Ranged Blaster/Scholar**
> **DM:** Core companion #1. Profile and Capital fallback scene here (not in KM_Companions_B.md).
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

## COMPACT LEVELING SEEDS — ALL SECTIONS

> **Coverage:** All Section B/C/D companions + WotR additions.
> **Excluded:** KM/WotR originals — boost priorities in KM_Companions_Leveling.md Quick Reference.
> **Format:** # | Name | Build | Boosts (L5/L10/L15/L20) | L1 Pick → Capstone
> **Auto-level rule:** Apply class auto-level from KM_DMRules.md. Apply boost priority + feats from this table on top.

---

### ALCHEMIST
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 2 | Sucrose | Mutagenist / Logistician | INT CON DEX WIS | Revivifying Mutagen + Specialty Crafting → Ultimate Mutagen |
| 3 | Excella Gionne | Toxicologist | INT CON DEX CHA | Poison Weapon → Debilitating Bomb |

### ANIMIST
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 4 | Senua | Echoing Hierophant | WIS CON INT CHA | Witness Apparition + Shift Apparition → Spirit Mastery |
| 5 | Jeanne d'Arc Alter | Dark Order | WIS CON INT CHA | Dark Ancestor → Void Channel Capstone |

### BARBARIAN
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 7 | Trever | Animal Instinct/Wolf | STR CON DEX WIS | Animal Rage → Apex of Power |
| 8 | Red Sonja | Fury Instinct | STR CON DEX WIS | Furious Focus → Apex of Power |
| 9 | Callisto | Dragon Instinct | STR CON WIS DEX | Furious Vengeance → Dragon's Rage Capstone |

### BARD
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 10 | Lem | Maestro/Polymath | CHA CON DEX WIS | Lingering Composition → Inspire Heroics |
| 11 | Storm Silverhand | Maestro | STR CHA CON DEX | Lingering Composition → Inspire Heroics |
| 12 | Tira | Warrior Muse | STR CHA CON DEX | Inspire Courage Melee → Warrior's Cadence |

### CHAMPION
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 13 | Seelah | Paladin/Iomedae | STR CHA CON DEX | Lay on Hands → Celestial Form |
| 14 | Minthara Baenre | Desecrator/Lolth | STR CHA CON WIS | Destructive Aura → Divine Vessel |
| 15 | Artoria Pendragon (Saber) | Redeemer / Shield of Purity | STR CON CHA DEX | Glimpse of Redemption + Lay on Hands → Champion Mastery |

### CLERIC
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 17 | Sosiel | Warpriest/Shelyn | WIS CHA CON DEX | Channel Smite → Avatar's Grace |
| 18 | Jaethal | Harm/Zon-Kuthon | WIS CON DEX CHA | Channel Smite → Divine Weapon |
| 19 | Kyra | Warpriest/Sarenrae | WIS STR CON CHA | Deadly Simplicity → Avatar's Grace |
| 20 | Harrim | Warpriest/Groetus | WIS STR CON DEX | Channel Smite → Heroic Recovery |
| 21 | Goldmoon | Grave-Warden Warpriest / Mishakal | WIS CON STR CHA | Warpriest Strike + Heal Font → Channel Smite Mastery |
| 22 | Viconia DeVir | Harm/Shar | WIS CON DEX CHA | Channel Smite → Night's Cloak Capstone |

### COMMANDER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 24 | Olivier Armstrong | Tactical Overlord | INT CON STR DEX | Tactical Orders + Banner → Supreme Command |
| 25 | Esdeath | Conquest | DEX CON INT CHA | Weiss Schnabel → Ice Dominion Capstone |

### DRUID
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 26 | Ulbrig | Animal Order/Griffon | WIS STR CON DEX | Griffon Shape → Dragon Shape |
| 27 | Lini | Animal Order | WIS CON DEX INT | Animal Companion → Masterful Companion |
| 28 | Pamela Isley (Poison Ivy) | Wild Order/Wood | WIS CON CHA INT | Verdant Weal → Primal Capstone |
| 29 | Keyleth of the Air Ashari | Wild Order+Kineticist | WIS CON DEX INT | Aramente Bond → Ashari Form → Planar Shift |

### EXEMPLAR
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 30 | Diana Prince (Wonder Woman) | Amazonian Ikon | STR CHA CON DEX | Lasso Ikon → Transcendence Burst |
| 31 | Hope (Lady Death) | Death's Aspect Ikon | CHA CON WIS DEX | Dark Ikon → Unholy War Capstone |

### FIGHTER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 23 | Regill | Hellknight/Precision | STR CON WIS DEX | Combat Flexibility → Weapon Mastery |
| 33 | Wenduag | Dual-Wield | DEX STR CON WIS | Double Slice → Impossible Flurry |
| 34 | Valeros | Sword and Shield | STR CON DEX WIS | Reactive Shield → Weapon Mastery |
| 35 | Tika Waylan | Polearm Master / Reach | STR CON DEX WIS | Guisarme reach/trip + AoO → Reach Mastery |
| 36 | Kitiara Uth Matar | Commanding Blade | STR CON DEX CHA | Combat Flexibility → Legendary Assault |

### GUARDIAN
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 37 | Hoshiguma Yuugi | Shield/Fortress | STR CON WIS DEX | Shield Wall → Fortress Bastion |
| 38 | Meredith Stannard | Control/Authority | STR CON WIS CHA | Authority Guard → Command Capstone |

### GUNSLINGER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 39 | Yoko Littner | Fake Out Sniper | DEX WIS CON INT | Fake Out + Aimed Shot → Shooter's Camouflage → Legendary Sniper |
| 40 | Rebecca Lee (Revy) | Way of the Pistolero | DEX CHA CON WIS | Pistol Twirl → Finishing Follow-Through |

### INVENTOR
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 41 | Winry Rockbell | Megavolt/Support | INT CON DEX WIS | Megavolt Blast → Innovation Mastery |
| 42 | Alex Wesker | Construct/Legacy | INT CON WIS DEX | Construct Companion → Efficient Helper |

### INVESTIGATOR
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 43 | Kyoko Kirigiri | Forensic Medicine + Medic | INT WIS CON DEX | Battle Medicine doubled + Doctor's Visitation → Trickster's Ace + Didactic Strike |
| 44 | Lust | Intuition/Reach | DEX INT CON WIS | Reach Attack Strike → Legendary Detective |

### KINETICIST
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 45 | Kalikke/Kanerah | Dual Gate | CON DEX WIS INT | Elemental Overlap → Dual Gate Mastery |
| 46 | Yang Xiao Long | Everbloom Bastion | CON STR DEX WIS | Wood Gate + Fresh Produce → Gate Mastery (Wood/Earth) |
| 47 | Caitlin Snow (Killer Frost) | Water/Cold Gate | CON DEX WIS INT | Cold Gate → Gate Mastery |

### MAGUS
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 48 | Regongar | Inexorable Iron/Spellstrike | STR INT CON DEX | Spellstrike Aggression → Iron Capstone |
| 49 | Weiss Schnee | Dimensional Striker | INT DEX CON WIS | Starlit Span + Archer Dedication → Expansive Spellstrike |
| 50 | Cinder Fall | Inexorable Iron/Flame | STR INT CON DEX | Spellstrike Aggression → Iron Capstone |

### MONK
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 51 | Lann | Monastic Archer | DEX WIS CON STR | Flurry Arrows → Masterful Archer |
| 52 | Sajan | Flowing Maneuver | DEX WIS CON STR | Stunning Fist → Legendary Reflexes |
| 53 | Tifa Lockhart | Brawler/Flurry | DEX STR CON WIS | Flurry of Blows → Legendary Brawler |
| 54 | Sandra Wu-San (Lady Shiva) | Stumbling Stance | DEX WIS CON STR | Stumbling Stance → Legendary Reflexes |

### ORACLE
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 55 | Daeran | Life Mystery | CHA WIS CON INT | Soothing Tones → Life-Link Capstone |
| 56 | Rei Hino (Sailor Mars) | Flames Mystery | CHA WIS CON INT | Oracular Warning → Cosmic Form |
| 57 | C.C. | Lore Mystery/Geass | CHA INT CON WIS | Whisper of Warning → Cosmic Form |

### PSYCHIC
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 58 | Tatsumaki | Chronos Master / Infinite Eye | INT CON WIS DEX | Infinite Eye + Precise Discipline → Time-Warp Burst |
| 59 | Emma Frost | Thoughtform/Telepathy | INT CHA CON DEX | Hallucination → Overpowering Mind |

### RANGER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 60 | Ekundayo | Precision Edge | DEX WIS CON STR | Hunted Shot → Masterful Hunter |
| 61 | Arueshalae | Precision Edge | DEX CHA WIS CON | Hunted Shot → Masterful Hunter |
| 62 | Greybor | Flurry Edge | DEX STR CON WIS | Twin Takedown → Masterful Hunter |
| 63 | Harsk | Precision Edge | DEX WIS CON STR | Hunted Shot → Masterful Hunter |
| 64 | Alleria Windrunner | Ghost-Wolf Hunter | DEX WIS CON STR | Outwit Edge + Animal Companion (Wolf) → Masterful Hunter (Outwit) |
| 65 | Sylvanas Windrunner | Flurry Hunter | DEX WIS CON STR | Aimed Shot → Fatal Wailing Arrow |

### ROGUE
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 66 | Nok-Nok | Scoundrel | DEX CON INT WIS | Tumbling Strike → Hidden Paragon |
| 67 | Woljif Jefto | Mastermind | DEX INT CON CHA | Mastermind Research → Legendary Sneak |
| 68 | Merisiel | Thief | DEX CHA CON STR | Tumbling Strike → Hidden Paragon |
| 69 | Imoen | Opportunistic Thief | DEX INT CON CHA | Trap Finder + Thief Racket → Hidden Paragon |
| 70 | Yor Briar (Yor Forger) | Elusive/Precision | DEX CON INT WIS | Tumbling Strike → Legendary Sneak |

### SORCERER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 71 | Seoni | Arcane Bloodline | CHA CON DEX INT | Dangerous Sorcery → Bloodline Paragon |
| 72 | Rachel Roth (Raven) | Demonic/Soul-Self | CHA CON WIS INT | Dangerous Sorcery → Bloodline Paragon |
| 73 | Ultimecia | Arcane/Time | CHA INT CON DEX | Dangerous Sorcery → Arcane Evolution |

### SUMMONER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 74 | Salem | Elder Grimm-Bonded | CHA CON WIS INT | Evolution Surge → Ultimate Evolution |
| 75 | Yuna | Fayth-Bonded | CHA WIS CON INT | Aeon Summon → Grand Summon |

### SWASHBUCKLER
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 76 | Isabella Valentine (Ivy Valentine) | Fencer/Duelist | DEX CHA CON WIS | Vivacious Bravado → Stylish Tricks |
| 77 | Isabela | Battledancer | DEX CHA CON WIS | Performance Panache → Battledancer Aura |

### THAUMATURGE
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 78 | Ryuko Matoi | Regalia / Aura King | CHA DEX CON WIS | Regalia Implement (Senketsu) + Whip → Aura Paragon |
| 79 | Nui Harime | Scissors/Needles | DEX INT CON WIS | Exploit Vulnerability → Implement Paragon |

### WITCH
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 80 | Ember | Curse Patron | INT WIS CHA CON | Cackle Sustain → Hex Paragon |
| 81 | Camellia | Shadow Patron/Pure Hex | WIS INT CON CHA | Evil Eye + Misfortune → Patron's Truth |
| 82 | Medusa Gorgon | Twisted Love Patron | INT WIS CON CHA | Evil Eye → Misfortune Stack |
| 83 | Morrigan | Hex-Bound Shepherd / Resentment | INT CON WIS DEX | Enfeeblement Hex + Cackle → Patron's Transformation |

### WIZARD
| # | Name | Build | Boosts | L1 → Capstone |
|---|------|-------|--------|---------------|
| 84 | Octavia | Transmutation | INT DEX CON WIS | Arcane Thesis → Transmutation Capstone |
| 85 | Nenio | Illusion | INT DEX CON WIS | Illusion Thesis → True Illusion |
| 86 | Ezren | Universalist | INT WIS CON DEX | Hand of the Apprentice → Archwizard's Spellcraft |
| 87 | Megumin | Evoker/Spellmaster | INT CON DEX WIS | Spell Penetration → Archwizard's Spellcraft |
| 88 | Liliana Vess | Necromancer | INT CON WIS DEX | Dangerous Spells → Army of the Dead |

---

> **Delegate note:** Companions not listed here use generic class priority: martials STR/DEX→CON→WIS, arcane INT→CON→DEX, divine WIS→CON, occult CHA/INT→CON.

---

*KM_Companions_Leveling_B.md — Kingmaker PF2e Text Adventure | Overflow leveling maps + Compact Seeds v5.0*
