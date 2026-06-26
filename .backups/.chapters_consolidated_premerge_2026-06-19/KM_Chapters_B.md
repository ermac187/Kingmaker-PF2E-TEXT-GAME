# KINGMAKER — CHAPTERS 3–7 (CONSOLIDATED, PART B)
## KM_Chapters_B.md | Split from KM_Chapters.md (v95.9 file-size remediation, 2026-05-29)
## Contains: Ch3 Varnhold Vanishing + Ch4–7 + Linzi Shrine of Returning
## KM_Chapters.md holds Ch1 (Stolen Land) + Ch2 (Troll Trouble / Bloom).

<!-- merged from KM_Ch3.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 3: THE VARNHOLD VANISHING
## KM_Ch3.md | Loads after: KM_Ch2_P2.md export | Loads before: KM_Ch4.md

---

> **DM:** Load with KM.txt, KM_Companions.md, KM_Companions.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md, KM_BuildGuide.md.
> Import Ch2 Export Block. Ch3 is shorter than Ch2 but the final dungeon is brutal — warn player to stock supplies before entering Vordakai's Tomb.
> EARLY REVEAL: Vordakai is responsible. The raven confirms it mid-chapter. Player learns this early.

---

## 📋 CH3 LOAD CHECKLIST

```
[GM CHAPTER 3 LOAD CHECK]
□ All files loaded
□ Ch2 Export Block imported and parsed
□ Key flags read:
    tristian_decision       : forgiven / condemned / absent
    tristian_betrayal_revealed : TRUE
    bloom_resolved          : TRUE
    hargulka_fate           : [value]
    ekundayo_recruited      : [TRUE/FALSE]
    nyrissa_awareness       : passive / active
    nyrissa_bloom_connection_known : [TRUE/FALSE]
    tartuccio_ch2_fate      : fled_to_varnhold_region
□ Kingdom state confirmed — turn count, stats, armies
□ Companion roster confirmed
□ Note: Tristian rejoins if condemned — separate encounter triggers this chapter
□ Game State Header output, then begin
```

---

## 🗺️ CHAPTER 3 OVERVIEW

**Levels:** 8 → 12
**Duration:** ~150 days before the kingdom stability check fails
**Tone:** Horror mystery. An entire settlement has vanished. Nobody knows why.
**New region:** Varnhold area, Numerian steppes, Valley of the Dead

**Main questline:** The Varnhold Vanishing
- Investigate the empty city
- Track the trail to the Kellid barbarian camp
- Navigate the Valley of the Dead
- Enter and clear Vordakai's Tomb (point of no return)
- Confront Vordakai — the cyclopean lich

**Parallel content:**
- Amiri's personal quest trigger (Pariah) — 135 days before chapter deadline
- Tristian re-recruitment (if condemned in Ch2)
- Companion quests for Harrim, Jaethal can be progressed here
- Guardian of the Bloom appears again — first real conversation with Nyrissa's servant

---

## 🚀 OPENING — THE MESSAGE

### Throne Room Event

> *The Councilor sets a letter on your desk. The seal is Jamandi's.*
>
> **Councilor:** *"Varnhold has gone silent. Its regent hasn't sent the weekly report in three weeks. Jamandi wants to know what happened."*

> *The letter is two sentences: "Varnhold is not responding. Find out why."*

**Player reactions affect alignment:**
- "I'll go immediately" → [Lawful] flag
- "Send a scout first" → [Neutral] — 3-day delay, scout returns with nothing
- "Why is this my problem?" → [Chaotic] — Jamandi's relationship -1 if used, but quest is still mandatory

**Guardian of the Bloom encounter** (before leaving capital):

> *You step out of the throne room into the courtyard. Except it isn't the courtyard.*
>
> *Stone. No sky. A woman stands in the center of a space that has no walls.*
>
> **Guardian:** *"You're going to Varnhold. Good. My mistress wants you to see what happens when something older than her takes an interest in your little kingdom."*

She disappears. Back in the courtyard. `guardian_first_contact = TRUE`

**Early reveal:** The raven — Vordakai's messenger — will confirm its master's role within the first visit to Varnhold. The mystery is not "who did it" but "what is Vordakai and how do you stop him."

---

## 📍 PHASE 1 — INVESTIGATING VARNHOLD

### Travel to Varnhold

New region unlocked. Mountains — 3 days per hex unless Expert Mountaineering project done (halves mountain travel).

**Barbarian Hunting Party (random encounter en route):**
A group of Kellid barbarians led by Nober.
- With Amiri in party: they are friendly from the start (she is Kellid)
- Without Amiri: Diplomacy DC 19 (or be a human/orc — no check needed)
- Hidden Perception DC 21 or Tristian in party: notice sick woman → heal her → `ashman_likes_us +1`
- `kellid_friendly = TRUE` if resolved peacefully — opens Kellid camp without hostility

---

### Varnhold — The Empty City

```
[GM SCENE BRIEF — Varnhold]
ATMOSPHERE : A town that should have 300 people has zero. Fires burned out 2–3 weeks ago.
             Food left on tables. Livestock dead in pens. No bodies. No blood.
             Two murder of crows occupy the eastern side of town. They watch you.
ENEMIES    : Spriggans (fey, hostile) — they moved in after the disappearance
             Spriggan Warrior ×6: HP 36 | AC 17 | Spear d20+8 (1d6+5, Reach 10 ft)
             Spriggan Shaman ×2: HP 28 | AC 14 | Spells: Bane, Fear
LOOT       : Wand of Displacement (south room), Ancient Rostlandic Coin (tavern crate),
             Two letters (story items — CRITICAL):
               Letter 1: Wilas Gunderson found a strange amulet. Ends mid-sentence:
                         "VORDAKAI VORDAKAI VORDAKAI"
               Letter 2: To Varnhold's regent, warning them not to ally with the player.
                         (unsigned — Pitax or Tartuccio handwriting if Perception DC 18)
XP         : 640 (spriggans)
[END BRIEF]
```

**The Raven:**
> *A crow lands on a fence post and turns one eye toward you.*
> *"VORDAKAI VORDAKAI," it says. And then: "My master is aware of you. My master is the reason this city is empty. You are walking toward him."*

`vordakai_identity_known = TRUE`
XP: +100 for this discovery

**Spriggans and Agai:**
Agai — the spriggan leader — is upstairs in the stockade.
```
AGAI — Spriggan Champion (Fighter 5)
HP: 52 | AC: 19 | Spear: d20+11 (1d6+8 P, Reach 10 ft)
Fort +9 | Ref +5 | Will +3

Approach options:
[Lawful] Claim authority as the Baron/Baroness:
  → Diplomacy DC 14 to make him recognize your right to the land
  → He tells you about Overgrown Cavern location without fighting
  → `agai_talked = TRUE` — spriggans can eventually return to their home
[Attack] → Fight. He's dangerous. Focus fire.
After defeat/surrender: reveals Overgrown Cavern
```

**Spriggan Resolution:**
- Kill all → `spriggans_killed = TRUE`
- [Lawful] negotiate return of their cave → `spriggans_given_home = TRUE` — minor Culture bonus later

---

## 📍 PHASE 2 — OVERGROWN CAVERN & KELLID CAMP

### Overgrown Cavern

The cavern Agai was driven from. Kellid barbarian women (the Defaced Sisters) are using it.

```
[GM SCENE BRIEF — Overgrown Cavern]
ENEMIES    : Defaced Sisters ×3 (barbarian women, cursed by Vordakai)
             Each: HP 44 | AC 17 | Greataxe d20+10 (1d12+7)
             CURSED: Each Sister carries one Cyclops Incense Burner (need all 3)
OBJECTIVES : Collect all 3 Cyclops Incense Burners from the Sisters
             These are the keys to the Valley of the Dead
RESOLUTION : Kill all Sisters → 3 burners, +420 XP
             Shame/defeat then release them → they return to camp, still have burners
             (must get burners at camp — risky encounter there)
WITH AMIRI : Barbarians inside are initially non-hostile. Easier resolution.
[END BRIEF]
```

---

### Kellid Barbarian Camp (Sepulcher area)

**Book event on arrival:**

```
Page 1: Enter the camp. Choose approach.
  → [Copy Amiri's lead] — if Amiri present — automatic peaceful entry
  → Diplomacy DC 21 (+56 XP)
  → Athletics DC 20 (+45 XP — demonstrate strength)
  → Fail: barbarians hostile

Page 2: Dugath speaks.
  He reveals the Cyclops Incense Burners unlock the Valley of the Dead.
  He knows what Vordakai is: "An eye. An ancient eye that drinks souls."
  +1,380 XP

Page 3: If Sisters were released (not killed):
  They accuse you at the camp. The raven hears your name spoken aloud.
  → Vordakai now knows your name. `vordakai_knows_your_name = TRUE`
  → Minor consequence: he prepares a trap in the tomb (+1 DC on his ambush)
```

**Sepulcher of Forgotten Heroes:**
Tomb near the camp. Password: "kheb" (player can discover through Lore: History DC 14 or Dugath tells them).

```
ENEMIES    : Dread Zombie Cyclops ×2: HP 80 each | AC 18 | Slam d20+12 (2d8+9)
             Negative Energy Drain on hit: Fort DC 16 or Drained 1
LOOT       : Harbinger (earth breaker +1, silver, deals double damage vs undead — CRUCIAL)
             Eternal Conduit (scythe, +1, ghost touch)
             Ancient Cyclops Coin (Storyteller item)
XP         : 560
```

**Two Greater Cyclops (alive, arguing over treasure):**
- Diplomacy DC 18 → convince them to share → +720 XP (no fight)
- Attack → fight both (HP 90 each, AC 20, Club d20+14 2d6+10)
- Let them fight each other → 0 XP, one survives at half HP

---

## 📍 PHASE 3 — VALLEY OF THE DEAD & VORDAKAI'S TOMB

### ⚠️ POINT OF NO RETURN WARNING

> **DM:** Before the player enters the Valley of the Dead, output this warning:
> *"You are about to enter a point of no return. Once inside Vordakai's Tomb, you cannot leave until it's completed. Ensure you have: rations for 6+ rests, Death Ward spell/scrolls, Lesser Restoration ×4+, fire/positive energy damage sources, full spell slots."*

---

### Valley of the Dead — Approach

**The raven appears one final time:**
> *"You have the burners. You are walking into his home. He is ready for you. He has been ready for three thousand years."*

Three incense burners on gate hooks → dramatic entrance → Valley unlocked.

**En route encounters:**
```
Ancient Cemetery — Zombie Cyclops ×4, Dread Zombie Priest ×1
  HP: 65–80 each | Negative Energy attacks | XP: 720
  LOOT: Padded Armor +3, Fallen Warrior's Buckle (Relic Fragment 2/5)
  Knowledge (World) DC 17 on pillars → history of Vordakai (+45 XP each)
```

---

### Vordakai's Tomb — Level 1

