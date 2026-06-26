# KINGMAKER — CHAPTER 2 PART 2: SEASON OF BLOOM
## KM_Ch2_P2.md | Continuation of: KM_Ch2.md

> **DM:** This file covers Phases 5–8: the Season of Bloom questline, Tristian's betrayal revelation, the Bald Hilltop resolution, chapter end, and the Ch2 Export Block.
> Load alongside: KM_Ch2.md, KM_Exploration.md, KM_Bestiary.md, KM_Leveling.md, and all standard files.

---

## 📍 PHASE 5 — SEASON OF BLOOM BEGINS

### The Ancient Curse Triggers

> *The season changes. Something changes with it.*
>
> *Plants along the road are dying — not from frost or drought. Something is eating them from within. Your advisors are worried. Jhod Kavken comes to the throne room with his hands shaking.*
>
> **Jhod:** *"Something is wrong with the land itself. I have felt it for weeks. It began in the north — near the Bald Hilltop. It is spreading."*

**Throne Room Event — Cultist Random Encounter:**
Triggers during overland travel soon after Troll Trouble resolution. A group of cultists attacks — one transforms into an owlbear mid-fight.

```
CULTISTS (×5):
  Cultist Fighter 6 (leader): HP 62 | AC 18 | Longsword d20+10
  Cultist Fighter 3: HP 32 | AC 16 | Longsword d20+7 (dies quickly, replaced)
  Cultist Archer 2: HP 22 | AC 14 | Composite Shortbow d20+6
  Cultist Rogue 2 (×2): HP 18 | AC 15 | Shortsword d20+6 | Sneak Attack +1d6

  OWLBEAR (summoned when Cultist Fighter 3 dies):
  HP: 85 | AC: 18 | Speed: 35 ft
  Beak: d20+11 (1d10+7 P) | Talon ×2: d20+11 (1d8+7 S)
  Grab on Beak hit — target Grabbed

XP: 480 total
NOTE: This encounter repeats periodically until Tristian's quest is resolved.
```

**After the encounter:**
> **Tristian** (if in party): *"I know this cult. I've seen their symbol before. It's connected to... something I need to tell you."*
> He stops himself. He's not ready. But the flag is set: `tristian_confession_imminent = TRUE`

---

### The Bald Hilltop — Part 1

**Quest: An Ancient Curse, Part One**
Located northeast of the capital. A barren hilltop with a dead tree and a stone circle.

> *The grass on the hilltop is black. Not burned — blackened, like something sucked all life from it. The stone circle at the summit pulses faintly with something that is not magic so much as its absence.*

**Encounter:**
```
Wyvern ×2 (guardian creatures, drawn to the corruption):
  HP: 72 each | AC: 19 | Speed: 20 ft, Fly 60 ft
  Jaws: d20+11 (1d10+7 P) | Stinger: d20+11 (1d6+7 P + Poison)
    Wyvern Venom: Fort DC 17, 2d6 poison, Enfeebled 1 on fail
  XP: 240 each = 480 total

After clearing wyverns: examine the stone circle (Arcana or Occultism DC 14)
  Success: "This is a seed point. Something was planted here, magically, years ago.
            It's been growing underground ever since. The hilltop is just where it
            breaks the surface."
  Critical Success: "Whoever planted this had help from within your kingdom.
                     They knew this land intimately."
```

**Reward:** 2,800 gp if enemies cleared before the Ancient Curse Part One deadline.
`bald_hilltop_p1_cleared = TRUE`

---

### Tristian's Confession — Kingdom of the Cleansed

**Trigger:** ~34 days before Ancient Curse Part 2 deadline. Tristian requests a private meeting.

> *He is waiting in the throne room at dawn. He looks like he hasn't slept.*
>
> **Tristian:** *"I have to tell you something. And I need you to hear all of it before you decide what you do with it."*

**The Confession:**

> *"Before I came to your kingdom... I served a goddess. Not Sarenrae. A different being. She called herself the Lantern King's sister. She gave me power I had never felt before. She told me to plant seeds — literal seeds, she said. That they would help the land grow. I believed her. I was young. I was desperate for purpose."*
>
> *"The seeds I planted are the source of the Bloom. The dying plants. The corrupted creatures. I didn't know. But my ignorance doesn't make people less dead."*
>
> *His hands are clasped in his lap. He is not defending himself. He is simply telling you the truth and waiting for whatever comes next.*

**THE CHOICE — Companion Alignment Gate:**

