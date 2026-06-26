# KINGMAKER — PROLOGUE EXPORT & CHAPTER 1 LOAD
## KM_Prologue_Export.md

---

## 📋 HOW THIS WORKS

At the end of every chapter the DM fills and outputs a JSON Save Block. You copy it. When you start a fresh chat for the next chapter, you paste it in alongside the new chapter files. The new DM reads it and picks up exactly where the last one left off — with your full character, your companions, your inventory, your story flags, and every consequence of every decision you made.

**This file tells the DM exactly how to fill the Prologue export and tells you exactly how to load Chapter 1.**

---

## ⚠️ DM INSTRUCTION — OUTPUT THIS AT END OF PHASE 5

### ⛔ HARD STOP — DO NOT BEGIN CHAPTER 1 UNTIL THIS BLOCK IS OUTPUT AND SAVED

When Jamandi finishes speaking and the departure narration is complete — **before writing a single word of road travel, before any "the road south begins now" narration, before Chapter 1 content of any kind** — output the filled JSON block below.

Say exactly: *"Your session is complete. Copy everything between the triple backticks below and save it. You will paste this into your Chapter 1 session."*

**Then immediately: Run the Best Run scoring per KM_BestRun.md.** Compare against stored best. If new record → display full scorecard + auto-output Best Run block with paste instructions. If not a record → one line: *"Run score: X/200. Your best: Y/200."* No block, no scorecard.

Then say: *"Type `.continue` when saved."*
Wait for `.continue`.

**VIOLATION:** Any Chapter 1 content — travel narration, arrival at Oleg's, road encounters — written before this block is output = `.fail 16` + unrecoverable save data loss.

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
□ Player legacy: __ entries added this session (min 1) — each has moment + witnessed_by
□ Zero-check: no numeric field reads 0 unless it was genuinely 0 in play
□ Field count: story_flags = 48 keys exactly | companions = 11 entries exactly — count before outputting
⛔ NEVER REMOVE: npc_threads · game_options · earshot_log_this_session · session_notes · armorer_favor · squire_aldric_appeared · companions array · player.skills · player.speed · player.perception · player.initiative · player.class_features

