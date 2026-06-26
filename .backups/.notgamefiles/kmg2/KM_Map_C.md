# KINGMAKER — CAMPAIGN MAP & HEX SYSTEM (PART C)
## KM_Map_C.md | Pair-load with KM_Map.md (and KM_Map_B.md as needed)
## Covers Chapter 2–7 named-location hex details.

> **DM:** Part C of the campaign map. Contains hex-by-hex location detail for Chapters 2 through 7. Pair with `KM_Map.md` (hex system, world map, Ch1 master index, capital selection, hex tracking JSON) and `KM_Map_B.md` (zone reference + exploration flags).

---

## 📍 CHAPTER 2 LOCATIONS (Narlmarches & Kamelands)

**HEX (4,-2) — SECLUDED LODGE** `⊕` | Status: UNEXPLORED
```
NPC     : Bartholomew Delbin (wizard, eccentric, friendly if not startled)
Quest   : Nature of the Beast — study troll regeneration weakness
Approach: Diplomacy DC 12 or knock before entering (he's paranoid)
Reward  : Potion of Fire Breath ×3 (50 gp each), Scroll of Burning Hands ×4,
          `troll_weakness_known = TRUE` — party gains +2 to attacks vs trolls
THREAT  : None — unless player is hostile
```

**HEX (-3,-2) — VERDANT CHAMBERS** `♣` | Status: UNEXPLORED
```
NPC     : Tiressia (Woodling Nymph, requires solo visit)
Trigger : Only accessible if tiressia_met = TRUE from Ch1 glade
Storybook: 3 pages. Guardian of the Bloom appears. Tristian's role revealed.
          `tristian_bloom_seeds_revealed = TRUE`
THREAT  : 3 monsters (Hydra, Manticore, Owlbear) — can be bypassed
```

**HEX (3,-3) — RUINED WATCHTOWER** `⟲` | Status: UNEXPLORED
```
NPC     : Ekundayo (taciturn ranger) + Trkaa (dog companion)
Recruit : Automatic if player agrees to help find Kargadd
Quest   : A Score to Settle — Kargadd is in Trobold Level 2
LOOT    : Masterwork Composite Longbow (in tower rubble, Perception DC 16)
```

**HEX (2,-4) — TROBOLD (DWARVEN RUINS)** `✗` | Status: HOSTILE (Ch2)
```
2-level dungeon. Troll kingdom. Hargulka's throne on Level 2.
Supply check: ensure fire/acid before entering (warn player if none)
Level 1: Sentinels ×4, Trollhounds ×6, Troll Shaman — see KM_Ch2.md
Level 2: Kargadd, Branded Trolls, Hargulka + Tartuccio
Key items: Trollreaper (fire-damage club), Iron Dwarven Key (opens deep vault)
Flags: `trobold_cleared`, `hargulka_fate`, `kargadd_killed`, `ekundayo_quest`
```

**HEX (-1,-3) — GOBLIN VILLAGE** `⊕` | Status: UNEXPLORED
```
Nok-Nok's former tribe. Bloom-corrupted elder controls them.
Approach : Diplomacy DC 14 (Nok-Nok in party: automatic peaceful entry)
Resolution: Kill the elder (Bloom recedes, goblins scatter) or
            Diplomacy DC 16 (cure elder via magic — requires Heal spell)
Quest link: Nok-Nok personal quest trigger if he's recruited
```

**HEX (1,-4) — BALD HILLTOP** `✦` | Status: UNEXPLORED
```
Barren hill with dead tree and stone circle — seat of the Ancient Curse.
Part 1: Wyvern ×2 (CR 7) guard the hill. Arcana DC 14 reveals seed point.
        Reward: 2,800 gp if cleared before Part 1 deadline.
Part 2: Bloom Manifestation boss (HP 140, fire weakness). Purify option available.
        Reward: 6,500 gp + 900 XP. `bloom_resolved = TRUE`
Flags: `bald_hilltop_p1_cleared`, `bald_hilltop_p2_cleared`, `bald_hilltop_resolution`
```

---

## 📍 CHAPTER 3 LOCATIONS (Varnhold Region)

**HEX (6,2) — VARNHOLD** `★` | Status: DISCOVERED (Ch3 opening)
```
Empty city. 300 vanished. Spriggans moved in.
Spriggan leader Agai: negotiate (Diplomacy DC 14) or fight.
Key items: Two story letters (one ends mid-word: "VORDAKAI"), Wand of Displacement
The Raven: appears here, confirms Vordakai's responsibility.
`varnhold_investigated`, `vordakai_identity_known`, `agai_fate`
```

**HEX (5,3) — OVERGROWN CAVERN** `⊕` | Status: UNEXPLORED (Ch3)
```
Defaced Sisters ×3 (cursed barbarian women, HP 44 each, AC 17)
Each carries one Cyclops Incense Burner — all 3 needed for Valley of the Dead.
With Amiri: non-hostile entry possible.
Without: full combat or Athletics DC 20 to impress them first.
```

