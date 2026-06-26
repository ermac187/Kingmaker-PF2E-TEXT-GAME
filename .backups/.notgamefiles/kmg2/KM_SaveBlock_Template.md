⛔ DM SAVE BLOCK DIRECTIVE — EXHAUSTIVE MODE (NON-NEGOTIABLE)
KM_SaveBlock_Template.md — Output verbatim. No exceptions.
============================================================

PLAYER STANDING ORDER: "Make the most comprehensive, exhaustive, complete
save block possible. I do not care how long it gets." Honor this every time.
A minimal save = broken seed = unplayable resume. There is NO upper length
limit. Erring large is correct; erring small is .fail 9.

⛔ ANTI-FABRICATION GATE (read before STEP 1):
   The save block has a fixed shape. Top-level keys = 49 in this exact order:
     save_version, chapter_completed, save_timestamp, save_label, dm_resume_note, player,
     companions, companions_selected, five_seekers, npc_threads, romance,
     companion_quests, active_quests, completed_quests, npc_relations, kingdom,
     crafting, story_flags, pre_prologue_state, scene_log, dice_log,
     dialogue_log_by_npc, decision_log, perception_log, loot_log, hp_ledger,
     xp_ledger, fail_log, dispositions, companion_titles, pending_hp_loot_rolls,
     pending_overflow, dream_log, dream_cooldown, player_legacy, current_chapter,
     current_scene, current_location, discovered_locations, party_formation,
     expedition_funds, overflow, injuries, passive_jealousy, companion_rivalry,
     date_log, dates_this_chapter, companion_fights, game_options.
   `save_version` is "1.7" (string). Field is named `save_version`, NOT `schema_version`,
   NOT `version`. If your output uses any other root structure, key list, or version
   string, you generated from training data or inference — that is `.fail 9`.

When any file instructs you to output the Save Block, follow these steps:

STEP 1 — Open this file IN THIS TURN. (Memory of prior reads does not count.)
STEP 2 — Copy the JSON block below EXACTLY — every key, every brace.
STEP 3 — Fill every placeholder with actual session data.
STEP 4 — Append session-specific log entries to scene_log, dice_log,
         dialogue_log_by_npc, decision_log, perception_log. Every roll,
         every NPC line spoken, every player choice, every DC offered.
STEP 5 — Self-audit: count top-level keys. Must be ≥ 30. If fewer, you
         dropped fields — STOP and rebuild from this template.
STEP 6 — Output the COMPLETE JSON. Every field. Every brace. Every key.

⛔ HARD RULES (every violation = .fail 9 per missing field):
  - EVERY field in this template MUST appear in your output.
  - Empty value is OK ("", 0, [], {}, false). MISSING KEY is not.
  - Do NOT collapse "" / 0 / [] fields by omitting them. Keep the key.
  - Do NOT invent your own JSON structure.
  - Do NOT remove, rename, or reorder fields.
  - Do NOT output a subset, summary, or "highlights" version.
  - Do NOT stop early. The closing `}` of the root object is mandatory.
  - Do NOT abbreviate log entries with "..." or "etc." Write them in full.
  - Do NOT decide a field is "uninteresting" and drop it. Every field matters.
  - If a log section has 47 entries this session, output all 47. No cap.

⛔ MINIMUM SIZE CHECK (post-output self-verify):
  - A complete save block at end of Pre-Prologue is ≥ 350 lines, ≥ 12,000 bytes.
  - End of Ch1: ≥ 500 lines, ≥ 18,000 bytes.
  - End of Ch2+: grows from there, never shrinks.
  - If your save is shorter than the minimum for the current chapter, you
    omitted fields or compressed logs. REBUILD before posting.

⛔ "BUT THE PLAYER'S RESUME WILL BE LONG" — IRRELEVANT.
  The player has explicitly authorized any length. Resumes work because the
  data is THERE. They break because the data ISN'T. Bias toward MORE detail.

============================================================
FILL GUIDE
============================================================