```
DUNGEON RULES:
  Cannot leave once inside. Rest available (with rations). No vendors.
  Energy Drain (Drained condition) is the primary hazard throughout.
  Death Ward spell/scroll prevents Drained from attacks. Bring multiples.

LEVEL 1 ENEMIES:
  Zombie Cyclops ×8 (in groups): HP 65 | AC 16 | Slam d20+10 (2d6+8) | Energy Drain
  Zombie Wizard (unnamed): HP 72 | AC 16 | Mirror Image | Enervation (Drained 2)
                            Summons zombie horde when engaged — pull him carefully
  Poisonous Hydra ×2 (water room): HP 95 | AC 17 | Multiple Bite attacks | Poison Fort DC 16
  
PUZZLE ELEMENTS:
  Green/yellow/red switches control locked doors
  Password "kheb" opens inner sanctum
  Athletics DC 18 to cross collapsed bridge (or go around — 2 extra rooms)

LOOT:
  Dark Acolyte's Robe (Occultism +2 item bonus)
  Ancient Cyclops Coin ×2 (Storyteller items)
  Scroll of Greater Restoration ×2
  Ring of Protection +3
  580 gp in scattered containers
```

---

### Vordakai's Tomb — Level 2

```
WILLAS GUNDERSON (Specter — the ghost of the scholar who found Vordakai's amulet):
  HP: 58 | AC: 18 (incorporeal — needs magic weapons) | Energy Drain touch
  He surrenders when below 20 HP.

  INTERROGATION (exhaust all options for XP):
    What happened to Varnhold? → Their souls are in jars. Vordakai is harvesting them.
    What is Vordakai? → Ancient cyclopean lich. Chosen of the Four Horsemen. 3000+ years old.
    The amulet? → Oculus of Abaddon. Allows Vordakai to steal souls on sight.
    Willas's role? → He found the amulet. Brought it to Varnhold. Everyone looked at it.

  MORAL CHOICE:
    [Lawful Good] "I will avenge them" → +Lawful, +Good
    [Lawful Neutral] Condemn him, leave → neutral
    [Lawful Evil] Attack the weakened ghost → he is destroyed, -alignment
    [Neutral] Leave without judgment → no consequence

  XP: 480 for the encounter, +200 for full interrogation

DINING ROOM — Zombie Horde:
  Varnhold citizens, risen as zombies, feasting in a great hall.
  Tank enters alone → draws aggro → flee back to party → AoE the horde.
  Zombie Horde ×16: HP 22 each | AC 13 | Slam d20+6 (1d6+3) | slow
  XP: 380 (worth it for story impact)

VARNHOLD'S REGENT (soul jar):
  Found in the storeroom beyond Vordakai's throne.
  The soul jar is intact.
  Decision: Break the jar → regent restored, returns to Varnhold → +kingdom bonus
             Keep the jar → the soul is forfeit, Varnhold never fully recovers
             Give to Vordakai [Evil] → Vordakai gains power, player gains dark favor
```

---

### VORDAKAI — Final Boss

```
[GM SCENE BRIEF — Vordakai's Chamber]
VORDAKAI — Cyclopean Lich (Wizard 15)
HP: 180 | AC: 26 (Deflection + natural) | Speed: 30 ft
Fort +9 | Ref +9 | Will +18 (legendary will)

PHASE 1 ABILITIES:
  Finger of Death: d20+18 vs Fortitude DC 22. Fail: 12d6+22 negative energy.
                   Critical Fail: instant death (no dying condition — direct death)
  Enervation: Ranged touch d20+12. Hit → Drained 2.
  Fear Aura: Will DC 20 or Frightened 2 (30 ft radius, start of combat)
  The Raven: Flies around battlefield. On its turn: +1 Frightened to ALL targets (Will DC 18)
             Kill the raven FIRST — it compounds fear rapidly.
  Soul Cage (lair action): Once per round as free action, Vordakai can restore 20 HP
             using a soul jar. He has 3 jars. Destroying them (AC 10, HP 10 each)
             prevents this healing.

PHASE 2 (below 90 HP — Tristian intervenes):
  TRISTIAN rushes forward and steals the Oculus of Abaddon from Vordakai.
  [Player must tell Tristian to DESTROY the Oculus — not use it]
    "Destroy it, Tristian! It has to end!" → Tristian destroys it → Vordakai weakened
      → Phase 2: Vordakai loses all Soul Cage ability, Fear Aura drops
      → Tristian casts Greater Restoration on party then disappears
      → `tristian_redeemed = TRUE` (regardless of Ch2 decision — this is his true choice)
    [Say nothing / "Keep it"] → Oculus corrupts Tristian briefly → he destroys it anyway
      → Same outcome but relationship -1

PHASE 2 STATS (after Oculus destroyed):
  HP: remaining from Phase 1 | AC: 22 | Will: +12
  Loses Finger of Death, Enervation
  Gains: Desperate Arcane Barrage (3x Magic Missile as 1 action, 6d4+6 each)

RESOLUTION OPTIONS:
  Defeat Vordakai → Standard. He is destroyed (lich's phylactery is the Oculus — it was destroyed).
  [Lawful Evil] Recruit Vordakai → he swears service, becomes Magister advisor.
                `vordakai_recruited = TRUE` — locks out some endings, dark path
  Spared (impossible — Vordakai does not surrender or negotiate)

LOOT:
  Oculus of Abaddon (destroyed, but fragments = major Storyteller item)
  Ancient Cyclops Coin ×3
  Staff of the Magi (Occultism focus item, +3 spell attack)
  Belt of Physical Perfection +2
  Ring of the Dead (+2 saves vs undead)
  820 gp
XP: 1,200 (highest single XP award so far)
```

---

## 📍 PHASE 4 — AFTERMATH

### The Regent Restored (if soul jar broken)

> *A translucent figure solidifies into a haggard, grateful figure — Varnhold's regent.*
> **REGENT:** *"I remember... all of it. Every moment in that jar."*
>
> *After a long silence:* *"Your kingdom saved mine. Varnhold swears fealty to you."*

`varnhold_regent_saved = TRUE`
Varnhold becomes a vassal settlement: +3 Economy, +2 Stability to kingdom per turn.
The regent is available as Grand Diplomat advisor.

**The Regent's Account — What Varnhold Found:**
Once recovered (1–2 days rest), the regent has information and can be questioned about the weeks before the disappearance. This is optional but rewards lore and a flag.

- *"Wilas found the amulet in the riverbed east of town. He brought it back. That night — the first of them forgot their names."*
- *"The amulet is still in the tomb. Vordakai was wearing it when you fought him. If you took it — don't keep it near people who sleep."*
- **If player asks about the unsigned letter warning the regent against the player:** → Diplomacy DC 12 → confirms it arrived from Pitax. `pitax_warned_varnhold = TRUE` — useful evidence in Ch5.

`regent_questioned = TRUE` | +200 XP | the regent's gratitude unlocks one free Varnhold conscript unit for army.

---

### 🛒 VARNHOLD STOCKADE VENDOR

**Available:** After clearing Varnhold of spriggans, before entering Overgrown Cavern. The stockade has a locked supply room the spriggans hadn't opened yet.

**Thievery DC 12** to open — or the regent gives the key if saved.

| Item | Stats | Price | Notes |
|------|-------|-------|-------|
| Healing Potion (Moderate) | 3d8+10 HP | 50 gp | ×3 in stock |
| Elixir of Life (Moderate) | 5d6+12 HP + resist | 75 gp | ×2 in stock |
| Scroll of Restoration (L4) | Remove drained/enfeebled | 70 gp | ×1 |
| Scroll of Haste (L3) | +2 AC, extra Strike action | 30 gp | ×2 |
| Cold Iron Dagger | 1d4 P/S, bypasses fey DR | 4 gp | ×3 |
| Alchemist's Fire (Greater) | 3d8 fire + 3 persistent | 18 gp | ×4 |
| Antiplague (Moderate) | +2 saves vs disease 24 hr | 15 gp | ×2 |

**These are one-time purchases — Varnhold's emergency reserves. No restock.**

---

### 🔨 DRAGN — DWARVEN SMITH (POST-TROBOLD)

**Available:** Ch2 onward, after Trobold is cleared. Dragn is the kobold artist's contact — a dwarven smith who relocated to the Greenbelt after hearing about the ruins. He sets up near the capital.

**Relationship base:** Friendly (grateful the ruins are accessible again)
**Restock:** Monthly. Dwarven-craft items only — he won't touch elven work or Pitax goods.

| Item | Stats | Price | Notes |
|------|-------|-------|-------|
| Dwarven Waraxe +1 | 1d8+1 S, sweep, versatile P | 35 gp | Dwarf-made, balanced |
| Warhammer +1 | 1d8+1 B, shove | 30 gp | — |
| Full Plate (Dwarven-forged) | AC+6, ACP −2 (reduced) | 45 gp | −1 ACP vs standard |
| Adamantine Shield (Lesser) | Hardness 10, HP 40 | 160 gp | One per month |
| Dwarven Ale (restorative) | Remove Fatigued condition | 5 gp | ×6 |
| Masterwork Mining Pick | +2 Athletics (break objects) | 20 gp | — |
| Repair Kit (Dwarven) | Restore 10 Hardness to item | 8 gp | ×3 |

**Build callouts:** Builds 1/3/4 (martial): Full Plate with reduced ACP is the best non-magical heavy armor until Ch3+. Build 5 (Champion): Adamantine Shield is a priority — Shield Block becomes near-invincible.

**After Harrim's quest complete:** Dragn and Harrim have a conversation. Dragn: *"You're one of Torag's fallen. I can see it."* Harrim: *"Groetus claimed me."* Dragn: *"Then we're both honest about which god answers."* They drink. Harrim Relationship +1 if player lets it happen without interrupting.

### Tristian's Return (after leaving the tomb)

> *He is waiting outside. Just standing there.*
> **Tristian:** *"I know that doesn't fix anything. But I needed to do something that was only mine."*

He rejoins regardless of Ch2 decision. `tristian_redeemed = TRUE` overrides `tristian_condemned`.
The player may still reject him (alignment choice) but he is available.

---

## 📊 CHAPTER 3 XP SUMMARY

| Source | XP |
|--------|----|
| Varnhold (spriggans + investigation) | 840 |
| Overgrown Cavern (Defaced Sisters) | 420 |
| Kellid Barbarian Camp (book event) | 1,480 |
| Sepulcher (zombie cyclops) | 560 |
| Two Greater Cyclops (negotiate) | 720 |
| Valley approach encounters | 720 |
| Vordakai's Tomb Level 1 | 1,200 |
| Willas Gunderson + interrogation | 680 |
| Zombie dining hall | 380 |
| Vordakai (boss) | 1,200 |
| Side quests and exploration | ~600 |
| **Chapter 3 Total** | **~8,800 XP** |

**Level benchmarks:**
- Level 9: 28,000 XP — around Varnhold investigation
- Level 10: 36,000 XP — mid-tomb
- Level 11: 45,000 XP — post-Vordakai
- Level 12: 55,000 XP — after side quest completion

---

## 💾 CHAPTER 3 → CHAPTER 4 EXPORT