**HEX (7,3) — KELLID BARBARIAN CAMP** `⚔` | Status: UNEXPLORED (Ch3)
```
NPC     : Dugath (camp leader)
Approach: Amiri = auto-peaceful. Diplomacy DC 21 or Athletics DC 20 otherwise.
Password for Sepulcher: "kheb" (Dugath tells player if relationship is good)
Sepulcher: Zombie Cyclops ×2 inside. Loot: Harbinger (earth breaker, deals double
           damage vs undead — crucial for Vordakai). Ancient Cyclops Coins ×2.
`kellid_friendly` based on approach
```

**HEX (8,4) — VALLEY OF THE DEAD** `▒` | Status: LOCKED (Ch3)
```
Requires all 3 Cyclops Incense Burners to open the gate.
Point of no return. Cannot exit until Vordakai is defeated.
Supply check: Death Ward scrolls, Lesser Restoration ×4, fire/positive energy sources.
Vordakai's Tomb: 2 levels, Willas Gunderson specter, Varnhold regent soul jar.
See KM_Ch3.md for full walkthrough.
`valley_entered`, `vordakai_fate`, `varnhold_regent_saved`
```

---

## 📍 CHAPTER 4–5 LOCATIONS (Glenebon & Pitax)

**HEX (0,5) — NUMERIAN STEPPES (Tiger Lord Territory)** `░`
```
Barbarian lands. Tiger Lord camp is the central location.
Approach: Amiri = less hostile. Diplomacy DC 28 to enter peacefully.
NPC     : Gwart (Tiger Lord dissident, can guide party)
Amiri's solo mission triggers here — she infiltrates to find Nilak.
`tiger_lord_hostile` until Ch4 resolved. `nilak_fate` set here.
```

**HEX (-2,4) — ARMAG'S TOMB** `⟲` | Status: UNEXPLORED (Ch4)
```
Entrance guardian: Zorek (Cleric 10 of Gorum) — see KM_Ch4.md for stats
Trial of Strength (DC 35 Athletics) and Trial of Pain (trap corridor, DC 30 Perception)
Two levels: Spectres, Dread Zombies, Greater Skeletons
Boss: Armag the Twice-Born (HP 220, Bastard Sword +5) — see KM_Ch4.md
Post-boss: Tiger Lord Chief selection. `armag_tomb_cleared`, `armag_fate`
```

**HEX (-4,2) — PITAX** `★` | Status: HOSTILE until Ch5
```
Irovetti's capital city. Academy of Grand Arts. Palace.
Military path: siege warfare, army combat, Brineheart first
Infiltration: sewers (Athletics DC 16), noble disguise (Deception DC 24),
              servant disguise (Deception DC 18)
Key NPCs: Irovetti (boss), Linxia (captain, defectable DC 28), Darven (merchant)
Loot: 8,400 gp vault, Ring of the Archmagi, Headband of Mental Perfection +4
`pitax_conquered`, `irovetti_fate`, `linxia_fate`
```

**HEX (-5,1) — BRINEHEART FORTRESS** `⚔` | Status: HOSTILE (Ch5)
```
First major Ch5 military engagement.
Fort: AC 22, HP 120, garrison of 8 soldiers + Linxia
Army assault OR player party direct assault (Athletics DC 16 to scale walls)
Linxia: Diplomacy DC 28 to defect (surrenders fort, +25,000 gp reward)
`brineheart_taken`, `linxia_fate`
```

---

## 📍 CHAPTER 6–7 LOCATIONS (Thousandbreaths & Beyond)

**HEX (0,-6) — THOUSANDBREATHS PORTAL** `◆` | Status: HIDDEN (Ch6)
```
Found in deep Narlmarches after Bloom reaches full manifestation.
Perception DC 22 to locate the portal (or follow Bloom corruption trail)
Entry: requires player to have entered Thousandbreaths consciously — no accident
`thousandbreaths_portal_found`
```

**THOUSANDBREATHS (Pocket Dimension)** `◆`
```
Nyrissa's domain. Not on the normal hex grid.
Dim light throughout (Low-light vision helps). Time distortion: Fatigued check every 2 rooms.
Enemies: Bloom Guardians, Nyrissa's Archers, Verdant Nightmare (boss room)
        See KM_Bestiary.md for stat blocks.
Linzi's death scene occurs at end of Phase 3 (before Nyrissa's chamber).
Linzi save option: if 4 conditions met, special dialogue available.
See KM_Linzi_Shrine.md if shrine quest is active.
```

**HOUSE AT THE EDGE OF TIME (Extradimensional)** `★`
```
Nyrissa's true domain. Accessible only at Ch7 climax.
POINT OF NO RETURN. Companion quest audit required before entry.
Time overlaps: rooms show past/present kingdom simultaneously.
Bad ending: defeat Nyrissa without the dialogue. Lantern King wins.
See KM_Ch4.md Ch7 section for full content.
```

---

*KM_Map_C.md — Kingmaker PF2e Text Adventure | Campaign Map Part C v1.0 (Ch2–7 location detail)*
