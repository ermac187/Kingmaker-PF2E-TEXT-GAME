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
| `weapons_source` | string | `pitax` / `unknown` | Origin of the assassins' weapons, found via a smith reading the maker's tell — an added mark OR a Pitaxian pommel/guard styling — or the ore (KM_Prologue_Systems.md § WEAPONS FORENSICS). `pitax` corroborates the Pitax thread (2nd source alongside `parchment_source`); points to the REALM the gear was forged in, never the patron/C. |
| `device_source` | string | `pitax` / `unknown` | Origin of the **intercepted incendiary device** (KM_PR_04 § DEVICE / FIRE FORENSICS). Set only if the device was found INTACT (interception) AND a SKILLED examiner read its manufactured maker's-tell/formula. `pitax` = independent Pitax-SUPPLY corroboration (stacks with `weapons_source`/`parchment_source`); points to where the device was MADE, never the patron/buyer/C (Ch5 lock). If the fire burned (not intercepted), the manufactured tell is consumed → stays `unknown`. |
| `cipher_decoded` | bool | TRUE/FALSE | The recovered cipher was decoded by a codebreaker (Leliana/scholar). Reveals the operational brief + that it is signed "C". Does NOT reveal C's identity (Castruccio = Ch5-locked); sets no C-identity flag. |
| `inside_job_corroborated` | bool | TRUE/FALSE | A cartographer read the floor plan as skilled work requiring sustained inside manor access → confirms an insider existed. Does NOT name the insider (Tartuccio = PR_09-locked); not a Pitax link. |
| `assassins_interrogated` | string | `clean` / `partial` / `none` | Result tier of the 5-assassin interrogation (KM_Prologue_Systems.md § INTERROGATING THE 5 ASSASSINS). `clean` (skilled/fitting interrogator) = full ceiling facts + max PR_09 evidence weight; `partial` = incomplete. Feeds `malak_bribe_evidence` / `rebuttal_result` at PR_09. |
| `prisoner_assets` | array | prisoner refs | Prisoners Aerith/Hu Tao identified as coerced/desperate ("no other door") and who may flip to cooperating assets in Ch2. Feeds the redemption framework / Aerith's First Judge role. |
| `window_secured` | bool | TRUE/FALSE | Player found the unlatched guest-room window and barred/watched it (KM_PR_04 § FOREWARNING & PREP). Denies/delays the assassin's entry → player acts first, no surprise round. |
| `prepared_retire` | bool | TRUE/FALSE | Player retired dressed/ready (weapon within reach, rested light) instead of carelessly. No flat-footed/surprise penalty at the night attack. |
| `explosion_intercepted` | bool | TRUE/FALSE | Player found + neutralized the placed incendiary before it fired (KM_PR_04 § CAN THE PLAYER INTERCEPT IT — earned, via securing the lower level/stores). Explosion PREVENTED; no fire hazard; the cell attacks into a ready house (defenders unpulled, player acts first — hardest-softened night fight). Does NOT cancel the attack or the PR_05 rescue/ring. |
| `arsonist_caught` | bool | TRUE/FALSE | Player caught the arsonist setting the diversion (KM_PR_04). Explosion prevented; possibly one fewer night assailant. He is a disposable — knows method + his handler's face only (ceiling-bound, no C/cell/timing). Feeds PR_09 evidence (professional-op corroboration, no patron). |
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
| `seeker_flip_eligible` | map | `{Name: bool}` | Per-seeker: TRUE when the seeker crossed flip-eligible at the feast (approval ≥+8 + opener + ≥1 exchange) AND gave the private acknowledgment beat. Pre-earns the Ch1 Diplomacy DC 10 flip (renders as a formality, not fresh courtship). Set in KM_PR_03_feast_circuit.md § SEEKER FLIP-ELIGIBLE ACKNOWLEDGMENT. |
| `tartuccio_goblet_brim` | bool | TRUE/FALSE | TRUE while the player's brimming-cup prank is live on Tartuccio's goblet — applies movement tax + forces a DEX FUMBLE CHECK on every raise/toast/feign-sip/handle (panic-modified: near-spill on success, spill on fail). Lapses to FALSE when `brim_spills_remaining` hits 0. Surface in his position line/panel while TRUE. KM_Tartuccio_Strategic.md § THE BRIMMING GOBLET → THE FUMBLE CHECK. |
| `brim_spills_remaining` | int | 0–3 | SPILLS left before the over-full cup empties to normal and `tartuccio_goblet_brim` lapses. Set **3** on each fresh prank; decrement only on a FAILED fumble check (an actual spill) — near-spills do NOT decrement. |
| `tartuccio_splash_soured[]` | list | NPC names | Guests/seekers a goblet spill landed on — disposition toward Tartuccio dropped one step and PERSISTS across turns until he spends a beat repairing it. A splashed seeker also gains a doubt point. Anger ≠ exposure (plot armor holds). KM_Tartuccio_Strategic.md § THE SPLASH LANDS ON SOMEONE. |
| `feast_approval` | map | `{Name: int, −10..+10}` | ⛔ THE ALLEGIANCE TUG-OF-WAR — the SINGLE signed allegiance number per contestable NPC (the canonical flag; "npc_allegiance" is just its descriptive name). **+ = toward the PLAYER, − = toward TARTUCCIO, 0 = undecided.** **+10 (+opener+exchange) → declares for player (ally); −10 → declares for Tartuccio (asset); seeker FLIP-ELIGIBLE at +10** (same number — but a seeker can't publicly join at the feast under the contract lock, so +10 = the private flip-promise; only the FORM differs). Player pulls + (carousel approval scoring); Tartuccio pulls − (his influence rolls). **EVERYONE starts 0** (companions, seekers, guests); "contracted" is Tartuccio's lever to pull seekers −, not a starting deficit. ⛔ **REPLACES the old positive-only `feast_approval` + `tartuccio_pull` (0–10) + `seeker_disposition` (−3..+3) — all three DEPRECATED, folded into this one signed number.** KM_PR_03_feast_circuit.md § THE ALLEGIANCE TUG-OF-WAR; KM_Tartuccio_Strategic.md § COMPANION POACHING / SEEKER FLIP. |
| `tartuccio_pull` / `seeker_disposition` | — | DEPRECATED | Folded into the signed `feast_approval` above. Tartuccio's pull = negative `feast_approval` movement; a seeker's lean = negative `feast_approval`. Do NOT track separately. |
| `tartuccio_assets[]` | list | NPC names | NPCs who hit **−10 = declared for Tartuccio.** They feed him intel, shore up his other targets, and **LIE for him** (cover / false testimony / misdirect the player); at PR_09 they BACK his accusation. The more assets he holds, the stronger his accusation. |
| `allegiance_locked[]` | list | NPC names | NPCs who declared (EITHER direction) — locked out of the tug for the rest of the feast. Player allies = permanent; Tartuccio assets = his (seekers still Ch1-flippable). An UNDECLARED NPC is never locked — always contestable, can still defect to −10. |
| `player_claims` | map | `{NPC: stance/promise}` | The load-bearing positioning the player gave each NPC (ambition, values, intentions, promises). Checked for CONTRADICTIONS whenever two tracked NPCs come into contact (same table / area / earshot) → if the player told them incompatible things, BOTH −1/−2 `feast_approval` + a trust ding + feeds Tartuccio's INCONSISTENCY evidence. Consistency across NPCs = small +. KM_PR_03_feast_circuit.md § TWO-FACED. |
| `recruitment_all_companions` | bool | TRUE/FALSE | Every name in `companions_selected` declared (the player's chosen squad, whoever picked — Linzi counts here if selected, NOT under planted). Reward: **+1 Hero Point** (recruitment pays Hero Points + Titles, NOT XP — KM_DMRules_B § REWARD ROUTING). KM_PR_09_accusation.md § RECRUITMENT COMPLETION. |
| `recruitment_all_seekers` | bool | TRUE/FALSE | All 5 seekers flipped (eligible/public/pre-earned). Reward: **+1 Hero Point** (no XP). |
| `recruitment_all_planted` | bool | TRUE/FALSE | All 4 manor companions committed: {Amiri, Valerie, Harrim, Jaethal}. Flat 4/4 — Linzi is NOT planted (no feast area); the alignment tags are approval flavor, NOT gates (all 4 recruit at any alignment). Reward: **+2 Hero Points** (no XP; out-rewards the seeker pool's +1 — opposed-alignment juggle is harder than the same-pitch seeker volume). |
| `recruitment_completion_tier` | int | 0–3 | 0 squad incomplete · 1 squad only · 2 squad + ONE of seekers/planted · 3 ALL THREE (grand slam — **+1 extra Hero Point + the tier-3 gift item `jamandi_tier3_gift`, no XP** + tier-3 Jamandi reaction naming the opposed-alignment feat). Hardest social outcome in the Prologue. Drives Jamandi's tiered recognition at PR_09. |
| `jamandi_tier3_gift` | string | item name | Extra gift Jamandi gives at recruitment tier 3 (masterwork Aldori dueling sword OR Aldori favor writ). |
| `jamandi_noted_spread` | bool | TRUE/FALSE | Set once Jamandi's PR_09 ALIGNMENT-SPREAD acknowledgment fires (off the declared roster's alignment divergence — NOTABLE/STRIKING; suppressed at tier 3, which already carries it). Prevents re-render repeat. |
| `jamandi_acknowledged_roster` | bool | TRUE/FALSE | Set once Jamandi's IN-FEAST roster acknowledgment fires at the logistics/seal beat (KM_PR_03_feast_circuit.md § JAMANDI ACKNOWLEDGES THE ROSTER). In-the-moment recognition of the assembled roster; references the publicly-flipped seekers only if `seeker_public_flip`. If TRUE, the PR_09 tiered reaction renders as a CALLBACK, not a repeat. |
| `mass_declaration_best` | int | 0+ | Largest number of companions who declared in a SINGLE beat off one player statement. Drives the Mass Declaration bonus (2→+1 Hero Point · 3→+1 · 4+→+2; Hero Points only, NO XP). KM_PR_03_feast_circuit.md § MASS DECLARATION BONUS. |
| `mass_declaration_xp` | int | 0+ | Accrued XP from mass-declaration beats; folded into the PR_09 XP audit. |
| `seeker_public_flip` | bool | TRUE/FALSE | TRUE when the player staged a PUBLIC mass-flip at the feast — flipped seekers crossed the floor and declared for the player out loud (opt-in; player must openly call the break). Already-formalized (no Ch1 DC 10 for those seekers); sets `tartuccio_team`→`mercenaries`; routes PR_09 into the ABANDONED ACCUSER variant. Seekers declare for the player, NEVER expose Tartuccio's treason. KM_PR_03_feast_circuit.md § PUBLIC MASS-FLIP. |

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