````json
{
  "save_version": "1.0",
  "export_from": "chapter_3",
  "import_to": "chapter_4",

  "player": {
    "name": "", "build_id": "", "class": "", "level": 0, "xp": 0,
    "attributes": {}, "hp_current": 0, "hp_max": 0, "hero_points": 1,
    "ac": 0, "saves": {}, "conditions": [], "skills": {},
    "feats": [], "spells": {}, "class_features": [],
    "inventory": { "weapons": [], "armor": [], "shields": [],
                   "magic_items": [], "consumables": [], "gear": [], "quest_items": [] },
    "gold": { "gp": 0, "sp": 0, "cp": 0 }
  },

  "companions": [
    { "name": "Amiri", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Friendly",
      "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral",
      "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral",
      "notes": "", "thread": "", "priorities": [] },
    { "name": "Ekundayo", "status": "active_party_OR_left",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "Tristian", "status": "active_party_OR_absent",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral",
      "notes": "If condemned in Ch2 and not re-recruited this chapter: absent", "thread": "", "priorities": [] }
  ],

  "kingdom": {
    "name": "", "capital_location": "", "turn": 0, "size": 0,
    "culture": 0, "economy": 0, "loyalty": 0, "stability": 0,
    "unrest": 0, "fame": 0, "infamy": 0, "treasury_rp": 0,
    "leadership_roles": {}, "settlements": [], "armies": [],
    "claimed_hexes": [], "roads": []
  },

  "story_flags": {

    "carried_from_ch2": {
      "hargulka_fate": "",
      "bloom_resolved": true,
      "bokken_relationship": "neutral",
      "tiressia_met": false,
      "nettles_crossing_resolved": false,
      "old_beldame_met": false,
      "jubilost_helped": false,
      "alignment_track": {}
    },

    "chapter_3": {
      "vordakai_fate": "",
      "oculus_destroyed": false,
      "tristian_redeemed": false,
      "varnhold_regent_saved": false,
      "varnhold_vassal": false,
      "vordakai_recruited": false,
      "kellid_friendly": false,
      "agai_fate": "",
      "spriggans_fate": "",
      "willas_gunderson_fate": "",
      "guardian_first_contact": true
    },

    "companion_quests": {
      "amiri_quest": "",
      "linzi_quest": "",
      "valerie_quest": "",
      "harrim_quest": "",
      "tristian_quest": "",
      "jaethal_quest": "",
      "octavia_quest": "",
      "regongar_quest": "",
      "noknok_quest": "",
      "lem_quest": "",
      "ekundayo_quest": "",
      "kalikke_kanerah_quest": ""
    },

    "nyrissa": {
      "nyrissa_awareness": "active",
      "nyrissa_identity_hint": false,
      "nyrissa_backstory_partial": false,
      "nyrissa_can_be_saved_hint": false,
      "nyrissa_backstory_known": false
    },

    "storyteller": {
      "fragments_delivered": 0,
      "coins_delivered": 0,
      "storyteller_collection": "incomplete",
      "nyrissa_origin_hint": false
    },

    "tartuccio": {
      "tartuccio_ch3_sighting": false,
      "tartuccio_ch3_fate": ""
    },

    "alignment_track": {
      "lawful_chaotic_axis": "neutral",
      "good_evil_axis": "neutral",
      "notable_choices": []
    },

    "relationships": {
      "jamandi": "neutral", "kassil": "neutral",
      "kesten": "neutral", "oleg": "neutral",
      "ekundayo": "neutral", "tristian": "neutral",
      "zorek": "neutral"
    },

    "npc_threads": {
      "Amiri":    { "thread": "", "priorities": [] },
      "Linzi":    { "thread": "", "priorities": [] },
      "Valerie":  { "thread": "", "priorities": [] },
      "Harrim":   { "thread": "", "priorities": [] },
      "Jaethal":  { "thread": "", "priorities": [] },
      "Tristian": { "thread": "", "priorities": [] },
      "Ekundayo": { "thread": "", "priorities": [] }
    },

    "world_state": {
      "varnhold_vanishing_resolved": true,
      "centaur_alliance": false,
      "pitax_threat_escalating": true,
      "tiger_lords_mobilizing": false,
      "public_reputation": 0,
      "reputation_tier": "UNKNOWN",
      "reputation_deeds": [],
      "reputation_notes": ""
    }
  },

  "quest_log": {
    "completed": [
      { "name": "The Varnhold Vanishing", "result": "", "xp": 0 }
    ],
    "active": [
      { "name": "Twice-Born Warlord",
        "objective": "Tiger Lord barbarians are mobilizing. Armag leads them.",
        "notes": "Chapter 4 begins with Tiger Lord raids on kingdom borders." }
    ]
  }
}
````

---

*KM_Ch3.md — Kingmaker PF2e Text Adventure | Chapter 3 v1.0*
*Source: Pathfinder Kingmaker AP (Paizo) + Owlcat Games | PF2e rules: 2e.aonprd.com*


---

<!-- merged from KM_Ch4.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTERS 4–7: WARLORD, WAR, BLOOM & FINALE
## KM_Ch4.md | Chapters 4, 5, 6, 7 Combined Reference

---

> **DM:** This file covers Chapters 4 through 7. Load alongside: KM.txt, KM_Companions.md, KM_Companions.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md, KM_BuildGuide.md. For Ch6+: also load KM_Linzi_Shrine.md. Chapter 7 contains bad ending and true ending conditions.

---

# ═══════════════════════════════════════════
# CHAPTER 4 — THE TWICE-BORN WARLORD
# ═══════════════════════════════════════════

**Levels:** 12 → 16 | **Duration:** ~120 days
**New region:** Glenebon, Numerian steppes, Tiger Lord territory

## Overview
Tiger Lord barbarians under Armag raid your kingdom borders. Irovetti of Pitax is behind them — paying Armag to destabilize your lands before Ch5. Two questlines: **Hour of Rage** (the barbarian camp assault) and **Betrayer's Flight** (Armag's Tomb). Amiri's personal quest — Blood Calling — runs through both. Optional by design.

---

## Phase 1 — Throne Room Opening

**Tiger Lord Raids** trigger as the first kingdom event of Ch4. Stability −1 each turn until resolved.

**Amiri's Quest Trigger (optional):**
If `amiri_quest` not yet complete: Amiri approaches the player in the throne room.
> **Amiri:** *"My old tribe. The Six Bears. They joined the Tiger Lords. Nilak is with them. I need to go. This isn't a request."*
`amiri_quest_triggered = TRUE`

---

## Phase 2 — Hour of Rage (Tiger Lord Camp)

**NPC: Gwart** — a Tiger Lord dissident who opposes Armag. Recruitable as guide.

```
TIGER LORD CAMP:
  Approach with Amiri → barbarians are less hostile (she is Kellid)
  Diplomacy DC 28 to enter peacefully → Gwart as guide, skip most combat
  Combat approach → full camp battle (Tiger Lord Warriors ×12, Shamans ×3)

AMIRI'S SOLO MISSION (if quest is active):
  Player hands control to Amiri to infiltrate the camp.
  She must reach Nilak without being caught (Athletics DC 15 each check).
  She finds Nilak and Dugath, kills the Defaced Sister threatening them.
  ARMAG arrives and challenges Amiri to single combat.
    [This duel CANNOT be won — Armag is CR 17, Amiri is at most CR 13]
    If player tries to win: Defaced Sister paralyzes Amiri. She is captured.
    Narrative outcome: Amiri is taken prisoner. Player must advance to free her.
    `nilak_survived = TRUE` if Amiri reached them in time.
    `nilak_died = TRUE` if Amiri failed the infiltration checks.
```

**Jamandi and Natala Surtova appear** after the camp fight:
This is the **coronation conversation** — choose your political allegiance:
- Side with Aldori Swordlords → Jamandi alliance bonus, Kassil returns
- Side with House Surtova → Natala alliance bonus, different advisors
- Declare independence → no bonuses, complete autonomy, some doors close

`political_allegiance = aldori / surtova / independent`

---

## Phase 3 — Armag's Tomb

**Location:** Glenebon northwest. Tomb of the original Armag — an ancient barbarian hero of Gorum.

```
TOMB ENTRANCE — Zorek (Gorum's guardian cleric):
  Social bypass (no combat):
  Diplomacy DC 28 "I destroyed Dugath's party!" (requires Dugath killed) → +300 XP
  Deception DC 30 "I serve Gorum!" → +300 XP
  Intimidation DC 26 (scales with deeds shown) → +300 XP
  Combat → fight Zorek. +640 XP but harder.

ZOREK — Cleric of Gorum (Cleric 10, Warpriest)
  HP: 112 | AC: 22 (Full Plate + Shield) | Speed: 25 ft
  Greatsword: d20+14 (2d6+9 S) | Divine Font: Harm (5d10+20, 30 ft burst)
  Spells: Flame Strike (8d6 fire+divine, 10 ft radius), Spiritual Weapon (sustained)
  Fort +16 | Ref +10 | Will +14
  Aura of Gorum: All within 20 ft +1 to attack rolls while adjacent to an enemy
  XP: 640 (if fought). Social bypass avoids combat entirely.

TRIAL OF STRENGTH: DC 35 Athletics → full access. DC 25 (2 fails) → partial.
TRIAL OF PAIN: Trap corridor. Bypass: Perc DC 30. Or run through with Evasion + speed.

DUNGEON ENEMIES (Levels 1–2):
  Spectres ×6: HP 58 each | AC 18 (incorporeal) | Energy Drain on hit
                Negative energy/positive energy weapons deal double damage
  Dread Zombie Barbarians ×8: HP 72 each | AC 16 | Greataxe
  Greater Skeleton Warriors ×4: HP 60 each | AC 18 | Longsword+Shield
```

**ARMAG — Final Boss:**
```
ARMAG — see KM_Bestiary.md for full stat block (CR 11, HP 205, AC 28)

SPECIAL: Blood Calling — Amiri focus (+2 atk vs her). nilak_survived → Amiri +2 vs Armag. nilak_died → Amiri Sickened 1.
Defaced Sister: kills her on arrival (scripted).

RESOLUTION:
  Kill → Ovinrbaane drops (Will DC 23/round or attack nearest). Full loot from Bestiary_B.
  Spare → Tiger Lord chief candidate.
  XP: 1,440
```

---

## Phase 4 — Aftermath & Coronation

**Tiger Lord Chief Selection** (if barbarians not all killed):
```
Candidates (only available if alive):
  Amiri → requires Blood Calling complete AND nilak_survived = TRUE
  Armag → if spared
  Dugath → if alive and player is in good standing with him
  Gwart → always available as fallback
  No chief → Tiger Lords scatter, no bonus
Best outcome: Amiri or Dugath → Barbarian Arena building unlocked
```

**Coronation Event** (back at capital):
Linzi asks questions about your reign. Answers affect alignment track.
Jamandi officially names you King/Queen of the Stolen Lands.
`coronation_complete = TRUE`

---

### 🏆 SIDE QUEST — RUSHLIGHT TOURNAMENT

**Available:** Ch4, after coronation. Irovetti sends a formal invitation to compete in the Rushlight Tournament in Pitax — a River Kingdoms arms competition. Optional but rewarding.

**Events (player chooses which to enter):**

| Event | Check | 1st Place Prize |
|-------|-------|----------------|
| Archery | Ranged attack vs DC 22/26/30 (3 rounds) | Composite Longbow +2 |
| Axe Throwing | Athletics DC 18/22/26 | Belt of Giant Strength |
| Horse Race | Survival DC 16 + Athletics DC 14 | War-trained horse |
| Wrestling | Athletics DC 20 vs opponent ×3 | Ring of Feather Falling |
| Grand Melee | Combat vs 3 CR 9 opponents (non-lethal) | +2 Striking Weapon (choice) |

