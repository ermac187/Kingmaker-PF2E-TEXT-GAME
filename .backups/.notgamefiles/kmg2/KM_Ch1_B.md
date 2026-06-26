# KINGMAKER — CHAPTER 1: STOLEN LAND (PART B)
## KM_Ch1_B.md | Pair-load with KM_Ch1.md
## Covers Phases 7–8 + XP Summary + Resolution Paths.

> **DM:** This is Part B of Chapter 1. Always pair-load with `KM_Ch1.md` (Part A covers the load checklist, overview, opening scene, and Phases 1–6: Oleg's, the bandit encounter, exploration, the Tomb, Thorn Ford, the Technic League encampment, Old Sycamore, and the Temple of the Elk).

---

## 📍 PHASE 7 — THE STAG LORD'S FORT

### Pre-Assault Preparation

**Available approaches (see KM_Map.md for full fort detail):**

```
A. Direct assault              — Hard. Full garrison alert from round 1.
B. Kressle's password          — Reduces garrison by 2, patrol timing known.
                                  Requires: Kressle fought + retrieved info from her camp.
C. Disguise as bandits         — Deception DC 16. Fails if Stag Lord sees player directly.
D. Basement/sewer entry        — Thievery DC 14 to locate hidden entry. Bypasses main gate.
E. Akiros opens a gate         — Requires akiros_turned = TRUE from Thorn Ford visit.
                                  He opens the east gate at midnight on Day [X].
F. Kressle's crew assists      — Requires [Good] resolution at Thorn Ford.
                                  Her bandits attack from outside while player goes in.
```

**Fort Layout:**
```
╔══════════════════════════════════════════════╗
║  STAG LORD'S FORT                            ║
╠══════════════════════════════════════════════╣
║  [Watch Tower]  [Watch Tower]                ║
║  N Gate ──────────────────────               ║
║  │  [Barracks]  [Barracks]  [Main Hall]  │   ║
║  │  Bandits ×6  Bandits ×4  Dovan+Auchs  │   ║
║  │                                       │   ║
║  │  [Stag Lord's Tower — top floor]      │   ║
║  │  [Basement — Nugrah's Prison]         │   ║
║  E Gate ──── (Akiros if turned) ─────────    ║
╚══════════════════════════════════════════════╝
```

**Key NPCs:**

**DOVAN (Rogue 5 — sadistic lieutenant):**
```
HP: 48 | AC: 20 | Speed: 30 ft
Daggers ×2: d20+10/+6 (1d4+5 P, Agile) — Sneak Attack +3d6
Cannot be talked down. Will not surrender. Fight or die.
```

**AUCHS (Fighter 4 — dimwitted brute):**
```
HP: 60 | AC: 17 (Chain Shirt) | Greatclub: d20+10 (2d6+8 B)
Special: Can be turned against Dovan.
  Diplomacy DC 14 if approached alone: "Dovan hurts people for fun. I don't like it."
  If turned: Fights Dovan during the assault. Player gains +ally for that fight.
```

**AKIROS ISMORT (Fighter 5 — fallen paladin):**
```
HP: 66 | AC: 22 (Full Plate) | Longsword: d20+10 (1d8+5 S)
If akiros_turned = TRUE: He does not fight the player. Joins assault on Stag Lord.
If NOT turned: He fights the player unless [Lore Religion DC 18] or [Diplomacy DC 23].
```

**NUGRAH (basement — Stag Lord's imprisoned father):**
```
Old druid, mad from years of imprisonment. Not hostile by default.
Releasing him: Diplomacy DC 12 to calm him. He gives a blessing (+1 to all saves, 1 day).
Leaving him: He escapes later on his own. No consequence.
XP for releasing: +25
```

### THE STAG LORD

```
THE STAG LORD — Ranger 7 (Outwit Hunter)
HP: 94 | AC: 21 (Leather Armor +2 + Dex) | Speed: 30 ft
Fort +12 | Ref +14 | Will +9

WEAPONS:
  Composite Longbow +2: d20+16 (1d8+7 P, range 100 ft) — his primary weapon
    Rapid Shot: Two arrows per action, each at −2 to hit
  Shortsword: d20+11 (1d6+5 P) — backup if engaged in melee

SPECIAL ABILITIES:
  Hunt Prey: Designate 1 target — +2 to Perception vs target, ignore first MAP penalty
  Masterful Hunter: +2d8 damage vs Hunted Prey
  Drunk but Deadly: If not surprised, −2 to Will saves but +2 to damage (ale in system)
  Stag's Helm: +2 to Intimidation, Fear aura 10 ft (Will DC 16 or Frightened 1)

TACTICS:
  Round 1: Hunt Prey on player character → Triple attack (Longbow −2/−7/−12)
  Round 2: Maintain range. Use difficult terrain. Shout for reinforcements if any remain.
  Round 3+: Switch to melee if cornered. His shortsword is his worst weapon — this is his mistake.

DEFEAT CONDITIONS:
  Reduced to 0 HP → unconscious (not dead)
  Hero Point? No — he's an enemy. He stays down.

DISPOSAL OPTIONS (see KM.txt Game Options):
  Kill immediately     : Standard
  Behead + send head   : +75 gp reward from Jamandi, Aldori commendation
  Capture + imprison   : Interrogation possible (reveals Nyrissa's early influence — +lore)
  Turn over to Kesten  : He arrives in 1d4 days
  Execute publicly     : +5 Loyalty to future kingdom, alignment flag (+Evil tendency)

XP: 600 (boss encounter)
```

**FORT LOOT (collect before leaving):**
```
From Stag Lord     : Stag Lord's Helm, Composite Longbow +2, +1 Leather Armor
                     Potion of Cure Moderate Wounds ×3, 230 gp
                     Letter from Nyrissa (story item — first contact, keep this)
From Dovan         : Daggers +1 ×2, 85 gp
From Akiros (if killed): Full Plate +1, Longsword +1
Fort treasury      : 340 gp (Stag Lord's accumulated tribute)
Secret room        : Thievery DC 16 — Headband of Inspired Wisdom +2, 95 gp
```

> ⚠️ **DM: Remind player to collect all loot before triggering the "victory" scene. Cannot return.**

---

## 📍 PHASE 8 — RETURN TO OLEG'S & KINGDOM FOUNDING

### Victory Scene

> *The Stag Lord is [dead/captured/beheaded]. The fort is yours. The Stolen Lands are — technically — clear.*
>
> *Linzi (or whoever is in party) opens her notebook.*
> **Linzi:** *"Chapter [X]: 'The Stag Lord Falls.' Has a good ring to it."*
> **Amiri:** *"Acceptable. I've fought better. But acceptable."*

**Nettle's Crossing (if applicable):**
If player has the Stag Lord's head/body, travel to Nettle's Crossing on the way back.
Davik Nettles' ghost accepts the offered remains → reward: **Ranseur +1** (1d10+5 S/P, Reach 10 ft, Trip, +1 item bonus to attack and damage), +50 XP.

### Bokken's Hut (optional search, Hex (-1,1))
Searchable if relationship positive (Fangberries/Radishes delivered).
```
Bokken's Hut (Perc DC 14, he's outside during day):
  Shelf: Antiplague, Oil of Potency (+1 spell DC, 1d4 charges)
  Cabinet (Thiev DC 15): Potion of Darkvision, 28 gp, Scroll of Grease
  Caught searching: −1 Bokken, full price permanent, no Fangberry discount
```

### Abandoned Hut (random exploration, Plains hexes)
```
Plains hex, Perc DC 12 during travel. Interior (Perc DC 14):
  Floorboard: 32 gp, Healer's Kit (10 uses), Masterwork Dagger (1d4+Str P, Agile)
  Back room       : Rotted bedroll, Torn Journal (lore — former settler, not mechanical)
  Trap (Thievery DC 13 to spot): Tripwire attached to crossbow. Reflex DC 14 or 1d8+3 P damage.
```

### At Oleg's — Kingdom Founding

**Kesten Garess and Jhod Kavken are both present.**

> *A messenger from Restov arrived two days ago. He left a sealed document and a note that says: "When you're ready."*

The sealed document is Jamandi's official Kingdom Charter. Opening it begins the Kingdom Founding sequence.

**Capital Selection:** Player chooses from 3 options (see KM_Map.md — Capital section). Record `capital_location` in Export Block.

**First Kingdom Turn:** Happens immediately after capital is founded. See KM_Kingdom.md.

**Seeker recruitment (Tartuccio's team):**
If seekers from Tartuccio's team have not yet been flipped, they can be recruited at Oleg's post-founding. They left Tartuccio after his behavior in the Stolen Lands. Level matches player per KM_Malak_Jail.md.

---

## 📊 CHAPTER 1 — XP SUMMARY

| Source | XP |
|--------|----|
| Thylacine ambush (3) | 90 |
| Bandit raid at Oleg's | 150 |
| Remus encounter | 20 |
| Ancient Tomb — mercenaries (4) | 180 |
| Ancient Tomb — storybook tracking | 55 |
| Thorn Ford — Kressle + bandits | 200 |
| Temple of the Elk — bear + frogs | 380 |
| Old Sycamore — mites/kobolds | 320 |
| Tartuccio confrontation (Ch1) | 240 |
| A Bitter Rival completion | 480 |
| Stag Lord's Fort — Dovan + Auchs | 280 |
| Stag Lord (boss) | 600 |
| Falgrim Sneeg (capture) | 150 |
| Lonely Warrior (resolved) | 150 |
| Side quests (Fangberry, Radishes, etc.) | ~150 |
| Exploration discoveries | ~200 |
| **Total (full completion)** | **~3,645 XP** |
| **Minimum (main quests only)** | **~2,100 XP** |

**Level benchmarks:** L2 at 1,000 | L3 at 2,000 | L4 at 3,000 | L5 at 4,000 (per KM_Leveling.md)

---

## 🔀 CHAPTER 1 RESOLUTION PATHS

### PATH A — SWIFT CONQUEST (under 30 days)
Mainline only. No diversions. Reward: Lord Protector (+2 Dueling Sword, Finesse) from Jamandi. Consequence: side quests incomplete, may be Level 3 only at chapter end.

### PATH B — FULL EXPLORATION (30–60 days)
All named hexes cleared, all Ch1 quests complete. Level 4 at chapter end. Best starting position for Ch2.

### PATH C — DIPLOMATIC RESOLUTION
Kressle turned, Akiros recruited, Sootscale allied, fey approached peacefully. Reward: +2 Stability to starting kingdom, Akiros available as Warden advisor.

### PATH D — MILITARY DOMINATION
Kressle killed, Akiros fought, kobolds wiped out, fey glade forcibly claimed. −Stability, +Economy. Jaethal approves. Valerie disapproves.

### PATH E — STAG LORD CAPTURED
Interrogation confirms Nyrissa's letter as real. `nyrissa_early_contact = TRUE`. Player decides his fate (Kesten, execute, imprison).

---

> **⚠️ DM: Chapter 1 ends when the player returns to Oleg's Trading Post after defeating the Stag Lord AND triggers the Kingdom Founding sequence. Output the Ch1 Export Block at this point.**

---

*KM_Ch1_B.md — Kingmaker PF2e Text Adventure | Ch1 Part B v1.0*