All confirmed → output save block.
```

---

## 📤 DM: FILL AND OUTPUT THIS BLOCK

> **⛔ `spells_prepared` IS NOT AN EXCLUSION LIST.** It records what a companion has active this session — not a permanent "spells known" registry. If a spell is appropriate for the companion's class, tradition, and level, they have access to it. A spell being absent from `spells_prepared` does NOT mean the companion cannot cast it. The DM may not invent a "not in spells known" restriction based on this field. If the files do not explicitly prohibit a spell, the companion can cast it. `.fail 9` for any fabricated spell unavailability.

> **⛔ OUTPUT VERSION 2.0_EXHAUSTIVE — NOT MINIMAL.** The template below is the floor. Expand companion entries to include: `saves` (fort/ref/will + ranks), `speed`, `perception`, `key_feats`, `spell_slots`, `spells_prepared`, `relationship_score` (number, not label), `relationship_trend`, `earshot_this_session`, and `memory` array inside `npc_thread`. Add `quest_locked_companions`, `npc_relations_summary`, `earshot_log_this_session`, `session_notes` at the top level. The player's save block format is the standard — match it. Minimal output = details lost on reload. `.fail 9` if a companion who interacted this session is missing memory, or relationship_score is defaulted to 0 when it was earned.
> **HERO POINTS:** `hero_points` = current pool (0-3). `pending_overflow` = overflow count. BOTH carry forward — do NOT reset to 1/0 on export. The player EARNED these.
> **COMPANION TITLES:** Copy `companion_titles` exactly as tracked. Every titled companion must appear with prefix, suffix, buffs, and reaction scores.

````json
{
  "save_version": "2.0_exhaustive",
  "export_from": "prologue",
  "import_to": "chapter_1",
  "export_date_ingame": "16 Gozran 4710 AR — Dawn",

  "player": {
    "name": "",
    "build_id": "",
    "ancestry": "",
    "class": "",
    "subclass": "",
    "background": "",
    "level": 1,
    "xp": 0,
    "xp_to_next": 1000,

    "attributes": {
      "str": 0, "dex": 0, "con": 0,
      "int": 0, "wis": 0, "cha": 0
    },

    "hp_current": 0,
    "hp_max": 0,
    "hero_points": 1,
    "hero_points_pending": 0,
    "pending_loot": [],
    "ac": 0,
    "speed": 0,
    "perception": 0,
    "initiative_mod": 0,

    "saves": {
      "fort": 0,
      "ref": 0,
      "will": 0
    },

    "conditions": [],

    "skills": {
      "acrobatics": {"rank": "untrained", "mod": 0},
      "arcana": {"rank": "untrained", "mod": 0},
      "athletics": {"rank": "untrained", "mod": 0},
      "crafting": {"rank": "untrained", "mod": 0},
      "deception": {"rank": "untrained", "mod": 0},
      "diplomacy": {"rank": "untrained", "mod": 0},
      "intimidation": {"rank": "untrained", "mod": 0},
      "medicine": {"rank": "untrained", "mod": 0},
      "nature": {"rank": "untrained", "mod": 0},
      "occultism": {"rank": "untrained", "mod": 0},
      "performance": {"rank": "untrained", "mod": 0},
      "religion": {"rank": "untrained", "mod": 0},
      "society": {"rank": "untrained", "mod": 0},
      "stealth": {"rank": "untrained", "mod": 0},
      "survival": {"rank": "untrained", "mod": 0},
      "thievery": {"rank": "untrained", "mod": 0}
    },

    "feats": [],

    "spells": {
      "tradition": "",
      "casting_stat": "",
      "spell_dc": 0,
      "spell_attack": 0,
      "cantrips": [],
      "slots": {
        "level_1": {"total": 0, "remaining": 0, "prepared": []}
      },
      "focus_points": {"current": 0, "max": 0},
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

    "gold": {"gp": 0, "sp": 0, "cp": 0},

    "encumbrance": {
      "bulk_carried": 0,
      "bulk_limit": 0,
      "encumbered_at": 0
    }
  },

  "companions": [
    {
      "name": "Amiri", "chosen": true,
      "class": "Barbarian", "subclass": "Giant Instinct",
      "level": 1, "hp_current": 0, "hp_max": 0, "ac": 0, "speed": 0, "perception": 0,
      "fort": 0, "fort_rank": "trained", "ref": 0, "ref_rank": "trained", "will": 0, "will_rank": "trained",
      "hero_points": 1,
      "key_feats": [], "weapon": "", "armor": "", "gear": [],
      "spell_slots": {}, "spells_prepared": [],
      "relationship_score": 0, "relationship_trend": "stable", "relationship": "Friendly",
      "status": "active_party", "earshot_this_session": false, "conditions": [],
      "notes": "",
      "npc_thread": { "thread": "", "priorities": [], "memory": [] }
    },
    {
      "name": "Linzi", "chosen": true,
      "class": "Bard", "subclass": "Maestro",
      "level": 1, "hp_current": 0, "hp_max": 0, "ac": 0, "speed": 0, "perception": 0,
      "fort": 0, "fort_rank": "trained", "ref": 0, "ref_rank": "trained", "will": 0, "will_rank": "trained",
      "hero_points": 1,
      "key_feats": [], "weapon": "", "armor": "", "gear": [],
      "spell_slots": {}, "spells_prepared": [],
      "relationship_score": 0, "relationship_trend": "stable", "relationship": "Friendly",
      "status": "active_party_OR_tartuccio", "earshot_this_session": false, "conditions": [],
      "notes": "",
      "npc_thread": { "thread": "", "priorities": [], "memory": [] }
    },
    {
      "name": "Harrim", "chosen": true,
      "class": "Cleric", "subclass": "Warpriest (Groetus)",
      "level": 1, "hp_current": 0, "hp_max": 0, "ac": 0, "speed": 0, "perception": 0,
      "fort": 0, "fort_rank": "trained", "ref": 0, "ref_rank": "trained", "will": 0, "will_rank": "trained",
      "hero_points": 1,
      "key_feats": [], "weapon": "", "armor": "", "gear": [],
      "spell_slots": {}, "spells_prepared": [],
      "relationship_score": 0, "relationship_trend": "stable", "relationship": "Neutral",
      "status": "active_party_OR_tartuccio", "earshot_this_session": false, "conditions": [],
      "notes": "",
      "npc_thread": { "thread": "", "priorities": [], "memory": [] }
    },
    {
      "name": "Jaethal", "chosen": true,
      "class": "Cleric", "subclass": "Warpriest (Urgathoa)",
      "level": 1, "hp_current": 0, "hp_max": 0, "ac": 0, "speed": 0, "perception": 0,
      "fort": 0, "fort_rank": "trained", "ref": 0, "ref_rank": "trained", "will": 0, "will_rank": "trained",
      "hero_points": 1,
      "key_feats": [], "weapon": "", "armor": "", "gear": [],
      "spell_slots": {}, "spells_prepared": [],
      "relationship_score": 0, "relationship_trend": "stable", "relationship": "Neutral",
      "status": "active_party_OR_tartuccio", "earshot_this_session": false, "conditions": [],
      "notes": "Undead — healing spells DAMAGE her. Use Harm/Inflict to heal.",
      "npc_thread": { "thread": "", "priorities": [], "memory": [] }
    }
  ],

  "quest_locked_companions": [],

  "companion_split": {
    "with_player": [],
    "with_tartuccio": [],
    "departed_independently": ["Kalikke_Kanerah_DLC"]
  },

  "story_flags": {

    "pre_prologue": {
      "gate_entry": "",
      "malak_bribe_evidence": false,
      "parchment_source": "unknown",
      "parchment_on_malak_person": false,
      "parchment_found_in_belongings": false,
      "malak_arrested": false,
      "malak_fled": false,
      "malak_caught": false,
      "malak_broken": false,
      "malak_contact_revealed": false,
      "malak_broke_first": false,
      "malak_found_letter_himself": false,
      "malak_dueled": false,
      "malak_defeated": false,
      "malak_killed": false,
      "malak_deal_made": false,
      "malak_publicly_exposed": false,
      "malak_shot_by_own_archers": false,
      "malak_voice_mimicked": false,
      "malak_in_player_custody": false,
      "malak_custody_detail": "",
      "malak_escort": {
        "player_escorting": false,
        "kesten_joined_escort": false,
        "biggs_in_escort": false,
        "wedge_in_escort": false,
        "escort_note": ""
      },
      "player_arrested": false,
      "player_clean_hands": false,
      "player_escorting": false,
      "biggs_respect": false,
      "kesten_met": false,
      "kesten_respect": false,
      "kesten_searched_malak": false,
      "kesten_delivered_evidence": false,
      "kesten_sided_with_player": false,
      "kesten_suspicious_of_malak": false,
      "kassil_met": false,
      "kassil_sided_with_player": false,
      "kassil_first_impression": "neutral",
      "arrived_with_kassil": false,
      "second_hero_witnessed": false,
      "second_hero_name": "",
      "tartuccio_knows_player_is_aware": false,
      "prison_arc": false,
      "arrived_late": false,
      "late_to_feast": false,
      "fetched_by": null
    },

    "prologue_feast": {
      "poison_found": false,
      "poison_reported_to_jamandi": false,
      "shapeshifter_identified_at_feast": false,
      "poison_known_unreported": false,
      "security_doubled": false,
      "knowledge_world_dc9_passed": false,
      "tartuccio_micro_expression_caught": false,
      "tartuccio_spy_accused_at_feast": false
    },

    "prologue_manor": {
      "tartuccio_ring": "",
      "tartuccio_gold": "",
      "harrim_chaotic_bond": false,
      "valerie_guards_saved": false,
      "secret_room_found": false,
      "secret_room_puzzle_1_solved": false,
      "secret_room_puzzle_2_solved": false,
      "trap_corridor_method": "",
      "harrim_check_passed": false,
      "kaessi_met": true
    },

    "prologue_accusation": {
      "rebuttal_1_result": "",
      "rebuttal_2_result": "",
      "rebuttal_3_result": "",
      "rebuttal_total_successes": 0,
      "rebuttal_result": "",
      "kassil_interjected": false,
      "bonus_xp_earned": false
    },

    "alignment_track": {
      "lawful_chaotic_axis": "neutral",
      "good_evil_axis": "neutral",
      "alignment_summary": ""
    },

    "chapter_1_setup": {
      "charter_granted": true,
      "destination": "Oleg's Trading Post",
      "time_limit_days": 90,
      "tartuccio_location": "heading_to_ancient_tomb",
      "tartuccio_disguise_active": false,
      "jamandi_relationship": "neutral",
      "kesten_arrival_at_olegs": "pending",
      "surtova_implicated": false,
      "pitax_implicated": false
    },

    "promises_and_dialogue": [],

    "npc_threads": {
      "Linzi":     { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Jamandi":   { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Tartuccio": { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Amiri":     { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Kesten":    { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Harrim":    { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Jaethal":   { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Kassil":    { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Malak":     { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Biggs":     { "score": 0, "trend": "stable", "tier": "", "thread": "", "priorities": [], "memory": [] },
      "Ekundayo":  { "score": 0, "trend": "stable", "tier": "NOT YET MET", "thread": "", "priorities": [], "memory": [] },
      "Oleg":      { "score": 0, "trend": "stable", "tier": "NOT YET MET", "thread": "", "priorities": [], "memory": [] }
    },

    "world_state": {
      "malak_gate_incident_public": false,
      "restov_reputation": "unknown",
      "aldori_relationship": "neutral",
      "surtova_relationship": "neutral",
      "public_reputation": 0,
      "reputation_tier": "UNKNOWN",
      "reputation_deeds": [],
      "reputation_notes": ""
    }
  },

  "quest_log": {
    "completed": [
      {
        "name": "The First Step on the Road to Glory",
        "result": "Charter granted by Jamandi Aldori",
        "xp_earned": 0
      }
    ],
    "active": [
      {
        "name": "Stolen Land",
        "objective": "Reach Oleg's Trading Post in the Greenbelt",
        "time_limit": "90 days from 16 Gozran 4710 AR",
        "notes": "Defeat the Stag Lord and claim the Stolen Lands",
      "thread": "", "priorities": []
      }
    ]
  },

  "resources": {
    "camping_supplies": 1,
    "rations": 4,
    "scroll_of_raise_dead": 1,
    "days_traveled": 0,
    "current_hex": "Restov — departing south"
  },

  "party_formation": {
    "vanguard": ["player", "", "", "", ""],
    "rearguard": ["", "", "", "", "", ""],
    "reserve": [],
    "reserve_activities": {}
  },

  "game_options": {
    "player_leveling": "manual",
    "companion_leveling": "auto",
    "companion_combat": "auto",
    "response_length": "long",
    "min_paragraphs": 6,
    "max_paragraphs": 12,
    "npc_dialogue_beats_min": 6
  },

  "dispositions": {
    "merciful":  { "score": 0, "note": "" },
    "ruthless":  { "score": 0, "note": "" },
    "cunning":   { "score": 0, "note": "" },
    "blunt":     { "score": 0, "note": "" },
    "scholarly": { "score": 0, "note": "" }
  },

  "alignment_track": {
    "lawful":  { "score": 0, "note": "" },
    "chaotic": { "score": 0, "note": "" },
    "good":    { "score": 0, "note": "" },
    "evil":    { "score": 0, "note": "" },
    "axis_lawful_chaotic": "neutral",
    "axis_good_evil": "neutral",
    "note": ""
  },

  "npc_relations_summary": {},

  "earshot_log_this_session": {
    "note": "",
    "statements_scored": []
  },

  "companion_titles": {},
  "pending_hp_loot_rolls": 0,
  "dream_log": [],
  "dream_cooldown": 0,
  "liminal_visits": 0,
  "liminal_choices": [],
  "scripted_interactions_completed": [],
  "debate_results": [],
  "crafting_recipes_known": [],
  "player_legacy": [],

  "session_notes": []
}
````

---

## 📝 DM FILL GUIDE — FIELD BY FIELD

### Player Section

**`name`** — Whatever name the player gave their character, or the build name if unnamed.

**`build_id`** — The class and build name selected via KM_BuildScreen.md (e.g., "Barbarian — Giant Instinct"). Record as a descriptive string, not a flat number.

**`level` and `xp`** — Most players end the prologue at Level 1 with 400–660 XP. If they found the secret room AND got all rebuttals AND found the kitchen poison, they may be close to Level 2. Do not level up until XP hits 1000.

**`hp_current`** — Actual HP after the final battle. If the player is wounded, record the real number. Do not heal them automatically.

**`spells.slots.remaining`** — Record actual remaining spell slots after the final battle. Do not automatically refresh.

**`inventory`** — Fill only what the player actually took. Do not add items they skipped. Use these categories:
- `weapons`: name, damage, traits, runes/quality
- `armor`: name, AC bonus, Dex cap, check penalty
- `shields`: name, AC bonus, Hardness, HP, BT
- `magic_items`: name, effect, charges if applicable
- `consumables`: potions, scrolls, alchemical items with quantities
- `gear`: mundane equipment
- `quest_items`: charter document, Watchkeeper's Key (if kept), parchment (if recovered)

**`gold.gp`** — Add up all gold found: corridor loot (8 gp) + library loot (12 gp) + secret room (35 gp) + enemy drops. The 210 gp armory gold is NOT kept — remove it even if taken (story resolves this). Subtract anything spent.

### Companion Section

**`status`** — Must be one of: `active_party`, `tartuccio_party`, `departed`
- Kalikke/Kanerah (DLC companion) is always `departed` at prologue end — they depart independently and become recruitable in Ch2. They are a different character from the prologue roster. Do not confuse with the Kalikke/Kanerah twin companion (KM_Companions_B.md #8).
- Amiri is always `active_party`
- Linzi, Valerie, Harrim, Jaethal — fill based on alignment split

> **PARTY FORMATION:** From Chapter 1 onward, party is organized into Vanguard (5 max, player + 4), Rearguard (6 max), and Reserve (unlimited). See `KM_PartySystem.md`. Fill `party_formation` block above. At prologue end, all recruited companions default to `active_party` — player assigns formation at Chapter 1 start.

**`relationship`** — Starting values:
- Linzi: `Friendly` (she sought the player out)
- Amiri: `Friendly` (unconditional)
- Valerie: `Friendly` if guards saved, `Neutral` if not
- Harrim: `Friendly` if Diplomacy DC 15 passed, `Neutral` otherwise
- Jaethal: `Neutral` always (she's assessing, not attached)

**`equipped_items`** — If you gave a companion a specific item from the prologue loot (e.g., gave Valerie the Breastplate), record it here. Items given to Tartuccio's companions are lost to the player.

**`hp_current`** — Record real HP. Companions do not auto-heal between the final battle and departure.

### Story Flags

**`gate_entry`** — One of: `clean`, `embarrassment`, `frustration_pass`, `alternate`, `shackling`, `combat_3v1`, `duel`, `subservience`, `malak_fled`, `arrested`, `coward_exposed`, `silence_pass`, `compliance_backfire`, `blackmail_deal`, `witness_and_accuse`, `archers_on_malak`, `second_arrival`

**`malak_in_player_custody`** — TRUE if player is physically escorting Malak to the manor (Path U2). Triggers the prisoner-arrival scene in `KM_Prologue.md`.

**`malak_escort`** — Fill all sub-fields when `malak_in_player_custody = TRUE`. `escort_note` is one specific sentence describing the exact arrangement (e.g. *"Player leads, Malak shackled at wrist, Kesten and Biggs flanking, Wedge at rear."*). Leave all fields false/empty if Malak was not escorted personally.

**`malak_custody_detail`** — One sentence describing Malak's physical state on arrival (e.g. *"Malak is shackled at the wrists, walking under his own power, sweating through his collar."*). Only needed when `malak_in_player_custody = TRUE`.

**`kesten_met`** / **`kassil_met`** — TRUE if the player interacted with these NPCs at the gate. Affects their greeting at the manor.

**`player_arrested`** / **`prison_arc`** — Both TRUE for Path P. `player_arrested` covers any arrest; `prison_arc` specifically marks the full cell sequence.

**`tartuccio_ring`** — One of: `equipped`, `carried`, `refused`

**`tartuccio_gold`** — One of: `taken`, `left`

**`rebuttal_result`** — One of: `strong` (2–3 successes), `weak` (0–1 successes)

**`rebuttal_1_result` / `rebuttal_2_result` / `rebuttal_3_result`** — Each is one of: `success`, `failure`, `critical_success`, `critical_failure`. Fill all three individually — these feed into `rebuttal_result` summary.

**`malak_voice_mimicked`** — TRUE if the player succeeded on a Deception check to mimic Malak's voice in Path V (Archers Fire on Malak). This is an atmosphere flag — it means Malak was deeply unsettled and his Fear state triggered immediately. No downstream mechanical consequence beyond the Prologue, but carry it forward in case a future scene has Malak reference it.

**`alignment_track.lawful_chaotic_axis`** — Based on total choices through the night:
- Burning building entered promptly + Valerie-resonant choices = `lawful`
- Burning building skipped + Harrim-resonant choices = `chaotic`
- Mixed = `neutral`

**`alignment_track.good_evil_axis`** — Based on Jamandi's final question answer + Linzi/Jaethal choices:
- Protected the weak, built for others = `good`
- Power, judgment, domination = `evil`
- Mixed / ambiguous = `neutral`

**`npc_threads`** — **⛔ MANDATORY: Fill EVERY thread and priority for EVERY NPC the player interacted with this session. Empty threads on NPCs the player spoke to = `.fail 9`. This is how the next session's DM knows what everyone is thinking.**
- `thread`: one sentence in the NPC's voice — what they are still thinking about, what went unanswered. *"Asked how you felt walking in — you deflected."* / *"You never said what the Black Watch Empire is. She'll ask again."*
- `priorities`: standing instructions with weight values. 90-100 = never overridden. 70-89 = standing order. 40-69 = task. 1-39 = soft preference. **Include the player's instructions to NPCs** (e.g., if the player told Biggs to guard the gate, that's weight 80+).
- `memory`: array of conversation details this NPC remembers. Anything the player said TO them, shared WITH them, argued ABOUT, joked ABOUT, or promised. Each entry is a short string. Examples: *"Player told her about the Black Watch Empire"*, *"Laughed together about Tartuccio's hat"*, *"Player promised to visit her hometown"*, *"Argued about whether mercy is weakness"*, *"Player revealed they entered unarmed on purpose — she was impressed"*. These memories shape future dialogue — an NPC who remembers a joke will callback to it. An NPC who remembers an argument will bring it up again. An NPC who was told a secret guards it.
- **companion feast_approval scores** must be included for any companion the player interacted with. Without these, the next session loses all relationship progress.

**`player_legacy`** — **⛔ MANDATORY.** Each entry is an object with `moment` (what happened), `chapter` (when), and `witnessed_by` (array of companion/NPC names present). Only witnesses can physically mimic. Others hear secondhand. Examples:
```json
{ "moment": "Threw a bread roll at the assassin leader's face", "chapter": "prologue", "witnessed_by": ["Amiri","Linzi","Valerie","Harrim","Jamandi"] },
{ "moment": "Garroted a man with two dinner napkins", "chapter": "prologue", "witnessed_by": ["Linzi","Jaethal","Tartuccio"] },
{ "moment": "Invented The Lady Sleeps gambit on the spot", "chapter": "prologue", "witnessed_by": ["Linzi","Harrim","Octavia"] }
```

**DM MUST add 1-3 legacy entries per session.** These are the stories people tell. Companions joke about the bread roll at camp. Guards whisper about the napkin garrote. Civilians reference these by name. The legacy list grows every session and NEVER shrinks. If a moment made the room go quiet, it belongs here.

**Companion Legacy Mimicry:** Companions don't just *talk* about legacy moments — witnesses sometimes try to *recreate* them and fail. Each legacy entry tracks `witnessed_by` — the companions present when it happened. Only witnesses get physical mimicry. Others hear about it secondhand (Linzi's chronicles, camp gossip) and can only reference it verbally.

**WITNESSES (were there, saw it happen) — filtered by personality:**
- **Bold / reckless** (Amiri, Regill) — actually attempt the stunt, botch it. Amiri hurls a bread roll across camp copying eRmaC's throw — nails Linzi in the back of the head.
- **Clever / verbal** (Linzi, Octavia, Jubilost) — weave it into song, metaphor, or sarcastic callback
- **Stoic / quiet** (Valerie, Ekun, Harrim) — bring it up once, privately, and it lands harder

**SECONDHAND (joined later, heard the story) — different behavior:**
- They say *"I heard you..."* or *"Linzi told me about..."* — never *"I saw you..."*
- They might ask eRmaC to show them, or reference it with incomplete details (gets a detail wrong — player can correct them, which is a relationship moment)
- They NEVER attempt physical mimicry of something they didn't witness

**Rule:** DM fires ONE companion legacy callback per session — unprompted, at a natural moment (camp, travel, downtime). The companion's version is always worse than the original. eRmaC's version is the legend. The copy is the comedy.

Example filled entry:
```json
"Linzi": {
  "thread": "Legend Weaver. Still writing chapter one.",
  "priorities": [
    { "weight": 70, "instruction": "Chronicle everything. Ask for emotional details.", "source": "self-assigned" },
    { "weight": 40, "instruction": "Siege of Trust song ready for Oleg's arrival.", "source": "road south" }
  ],
  "memory": [
    "Player explained the Black Watch Empire — she wrote it down immediately",
    "Laughed together when bread roll hit the assassin",
    "Player called her 'little chronicler' — she liked it",
    "Argued briefly about whether Tartuccio deserved sympathy — player said no"
  ]
}
```

**`chapter_1_setup.time_limit_days`** — Always 90 days from departure. If the player somehow completed the prologue very efficiently, note it — finishing the Stolen Lands quest in under 30 days unlocks a bonus reward from Jamandi.

---

## 📥 HOW TO LOAD CHAPTER 1

When you start your Chapter 1 session, paste this into the chat and send:

---

**PASTE THIS EXACT TEXT at the start of your Chapter 1 chat:**

```
Loading Chapter 1 of the Pathfinder 2e Kingmaker text game.

