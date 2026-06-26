# KINGMAKER — GLOSSARY
## KM_Glossary.md | Flag Definitions, System Terms, Save Block Reference

> **DM:** Load this file when:
> - A flag's meaning is unclear
> - Checking whether a flag has been set correctly
> - Resolving a contradiction between two flags
> - A player asks what a save block field means

---

## 📖 HOW TO USE THIS FILE

Flags are listed alphabetically within sections. Each entry shows:
- **Flag name** (exactly as it appears in the save block)
- **Type** — TRUE/FALSE, string, integer, or object
- **Set by** — which file/scene sets it
- **Read by** — which files check it
- **Values** — all valid values with meaning

---

## 🔤 PRE-PROLOGUE FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `gate_entry` | string | `clean` / `embarrassment` / `frustration_pass` / `alternate` / `shackling` / `combat_3v1` / `duel` / `subservience` / `malak_fled` / `arrested` / `coward_exposed` / `silence_pass` / `compliance_backfire` / `blackmail_deal` / `witness_and_accuse` / `archers_on_malak` / `second_arrival` / `dismissal` / `friendly_fire` | Which path the player took through the Restov gate scene |
| `malak_bribe_evidence` | bool | TRUE/FALSE | Player found and possesses evidence of Malak's bribe |
| `malak_arrested` | bool | TRUE/FALSE | Malak was arrested at the gate |
| `malak_broke_first` | bool | TRUE/FALSE | Malak initiated speech during Path Q (silence approach) — he cracked first |
| `malak_caught` | bool | TRUE/FALSE | Malak was physically caught or restrained during the gate scene |
| `malak_broken` | bool | TRUE/FALSE | Malak's will collapsed — he stopped resisting |
| `malak_contact_revealed` | bool | TRUE/FALSE | Malak's external contact (Pitax/Surtova) was publicly named |
| `malak_deal_made` | bool | TRUE/FALSE | Player struck a mutual silence deal with Malak (Path T blackmail) |
| `malak_defeated` | bool | TRUE/FALSE | Malak was defeated in combat (Path F or G) |
| `malak_dismissed` | bool | TRUE/FALSE | Player actively ignored Malak (Path U — The Dismissal) |
| `malak_dueled` | bool | TRUE/FALSE | Malak fought the player one-on-one (Path G) |
| `malak_found_letter_himself` | bool | TRUE/FALSE | Malak discovered his own bribe letter during the scene (Path R) |
| `malak_in_player_custody` | bool | TRUE/FALSE | Player is physically escorting Malak to the manor |
| `malak_killed` | bool | TRUE/FALSE | Malak was killed at the gate |
| `malak_publicly_exposed` | bool | TRUE/FALSE | Malak's corruption was exposed in front of the crowd |
| `malak_shot_by_own_archers` | bool | TRUE/FALSE | Wall archers fired on Malak (Path V — friendly fire variant) |
| `malak_voice_mimicked` | bool | TRUE/FALSE | Player mimicked Malak's voice (Path V Deception check) |
| `malak_custody_detail` | string | descriptive | One sentence describing Malak's physical state on arrival |
| `malak_escort` | object | sub-fields | Escort arrangement when malak_in_player_custody = TRUE |
| `parchment_source` | string | `pitax` / `unknown` | Origin of the bribe parchment. Always `pitax` if found. |
| `parchment_on_malak_person` | bool | TRUE/FALSE | Parchment was physically on Malak's body when found |
| `parchment_found_in_belongings` | bool | TRUE/FALSE | Parchment was found in Malak's belongings (searched separately) |
| `player_arrested` | bool | TRUE/FALSE | Player was arrested at the gate (Path P or combat escalation) |
| `player_clean_hands` | bool | TRUE/FALSE | Player accused without touching evidence — authority searched instead |
| `player_escorting` | bool | TRUE/FALSE | Player is physically walking Malak to the manor |
| `prison_arc` | bool | TRUE/FALSE | Player went through the full cell sequence after arrest |
| `biggs_respect` | bool | TRUE/FALSE | Biggs was impressed by the player's gate conduct |
| `kesten_met` | bool | TRUE/FALSE | Player interacted with Kesten Garess at the gate |
| `kesten_respect` | bool | TRUE/FALSE | Kesten Garess was impressed by the player's gate conduct |
| `kesten_searched_malak` | bool | TRUE/FALSE | Kesten performed the evidence search on Malak |
| `kesten_delivered_evidence` | bool | TRUE/FALSE | Kesten delivered recovered evidence to Jamandi |
| `kesten_sided_with_player` | bool | TRUE/FALSE | Kesten took the player's side during the gate confrontation |
| `kesten_suspicious_of_malak` | bool | TRUE/FALSE | Kesten independently suspects Malak of wrongdoing |
| `kassil_met` | bool | TRUE/FALSE | Player interacted with Kassil Aldori at the gate |
| `kassil_sided_with_player` | bool | TRUE/FALSE | Kassil took the player's side during the gate confrontation |
| `kassil_first_impression` | string | `positive` / `neutral` / `negative` | Kassil Aldori's first impression of the player |
| `second_hero_witnessed` | bool | TRUE/FALSE | A second hero arrived mid-scene (Path S) |
| `second_hero_name` | string | Player-named | Name of the second hero if Path S was taken |
| `arrived_late` | bool | TRUE/FALSE | Player arrived late to the manor due to gate delay |
| `late_to_feast` | bool | TRUE/FALSE | Player arrived late to the feast specifically |
| `fetched_by` | string / null | NPC name or null | Who came to fetch the player if they were late/arrested |
| `flatbread_vendor_spoken` | bool | TRUE/FALSE | Player interacted with the flatbread vendor at the gate (Path U Dismissal) |
| `alternate_entry_method` | string | `stealth` / `bribe` / `climb` / `smuggler` | Method used for Path D alternate entry |
| `malak_coin_purse_assessed` | bool | TRUE/FALSE | Kesten, Kassil, or Jamandi visually assessed the coin purse as more than a year's wages |
| `jail_detour_taken` | bool | TRUE/FALSE | Player went to the Restov City Jail before the feast |
| `five_seekers_freed_by_player` | bool | TRUE/FALSE | Player directly secured release of the five imprisoned seekers |
| `five_seekers_freed_by_jamandi` | bool | TRUE/FALSE | Jamandi dispatched Kesten to free the five during the feast |
| `five_seekers_released_late` | bool | TRUE/FALSE | Five seekers released next morning — neither rescue path taken |
| `kesten_dispatched_to_jail` | bool | TRUE/FALSE | Kesten was sent to the jail during the feast |
| `drevic_released_on` | string | descriptive | Authority basis Drevic used to release the prisoners |
| `tartuccio_team` | string | `five_seekers` / `mercenaries` / `unknown` | Who forms Tartuccio's team in Ch1. Five seekers if either rescue path taken; mercenaries if late release. |