```
FORGIVE: "You were deceived. That matters."
  → tristian_quest = forgiven
  → He remains in party. His powers evolve from genuine redemption.
  → Sarenrae's light grows stronger in him — gains Healer's Blessing improvement.
  → +2 Relationship

CONDEMN: "You planted the seeds. People are dying. I can't trust you."
  → tristian_condemned = TRUE
  → He accepts it. Leaves quietly.
  → Can be re-recruited in Ch4 after a separate encounter (see Companion Notes)
  → Party loses their best healer if no other healer present

INVESTIGATE FIRST: "I need to verify this before I decide."
  → Available if bald_hilltop_p1_cleared = TRUE (player has the seed evidence)
  → Lore (Religion) DC 14: confirms his account is credible
  → Then make the Forgive/Condemn choice with better information
  → No alignment penalty for investigating first
```

`tristian_betrayal_revealed = TRUE` — this flag carries through all chapters.

---

## 📍 PHASE 6 — SEASON OF BLOOM MAIN EVENTS

### Monster Invasion (Scripted Kingdom Event)

> *At dawn, the alarm bells ring.*

Monsters transformed by the Bloom attack the capital. Must be fought in the throne room area — this is not optional.

```
CAPITAL DEFENSE ENCOUNTER:
  Bloom-Touched Owlbear (Leader): HP 95 | AC 20 | Jaws+Talons, Grab
  Bloom-Infected Wolf ×4: HP 28 | AC 15 | Jaws d20+7 (1d8+4)
  Bloom-Touched Bandit (human, partially transformed): HP 38 | AC 16 | Chaos

XP: 640 total
After combat: Linzi scribbles furiously.
  "I'm calling this chapter 'The Bloom.' No — 'The Season of Screams.' 
   Working title."
```

**Kingdom damage:** If player is not in the capital when this triggers — Stability −2, Loyalty −1. If present and fights: no damage, +100 XP for defending.

---

### The Goblin Fort and Womb of Lamashtu

**Investigation path:** The Bloom source is being actively channeled through a Lamashtu cult network. Two key locations:

**Goblin Village (Shrike Hills):**
- Nok-Nok's old tribe is here (triggers his personal quest if recruited)
- Bloom-corrupted goblin elder is the village's problem — not hostile if player is diplomatic
- Diplomacy DC 14: learn about the "mother of monsters" rituals feeding the Bloom
- Kill the elder: goblins scatter. Slightly more Bloom activity short-term.

**Goblin Fort:**
```
GOBLIN FORT — Season of Bloom cultists using goblins as cover
  Enemies: Cultist Leader (Cleric 7 of Lamashtu): HP 74 | AC 20 | Spells: Harm, Spiritual Weapon
           Branded Cultist ×4: HP 42 | AC 17 | Falchion d20+9
           Goblin Shaman ×2: HP 28 | AC 14 | Spells: Produce Flame, Bane
  XP: 860 total
  Loot: Periapt of Wound Closure, Cloak of Resistance +2, 340 gp, Bloom Seed Fragment
        (story item — confirms Tristian's account even if he already confessed)
```

---

### The Bald Hilltop — Part 2 (Resolution)

**Quest: An Ancient Curse, Part Two**
Return to the Bald Hilltop with the Bloom Seed Fragment and/or Tristian (if still in party).

> *The dead tree at the summit is moving.*
> *Not in wind. Something inside it.*

**Final Encounter:**

```
BLOOM MANIFESTATION (nature horror, not a creature with intelligence):
  HP: 140 | AC: 16 (not armored — it's a plant-creature mass)
  Tendril Slam ×3: d20+10 (2d6+7 B, Reach 15 ft)
  Spore Cloud (Aura 10 ft): Fort DC 16 or Sickened 1 each round inside
  WEAKNESS: Fire damage (double damage). Tristian's positive energy spells (Heal) deal +4d6.
  XP: 720

AFTER COMBAT — Moral Choice:
  Purify the site (requires Religion DC 15 or Tristian present):
    → Bald Hilltop becomes a healing ground (+2 Culture to nearby settlements)
    → tristian_healing = TRUE if he was present
  Abandon it:
    → Site remains dead but inert
  Claim it for kingdom use (dark):
    → Brief Economy boost, permanent Unrest +2 from cursed land influence
```

**Reward for completing Part 2:** 6,500 gp (from kingdom coffers — Linzi and Tristian report it), +900 XP. `bloom_resolved = TRUE`

---

## 📍 PHASE 7 — CHAPTER RESOLUTION

### A Noble's Amusement (Optional but Recommended)

**Triggered:** ~11 days before Ancient Curse Part 2 deadline. Noble invitation to your court.

> *Lady Aldori sends a courier: a group of Rostland nobles wishes to visit your court. "Show them something impressive," she writes. "They are considering backing your kingdom's expansion."*