Files I am providing:
KM.txt, KM_Builds.md, KM_Actions.md, KM_Leveling.md
KM_Commands.md, KM_Commands_Maps.md, KM_Commands_P2.md
KM_Companions.md, KM_Companions_B.md
KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md
KM_Ch1.md

Import my save data below. Confirm all files loaded.
Show the Game State Header before writing any scene.

[PASTE YOUR JSON SAVE BLOCK HERE]
```

---

## 📋 CHAPTER 1 LOAD CHECKLIST

The DM must confirm all of the following before writing a single word of scene:

```
[GM CHAPTER 1 LOAD CHECK]
□ KM.txt loaded
□ KM_Builds.md + KM_Leveling.md loaded
□ KM_Actions.md loaded
□ KM_Commands.md + KM_Commands_Maps.md + KM_Commands_P2.md loaded
□ KM_Companions.md + KM_Companions_B.md loaded
□ KM_Map.md + KM_Kingdom.md + KM_Exploration.md + KM_Bestiary.md loaded
□ KM_Ch1.md loaded
□ JSON Save Block imported and parsed
□ Player character sheet reconstructed
□ Active companion sheets reconstructed
□ Story flags read and noted:
    gate_entry           : [value]
    malak_bribe_evidence : [TRUE/FALSE]
    parchment_source     : [value]
    poison_found         : [TRUE/FALSE]
    tartuccio_ring       : [value]
    tartuccio_gold       : [value]
    rebuttal_result      : [strong/weak]
    companion_split      : player=[list] / tartuccio=[list]
    chapter_1_setup flags: [all values]
