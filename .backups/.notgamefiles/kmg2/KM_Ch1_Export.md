# KINGMAKER — CHAPTER 1 EXPORT & CHAPTER 2 LOAD
## KM_Ch1_Export.md | Transition: Ch1 → Ch2

---

## ⚠️ DM INSTRUCTION — WHEN TO OUTPUT THIS

### ⛔ HARD STOP — DO NOT BEGIN CHAPTER 2 UNTIL THIS BLOCK IS OUTPUT AND SAVED

Output this block when ALL of the following are true:
1. The Stag Lord has been defeated (any method)
2. The player has returned to Oleg's Trading Post
3. The Kingdom Founding sequence has triggered
4. The player has selected their capital location

**Before any Chapter 2 content — before troll raid reports, before road travel, before any scene outside Oleg's post-founding — output this block.**

Say exactly: *"Chapter 1 is complete. Copy everything between the markers below and save it. You will paste this into your Chapter 2 session."*

**Then immediately: Run the Best Run scoring per KM_BestRun.md.** Compare against stored best. If new record → display full scorecard + auto-output Best Run block with paste instructions. If not a record → one line: *"Run score: X/200. Your best: Y/200."* No block, no scorecard.

Then say: *"Type `.continue` when saved."*
Wait for `.continue`.

**VIOLATION:** Any Chapter 2 content written before this block is output and confirmed = `.fail 16` + unrecoverable save data loss.

---

## ⛔ PRE-EXPORT AUDIT — OUTPUT THIS BEFORE THE SAVE BLOCK

> **⛔ DM: Fill and output this audit FIRST. Save block without preceding audit = `.fail 9`.**

```
SAVE BLOCK AUDIT — fill from session, not from template defaults:

□ HP: __/__ (final battle, not reset) | XP: ____ | Gold: __ gp | Hero Points: __ (don't reset)
□ Conditions: [active or "none"] | Inventory: __ weapons, __ armor, __ consumables, __ gear, __ quest items
□ Story flags changed: [flag: old→new] for every flag that changed — min 3 if events occurred
□ Companion relationship changes: [name: X→Y] for each that moved | HP filled for all active
□ Companion memory[]: filled for every companion spoken to — empty memory = session erased
□ NPC threads: thread + memory[] for every NPC spoken to — not filled = that NPC reset on reload
□ Kingdom stats: culture/economy/loyalty/stability all filled if kingdom turn ran — not 0
□ Zero-check: no numeric field reads 0 unless it was genuinely 0 in play
□ Field count: story_flags = 12 top-level sections | companions = entry for every active + bench companion
⛔ NEVER REMOVE: kingdom · hexes · npc_threads · nyrissa · world_state · ending_flags · carried_from_prologue · companion_quests · alignment_track · player.skills · player.speed · player.perception · player.class_features

All confirmed → output save block.
```

---

## 📤 FILL AND OUTPUT THIS BLOCK