player
  build_id       — e.g. "Fighter_Build_2"
  build          — full build name from KM_Builds_*.md
  build_source   — source file, e.g. "KM_Builds_E2.md"
  attributes     — STR/DEX/CON/INT/WIS/CHA final values
  saves          — L1: class proficiency + stat mod (Fort/Ref/Will)
  speed          — base speed; subtract 5 if Heavy armor + no proficiency reduction
  skills_trained — class + background + heritage grants (no double-counting)
  languages      — Common + ancestry language + any bonus
  feats          — ancestry feat, background skill feat, L1 class feat
  inventory      — all starting gear
  known_spells   — leave empty [] for non-casters; fill for casters
  focus_points   — 0 for non-casters; fill for casters with Focus Pool

companions[]
  One entry per companion in companions_selected (11 entries = 10 + Linzi).
  build_id       — from KM_Companions_Builds.md
  hp_max         — from build file at level 1
  status         — "active" | "incapacitated" | "dead" | "absent"
  location       — "party" | "reserve" | "seekers" | "absent"

five_seekers     — seeker_1 through seeker_5 from player's Pick-5
npc_threads      — empty {} at session start; add per NPC as scenes occur
romance          — active_romance = name or "none"; per-companion stage/affection;
                   love scene fields (v66): love_scene_occurred | love_scene_partner |
                   love_scene_interrupted | love_scene_rival | love_scene_choice |
                   love_scene_aborted — add to each companion's romance entry
companion_quests — keyed by companion name; each entry has status + flags
active_quests    — list of quest names currently in progress
completed_quests — list of quest names fully resolved
npc_relations    — keyed by NPC name; value = integer relationship score
kingdom          — leave all zeroes/empty at pre-prologue; fill when kingdom founded

story_flags      — fill all triggered; leave untriggered at listed defaults
  tartuccio_team — always "five_seekers" once seekers assigned
  malak_escort sub-fields: player_escorting / kesten_joined / biggs / wedge = true/false
  escort_note    — one sentence on escort arrangement
  malak_custody_detail — one sentence on Malak's physical state at handoff

game_options.leveling_mode — PLAYER level-up mode (auto|ask|manual); default = "manual"
game_options.companion_leveling_mode — COMPANION level-up mode (auto|ask|manual); default = "auto"
party_formation.vanguard[0] — always "eRmaC"
hero_points      — carry forward exactly; do NOT reset
pending_overflow — carry forward exactly; do NOT reset

============================================================
JSON TEMPLATE — COPY VERBATIM, FILL ALL PLACEHOLDERS
============================================================