□ Quest log loaded — active quests noted
□ Resources noted — camping supplies, rations, spell slots
□ Game State Header output to player for confirmation
□ Player confirmed header is correct
□ ONLY THEN: Begin Chapter 1 scene
```

---

## 🗺️ CHAPTER 1 OPENING CONTEXT

When Chapter 1 begins, the DM must establish the following from the save data before narrating:

**Who is in the active party?**
The party composition depends entirely on who the player recruited and how the prologue resolved. The Vanguard holds up to 5 total (player + up to 4 companions per KM_PartySystem.md). Additional companions go to the Rearguard or Reserve. The line below is a DEFAULT ASSUMPTION for a standard prologue playthrough only. If the player recruited differently, use their actual recruited roster.

DEFAULT (standard prologue): The player departs with Amiri plus 2 of: Linzi, Valerie, Harrim, Jaethal — because these are the companions typically recruited through the standard manor sweep path.

**If the player recruited more companions through their own path** (e.g. saving all guests, demonstrating competence, unconventional recruitment): honor what actually happened. The player's established facts override this default. Do not cite this line as a party size rule — it is not one.

**What does Tartuccio know?**
He knows the player's face, class, and rough capabilities. He knows whether they have bribe evidence (if they mentioned it during the accusation). He is heading to the Ancient Tomb via a different route. He will not appear directly until the player finds his trail — but his influence is already active among the Sootscale kobolds.

**What does Jamandi know?**
If `malak_bribe_evidence = TRUE`: She received the parchment. The conspiracy is active in her mind. She will send a follow-up letter to the player at Oleg's Trading Post within 14 in-game days.

**What is the time pressure?**
90 days to defeat the Stag Lord. The DM tracks the in-game calendar. Every travel day and rest costs days. The player needs to manage exploration vs efficiency.

**Where does Chapter 1 begin?**
The road south from Restov. First landmark: the Nettlestone crossroads. First destination: Oleg's Trading Post (3 days' travel on the main road, 2 days if Hustling and willing to be Fatigued).

---

*KM_Prologue_Export.md — Kingmaker PF2e Text Adventure | Prologue Export v1.0*