**Intelligence:** Attending grants access to Pitax. Perception DC 18 → spot Tartuccio in crowd (`tartuccio_pitax_sighted = TRUE`). Stealth DC 16 to investigate → find Irovetti's River Kingdom recruitment posters. `pitax_war_prep_discovered = TRUE` → Ch5 first army engagement +2.

**Irovetti** approaches after any event. Courteous, testing. Sense Motive DC 14: he is afraid of you and covering it well.

`rushlight_attended = TRUE` | `rushlight_events_won = [list]` | `pitax_intel_gathered = TRUE/FALSE`

**XP:** +200 attending. +100 per event won. +300 if `pitax_war_prep_discovered = TRUE`.

---

## Ch4 → Ch5 Export
```json
{
  "export_from": "chapter_4", "import_to": "chapter_5",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "size": 0, "armies": [] },
  "story_flags": {
    "armag_fate": "",
    "armag_tomb_cleared": true,
    "nilak_fate": "",
    "amiri_quest": "",
    "tiger_lord_chief": "",
    "political_allegiance": "",
    "coronation_complete": true,
    "pitax_irovetti_aware": true,
    "jamandi_relationship": "neutral",
    "kassil_relationship": "neutral",
    "alignment_track": { "lawful_chaotic": "neutral", "good_evil": "neutral" },
    "companion_quests": {}
  },
  "dispositions": {}, "companion_titles": {}, "faction_tiers": {},
  "standing_orders": {}, "crafting": {}, "mobile_base": {},
  "dream_log": [], "prestige": {}, "ending_flags": {}
}
```

## 📋 CH5 LOAD CHECKLIST
```
[GM CHAPTER 5 LOAD CHECK]
□ KM_Ch4.md loaded (this file — chapters 5-7 are in here)
□ All standard files loaded (see KM.txt How to Continue)
□ Ch4 Export Block imported and parsed
□ Player level 16+, inventory and kingdom state confirmed
□ Key flags read:
    political_allegiance    : aldori / surtova / independent
    coronation_complete     : TRUE
    pitax_irovetti_aware    : TRUE
    all companion quests    : [status of each]
    alignment_track         : [both axes]
□ Note: Military path and infiltration path BOTH available — confirm preference
□ Game State Header output, then begin
```

---

# ═══════════════════════════════════════════
# CHAPTER 5 — WAR OF THE RIVER KINGS
# ═══════════════════════════════════════════

**Levels:** 16 → 18 | **Duration:** ~90 days
**New region:** Pitax, River Kingdoms, Irovetti's palace

## Overview
Irovetti of Pitax invades. Two parallel approaches: **military campaign** (army battles, siege warfare) and **infiltration** (assassination, political subversion). Both are available and can be combined. Irovetti must be defeated. His palace must be taken.

---

## Phase 1 — War Declaration

> **Herald:** *"Irovetti of Pitax declares that the Stolen Lands are an illegal territory, their ruler a bandit-king, and their kingdom a blight upon the River Kingdoms. He invades in the name of civilization."*

Kingdom events become war events — economy disrupted, borders threatened.

---

## Phase 2 — Military Campaign (available)

```
ARMY SYSTEM BECOMES ACTIVE:
  Player's armies engage Pitax forces on the hex map.
  Pitax has 3 initial army units:
    Pitax Royal Guard: Offense +8, Defense 18, Morale 16
    River Mercenaries ×2: Offense +5, Defense 14, Morale 12
  Player must match with equivalent armies or better.

BRINEHEART SIEGE:
  Border fortress — first major military engagement.
  Army combat OR player party assault on the fort directly.
  Fort AC 22, HP 120. Garrison: 8 soldiers + Linxia (Pitax captain).

LINXIA:
  HP: 96 | AC: 22 | Rapier d20+15 (1d6+8, Sneak Attack +5d6) | Evasion
  Persuade her to defect: Diplomacy DC 28 → +25,000 gp reward, fort surrenders
  Kill her: standard loot + fort taken

DARVEN — PITAX MERCHANT (SIDE QUEST):
  Darven Mourne approaches during Brineheart siege or at capital (infiltration path).
  Not a fighter. A businessman who backed the wrong king.

  DARVEN: "I funded Irovetti for six years. I would prefer my head stay attached.
           I can offer something worth more than my neck."

  Offer: 25,000 gp, four Pitax supply chain maps (army costs −10% for 2 turns),
  signed confession of war crimes (River Kingdoms diplomacy post-Ch5).
  In exchange: his life and safe conduct through the Stolen Lands.

  - Accept → `darven_deal = accepted` → 25,000 gp + maps + confession. Recurring Ch6 contact.
  - Negotiate (Diplomacy DC 18) → same + hidden palace basement cache. `darven_cache_location = TRUE`
  - Arrest → `darven_arrested = TRUE` → +1 Loyalty, +5,000 gp seized. No maps.
  - Kill → `darven_killed = TRUE` → nothing. Slight evil tendency.

  `darven_fate = [accepted / negotiated / arrested / killed]`
  XP: +200 any resolution except kill. +100 if negotiated.
```

---

## Phase 3 — Infiltration Path (available)

```
PITAX INTELLIGENCE:
  Spymaster role (if filled) provides advantages: maps, guard patrol timing
  Without Spymaster: Perception DC 20 checks throughout Pitax

IROVETTI'S PALACE APPROACH:
  Three infiltration options:
  A. Sewers (Athletics DC 16 per junction, multiple junctions)
  B. Noble disguise (Deception DC 24, requires noble outfit purchased for 500 gp)
  C. Servant disguise (Deception DC 18, servants are questioned less)

INSIDE THE PALACE:
  Irovetti's vault: 8,400 gp, Ring of the Archmagi
  Tartuccio's note: `tartuccio_pitax_connection_confirmed = TRUE`
    (A letter in Irovetti's desk — Tartuccio has been reporting on the player since Ch1)
```

---

## Phase 4 — Irovetti

> **⛔ GM EYES ONLY — IROVETTI'S FULL NAME — READ BEFORE RUNNING ANY SCENE WHERE HIS NAME COMES UP**
>
> **Full name: Castruccio Irovetti of Pitax**
> "Irovetti" is his house name. He rules exclusively as "Irovetti of Pitax" — his given name Castruccio is suppressed. He does not use it, sign with it, or acknowledge it publicly. Most of the River Kingdoms do not know it exists. Paizo buries it deliberately so players do not make the connection immediately.
>
> **THE TARTUCCIO CONNECTION — NEVER VOLUNTEER THIS:**
> Castruccio → Tartuccio. Same Taldan diminutive construction (-struccio / -tuccio). One letter apart. Same rhythm. Same origin.
> Tartuccio is named in deliberate echo of his patron's buried given name. It is a calling card legible only to someone who knows both names.
> When Tartuccio said *"my mother had aspirations"* — he was not lying. She named him after the part of the king that nobody says out loud.
>
> **DISCOVERY RULE — MANDATORY:**
> The DM never surfaces this connection unprompted. It exists to be found by the player through logical deduction: naming conventions → River Kings' full names → first name vs house name → what is Irovetti's given name → Castruccio → Castruccio/Tartuccio said aloud in the same breath.
> Linzi is the natural vector. She notices linguistic patterns. If the player leads her toward it, she can arrive at it. The DM's job is to follow the chain and let it land — not to shortcut it and not to stall when the player is clearly building toward it.
> The payoff is Linzi saying "Castruccio" out loud while Tartuccio is in the room and watching his face.

```
IROVETTI — see KM_Bestiary.md for full stat block (CR 13, HP 195, AC 32)

SPECIAL: Court musicians play during fight — Performance DC 20 to silence.

RESOLUTION:
  Kill → Kingdom gains Pitax as vassal.
  Capture → Public trial. Handed to Brevoy → Jamandi bonus.
  Recruit [Evil] → Impossible. Too vain.

LOOT: +2 Striking Rapier, Cloak of Resistance +4, Headband of Mental Perfection +4,
      Irovetti's Crown, 8,400 gp vault, 3,789 gp treasury
XP: 1,560
```

```
LINXIA — Pitax Captain (Rogue 9)
HP: 96 | AC: 22 (Studded Leather +2 + Dex) | Speed: 30 ft
Fort +12 | Ref +18 | Will +11
Rapier: d20+15 (1d6+8 P, Finesse) | Sneak Attack: +5d6
Evasion: On Ref success vs AoE — no damage
Gang Up: gains Flanking bonus even without an ally (her shadows count)
Persuade to defect: Diplomacy DC 28 → surrenders fort, joins as informant
XP: 480
```

---

## Ch5 → Ch6 Export
```json
{
  "export_from": "chapter_5", "import_to": "chapter_6",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "armies": [],
               "pitax_vassal": false },
  "story_flags": {
    "irovetti_fate": "",
    "pitax_vassal": false,
    "linxia_fate": "",
    "darven_fate": "",
    "lem_quest": "",
    "tartuccio_pitax_confirmed": true,
    "tartuccio_final_fate": "",
    "military_path_used": false,
    "infiltration_path_used": false,
    "brineheart_taken": false,
    "river_kingdoms_allied": [],
    "companion_quests": {},
    "alignment_track": {}
  },
  "dispositions": {}, "companion_titles": {}, "faction_tiers": {},
  "standing_orders": {}, "crafting": {}, "mobile_base": {},
  "dream_log": [], "prestige": {}, "mythic_path": {}, "ending_flags": {}
}
```

## 📋 CH6 LOAD CHECKLIST
```
[GM CHAPTER 6 LOAD CHECK]
□ KM_Ch4.md loaded (this file — Ch6 is in here)
□ KM_Linzi_Shrine.md loaded — shrine quest may trigger this chapter
□ All standard files loaded (see KM.txt How to Continue)
□ Ch5 Export Block imported and parsed
□ Player level 16–18, kingdom state confirmed
□ Key flags read:
    irovetti_fate           : [value]
    pitax_vassal            : [TRUE/FALSE]
    tartuccio_final_fate    : [value — he should be resolved by now]
    all companion quests    : [status — CRITICAL for Ch7 survival]
    alignment_track         : [both axes]
    nyrissa_backstory_known : [TRUE/FALSE — affects true ending]
□ COMPANION QUEST AUDIT: list every companion and their quest status
   Any incomplete quests = risk of losing that companion in Ch6 or Ch7
□ Bloom escalation will consume hexes each kingdom turn — prepare defenses
□ Game State Header output, then begin
```

---

# ═══════════════════════════════════════════
# CHAPTER 6 — SOUND OF A THOUSAND SCREAMS
# ═══════════════════════════════════════════

**Levels:** 18 | **Duration:** ~60 days (hard — Bloom escalates fast)
**Tone:** Supernatural horror. Your kingdom is being consumed.

## Overview
The Bloom reaches its final stage. Nyrissa reveals herself directly. Your kingdom loses hexes to supernatural infestation each turn. You must: defend key settlements, find Nyrissa's lair (Thousandbreaths), and enter it. This chapter is a race against collapse.

---

## Phase 1 — The Kingdom Crumbles