```json
{
  "save_version": "1.7",
  "chapter_completed": "pre_prologue",
  "save_timestamp": "",
  "save_label": "",

  "dm_resume_note": {
    "instruction": "",
    "player_position": "",
    "player_last_action": "",
    "player_intent": "",
    "room_state": {},
    "carousel_state": "",
    "open_threads": [],
    "level_up": "",
    "weapons": ""
  },

  "player": {
    "name": "eRmaC",
    "gender": "male",
    "build_id": "",
    "build": "",
    "build_source": "",
    "class": "",
    "ancestry": "",
    "heritage": "",
    "heritage_source": "",
    "heritage_granted_features": [],
    "background": "",
    "background_skill": "",
    "background_skill_feat": "",
    "weapon": "",
    "armor": "",
    "deity": "none",
    "level": 1,
    "xp": 0,
    "attributes": { "STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0 },
    "hp_current": 0,
    "hp_max": 0,
    "hero_points": 1,
    "ac": 0,
    "speed": 25,
    "saves": { "fort": 0, "ref": 0, "will": 0 },
    "perception": 0,
    "conditions": [],
    "skills_trained": [],
    "languages": [],
    "feats": {
      "ancestry": "",
      "background": "",
      "class_1": "",
      "general": [],
      "skill": []
    },
    "known_spells": [],
    "focus_points": 0,
    "inventory": [],
    "gold": { "gp": 0, "sp": 0, "cp": 0 },
    "notes": []
  },

  "companions": [
    {
      "name": "",
      "build_id": "",
      "class": "",
      "level": 1,
      "hp_current": 0,
      "hp_max": 0,
      "conditions": [],
      "gear": [],
      "status": "active",
      "location": "party"
    }
  ],

  "companions_selected": [],

  "five_seekers": {
    "seeker_1": "",
    "seeker_2": "",
    "seeker_3": "",
    "seeker_4": "",
    "seeker_5": ""
  },

  "npc_threads": {},

  "romance": {
    "active_romance": "none",
    "companions": {
      "CompanionName": {
        "stage": 0,
        "score": 0,
        "declaration_made": false,
        "declaration_result": "",
        "consort_unlocked": false,
        "date_count": 0,
        "gesture_returned": 0,
        "awkward_flag": false,
        "heart_scene_triggered": false,
        "date_awkward": false,
        "love_scene_occurred": false,
        "love_scene_partner": "",
        "love_scene_interrupted": false,
        "love_scene_rival": "",
        "love_scene_choice": "",
        "love_scene_aborted": false,
        "fade_active": false,
        "fade_chapters_remaining": 0,
        "cheating_detected": false,
        "cheating_confrontation_count": 0,
        "deny_used_this_arc": false
      }
    }
  },

  "companion_quests": {},

  "active_quests": [],

  "completed_quests": [],

  "npc_relations": {},

  "kingdom": {
    "name": "",
    "founded": false,
    "ruler_title": "",
    "advisors": {},
    "stats": { "economy": 0, "loyalty": 0, "stability": 0, "unrest": 0 },
    "buildings": [],
    "active_events": [],
    "completed_events": [],
    "treasury": { "gp": 0 },
    "army_units": [],
    "prestige_upgrades": []
  },

  "crafting": {
    "known_formulas": [],
    "in_progress": []
  },

  "story_flags": {
    "gate_entry": "",
    "gate_remanned_by": "",
    "malak_arrested": false,
    "malak_in_player_custody": false,
    "malak_fled": false,
    "malak_broken": false,
    "malak_contact_revealed": false,
    "malak_broke_first": false,
    "malak_found_letter_himself": false,
    "malak_deal_made": false,
    "malak_bribe_evidence": false,
    "parchment_source": "unknown",
    "parchment_recovered": false,
    "parchment_on_malak_person": false,
    "malak_escort": {
      "player_escorting": false,
      "kesten_joined_escort": false,
      "biggs_in_escort": false,
      "wedge_in_escort": false,
      "escort_note": ""
    },
    "malak_custody_detail": "",
    "kesten_met": false,
    "kesten_searched_malak": false,
    "kesten_delivered_evidence": false,
    "kesten_respect": false,
    "biggs_respect": false,
    "kassil_met": false,
    "kassil_first_impression": "neutral",
    "arrived_with_kassil": false,
    "prison_arc": false,
    "arrived_late": false,
    "player_clean_hands": false,
    "second_hero_witnessed": false,
    "second_hero_name": "",
    "tartuccio_knows_player_is_aware": false,
    "tartuccio_team": "five_seekers",
    "tartuccio_spy_discovered": false,
    "tartuccio_spy_discovery_method": "",
    "tartuccio_plot_armor_intact": true,
    "tartuccio_recruited_seekers": false,
    "malak_coin_purse_assessed": false,
    "jail_detour_taken": false,
    "five_seekers_freed_by_player": false,
    "five_seekers_freed_by_jamandi": false,
    "five_seekers_released_late": false,
    "kesten_dispatched_to_jail": false,
    "drevic_released_on": "",
    "public_reputation": 0,
    "reputation_tier": "UNKNOWN",
    "reputation_deeds": [],
    "reputation_notes": "",
    "marriage": {
      "married": false,
      "spouse": "",
      "spouse_origin": "",
      "wedding_chapter": null,
      "wedding_type": "",
      "wedding_vow_freeform": false,
      "anniversary_count": 0,
      "anniversary_last_session": 0,
      "heir_declared": false,
      "heir_source": "",
      "heir_name": "",
      "heir_age_narrative": 0,
      "separated": false,
      "separation_reason": "",
      "separation_chapter": null,
      "partner_left_voluntarily": false,
      "widowed": false,
      "widow_chapter": null,
      "marriage_history": [],
      "marriage_strain": 0,
      "strain_scene_fired": false,
      "strain_confrontation_active": false
    },
    "jealousy": {
      "love_triangle_active": false,
      "competing_companions": [],
      "tier_reached": 0,
      "open_arrangement": false,
      "open_partners": [],
      "secretly_aware": {},
      "resolution_attempts": [],
      "jealousy_resolved": false,
      "resolution_session": null
    },
    "weapons_in_garden": false,
    "promises": [],
    "dialogue_choices": [],
    "linzi_witnessed_gate": false,
    "tutorial_pickpocket_resolved": "",
    "tutorial_thief_gender": "",
    "tutorial_thief_class": "",
    "feast_approval": 0,
    "feast_companions_satisfied": [],
    "feast_companions_unsatisfied": [],
    "feast_companions_declared": [],
    "night_attack_outcome": "",
    "jamandi_survived": true,
    "oleg_met": false,
    "stag_lord_known": false,
    "irovetti_letter_found": false
  },

  "pre_prologue_state": {
    "active": true,
    "malak_anger": 0,
    "biggs_drift": 0,
    "wedge_drift": 0,
    "gate_window": "open",
    "tutorial_state": "pending",
    "tutorial_outcome": "",
    "linzi_beats_fired": [],
    "perception_tells_revealed": [],
    "companions_witnessed": [],
    "malak_priority_violations": [],
    "scene_phase": "arrival",
    "exit_trigger": "enters_jamandi_manor"
  },

  "scene_log": [
    {
      "scene_id": "",
      "scene_label": "",
      "entered_at_turn": 0,
      "exited_at_turn": 0,
      "key_events": [],
      "outcome": ""
    }
  ],

  "dice_log": [
    {
      "turn": 0,
      "scene_id": "",
      "actor": "",
      "check": "",
      "dc": 0,
      "modifier": 0,
      "raw_roll": 0,
      "total": 0,
      "result": "",
      "consequence": ""
    }
  ],

  "dialogue_log_by_npc": {
    "Malak": [],
    "Biggs": [],
    "Wedge": [],
    "Linzi": [],
    "Squire_Aldric": [],
    "Kesten": [],
    "Kassil": [],
    "Jamandi": [],
    "Tartuccio": []
  },

  "decision_log": [
    {
      "turn": 0,
      "scene_id": "",
      "prompt_summary": "",
      "options_offered": 0,
      "player_choice": "",
      "consequence": ""
    }
  ],

  "perception_log": [
    {
      "turn": 0,
      "target": "",
      "dc": 0,
      "rolled": 0,
      "tell_revealed": ""
    }
  ],

  "loot_log": [
    {
      "turn": 0,
      "source": "",
      "items": [],
      "gold_added": { "gp": 0, "sp": 0, "cp": 0 },
      "hp_award_loot": false
    }
  ],

  "hp_ledger": [
    {
      "turn": 0,
      "trigger": "",
      "awarded": 0,
      "pool_after": 0,
      "overflow_after": 0
    }
  ],

  "xp_ledger": [
    {
      "turn": 0,
      "source": "",
      "amount": 0,
      "running_total": 0
    }
  ],

  "fail_log": [
    {
      "turn": 0,
      "code": ".fail N",
      "description": "Specific description of what fired, what file rule was violated, and what was re-rendered. Example: '.fail 9 — Jamandi described with dark braided hair. KM_NPC_Profiles.md states iron-gray jaw-length never braided. Re-rendered with correct description.' Empty array OK if zero fails this session.",
      "corrected": true
    }
  ],

  "dispositions": {
    "merciful": 0,
    "ruthless": 0,
    "cunning": 0,
    "blunt": 0,
    "scholarly": 0
  },

  "companion_titles": {},

  "pending_hp_loot_rolls": 0,
  "pending_overflow": 0,
  "dream_log": [],
  "dream_cooldown": 0,
  "player_legacy": [],

  "current_chapter": "pre_prologue",
  "current_scene": "restov_gate",
  "current_location": "Restov — South Gate",
  "discovered_locations": [],

  "party_formation": {
    "vanguard": ["eRmaC", "", "", "", "", ""],
    "rearguard": ["", "", "", "", "", ""],
    "reserve": [],
    "reserve_activities": {},
    "combat_formation": "shield_wall",
    "custom_positions": {}
  },

  "expedition_funds": 0,
  "overflow": 0,
  "injuries": [],

  "passive_jealousy": {
    "WatcherName_watching_RivalName": {
      "heat": 0,
      "rival": "",
      "last_trigger": "",
      "behavior_tier": "none",
      "boiling_point": 10,
      "confrontation_fired": false
    }
  },

  "companion_rivalry": {
    "CompanionA_CompanionB": {
      "tier": 0,
      "cause": "",
      "last_event": "",
      "combat_cohesion": true,
      "mutual_respect": false,
      "resolution": null
    }
  },

  "date_log": [],

  "dates_this_chapter": 0,

  "companion_fights": {
    "CompanionName": {
      "fight_active": false,
      "fight_trigger": "",
      "fight_chapter": null,
      "posture_used": "",
      "paused_duration": 0,
      "paused_chapters_remaining": 0,
      "grand_gesture_available": true,
      "agenda_ignored_count": 0,
      "mend_attempts": []
    }
  },

  "game_options": {
    "leveling_mode": "manual",
    "companion_leveling_mode": "auto",
    "companion_combat": "auto",
    "response_length": "long",
    "min_paragraphs": 6,
    "max_paragraphs": 12,
    "npc_dialogue_beats_min": 6
  }
}
```