````json
{
  "save_version": "1.0",
  "export_from": "chapter_1",
  "import_to": "chapter_2",
  "export_date_ingame": "",
  "days_elapsed_ch1": 0,
  "ch1_speed_bonus": false,

  "player": {
    "name": "",
    "build_id": "",
    "ancestry": "",
    "class": "",
    "subclass": "",
    "background": "",
    "level": 0,
    "xp": 0,
    "xp_to_next": 0,
    "attributes": {
      "str": 0, "dex": 0, "con": 0,
      "int": 0, "wis": 0, "cha": 0
    },
    "hp_current": 0,
    "hp_max": 0,
    "hero_points": 1,
    "ac": 0,
    "speed": 0,
    "perception": 0,
    "saves": { "fort": 0, "ref": 0, "will": 0 },
    "conditions": [],
    "skills": {},
    "feats": [],
    "spells": {
      "tradition": "",
      "spell_dc": 0,
      "spell_attack": 0,
      "cantrips": [],
      "slots": {},
      "focus_points": { "current": 0, "max": 0 },
      "focus_spells": []
    },
    "class_features": [],
    "inventory": {
      "weapons": [],
      "armor": [],
      "shields": [],
      "magic_items": [],
      "consumables": [],
      "gear": [],
      "quest_items": []
    },
    "gold": { "gp": 0, "sp": 0, "cp": 0 },
    "bulk_carried": 0
  },

  "companions": [
    {
      "name": "Amiri",
      "status": "active_party",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "ac": 0,
      "hero_points": 1,
      "relationship": "Friendly",
      "conditions": [],
      "equipped_items": [],
      "notes": "", "thread": "", "priorities": []
    },
    {
      "name": "",
      "status": "active_party",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "ac": 0,
      "hero_points": 1,
      "relationship": "Neutral",
      "conditions": [],
      "equipped_items": [],
      "notes": "", "thread": "", "priorities": []
    },
    {
      "name": "",
      "status": "active_party",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "ac": 0,
      "hero_points": 1,
      "relationship": "Neutral",
      "conditions": [],
      "equipped_items": [],
      "notes": "", "thread": "", "priorities": []
    },
    {
      "name": "Tristian",
      "status": "available_at_base",
      "level": 0,
      "hp_current": 0,
      "hp_max": 0,
      "relationship": "Friendly",
      "notes": "Recruited at Temple of the Elk if player visited. Waiting at Oleg's/Capital."
    }
  ],

  "kingdom": {
    "name": "",
    "capital_location": "",
    "capital_coords": [0, 0],
    "founded_date": "",
    "turn": 1,
    "size": 1,
    "culture": 0,
    "economy": 0,
    "loyalty": 0,
    "stability": 0,
    "unrest": 0,
    "fame": 0,
    "infamy": 0,
    "treasury_rp": 0,
    "consumption": 0,
    "leadership_roles": {
      "ruler": "",
      "councilor": "",
      "general": "",
      "grand_diplomat": "",
      "high_priest": "",
      "magister": "",
      "marshal": "",
      "royal_enforcer": "",
      "spymaster": "",
      "treasurer": "",
      "warden": ""
    },
    "settlements": [
      {
        "name": "",
        "coords": [0, 0],
        "size": "Village",
        "population": 0,
        "buildings": [],
        "defense_ac": 15,
        "defense_hp": 20,
        "morale": 50
      }
    ]
  },

  "hexes": [
    {
      "coords": [1, 0],
      "name": "Oleg's Trading Post",
      "status": "controlled",
      "cleared": true,
      "scripted_encounter_done": true,
      "notes": "Kesten Garess stationed here. Oleg/Svetlana vendors active."
    }
  ],

  "story_flags": {

    "carried_from_prologue": {
      "gate_entry": "",
      "malak_bribe_evidence": false,
      "parchment_source": "pitax",
      "malak_arrested": false,
      "malak_broke_first": false,
      "malak_found_letter_himself": false,
      "kesten_searched_malak": false,
      "player_clean_hands": false,
      "second_hero_witnessed": false,
      "malak_deal_made": false,
      "tartuccio_knows_player_is_aware": false,
      "rebuttal_result": "",
      "kassil_first_impression": "neutral",
      "kesten_respect": false,
      "arrived_with_kassil": false,
      "prison_arc": false,
      "harrim_chaotic_bond": false,
      "tartuccio_ring": "",
      "tartuccio_gold": ""
    },

    "chapter_1": {
      "ch1_opening_path": "",
      "days_elapsed": 0,
      "speed_bonus_earned": false,
      "stag_lord_fate": "",
      "stag_lord_head_sent_to_jamandi": false,
      "nyrissa_letter_found": false,
      "nyrissa_early_contact": false,

      "ancient_tomb": {
        "visited": false,
        "companion_recruited_back": false,
        "companion_name": "",
        "tomb_explored": false
      },

      "thorn_ford": {
        "visited": false,
        "kressle_fate": "",
        "akiros_turned": false,
        "svetlana_ring_recovered": false
      },

      "temple_elk": {
        "cleared": false,
        "tristian_recruited": false,
        "jhod_settled": false
      },

      "old_sycamore": {
        "visited": false,
        "kobold_resolution": "",
        "mite_resolution": "",
        "tartuccio_confronted_ch1": false,
        "tartuccio_journal_found": false,
        "sootscale_alliance": false,
        "companions_rescued_from_cage": false
      },

      "stag_lords_fort": {
        "entry_method": "",
        "dovan_fate": "",
        "auchs_fate": "",
        "akiros_fate": "",
        "nugrah_released": false,
        "kressle_assisted": false
      },

      "side_quests": {
        "bandits_at_olegs": false,
        "oleg_expanded": false,
        "svetlana_ring_returned": false,
        "falgrim_sneeg": "",
        "fangberries_delivered": false,
        "moon_radishes_delivered": false,
        "scythe_tree_defeated": false,
        "tiressia_met": false,
        "nettles_crossing_resolved": false,
        "bokken_relationship": "neutral",
        "jubilost_helped": false,
        "old_beldame_met": false,
        "tuskgutter_killed": false,
        "kingdom_founded": false,
        "storyteller_available": false
      }
    },

    "tartuccio": {
      "tartuccio_as_tartuk_revealed": false,
      "tartuccio_journal_contents_known": false,
      "tartuccio_location_ch2": "fled_greenbelt",
      "tartuccio_contact_named": false
    },

    "companions": {
      "tristian_recruited": false,
      "nok_nok_available": false,
      "lem_available": false,
      "ekundayo_recruited": false,
      "prologue_companions_recovered": []
    },

    "companion_quests": {
      "amiri_quest": "inactive",
      "amiri_quest_stage": 1,
      "linzi_quest": "inactive",
      "valerie_quest": "inactive",
      "harrim_quest": "inactive",
      "tristian_quest": "inactive",
      "tristian_betrayal_revealed": false,
      "jaethal_quest": "inactive",
      "octavia_quest": "inactive",
      "regongar_quest": "inactive",
      "noknok_quest": "inactive",
      "lem_quest": "inactive",
      "ekundayo_quest": "inactive",
      "kalikke_kanerah_quest": "inactive"
    },

    "storyteller": {
      "storyteller_available": false,
      "fragments_delivered": 0,
      "coins_delivered": 0,
      "storyteller_collection": "incomplete"
    },

    "alignment_track": {
      "lawful_chaotic_axis": "neutral",
      "good_evil_axis": "neutral",
      "notable_choices": []
    },

    "relationships": {
      "jamandi": "neutral",
      "kassil": "neutral",
      "kesten": "neutral",
      "oleg": "neutral",
      "svetlana": "neutral",
      "jhod": "neutral",
      "akiros": "neutral",
      "kressle": "neutral",
      "sootscale": "neutral"
    },

    "promises_and_debts": [],

    "npc_threads": {
      "Amiri":    { "thread": "", "priorities": [] },
      "Linzi":    { "thread": "", "priorities": [] },
      "Valerie":  { "thread": "", "priorities": [] },
      "Harrim":   { "thread": "", "priorities": [] },
      "Jaethal":  { "thread": "", "priorities": [] },
      "Tristian": { "thread": "", "priorities": [] },
      "Kesten":   { "thread": "", "priorities": [] },
      "Oleg":     { "thread": "", "priorities": [] },
      "Svetlana": { "thread": "", "priorities": [] },
      "Jhod":     { "thread": "", "priorities": [] },
      "Akiros":   { "thread": "", "priorities": [] },
      "Jamandi":  { "thread": "", "priorities": [] }
    },

    "world_state": {
      "stag_lord_defeated": true,
      "stolen_lands_claimed": true,
      "kingdom_founded": true,
      "brevoy_notified": false,
      "maegar_varn_competing": false,
      "time_limit_missed": false,
      "public_reputation": 0,
      "reputation_tier": "UNKNOWN",
      "reputation_deeds": [],
      "reputation_notes": ""
    },

    "nyrissa": {
      "nyrissa_awareness": "passive",
      "nyrissa_backstory_known": false,
      "nyrissa_backstory_partial": false,
      "nyrissa_can_be_saved_hint": false,
      "nyrissa_identity_known": false,
      "nyrissa_bloom_connection_known": false
    }
  },

  "romance": {
    "active_romance": "",
    "romance_score": 0,
    "romance_stage": 0,
    "romance_history": []
  },

  "brotherhood": {
    "active_bonds": [],
    "bond_scores": {},
    "fire_test_completed": []
  },

  "crime": {
    "infamy": 0,
    "active_bounties": [],
    "outstanding_fines": 0,
    "known_crimes": [],
    "witnesses_outstanding": [],
    "fugitive_regions": [],
    "trial_pending": false,
    "last_crime_chapter": null
  },

  "living_world": {
    "party_morale": 5,
    "companion_moods": {},
    "fracture_scene_pending": false
  },

  "found_documents": [],

  "companion_agendas": {},

  "companion_relations": {},

  "incompatibility_countdowns": {
    "jaethal_tristian":  {"count":0,"max":10,"stage":0,"ultimatum_fired":false},
    "jaethal_imrijka":   {"count":0,"max":6, "stage":0,"truce_active":false,"ultimatum_fired":false},
    "regongar_valerie":  {"count":0,"max":8, "stage":0,"ultimatum_fired":false},
    "harrim_tristian":   {"count":0,"max":14,"stage":0,"truce_active":false,"ultimatum_fired":false}
  },

  "npc_relations": {},

  "quest_log": {
    "completed": [
      { "name": "Stolen Land", "result": "Stag Lord defeated", "xp": 0 },
      { "name": "A Bitter Rival", "result": "", "xp": 0 }
    ],
    "active": [
      {
        "name": "Troll Trouble",
        "objective": "Reports of trolls in the Greenbelt. Investigate.",
        "notes": "Chapter 2 begins with first troll encounter near kingdom borders."
      }
    ],
    "failed_or_missed": []
  },

  "resources": {
    "camping_supplies": 0,
    "rations": 0,
    "days_into_ch2": 0,
    "current_hex": "Oleg's Trading Post / Capital"
  },

  "dispositions": { "merciful": 0, "ruthless": 0, "cunning": 0, "blunt": 0, "scholarly": 0 },
  "companion_titles": {},
  "pending_hp_loot_rolls": 0,
  "faction_tiers": { "aldori": 0, "surtova": 0, "kellid": 0, "river_kingdoms": 0, "pitax": 0 },
  "standing_orders": {},
  "adventurer_board": { "posted_bounties": [], "active_missions": [], "completed_reports": [], "guild_upgraded": false },
  "border_raids": { "pending": [], "resolved": [], "consecutive_unanswered": 0 },
  "hex_fortifications": [],
  "crafting": { "known_recipes": [], "materials": {} },
  "mobile_base": { "type": "none" },
  "stronghold_events_completed": [],
  "dream_log": [],
  "dream_cooldown": 0,
  "liminal_visits": 0,
  "liminal_choices": [],
  "scripted_interactions_completed": [],
  "debate_results": [],
  "advisor_intrigue": { "active": [], "detected": [] },
  "quest_conflicts": { "tristian_jaethal": "unresolved", "regongar_valerie": "unresolved", "amiri_ekundayo": "unresolved" },
  "ending_flags": { "nyrissa_saveable": 0, "true_ending_path": false, "golden_ending_eligible": false },
  "prestige": { "l10_choice": null, "l15_choice": null },
  "mythic_path": { "chosen": null, "abilities": [], "power_level": 0 }
}
````

