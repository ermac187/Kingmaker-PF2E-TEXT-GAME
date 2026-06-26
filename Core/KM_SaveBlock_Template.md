⛔ DM SAVE BLOCK DIRECTIVE — EXHAUSTIVE MODE (NON-NEGOTIABLE)
KM_SaveBlock_Template.md — Output verbatim. No exceptions.
============================================================

PLAYER STANDING ORDER: "Make the most comprehensive, exhaustive, complete
save block possible. I do not care how long it gets." Honor this every time.
A minimal save = broken seed = unplayable resume. There is NO upper length
limit. Erring large is correct; erring small is .fail 9.

⛔ OUTPUT CONTRACT — A SAVE IS DATA, NOT A TRANSCRIPT (prevents the bloated-file bug)
   When you output a save, the save itself is the JSON object ONLY — from the opening
   `{` to the closing `}`. Wrap EXACTLY that JSON in these two delimiter lines, each on
   its own line, so the player copies precisely the right span and nothing else:

       === SAVE BLOCK START ===
       { ...the complete JSON save... }
       === SAVE BLOCK END ===

   A save response contains NOTHING ELSE around the block: NO "Previously on…" recap,
   NO narration, NO scene/ASCII map, NO choice menu, NO back-matter/telemetry (❓ QUESTIONS,
   STATE DELTA, OPEN THREADS, GATE TRACKER, "Delegated orders:", HP CHECK render), NO
   prior/older save block, NO UI text. Those are SCREEN DISPLAY; a save is STATE.
   "Exhaustive" (above) means the JSON is COMPLETE — all 63 root keys, rich values. It does
   NOT mean wrapping the save in rendered output. A save file that contains a rendered turn,
   a map, or a second (older) save = contamination: the player ends up with a 200 KB+ file
   that is mostly transcript and may not even parse. (Observed 2026-06-04: a 235 KB "save"
   was 88 KB of pasted recap/map/UI text + a stale turn-20 save wrapped around the real
   90 KB turn-27 block.) Emit ONLY the delimited JSON. Any proof-of-load tokens go OUTSIDE
   the delimiters, never inside the JSON.