---
*KM_SaveBlock_Template.md — Kingmaker PF2e | Save Block v1.7*
*v1.7: Expanded per-companion romance schema in companions{} (stage, score, declaration,
consort, date_count, gesture_returned, fade, cheating, love scene fields). Expanded
passive_jealousy{}, companion_rivalry{}, companion_fights{} with full sub-field schemas.
Removed duplicate dispositions from story_flags (root-level is canonical). Version 1.6 → 1.7.*
*v1.6: Added love scene sub-fields to per-companion romance entries (v66 love scene
system): love_scene_occurred | love_scene_partner | love_scene_interrupted |
love_scene_rival | love_scene_choice | love_scene_aborted. Version string 1.5 → 1.6.*
*v1.5: Added companion_fights{} (v63 fight system — fight state, posture, paused
duration, grand gesture availability, agenda_ignored_count, mend_attempts per
companion). Version string bumped 1.4 → 1.5.*
*v1.4: Added passive_jealousy{} (v60 passive heat meter), companion_rivalry{}
(v60 rivalry tier + injury state), date_log[] (v62 date system log),
dates_this_chapter (v62 per-chapter date counter). Version string corrected
1.3 → 1.4.*
*v1.3: EXHAUSTIVE MODE enforcement. Added hard rules: every field MUST appear,
empty allowed but missing = .fail 9 per field. Minimum line/byte floors per
chapter (Pre-Prologue ≥350 lines/12KB, Ch1 ≥500/18KB). Self-audit step (count
top-level keys ≥30) before posting. Added new blocks: pre_prologue_state
(Drift/Anger/Gate Window/tutorial trackers — active in custom-rules zone from
Restov arrival through Jamandi's manor entry), scene_log (per-scene event
record), dice_log (every roll), dialogue_log_by_npc (every NPC line spoken),
decision_log (every player choice + consequence), perception_log, loot_log,
hp_ledger, xp_ledger, fail_log. Added save_timestamp + save_label at top.
save_version bumped 1.1 → 1.3.*
*v1.2: Exhaustive rewrite. Added: companion state objects (full per-companion entry),
romance system block, companion_quests, active_quests, completed_quests, npc_relations,
kingdom stub, crafting stub, expanded story_flags (feast/night-attack/chapter flags),
expanded feats object (ancestry/background/class_1/general/skill), perception, focus_points,
known_spells, background_skill fields. save_version bumped to 1.1.*