---

## 🎭 PROLOGUE FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `rebuttal_result` | string | `strong` / `weak` | 2–3 successes = strong; 0–1 = weak. Affects Jamandi's final assessment. |
| `rebuttal_1_result` / `_2` / `_3` | string | `success` / `failure` / `critical_success` / `critical_failure` | Individual rebuttal check results |
| `tartuccio_ring` | string | `equipped` / `carried` / `refused` | What the player did with Tartuccio's signet ring |
| `tartuccio_gold` | string | `taken` / `left` | Whether player took the gold from Tartuccio's room |
| `tartuccio_knows_player_is_aware` | bool | TRUE/FALSE | Tartuccio knows the player suspects him. Set only on direct confrontation — NOT set from finding his journal. |
| `linzi_tartuccio` | bool | TRUE/FALSE | Linzi went with Tartuccio's party at the prologue split |
| `arrived_with_kassil` | bool | TRUE/FALSE | Kassil Aldori escorted the player to the manor (Path A variant) |
| `harrim_chaotic_bond` | bool | TRUE/FALSE | Player bonded with Harrim over a chaotic/nihilistic choice — affects starting relationship |
| `poison_found` | bool | TRUE/FALSE | Player found the poison at the feast |
| `poison_reported_to_jamandi` | bool | TRUE/FALSE | Player reported the poison to Jamandi |
| `poison_known_unreported` | bool | TRUE/FALSE | Player found poison but did not report it |
| `shapeshifter_identified_at_feast` | bool | TRUE/FALSE | Player identified the shapeshifter during the feast |
| `security_doubled` | bool | TRUE/FALSE | Security was doubled after player's report |
| `knowledge_world_dc9_passed` | bool | TRUE/FALSE | Player passed the DC 9 Knowledge (World) check at the feast |
| `tartuccio_micro_expression_caught` | bool | TRUE/FALSE | Player caught Tartuccio's micro-expression at the feast |
| `tartuccio_spy_accused_at_feast` | bool | TRUE/FALSE | Player accused Tartuccio of being a spy at the feast |
| `valerie_guards_saved` | bool | TRUE/FALSE | Player saved Valerie's guards during the manor attack |
| `secret_room_found` | bool | TRUE/FALSE | Player found the secret room in the manor |
| `secret_room_puzzle_1_solved` | bool | TRUE/FALSE | First puzzle in the secret room solved |
| `secret_room_puzzle_2_solved` | bool | TRUE/FALSE | Second puzzle in the secret room solved |
| `trap_corridor_method` | string | descriptive | How the player handled the trap corridor |
| `harrim_check_passed` | bool | TRUE/FALSE | Player passed the Harrim-related check in the manor |
| `kaessi_met` | bool | TRUE/FALSE | Player met Kaessi (DLC companion) during the prologue |
| `kassil_interjected` | bool | TRUE/FALSE | Kassil interjected during the accusation scene |
| `bonus_xp_earned` | bool | TRUE/FALSE | Player earned bonus XP during the prologue |