**Each kingdom turn this chapter:** Roll d6. On 1–3, a hex is consumed by the Bloom. Claimed hexes revert to Hostile. Buildings in consumed settlements take damage.

**Nyrissa speaks for the first time (scripted):**
> *She is standing in your throne room.*
> *Not attacking. Not threatening. Just standing there as if she owns it.*
>
> **Nyrissa:** *"I have been watching you since before you arrived at that gate in Restov. Every choice you made, I helped arrange. Not because I wanted you to fail — because I needed you to succeed at exactly this level."*
>
> *"Your kingdom is not your achievement. It is my vessel."*

`nyrissa_revealed = TRUE`

**True ending requirement begins here:** How the player responds to Nyrissa matters.
- Aggressive → she disappears, nothing changes
- [Curious] "What do you actually want?" → +lore, Nyrissa explains her curse (Lantern King imprisoned her love) → `nyrissa_backstory_known = TRUE` — **this flag is required for the true ending**

---

## Phase 2 — Companion Survival Checks

This chapter triggers any incomplete companion quest consequences:
```
valerie_quest incomplete → Valerie trapped in burning prison this chapter
                           Player must choose: save Valerie or continue forward
                           Saving her: Perception DC 16 + Athletics DC 18

harrim_quest incomplete → Harrim wanders off during Ch6 dungeon exploration
                          Returns but misses critical fights

jaethal_quest incomplete → Jaethal briefly hostile (Urgathoa influence)
                           Diplomacy DC 20 to bring her back each scene

linzi_quest and 3 other conditions for save → see below
```

---

## Phase 3 — Thousandbreaths

**Thousandbreaths** — Nyrissa's domain. A pocket dimension accessible via a portal in the Narlmarches.

```
DUNGEON PROPERTIES:
  Extradimensional space — rules of normal reality are unstable
  Lighting: perpetual deep twilight — Dim Light conditions everywhere
             (Elves, Half-Elves immune via Low-Light Vision)
  Time distortion: every 2 rooms, party gains Fatigued unless Fort DC 16 succeeded

ENEMIES (all Nyrissa's servitors — fey and bloom-touched):
  Bloom Guardian ×6: HP 85 | AC 20 | Tendril ×2 d20+12 (2d6+8, Grab)
  Nyrissa's Archer ×4: HP 68 | AC 18 | Longbow d20+14 (2d8+6, Vital Strike)
  Verdant Nightmare (boss room guardian):
    HP: 145 | AC: 22 | Slam d20+15 (3d6+10) | Aura: Frightened 2 (Will DC 20)

LOOT: Staff of Nyrissa (Occultism +4 item bonus, cast Wall of Thorns at will),
      Ring of Regeneration, Cloak of Elvenkind, 4,400 gp
```

**LINZI'S DEATH — Ch6 trigger:**
The exact moment Nyrissa kills Linzi occurs at the end of Phase 3, just before the final confrontation room.

> *Nyrissa steps from the shadows. She is beautiful and entirely wrong.*
> *She looks at Linzi with something almost like pity.*
> **Nyrissa:** *"The little one. She has been writing everything down. That is a kind of immortality."*
> *She touches Linzi's chest. Linzi crumples.*

**OPTIONAL SAVE CHECK** (if all 4 conditions met — see KM_Companions.md):
Diplomacy DC 28 or 2 Hero Points to interpose before Nyrissa acts.
Success: `linzi_saved = TRUE` — she survives Ch6 physically. Skip shrine quest.
Failure or conditions not met: Linzi dies. `linzi_dead = TRUE`

**SHRINE QUEST TRIGGERS ON RETURN TO CAPITAL:**
If `linzi_dead = TRUE`: Jhod Kavken meets the player with three scrolls.
The player must choose ONE god's shrine to build. This is the only chance.
One choice. One price. One outcome.

> **See `KM_Linzi_Shrine.md` for the complete three-path resurrection quest:**
> - **Shelyn (Good)** — Give something you made that matters
> - **Pharasma (Neutral)** — Destroy an abomination against death
> - **Urgathoa (Evil)** — A feast, an ongoing kingdom tithe, and Linzi's consent

The shrine quest must be resolved before entering the House at the Edge of Time (Ch7).
If the player enters Ch7 without resolving it: the window closes. `linzi_dead = TRUE` permanently.

---

## Ch6 → Ch7 Export
```json
{
  "export_from": "chapter_6", "import_to": "chapter_7",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "bloom_consumed_hexes": 0 },
  "story_flags": {
    "nyrissa_revealed": true,
    "nyrissa_backstory_known": false,
    "thousandbreaths_entered": true,
    "linzi_dead": false,
    "linzi_saved_interpose": false,
    "linzi_shrine_completed": false,
    "linzi_mark": "",
    "valerie_survived_ch6": true,
    "harrim_quest": "",
    "jaethal_quest": "",
    "octavia_quest": "",
    "regongar_quest": "",
    "amiri_quest": "",
    "nilak_survived": false,
    "tristian_redeemed": false,
    "ekundayo_quest": "",
    "noknok_quest": "",
    "lem_quest": "",
    "kalikke_kanerah_quest": "",
    "storyteller_collection": false,
    "bloom_consumed_hexes": 0,
    "kingdom_stability_at_ch7": 0,
    "alignment_track": {}
  },
  "dispositions": {}, "companion_titles": {}, "faction_tiers": {},
  "crafting": {}, "dream_log": [], "prestige": {}, "mythic_path": {}, "ending_flags": {}
}
```

## 📋 CH7 LOAD CHECKLIST
```
[GM CHAPTER 7 LOAD CHECK — THE FINAL ACT]
□ KM_Ch4.md loaded (this file — Ch7 is in here)
□ KM_Linzi_Shrine.md loaded (if shrine quest is active or pending)
□ All standard files loaded
□ Ch6 Export Block imported and parsed
□ Player level 18–20, full inventory confirmed

CRITICAL PRE-ENTRY AUDIT:
□ Read every companion's quest status aloud to the player:
  → "Amiri: [complete/incomplete] — [consequence if incomplete]"
  → "Linzi: [alive/dead/shrine-returned] — mark = [none/shelyn/pharasma/urgathoa]"
  → [repeat for all 11 companions]
□ Ask: "Are you ready to enter the House at the Edge of Time?
         Once inside, you cannot leave until it's over."

TRUE ENDING READINESS:
□ nyrissa_backstory_known = TRUE? (from Ch6 Phase 1 curiosity response)
□ If FALSE: warn player the true ending requires this flag.
             Last chance — they can ask Nyrissa now (she's in their throne room).

□ storyteller_collection = COMPLETE? (all 10 fragments)
   If yes and Linzi is alive + Devoted: Linzi save option still available inside.

□ Game State Header output, then ask player to confirm before writing any scene.
```

---

# ═══════════════════════════════════════════
# CHAPTER 7 — THE FINAL ACT
# ═══════════════════════════════════════════

**Levels:** 18–20 | **Final chapter**
**Location:** House at the Edge of Time — Nyrissa's true domain

## Overview
The final dungeon. The Lantern King's curse is the root of everything. Five endings exist based on accumulated flags — see `KM_Mythic_Systems.md` for full requirements and scripted narration. The ending is NOT chosen from a menu — it emerges from play.

---

## The House at the Edge of Time

**Point of no return.** All companion quests must be resolved before entering.

> **DM:** Before the player enters, run the companion check:
> - List every companion's quest status
> - Warn: "Any incomplete quests mean that companion faces their Ch7 risk inside"
> - Ask: "Are you ready to proceed?"

```
DUNGEON PROPERTIES:
  Time flows differently — past and present overlap in different rooms
  Some rooms show the kingdom's founding; others show its destruction
  Companions see visions of their personal fears (roleplay opportunities)
```

---

## Companion Fates Inside

```
All quests complete → all companions present for the final fight

Incomplete quests trigger:
  Valerie → burning prison room — Perception 16 + Athletics 18 to save her
  Harrim  → wanders off, rejoins after Nyrissa fight
  Jaethal → Urgathoa influence — Diplomacy 20 each scene to keep her aligned
  Octavia + Regongar (one quest incomplete) → prison room, save one
  Octavia + Regongar (both incomplete) → both imprisoned, save one only
  Amiri (nilak_died) → present but leaves after Nyrissa is defeated (grief)
```

---

## Nyrissa — The True Fight

```
NYRISSA — see KM_Bestiary.md for full stat block (CR 20, HP 380, AC 43)

PHASE 1 (HP 380–190): Thorn Wall, Dominate (lowest Will), Wail of the Lost, Fey Step (teleport 60 ft).

PHASE 2 (below 190 — Lantern King intervenes):
  Heals Nyrissa to 190 HP. "Go on then. Finish her. That's what I've been waiting for."
  He wants you to kill her — that's part of the curse.

THE CHOICE (true ending gate):
  Kill Nyrissa (standard) → BAD ENDING
  [Requires: nyrissa_backstory_known = TRUE]:
    "I know what he did to you. I know what was taken."
    → Nyrissa pauses. She looks at the Lantern King.
    → Diplomacy DC 30 OR 2 Hero Points
    → SUCCESS: Break the curse. Confront the Lantern King. TRUE ENDING.
    → FAIL: Fight continues, bad ending.
```

---

## Default Ending (The Ruler's Ending)

Kill Nyrissa without meeting true ending requirements. Kingdom survives with reduced stats. No resolution to the Lantern King's curse. Full scripted narration in `KM_Mythic_Systems.md` — Ending 1.

**Other endings** (Conquest, Transcendence, Golden) fire based on accumulated flags. See `KM_Mythic_Systems.md` for all 5 ending variants and their flag checklists. DM checks eligibility at Ch6 opening.

---

## True Ending

> *Nyrissa stares at the Lantern King.*
> **Nyrissa:** *"You gave me a heart so you could take it. You cursed me to love what I destroy. For ten thousand years."*
>
> *The Lantern King is not laughing anymore.*
>
> *"You were supposed to kill her," he says to you. "That was the arrangement."*
>
> *The Lantern King waits for an answer. Present a choice menu — the player's response is their own.*

```
LANTERN KING — Eldest Fey (Trickster Divinity)
HP: 320 | AC: 30 | Cannot be permanently killed (he is a fundamental force)
His attacks deal Confused 1 (Will DC 26) on hit — trickery made manifest
His weakness: Honesty. The more directly the player speaks truth to him, the lower his DCs.

Each round: Player can attack OR speak truth:
  [Attack] → deals damage, no special effect
  [Truth] → Lore (Fey) DC 20 OR player identifies something real about him
    → His AC drops by 1 per truth told (cumulative, max −6)
    Examples: "You're afraid of what you created." (+1 AC reduction)
              "You've been alone since before this kingdom existed." (+1)
              "She loved something you made and you couldn't stand it." (+2)

At 0 HP: The Lantern King cannot die. He yields. For the first time in ten thousand years, someone made him yield.
He removes Nyrissa's curse. She is free.
```

> *Nyrissa kneels in the ruins of the House.*
> **Nyrissa:** *"I don't know what I am without the curse."*
> *She looks at you. And at the kingdom visible through the crumbling walls.*
> *"But I would like to find out."*