**Storybook event:** Player must organize entertainment, a feast, and demonstrations for the visiting nobles. Three skill checks:
- Performance or Crafting DC 16 → entertainment quality
- Diplomacy DC 15 → how well the feast is managed  
- Warfare Lore or Society DC 14 → military demonstration

Outcomes:
- 3 successes: +2 Stability, +800 gp, +1 Fame, `noble_patrons = TRUE`
- 2 successes: +1 Stability, +400 gp
- 1 or fewer: no benefit, minor reputation hit

---

### Return to Jamandi

**Triggered after Bloom resolution.** Optional visit to Restov.

> *Jamandi receives you in her private study. Her expression is difficult to read.*
>
> **Jamandi:** *"You've dealt with the trolls. You've survived the Bloom. I'll be honest — I didn't expect this to last the first winter. You've surprised me."*

She provides:
- Kingdom funding: +1,500 gp
- Political intelligence: "Irovetti of Pitax is watching your kingdom. Closely."
- If `nyrissa_letter_found = TRUE`: *"That letter you found. I had it analyzed. The magic on it is old. Older than Pitax. Older than Brevoy. Whatever is interested in your kingdom — it isn't human."*

`jamandi_ch2_meeting = TRUE`

---

## 📊 CHAPTER 2 COMPLETE XP SUMMARY

| Source | XP |
|--------|----|
| Troll Trouble (KM_Ch2.md) | ~5,100 |
| Cultist encounter (×1 at minimum) | 480 |
| Bald Hilltop Part 1 (wyverns + checks) | 600 |
| Tristian investigation/choice | 200 |
| Monster Invasion defense | 640 |
| Goblin Fort | 860 |
| Bald Hilltop Part 2 (Bloom Manifestation) | 720 |
| Lost Child quest | 320 |
| Noble's Amusement (if done) | 300 |
| Side content, exploration | ~600 |
| **Chapter 2 Total** | **~10,180 XP** |

**Level benchmarks:**
- Level 5: 6,000 XP — roughly at Trobold entrance
- Level 6: 10,000 XP — around Hargulka fight
- Level 7: 15,000 XP — mid Season of Bloom
- Level 8: 21,000 XP — after chapter completion

---

## 🔀 CHAPTER 2 KEY RESOLUTION FLAGS

| Decision | Options | Ch3+ Impact |
|----------|---------|-------------|
| Hargulka fate | `killed` / `vassal` | Vassal → Ekundayo leaves |
| Tartuk/Tartuccio fate | `fled` / `vassal` / `defeated` | All lead to Ch3 appearance |
| Tristian decision | `forgiven` / `condemned` | Condemned → absent Ch3-4 unless re-recruited |
| Bloom resolution | `purified` / `abandoned` / `claimed` | Affects kingdom stats Ch3+ |
| Ekundayo status | `recruited` / `left_hargulka` / `never_recruited` | Ch7 survival requires quest |
| Noble visit | `done` / `skipped` | Patron support affects Ch5 war resources |

---

> **⛔ HARD STOP — Chapter 2 ends when BOTH Troll Trouble AND Season of Bloom are resolved (`bloom_resolved = TRUE` AND `hargulka_fate` is set). Before any Chapter 3 content — before Varnhold messenger, before any new scene — output the export block below. Say: *"Chapter 2 is complete. Copy the block below and save it. Type `.continue` when saved."* Wait for confirmation. VIOLATION = `.fail 16`.**

---

## 💾 CHAPTER 2 → CHAPTER 3 EXPORT

