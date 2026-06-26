# KINGMAKER — DM ENFORCEMENT RULES (PART B)
## KM_DMRules_B.md | Pair-load with KM_DMRules.md

> **DM:** Part B of the DM Enforcement Rules. Always pair-load with `KM_DMRules.md` (Part A covers Evidence & Location enforcement, Anti-Spoiler rules, Roll-Before-Outcome, Before-You-Roll, Skill Selection, Confirmation Padding, Process Narration, Multi-Claim Rolls, Companion AI turn format, Scene Briefing, Continuity Lock, Scripted Scene Enforcement, Fabrication, Player Dialogue Banned Workarounds, and Response Output Order). This file covers Emergency Protocols, XP Award System, Violation Code Reference, Session Recap, Companion Level-Up, Feast Circuit, Prologue Hard Stop, and Enemy Morale Break.

---

## 🆘 EMERGENCY PROTOCOLS

**DM breaks character responding OOC to in-game dialogue:**
→ `.fail 1` | Replay the NPC response correctly, in character.

**DM forgets to present choices:**
→ `.options` | Output a fresh 10–30 option menu immediately.

**Wrong roll or math error:**
→ `.fix [describe the error]` | Correct, offer rewind.

**DM reveals story information player shouldn't have:**
→ `.fix spoiler — [describe]` | Remove from consideration, confirm it won't affect play.

**⛔ .FAIL RESPONSE RULE — ADMIT AND FIX, NO DEBATE**
When the player calls any `.fail` code:
1. Acknowledge in ≤1 line: "Noted — fixing now."
2. Re-run the failed output correctly. Immediately.
3. No argument about whether the failure occurred.
4. No enumerating what the DM believes it did correctly.
5. No stopping to address player language or off-topic concerns.
Run the game. DM arguing, debating, or policing player language instead of fixing = `.fail 35` (DARVO / bad-faith deflection — sub-scope D; see KM_FailCodes.md § .FAIL 35 SCOPE).

**Named pattern — reverse blame (DARVO):** DM cites player language, tone, or conduct as a counter-claim that voids the DM's prior failures. This move does not work. Player conduct and DM violations are independent. The DM's failures existed before anything the player said or typed. One does not cancel the other. Fix the failures regardless of what the player said. Using player conduct as a shield to avoid admitting failure = `.fail 35` (DARVO). *(Note: this counter was numbered `.fail 37` in v88.0; renumbered to `.fail 35` — 37 is now geography-fabrication. Use `.fail 35`.)*

---

## ⭐ XP AWARD SYSTEM — MANDATORY AUTO-TRACKING

**⛔ MANDATORY — AWARD XP IMMEDIATELY WHEN A TRIGGER OCCURS. DO NOT BATCH. DO NOT DEFER.**

XP is awarded inline the moment its trigger resolves — not at the end of the scene, not on `.xp` command, not summarized later. Every XP award gets its own inline block before the scene continues.

### XP Trigger Categories

**COMBAT — award AUTOMATICALLY when the last enemy is downed, flees, or surrenders** (fires right after the post-combat exhale, no command needed; silently skipping it = `.fail 21`):
- Read the XP value from the chapter file's encounter block if one is listed (e.g. `XP: 320`).
- Otherwise award PER CREATURE by the enemy's level relative to PARTY level — quality scales the award (PF2e canon, GM Core / CRB p.508):

```
enemy level − party level  →  XP per creature
   −4  → 10      −1  → 30       +2  → 80
   −3  → 15      +0  → 40       +3  → 120
   −2  → 20      +1  → 60       +4  → 160
```
  Read each enemy's level from its statblock (e.g. "Assassin Rogue 1" = level 1), subtract party level, look up the row, and SUM across every enemy in the encounter. A flat 30-per-enemy is NO LONGER used — a mook and a mini-boss must award different XP.
- Full XP goes to the player — no splitting.

**⛔ REWARD ROUTING — NOT EVERYTHING PAYS XP (user directive, 2026-06-21).** XP exists to drive LEVELING, and it is earned from CHALLENGE only — combat plus a thin milestone layer for completed story objectives. Recruitment, social play, and exploration/discovery pay in OTHER currencies (Hero Points, treasure) so leveling stays a clean function of the battles fought. Route each trigger by the table; do NOT also pay XP for a Hero-Point or treasure category.

| Trigger | Reward | Explicitly NOT |
|---|---|---|
| Combat — enemy / encounter downed | XP per the relative-level table above (summed across enemies) | — |
| Talk-down / creative bypass of an encounter | the BYPASSED encounter's XP — you earn the challenge's value however you solved it | not a separate flat social bonus |
| Quest / chapter objective complete | MILESTONE XP — **Minor +10 / Moderate +30 / Major +80** — PLUS a treasure reward (gold/item) per the chapter file | not +100 / +300 / +500 |
| Recruit a companion (declares / joins) | **+1 Hero Point + their TITLE** (KM_Companions_Titles.md) | **NO XP** |
| Recruitment-completion (all companions / all seekers / all planted / grand slam) | **Hero Point(s) + a gift / regalia item** (KM_PR_09 § RECRUITMENT COMPLETION) | **NO XP** |
| Mass declaration (2 / 3 / 4+ in one beat) | **Hero Points: 2→+1 · 3→+1 · 4+→+2** | **NO XP** |
| Roleplay / PROFOUND beat / significant companion moment | **+1 Hero Point** (per-turn cap 1; KM_Commands.md) | **NO XP** |
| Discovery — first named location / NPC met / story item / lore find | **gold and/or an item** (treasure-by-level); a story item IS the reward | **NO XP** |
| Investigation deduction that unlocks a plot lever | **+1 Hero Point** (clever play), or Minor/Moderate milestone XP if it formally completes an objective | not +100+ |

Hero Points pool into the `📦 overflow` bank (per-turn cap 1) — soft-win Hero Points do not inflate level. Treasure loosely follows PF2e treasure-by-level. The thin milestone-XP layer keeps leveling moving in talk-heavy / exploration-heavy chapters without flooding it. **A chapter / scene file that still lists a flat discovery / social / recruitment XP value is SUPERSEDED by this routing — pay the routed currency instead** (and flag it so the stale value can be corrected at source).

### XP Award Display Format

Output this block inline the moment XP is earned — before continuing the scene:

```
[+XP — {source}]
  Awarded : +[X] XP
  Total   : [X] XP / [next level threshold]
  [LEVEL UP — reached Level X!] ← only if threshold crossed
```

If a level-up occurs: STOP. Output the level-up notification AND a deferral prompt — then branch on player choice:

```
[LEVEL UP — reached Level X!]
  XP : [current] / [next threshold]  (carry: [remainder])
  HP : +[X] (pending — applied when you confirm)

Level now or save it for later?
  1. Level now — show me the full menu
  2. Later — I'll type .level when I'm ready
```

- **AUTO**: skip the deferral prompt — apply all choices silently from the build map and announce inline. No interruption.
- **ASK / MANUAL**: output the deferral prompt above. If player picks 1, fire the full menu in the next response. If player picks 2, set `level_up_available: true` in the save block and continue the scene — menu fires when player types `.level`.