---

## 🗺️ CHAPTER 1 FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `stag_lord_fate` | string | `killed` / `beheaded_head_sent` / `captured_kesten` / `captured_imprisoned` / `executed_publicly` | How the Stag Lord was dealt with |
| `stag_lord_head_sent_to_jamandi` | bool | TRUE/FALSE | Head delivered to Jamandi — diplomatic gesture |
| `ch1_opening_path` | string | `tomb_first` / `thorn_first` | Which main location the player went to first |
| `nyrissa_letter_found` | bool | TRUE/FALSE | Player found Nyrissa's letter in the Stag Lord's fort |
| `nyrissa_early_contact` | bool | TRUE/FALSE | Set when nyrissa_letter_found = TRUE. Tracks that Nyrissa has been in contact with Stolen Lands actors. |
| `akiros_turned` | bool | TRUE/FALSE | Akiros Ismort defected from the Stag Lord |
| `akiros_fate` | string | `turned_ally` / `fought_defeated` / `killed` / `fled` | Final disposition of Akiros |
| `kressle_fate` | string | `killed` / `turned_good` / `intimidated_fled` / `escaped` | Final disposition of Kressle |
| `oleg_expanded` | bool | TRUE/FALSE | Set TRUE after the first kingdom turn resolves — triggers Oleg's expanded stock |
| `bokken_relationship` | string | `neutral` / `friendly` / `hostile` | Relationship with Bokken the alchemist (fangberry quest affects this) |
| `tiressia_met` | bool | TRUE/FALSE | Player visited Tiressia's glade in Ch1 |
| `nettles_crossing_resolved` | bool | TRUE/FALSE | Nettles' ghost at the river crossing was resolved (Stag Lord's head thrown in) |
| `sootscale_alliance` | bool | TRUE/FALSE | Player allied with the Sootscale kobolds |
| `jubilost_helped` | bool | TRUE/FALSE | Player helped Jubilost Narthropple — he provides Varnhold information in Ch3 |
| `old_beldame_met` | bool | TRUE/FALSE | Player met Old Beldame — affects her availability as an NPC resource |
| `tartuccio_as_tartuk_revealed` | bool | TRUE/FALSE | Player discovered Tartuccio was disguised as the kobold shaman Tartuk |
| `tartuccio_journal_found` | bool | TRUE/FALSE | Player found Tartuccio's personal journal at Old Sycamore |
| `tartuccio_journal_contents_known` | bool | TRUE/FALSE | Player read the journal (requires finding it first) |
| `tartuccio_confronted_ch1` | bool | TRUE/FALSE | Player confronted Tartuccio/Tartuk at Old Sycamore |
| `tartuccio_contact_named` | bool | TRUE/FALSE | Player identified Tartuccio's external contact by name |
| `ch1_speed_bonus` | bool | TRUE/FALSE | Chapter 1 completed in ≤30 days — Lord Protector sword awarded |
| `companions_rescued_from_cage` | bool | TRUE/FALSE | Prologue companions rescued from kobold cage at Old Sycamore |
| `dovan_fate` | string | descriptive | Disposition of Dovan from Nisroch (Stag Lord's fort) |
| `auchs_fate` | string | descriptive | Disposition of Auchs (Stag Lord's fort) |
| `nugrah_released` | bool | TRUE/FALSE | Nugrah the old druid was released from the Stag Lord's basement |
| `kressle_assisted` | bool | TRUE/FALSE | Kressle assisted the player during the Stag Lord assault |
| `svetlana_ring_recovered` | bool | TRUE/FALSE | Svetlana's wedding ring recovered from bandits |
| `svetlana_ring_returned` | bool | TRUE/FALSE | Ring returned to Svetlana at Oleg's |
| `falgrim_sneeg` | string | descriptive | Disposition of Falgrim Sneeg (bounty target) |
| `fangberries_delivered` | bool | TRUE/FALSE | Fangberries delivered to Bokken |
| `moon_radishes_delivered` | bool | TRUE/FALSE | Moon radishes delivered to Svetlana |
| `scythe_tree_defeated` | bool | TRUE/FALSE | Scythe tree in the Narlmarches defeated |
| `tuskgutter_killed` | bool | TRUE/FALSE | Tuskgutter the boar killed (bounty quest) |
| `nok_nok_available` | bool | TRUE/FALSE | Nok-Nok is available for recruitment |
| `lem_available` | bool | TRUE/FALSE | Lem is available for recruitment |
| `prologue_companions_recovered` | array | name list | Companions rescued from Tartuccio's party/kobold cage |
| `amiri_quest_stage` | integer | 1–3 | Current stage of Amiri's personal quest progression |
| `varnhold_competing` | bool | TRUE/FALSE | Varnhold is actively competing for the Stolen Lands |

---

## 🪨 CHAPTER 2 FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `hargulka_fate` | string | `killed` / `vassal` | Whether Hargulka was killed or made a vassal. Vassal = Ekundayo leaves. |
| `hargulka_vassal` | bool | TRUE/FALSE | Redundant with hargulka_fate but used as quick-check in companion logic |
| `kargadd_killed` | bool | TRUE/FALSE | Kargadd the rock troll (Ekundayo's target) was killed |
| `ekundayo_recruited` | bool | TRUE/FALSE | Ekundayo joined the party |
| `ekundayo_quest` | string | `inactive` / `active` / `complete` | Status of A Score to Settle |
| `ekundayo_committed_to_kingdom` | bool | TRUE/FALSE | Ekundayo declared he wants to help build the kingdom (post-quest scene) |
| `tristian_betrayal_revealed` | bool | TRUE/FALSE | Tristian's connection to the Bloom was revealed. Always set TRUE in Ch3. |
| `tristian_quest` | string | `forgiven` / `condemned` / `absent` | **AUTHORITATIVE FLAG.** Player's choice + outcome. `absent` = condemned and never re-recruited. Use this flag for all quest checks. |
| `tristian_decision` | string | `forgiven` / `condemned` | Alias for `tristian_quest`. Legacy name — use `tristian_quest` going forward. |
| `tristian_condemned` | bool | TRUE/FALSE | Quick-check alias. TRUE when `tristian_quest = condemned`. Set simultaneously with tristian_quest. |
| `tristian_redeemed` | bool | TRUE/FALSE | Set TRUE in Ch3 when Tristian rejoins after condemnation. Overrides `tristian_condemned`. When TRUE: treat as forgiven for all downstream checks. |
| `bloom_resolved` | bool | TRUE/FALSE | Season of Bloom main quest completed |
| `bald_hilltop_resolution` | string | `purified` / `abandoned` / `claimed` | How the Bald Hilltop was resolved |
| `tartuccio_ch2_confronted` | bool | TRUE/FALSE | Player confronted Tartuccio/Tartuk at Hargulka's throne room |
| `tartuccio_ch2_fate` | string | `fled_to_varnhold_region` / `vassal` / `defeated` | Tartuccio's Ch2 outcome |
| `jazon_escort` | bool | TRUE/FALSE | Player escorted the Jazon character to Trobold — unlocks peaceful dialogue option with Hargulka |

---

## 💀 CHAPTER 3 FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `vordakai_fate` | string | `destroyed` / `recruited` | Vordakai killed or recruited as evil path advisor |
| `oculus_destroyed` | bool | TRUE/FALSE | Vordakai's phylactery (the Oculus of Abaddon) was destroyed. Required for Pharasma's shrine path. |
| `vordakai_phylactery_destroyed` | bool | TRUE/FALSE | Alias for oculus_destroyed — both flags are set simultaneously |
| `vordakai_recruited` | bool | TRUE/FALSE | Vordakai joined as Magister advisor. Locks some endings. Blocks Pharasma shrine Option A. |
| `varnhold_regent_saved` | bool | TRUE/FALSE | Varnhold's regent was freed from the soul jar |
| `varnhold_vassal` | bool | TRUE/FALSE | Varnhold became a vassal settlement |
| `kellid_friendly` | bool | TRUE/FALSE | Player made positive contact with Kellid barbarians |
| `willas_gunderson_fate` | string | `saved` / `died` / `unknown` | Fate of Willas Gunderson (Varnhold survivor) |

---

## 🌿 NYRISSA / BLOOM FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `nyrissa_awareness` | string | `passive` / `active` | Passive = she's watching but not engaging. Active = she's intervening. Shifts to active mid-Ch2. |
| `nyrissa_revealed` | bool | TRUE/FALSE | Nyrissa appeared directly in the throne room (Ch6) |
| `nyrissa_backstory_known` | bool | TRUE/FALSE | **CRITICAL.** Player knows Nyrissa's full history (Lantern King cursed her). Required for true ending. Multiple paths to this. |
| `nyrissa_backstory_partial` | bool | TRUE/FALSE | Player knows something but not everything. Set after Storyteller fragment 4. |
| `nyrissa_can_be_saved_hint` | bool | TRUE/FALSE | Player received the hint that Nyrissa CAN be saved (Storyteller fragment 7). |
| `nyrissa_origin_hint` | bool | TRUE/FALSE | Cyclops coin reward reveals her origin (connection to ancient history). |
| `nyrissa_identity_hint` | bool | TRUE/FALSE | Player has partial identification of Nyrissa as a specific entity. |
| `nyrissa_bloom_connection_known` | bool | TRUE/FALSE | Player knows Nyrissa is connected to the Season of Bloom. |
| `nyrissa_identity_known` | bool | TRUE/FALSE | Player knows who Nyrissa actually is. |

---

## 🌹 LINZI FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `linzi_quest` | string | `inactive` / `active` / `complete` | Status of Easier to Ask Forgiveness quest |
| `linzi_dead` | bool | TRUE/FALSE | Linzi died in Thousandbreaths |
| `linzi_saved` | bool | TRUE/FALSE | Player successfully interposed before Nyrissa killed Linzi (all 4 conditions met) |
| `linzi_shrine_completed` | bool | TRUE/FALSE | Shrine of Returning quest completed (any god path) |
| `linzi_mark` | string | `none` / `shelyn_marked` / `pharasma_marked` / `urgathoa_marked` | Permanent mark from resurrection god |
| `linzi_accepted_urgathoa` | bool | TRUE/FALSE | Linzi accepted Urgathoa's terms after undead resurrection |
| `linzi_refused_urgathoa` | bool | TRUE/FALSE | Linzi refused Urgathoa's terms — returned to death |

---

## 📖 STORYTELLER FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `storyteller_available` | bool | TRUE/FALSE | Storyteller NPC is accessible in the capital (set at kingdom founding) |
| `storyteller_collection` | string | `incomplete` / `COMPLETE` | Whether all 10 relic fragments have been delivered. Note: case-sensitive — must be `COMPLETE` (uppercase) for Linzi save condition check. |
| `fragments_delivered` | integer | 0–10 | Number of relic fragments delivered to the Storyteller |
| `coins_delivered` | integer | 0–12 | Number of Ancient Cyclops Coins delivered |

---

## ⚖️ ALIGNMENT FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `lawful_chaotic_axis` | string / integer | `lawful` / `neutral` / `chaotic` OR −10 to +10 | Positive = Lawful. Negative = Chaotic. |
| `good_evil_axis` | string / integer | `good` / `neutral` / `evil` OR −10 to +10 | Positive = Good. Negative = Evil. |
| `alignment_track` | object | Both axes as above | Full alignment object in save block |

---

## 🏛️ KINGDOM FLAGS

| Flag | Type | Values | Meaning |
|------|------|--------|---------|
| `capital_location` | string | `olegs` / `sycamore` / `forest_edge` | Capital site chosen at founding |
| `political_allegiance` | string | `aldori` / `surtova` / `independent` | Coronation allegiance choice (Ch4) |
| `coronation_complete` | bool | TRUE/FALSE | Coronation ceremony has occurred |
| `kingdom_founded` | bool | TRUE/FALSE | Kingdom formally established (Ch1 end) |
| `true_ending_achieved` | bool | TRUE/FALSE | True ending completed — Lantern King yielded, Nyrissa freed |

---

## 🗡️ COMPANION QUEST STATUS VALUES

All companion quest flags use these standard values unless otherwise noted:

| Value | Meaning |
|-------|---------|
| `inactive` | Quest not yet triggered (companion not recruited or threshold not met) |
| `triggered` | Quest has triggered but not yet started in earnest |
| `active` | Quest is in progress |
| `complete` | Quest completed successfully |
| `failed` | Quest failed or window closed |
| `incomplete` | At chapter 7 — quest was not finished (triggers Ch7 risk) |

**Companion quest flags (1–12):** `amiri_quest` / `linzi_quest` / `valerie_quest` / `harrim_quest` / `tristian_quest` / `jaethal_quest` / `octavia_quest` / `regongar_quest` / `noknok_quest` / `lem_quest` / `ekundayo_quest` / `kalikke_kanerah_quest`

**Companion quest flags (13–31):** `jubilost_quest` / `seelah_quest` / `merisiel_quest` / `valeros_quest` / `ezren_quest` / `fumbus_quest` / `feiya_quest` / `quinn_quest` / `jirelle_quest` / `lini_quest` / `harsk_quest` / `yoon_quest` / `korakai_quest` / `nhalmika_quest` / `nahoa_quest` / `samo_quest` / `sajan_quest` / `crowe_quest` / `seoni_quest`

**Companion quest flags (32–53):** `imrijka_quest` / `alain_quest` / `damiel_quest` / `hayato_quest` / `oloch_quest` / `shardra_quest` / `adowyn_quest` / `erasmus_quest` / `estra_quest` / `reiko_quest` / `rivani_quest` / `meyanda_quest` / `mazlova_quest` / `kess_quest` / `zadim_quest` / `ostog_quest` / `enora_quest` / `arueshalae_quest` / `quig_quest` / `thalia_quest` / `zova_quest` / `daeran_quest`

---

## 📊 RELATIONSHIP SCORE VALUES

| Score | Label | Companion behavior |
|-------|-------|--------------------|
| −2 | Hostile | May argue, give false info, perform minimally |
| −1 | Strained | Clipped dialogue, minimum combat performance |
| 0 | Neutral | Professional, duties only |
| +1 | Friendly | Shares opinions, full performance, opens personal dialogue |
| +2 | Devoted | Takes hits for player, shares hidden info, quest unlocked |

---

*KM_Glossary.md — Kingmaker PF2e Text Adventure | Flag Glossary v1.0*