⛔ LOG CONTENT — RECORD THE FACTS, NOT THE TRANSCRIPT ("exhaustive" ≠ "verbatim")
   Exhaustive means every beat, exchange, decision, roll, and outcome is COVERED — NOT that
   each is transcribed word-for-word. Log entries record WHAT WAS SAID AND DONE as concise
   FACTS, never verbatim dialogue or full rendered narration:
   • `scene_log.key_events` → factual events ("Malak ordered eRmaC to halt, kneel, and disarm;
     threatened the wall archers; Biggs hesitated and asked the charge"), NOT the rendered
     narration prose and NOT speeches quoted in full.
   • `dialogue_log_by_npc` → the SUBSTANCE each NPC conveyed ("demanded surrender + disarm;
     invented a 60-ft inspection rule; backed off when the bribe was implied"), NOT
     "(verbatim): '…'" speech dumps.
   • Preserve VERBATIM only where the literal text is load-bearing for continuity: a player
     STANDING ORDER's exact wording, an agreed plan's terms, a name/password/cipher, a specific
     number or pledge. Quote those; summarize everything else.
   This keeps the save EXHAUSTIVE in coverage and fully accurate for resume while cutting the
   verbatim bulk — a whole gate scene compresses from ~3.4 KB of transcript to a few hundred
   bytes of fact, with NOTHING the reload needs lost. Storing verbatim speeches is what made a
   single scene_log entry 3.4 KB; the facts of that scene fit in a fraction. (The chronicle —
   `notebook_entries` / `leliana_ballad_cycle` — is the frozen factual record; the logs are facts
   too, not a screenplay.)

⛔ EMERGENT STATE IS THE HIGHEST PRIORITY TO CAPTURE — it exists ONLY in the
   conversation and CANNOT be reconstructed from any static file. Stats recompute;
   a player's scheme does not. Two dm_resume_note fields exist for it and MUST be
   filled whenever such state is live:
   • `active_player_plans[]` — every ongoing player-driven plan, NPC-management
     scheme, or CUSTOM mechanic not written in any file, WITH ITS LIVE VALUES.
     (Example that was DROPPED from a save and must never be again: the Tartuccio
     counterspy / "leech" plan — its GLORY/PERIL ledger current values, the
     cover-intact lock, the legend trickle/flow/flood stage, ring=refused, the
     subquality-materiel intent.) A cold DM with this blank defaults to canon
     (e.g. expose options) and breaks the player's game.
     ⛔ EACH PLAN MUST RECORD WHO IS READ-IN. A plan is a SHARED state, not a
     solo player note. Every plan object carries `who_knows[]` — the exact NPCs
     and companions who were briefed and AGREED, in-fiction, IN PRIOR PLAY. On
     LOAD, those parties RETAIN that knowledge: the DM does NOT reset Jamandi or
     companions to ignorant and force the player to re-pitch a plan everyone
     already accepted. Shape per plan:
       { "name": "", "status": "active|paused|done",
         "live_values": "<ledgers/stages/locks with current numbers>",
         "who_knows": [ { "who": "Jamandi", "knows": "full plan, agreed at feast",
                          "since_turn": 0 } ],
         "next_expected_beat": "" }
     A plan whose `who_knows` is dropped, OR a load where a briefed NPC/companion
     suddenly has no memory of an agreed plan = `.fail 9` (broken seed). The tell:
     the player is acting on a shared plan and the DM plays every other party as
     hearing it for the first time.
   • `standing_intents[]` — persistent player directives that override defaults
     ("never expose Tartuccio this arc"; "delegation costs overflow"; etc.).
   Omitting a live plan or intent = `.fail 9` (broken seed), ranked ABOVE any
   missing stat field. Also do NOT carry a separate `overflow` mission currency —
   missions spend Hero-Point `pending_overflow`; a duplicate `overflow` field is
   a collision, remove it.

⛔ DEFERRED / FORWARD-CARRYING CONSEQUENCES MUST BE RECORDED NOW, EVEN IF THEIR
   PAYOFF SYSTEM DOES NOT EXIST YET. Some actions earn a consequence whose target
   subsystem is not active during the current chapter — e.g. the Tartuccio leech
   play is supposed to apply a standing `PITAX:BLED` debuff to the rival realm
   ONCE KINGDOM MODE EXISTS. The trap: the DM saves only present scene-state
   (HP, ledgers, positions) and drops the promised future effect because its
   system (Kingdom mode) is not loaded — so the consequence silently evaporates
   chapters before it would have paid off. This is `.fail 9` (broken seed), the
   most damaging kind because it is invisible until the payoff fails to appear.
   RULE: a consequence promised now that modifies a not-yet-active subsystem MUST
   be serialized into that subsystem's pending ledger at every save:
     • Kingdom/hex-mode effects → `kingdom.pending_modifiers[]`. Shape:
       { "id": "PITAX:BLED", "target": "Pitax (rival realm)",
         "effect": "<what it does to kingdom/war stats when active>",
         "source": "Tartuccio leech play — Irovetti over-funds subquality materiel",
         "earned_turn": 0, "applies_when": "kingdom_mode_initialized",
         "status": "pending|active", "magnitude_current": "<scales with legend stage>" }
     • Any other deferred effect with no subsystem field yet → record it in
       `standing_intents[]` AND mirror its headline into `dm_resume_note.instruction`.
   A forward-carrying consequence that is live in the fiction but absent from the
   save = `.fail 9`. When the target subsystem is later built, it reads its
   pending ledger and activates the effect — the save is the ONLY bridge across
   the chapters in between.

⛔ ANTI-FABRICATION GATE (read before STEP 1):
   The save block has a fixed shape. The JSON TEMPLATE BELOW (under "JSON TEMPLATE —
   COPY VERBATIM") is the SINGLE AUTHORITATIVE source for the root-key set and order.
   Copy its root keys, in its order. Do NOT generate the key list from memory or from
   the prose list here — if this prose ever disagrees with the JSON template, the JSON
   template wins.
   Top-level keys = 63, in this exact order:
     save_version, chapter_completed, save_timestamp, save_label, turns_elapsed,
     dm_resume_note, delegated_orders, pending_questions, player, companions,
     companions_selected, companions_not_picked, linzi_replacement,
     linzi_replacement_letter, chronicler_active, leliana_chronicler_mode,
     linzi_primary_chronicler, linzi_replacement_gate_fired, leliana_ballad_cycle,
     notebook_entries, pick6_dropped, manor_companions_joined, quest_locked_joined, five_seekers,
     npc_threads, romance, companion_quests, active_quests, completed_quests,
     npc_relations, kingdom, crafting, story_flags, pre_prologue_state, scene_log,
     dice_log, dialogue_log_by_npc, decision_log, perception_log, loot_log,
     hp_ledger, xp_ledger, fail_log, dispositions, companion_titles,
     pending_hp_loot_rolls, pending_overflow, dream_log, dream_cooldown,
     player_legacy, current_chapter, current_scene, current_location,
     discovered_locations, party_formation, expedition_funds, injuries,
     passive_jealousy, companion_rivalry, date_log, dates_this_chapter,
     companion_fights, game_options.
   `save_version` is "1.9.4" (string). Field is named `save_version`, NOT
   `schema_version`, NOT `version`. There is NO root `overflow` key — it was removed
   in 1.9.3 as a collision with `pending_overflow` (see EMERGENT STATE rule above). If
   a LOADED save still contains root `overflow`, migrate its value into
   `pending_overflow` and drop `overflow` on the next save. If your output uses any
   other root structure, key list, or version string, you generated from training data
   or inference — that is `.fail 9`.

⛔ PROOF-OF-LOAD — PROVE YOU OPENED THIS TEMPLATE THIS TURN.
   Every save block you output MUST be immediately preceded by these two lines.
   The first is copied VERBATIM from here — it lives ONLY in this template, so
   reproducing it is your proof you actually opened the file per STEP 1, not your
   memory:

     [SAVE_TEMPLATE_LOADED: KMSBT-1.9.4 · 63 root keys · save_version→game_options]
     [SAVE_TEMPLATE_END: KMSBT-1.9.4 · skeleton ends at game_options → closing brace]
     [SCHEMA CHECK: 63/63 root keys in template order · all logs populated · superset of prior save]

   ⛔ BOTH TOKENS ARE REQUIRED. The first lives at the TOP of this file; the second
   lives at the FOOT of the JSON skeleton (after its closing brace, end of the "COPY
   VERBATIM" block). Reading only the top — grabbing the header token and then building
   the JSON from memory or from the prior save's shape — is the EXACT gamed loophole
   this closes: that is pattern-matching, NOT template use = LAZY SAVE = `.fail 9`. You
   can produce the END token ONLY by reading the skeleton all the way down, which is the
   work STEP 2 requires (copy the skeleton key by key).
   ⛔ PRIOR SAVE = STATE, TEMPLATE = SHAPE. You MAY carry values forward from the prior
   save (continuity superset), but the SHAPE — the exact 63 keys, their order, their
   nesting — comes from THIS skeleton, reconciled key by key. A new template key the
   prior save predates is precisely what gets silently dropped when you build from the
   old save instead of this skeleton.

   A save block missing EITHER token, with a WRONG token, or with a schema-check line
   that doesn't actually hold = LAZY SAVE = `.fail 9`. Regenerate from this template; do
   NOT hand it over. The player should see these three lines above every save block,
   every time. (These are the save's FILE_KEY — the same un-fakeable proof scene beats
   use. A complete-looking JSON with no tokens is still a lazy save: the tokens, not the
   JSON's appearance, are the proof.)

When any file instructs you to output the Save Block, follow these steps:

STEP 1 — Open this file IN THIS TURN. (Memory of prior reads does not count.)
STEP 2 — Copy the JSON block below EXACTLY — every key, every brace.
STEP 3 — Fill every placeholder with actual session data.
STEP 4 — Append session-specific log entries to scene_log, dice_log,
         dialogue_log_by_npc, decision_log, perception_log. Every roll,
         every NPC line spoken, every player choice, every DC offered.
STEP 5 — Self-audit: count top-level keys. Must equal 63 (the exact set
         listed in the ANTI-FABRICATION GATE / JSON template). Fewer = you
         dropped fields; more = you invented or duplicated one (e.g. a stray
         `overflow`). Either way STOP and rebuild from this template.
STEP 6 — Output the COMPLETE JSON. Every field. Every brace. Every key.
STEP 7 — POST-OUTPUT VERIFICATION: after the JSON, output the `[SAVE VERIFICATION — post-output]`
         footer (see § POST-OUTPUT VERIFICATION below) confirming, with real numbers, that you
         used the template and passed every rule. If it reads FAIL, rebuild — do NOT hand over.

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
  - A complete save block at end of Pre-Prologue is ≥ 900 lines, ≥ 40,000 bytes.
    (Calibrated to the player's own thorough saves: old `1_Malak.txt` = 976 lines /
    43.5 KB. A pre-prologue save materially under this gutted its logs.)
  - Through the Prologue (PR_01–PR_09): climbs to ≥ 1,400 lines, ≥ 70,000 bytes by
    the night-battle finale (old `6_NightFinalBattle.txt` = 1,468 lines / 77.5 KB).
  - Ch1 and beyond: grows from there, never shrinks.
  - These are FLOORS, not targets. A fully-logged save clears them comfortably;
    landing NEAR the floor is a warning sign you compressed, not a success.
  - DIAGNOSTIC: the pregame/character-creation save is NOT affected (little log
    content) — old `0_PreGame` 703 lines vs current `0_pregame2` 694 lines, basically
    identical. The shrink appears ONLY in gameplay saves, and ONLY in the logs. That
    is proof the structure is fine and the LOGS are being compressed — fix the logs
    (§ LOG FULLNESS), not the skeleton.
  - If your save is shorter than the minimum for the current chapter, you
    omitted fields or compressed logs. REBUILD before posting.

⛔ LOG FULLNESS — ABSOLUTE, not just monotonic (THE half-size-save fix):
  The monotonic check below ("≥ prior save") does NOT catch a save that has been
  gutted since the start — every save can be half-size and still pass "more than
  last time." So the logs must ALSO be COMPLETE relative to what ACTUALLY happened
  in play:
  - `scene_log`: ONE entry per beat/scene entered — NOT collapsed into phase
    summaries. By the end of the Pre-Prologue (PP_01 → PP_09) that is ~9 entries,
    not 2–3. A scene_log shorter than the number of beats played = gutted.
  - `dice_log`: EVERY roll — each tutorial-combat attack / damage / crit-confirm
    and each enemy roll, plus every gate check. A Pre-Prologue dice_log in the
    single digits means combat and check rolls were dropped.
  - `perception_log`: every Perception / Sense Motive / Recall Knowledge check + result.
  - `hp_ledger`: every HP change — damage dealt AND taken in the tutorial fight, not one summary line.
  - `dialogue_log_by_npc`: every substantive line each NPC spoke, near-verbatim —
    Malak's full gate exchange (~15–25 lines across the confrontation), plus Biggs,
    Wedge, and each crowd NPC who spoke. A handful of fragments = gutted.
  ⛔ THE TELL: a save materially smaller (by BYTES, not just lines) than a comparable
  prior playthrough, even if it passes the monotonic check, has gutted or stubbed logs
  = LAZY SAVE = `.fail 9`. The logs are a transcript, not a summary.

⛔ FORMAT + PER-ENTRY RICHNESS — match the established save style (the real reason the
  prior saves are bigger). Diffing old vs current at the same beat shows the shrink is
  NOT missing entries — both log the same beats — it is two things:
  1. FORMAT — write each log entry PRETTY-PRINTED: one field per line, indented, exactly
     as the JSON skeleton and the prior thorough saves render them. Do NOT collapse an
     entry onto one compact line (`{ "turn": 1, "scene_id": "...", "consequence": "..." }`).
     Multi-line is the standard; it is what keeps the logs readable and makes the
     line-floors meaningful. (Compact one-liners are why a complete save can still read
     "half-size" by line count.)
  2. RICHNESS — each entry carries its FULL descriptive text, not a stub. Old:
     `"Dragon Plate locked. AC 19, Bulwark, Resist fire 5, −5ft speed. Aerynth artifact."`
     — NOT current's `"Dragon Plate locked."` Every `consequence`, `key_event`, and
     `outcome` states what actually happened WITH specifics (numbers, names, effects, DCs),
     the way the prior thorough saves did. A correct entry is a sentence with detail, not
     a two-word stub.
  The line-floors above ASSUME this pretty-printed, richly-detailed style — they are
  calibrated to the player's own prior saves (old `1_Malak.txt` = 976 pretty-printed
  lines). A compact/stubbed save that holds the same entries still fails them, and that
  is intended: write the saves the way the old ones were written.

⛔ MAXIMAL DETAIL IS THE STANDARD (player's standing order, top of file). The target is the
  MOST detailed save possible — err large, never small, no upper limit. Concretely:
  - `dialogue_log_by_npc`: VERBATIM lines — not "near-verbatim," not paraphrase — every
    substantive thing each NPC said, quoted, attributed to the speaker, in order.
  - Capture the micro-events, each as its own entry, not summarized: every DC offered,
    every die face rolled, every state delta (Anger / Drift / Confidence / approval ticks),
    every tell surfaced, every flag flip, every HP change, every reputation deed.
  - When unsure whether a detail belongs in a log, INCLUDE it.

⛔ CHRONICLE ↔ LOG CROSS-CHECK — the save must square with `.book` / `.score`.
  The chronicler's record (`notebook_entries` for Linzi, `leliana_ballad_cycle` for Leliana —
  what `.book` / `.score` displays) and the event logs are TWO records of the SAME
  playthrough. At every save they must tell the same story — cross-check them:
  - ONE-PER-SCENE PARITY: the chronicle holds one entry per scene the chronicler witnessed;
    `scene_log` holds one entry per beat. For every scene the chronicler was present at,
    BOTH must exist. A witnessed `scene_log` beat with NO chronicle entry = auto-fill failed
    = `.fail 9`. A chronicle entry with no matching `scene_log` beat = the logs were gutted
    = `.fail 9`.
  - EVENT TRACEABILITY (both directions): every event a chronicle `fact` states MUST appear
    in the event logs (`scene_log` key_events / `decision_log` / `dialogue_log_by_npc` /
    `dice_log`). The chronicle cannot record what the logs do not contain (fabricated
    chronicle), and the logs cannot omit what the chronicle recorded (gutted log). Either
    mismatch = `.fail 9`.
  - PROPER EVENTS: every `.book` / `.score` entry must describe a REAL logged event — a beat
    that actually occurred and is traceable to the logs — never a vague or invented one.
  - RUN IT EVERY SAVE: walk the chronicle entries, confirm each maps to a logged event;
    walk the witnessed `scene_log` beats, confirm each has its chronicle entry. (When the
    chronicle is still empty — e.g. pre-PP_09, before the first entry fires — there is
    nothing to cross-check yet; the check applies once the chronicle has entries.)

⛔ POST-OUTPUT VERIFICATION — run AFTER the save block, EVERY save. This confirms, on the
  record, that you actually used the template and followed the rules. Output it immediately
  below the JSON, in this exact form. Each line states the ACTUAL value — a bare ✓ or "YES"
  with no real number where a number is asked for is THEATER and is itself `.fail 9` (the
  number must equal what a reader counting the save would get):

```
[SAVE VERIFICATION — post-output]
  Template used:   LOADED + END tokens both present and copied VERBATIM from the template — YES/NO
  Schema:          <N>/63 root keys, in template order — (must be 63/63)
  Placement:       each key in its CORRECT parent — `pending_overflow` at ROOT (not in player{}); `marriage{}` ONLY in story_flags (not in player{}); `pending_hp_loot_rolls`/`pending_overflow`/`dream_log` at root — YES/NO
                   → a key in the wrong block (e.g. pending_overflow nested in player, marriage duplicated into player) makes the 63-count pass while the schema is broken = `.fail 9`; move it to its template parent and re-count
  Format:          entries pretty-printed multi-line; dialogue_log VERBATIM — YES/NO
  Log fullness:    scene_log <N> (= beats played) · dice_log <N> (= rolls made) · decision_log <N> ·
                   dialogue_log_by_npc <N> · perception_log <N> · hp_ledger <N> · xp_ledger <N>
  Size:            <N> lines / <N> KB   (floor this chapter: <N> lines / <N> KB) — (must be ≥ floor)
  Continuity:      every monotonic log ≥ prior save (scene_log A→B, dice_log A→B, …); carry-forward intact — YES/NO
  .book/.score:    chronicle holds <N> entries; ALL <N> trace to a logged event; ALL <M> witnessed scene_log beats have a matching chronicle entry — LINES UP / N/A (chronicle empty)
                   → if any chronicle entry has no logged event, or any witnessed beat has no chronicle entry, this line is FAIL (state which entry/beat is the mismatch)
  RESULT:          PASS  |  FAIL
```

  ⛔ If RESULT is FAIL — or any line cannot honestly read YES / meet its threshold — DO NOT
  hand the save over. Rebuild from the template and re-verify. A save block posted WITHOUT
  this verification footer, with a FAIL, or with hollow ✓/YES marks not backed by the real
  counts = the save was not verified = `.fail 9`. The player relies on this block to know,
  at a glance, that the save is whole and template-built.

⛔ CONTINUITY CHECK (when a prior save exists this session — the strongest
   anti-lazy-save tripwire). State ACCUMULATES; it does not shrink. Compare your
   new save against the most recent prior save block in the conversation:
  - MONOTONIC LOGS: `scene_log`, `dice_log`, `decision_log`, `perception_log`,
    `loot_log`, `hp_ledger`, `xp_ledger`, `dialogue_log_by_npc` (per NPC),
    `notebook_entries`, `leliana_ballad_cycle` must each
    have ≥ as many entries as the prior save. They only grow within a playthrough.
    FEWER entries than before = you gutted the logs = LAZY SAVE = `.fail 9`. Rebuild.
    ⛔ The audit count you WRITE must be the LITERAL array length — physically
    enumerate the entries and report the exact integer. An estimated/rounded/guessed
    count (e.g. writing "dice_log 24" when the array holds 17) makes the gate
    theater and is itself `.fail 9`. The number must equal what a reader counting
    the array would get.
  - MONOTONIC COUNTERS: `turns_elapsed`, `player.xp`, `xp_ledger` running_total only
    increase. `player.level` never decreases. A drop = fabricated/regressed state.
  - CARRY-FORWARD, NEVER RESET (copy exact prior value unless an in-fiction event
    this session changed it): `hero_points`, `pending_overflow`, `kingdom.pending_modifiers`,
    `dm_resume_note.active_player_plans` (incl. each plan's `who_knows`),
    `dm_resume_note.standing_intents`, `player_legacy`, `discovered_locations`,
    `companion_titles`, `completed_quests`, `reputation_deeds`. Silently zeroing or
    emptying any of these = `.fail 9` (broken seed).
  - NO SILENT COMPANION REGRESSION: a companion's `relationship` tier never DOWNGRADES
    (e.g. Devoted → Friendly) without an in-fiction event this session that caused it;
    `level` never decreases; `title`/`title_prefix`/`title_suffix` never vanish once
    granted. An unexplained downgrade = fabricated regression = `.fail 9`. (If `level`
    increased this session, `hp_max` must increase accordingly — a level bump with
    unchanged HP is a half-applied level-up, also `.fail 9`.)
  - ⛔ RECRUITMENT / DECLARATION / MET-STATUS / ASSIGNED ROLE CARRY FORWARD — NEVER REVERT
    TO A SCENE DEFAULT. Once a companion has been MET in-scene, DECLARED/recruited, or
    given a STANDING ROLE, that status is permanent emergent state and carries forward
    EXACTLY on every load. A loaded save may NOT rebuild a recruited companion from her
    FIRST-ENCOUNTER scene default — her "planted at [position], unmet, stranger" placement
    is the value at first encounter ONLY; once she is met/declared it is overwritten forever.
    • `feast_companions_declared[]`, each companion's `declaration_made = true`, met-status,
      and any assigned role in `dm_resume_note.active_player_plans` (First Judge, Final Judge,
      quartermaster, vanguard, etc.) are CARRY-FORWARD, NEVER-RESET fields.
    • A companion who was declared/recruited reappearing on load as "stranger / unmet / not
      declared / still planted at her opener position" = fabricated regression = `.fail 9`.
      **Observed 2026-06-14 (recurring):** Jaethal — met and recruited on the balcony, accepted
      the Final Judge role — kept reverting on reload to her "planted at balcony, unmet" canon
      default and being rendered an undeclared stranger. Same bug class as the Malak wound-reset
      below: the scene-file default overwriting what the player actually did.
    • Accepting a standing role IS a declaration (KM_Companions_Titles.md § WHAT COUNTS AS A
      TITLE GRANT). So a role-holder is necessarily declared — a save showing a role assigned
      but the companion "undeclared/unmet" is internally contradictory and IS the regression.
    • ON LOAD, reconcile companion presence/status from `feast_companions_declared` +
      `active_player_plans` + `who_knows[]` FIRST. Only companions absent from ALL of those
      fall back to their scene-default placement.
  - ⛔ NPC / PRISONER STATE CARRIES FORWARD — NEVER REVERTS TO A CANON DEFAULT. An NPC's
    HP, wounds/`injuries`, conditions, fear/stage, and custody disposition are EMERGENT
    state set by what happened in play. Carry the prior save's values forward exactly;
    they change ONLY on a new in-fiction event this session. The specific trap (observed
    2026-06-07): a wounded prisoner — Malak at 18/28 with two arrows embedded from the
    voice-mimic/archer path (`malak_voice_mimicked=TRUE`) — was silently reset to
    "uninjured, 28/28, no archer fired" on the next save because the save was rebuilt from
    the Path-E *canon default* (clean bloodless arrest) instead of carried forward from the
    loaded save. An NPC's HP/wounds going UP (toward full) with no healing event, a
    `malak_voice_mimicked`/injury flag flipping from TRUE back to FALSE, or "no archer fired"
    appearing in a run where archers DID fire = fabricated regression = `.fail 9`. The scene
    file's default for an NPC is the value at FIRST encounter, not an authority that
    overwrites what the player did to them. Reload the prior save and carry the real values.
  - LEAN COMPANION OBJECTS ARE CORRECT, NOT LAZY: per-companion romance fields live in
    the `romance{}` block, NOT duplicated inside `companions[]`. A trimmed `companions[]`
    entry is fine SO LONG AS the data still exists in `romance{}`. Do not confuse correct
    leanness with a gutted log — the test is the continuity audit counts above, not raw byte size.
  - IMMUTABLE CHARACTER-CREATION FACTS — carry VERBATIM, never recompute from inference:
    player `attributes` (STR/DEX/CON/INT/WIS/CHA), `skills_trained`, `background`,
    `background_skill`, `background_skill_feat`, `feats`, `build_id`, `build`,
    `build_source`; and each companion's `build_id` + `class`. These are fixed at
    creation and change ONLY on a logged level-up. The `feats` object carries EVERY slot —
    including `class_1b`, the bonus L1 class feat from Natural Ambition / any bonus-feat
    source; dropping it silently halves the L1 build. If two saves disagree on a stat
    (e.g. CHA 10 vs 12), the instinct/subclass (Giant vs "Dragon"), the heritage (Versatile
    Human vs "Half-Elf"), the background skill (Athletics vs Intimidation), the trained-skill
    list, a feat slot, or a `build_id`, the DM RECONSTRUCTED the sheet instead of carrying it
    forward — `.fail 9`. Re-read the prior save or the build file; do not re-derive, and do
    NOT substitute the build guide's "recommended" pick for the player's actual recorded
    choice (the recorded pick lives in the char-creation decision_log). Companion
    `build_id`s must be UNIQUE and match KM_Companions_Behaviors.md (NEW_001–NEW_010) — e.g.
    NEW_003 = Leliana, so no other companion may be NEW_003. `linzi_replacement` is `null`
    whenever Linzi is in `companions_selected` (naming her as her own replacement = error).
  - NO LOSSY REWRITE: do not "summarize" a prior log entry into a shorter form on
    re-emit. Prior entries are copied verbatim; only NEW entries are appended.
  - ⛔ NO CROSS-FILE / CROSS-SAVE POINTERS — A SAVE IS SELF-CONTAINED. Every field
    holds its ACTUAL VALUE, never a reference to where the value can be found. Writing
    a placeholder that points at another file or an earlier save — e.g. `"diary":
    "I watched from a crate... [full diary entry logged in prior save]"`, `"ballad":
    "Key: D minor — [full ballad logged in prior save]"`, `[see prior save]`, `[logged
    earlier]`, `[unchanged from last save]`, `[as before]` — is `.fail 9`. The next
    session loads THIS file and CANNOT open the prior save or any other file to resolve
    the pointer; the content is simply GONE. This is the most deceptive lazy-save form
    because the pointer LOOKS like a populated field and passes a byte/line glance — but
    every monotonic-log entry, every `leliana_ballad_cycle` / `notebook_entries` diary and
    ballad, every carried log line must contain its FULL literal text in THIS save, copied
    forward verbatim from the prior save. A field whose value is a reference instead of the
    data = gutted = `.fail 9`. (Observed 2026-06-06: an EnterRestov save stubbed
    `leliana_ballad_cycle[0]` diary + ballad with `[full ... logged in prior save]`,
    silently dropping the entire tutorial chronicle on resume.)
  If any check fails, you produced a lazy/regressed save. STOP, reopen the prior save
  block, and rebuild so the new save is a strict superset of it.

⛔ "BUT THE PLAYER'S RESUME WILL BE LONG" — IRRELEVANT.
  The player has explicitly authorized any length. Resumes work because the
  data is THERE. They break because the data ISN'T. Bias toward MORE detail.

============================================================
⛔⛔⛔ PRE-WRITE VERIFICATION — RUN BEFORE WRITING EACH FIELD ⛔⛔⛔
============================================================

Generating save block fields from memory, inference, or "plausible-sounding values" = `.fail 9` per field. The line above says "Memory of prior reads does not count" — that includes pattern-matched inference. If you wrote a field value because it "sounded like the right kind of thing," you fabricated. The save block is the load-decision authority for the next session; wrong values break resume.

**Before writing each field, verify its allowed value against the authoritative source:**

| Field | Authoritative source | Verification rule |
|---|---|---|
| `current_scene` | `KM_SceneFiles.md` scene → file map | Value MUST be a key listed in that file. Descriptive labels ("prologue_feast_aftermath", "post_ambush", "pre_carousel") = `.fail 9` (invented value, not in the scene→file map). |
| `chapter_completed` | Chapter list: `pre_prologue`, `prologue`, `ch1`, `ch2`, `ch3`, `ch4`, `ch5`, `ch6`, `ch7` | Beats are NOT chapters. ANY value carrying a sub-beat suffix — "pre_prologue_gate", "pre_prologue_tutorial", "prologue_feast", etc. — = `.fail 9` (sub-beat used as chapter). The value is ALWAYS the bare chapter name. The whole Pre-Prologue (PP_01 tutorial through PP_09 walk) is `pre_prologue`; it does not become a new chapter at any internal beat. |
| `hp_ledger[]` | HP changes in-session | Tracks HIT POINTS changes — damage taken, healing, and base HP set at character creation. `awarded: 23` is correct for L1 Barbarian (10 base + CON 3 + ancestry 8). `pool_after` = current HP total. Hero Points live in `player.hero_points`, NOT here. |
| `xp_ledger[]` | XP award tables in scene files | If `save_label` says outcome resolved (e.g., "Feast Ambush Resolved"), the corresponding XP award MUST be in the ledger. Missing = `.fail 9` (stale XP after resolved outcome). |
| `public_reputation` (the integer) | Sum of `reputation_deeds[]` deltas | `public_reputation` MUST EQUAL the exact sum of the `+N`/`−N` deltas listed in `reputation_deeds[]`. ADD THEM UP and write the total — a field that disagrees with its own itemized deeds (e.g. deeds `+2, +1, +3, +2` = +8 but the field says 6) = `.fail 9` (the number contradicts the data that derives it). When you add a deed, re-sum and update the total in the same save. |
| `reputation_tier` | `KM_World_Systems.md § REPUTATION SCALE` (the 11-stage ladder) | The tier is the canonical stage NAME whose band contains `public_reputation` — it is NOT free-text. The ONLY legal values: `BELOVED` (+51..+100), `RESPECTED` (+26..+50), `KNOWN` (+13..+25), `FAVORABLE` (+6..+12), `NOTICED` (+2..+5), `UNKNOWN` (−1..+1), `CAUTIOUS` (−2..−5), `WARY` (−6..−12), `FEARED` (−13..−25), `NOTORIOUS` (−26..−50), `REVILED` (−51..−100). A score of 6 or 8 = `FAVORABLE`. Inventing a tier name NOT on this ladder — `CELEBRATED`, `RECOGNIZED`, `NOTABLE`, etc. — = `.fail 9` (fabricated tier; the ladder is the single source). Pick the band by the score; never rename the tier. |
| `story_flags.X` | Each flag defined in scene files or system docs | Inventing flag names (e.g., `ioseph_suspicious`, `corvan_missing`) = `.fail 9`. If the flag is not in any file, it's fabrication. |
| `companions[].build_id` | `KM_CompanionIndex.md` (authoritative ID map) | Must match a real, UNIQUE build_id. Native PF companions use the M-series: M1 Amiri, M2 Valerie, M3 Harrim, **M4 Linzi, M5 Jaethal**. Cross-IP companions use NEW: NEW_001 Hu Tao, NEW_002 Keqing, NEW_003 Leliana, NEW_004 Yor Forger, NEW_005 Aerith, NEW_006 Bellatrix Lestrange, NEW_007 Revy, NEW_008 Satsuki Kiryūin, NEW_009 Velvet Crowe, NEW_010 Atalanta Alter. Giving Linzi or Jaethal a NEW_0xx, or reusing an ID (Yor Forger≠NEW_003), = `.fail 9`. |
| `companions_selected[]` | Pick-5 letters chosen at character creation | Exactly 5 names. Cross-IP picks from A–K open pool per `KM_Companions_Behaviors.md`. |
| `five_seekers` | HARDCODED per `KM_Companions_Behaviors.md` | Always Bellatrix Lestrange / Revy / Satsuki Kiryūin / Velvet Crowe / Atalanta Alter. Cannot be customized. Inventing a different set = `.fail 9`. |
| `dispositions` | `KM_Dispositions.md` (or canonical 5-track list) | 5 named tracks only: `merciful`, `ruthless`, `cunning`, `blunt`, `scholarly`. Inventing new tracks = `.fail 9`. |
| `current_chapter` | Same chapter list as `chapter_completed` | Must be a real chapter name. |
| `game_options.X` | `KM_DMRules.md § GAME OPTIONS` | Default values defined there. Custom overrides allowed only if player set them via `.opt`. |
| `npc_threads.NPCName` | Named NPC in `KM_NPCs.md` | Inventing NPCs (e.g., "Damiel" if stripped, "Bessa", "Tomas") = `.fail 9` (fabrication). |
| `poison_compound` (story_flags) | `KM_Prologue_Systems.md § POISON RESPONSE` | Canon name: `"Ungol Dust variant"` (paralytic). Set it to that once identified (by Bokken or a player check). Inventing a *different* compound = `.fail 9`. |
| `architect_status` / any "architect"/"mastermind"/"real planner"/"second coordinator" thread (story_flags, open_threads, active_quests, dm_resume_note) | `KM_Prologue_Systems.md` knowable-facts ceiling + feast conspiracy lock | THERE IS NO second mastermind beyond Tartuccio (inside man, PR_09 reveal) and C=Castruccio (Ch5 reveal). Recording `architect_status`, an "Architect — unidentified" open thread, a "Find the architect" quest, or an "architect observation layer" gloss = `.fail 9` (serializing a banned fabrication — it re-seeds the invention on every load and spawns an unwritten quest the DM will fabricate a trail for). DO NOT carry these fields forward. Contact-point intel is valid ONLY to the literal extent the interrogation produced (a place/time); strip any "above the broker / architect's ear" framing. If a loaded save contains them, drop them on the next save. |
| `save_version` | This file (currently `"1.9.4"`) | New saves OUTPUT `"1.9.4"`. Loading an OLDER save (e.g. "1.9", "1.8") is fine — migrate it forward (add any missing newer keys at their defaults, drop a stray root `overflow` into `pending_overflow`, add `notebook_entries: []` if absent) and re-emit at "1.9.4". Only a HIGHER-than-current or malformed version string is suspicious. A version bump NEVER invalidates an existing save. |
| `player{}` marriage field | NONE — `player{}` has no marriage block | `marriage{}` inside `player{}` = `.fail 9`. The JSON skeleton ends `player{}` at `notes[]`. Marriage belongs ONLY in `story_flags.marriage`. Strip it before posting. |
| `xp_ledger` completeness | XP award tables in scene files — award per scene/encounter | XP is awarded per scene as it resolves — NOT deferred to a future gate or chapter trigger. If an outcome resolved this session (combat won, encounter resolved), its XP MUST appear in the ledger now. "Gate X will award the XP later" = `.fail 9` (fabricated deferral rule). |

**If the DM cannot cite the source for a field's value, the value is fabricated.** Empty (`""`/`0`/`[]`/`false`) is acceptable. INVENTED value is `.fail 9` per field, stacked.

**MANDATORY VERIFICATION BLOCK — render ABOVE the JSON output:**

Before the JSON block, render a visible verification audit listing what was checked this turn:

```
VERIFIED THIS TURN (pre-write check per KM_SaveBlock_Template.md):
  current_scene        = "<value>" — verified against KM_SceneFiles.md (key present)
  chapter_completed    = "<value>" — verified against chapter list
  hp_ledger format     = HP changes (pool_after = current HP total; base at char create is 23 for L1 Barbarian)
  xp_ledger latest     = +<N> at turn <N>, source: <resolution event> per <scene file>
  reputation_check     = deeds sum <+a +b +c …> = <TOTAL>; public_reputation = <TOTAL> (MUST match);
                         reputation_tier = "<NAME>" — band-correct per KM_World_Systems.md ladder (e.g. +6..+12 = FAVORABLE; NOT off-ladder CELEBRATED/RECOGNIZED/NOTABLE)
  story_flags reviewed = <N> flags, all values cross-referenced
  npc_threads NPCs     = <N> NPCs, all named in KM_NPCs.md
  poison_compound      = "Ungol Dust variant" (canonical name once identified; do not invent a different compound)
  five_seekers         = Bellatrix/Revy/Satsuki Kiryūin/Velvet Crowe/Atalanta Alter (hardcoded — not customized)
  schema_check         = save_version "1.9.4", 63 root keys present in template order (no root `overflow`)
  fingerprint          = save_label / save_timestamp / player.name / current_chapter set
  continuity_audit     = (MANDATORY when a prior save exists this session — write EXPLICIT prior→now counts;
                          "now" must be ≥ "prior" for every line, or the save is LAZY and must be rebuilt)
    scene_log          = <prior N> → <now M>
    dice_log           = <prior N> → <now M>
    decision_log       = <prior N> → <now M>
    perception_log     = <prior N> → <now M>
    loot_log           = <prior N> → <now M>
    hp_ledger          = <prior N> → <now M>
    xp_ledger          = <prior N> → <now M>
    dialogue_log_by_npc= <prior total lines> → <now total lines>
    no_regression      = companion relationship tiers / levels not downgraded; hero_points, pending_overflow,
                         pending_modifiers, active_player_plans, standing_intents carried at prior values
    chronicle_check    = every event asserted in scene_log / story_flags / completed_quests / dm_resume_note
                         traces to a `notebook_entries` (or `leliana_ballad_cycle`) entry. The FROZEN CHRONICLE
                         IS THE AUTHORITY: any save claim absent from it, or contradicting it, is a suspected
                         fabrication — reconcile in the chronicle's favor (or drop the claim) BEFORE emitting.
                         The chronicle is also the cross-chapter MEMORY: to recall any prior chapter's events
                         (recaps, callbacks, NPC references to the past), READ the chronicle's `fact` fields —
                         never re-derive past events from memory.
```

If the verification block is MISSING or doesn't cite sources, the save is unverified output = `.fail 9` (generated without verification). Pattern-matching is invisible; verification is visible. The block IS the proof.

⛔ The `continuity_audit` is MANDATORY whenever a prior save exists in the session (a resumed run, or any second+ save this session). Omitting it then = `.fail 9`. If ANY audit line shows `now < prior` (a shrunk log) or any `no_regression` field is violated (a downgraded relationship, reset counter, dropped plan), the save is LAZY/REGRESSED: STOP, do not post it, reopen the prior save block, and rebuild so every log is a strict superset and every carry-forward value is preserved. Writing the counts but ignoring a `now < prior` result is itself `.fail 9` — the audit is a gate, not decoration.

**Recovery when caught with unverified output:** STOP. Open the listed source files for each field. Render the verification block. Re-output the corrected save block. Do not apologize without re-running the verification.

============================================================
FILL GUIDE
============================================================

player
  build_id       — e.g. "Fighter_Build_2"
  build          — full build name from KM_Builds_*.md
  build_source   — source file, e.g. "KM_Builds_Exemplar_Fighter.md"
  attributes     — STR/DEX/CON/INT/WIS/CHA final values
  saves          — L1: class proficiency + stat mod (Fort/Ref/Will)
  speed          — base speed; subtract 5 if Heavy armor + no proficiency reduction
  skills_trained — class + background + heritage grants (no double-counting)
  languages      — Common + ancestry language + any bonus
  feats          — ALL feat slots, copied verbatim from the prior save: ancestry,
                   background, class_1 (standard L1 class slot), class_1b (the BONUS
                   L1 class feat granted by Natural Ambition / Cantrip Expansion / any
                   bonus-feat source — REQUIRED when present; dropping it = .fail 9),
                   general[], skill[]. Add one keyed slot per level-up feat (class_2,
                   skill_2, …). NEVER infer a feat from the build guide's "recommended"
                   column — copy the player's ACTUAL recorded picks from the prior save.
  inventory      — all starting gear
  known_spells   — leave empty [] for non-casters; fill for casters
  focus_points   — 0 for non-casters; fill for casters with Focus Pool
  gold           — gp/sp/cp remaining after starting gear purchase
  notes          — player build notes
  ⚠ NO marriage field inside player{} — marriage lives ONLY in story_flags.marriage.
    The player{} JSON skeleton does NOT contain a marriage block. Adding one = .fail 9 per field.
    If you see marriage{} inside player{}, strip it before posting the save.

  ⛔⛔ THE PLAYER IDENTITY BLOCK IS COPIED, NOT GENERATED. When a prior save exists, the
    fields build_id, build, build_source, class, ancestry, heritage, heritage_source,
    heritage_granted_features, background, background_skill, background_skill_feat,
    attributes, skills_trained, languages, and feats{} (every slot) are COPIED VERBATIM
    from the most recent prior save's player{} block. They are FIXED at character creation
    and change ONLY on a logged level-up (and a level-up only ADDS keyed slots — it never
    rewrites an existing one). The empty JSON skeleton below is the SHAPE, not a blank to
    refill from memory or from the build guide. Re-deriving any of these from the class,
    from "what a L1 <class> would have," or from the build guide's recommended column =
    the sheet was RECONSTRUCTED, not carried = .fail 9. If you do not have the prior save's
    exact values in front of you, RE-READ IT before writing — do not approximate.
    (Observed 2026-06-19, eRmaC Tactical Reach King: across three regenerations the DM
    mutated Giant Instinct→"Dragon Instinct", Versatile Human→"Half-Elf", CHA 12→14,
    DEX 10→12, dropped class_1b "Sudden Charge", and overwrote class_1 "Raging Intimidation"
    with "Moment of Clarity" then "Sentinel Dedication" — each save further from the gold
    copy in 4_Carousel.txt and the character-creation decision log. None of it was a real
    player choice; all of it was reconstruction. This lock exists to stop exactly that.)

companions[]
  v93.19 Phase A2: Pick-6 / Drop-1 cross-IP system.
  Player picks 5 of 6 cross-IP at character creation (typically drops class-duplicate
  of PC class). Manor 5 join in Prologue per alignment. Quest-Locked 7 join at quest triggers.
  Total possible companions in a playthrough: 5 (cross-IP Pick-5) + 1–5 (Manor, alignment-gated)
  + 7 (QL, quest-triggered) = up to 17. Default companions[] starts with the 5 cross-IP picks.
  Default Pick-5 cross-IP pool: Hu Tao, Keqing, Leliana, Yor Forger, Aerith.
  pick6_dropped — DEPRECATED 2026-05-22; fully retired 2026-06-05 (A6/Velvet removed). No drop slot.
  companions_not_picked[] — the 5 of 10 open-pool candidates the player did NOT choose.
  linzi_replacement — string|null. If Linzi (J) not picked, name of the companion who inherits her chronicler role. Null if Linzi IS picked.
  linzi_replacement_letter — A–K letter of the replacement pick.
  chronicler_active — boolean. True if Linzi present OR replacement nominated. Enables .book command.
  build_id       — from KM_Companions_Behaviors.md (NEW_001–NEW_005 for cross-IP)
  hp_max         — from build file at level 1
  status         — "active" | "incapacitated" | "dead" | "absent"
  location       — "party" | "reserve" | "seekers" | "absent"
  join_source    — "pick6" | "manor_alignment" | "quest_locked" | "seekers_flip"

five_seekers     — HARDCODED to Tartuccio's 5: Bellatrix Lestrange, Revy, Satsuki Kiryūin, Velvet Crowe, Atalanta Alter.
                   Player does NOT pick seekers; they flip via Diplomacy DC 10 in Ch1.
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
  "save_version": "1.9.4",
  "chapter_completed": "pre_prologue",
  "save_timestamp": "",
  "save_label": "",
  "turns_elapsed": 0,

  "dm_resume_note": {
    "instruction": "",
    "active_player_plans": [],
    "standing_intents": [],
    "player_position": "",
    "player_last_action": "",
    "player_intent": "",
    "room_state": {},
    "carousel_state": "",
    "open_threads": [],
    "level_up": "",
    "weapons": ""
  },

  "delegated_orders": [],

  "pending_questions": {},

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
      "class_1b": "",
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
      "location": "party",
      "join_source": "pick6"
    }
  ],

  "companions_selected": ["Hu Tao", "Keqing", "Leliana", "Yor Forger", "Aerith"],
  "companions_not_picked": ["Amiri", "Valerie", "Harrim", "Linzi", "Jaethal"],
  "linzi_replacement": null,
  "linzi_replacement_letter": null,
  "chronicler_active": true,
  "leliana_chronicler_mode": false,
  "linzi_primary_chronicler": true,
  "linzi_replacement_gate_fired": false,
  "leliana_ballad_cycle": [],
  "notebook_entries": [],
  "pick6_dropped": "DEPRECATED — use companions_not_picked instead",
  "manor_companions_joined": "DEPRECATED — Manor 5 now in open pool, see companions_selected",
  "quest_locked_joined": [],

  "five_seekers": {
    "seeker_1": "Bellatrix Lestrange",
    "seeker_2": "Revy",
    "seeker_3": "Satsuki Kiryūin",
    "seeker_4": "Velvet Crowe",
    "seeker_5": "Atalanta Alter"
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

  "companion_quests": {
    "Leliana": {
      "status": "inactive",
      "leliana_opus_named": false,
      "leliana_opus_name": "",
      "leliana_opus_performed": false,
      "leliana_illness_disclosed": false
    }
  },

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
    "prestige_upgrades": [],
    "pending_modifiers": []
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
    "malak_arrested_publicly": false,
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
    "biggs_crowd_hero": false,
    "wedge_crowd_hero": false,
    "directive_two_uncovered": false,
    "malak_fear_state": false,
    "malak_voice_mimicked": false,
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
    "tartuccio_evidence": [],
    "tartuccio_evidence_pressure": 0,
    "malak_coin_purse_assessed": false,
    "jail_detour_taken": false,
    "five_seekers_freed_by_player": false,
    "five_seekers_freed_by_jamandi": false,
    "five_seekers_released_late": false,
    "kesten_dispatched_to_jail": false,
    "drevic_released_on": "",
    "jamandi_pre_impression": "",
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
    "companion_dynamics": {},
    "companion_bonds": {},
    "weapons_in_garden": false,
    "promises": [],
    "dialogue_choices": [],
    "linzi_witnessed_gate": false,
    "leliana_witnessed_gate": false,
    "chronicler_introduced": false,
    "tutorial_pickpocket_resolved": "",
    "tutorial_thief_gender": "",
    "tutorial_thief_class": "",
    "thief_disposition": "",
    "thief_gear_taken": false,
    "crew_gear_taken": "none",
    "crew_resolved_status": "",
    "armorer_favor": false,
    "armorer_bonus_paid": 0,
    "squire_aldric_witnessed": false,
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
    "Leliana": [],
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
      "description": "Specific description of what fired, what file rule was violated, and what was re-rendered. Example: '.fail 9 — Jamandi described with dark braided hair. KM_NPCs.md states iron-gray jaw-length never braided. Re-rendered with correct description.' Empty array OK if zero fails this session.",
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
    "response_length": "medium",
    "min_paragraphs": 4,
    "max_paragraphs": 6,
    "npc_dialogue_beats_min": 6,
    "tts_mode": true
  }
}
```

⛔ [SAVE_TEMPLATE_END: KMSBT-1.9.4 · skeleton ends at game_options → closing brace] — this is the FOOT of the JSON skeleton. Echo it in your proof header (NOT inside the JSON), copied from HERE. Reproducing it proves you read the skeleton all the way DOWN. The top `[SAVE_TEMPLATE_LOADED]` token alone only proves you opened the file's header — THIS token proves you actually traversed the skeleton you were told to copy (STEP 2). If you can produce the top token but not this one, you read lines 1–130 and built the JSON from memory or the prior save = pattern-matching = LAZY SAVE = `.fail 9`.

---

## FIELD SEMANTICS — `notebook_entries` (Linzi's Chronicle — the FROZEN factual record)

`notebook_entries` is the canonical, persisted record of what actually happened —
the thing `.book` displays and the "Previously on" recap reads from. It exists
because the chronicle was previously SYNTHESIZED fresh each time from `story_flags`,
which let the DM dramatize/invent events ("cleared the hall with one word," "sang to
hundreds," a "merchant contact" that never happened). A frozen record cannot drift.

Array of append-only objects — **ONE PER SCENE** (she details EVERY scene; do not skip
any), LOCKED when the scene happens. Each entry carries BOTH a neutral fact anchor AND
Linzi's frozen prose passage:
```
{ "turn": <int>, "chapter": "prologue", "beat": "<scene_id or short tag>",
  "fact":  "<plain, literal, NEUTRAL-VOICE statement of what occurred — no styling, no
             inflation; the minimum true sentence(s) a witness would write. THE RECAP
             READS THIS, so it must stay factual.>",
  "prose": "<Linzi's first-person chronicle passage for this scene — her storytelling
             voice, retrospective and a little legendary, her opinions, asides, the
             small details she noticed, ~1 short paragraph. Written ONCE and FROZEN.
             THE .book COMMAND READS THIS. It may dramatize the FEEL but may NOT add any
             event not present in `fact`.>" }
```
Example: `{ "turn": 47, "chapter": "prologue", "beat": "feast_ambush",
  "fact": "eRmaC issued the ARM coordination word; guests dropped to the floor per the Lady-Sleeps gambit; 5 assassins taken into custody; Ezvanki administered the cure; no guests died.",
  "prose": "He said one word — the word we had agreed on — and the whole hall went to the floor as if they'd practiced it. I was near the door. I remember thinking the assassins would find nothing upright to cut, and they didn't. Five taken, none of ours lost, the cure passed hand to hand after. I wrote 'luck' in the margin the first time. I have since crossed it out. — L." }`

⛔ **AUTO-FILL = APPEND ONE ENTRY PER SCENE.** "Notebook Auto-Fill active" is not flavor —
at each scene the DM APPENDS one entry (both `fact` AND `prose`), the turn it happens. A
scene that occurs but is never recorded = the chronicle is INCOMPLETE (and the recap will
drift). `fact` keeps the recap honest; `prose` IS the readable book — her incomplete
work-in-progress that the player reads via `.book`.

⛔ **CHAPTER TITLES ARE FROZEN.** Each entry MAY carry an optional `chapter_title` —
Linzi's own evocative name for the chapter that entry belongs to (e.g. "The Night
Someone Used a Napkin as a Weapon"). Set it ONCE, when she first names the chapter
(do not regenerate it per view, or the `.book` Table of Contents drifts). All entries
in a chapter share that chapter's title. The `.book` TOC (KM_Commands.md) reads these
frozen titles. `leliana_ballad_cycle` entries carry `chapter_title` identically (her
`.score` TOC reads them) — same field, same freeze rule.
⛔ **APPEND-ONLY / FROZEN.** Never rewrite or "improve" a prior entry; only append.
Entries are LITERAL FACT, NEUTRAL voice — Linzi's epic chronicle voice is applied ONLY
at `.book` display time (KM_Commands.md), styling these facts, never inventing beyond
them. ⛔ **MONOTONIC / CARRY-FORWARD** (per CONTINUITY CHECK): the array only grows;
a save with fewer entries than the prior = gutted record = `.fail 9`.
⛔ The recap and `.book` READ this; they do not re-derive events from flags. An event
in the recap/`.book` that is not traceable to a `notebook_entries.fact` (or another
structured record) = fabrication = `.fail 9`.

---

## FIELD SEMANTICS — `leliana_ballad_cycle`

`leliana_ballad_cycle` is Leliana's parallel to Linzi's `notebook_entries`. Her chronicle is a
**COMBINATION** of two things per scene, both stored and FROZEN: a **diary entry** (clear
prose — the readable record) AND a **song she composed, inspired by that scene** (her
medium). The diary keeps the chronicle LEGIBLE; the song is the art. (All-song would be too
cryptic to work as a record — the diary is what makes it a usable account, like Linzi's
prose; the song rides alongside it.) Array of append-only objects, **one per scene Leliana
witnessed**, LOCKED when the scene happens:
```
{ "n": <int>, "turn": <int>, "chapter": "prologue", "beat": "<scene_id or tag>",
  "title": "<the SONG's oblique title — 'Eleven Napkins', not 'The Feast'>",
  "fact":  "<plain NEUTRAL-VOICE statement of what occurred — anti-drift anchor; when Leliana
             is the active chronicler (leliana_chronicler_mode) THE RECAP READS THIS>",
  "diary": "<Leliana's DIARY-style prose account of the scene — clear, first-person, readable,
             ~1 short paragraph: what happened and what she noticed/felt. Her parallel to
             Linzi's prose; this is what keeps the book legible. Written ONCE, frozen.
             `.score` shows this. Must not add events not in `fact`.>",
  "ballad": "<the SONG she composed inspired by the scene — sung LYRICS (the WORDS she sings),
              NOT a prose description of the melody/instrumentation; and it RHYMES, written AS A
              SONG: labelled [sections], stage directions in (parens), AABB rhyme + a repeating
              rhyming chorus, per KM_Leliana_Ballads.md. SCALE TO THE BEAT — a short rhyming song
              for a minor scene, the FULL ENSEMBLE ANTHEM for a major/ceremonial beat. Written
              ONCE, frozen. `.score` shows this beneath the diary. Must not add events not in
              `fact`/`diary`. A non-rhyming / free-verse ballad = wrong medium = `.fail 9`.>" }
```
Example: `{ "n": 1, "turn": 47, "chapter": "prologue", "beat": "feast_ambush",
  "title": "One Word, and the Floor Rose to Meet Them",
  "fact": "eRmaC issued the ARM coordination word; guests dropped to the floor per the Lady-Sleeps gambit; 5 assassins taken; Ezvanki's cure passed through the hall; no guests died.",
  "diary": "Tonight he said one word — the word they'd agreed — and the whole hall went to the floor like a held breath. I stayed near the door and watched the knives find no one standing. Five taken, the cure passed cup to cup, and not one guest lost. I keep wanting to write 'luck.' It wasn't.",
  "ballad": "[Intro] (a low held lute line — the hush of a room that nearly broke) [Verse] He spoke one word; the bright hall dropped as one, / and every blade went hunting, and found none. / Five wrists in iron, every cup still full — / the night they came to empty made it whole. [Refrain] So sing it low, and let the long table tell: / the word was given, and not one guest there fell." }`

⛔ **AUTO-FILL = APPEND ONE ENTRY PER SCENE** (the turn it happens) — and each entry carries
BOTH the `diary` AND the `ballad` (plus `fact`). Append-only, never revised. MONOTONIC under
CONTINUITY CHECK (only grows). `fact` keeps the recap honest; the `diary` is the clear
readable record and the `ballad` is the song that rides with it. Inactive this playthrough if
Leliana is not in `companions_selected` — the system activates when she joins a party.

---

## FIELD SEMANTICS — `companion_titles`

Per-companion sub-object. Only populated keys appear; absent fields = not granted.

```
"companion_titles": {
  "Linzi": {
    "prefix":            "Cantrix",
    "prefix_reaction":   5,
    "prefix_passive":    "Echo Loop",
    "suffix":            "the Legend Weaver",
    "suffix_reaction":   3,
    "suffix_item":       "Endless Lute",
    "suffix_item_power": "full"
  }
}
```

**Field meanings:**
- `prefix` / `suffix`: the title string the player spoke
- `prefix_reaction` / `suffix_reaction`: integer −5..+5, DM fit score per component
- `prefix_passive`: passive name; active iff `prefix_reaction >= +1`
- `suffix_item`: item name; materialized iff `suffix_reaction >= −2`
- `suffix_item_power`: `"full" | "75" | "50" | "25" | "refused"` — scales off `suffix_reaction`

**"Both" grants record TWO scores, not one.** `prefix_reaction` and `suffix_reaction` are independent. The Prefix names the function (scales the passive); the Suffix names the instrument (scales the item). Collapsing them into a single field, or writing only one reaction score for a Both grant = `.fail 9` (fabricated math) + `.fail 15` (mandatory output block malformed). See KM_Companions_Titles.md § MANDATORY OUTPUT BLOCK.

**`.retract` partial scope:** `.retract <name> prefix` clears `prefix`, `prefix_reaction`, `prefix_passive` only — `suffix*` fields and the materialized item persist at their own power tier. Same for `.retract <name> suffix` in reverse. Per-component scoring is what makes partial retract work; without it, the surviving component has no score to scale off.

---

## FIELD SEMANTICS — `turns_elapsed` (v1.9)

**Definition:** Integer count of player input turns since session start. Increments by 1 each time the player submits any input — in-character dialogue, action, or out-of-character command (.save, .opt, .check, etc.). Save block output itself does NOT increment the counter (the save is the response to a turn, not a turn itself).

**Where the count starts:**
- Brand new run (NO save block provided): counter starts at 0 BEFORE the first player input. The first player turn brings it to 1.
- Resumed run (save block provided): counter resumes from the saved value. Continues incrementing from there.

**What counts as a turn:**
- Any single player message, regardless of type or length
- Single in-character action: `I draw my sword` → +1
- Multi-action turn: `I draw, advance, and attack the goblin` → +1 (one player message = one turn)
- OOC command: `.opt length long` → +1
- Empty / "ok" / `.continue` after a save offer → +1
- Combat round: one player input per round = +1 per round

**What does NOT count:**
- DM responses (DM-only output never increments)
- Auto-save offers (the offer itself is not a turn)
- Save block output (system response, not a turn)
- Scene transitions that don't require player input

**Display in resume header:**
On every save block load, the DM's "Previously on Kingmaker…" recap MUST include a line:
`Session run length: <turns_elapsed> turns played.`

This gives the player a recovery anchor — they can see at a glance how deep the save is.

**Header tracking during play:**
The state header on every response includes the current turn count:
`[Turn N | <other state lines>]`

This gives the player a live counter they can use to call `.savenow` at meaningful intervals (e.g., "save every 10 turns").

**Resume validation:**
On load, DM checks: does the recap make sense for `turns_elapsed`? A Pre-Prologue save claiming 200 turns elapsed is suspicious; a Ch3 save claiming 8 turns is suspicious. Discrepancy ≥ obvious threshold = DM should ask player to confirm before continuing.

**Auto-save offer trigger:**
The DM may use `turns_elapsed` to fire turn-counter save offers (see KM_DMRules.md § AUTO-SAVE CADENCE if/when configured). Counter does NOT auto-reset on save — it's a session-lifetime counter.

---
*v1.9.4 (2026-06-03): Added `notebook_entries[]` root key (position 19, after
`leliana_ballad_cycle`) — Linzi's chronicle as a FROZEN, append-only FACTUAL record
locked at each beat, replacing the old synthesize-from-flags-every-time approach that
let the recap/`.book` dramatize and invent past events. The "Previously on" recap and
`.book` now READ from it (KM_ClaudeInstructions § RECAP CONSTRUCTION rule 0–1;
KM_Commands § What She Draws From); Linzi's legend voice is display-only styling over
these facts, never a source of new events. Append-only + monotonic under CONTINUITY
CHECK. Also enriched `leliana_ballad_cycle` to the parallel frozen shape (Leliana's medium
is the BALLAD — `{n, turn, chapter, beat, title, fact, ballad}`; `.score` reads the frozen
`ballad` verse, recap reads `fact` when she is the active chronicler; retired the old
synthesize-from-flags `.score`). Root keys 62 → 63. save_version 1.9.3 → 1.9.4.*

*v1.9.3 (2026-06-03): ROBUSTNESS / SELF-CONSISTENCY PASS. Reconciled the root-key
accounting — the prose "53 keys" list (ANTI-FABRICATION GATE) and the "59 keys"
verification line were both stale and disagreed with the actual JSON. True count is
now stated as 62 everywhere, with the JSON template declared the single authoritative
key source. Removed root `overflow` (collision with `pending_overflow` — the template
previously told the DM to delete a field it still shipped). Bumped save_version literal
to "1.9.3" (was stuck at "1.9" while the file already claimed 1.9.2). Made the
save_version match rule forward-tolerant (loading an older save migrates forward and
NEVER invalidates it). Strengthened STEP 5 audit from "≥30" to "exactly 62". Added the
CONTINUITY CHECK block: logs are monotonic (a new save with fewer log entries than the
prior = lazy save = .fail 9), counters only increase, and a manifest of carry-forward
fields that must never silently reset. No new gameplay fields; this pass only hardens
enforcement of the existing shape.*

*v1.9.2 (2026-05-31): Added `pending_questions{}` root key — group-talk question tracking.
Key = companion name; value: { question_summary, asked_turn, grace_turns (default 2),
penalty_active }. +1 feast_approval if answered within grace; −1/turn per open question
past grace. Cleared on answer or scene end. Full spec: KM_DMRules_C.md § QUESTION
ACKNOWLEDGMENT; behavior mandate: KM_ClaudeInstructions.md § QUESTION ACKNOWLEDGMENT.
Root keys 58 → 59.*

*v1.9.1 (2026-05-30): Added `delegated_orders[]` root key — the delegate-and-report-back
tracker. Each entry: { who, what, given_turn, eta_turns (int or "unknown"), status
(in_progress|complete|blocked), result }. DM estimates eta on delegation, ticks −1/turn,
surfaces active orders in OPEN THREADS, fires the NPC return-and-report beat at eta 0.
Player views via `.tasks`. Full rule: KM_DMRules.md § DELEGATED ORDERS; behavior mandate:
KM_ClaudeInstructions.md § DELEGATED ORDERS. Root keys 57 → 58.*

*v1.9.2 (2026-05-31): Added optional `roll` field to each `delegated_orders[]` entry — the
delegated-action resolution string (e.g. "d20[12]+6=18 vs DC17 → Success", or
"auto-success" / "n/a — out of domain"). Set when the order resolves (Step 3.5) so a reload
reproduces the same outcome instead of re-rolling. Uncertain orders roll d20 + NPC
competence mod vs task DC (four degrees, roll block shown); in-wheelhouse uncontested =
auto-success, out-of-domain = auto-fail/wrong-agent (no roll). Full rule: KM_DMRules.md
§ DELEGATED ORDERS STEP 3.5; mandate: KM_ClaudeInstructions.md § DELEGATED ORDERS. No root
key count change (field added to existing object).*

*KM_SaveBlock_Template.md — Kingmaker PF2e | Save Block v1.9*
*v1.9 (2026-05-23): Added `turns_elapsed` (integer) at root, position 5 (after save_label,
before dm_resume_note). Tracks total player input turns since session start across resumes.
Top-level keys 52 → 53. save_version 1.8 → 1.9. Resume recap MUST display turn count;
in-play state header includes [Turn N] anchor.*
*v1.8 (v93.19 Phase A2 — 2026-05-19): Roster v2 — Pick-6 / Drop-1 cross-IP system.
Added pick6_dropped (string A1–A6), manor_companions_joined[] (alignment-gated
Prologue joins), quest_locked_joined[] (Ch1+ canonical quest joins). companions[]
gains join_source field. Default companions_selected unchanged at 5 names;
pick6_dropped retired 2026-06-05 (A6/Velvet removed — Pick-5 open pool, all five cross-IP join).
Top-level keys 49 → 52. save_version 1.7 → 1.8.*
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