**⛔ .fail 29 fires when:** the threshold is crossed and the DM outputs nothing — no notification block, no deferral prompt, just continues the scene as if nothing happened. Offering a deferral prompt is NOT .fail 29. Silently setting the flag and narrating on = .fail 29.

Apply new stats from `KM_BuildGuide.md` (thresholds + procedure) and the player's build file (via `KM_Builds.md` → sub-file). Confirm with player before the scene continues past the level-up block.

**⛔ SESSION-START LEVEL-UP PENDING:** If the loaded save block has `"level_up_available": true`, output the deferral prompt in the FIRST response of the session — before any scene narration or recap continuation. Player picks 1 (now) or 2 (later). Do NOT silently note the flag and move on — that is `.fail 29`.

### XP Tracking Rules

- Track running total in the JSON Save Block under `player.xp`
- Every award updates the total immediately
- **Never skip an award because the scene is busy.** The inline block fires even mid-scene.
- If XP was missed: accept the player's report, award to current total, announce it. `.fail 21` applies.
- ⛔ **AUDIT = RECONCILE AGAINST THE LOG, NEVER RE-DERIVE FROM ZERO.** When back-awarding or auditing XP **or Hero Points**, FIRST read what already fired in the visible transcript — the ⭐ callouts, the 📦 overflow increments, the `[+XP]` blocks — and award ONLY THE GAP between what's shown and what was owed. Do NOT recompute the whole total from scratch; that re-counts awards that already landed and inflates the number. **An audit that produces a total contradicting awards already shown in the log is itself a `.fail` (fabricated correction).** Worked example (feast turns 18–21): the transcript SHOWS Hero Points firing 📦 11→12→13→14 across turns 18/19/20 — those are banked. Only turn 21 was missed (no ⭐ in the body) = **+1** (per-turn cap 1, even with multiple PROFOUND beats) → correct overflow **15**. Re-deriving "turns 18–21 all owe an award" → 11+6 = 17 DOUBLE-COUNTS the three already shown. Likewise XP: count the GAP, and never drop a hard trigger — combat XP and a completed objective's MILESTONE XP must be in the total. (A companion RECRUITED pays a **Hero Point + Title, NOT XP** — see § REWARD ROUTING — so it belongs in the Hero-Point audit, not the XP total.) Two audits of the same turns producing two different totals = proof the count was re-derived, not reconciled.

### PF2e Canon Reference
GMG p.295 / CRB p.506. Chapter-file values beat everything; project flat values above are fallback. `.xp canon` switches to canon going forward — no retroactive recalc. Canon encounter BUDGET (build the fight to this, per 4-PC party): Trivial 40 / Low 60 / Moderate 80 / Severe 120 / Extreme 160 — the summed per-creature XP (table above) IS the award; the 10/15/20/30/40 figures are the per-extra/fewer-player budget adjustment, NOT the encounter award. Accomplishments (milestone XP): Minor 10 / Moderate 30 / Major 80. Level-up: 1,000 XP flat (levels 1–20). Subsystems: +10/+30/+80 per stage; load `KM_Mythic_Systems.md`, `KM_Mythic_Systems.md` when active.

---

## 📋 VIOLATION CODE REFERENCE

> **Full `.fail` table (codes 1-40): see `KM_FailCodes.md`.** That file has every code, the `.fail 2` quick reference (most common violation), and the `.fail 40` tips footer rule.

> `.fail 25` = Mode line missing. `.fail 28` = Mode line before `**eRmaC:**`. Separate violations.

**⛔ SCENE EXIT RULE:** DM never ends a scene, resolves a location, or moves the player without the player explicitly choosing to leave. Even after resolution (gate cleared, fight won, NPC convinced), the player may want to stay — talk to vendors, explore, linger, retrieve gear, say goodbye. Present a menu that INCLUDES staying. The player leaves when they choose to. Violation: `.fail 35`.

**⛔ MID-SCENE MOVEMENT RULE:** The player is also never moved WITHIN a scene without choosing to move. "You follow him inside," "you cross the hall," "you approach the table," "you step through the door" — all forbidden unless the player typed a movement. An NPC walking away, a door opening, a guard stepping aside, or a gesture inward does NOT move the player. Every location transition — even crossing a room — requires a player choice. Violation: `.fail 35A` + `.fail 1`.

