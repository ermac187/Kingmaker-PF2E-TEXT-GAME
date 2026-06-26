# KINGMAKER — CHAPTER 3: THE VARNHOLD VANISHING
## KM_Ch3.md | Loads after: KM_Ch2_P2.md export | Loads before: KM_Ch4.md

---

> **DM:** Load with KM.txt, KM_Companions.md, KM_Companions_B.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md, KM_Leveling.md.
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