````json
{
  "save_version": "1.0",
  "export_from": "chapter_2",
  "import_to": "chapter_3",
  "export_date_ingame": "",

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
      "hp_current": 0, "hp_max": 0, "relationship": "Friendly", "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "Ekundayo", "status": "active_party_OR_left",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "Tristian", "status": "active_party_OR_condemned",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral",
      "notes": "If condemned: tristian_condemned = TRUE, not in party" }
  ],

  "kingdom": {
    "name": "", "capital_location": "", "turn": 0, "size": 0,
    "culture": 0, "economy": 0, "loyalty": 0, "stability": 0,
    "unrest": 0, "fame": 0, "infamy": 0, "treasury_rp": 0,
    "leadership_roles": {}, "settlements": [], "armies": [],
    "claimed_hexes": [], "roads": []
  },

  "story_flags": {
    "carried_from_ch1": {
      "stag_lord_fate": "", "nyrissa_letter_found": false,
      "nyrissa_early_contact": false, "akiros_fate": "",
      "tartuccio_journal_found": false, "alignment_track": {},
      "bokken_relationship": "neutral",
      "tiressia_met": false,
      "nettles_crossing_resolved": false,
      "old_beldame_met": false,
      "jubilost_helped": false,
      "sootscale_alliance": false,
      "svetlana_ring_returned": false,
      "oleg_expanded": false
    },
    "chapter_2": {
      "hargulka_fate": "",
      "jazon_escort": false,
      "jazon_spared": false,
      "tartuk_ch2_fate": "",
      "tartuccio_ch2_confronted": true,
      "ekundayo_recruited": false,
      "ekundayo_quest": "",
      "kargadd_killed": false,
      "harrim_statue_check": false,
      "tristian_betrayal_revealed": true,
      "tristian_decision": "",
      "tristian_healing": false,
      "bloom_resolved": true,
      "bald_hilltop_resolution": "",
      "verdant_chambers_visited": false,
      "bartholomew_met": false,
      "troll_weakness_known": false,
      "stefano_survived": false,
      "noble_patrons": false,
      "jamandi_ch2_meeting": false,
      "noknok_quest_triggered": false,
      "linzi_quest_triggered": false,
      "side_quests": {
        "lost_child": false,
        "cog_wheel_rings": false,
        "bokken_brother": false,
        "nature_of_beast": false
      }
    },
    "tartuccio": {
      "tartuccio_ch2_fate": "fled_to_varnhold_region",
      "tartuccio_journal_ch2": false,
      "tartuccio_knows_player_is_aware": false
    },
    "nyrissa": {
      "nyrissa_awareness": "passive_OR_active",
      "nyrissa_bloom_connection_known": false,
      "nyrissa_identity_known": false
    },
    "alignment_track": {
      "lawful_chaotic_axis": "neutral",
      "good_evil_axis": "neutral",
      "notable_choices": []
    },
    "relationships": {
      "jamandi": "neutral", "kassil": "neutral",
      "kesten": "neutral", "oleg": "neutral",
      "ekundayo": "neutral", "bartholomew": "neutral",
      "tiressia": "neutral", "hargulka": "dead_OR_vassal"
    },

    "npc_threads": {
      "Amiri":     { "thread": "She asked about the bread roll. He said a disarmed soldier is useless. She's been sitting with the word *disarmed* ever since.", "priorities": [
        { "weight": 55, "instruction": "Disarmament question active — Stage 1. Think/test alone in quiet moments. Stage 2 = first actual disarm: one beat pause, then reach for nearest object. Stage 3 = occasional first choice even when sword is available. Never skip the beat. Track stage toward amiri_disarm_resolved.", "source": "road south — eRmaC told her a disarmed soldier is useless" }
      ] },
      "Linzi":     { "thread": "", "priorities": [] },
      "Valerie":   { "thread": "", "priorities": [] },
      "Harrim":    { "thread": "", "priorities": [] },
      "Jaethal":   { "thread": "", "priorities": [] },
      "Tristian":  { "thread": "", "priorities": [] },
      "Ekundayo":  { "thread": "", "priorities": [] },
      "Kesten":    { "thread": "", "priorities": [] },
      "Jamandi":   { "thread": "", "priorities": [] },
      "Oleg":      { "thread": "", "priorities": [] },
      "Nok-Nok":   { "thread": "", "priorities": [] },
      "Lem":       { "thread": "", "priorities": [] },
      "Octavia":   { "thread": "", "priorities": [] },
      "Regongar":  { "thread": "", "priorities": [] }
    },

    "world_state": {
      "troll_trouble_resolved": true,
      "season_of_bloom_resolved": true,
      "pitax_watching": true,
      "varnhold_silent": false,
      "nyrissa_next_move": "varnhold_vanishing",
      "public_reputation": 0,
      "reputation_tier": "UNKNOWN",
      "reputation_deeds": [],
      "reputation_notes": ""
    }
  },

  "quest_log": {
    "completed": [
      { "name": "Troll Trouble", "result": "", "xp": 0 },
      { "name": "Season of Bloom / Ancient Curse", "result": "", "xp": 0 }
    ],
    "active": [
      { "name": "The Varnhold Vanishing",
        "objective": "Varnhold has gone silent. Investigate.",
        "notes": "Chapter 3 begins with a messenger arriving with no news from Varnhold." }
    ]
  }
}
````

---

## 📥 HOW TO LOAD CHAPTER 3

**Paste at start of Chapter 3 chat:**
```
Loading Chapter 3 of Pathfinder 2e Kingmaker.

Files to load:
KM.txt, KM_Builds.md, KM_Actions.md, KM_Commands.md, KM_Commands_Maps.md,
KM_Commands_P2.md, KM_Companions.md, KM_Companions_B.md,
KM_Map.md, KM_Kingdom.md, KM_Ch3.md

[PASTE CH2 JSON EXPORT HERE]
```

---

*KM_Ch2_P2.md — Kingmaker PF2e Text Adventure | Chapter 2 Part 2 v1.0*