---

## 📝 DM FILL GUIDE — CH1-SPECIFIC FIELDS

**`days_elapsed_ch1`** — Count travel days from Day 1 to chapter end. If ≤ 30: `ch1_speed_bonus = true` → Lord Protector sword added to inventory.

**`stag_lord_fate`** — One of: `killed`, `beheaded_head_sent`, `captured_kesten`, `captured_imprisoned`, `executed_publicly`

**`ch1_opening_path`** — One of: `tomb_first`, `thorn_first`, `neither_yet` (shouldn't happen at export)

**`kobold_resolution`** — One of: `sootscale_allied`, `mites_allied`, `both_wiped`, `neutral_departed`

**`kressle_fate`** — One of: `killed`, `turned_good`, `intimidated_fled`, `escaped`

**`akiros_fate`** — One of: `turned_ally` (in kingdom as advisor), `fought_defeated`, `killed`, `fled`

**`companions_recovered`** — List the names of prologue companions rescued from kobold cage.

**Kingdom fields:** Fill all stats from the first Kingdom Turn if it was run. If not yet run, leave at 0 and note `"turn": 0`.

**`nyrissa_letter_found`** — Only TRUE if player physically found and read the letter in the Stag Lord's Fort treasury.

**`oleg_expanded`** — Set TRUE after the first Kingdom Turn resolves. Controls which vendor table Oleg uses in Ch2. If the first kingdom turn was not run before chapter end, leave FALSE.

---

## 📥 HOW TO LOAD CHAPTER 2

**PASTE THIS at the start of your Chapter 2 chat:**

```
Loading Chapter 2 of the Pathfinder 2e Kingmaker text game.

Files: KM.txt, KM_Builds.md, KM_Actions.md, KM_Leveling.md
       KM_Commands.md, KM_Commands_Maps.md, KM_Commands_P2.md
       KM_Companions.md, KM_Companions_B.md
       KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md
       KM_Ch2.md, KM_Ch2_P2.md

Import my Chapter 1 save below. Show Game State Header before any scene.

[PASTE YOUR CH1 JSON EXPORT HERE]
```

---

## 📋 CHAPTER 2 LOAD CHECKLIST

```
[GM CHAPTER 2 LOAD CHECK]
□ All files loaded
□ Ch1 JSON Export imported and parsed
□ Player level, XP, and inventory confirmed
□ Kingdom state confirmed — turn count, stats, capital
□ Hex map state restored — controlled/discovered hexes noted
□ Companion roster confirmed — active party + bench
□ Story flags read and noted:
    stag_lord_fate          : [value]
    nyrissa_letter_found    : [TRUE/FALSE]
    nyrissa_early_contact   : [TRUE/FALSE]
    sootscale_alliance      : [TRUE/FALSE]
    akiros_fate             : [value]
    tartuccio_location_ch2  : fled_greenbelt
    alignment_track         : [both axes]
    relationships           : [key NPCs]
□ Active quests confirmed — Troll Trouble is primary Ch2 quest
□ Kingdom turn status — is Turn 1 complete or pending?
□ Game State Header output and confirmed
□ ONLY THEN: Begin Ch2 opening
```

---

## 🗺️ CHAPTER 2 OPENING CONTEXT

**Party composition:** Player character + up to 4 companions in Vanguard (per KM_PartySystem.md). Can swap at Capital.

**Where the story picks up:**
- First troll sighting reports arrive at the Capital within the first kingdom turn
- Jhod Kavken brings news: something is wrong with the Greenbelt flora — plants dying abnormally
- Kesten reports a missing patrol in the southern hexes
- The Season of Bloom has not yet begun but something is stirring

**What Tartuccio is doing:**
He fled south after Ch1. His journal mentioned a contact in Pitax. He will not appear directly until the player investigates the Troll Lair area deeper in Ch2. His influence is being felt through the Season of Bloom curse seeds he planted earlier.

**What Nyrissa knows:**
If `nyrissa_letter_found = TRUE` — she knows the player read her letter. The tone of Chapter 2's supernatural events will be more overtly directed. `nyrissa_awareness = active`
If `nyrissa_letter_found = FALSE` — she is watching but has not yet made direct contact. `nyrissa_awareness = passive`

---

*KM_Ch1_Export.md — Kingmaker PF2e Text Adventure | Ch1 Export v1.0*