**True Ending outcomes:**
- Nyrissa can be offered a place in your kingdom (she becomes a permanent ally — unique advisor)
- Kingdom receives the Bloom's land back (all consumed hexes restored)
- `true_ending_achieved = TRUE`
- Linzi (if saved): writes the final chapter of the chronicle — the real one
- Leliana (if `leliana_chronicler_mode` + survived to here): performs the completed Verse as the final movement — the real ending, played rather than written. If the Verse was never finished, she plays it to where she got and lets the last note hang unresolved (intentional — do not "complete" it for her).

---

## Final XP & Epilogue

| Source | XP |
|--------|----|
| Ch7 dungeon encounters | ~4,800 |
| Nyrissa (boss) | 2,000 |
| Lantern King (true ending) | 1,600 |
| Companion saves | 400–800 depending |
| **Chapter 7 Total** | **~9,200–10,000** |

**Final Kingdom State:**
- True Ending: All stats restored, Bloom land reclaimed, Nyrissa as optional advisor
- Bad Ending: Kingdom survives, permanently reduced Culture and Loyalty, cursed undercurrent

---

## 🎭 EPILOGUE SCENES (Linzi's Questions)

Linzi (or her book, if she died) asks the player a final series of questions about their reign. Answers generate the epilogue narrative.

**If `leliana_chronicler_mode = true`:** Leliana runs this beat instead of Linzi — she asks the same reign questions between movements of the Verse (or, if she died, they surface as the untitled pieces in her Ballad Cycle / the final score page, and the player answers by choosing which get performed). Same epilogue-generation function, her register not Linzi's: less "what will the official account say" and more "what was this worth — was it worth finishing." The generated epilogue is delivered as the closing performance of the Verse rather than the closing page of the chronicle.

```
1. What was your kingdom known for? (Culture / Economy / Military / Justice)
2. What happened to [key NPC]? (For each major NPC — outcomes based on flags)
3. Did you rule with the sword or the word? (Alignment-based)
4. What came next? (Open-ended — player describes what happens after)
```

---

*KM_Ch4.md — Kingmaker PF2e Text Adventure | Chapters 4–7 v1.0*
*Source: Pathfinder Kingmaker AP (Paizo) + Owlcat Games | PF2e rules: 2e.aonprd.com*


---

<!-- merged from KM_Linzi_Shrine.md (v93.21 file consolidation) -->

# KINGMAKER — THE SHRINE OF RETURNING
## KM_Linzi_Shrine.md | Active: Chapter 6 | Referenced by: KM_Ch4.md (Ch6 section)

---

> **DM:** Load this file during Chapter 6. The shrine quest becomes available the moment the player returns to the capital after Linzi's death in Thousandbreaths. This is a one-chance, one-god decision. The player chooses which shrine to build. That choice is permanent. Once a shrine is selected and construction begins, the other two gods will not hear prayers on this matter.
>
> **CRITICAL FLAGS:**
> - `linzi_dead = TRUE` — triggers this quest
> - `shrine_god_chosen` — set when player commits to a shrine (`shelyn` / `pharasma` / `urgathoa`)
> - `shrine_built = TRUE` — set when construction is complete
> - `linzi_resurrection_attempted = TRUE` — set when the ritual is performed
> - `linzi_returned = TRUE/FALSE` — outcome
> - `linzi_mark` — the permanent mark left on her (`shelyn_marked` / `pharasma_marked` / `urgathoa_marked`)

---

## 🕯️ QUEST TRIGGER — RETURN FROM THOUSANDBREATHS

> *Back at the capital. The throne room feels different without her in it.*
> *Her notebook is on the table. She left it there before you departed.*
> *The last entry is dated the morning you left for Thousandbreaths.*
> *"Chapter [X]: The Final Chapter. Working title. Obviously."*

Jhod Kavken approaches the player within 24 hours of return:

> **Jhod:** *"There are those who say death is not always final. I've spent my life in service to a god who healed the unhealable. I won't tell you it's possible. But I won't tell you it's impossible either."*
>
> *He sets three scrolls on the table.*
> *"These are the forms. Each one is a covenant with a different power. You should read all three before you decide. Once you begin construction — once the first stone is laid — the other two doors close. The gods do not share this kind of claim."*

**Player must read all three scrolls before choosing.** Each scroll describes the god's nature and the general shape of what they'll ask. DM presents the overview below — do not yet reveal the specific prices.

---

## 📜 THE THREE SCROLLS — OVERVIEW

> **SCROLL OF SHELYN** — *The Eternal Rose, Goddess of Love, Beauty, and Art*
> *"She governs what endures. What is made with love outlasts what is made for power. Her shrines are built in beauty. Her prices are paid in beauty. She has been known to return what was lost — but she will ask you to understand what you are asking for."*

> **SCROLL OF PHARASMA** — *The Lady of Graves, Goddess of Death, Fate, and Prophecy*
> *"She governs every soul that passes. The dead belong to her. To ask for one back is to ask her to undo her own work. She does not do this lightly, or cheaply, or without consequence. But she has done it. She is not cruel. She is absolute."*

> **SCROLL OF URGATHOA** — *The Pallid Princess, Goddess of Undeath, Gluttony, and Disease*
> *"She can return the dead. She returns them as they are — which is to say, changed. What she gives is real. What she takes is also real. Her shrines are not built in beauty. Her prices are not paid in beauty. But she delivers."*

**Player chooses one.** The other two scrolls turn to ash when the first shrine stone is laid.

---

## 🌸 PATH 1 — SHELYN'S SHRINE

### The Shrine

**Without existing temple:** Requires 8 RP and 30 days of construction. A freestanding marble structure with rose motifs. No prior religious infrastructure needed.

**With existing Temple of Shelyn (max tier):** Requires 4 RP and 14 days. The shrine is an extension of what already exists — the god is already present in your kingdom.

**Construction event:** As the shrine nears completion, roses begin growing around it — unseasonably, out of season. Local children bring flowers without being asked. `shelyn_shrine_attention = TRUE`

---

### Shelyn's Price — What She Asks

When the shrine is complete, a vision comes. Not a booming divine voice — a woman's voice, warm and tired, like someone who has seen everything and still chooses to love it.

> **Shelyn:** *"She wrote everything down. Do you know how rare that is? Most lives are lived and lost and no one thought to make them permanent."*
>
> *A pause.*
>
> **Shelyn:** *"I will bring her back. But you have to give me something that matters. Not gold. Not blood. Something you made — that you put yourself into — that you would keep if you could."*

**THE PRICE — The Chronicle:**
Shelyn asks for the original manuscript of Linzi's chronicle. Every page. Every word Linzi wrote.

The chronicle is the record of your entire campaign — every battle, every companion, every choice. It is the only copy. If you give it:
- Linzi returns
- The chronicle goes to Shelyn's domain
- Linzi remembers everything she wrote but has no physical record of it
- She will have to write it again from memory — and the new version will be different

```
PLAYER MUST CHOOSE:
A. Give the chronicle → Shelyn accepts. Ritual begins.
B. "I can't give this away — it's her life's work" → Shelyn:
   "Then perhaps you understand why I asked for it. She would want you to keep it.
    Give me something else — something you made that matters to you personally."
   → Alternative: Player must create something (Crafting DC 22 + 3 days + 100 gp)
     A piece of art, a monument design, a composition — made BY the player, not bought.
     On success: Shelyn accepts the alternative.
     On failure: The offering is insufficient. Shelyn does not respond.
     One attempt only.
C. "Is there anything else?" → "No. I ask for what is real."
```

**If the chronicle is given OR the alternative succeeds:**

> *The shrine glows softly. Not dramatically — the way sunlight looks through leaves.*
> *Linzi's notebook opens on the table. The pages turn on their own.*
> *Then she is there. Standing in the shrine garden.*
> *She looks at her hands. Then at you.*
>
> **Linzi:** *"...I had the strangest dream. I was somewhere very bright and someone was asking me to sing and I kept saying I wasn't ready yet."*
> *She looks around. The capital. The shrine. Roses.*
> *"...Did you build this for me?"*

---

### Shelyn's Mark

`linzi_mark = shelyn_marked`

Linzi returns fully herself — warm, enthusiastic, notebook always in hand. But Shelyn's touch remains:

- Her new chronicle glows faintly when she reads passages aloud
- Flowers grow slightly faster near wherever she camps
- Once per long rest: she can cast *Soothe* (2d10+8 healing) without components — she hums it into existence without knowing she's doing it
- **Permanent:** Her writing is subtly, indefinably better. Even she notices it. She cannot explain it.

**Companion reactions:**
- Amiri: *"Hm. You came back. Good. It was quiet."* (She is relieved. She will not say so.)
- Tristian: Weeps quietly in the shrine garden. Says nothing for a while. Then: *"Thank you."*
- Valerie: Formally acknowledges her return. Notes that Shelyn's blessing on a bard is *"fitting, if sentimental."*
- Jaethal: *"Interesting. She looks alive. Almost entirely."* (Means this as a compliment.)

---

## ⚖️ PATH 2 — PHARASMA'S SHRINE

### The Shrine

**Without existing temple:** Requires 10 RP and 45 days. A stark stone structure — no ornamentation, no flowers, no warmth. Just clean edges and a scale motif carved above the entrance. The locals find it unsettling. Unrest +1 during construction.

**With existing Temple of Pharasma (max tier):** Requires 5 RP and 20 days. Unrest +0 (the temple's presence has already normalized Pharasma's aesthetic in your kingdom).

**Construction event:** A psychopomp — a hooded figure with a pale mask — appears at the construction site on the third day. It says nothing. It observes. It leaves. `pharasma_shrine_noticed = TRUE`

---

### Pharasma's Price — What She Asks

The vision comes at midnight, exactly. The shrine is cold even in summer. A voice like stone sliding against stone.

> **Pharasma:** *"You want her back."*
> *Not a question.*
>
> **Pharasma:** *"You understand that I have processed ten thousand souls today. That each of them had someone who wanted them back. That I made no exceptions."*
>
> *A pause that lasts longer than it should.*
>
> **Pharasma:** *"But you are not ten thousand somebodies. You are the ruler of a kingdom that sits on land I have particular interest in. And she is — I will admit — not finished yet. There is more chronicle in her. I can see it."*
>
> **Pharasma:** *"My price is this: something that should not exist, ends. You will know it when you find it. Bring me the proof, and she comes home."*

**THE PRICE — Destroy an Abomination Against Death:**

Pharasma requires the player to end something that violates the natural order of death. Three valid targets exist — player must complete one:

```
OPTION A: A LICH'S PHYLACTERY
  Any active lich in the Stolen Lands region whose phylactery has not been destroyed.
  If Vordakai's Oculus was destroyed in Ch3: this option is already fulfilled.
    → `vordakai_phylactery_destroyed = TRUE` from Ch3 carries here
    → Present the Oculus fragments at the shrine. Pharasma accepts immediately.
    → This is the "easy" path — players who finished Ch3 thoroughly get rewarded.
  If Vordakai was recruited [evil path]: this option is NOT available.
  Alternative phylactery: A minor lich in the Narlmarches (new encounter, Level 14).
    → HP: 140 | AC: 26 | Spells: 8th level | Phylactery: stone box in a hidden tomb
    → +1,800 XP

OPTION B: SEAL A PORTAL TO THE NEGATIVE PLANE
  A rift has been leaking negative energy into a Narlmarches hex.
  Location: revealed by the psychopomp if player asks it (Diplomacy DC 18 to communicate)
  The seal: Occultism DC 28 + 3 castings of Consecrate (requires a cleric in party)
           Or: sacrifice a Level 5+ magic item into the rift (consumed, gone)
  Time: 2 days on-site
  → +1,200 XP

OPTION C: DESTROY THE UNDEAD ARMY
  If any undead NPC was recruited as an advisor (Vordakai, or certain evil path choices)
  Pharasma will not accept Linzi's return while a warlord of undeath advises the ruler.
  This option requires the player to dismiss and destroy the undead advisor.
  A steep price for players who took the evil path.
```