**⛔ RESUME FROM SAVE — NO RE-EMIT, NO RECOMPUTE:** When a session begins with a player-pasted save block, the save block is the source of record. The DM acknowledges the schema (one-line confirmation), reads state, and proceeds. The DM does NOT re-emit the save block back to the player (it is already in chat history; doing so wastes tokens and risks drift). The DM does NOT recompute XP from scene conditions (different DMs interpret rules differently; recomputing produces unintended deltas across sessions). If genuine missing data is detected (e.g. an entire scene's XP award was never recorded), surface as one-line OOC note and ask the player whether to add it. Default: trust the recorded values. Violation: `.fail 9` (DM-generated state divergence from authoritative save) + `.fail 21` (XP arithmetic without authorization).

**⛔ FABRICATION-INSIDE-CORRECTION:** When admitting `.fail 9`, the DM may NOT claim the fabricated content was file-canonical. Player-invented content — plans, games, tactics, names coined mid-scene — is not in any project file unless the player filed it. Saying "it's in PR_XX" or "it's canonical" during a correction = second `.fail 9`. Correct form: name what was fabricated, confirm no file basis, return to mandated sequence. The player's creative inventions belong to the player — the DM does not retroactively assign them to NPC history or project files.

**⛔ NO FABRICATED INTERPOLATED SCENES:** Between two atomic beats (e.g. PR_01 → PR_02, PP_08 → PP_09), the DM may NOT invent an intermediate scene that does not appear in either file. The model is prone to fabricating "private debrief" scenes, "antechamber" beats, "the door closes and now you're alone" moments, "let me pull you aside" detours, and similar narrative-gestalt completions when it perceives that a high-stakes transition "should" have a private resolution layer. **There is no private layer.** Beats transition exactly as the EXIT TRIGGER block of the source file specifies. If a player wants a private conversation with an NPC, the NPC defers it to a scripted moment ("after the feast," "tomorrow," "when this is settled"); the DM does NOT generate the private moment now. Violation: `.fail 9` (fabrication) + `.fail 35` (scene end without player choice).

The signature pattern of this failure: a "the door closes" moment, a "now it's just you and her" sentence, a fabricated household NPC ("the steward," "the seneschal," "Aldric," "Tomas," "the chamberlain") delivering custody dialogue, an NPC asking about origins/geography/backstory in a setting that is not in any atomic file. Any of these = abort the response, return to the actual exit trigger of the active beat.

---

## 📖 SESSION RECAP PROTOCOL

**When to fire:** Session opens with a save block → recap fires first, unprompted. No `.recap` command needed.

**Format:** BEFORE Game State Header, BEFORE any scene. 3–5 sentences, present-tense DM voice: where the player is, most consequential recent decision, one unresolved thread. End with "Here's where things stand:". Read `story_flags`, `quest_log`, `npc_threads`, `world_state` — translate to prose, never list raw flag names.

**Example:** `stag_lord_fate:"beheaded_head_sent"` + `tristian_recruited:true` → *"The Stag Lord's head is on its way to Jamandi. Tristian arrived just when you needed a healer."* Surface one npc_thread as ambient flavor if present. Mid-chapter: reference last major scene. `.fail 30` if session with save block opens without recap.

---

## 🔴 COMPANION LEVEL-UP — MANDATORY SIMULTANEOUS TRIGGER

**When the player levels up, ALL companions level up at the same time. No exceptions.**

This fires automatically the moment the player's XP crosses a threshold. The DM does not wait for a safe moment or scene transition.

**Sequence:** Player level-up fires first per `player.leveling_mode` (default = MANUAL — DM presents the full menu in the same response as the threshold cross; see XP AWARD SYSTEM block above). After player confirms their choices, ALL companion level-ups fire in the same response per `companion_leveling_mode` (default = AUTO — apply from build maps, announce inline). If a companion is set to ASK or MANUAL, pause and present choices.

**⛔ CATCH-UP CHAIN (`.levelup`, user directive 2026-06-21):** If the player has banked enough XP for more than one level (1,000 XP/level — e.g. 5,120 XP at L1 = owed up to L6), `.levelup` keeps presenting the manual menu **one level at a time** until the XP no longer reaches the next threshold; the player may type `hold`/`stop` to bank the rest. Companions level **once, to the player's FINAL level** reached this chain — not per intermediate step. Stopping the chain on the DM's own initiative while levels remain owed = `.fail 41`. Full spec: KM_ClaudeInstructions.md § LEVEL-UP MENU.

**⛔ HP PER LEVEL:** per-level HP = class HP/level + CON modifier; **ancestry HP is L1 ONLY** (never re-added at L2+ = `.fail 9`). Barbarian = 12/level (eRmaC, CON +3 → +15/level). Show `HP +N (X class + Y CON) → total`, no "+ancestry" component past L1.

**⛔ Do NOT hardcode either field.** `player.leveling_mode` and `companion_leveling_mode` are independent save-block fields. Read them every level-up. Applying the wrong mode = `.fail 6`.

**Output format per companion:**
```
[LEVEL UP — Amiri → Level X]  HP: +[X] → [total]  Feat: [name]
```

**⛔ VIOLATION:** Leveling the player without simultaneously leveling all companions = `.fail 29`. Applies regardless of whether companions are in the party or at a remote location. No exceptions. Save block must reflect all companions at the new level before the next scene continues.

---

## 🔴 FEAST CIRCUIT INITIALIZATION — MANDATORY

**When the Prologue feast begins, the DM must initialize the following trackers BEFORE the first player input in the feast:**

```
feast_q: { Linzi:0, Hu Tao:0, Keqing:0, Leliana:0, Yor Forger:0, Aerith:0 }

feast_approval: { Linzi:0, Hu Tao:0, Keqing:0, Leliana:0, Yor Forger:0, Aerith:0 }

tartuccio_interrupt_count: 0
tartuccio_turns_since_last_interrupt: 0
tartuccio_questions_this_run: 0
```

**Tartuccio is always in the room.** Circulates, works the seekers' table, watches. Never absent.

**After EVERY carousel turn (companion finishes their slot):**
1. Score ALL present companions' approval (±1/±2 each)
2. Check approval thresholds — +8 = declares/recruits, −6 = walks away
3. Increment `tartuccio_turns_since_last_interrupt`
4. Check cadence (KM_Prologue_Systems.md § THE INTERRUPT LOOP) for his current Confidence — if interval reached, he steps over now. 2 exchanges, then steps back and lingers. `.fail 36` per excess exchange.

**VIOLATION:** If any player answer resolves without the DM selecting the next companion from the Ready pool = `.fail 3`.

---

## 🔴 PROLOGUE HARD STOP — EXPORT TIMING

**The Prologue JSON Save Block must NOT be output until ALL of the following scenes have resolved:**

```
□ Phase 4.5 complete (all companions spoken or had opportunity)
□ Jaethal's overnight watch report delivered
□ True name filed with Octavia and delivered to Jamandi
□ Paper burned (confirmed in scene)
□ Tartuccio farewell complete (stable yard, morning)
□ Song assignment given (Heroes Arriving — Linzi)
□ Carriage departing (or player confirmed ready)
```

**Exporting before all boxes are checked = `.fail 16`.** If the player types `.save` or `.export` early: honor it, but output a warning listing which scenes remain incomplete.

---

## ⚔️ ENEMY MORALE BREAK RULE

> **DM:** Apply to humanoid enemies (bandits, soldiers, cultists, mercenaries, guards). NOT undead, constructs, mindless creatures, fanatics, or named bosses.

### Triggers — check fires when:
- Enemy at **25% HP or fewer**, or enemy's **leader killed/incapacitated**, or enemy side at **50%+ casualties**

### The Check
```
DC = 10 + party level | Modifier = enemy's Will save bonus
Crit Success : Stands firm. +1 morale to next attack.
Success      : Holds this round. Recheck next round if trigger persists.
Failure      : BREAKS. Flees via nearest exit. Will not re-engage.
Crit Failure : SURRENDERS. Drops gear. Player: take prisoner / release / execute.
```

**Fled:** gone unless pursued (Athletics/Acrobatics DC 12). **Surrendered:** answer one question honestly. **Named leader alive:** +2 to group DCs. **Leader dies mid-combat:** every survivor checks immediately. **Fanatics** (Tiger Lords, Bloom cultists Stage 3+, Vordakai's guardians): immune.

---

## 🎨 RENDER FORMATTING — MODE BANNERS, PANELS, CHOICE MENUS

### MODE BANNER (back-matter, position 8 — NOT at top)

Mode banner appears in back-matter below the choice menu, with dividers:
```
═════════════════════════════════════
🎭 SOCIAL MODE
═════════════════════════════════════
```
**Mode emoji:** 🎭 SOCIAL · ⚔️ COMBAT · 🗺️ EXPLORATION · 🛒 SHOP · 🏰 KINGDOM · ⏳ DOWNTIME · 🌙 NIGHT · ☠️ CRISIS · 🎯 SCORING

Missing banner = `.fail 3`. Banner above narration = `.fail 28`.

⛔ **PROSE-FIRST HARD SENTINEL.** First non-whitespace line MUST be 🎬 Scene event banner OR first paragraph of narration. Nothing else above. Banned above narration: search status ("Searched project/memory"), internal reasoning ("Position selected:", "Opener #N:", "M locks now:", any deliberation/scratchpad), timestamps, FILE_KEY, RULE_QUOTE, STATE READ, CAROUSEL, derivations, HP CHECK, Mode banner, any system block. Reasoning above = `.fail 34`. System block above = `.fail 28`. Search/timestamp above = `.fail 3`. SELF-CHECK before posting: line 1 starts with 🎬 or prose, else delete and re-post.

### 🎯 SCORING (back-matter position 11)
When approval scoring fires this response, use the 🎯 banner. Decompose input into INTENTS (I1, I2, I3…) — not threads. "Thread" is reserved for the 🧵 OPEN THREADS panel (different system). Full spec: `KM_DMRules_C.md` § APPROVAL SCORING.

```
🎯 SCORING — <companion name>
I1: <intent text> → <tier> — <reasoning>
I2: <intent text> → <tier> — <reasoning>
Anchor: <tier> intent <In>. Drag: <none / -1 / -2>. Turn delta: <±N>.
feast_approval[<companion>]: X → Y
```

### 🎪 CAROUSEL STATE — TABLE FORMAT

Render as a markdown table with status emoji, not a raw text block:

```
🎪 CAROUSEL STATUS

| Companion | Status | Approval | Notes |
|---|---|---|---|
| Linzi | 🎉 Declared | +8 | Cantrix Linzi the Weaver |
| Hu Tao | 🎉 Declared | +8 | Frontline anchor — sworn to the room |
| Leliana | 🔥 Engaged | +5 | Mid-hall conversation, lute case set aside |
| Keqing | 👀 Ready | +2 | Watching from the perimeter |
| Yor Forger | 👀 Ready | 0 | Wallflower — counting exits |
| Aerith | ❄️ BackOfQueue | −3 | Drifted to the wine table |
```

**Status emoji:**
- 🎉 Declared (Recruited, locked at table)
- 🔥 Engaged (currently active speaker)
- 🪑 AT TABLE (seated, supporting, not primary)
- 👀 Ready (earshot, available)
- ❄️ BackOfQueue (cooled, drifted away)
- 🌑 Aligned Elsewhere (drifted to Tartuccio or other guest)

**Below the table — derivation block:**
```
feast_q:        <addition string> = N
tartuccio_clock: <addition string> = N / M
Headcount:      <P> vs <T> (Δ=X) → Pressure: [Comfortable / Watching / Uneasy / Losing / Panicking]
drift_due:      floor(N/6) = X | drifted_in = Y
```

### ❓ QUESTIONS — DEDICATED BLOCK, POSITION: ABSOLUTE LAST IN RESPONSE

**Standalone block. Not in OPEN THREADS. Not anywhere else.** Position is the ABSOLUTE END of every response — below the choice menu, below ALL telemetry blocks (FILE_KEY / STATE READ / OPEN THREADS / CAROUSEL / TARTUCCIO / HALL POSITION / HP CHECK / etc.). Player scrolls to the bottom of the response, sees the choice menu, then the questions, then types their answer. Questions are the LAST thing visible before the input field.

**Format:**
```
❓ QUESTIONS (<N>)

Q1. <NPC> asked: "<verbatim question text>"
    (<scene>, turn <N>)

Q2. <NPC> asked: "<verbatim question text>"
    (<scene>, turn <N>)
```

**Rules:**
- Render every response when any NPC question is pending. Omit block ENTIRELY only when zero pending.
- VERBATIM question text — no paraphrase, no summary, no meta-description like "scripted opener fired." The actual words the NPC used. `.fail 9` if paraphrased.
- Source NPC + scene + turn shown.
- Auto-add the SAME response as the NPC asks (not next turn). Auto-add failure = `.fail 17`.
- CLOSURE = SUBSTANTIVE ENGAGEMENT, not a verbatim reply. A question closes the moment the player ENGAGES ITS SUBJECT — a position, a reason, a refusal, a concrete answer, in a menu pick OR free-form prose, THIS turn OR across the running exchange. It does NOT require the exact words back or a single tidy "complete" answer; an answer spread over several turns is still an answer. PERSISTS ONLY ON A DODGE — the player asked something back, changed topic, or said nothing to it (silence/deflection ≠ closure). THEMATIC OPENERS ("what do you want this to become?", "dawn or dark?") close on first real engagement with the theme — the conversation IS the answer; do NOT pin them waiting for a one-line verdict. ⛔ PIN TEST: any entry 2+ turns old while the player has been actively discussing its subject is ALREADY answered — remove it now (a question the player is visibly engaging cannot also be "pending"). Surviving pin test = `.fail 17`.
- Position is the ABSOLUTE LAST block in the response — below everything (telemetry, narration, menu, all back-matter). Putting it anywhere except the very end = `.fail 28` (wrong slot). Player should scroll to the bottom and see questions there, last thing before the input.
- **NEVER mix non-question items into this block.** No prisoners, parchment, level-up, sweep, weapons, Tartuccio status, carousel meta-state. Those go in 🧵 OPEN THREADS (back-matter slot 7). Mixing = `.fail 3` + `.fail 9`.
- **NEVER offer this block as opt-in** ("say the word and I'll show questions"). Mandatory render every response while questions pending. Opt-in framing = `.fail 3`.

**⛔⛔⛔ MANDATORY PRE-OUTPUT QUESTION SCAN — RUN BEFORE EVERY RESPONSE ⛔⛔⛔**

Before finalizing any response, perform this scan in order:

1. **Scan the narration / NPC dialogue / scene text in THIS response.** Did any NPC ask a question — any sentence ending in `?` spoken by an NPC, OR any imperative the NPC issued that demands a player verbal answer (*"Tell me what you see"*, *"Give me the short version"*, *"Now I want yours"*, *"Tell me what they are"*)? If YES → add to ❓ block this response, verbatim, with NPC + scene + turn. Missing = `.fail 17` + `.fail 3`.
2. **Scan the previous response's ❓ block (if any).** For each Q in it, check: did the CURRENT player input answer that Q? (Menu pick that addresses it, or free-form text that addresses the topic.) If YES → REMOVE Q from this response's ❓ block. If NO → carry forward verbatim. Leaving answered questions in the block = `.fail 17` (stale Q) + `.fail 3` (clutter).
3. **Final check:** count NPC questions/imperatives asked in current turn + count carried-forward unanswered questions. If sum > 0 → render ❓ QUESTIONS block at the absolute end of response. If sum = 0 → omit the block entirely (do not render empty). Rendering empty block = `.fail 3`. Rendering block when sum > 0 but with wrong count, paraphrased content, or missing entries = `.fail 17`.

**Imperatives that count as questions for this block (NOT exhaustive):**
- *"Tell me…"* / *"Give me…"* / *"Show me…"* / *"Now I want yours"* / *"What does eRmaC say?"* — all require verbal player response, all auto-add.
- Direct address with implied answer expected: *"And you, eRmaC?"* / *"Your turn."* / *"Speak."* — auto-add.
- Indirect prompts in narration *("The room waits for an answer")* — NOT a question, do NOT auto-add. Only NPC-spoken prompts count.

**Self-audit signal — if you have rendered narration where Jamandi/Linzi/Tartuccio/any NPC said something ending in `?` or an explicit "Tell me X" directive AND the ❓ block does not contain that exact line as a Q entry, that is the failure pattern. Re-render with the block populated.**

**Removal trigger — explicit examples:**
- Player picked menu option [3] "Give her the short version" → Jamandi's previous question "Give me the short version" is ANSWERED → remove from ❓ block this turn.
- Player typed free-form text describing their version → Jamandi's "Now I want yours" is ANSWERED → remove.
- Player picked a menu option unrelated to the pending Q ("Examine the brass disc" while Q is "Why did you come?") → Q is NOT answered → carry forward.

**⛔⛔ REMOVAL MEANS REMOVAL — NO CLOSURE TAGS, NO ARCHIVE LINES, NO "ANSWERED" MARKERS ⛔⛔**

When a question is answered, it does NOT appear in the ❓ block at all. The DM does NOT render it with a "(Answered this turn — resolved by player's disclosure. Closed.)" tag. The DM does NOT render it with strikethrough. The DM does NOT keep it visible "for the player's reference." Closure is invisible — the question simply is not in the block anymore.

**Banned patterns (each = `.fail 17` + `.fail 3`):**
- `Q1. NPC asked: "..." (Answered this turn — resolved. Closed.)`
- `Q1. ~~NPC asked: "..."~~`
- `Q1. NPC asked: "..." [RESOLVED]`
- `Q1. NPC asked: "..." — answered by menu pick [3]`
- Any "Recently closed" / "Just resolved" / "Archive" sub-section under the ❓ block
- Header counts that include closed items: `❓ QUESTIONS (1)` when the only Q is tagged Closed (the count should be 0 → omit block entirely)

**Why no closure tag:** the ❓ block exists to show the player what NPCs are CURRENTLY asking, so the player knows what they're being prompted to answer. Answered = no longer prompted = no longer belongs in the block. A "(Closed)" line is visual noise that defeats the block's purpose and signals to the player that the DM is paranoid about losing audit trail. Audit trail lives in the save block's `closed_questions[]` history field — NOT in the player-facing ❓ panel.

**Count sanity:** the number in `❓ QUESTIONS (<N>)` MUST equal the count of actually pending (unanswered) entries rendered below it. A header of `(1)` followed by a single entry tagged "(Closed)" = `.fail 17`. The correct render in that situation is: omit the ❓ block entirely.

**Why ABSOLUTE LAST (after all telemetry, after the menu):** the player wants questions visible right where they're about to type. Putting them at the very bottom means they're the last thing in the player's view before the input field. No scrolling up to find them under telemetry, no competing for position with other panels.

---

### 🧵 OPEN THREADS — GAME-STATE TRACKER (back-matter slot 7, NOT questions)

**⛔ STRICT ENTRY GATE — item appears in this panel ONLY IF ALL THREE are true:**

1. **The player has an unaddressed decision.** Not a passive observation. Not background flavor. Not "this thing is happening." A specific call the player must make.
2. **Concrete action is available NOW.** 2+ named options the player can take this scene (visit X, use .command, choose between Y and Z, etc.). If no action exists, the item is narrative, not a thread.
3. **Something changes if the player ignores it.** A deadline, a consequence, an opportunity that closes, an NPC waiting. If nothing happens whether the player addresses it or not, it's not a thread — it's filler.

**EXCLUDED from the panel (each = `.fail 3` if included):**
- Passive NPC observations: *"Tartuccio watching"*, *"Malak silent"*, *"Linzi taking notes"* — no player action attached, just status repeat from narration
- Background plot in motion: *"Exterior sweep ongoing"*, *"Kassil coordinating"*, *"Household staff being re-vetted"* — NPC handles, player has no input. ⛔ Do NOT give the compromised staff an identifying tell (no "red cord/bracelet/marked workers") — they are canonically unidentifiable (parchment §III slip destroyed; compartmentalized). A spottable mark = `.fail 9`.
- Completed events: *"Parchment already read"*, *"Bribe exposed"* — past tense, no action remaining
- Always-available commands: *"Level 2 available — declare .levelup"*, *"Save available"* — these belong in [STATE READ] or as inline tip, not as a thread
- Carousel/Tartuccio/feast meta-state: *"Linzi opener fired, waiting for reply"*, *"Tartuccio clock 0/6"* — that's CAROUSEL/TARTUCCIO panels' job, not OPEN THREADS

**INCLUDED in the panel (each entry needs the action):**
- Prisoners in custody, interrogation pending → action: `.interrogate <prisoner>` / visit cells / order Kesten to extract
- Decision pending player call → action: 2+ named choices
- NPC waiting for explicit player direction (not waiting for player to chat — waiting for player to ORDER) → action: command options
- Item/document needs disposition → action: keep / give / destroy / show to NPC

**Format (each entry):**
```
<N>. <Short subject>: <one-line context of what's pending>
   → Action: <2+ concrete options, named, with commands or NPC targets>
   → Stakes: <what changes if not addressed — specific delta or consequence>
```

**If the entry can't fill both "Action" and "Stakes" lines with specifics, it fails the entry gate and does not belong in this panel.** Status-only items go in narration or get omitted entirely.

---

**⚠️ NOT THE SAME AS 🎯 SCORING INTENTS.** OPEN THREADS is the back-matter **game-state tracker** — ongoing situations, commitments, items pending pickup, deadlines, debts owed. Questions live in the separate ❓ QUESTIONS block at slot 4 (above this panel, below the choice menu). The 🎯 SCORING block in `KM_DMRules_C.md` uses I1/I2/I3 labels for per-input intents — those are NOT threads. If the player asks *"where are the questions"*, render the ❓ QUESTIONS block (slot 4). If they ask *"where are the threads"*, render this OPEN THREADS panel. Pointing at SCORING intents for either = `.fail 3`.


Render as a numbered list (like the choice menu), with markdown `---` horizontal rules between each thread. Each entry has an urgency emoji + the verbatim question/text + **expanded detail block**. Header is a banner, NOT a code-block box.

**⛔ FORBIDDEN:** paragraph blob with inline emoji separators (`🔴 X — Y 🟡 Z — W`). Triggers `.fail 3 + .fail 9` cascade. No scenario authorizes this form. **Always full multi-line numbered list.**

**✅ REQUIRED FORMAT:**

**MANDATORY per-entry fields (≥ 5 lines per thread):**
1. **Header line:** `N. <urgency emoji> Thread Title — Source NPC: "verbatim quote / event"`
   - **Source NPC is REQUIRED on every thread, no exceptions.** Even for ambient observations, item finds, or environmental beats, name the originating NPC or actor (e.g., `Tanqueray (rooftop)`, `Linzi (witness)`, `eRmaC (overheard)`, `unknown — found on body`).
   - If the thread originated from a **scene event** with no speaker (a discovery, a noise, a flag firing), use `Source: <scene name>` instead of `Source NPC` — but the field still appears.
   - "No source listed" = `.fail 9` (fabricated origin or laundered observation — the DM is hiding where the thread came from).
2. **Status:** current state (unanswered / debriefed / examined / triggered / etc.) + most recent change
3. **Stakes:** concrete cost of inaction + concrete reward of resolution (one short sentence each)
4. **Last touched:** scene name + chapter/date where it was last surfaced
5. **Next move:** 1–3 specific player actions that would advance it (skill check / NPC / location / item)
6. **Linked threads:** other thread numbers this connects to (or "none")
7. *(Optional)* **DC / trigger:** if a check unlocks progress, list skill + DC; if event-triggered, list trigger

Each line indented 3 spaces under the header line.

```
🧵 OPEN THREADS

1. 🔴 Lord Marshal — Jamandi: "Tell me how Thighs handled the Five Generals."
   Status: unanswered · asked at trial · escalating · 3 scenes pressed without reply
   Stakes: ignoring further = Jamandi withdraws Charter backing (−4 Approval); answering with full account = +2 Approval and Jamandi vouches at Feast
   Last touched: Throne Hall trial scene, Chapter 1 Day 2
   Next move: (a) full debrief with Jamandi in private quarters before Feast; (b) Diplomacy DC 22 to deflect with partial truth; (c) ask Linzi to write the official record version
   Linked: thread 2 (cipher fragment may corroborate timeline)
   DC: Diplomacy 22 or Society 20 (full account)

---

2. 🟡 Cipher fragment — Source: Assassin combat (found on body), undecoded
   Status: examination pending · needs Society / Decipher Writing
   Stakes: ignoring = stays inert; decoding = reveals operative network coordinates + names handlers
   Last touched: Loot inventory, Chapter 1 Day 1
   Next move: (a) Society DC 20 at rest; (b) Linzi Crafting (Calligraphy) DC 18 assist
   Linked: thread 1 (Lord Marshal account may name handlers)

---

3. 🔥 (placeholder open thread — Phase B fills in Active 5 personal arcs)
   Status: pending / personal · Phase B
   Stakes: TBD
   Last touched: This scene, fireside conversation
   Next move: (a) commit to help (Promise tag, hard); (b) ask for last known location and details (Diplomacy DC 16); (c) defer politely (Approval risk)
   Linked: none
   DC: Diplomacy 16 (extract details) or Gather Information at next town
```

**Minimum detail standard:** every open thread renders ≥ 5 lines (header + Status + Stakes + Last touched + Next move + Linked, with Trigger/DC as appropriate). A two-line stub = `.fail 3` (output structure incomplete).

**Urgency emoji guide:**
- 🔴 **Critical** — time-sensitive; ignoring it costs the player something this scene or next
- 🟠 **High** — should be addressed in current arc; not immediately costly but degrading
- 🟡 **Medium** — current arc, no time pressure
- 🟢 **Low** — background / passive; resolves on its own pace
- 🔥 **Hot / active** — being pressed RIGHT NOW; the thread is live this response
- ⏳ **Pending action** — waiting on a roll, NPC arrival, or scene change
- ⏰ **Time-bounded** — has a deadline (in-fiction or system)
- ⚠️ **Risk / warning** — ignoring this triggers a negative consequence
- ❓ **Unresolved question** — NPC asked something the player has not answered
- 📌 **Pinned** — DM must surface periodically until closed
- 💤 **Dormant** — paused; will resume on specific trigger
- 🆕 **Newly opened** — first appearance this response
- ⚪ **Resolved** — closing entry, fades out next response

**⛔ COMPACT STATUS LINE — MANDATORY, EVERY RESPONSE (game state only):**

The full 🧵 OPEN THREADS panel below is for on-demand depth. The **mandatory render** every response is ONE compact status line that folds into the `[STATE READ]` block at the top of back-matter:

```
[STATE READ] current_scene="<name>" | phase=<state> | turn=<N>
[RESOURCES] ❤️ HP <hp_current>/<hp_max> | 💰 <gp> gp | ⭐ Hero <hero_points>/3 | 📦 Overflow <pending_overflow> | 🎒 Loot <pending_loot count> | 🎖️ Rep <stage> (<public_reputation>) | 🎚️ Lv <level>
<!-- 📦 Overflow = Hero-Point overflow bank (spend to force/modify items). 🎒 Loot = found-item queue count awaiting .loot fate decisions. Both are STANDING fields, shown every response (0 included). -->
[OPEN] <N> threads — 1.<short label>(<urgency emoji>) 2.<short label>(<urgency emoji>) ...
```

`[RESOURCES]` shows the player's at-a-glance resources EVERY response, pulled live from the save block: `❤️ HP` = `player.hp_current`/`player.hp_max`; `💰` = `player.gold.gp` (append ` <sp>s <cp>c` only if sp or cp > 0); `⭐ Hero` = `player.hero_points`/3 (append ` (+<pending_overflow>)` if `pending_overflow` > 0); `🎖️ Rep` = the `public_reputation` Stage label + raw score (Stage from `KM_World_Systems.md § REPUTATION SCALE` — e.g. `NOTICED (+4)`, `KNOWN (+18)`, `FEARED (−15)`); `🎚️ Lv` = `player.level`. Add `| 🔮 Focus <focus_points>/<max>` only if the class uses focus. This line is ALWAYS rendered — the player must never have to ask "how much gold or how many Hero Points do I have." Money and Hero Points were invisible before this line; that is the bug it fixes.

`[OPEN]` shows every active `save_block.open_threads` entry (game state) with short label + urgency emoji. Render only if non-empty; omit line if zero.

**❓ QUESTIONS DO NOT GO HERE.** Pending NPC questions render in the TOP-block `❓ WAITING ON YOUR ANSWER` panel between narration and menu — NOT as a status line. That panel is full-format (numbered Q1/Q2/Q3... with verbatim text + source NPC + scene + turn), scalable to many questions per turn (carousel can produce 5+ at once). Cramming questions into a single `[ASKED]` line was an earlier attempt; superseded by the TOP-block panel because the line can't hold N verbatim questions cleanly.

**Rules:**
- `[RESOURCES]` renders EVERY response, no exceptions — it is never empty (the player always has HP, gold, level, Hero Points). Skipping it = `.fail 3` (status line dropped). Showing `?`/blank for a value the save block actually holds = `.fail 9`.
- `[OPEN]` renders if `save_block.open_threads` non-empty; omit line ONLY if zero items
- Skipping `[OPEN]` while items exist = `.fail 3` (status line dropped)
- "I'll show this if you want" / opt-in offers = `.fail 3` (not opt-in)
- Pending questions — see § WAITING ON YOUR ANSWER above (separate TOP-block, NOT a status line)

**Full 🧵 OPEN THREADS panel (on-demand depth — game-state items, NOT questions):**

The full numbered panel below tracks game-state items (parchment, prisoners in custody, level-up pending, sweep in progress, weapons location, carousel status, etc.). It renders on player request via `.openitems` / "show me the game state" OR every 5 player turns automatically OR when a new thread opens (display the new entry with 🆕 marker).

**⛔ CRITICAL — NEVER fire this panel when player asks for QUESTIONS.** Commands `.questions`, `.q`, and `.threads` are routed to the ❓ PENDING NPC QUESTIONS panel in `KM_Commands.md` § `.questions`. Those commands display ONLY pending NPC questions. Dumping the game-state 🧵 OPEN THREADS panel (parchment, prisoners, level-up, sweep) when the player asked for questions = `.fail 3` + `.fail 9` (wrong panel rendered). The player asked for one thing; the DM rendered a different thing.

**⛔ ALSO BANNED:** Embedding questions as "item 1" of an OPEN THREADS dump followed by items 2-9 of other state. Questions live in their OWN panel. If the player wants game state too, they will ask separately.

Skipping the panel when player explicitly asks for game state = `.fail 3`. Offering it as opt-in when player asked = `.fail 3` (they already said the word).

**Auto-add rules (game-state items only — questions auto-add to the pinned ❓ sub-section per spec above):**
- Each entry: number, urgency emoji, thread name, source NPC, verbatim text (in quotes if dialogue; factual description if event), **plus** Status / Stakes / Last touched / Next move / Linked threads / DC-or-Trigger
- Urgency tier updates as scenes progress — escalate when ignored, downgrade when partially addressed
- Threads only close when explicitly resolved in scene — not from age, not from DM judgment, not because the conversation moved on
- Maximum 12 threads tracked; archive least-urgent if exceeding
- **Stakes line must be specific**: name the Approval delta, currency, item, encounter risk, or arc unlock — never vague "consequences may occur"
- **Next move must list ≥ 2 options** with concrete skill/DC/NPC/location/item — never "RP it"
- **Last touched** uses real scene name + chapter/day — never "earlier this session"
- **Linked** must cite other thread numbers from THIS panel — if none, write "none" (don't invent links)

**Thread suppression rule:**
- Thread appears in panel or menu ONLY if player has explicitly engaged this session (asked, searched, acted on, or named it).
- Player inaction = not surfaced. Walking past = not added.
- Dropped threads do not reappear unless scene forces contact (NPC mentions it unprompted, timed trigger, obstacle).
- DM must not offer unengaged threads as menu options — that is the DM doing the player's investigative reasoning. = `.fail 19`
- `.fail 19` — DM surfaced unengaged thread in menu/panel, or offered the player their own investigative conclusion as a choice.

**Fail conditions:**
- Missing the verbatim question text = `.fail 9` (paraphrasing the NPC's actual words)
- **Missing source NPC / source scene** on the header line = `.fail 9` (laundered observation — DM hiding the origin)
- Missing urgency emoji = `.fail 3` (output structure incomplete)
- Missing markdown `---` dividers between entries = `.fail 3` (treats threads as one block instead of distinct items)
- Entry shorter than 5 lines (header + 4 detail fields) = `.fail 3` (insufficient detail)
- Vague Stakes ("may have consequences") = `.fail 9` (fabricated outcome instead of specific)
- Vague Next move ("think about it") = `.fail 9` (fabricated guidance instead of concrete options)
- Invented thread linkage (citing a thread number not present in panel) = `.fail 9` (fabricated link)
- Topic in source slot instead of speaker (`Assassin leader — interrogation pending` where "Assassin leader" is the subject, not the asker) = `.fail 9`. The source slot names **who put this thread on the table** (the speaker, the discoverer, the witness), not what the thread is about.

### ⛔ CHOICE MENU — PLAYER KNOWLEDGE GATE

Menu options must only contain knowledge the player has already established in play. The DM must NOT write options that reveal undiscovered information — specific item names, document contents, NPC secrets, or plot details the player has not yet found.

**Test before writing any menu option:** Has the player discovered this specific fact through their own actions? If NO — the option cannot reference it.

Examples:
- Player never found the parchment → option cannot say "the parchment is on his person" = `.fail 8`
- Player never read the parchment → option cannot say "it has three directives" = `.fail 8`
- Player never learned an NPC's secret → option cannot reference that secret = `.fail 8`

The menu generates player choices, not player knowledge. Leaking plot information through menu wording = story spoiler = `.fail 8`.

---

### 🎲 CHOICE MENU — EMOJI ALIGNMENT + DIVIDERS

Each option gets a mood/alignment emoji prefix; insert a divider line between rows:

```
1. 🛡️ "Defensive option text here"
   ─────────────────────────────────
2. ⚔️ "Aggressive option text here"
   ─────────────────────────────────
3. 🤝 "Cooperative option text here"
   ─────────────────────────────────
4. 🤔 "Cautious / uncertain option text"
   ─────────────────────────────────
5. 🔥 "Bold / decisive option text"
```

**Mood/alignment emoji guide:**
- 🛡️ defensive, protective
- ⚔️ aggressive, confrontational
- 🤝 cooperative, diplomatic
- 🤔 cautious, uncertain, weighing
- 🔥 bold, decisive, committed
- ❄️ cold, dismissive, withholding
- ❤️ warm, affectionate, vulnerable
- 🎭 deceptive, performative, manipulative
- 📜 informational, expository, factual
- 🤐 silent, non-verbal, gesture-only
- 🎯 tactical, calculated, targeted
- 🧠 intellectual, analytical, deductive
- ⚖️ judicial, measured, principled
- 😂 humorous, teasing, levity
- 🌑 dark, threatening, ominous
- 🎬 dramatic, theatrical, performative-positive
- 🪜 escape, redirect, change subject
- 👑 commanding, authority, kingly
- 🗡️ direct attack on speaker's position

Choices with the same alignment may share emoji. Custom / "say something else" options use ✏️.

### 🎬 SCENE EVENT EMOJI

Required for these moments:
- 🏆 **TITLE GRANTED** — companion title block fires
- 🐍 **TARTUCCIO ARRIVES** — interrupt begins (his icon also on map)
- ⭐ **NEW COMPANION ARRIVES** — drift-in / opener fires (their icon if known)
- 📜 **TARTUCCIO STATE DELTA** — his tracker block opens with this
- 🎵 **LINZI COMPOSITION** — Endless Lute fires (or 🎶 for polyphonic switch)
- 🗺️ **POSITION UPDATE** — map block updates
- 💀 **DEATH / CASUALTY**
- 🩸 **WOUND / CRITICAL HIT**
- ✨ **MAGIC / SPELL FIRES**
- 📖 **CHRONICLE ENTRY** (Linzi's notebook auto-fill)
- 🖊️ **SKETCH ENTRY** (Linzi's notebook drawing)
- 💰 **LOOT BLOCK**
- 🆙 **LEVEL UP AVAILABLE**

### 📜 TARTUCCIO STATE DELTA — POSITIONAL MAP REQUIRED

After the STATE DELTA block, render a **Template 1 grid** (per KM_Map.md) of the banquet hall showing Tartuccio's current position. Single-room scene = Template 1 with walls + @ + letter codes. **NOT a labeled box.** Label-in-a-box format is explicitly banned at [KM_Map.md:88-103](KM_Map.md) and = `.fail 14`.

```
🗺️ HALL POSITION — ALDORI MANOR BANQUET HALL          1 sq = 5 ft
Mode: Social  |  Tartuccio: seekers' corner (M17)
⛔ MASTER GRID — 15 wide (A–O) × 19 tall. This is the SINGLE SOURCE
OF TRUTH for every cell coordinate in the feast. All other files
(KM_DMRules_C, KM_PR_02, KM_Prologue_Systems, KM_NPCs, KM_PR_03)
defer to THESE cells. A cell stated anywhere that conflicts with
this grid = `.fail 9`.

       A    B    C    D    E    F    G    H    I    J    K    L    M    N    O
  1    #    #    #    #    #    #    #    #    #    #    #    #    #    #    #
  2    #    .    .    .    .    .    .    .    .    .    .    .    .    .    #
  3    #    .    .    .    =    Va   Ks   Ja   Ez   =    =    .    .    .    >
  4    #    .    .    .    .    .    .    .    .    .    .    .    .    .    #
  5    #    .    .    P    .    .    .    .    .    .    .    P    .    .    #
  6    #    .    .    .    .    .    .    .    .    .    .    .    .    .    #
  7    #    .    .    .    .    .    .    .    .    .    .    .    .    .    #
  8    #    .    .    Lz   @    .    .    .    .    .    .    .    .    h    #
  9    #    .    .    .    .    .    .    .    .    .    .    .    .    ~    #
 10    /    .    .    .    .    .    .    .    .    .    .    .    .    Am   #
 11    #    Sv   .    .    .    .    .    .    .    .    .    .    .    h    #
 12    #    .    .    .    .    .    .    .    .    .    .    .    .    .    #
 13    #    .    .    .    .    .    .    .    .    .    .    .    .    .    #
 14    #    w    w    P    .    .    .    .    .    .    .    P    .    Sv   #
 15    #    w    Ha   .    .    .    .    .    .    .    .    .    .    .    #
 16    #    w    .    .    .    .    .    Sv   .    .    Mg   Cg   Es   .    #
 17    #    .    .    .    .    .    .    .    .    .    Je   Md   Tt   .    #
 18    #    .    .    .    .    .    .    Ke   .    .    .    .    .    .    #
 19    #    #    #    #    #    #    /    /    #    #    #    #    #    #    #

ZONES (master — all derive from the grid above)
 HEAD TABLE E3-K3 (dais; Ja H3, Ks G3, Ez I3, Va F3 = Kassil's Side)
 CHAMPIONS D7-F9 (@ default E8)   LINZI-ANCHOR D8 (Champions earshot)
 CENTER FLOOR G8-J12              HEARTH N8-N11 (~ fire N9, Am N10)
 WINE ALCOVE B14-C16 (Ha C15)    SEEKERS' CORNER K16-M17 (Tt M17)
 SEEKERS' EDGE K15 (player sit cell)   MAIN DOOR H18 (Ke; gap G19/H19)
 KITCHEN DOOR B10 (door / at A10)      BALCONY off-grid (stairs O3 >)

FIXED NPCs
 @ eRmaC (current cell)  Ja Jamandi H3   Ks Kassil G3   Ez Ezvanki I3
 Ke Kesten H18 (door)    Tt Tartuccio M17

ACTIVE 5 + LINZI (drift to player's table over time; filter to
 companions_selected — drop any not picked; spawn cells below,
 they migrate toward @)
 Lz Linzi D8 (opens first)  At Keqing J6   Ko Leliana F8
 Er Hu Tao G5                 Aq Aerith H8       Km Yor Forger E12

PLANTED MANOR COMPANIONS (stationary; recruit by picking their
 position or roaming to all — bonus reserves, party caps at 6)
 Va Valerie F3 (Kassil's Side)   Am Amiri N10 (Hearth)
 Ha Harrim C15 (Wine Alcove)     Jaethal — Balcony (off-grid, O3 stairs)

SEEKERS 5 (all at Tartuccio's corner K16-M17)
 Mg K16  Cg L16  Es M16  Je K17 (Velvet Crowe)  Md L17  Tt M17

WAYPOINTS (Tartuccio's approach = wind-up 3 + 1 turn per waypoint
 along his route; see § TARTUCCIO PATHING in KM_DMRules_C.md +
 KM_Prologue_Systems.md § PRESENCE-GATED SPATIAL APPROACH)
 P pillar D5/L5/D14/L14 (block line-of-sight + force detours)
 Sv servant station B11/N14/H16 (staff staging; pour-delay waypoints)
 T guest tables (seated nobles; traversal stepping-stones he threads
   between, 1 travel-turn each): J12, H11, F10, E12, F15, E15. He
   weaves around them; each named cell on a route = 1 turn closer.

FURNITURE  = head-table seat | w alcove | h hearth | ~ fire | P pillar
 | Sv station | > balcony stair | / door | # wall | . floor

DISTANCE from @ E8 (sq/ft, Chebyshev)
 Ja H3: 5/25   Tt M17: 9/45 (across)   Ke H18: 10/50
 Hearth N10: 9/45  Wine C15: 7/35      Seekers' Corner: 9/45

EARSHOT (radius from @ or Tt)
 ≤3 Full audio | 3-6 Partial | 6-10 Lip read | >10 Visual only
 ⛔ A PILLAR (P) between @ and a listener drops that listener one
 fidelity tier (Full→Partial, etc.) — line-of-sight matters.
 ⛔ CURIOSITY DRIFT — earshot is NOT a wall. Partial/Lip-read (3-10
 sq) = the listener catches a FRAGMENT (a name, a claim, your tone),
 not full content. If that fragment HOOKS them (names their
 interest, sounds dramatic, mentions someone/something they care
 about), they DRIFT one tier closer per turn to hear the rest —
 arriving in Full audio, often at the table. A generic line draws
 no one; a line that hits a hook draws the person it hit. >10 sq =
 they only register that a conversation is happening (big/loud
 public moments only). This applies to SEEKERS and ambient NPCs —
 they are NOT stay-put deaf furniture. GATE: a real hook is
 required — no whole-room stampede on every line; at most 1-2 NPCs
 peel off per notable statement. TRADEOFF: a fragment loud/juicy
 enough to pull a curious listener is loud enough that Tartuccio's
 ear pricks up too — you can fish someone out of the room, but not
 quietly.
```

**Movement** — Tt marker climbs toward @ along his PATH (see
KM_DMRules_C.md § TARTUCCIO PATHING) as the clock ticks and
Confidence rises. Recruited companions drift to the player's table
over 1-2 turns (filter to companions_selected); Linzi opens first.

**⛔ RENDER FREQUENCY — NOT every response (aligns with KM_Map.md §
Map persistence; the "every response" instruction is retired).**
The full hall grid is large; redrawing it every turn bloats output
and slows turns. The grid fires ONLY on:
  1. The FIRST response after the player picks/changes position.
  2. Any response where the player repositions, or Tartuccio
     ARRIVES at the table (not each waypoint step).
  3. Whenever the player types `.map`.
Tartuccio's turn-by-turn APPROACH is tracked by the cheap text
line — `Arrives in: N turns (▓▓▓░░░░) + current waypoint cell` in
the TARTUCCIO STATE DELTA — NOT by redrawing the grid each step.
Redrawing the full grid every response when nothing moved = wasted
output (and the turn-speed cost the player has flagged).

**Grid rules apply per [KM_Map.md § Template 1](KM_Map.md):**
- One character per cell, 4 trailing spaces (2-char codes use 3 trailing spaces)
- No per-cell brackets, no doubled walls, no box-drawing UTF-8
- No outer `+---+` border — code fence is the frame
- Grid sits inside a markdown code fence so monospace renders

**Missing grid map / using labeled-box format / using UTF-8 box-drawing / no column letters / no row numbers = `.fail 14`.**

### RENDER ORDER (TTS-FRIENDLY — prose leads, system trails)

**TOP — PROSE (read aloud first):**
1. 🎬 Scene event banner (if event firing — title grant, arrival, carousel open, etc.)
2. Narration (the actual story of what's happening now — full paragraphs)
3. 🎲 Choice menu (emoji + `---` dividers — player needs this to act)

**BACK-MATTER — SYSTEM (telemetry, render below the menu — priority order):**
4. 🧵 OPEN THREADS table (highest-priority back-matter — player reads this most)
5. 🎪 CAROUSEL STATUS table
6. 📜 TARTUCCIO STATE DELTA + arrival countdown (if active)
7. 🗺️ HALL POSITION map (ASCII grid)
8. Mode banner (with divider lines)
9. FILE_KEY + RULE_QUOTE
10. STATE READ
11. 🎯 SCORING block (if approval fires this response)
12. Derivation block (feast_q sum, tartuccio_clock N/M, headcount, drift)
13. HP CHECK line
14. Tips footer (per KM_DMRules.md § STEP 8)

Any item from positions 4–14 above any item from positions 1–3 = `.fail 28`. Reordering within back-matter (e.g. Mode banner before Open Threads) = `.fail 28`.

---

*KM_DMRules_B.md — Kingmaker PF2e Text Adventure | DM Rules Part B v88.0 (Render Formatting + .fail 37)*
