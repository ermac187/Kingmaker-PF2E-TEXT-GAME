# KINGMAKER — COMPANION BUILD ASSIGNMENT
## KM_Companions_Builds.md | Referenced by: KM_Companions_Iconics.md, KM_DMRules.md

> **⛔ NO TRAINING DATA. Preset numbers and names refer ONLY to `KM_BuildGuide_A.md` (classes 1–13) and `KM_BuildGuide_B.md` (classes 14–27) — 27 classes × 10 presets each. Using PF2e training knowledge to substitute names or numbers = `.fail 9`.**
>
> **Signature moves / unique powers:** See `KM_Signatures_A/B/C.md` for per-companion canonical signature abilities. Load when the companion is in the active party; surface MOVE in their combat menu.
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
  Assign presets for all 11 companions. Options:
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
  2. Load that class's build block from KM_BuildGuide_A.md (classes 1–13) or KM_BuildGuide_B.md (classes 14–27).
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
  7. Next companion. Repeat until all 11 assigned.

After all 11 assigned, display summary:
  Companion | Class | Preset # | Preset Name | Lore Fit (★/⚠️/—)
  Then proceed to Pre-Prologue.
```

---

## 🧭 COMPANION → PRESET TABLE

> **DM:** Preset numbers refer to `KM_BuildGuide_A.md` / `KM_BuildGuide_B.md` (1–10 per class). `—` in Avoid = no conflict.

### SECTION A — KINGMAKER CRPG (12)

| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 1 | Jubilost | Alchemist | #6 Pure Bomber | — | Quest-locked. Pure bomber identity, no dip |
| 6 | Amiri | Barbarian | #1 Tactical Reach King | #3 #4 | Giant sword IS her identity; reach flavor |
| ✦ | Linzi | Bard | #1 Virtuoso Maestro | #3 | Forced. Inspire Courage + ranged; too fragile for melee |
| 16 | Tristian | Cleric | #2 Cloistered Heal | #1 #10 | Quest-locked. Gentle healer, avoids weapons |
| 32 | Valerie | Fighter | #4 Shield Bastion Fighter | #8 | IS the shield wall — removing shield removes her |
| 45 | Kalikke/Kanerah | Kineticist | #1 Element Blaster/Tank | #6 | Quest-locked. Dual gate water+fire; not metal |
| 60 | Ekundayo | Ranger | #3 Archer Sniper | — | Quest-locked. Patient hunter; Hunted Shot precision |
| 66 | Nok-Nok | Rogue | #1 Scoundrel + Thaumaturge | #3 | Quest-locked. Trickster goblin; INT 10, not scholarly |
| 84 | Octavia | Wizard | #4 Universalist Utility + Investigator | — | Quest-locked. Self-taught, resourceful, no fixed school |
| 18 | Jaethal | Cleric | #3 Deadly Simplicity | #2 | Undead elf inquisitor; Harm channel, Zon-Kuthon flavor |
| 20 | Harrim | Cleric | #1 Warpriest Font | #2 | Groetus warpriest; heavy flail + Channel Smite |
| 48 | Regongar | Magus | #1 Spellstrike Hybrid | #6 | Half-orc Inexorable Iron; aggressive Spellstrike |

> **QUEST-LOCKED BUILD RULE:** QL companions (#1 #16 #45 #60 #66 #84) use their ★ preset for auto-leveling from session start. DM levels them silently to match player level. When they join, player may KEEP ★ or CHANGE — if changed, DM respeccs on the spot.

---

### SECTION B — WRATH OF THE RIGHTEOUS CRPG (14)

| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 23 | Regill | Commander | #9 Vanguard Fighter | #3 | Hellknight frontline enforcer; Fighter Ded. + AoO |
| 51 | Lann | Monk | #5 Pure Flurry Agile | #2 | Monastic Archer variant: Flurry applies to bow |
| 55 | Daeran | Oracle | #6 Life Mystery + Cleric | — | Curse-powered healer; Life Link with outsider |
| 61 | Arueshalae | Ranger | #3 Archer Sniper | — | Redeemed succubus; patient precision archer |
| 80 | Ember | Witch | #8 Lesson of Life Heal | #1 | Gentle child-prophet; avoids cruelty hexes |
| 85 | Nenio | Wizard | #4 Universalist Utility + Investigator | #3 | Refuses to specialize; studies everything |
| 81 | Camellia | Witch | #5 Pure Hex Debuff | #8 | Shadow curse patron; Evil Eye + Misfortune stacked |
| 33 | Wenduag | Fighter | #8 Longbow Archer Fighter | #4 | Crossbow ambush striker; ranged first, no shield |
| 67 | Woljif | Rogue | #4 Eldritch Trickster + Psychic | #5 | Arcane tricks extend Sneak Attack; shadow repositioning |
| 17 | Sosiel | Cleric | #2 Cloistered Heal | #4 | Desna cleric; gentle healer, positive font only |
| 62 | Greybor | Ranger | #1 Flurry Hunter | #8 | Contract kill precision; Twin Takedown on the mark |
| 26 | Ulbrig | Druid | #2 Wild Pet Army | #4 | Wild Shape + bear companion both flank simultaneously |
| 7 | Trever | Barbarian | #2 Fury Flurry | #6 | Kellid fury; aggressive dual-weapon pressure forward |
| 13 | Seelah | Champion | #1 Radiant Reach | #5 | Iomedae paladin; Retributive Strike frontline anchor |

---

### SECTION C — PATHFINDER 2E ICONICS (9)

| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 34 | Valeros | Fighter | #4 Shield Bastion Fighter | #1 | Iconic shield fighter; Double Slice off shield arm |
| 19 | Kyra | Cleric | #1 Warpriest Font | #2 | Sarenrae warpriest; longsword + Heal font |
| 71 | Seoni | Sorcerer | #1 Draconic Blaster | #4 | Draconic bloodline; flat fire damage + aura |
| 86 | Ezren | Wizard | #4 Universalist Utility + Investigator | #8 | Methodical late-bloomer; every spell chosen with purpose |
| 52 | Sajan | Monk | #5 Pure Flurry Agile | #10 | Vudrani flurry; Stunning Fist precision striker |
| 27 | Lini | Druid | #2 Wild Pet Army | #4 | Small predator Wild Shape + animal companion flanks |
| 63 | Harsk | Ranger | #9 Crossbow Ace + Gunslinger | #5 | Crossbow sniper; Aimed Shot at extreme range |
| 10 | Lem | Bard | #1 Virtuoso Maestro | — | Halfling maestro; Inspire Courage + ranged support |
| 68 | Merisiel | Rogue | #6 Thief Dexterity God | #3 | Iconic finesse executer; 35 ft mobility + Sneak Attack |

---

### SECTION D — CROSS-IP CONVERSIONS (54)

**ALCHEMIST**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 2 | Sucrose | Alchemist | #7 Grand Mutagenic Logistician | #6 | INT 18 mutagen factory; alchemy researcher identity |
| 3 | Excella Gionne | Alchemist | #4 Rogue Toxicologist | #2 | Precision toxins + Sneak Attack biology |

**ANIMIST**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 4 | Senua | Animist | #9 Echoing Hierophant | — | Flexible multi-apparition support; Witness Reactive Strike free AoO from L1 |
| 5 | Jeanne d'Arc Alter | Animist | #7 Apparition Blaster | #10 | Corrupted holy; all feats blast, no dedication tax |

**BARBARIAN**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 8 | Red Sonja | Barbarian | #4 Spirit Oracle | #5 | Spirit Instinct + Oracle Ded.; ghost-touch ancestral fury |
| 9 | Callisto | Barbarian | #8 Elemental Rage | #6 | Fury Instinct + Kineticist; raw elemental outburst |

**BARD**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 11 | Storm Silverhand | Bard | #2 Warrior Melee | — | Sword + silver fire; Chosen of Mystra frontline |
| 12 | Tira | Bard | #2 Warrior Melee | #1 | Warrior Muse; ring blade frontline + Inspire display |

**CHAMPION**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 14 | Minthara Baenre | Champion | #9 Tyrant Cause | #1 | Evil desecrator; Selfish Shield + fear aura |
| 15 | Artoria Pendragon (Saber) | Champion | #4 Shield of Purity | #9 | Redeemer Sarenrae; Longsword (Caliburn) + Shield (Avalon) protector identity |

**CLERIC**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 21 | Goldmoon | Cleric | #9 Grave-Warden Warpriest | — | Mishakal warpriest; Warhammer + WIS 18 Heal font frontline |
| 22 | Viconia DeVir | Cleric | #4 Harm-Spammer | #1 | Shar; negative font + shadow curse debuff chain |

**COMMANDER**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 24 | Olivier Armstrong | Commander | #6 Tactical Overlord | #3 | Iron Wall; Hobgoblin discipline + Longsword + INT 18 tactics |
| 25 | Esdeath | Commander | #3 Strategist Spellcaster | #4 | Ice arcane control + Wizard Ded.; Slow battlefield |

**DRUID**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 28 | Pamela Isley (Poison Ivy) | Druid | #5 Wave Controller | #4 | Vine entanglement = push/prone control; plant battlefield |
| 29 | Keyleth | Druid | #1 Wild Shape Ki Strike | — | Wild Shape + multi-element blasts; Aramente attunement |

**EXEMPLAR**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 30 | Diana Prince (Wonder Woman) | Exemplar | #5 Divine Ikon Support | #7 | Lasso + Shield + Bracers triple ikon; Share Transcendence |
| 31 | Hope (Lady Death) | Exemplar | #1 Victor's Wreath | #5 | Kill-fed Transcendence; unkillable wound-scaling |

**FIGHTER**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 35 | Tika Waylan | Fighter | #5 Polearm Master | #4 | Reach/trip control; Guisarme + AoO chain |
| 36 | Kitiara Uth Matar | Fighter | #6 Rapier Finesse Fighter | #4 | Duelist precision; Feint + mobile cycling |

**GUARDIAN**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 37 | Hoshiguma | Guardian | #5 Party Shield Wall | #7 | Shield Warden + Tower Shield; anchors two adjacent allies |
| 38 | Meredith Stannard | Guardian | #2 Protector + Champion | #7 | Templar anti-magic + Lay on Hands protective reaction |

**GUNSLINGER**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 39 | Yoko Littner | Gunslinger | #9 Fake Out Sniper | #7 | Kobold-style precision; Fake Out feint + Aimed Shot Arquebus |
| 40 | Rebecca Lee (Revy) | Gunslinger | #7 Pistolero + Swashbuckler | #2 | Dual akimbo; Panache + Finisher aggression |

**INVENTOR**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 41 | Winry Rockbell | Inventor | #3 Construct + Summoner | #4 | Automail construct as eidolon partner |
| 42 | Alex Wesker | Inventor | #8 Construct + Ranger | #4 | Drone-construct Hunt Prey precision targeting |

**INVESTIGATOR**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 43 | Kyoko Kirigiri | Investigator | #6 Forensic Medicine Investigator | #4 | Forensic Medicine + Medic Ded.; Battle Medicine doubled, prepared crit chain |
| 44 | Lust | Investigator | #1 Forensic + Rogue | #10 | Anatomy exploitation + Sneak Attack crit machine |

**KINETICIST**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 46 | Yang Xiao Long | Kineticist | #2 Everbloom Bastion | — | CON 18 fortress healer; Fresh Produce = Semblance HP recovery + Jagged Berms terrain |
| 47 | Caitlin Snow (Killer Frost) | Kineticist | #4 Water Control + Guardian | #3 | Ice entombment; redirect + impulse tank |

**MAGUS**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 49 | Weiss Schnee | Magus | #6 Pure Spellstrike | #2 | Laughing Shadow rapier (Myrtenaster); teleport-Spellstrike maps to Glyph Step |
| 50 | Cinder Fall | Magus | #6 Pure Spellstrike | #2 | Laughing Shadow fire teleport-Spellstrike |

**MONK**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 53 | Tifa Lockhart | Monk | #5 Pure Flurry Agile | #10 | Limit Break cycling; 3 strikes/action combo |
| 54 | Sandra Wu-San (Lady Shiva) | Monk | #3 Stance Master + Guardian | #10 | Iron Mountain + Guardian wall; no wasted motion |

**ORACLE**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 56 | Rei Hino (Sailor Mars) | Oracle | #3 Flames Mystery Blaster | #6 | Sacred fire AoE nova; Battle Oracle secondary |
| 57 | C.C. | Oracle | #5 Pure Curse Control | #6 | Contract compulsion debuff; Regeneration sustain |

**PSYCHIC**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 58 | Tatsumaki | Psychic | #10 The Chronos Master | #2 | Infinite Eye + Precise Discipline; INT 18 staff time-control |
| 59 | Emma Frost | Psychic | #2 Puppet Master Control | #10 | Mass Suggestion + Dominate; Diamond Form fallback |

**RANGER**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 64 | Alleria Windrunner | Ranger | #8 Ghost-Wolf Hunter | #1 | Outwit wolf-pack tactics; Monster Hunter free RK + Wolf auto-trip flanking |
| 65 | Sylvanas Windrunner | Ranger | #3 Archer Sniper | #1 | Black Arrow kill-convert; Wailing Arrow fear burst |

**ROGUE**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 69 | Imoen | Rogue | #5 Opportunistic Thief | #3 | Halfling thief roots; Trap Finder + Gang Up + Dread Striker + Precise Debilitations |
| 70 | Yor Briar (Yor Forger) | Rogue | #3 Mastermind Precision + Investigator | #2 | Recall Knowledge = Flat-footed; deliberate precision |

**SORCERER**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 72 | Rachel Roth (Raven) | Sorcerer | #4 Shadow Control | #1 | Diabolic shadow bloodline; darkness + debuff king |
| 73 | Ultimecia | Sorcerer | #7 Aberrant Support | #5 | Hag bloodline; mind control + time-compression crowd control |

**SUMMONER**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 74 | Salem | Summoner | #5 Pure Eidolon Striker | #8 | Grimm Phantom charges first; aggressive max evolutions |
| 75 | Yuna | Summoner | #8 Phantom Support | #5 | Devotion Aeon summons + party heals between actions |

**SWASHBUCKLER**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 76 | Isabella Valentine (Ivy Valentine) | Swashbuckler | #9 Battledancer Aura | #2 | Serpentine reach Panache; Performance pulse |
| 77 | Isabela | Swashbuckler | #9 Battledancer Aura | #8 | Daggers + dance; Battledancer Aura every round |

**THAUMATURGE**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 78 | Ryuko Matoi | Thaumaturge | #1 Regalia Thaumaturge | #6 | Senketsu Regalia primary; Whip reach + CHA 18 implement focus |
| 79 | Nui Harime | Thaumaturge | #3 Cursed Saboteur | #6 | Mirror + Effigy + Bell; Cursed Effigy debuff loop |

**WITCH**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 82 | Medusa Gorgon | Witch | #5 Pure Hex Debuff | #8 | Death Patron; snake-hair multi-target hex stacking |
| 83 | Morrigan | Witch | #9 Hex-Bound Shepherd | #8 | Resentment patron + Changeling; Raven familiar + Enfeeblement chain |

**WIZARD**
| # | Companion | Class | ★ Preset | ⚠️ Avoid | Reason |
|---|-----------|-------|----------|----------|--------|
| 87 | Megumin | Wizard | #1 Spellbook Blaster + Psychic | #10 | Evoker; Heightened Fireball max slot — nothing else |
| 88 | Liliana Vess | Wizard | #2 School Specialist + Magus | #4 | Necromancy specialist; Animate Dead army economy |

---

## 📊 COMPANION CLASS REFERENCE

> **DM:** Look up companion's class here, then open their build file from KM_Builds.md. Presets 1–6 use the A-file; presets 7–10 use the B-file.

### KM CRPG
| # | Companion | Class | Build File (1–6 / 7–10) |
|---|-----------|-------|--------------------------|
| 1 | Jubilost | Alchemist | KM_Builds_A.md / _A2.md / _A5.md |
| 6 | Amiri | Barbarian | KM_Builds_B.md / _B2.md |
| ✦ | Linzi | Bard | KM_Builds_B4.md / _B3.md |
| 16 | Tristian | Cleric | KM_Builds_C4.md / _C3.md |
| 32 | Valerie | Fighter | KM_Builds_E2.md / _E4.md |
| 45 | Kalikke/Kanerah | Kineticist | KM_Builds_G3.md / _G4.md |
| 60 | Ekundayo | Ranger | KM_Builds_I3.md / _I6.md |
| 66 | Nok-Nok | Rogue | KM_Builds_J2.md / _J3.md |
| 84 | Octavia | Wizard | KM_Builds_M.md / _M2.md |
| 18 | Jaethal | Cleric | KM_Builds_C4.md / _C3.md |
| 20 | Harrim | Cleric | KM_Builds_C4.md / _C3.md |
| 48 | Regongar | Magus | KM_Builds_H.md / _H2.md |

### WotR CRPG
| # | Companion | Class | Build File (1–6 / 7–10) |
|---|-----------|-------|--------------------------|
| 23 | Regill | Commander | KM_Builds_D.md / _D2.md |
| 51 | Lann | Monk | KM_Builds_H3.md / _H4.md |
| 55 | Daeran | Oracle | KM_Builds_I.md / _I2.md |
| 61 | Arueshalae | Ranger | KM_Builds_I3.md / _I6.md |
| 80 | Ember | Witch | KM_Builds_L4.md / _L2.md |
| 85 | Nenio | Wizard | KM_Builds_M.md / _M2.md |
| 81 | Camellia | Witch | KM_Builds_L4.md / _L2.md |
| 33 | Wenduag | Fighter | KM_Builds_E2.md / _E4.md |
| 67 | Woljif | Rogue | KM_Builds_J2.md / _J3.md |
| 17 | Sosiel | Cleric | KM_Builds_C4.md / _C3.md |
| 62 | Greybor | Ranger | KM_Builds_I3.md / _I6.md |
| 26 | Ulbrig | Druid | KM_Builds_D4.md / _D3.md |
| 7 | Trever | Barbarian | KM_Builds_B.md / _B2.md |
| 13 | Seelah | Champion | KM_Builds_C.md / _C2.md |

### PF2e Iconics
| # | Companion | Class | Build File (1–6 / 7–10) |
|---|-----------|-------|--------------------------|
| 34 | Valeros | Fighter | KM_Builds_E2.md / _E4.md |
| 19 | Kyra | Cleric | KM_Builds_C4.md / _C3.md |
| 71 | Seoni | Sorcerer | KM_Builds_J.md / _J4.md |
| 86 | Ezren | Wizard | KM_Builds_M.md / _M2.md |
| 52 | Sajan | Monk | KM_Builds_H3.md / _H4.md |
| 27 | Lini | Druid | KM_Builds_D4.md / _D3.md |
| 63 | Harsk | Ranger | KM_Builds_I3.md / _I6.md |
| 10 | Lem | Bard | KM_Builds_B4.md / _B3.md |
| 68 | Merisiel | Rogue | KM_Builds_J2.md / _J3.md |

### Section D Cross-IP
> All Section D companions use standard class build files. Look up the companion's class above, then route via the class mapping in KM_Builds.md. The complete class → file routing table is in that router file.

---

## 💾 SAVE BLOCK FORMAT

```json
"companions": [
  {
    "name": "Linzi",
    "class": "Bard",
    "preset": 1,
    "preset_name": "Virtuoso Maestro",
    "build_file": "KM_Builds_B4.md",
    "relationship": 0
  }
]
```

---

*KM_Companions_Builds.md — Preset Mapping v9.1 | Presets from KM_BuildGuide_A/B.md | 89 companions (12 KM · 14 WotR · 9 PF2e · 54 Cross-IP)*