**When the price is paid:** Return to the shrine with proof (phylactery fragments / sealed rift / dismissal record).

> *The shrine's scale tilts. Slightly. Then levels.*
>
> *Pharasma's voice, once:*
> **Pharasma:** *"The scales are balanced. A wrong against death is corrected. A right against death is permitted."*
>
> *Linzi walks out of the shrine door. She looks dazed. Like someone who fell asleep mid-sentence and woke up in a different room.*
>
> **Linzi:** *"...It was very organized there. Very — orderly. There was a queue. I was number [X]. I never found out what [X] meant."*
> *She blinks. Looks at you.*
> *"You balanced the scales for me, didn't you."*

---

### Pharasma's Mark

`linzi_mark = pharasma_marked`

Linzi returns fully herself — but she has stood in Pharasma's hall and remembers it, dimly, the way one remembers a dream that meant something.

- She no longer fears death in the abstract. She has seen the process. It's orderly.
- Once per session: when any party member reaches 0 HP, Linzi can call out a number — their number from the queue — and they automatically stabilize (no recovery check needed). She doesn't fully understand how she knows. She just does.
- Her chronicle entries about death — of enemies, of companions, of moments — are now written with uncommon precision. She does not flinch from them.
- **Permanent:** Pharasma's psychopomps leave her alone. Undead creatures treat her as one degree less hostile by default (they sense she has stood in that hall and returned with permission).

**Companion reactions:**
- Harrim: *"You've seen the Gray Lady's hall. I have dreamed of it my entire life."* He sits with her for an hour. Neither speaks much. It is the most at peace he has seemed.
- Jaethal: Studies her with genuine interest. *"What was it like? Tell me everything."*
- Tristian: Troubled. *"The Lady of Graves gave her back. That doesn't happen. What did we trade for that?"*
- Amiri: *"The dead stay dead. Except when they don't. Fine."*

---

## 💀 PATH 3 — URGATHOA'S SHRINE

### The Shrine

**Without existing temple:** Requires 6 RP and 21 days. Faster and cheaper than the others — Urgathoa is not particular about aesthetics. The shrine is functional, dark-stoned, with a bone motif. Unrest +2 during construction and permanently while it stands. Citizens avoid the street it's on.

**With existing Temple of Urgathoa (max tier):** Requires 3 RP and 10 days. The temple's presence already marks your kingdom as darkness-touched. No additional unrest.

**Construction event:** The night the shrine is completed, something dies near it. An old dog. A tree. Nothing dramatic. Just — something. `urgathoa_shrine_fed = TRUE`

---

### Urgathoa's Price — What She Asks

The vision comes during a feast. Urgathoa appreciates irony.

> *The food tastes different suddenly. Richer. Too rich. Overwhelming.*
>
> **Urgathoa:** *"Oh, I like you. You built me a shrine. In your nice clean capital."*
> *A laugh — it sounds like something eating.*
>
> **Urgathoa:** *"I'll bring your little bard back. She'll be exactly herself. Mostly. There's just one thing."*
>
> **Urgathoa:** *"I'm hungry. I'm always hungry. Your kingdom is going to feed me — just a little, just an ongoing contribution — and your bard is going to carry my mark whether she likes it or not. And she will not like it."*
>
> *"The question is: does she get to decide? Or do you?"*

**THE PRICE — Three Components:**

```
COMPONENT 1: The Feast of Urgathoa (immediate)
  A feast must be held in the shrine. Not symbolic — a real feast, with real food,
  and at least one living person must eat until they are genuinely ill.
  The player must participate (or order it). Alignment: [Evil] flag.
  Duration: one evening. Cost: 200 gp in food and wine.

COMPONENT 2: The Ongoing Tithe
  Every kingdom turn: −1 to one of the following (player's choice each turn):
    Economy, Culture, or Loyalty
  This represents Urgathoa's ongoing appetite from your kingdom.
  Cannot be removed while the shrine stands.
  Removing the shrine: Urgathoa's mark on Linzi intensifies for 30 days (she is Sickened 1
  until a Remove Curse DC 25 is performed). After that: the tithe ends and the mark
  fades to its permanent baseline.

COMPONENT 3: Linzi's Consent (the real price)
  Urgathoa adds one condition: "She has to agree. I don't take what isn't offered."
  (She is lying about why she requires consent — she doesn't require it. She enjoys
  the moment when Linzi finds out and has to choose.)
  When Linzi returns: she is undead, functional, herself.
  She will be told immediately what happened.
  She will have one conversation with the player.
  She must then decide: accept Urgathoa's mark and live on as she is, or refuse
  it, which means returning to death.
```

**LINZI'S RETURN — The Conversation:**

> *She walks out of the shrine. She stops. She puts her hand to her chest.*
> *No heartbeat.*
>
> **Linzi:** *"...Oh."*
> *She looks at her hand. Holds it up to the light.*
> *"...I'm dead, aren't I. I mean — I'm here. But I'm dead."*
>
> *She turns to you. Her expression is complicated.*
> **Linzi:** *"You built a shrine to Urgathoa. For me."*
> *A long pause.*
> *"Tell me the price. All of it. Don't soften it."*

**Player must tell her. The DM presents the three components.**

```
LINZI'S DECISION:
  "I accept it."
    → She closes her notebook. Opens it again.
    → "Well. This will make for a very interesting chapter."
    → `linzi_accepted_urgathoa = TRUE`
    → She stays. Undead but herself.

  "I don't accept it."
    → She exhales — a habit, since she doesn't need to breathe anymore.
    → "Then I think... I think I have to go back."
    → She reaches out and touches your hand.
    → "Write the ending yourself. You know how the story goes."
    → She fades.
    → `linzi_refused_urgathoa = TRUE` — she returns to death
    → The shrine remains. The tithe begins regardless.
    → This is the worst outcome. Urgathoa got her feast and her tithe
      and the player has nothing.
    → Urgathoa: (distant, amused) "I did say she had to agree."
```

**If Linzi accepts:**

She stays. But the Urgathoa path has a redemption arc built in:

```
SECONDARY QUEST — Linzi's Cure (optional, available any time after Ch6):
  Jaethal knows a way to remove Urgathoa's mark — she had it done to herself
  once, partially. Reverse-engineer the process.
  Requires: Jaethal's quest complete + Occultism DC 28 + Remove Curse DC 25
  + A cleric of Sarenrae or Pharasma performing the rite (Tristian, Jhod)
  + 500 gp in ritual components
  On success: Mark removed. Linzi becomes fully alive again.
  The ongoing tithe ends.
  The shrine still stands (and still generates unrest) but is now inert.

  LINZI after cure: "I keep expecting the heartbeat to feel wrong. It doesn't."
  She is quiet for a moment. "Thank you. Both times."
```

---

### Urgathoa's Mark (if uncured)

`linzi_mark = urgathoa_marked`

Linzi is undead. She is herself — her humor, her writing, her warmth — but she is cold to the touch and has no heartbeat. She knows it. She writes about it with the same directness she writes about everything.

- She does not need food, water, or sleep (she still eats and sleeps by habit — she finds it comforting)
- She is immune to poison, disease, and sleep effects
- She is harmed by positive energy healing (heals for 0, or use Harm instead)
- Once per day: she can cast *Feast of Ashes* on a target (Fortitude DC 19 or Starving — no healing for 24 hours)
- **Permanent:** NPCs who can sense undead react poorly to her (−2 to her Diplomacy in formal settings). Urgathoa's mark glows faintly at the base of her throat when she writes at night.

**Companion reactions:**
- Jaethal: Sits beside her immediately. *"I understand what you are now better than any of them. Ask me anything."* Relationship +1.
- Harrim: *"The Pallid Princess claims another. And yet you persist. Curious."* He is not dismissive. He is genuinely observing.
- Tristian: Cannot look at her directly for three days. On the fourth day he sits across from her at breakfast. *"I'm sorry. I'm working on it."* She: *"I know. Take your time."*
- Amiri: *"You smell different."* Pause. *"You're still annoying. Good."*
- Valerie: Treats her with complete formal normality. Does not mention it once. This is, strangely, the kindest response.

---

## 📊 SUMMARY TABLE

| | Shelyn | Pharasma | Urgathoa |
|---|---|---|---|
| **Alignment** | Good | Neutral | Evil |
| **Cost (no temple)** | 8 RP / 30 days | 10 RP / 45 days | 6 RP / 21 days |
| **Cost (max temple)** | 4 RP / 14 days | 5 RP / 20 days | 3 RP / 10 days |
| **Price** | Something you made that matters | Destroy an abomination against death | A feast + ongoing kingdom tithe + Linzi's consent |
| **Difficulty** | Medium (can fail craft check) | Easy if Ch3 complete, harder otherwise | Low (Linzi may refuse) |
| **Linzi returns as** | Fully alive, Shelyn-touched | Fully alive, death-aware | Undead (curable) |
| **Permanent mark** | Faint glow, passive *Soothe* | Stabilize any ally 1/session, undead neutral | Undead traits, *Feast of Ashes* |
| **Unrest during build** | 0 | +1 | +2 |
| **Kingdom ongoing cost** | None | None | −1 stat per turn |
| **Can fail?** | Yes (craft check fails) | Rare (if Vordakai recruited) | Yes (Linzi refuses) |

---

## 💾 FLAGS TO CARRY IN SAVE BLOCK

```json
"linzi_shrine": {
  "triggered": true,
  "god_chosen": "",
  "shrine_built": false,
  "price_paid": false,
  "resurrection_attempted": false,
  "linzi_returned": false,
  "linzi_mark": "",
  "linzi_accepted_urgathoa": false,
  "linzi_refused_urgathoa": false,
  "linzi_cured_urgathoa": false,
  "chronicle_given_to_shelyn": false,
  "vordakai_phylactery_used": false,
  "ongoing_tithe_active": false
}
```

---

## 🏛️ MUTUAL EXCLUSION — CHRONICLER KINGDOM BUILDINGS

**Condition gate (set at LINZI-REPLACEMENT GATE or Linzi dismissal):**

| Flag state | Available building |
|---|---|
| `linzi_primary_chronicler = TRUE` (default) | Linzi Shrine of Returning (above) |
| `leliana_chronicler_mode = TRUE` | Hall of the Unfinished Verse (below) |

Both are Tier 2+ kingdom structures, and since Linzi and Leliana are **never both in a run** (NEVER-BOTH invariant, KM_Companions_Behaviors.md § LINZI-REPLACEMENT GATE), only ONE is ever built.

⛔ **UPDATED — supersedes the old "by choice, not by grief" framing.** Per the MASTER TRANSFORMATION RULE, when Leliana holds the chronicler-bard slot she INHERITS Linzi's full death arc: it is **Leliana** whom Nyrissa takes in Thousandbreaths (Linzi is not in the run), and the **Hall of the Unfinished Verse is her RESURRECTION shrine — by grief, triggered by her Ch6 death**, derived from the Linzi Shrine of Returning by swapping words→music. Same death trigger, same 4 save conditions (her 10 ballad verses / the Unfinished Verse replace the Storyteller fragments), same three gods (Shelyn/Pharasma/Urgathoa), same prices, same outcomes, same epilogue role. If Leliana is SAVED (4 conditions + interpose), she lives and the shrine is skipped — exactly as for Linzi. Use the Linzi Shrine mechanics below, re-skinned to music.

---

<!-- LELIANA CONCERT HALL — parallel to Linzi Shrine kingdom building -->

# KINGMAKER — THE HALL OF THE UNTITLED OPUS
## KM_Leliana_Hall (inline) | Active: Ch2+ (Realm Tier 2) | Condition: leliana_chronicler_mode = TRUE

---

> **DM:** This section activates when `leliana_chronicler_mode = TRUE` AND `leliana_opus_named = TRUE` AND the kingdom has reached Realm Tier 2. The Hall is a voluntary construction — the player proposes it, the kingdom builds it. It is not triggered by a death. It is triggered by a performance.
>
> **CRITICAL FLAGS:**
> - `leliana_chronicler_mode = TRUE` — prerequisite (Leliana holds the chronicler role)
> - `leliana_opus_named = TRUE` — prerequisite (player gave the opus its name in Beat 2)
> - `hall_proposed = TRUE` — set when player initiates construction
> - `hall_built = TRUE` — set when construction completes
> - `leliana_opus_performed = TRUE` — set at companion quest Beat 4; activates landmark tier
> - `hall_landmark = TRUE` — set after first foreign dignitary visit post-performance
> - `linzi_primary_chronicler = FALSE` — must be false; mutual exclusion with Linzi Shrine

---

## 🎵 QUEST TRIGGER — THE PERFORMANCE PROPOSAL

Unlike the Linzi Shrine, the Hall is not born from loss. It is born from the moment the expedition becomes something worth commemorating in stone.

The trigger fires after `leliana_opus_performed = TRUE` (companion quest Beat 4 — Leliana's first public performance of the Verse). Within one kingdom turn of that event:

> *The throne room feels different after the concert. Not quieter — fuller. As if the air retained the last chord.*
> *Leliana is at the far end of the room, running her hands along the lute strings, re-tuning by ear. She does not look up when you approach.*
>
> **Leliana:** *"You know what the trouble with a performance is, child? It ends. The moment ends. The piece ends. The room forgets it by morning — and I have outlived more rooms than you'd credit."*
>
> *She finally looks up. The easy warmth has gone quiet and serious — the way it does when she means a thing all the way down.*
>
> **Leliana:** *"I'm not asking for anything. I just think — if a kingdom is going to keep a chronicle, it should have a place where the chronicle lives. Somewhere the music doesn't end just because the hand leaves the strings."*
>
> *A beat.*
>
> **Leliana:** *"That's all. That's the whole thought."*

**Player may respond:**
- "I'll have it built." → `hall_proposed = TRUE`; construction begins
- "What would you want it to be called?" → She: *"Whatever you want. I named the piece. The building is yours."* → player may name it (stored as `hall_name`; defaults to `"Hall of the [leliana_opus_name]"`)
- "Not right now." → quest waits; she nods and says nothing more; trigger re-fires at next major kingdom milestone

---

## 🏛️ THE HALL — CONSTRUCTION

**Requirement:** Realm Tier 2+, `leliana_chronicler_mode = TRUE`, `leliana_opus_named = TRUE`

**Without existing Bardic College or Conservatory:** 10 RP and 40 days. A dedicated concert hall with a Ballad Vault beneath it — shelved archives of composed works, performances recorded in notation. Designed for the living chronicle, not religious purpose.

**With existing Bardic College (max tier):** 6 RP and 20 days. The Hall becomes an attached wing of the College — the archive and the academy share a building. Leliana finds this deeply appropriate. She does not say so.

**Construction event:** Three days before completion, musicians from the capital begin arriving at the construction site uninvited. They play outside. Nobody organized this. Nobody asked them to. By the final day there are eleven of them. `hall_spontaneous_musicians = TRUE`

> *When the last stone is set, Leliana walks in alone. She stays for twenty minutes. She comes out and says:*
> **Leliana:** *"The acoustics are perfect. I don't know how. They're just perfect."*

---

## 🎼 THE SCORE VAULT — WHAT LIVES INSIDE

The Hall has two levels:

**Upper level — The Performance Hall:**
Open to the public. Concerts occur here monthly (automatic Culture event). The Verse is performed on the first of each month if Leliana is present in the kingdom. If Leliana is on expedition, the Hall's resident musicians perform an arrangement from the Ballad Cycle.

**Lower level — The Ballad Vault:**
The full Ballad Cycle in physical form. Each entry from `leliana_ballad_cycle` corresponds to a bound score on the shelves. Pages glow faintly with harmonic residue — anyone who reads a score hears a ghost of the original performance (ambient, 10 seconds, non-magical).

The Vault is accessible to scholars, visiting diplomats, and — eventually — to the player in a special menu:

```
.vault command (when player is at the Hall):
Output: Ballad Vault contents (same as .score, plus building notes)
Each entry: [N] "[title]" — [scene description] — [date, if known]
Example:
  [1] "Overture for a House on Fire" — the night of Jamandi's banquet — Day 1
  [2] "First Movement: Stolen Land" — the party's first hex claimed — Day 14
  ...
```

---

## 🌟 HALL EFFECTS — KINGDOM MECHANICS

**Passive (always active while Hall stands):**

| Effect | Value | Notes |
|---|---|---|
| Culture per turn | +2 | Living chronicle reputation |
| Stability per turn | +1 | Cultural anchor; citizens know the story |
| Loyalty per turn | +1 | The chronicle is *about them*; they recognize themselves in it |
| All Stability/Culture events | +1 bonus | "Living chronicle" reputation modifier applies to all such rolls |

**Note:** The +1 bonus to all Stability/Culture events represents the kingdom's reputation as a place with a living historical witness. Diplomats and merchants give more credit to a kingdom whose chronicle is ongoing, not archived.

**Active (once per kingdom arc, player-triggered):**

**"THE CHRONICLE SPEAKS"** — Leliana performs a new composition at the Hall publicly before a specific negotiation, crisis, or court event.
- Roll Performance DC 18 (Leliana's modifier applies)
- Success: the target event's DC is reduced by 4 (the chronicle shifts perception — foreign parties arrive already sympathetic to your story)
- Critical success: DC reduced by 8; the opposing party asks to hear more. Leliana's approval +1.
- Failure: no effect; normal DC
- Costs: one kingdom turn (Leliana is occupied composing and performing)

---

## 🏆 LANDMARK TIER — AFTER leliana_opus_performed = TRUE

When the companion quest Beat 4 is complete AND the Hall is built, the Hall becomes a **kingdom landmark** within one turn:

> *A delegation from the Rostland Court arrives. Their herald asks, with evident rehearsal:*
> **Herald:** *"We heard there is a bard here whose work chronicles the founding of a kingdom in real time. The Sword Lords wish to hear it."*

`hall_landmark = TRUE`

**Landmark effects (permanent additions to passive):**

| Effect | Value |
|---|---|
| Fame per turn | +1 |
| Diplomatic relations | All River Kingdom factions +1 disposition on first contact |
| Foreign dignitary visits | 1d4 visiting nobles per 6 turns (Economy +1 per visit, automatic) |
| Rival kingdoms | Pitax/Brevoy may attempt to commission Leliana directly — player can allow or refuse |

**If a rival kingdom attempts to commission Leliana:**
```
PLAYER CHOICE:
  Allow → Leliana composes one piece for them. She makes it complimentary but not flattering.
           Rival faction disposition +1; Leliana approval −1 (she didn't want to; she did it anyway)
  Refuse → Leliana: "Good. I don't write on commission." Approval +1.
  "Ask Leliana" → She: "Whatever you think is right." [defers to player; no approval change]
```

---

## 💾 THE HALL AND THE OPUS — SAVE BLOCK FLAGS

Add to SaveBlock_Template.md:

```json
"leliana_hall": {
  "hall_proposed": false,
  "hall_built": false,
  "hall_name": "",
  "hall_landmark": false,
  "hall_spontaneous_musicians": false,
  "vault_accessible": false,
  "chronicle_speaks_used": false,
  "rival_commission_attempted": false,
  "rival_commission_accepted": false
},
"leliana_opus": {
  "opus_named": false,
  "opus_name": "",
  "opus_performed": false,
  "opus_print_item": false
}
```

**Mutual exclusion flag (set at gate):**
```json
"chronicler_building": {
  "linzi_shrine_available": true,
  "leliana_hall_available": false,
  "linzi_shrine_built": false,
  "leliana_hall_built": false
}
```

If `leliana_chronicler_mode` becomes true mid-playthrough (Linzi dismissed): `linzi_shrine_available` flips to `false`, `leliana_hall_available` flips to `true`. If Linzi Shrine was already built: it remains but the Hall cannot be built. If neither was built: mutual exclusion applies.

---

## 📊 COMPARISON TABLE — LINZI SHRINE VS LELIANA HALL

| | Linzi Shrine of Returning | Hall of the Unfinished Verse |
|---|---|---|
| **Trigger** | Linzi's death (Ch6) | Leliana's death (Ch6) — she inherits Linzi's death arc, medium-swapped (the old "first public performance" trigger is SUPERSEDED) |
| **Availability** | `linzi_primary_chronicler = TRUE` | `leliana_chronicler_mode = TRUE` |
| **Tone** | Grief and resurrection | Grief and resurrection (same as Linzi, re-skinned to music) |
| **Cost (no existing temple/college)** | 6–10 RP / 21–45 days (varies by god) | 10 RP / 40 days |
| **Cost (max existing building)** | 3–5 RP / 10–20 days (varies by god) | 6 RP / 20 days |
| **Alignment resonance** | Good / Neutral / Evil (player's choice of god) | Neutral (no alignment requirement) |
| **Passive kingdom bonus** | Varies by god; shrine-specific | +2 Culture, +1 Stability, +1 Loyalty, +1 all Stability/Culture events |
| **Active power** | Varies by god; resurrection-focused | "The Chronicle Speaks" — reduce event DC by 4–8 |
| **Landmark tier** | N/A | Yes — fires after `leliana_opus_performed = TRUE` |
| **Landmark effects** | N/A | +1 Fame/turn, foreign dignitary visits, diplomatic +1 |
| **Can fail?** | Yes (price-dependent) | Only if player never triggers Beat 4 of Leliana's quest |
| **Mutual exclusion** | Yes — cannot build if `leliana_chronicler_mode = TRUE` | Yes — cannot build if `linzi_primary_chronicler = TRUE` |

---

*KM_Leliana_Hall (inline) — Kingmaker PF2e Text Adventure | Leliana Concert Hall / Ballad Vault v1.0*
