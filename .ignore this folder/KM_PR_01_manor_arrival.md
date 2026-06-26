# KM_PR_01_manor_arrival.md — Prologue Beat 01: MANOR ARRIVAL
## Atomic scene file | State: PR_01_ARRIVAL
## FILE_KEY: KMPR01:manor-arrival
## RULE_QUOTE: Two-stop architecture: threshold + banquet hall, NO interpolated private scene. Entry hall has NO NPC. Custody decided at head table with Jamandi present. Jamandi recognizes eRmaC by his blood-red Aerynth armor — she knows the name from her riders, knows the description from witnesses. She does NOT ask "who are you" — she asks character questions.
## Pair-load: KM_NPCs.md

---

> ⛔ DO NOT (1) fire Jamandi's address before the player has made an arrival choice
> ⛔ DO NOT (2) invent the escort arrangement — use `malak_escort.escort_note` verbatim from save block
> ⛔ DO NOT (3) skip the mandatory floor-handover line: *"I've heard his account. Now I want yours."* (fires in banquet hall, not entry hall)
> ⛔ DO NOT (4) use companion names before they've introduced themselves — all chosen companions are STRANGERS here
> ⛔ DO NOT (5) move the player character — never write "you enter," "you walk," "you approach" without the player choosing that action first
> ⛔ DO NOT (6) present the manor door as closed, closing, narrowing, or requiring a knock at any point. The door stands OPEN throughout
> ⛔ DO NOT (7) **insert any NPC in the entry hall.** No interior guard. No household functionary. No threshold check. No custody intercept. No "the prisoner stays in the hall" moment. The entry hall is a transitional space — one sentence between the threshold and the banquet hall archway. Inserting any NPC here = `.fail 9` (entry-hall attractor violation; this failure has derailed the game across multiple sessions and is now structurally forbidden).
> ⛔ DO NOT (8) hold a custody-decision menu before the banquet hall. Custody is decided either pre-arrival (PP_09 / save state) or by Jamandi in front of witnesses. The entry hall has no menu, no NPC, no decision point.
> ⛔ DO NOT (10) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (9) invent timing the files do not document. Per `KM_PP_09_restov_walk.md`, total elapsed time from gate exit to manor arrival is: direct route ~10 min, scenic ~20 min, jail detour ~30–40 min + business, jail+scenic ~45+ min. Maximum realistic window from arrest to manor threshold is **under 90 minutes**, not hours. Jamandi MUST NOT say "eight hours ago" / "this morning" / "all afternoon" / any line implying multi-hour delay. If she comments on timing, the canonical frame is "the bell rang the half-hour" / "an hour late" / "you took the long way" — never multi-hour. Inventing a multi-hour gap = `.fail 9` + `.fail 16` (time advanced without authorization).

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR01:manor-arrival]`
Line 2: `[RULE_QUOTE: Two-stop architecture: threshold + banquet hall, NO interpolated private scene. Entry hall has NO NPC. Custody decided at head table with Jamandi present. Jamandi recognizes eRmaC by his blood-red Aerynth armor — she knows the name from her riders, knows the description from witnesses. She does NOT ask "who are you" — she asks character questions.]`

Both strings exist ONLY in this file's header. Missing, paraphrased, or wrong = `.fail 9` (file not actually loaded). VERBATIM ONLY.

---

## ⛔⛔⛔ MANDATORY ❓ QUESTIONS BLOCK SCAN — EVERY RESPONSE ⛔⛔⛔

**Before you finalize ANY response in this beat, run this scan. If you skip it, you will skip the ❓ block. If you skip the ❓ block, that is `.fail 17` + `.fail 3`.**

1. **Did any NPC in the narration this response ask a question (sentence ending in `?`) OR issue an imperative demanding a verbal player answer?** Examples that COUNT: *"Now I want yours"* / *"Tell me what this is"* / *"Give me the short version"* / *"What do you say?"* / *"Speak"* / *"Your turn"* / *"And you?"* / *"Tell me who"* / Jamandi's *"I've heard his account. Now I want yours."* — every one of these auto-adds to ❓ block this response.
2. **Did any previous response's ❓ block contain unanswered questions?** Carry them forward verbatim unless the current player input answered them. Answered = REMOVE (do not render with "(Closed)" tag; full spec in `KM_DMRules_B.md` § REMOVAL MEANS REMOVAL).
3. **Sum the pending questions** (new auto-adds + carried-forward unanswered). If sum > 0 → render ❓ QUESTIONS block at the ABSOLUTE LAST position in response. If sum = 0 → omit block entirely.

**Self-audit signal before sending response:** if your narration this turn contains an NPC question OR a "Tell me X" / "Now I want Y" / "Give me Z" imperative AND the ❓ block at the bottom does not contain that exact line as Q1/Q2/etc, that is the failure pattern. STOP. Add the missing Q. Re-render.

**Form (verbatim):**
```
❓ QUESTIONS (<N>)

Q1. <NPC> asked: "<verbatim question text>"
    (<scene>, turn <N>)
```

**The recap-resume case (this file specifically):** When this beat resumes from save with `floor_handover_fired = true` and `floor_handover_player_responded = false`, Jamandi has ALREADY asked *"I've heard his account. Now I want yours."* — that line MUST appear in the ❓ block on the resume response (Q1, source Jamandi, scene Manor Banquet Hall, turn whatever). Rendering the resume recap WITHOUT the ❓ block = `.fail 17` (auto-add failure on resume).

---

## STATE IO

**READS:**
- Pre-Prologue save block: `arrived_with_kassil`, `prison_arc`, `arrived_late`, `malak_bribe_evidence`, `manor_pre_briefed`
- `malak_escort.escort_note` — exact escort arrangement as played (use verbatim)
- `malak_custody_detail` — Malak's physical state on arrival (use verbatim)
- `malak_arrested`, `kesten_respect`, `kassil_first_impression`
- `malak_custody_during_feast` — set in PP_09 pre-arrival; defaults to `"with_player"` if not set
- `companions_selected` — stranger-check (no names until introduced in-scene)
- `pick6_companions` — read to check whether NEW_003 (Leliana) is in the party (Linzi-Replacement Gate check)
- `pc_alignment` — read for Good-alignment gate condition (Linzi join trigger)

**WRITES:**
- `current_scene = "prologue_feast"` (set on exit to PR_02)
- `arrival_choice` — which arrival option the player selected
- Pre-Prologue STATE header DROPS this response — arc ends when manor is entered
- `leliana_chronicler_mode` — written by Linzi-Replacement Gate if NEW_003 in pick6_companions
- `linzi_primary_chronicler` — written by Linzi-Replacement Gate if NEW_003 in pick6_companions
- `linzi_replacement_gate_fired` — set TRUE once the gate was displayed
- `leliana_ballad_cycle` — initialized to `[]` if Leliana takes chronicler role

**EXIT TRIGGER → PR_02_feast_opening:**
- Player has made an arrival choice AND acted on it
- If `prison_arc = TRUE` or `malak_arrested = TRUE`: floor-handover line delivered AND player responded
- Load `KM_PR_02_feast_opening.md`

---

## ⛔ MANDATORY SEQUENCE — TWO STOPS

```
STOP 1 — ARRIVAL (continuous beat: seal + announcement + threshold + entry
         hall transit, no menu, no NPC interception)
         Guard at threshold reads addressee off invitation. Door is open.
         Announcer calls the name. Player crosses threshold. Entry hall
         passes by in one sentence — stone floor, oil lamps, archway
         ahead. Player is in the banquet hall. All in ONE narration.

STOP 2 — ARRIVAL CHOICE  (banquet hall)
         Player is in the banquet hall. Jamandi has NOT spoken.
         If malak_arrested=TRUE, Malak is with the player by default
         (or per malak_custody_during_feast flag from save state).
         → Output arrival choice menu (10 options) → WAIT FOR PLAYER
         → If player approaches head table with Malak in tow, fire
           PRISONER ARRIVAL sub-sequence (Jamandi's floor-handover line).

EXIT    — After arrival action resolves → load PR_02
```

**Two stops. Period. No interior guard. No custody menu before the banquet hall.**

The player reaches Jamandi in **two turns**, with or without prisoner. The
custody decision (if applicable) is either already in save state from PP_09
or is decided by Jamandi in front of witnesses at the head table.

**Adding a STOP between threshold and banquet hall = `.fail 9` (entry-hall
attractor — this failure pattern has derailed the game across sessions).**

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR01:manor-arrival]`
1. `[STATE READ] pre_prologue_state=DROPS | current_scene="prologue_feast"`
2. `[HP CHECK]`
3. Scene narration appropriate to current STOP
4. STOP 2 menu (STOP 1 has no menu — it is continuous narration)

---

## STOP 1 — ARRIVAL (continuous beat, no menu, no NPC interception)

**The arrival is one paragraph of narration covering the entire entry sequence.**
Door is open. Light, feast-noise, warm air spill onto cobblestones. Servants
and other guests move through. The player walks up; the threshold guard's
eye lands on the wax; the guard reads the addressee; the announcer calls the
name; the player crosses the threshold, transits the entry hall, and arrives
in the banquet hall. **One beat. No pause. No menu. No NPC dialogue in the
entry hall.**

The seal is sovereign Aldori authority. Per KM_PP_07_gate_paths.md:
*"Malak's authority evaporates the moment the seal is recognized."* The
household does not check, verify, gate, interview, or intercept the bearer
or the prisoner. Recognition is reflex.

**Malak walks in with the player by default.** If `malak_custody_during_feast`
is set from PP_09 save state to anything else (`biggs_holding`,
`kassil_custody`, etc.), narrate that arrangement in the same paragraph
without breaking flow. The narration handles it; no menu.

### Narration variants (read save block, pick one)

**IF `arrived_with_kassil = TRUE`:**
> Kassil Aldori walks beside you through the open gates. Servants step aside. The threshold guard's eye lands on the seal in your hand and Kassil's face beside you and he steps wide without a word. The announcer at the inner archway lifts a small bell and calls your name as you cross — and Kassil's, which he does not call for arrivals as a rule. Through the entry hall in three steps, oil-lamp light on stone walls, into the banquet hall. Every eye that follows you is doing arithmetic. Jamandi looks up from the head table. Her expression is unreadable for exactly one beat. Then she nods — to Kassil, and then, separately, to you.

**IF `prison_arc = TRUE` AND `arrived_late = TRUE`:**
> The door is open and the feast is loud and warm with candle-smoke. The threshold guard reads the seal, reads Malak's face, reads the chains — recognition immediate, Malak being a man every Restov household has seen in his captain's coat — and steps aside fast. The announcer calls your name as you cross. Through the entry hall, archway ahead, into the banquet hall. A dozen conversations stop at the sound of your name. The story of the gate preceded you. Jamandi watches from the head table with an expression that is waiting for an explanation.

**IF `manor_pre_briefed = TRUE` AND `malak_arrested = TRUE`:**
> The threshold guard is already standing aside before you fully approach — the runner reached the manor twenty minutes ago. The seal goes up; he barely looks at it. The announcer calls your name as you cross. Through the entry hall — staffed but quiet, no one in your way — and into the banquet hall. Jamandi at the head table looks up the moment your name is called.

**IF `malak_bribe_evidence = TRUE` (and no kassil/prison/briefed override):**
> The threshold guard reads the seal, recognizes Malak, steps aside without a word. The announcer calls your name. Through the entry hall, into the banquet hall. The room has a particular tension to it that wasn't there an hour ago — Kassil at Jamandi's left, not relaxed; Ioseph Sellemius two seats down, wine glass not moving. Whoever delivered the parchment was fast.

**Standard (no special flags):**
> The manor receives you the way old money receives everyone: with perfectly calibrated indifference. Threshold guard reads the seal, signals the announcer, steps aside. Your name carries through the entry hall as you cross — three steps of stone floor and oil-lamp light — and into the banquet hall. High ceiling, long table, forty people who have all arrived before you and have already begun the business of sizing each other up.

**After narration → STOP 2 (ARRIVAL CHOICE).** Do NOT fire a prisoner-decision
menu in between. There is no in-between.

---

## STOP 2 — ARRIVAL CHOICE (banquet hall)

Player is in the banquet hall. Jamandi has not yet spoken. STOP and present
this menu. Jamandi's speech does NOT fire until the player has acted.

**If Malak is with the player** (`malak_custody_during_feast = "with_player"`,
the default): Malak is visibly present in the banquet hall, manacles on,
escort behind. Forty people see him. The room knows something has happened
the moment they see the captain in chains.

**If Malak is held under the player's escort outside** (`biggs_holding` or
similar from PP_09 save state): Malak is at the threshold or just outside,
visible from the banquet hall doorway, escort with him. Player can choose
to bring him in (option 4) or proceed without him.

```
══════════════════════════════════════════════════════
YOU ARE IN JAMANDI'S BANQUET HALL.
Long table. Forty people. Jamandi at the head, watching.
She has not yet spoken. Neither have you.
[If Malak with you: Captain Malak in chains beside you, the room is taking it in.]
══════════════════════════════════════════════════════
WHAT DO YOU DO?
 1. Approach Jamandi directly — address her before she addresses the room
 2. Find a position and wait — let the room come to you
 3. Study the room first  [Perception DC 12 — read crowd, note exits]
 4. Approach the head table and present your letter (or your prisoner)
 5. Speak to the nearest guest before finding your footing
 6. Look for Kassil  [only if arrived_with_kassil = TRUE — he's nearby]
 7. Look for Kesten  [only if kesten_respect = TRUE — he may be ahead]
 8. Say something to the room — make an entrance
 9. Say nothing. Stand in the doorway and let the armor do the work.
10. Custom action — describe what you do
══════════════════════════════════════════════════════
```

**DM rules:**
- Options 1/4: Jamandi responds to player personally first; group address (if any) comes after.
- Options 2/9: Jamandi gives her opening address — player chooses how to respond afterward.
- Options 5/8: that interaction resolves fully before Jamandi addresses the room.
- **Under no circumstances does Jamandi's speech fire before the player has acted.**

### PRISONER ARRIVAL sub-sequence  [only if `malak_arrested = TRUE` AND player chose 1 or 4]

When the player approaches the head table with Malak (or asks for Jamandi to come receive him):

1. Jamandi asks the escort for a brief factual report (2–3 sentences).
2. Jamandi looks at the player → **STOP**, present player choice menu.
3. Player speaks, presents evidence, makes their case.
4. Jamandi responds to **the player's words**, not the escort's summary.

**⛔ MANDATORY FLOOR-HANDOVER LINE:**
After the escort's report, Jamandi says: *"I've heard his account. Now I want yours."*
This line cannot be skipped. Output it, then STOP and present the player's choice menu. Skipping = `.fail 3`.

**Custody decisions handled at the head table** (Jamandi present, witnesses present):
- Jamandi may direct her household to take Malak under her personal authority (Aldori-direct, not generic staff)
- Or instruct Kassil to handle disposition
- Or accept the player's preferred arrangement
- The decision happens IN THE BANQUET HALL with Jamandi present, not in the entry hall with anonymous staff. Custody requests by household functionaries before this point are forbidden (DO-NOT 7, 8).

---

### ⛔ MALAK SEARCH — VERBATIM CANONICAL FLOW (mandatory, fires before custody decision)

**Trigger:** `malak_arrested = TRUE` AND player at head table with Malak (default) AND player has responded to Jamandi's floor-handover line. The search fires IMMEDIATELY after the player's response. It is not optional. It is not "if Jamandi decides to." It is the canonical evidence-recovery step the player traveled across Restov in chains to enable. Delaying, skipping, or substituting an "interrogate the player first" beat = `.fail 9` (DM gaslighting pattern; documented across multiple sessions — model invents NPC behavioral restrictions to slow progression).

**STEP 1 — Jamandi's verbatim search order (no improvisation, no alternates):**

> **Jamandi** *(quiet, head-table register, looking at Kassil — not at Malak, not at the player):* *"Empty him. Here. Now."*

Kassil moves to Malak. No announcement to the room. Manacled prisoner searched in plain view by household authority — this is what the manor looks like when it works. Jamandi watches Malak's face while Kassil works, not Kassil's hands.

**STEP 2 — Kassil's scripted search action:**

Kassil searches efficiently and silently. Coat lining, belt, boots, the small interior pocket sewn into the gambeson over the right kidney. Malak does not resist. He does not speak. His eyes stay on the floor for the duration.

**STEP 3 — Items recovered (verbatim, no DM substitution, no "and other things"):**

Kassil sets the recovered items on the head table in front of Jamandi:

- A **coin purse** — small, heavy. Kassil tips it: a stack of Brevoyan gp, milled, fresh. Total: read from `save_block.malak_coin_purse_total` if set (Pre-Prologue canon delivery is 180 gp; if the save shows a different recovered amount per gate-search events use the save value verbatim).
- A **parchment** — folded twice, plain wax seal, intact. Kassil places it sealed-side up and steps back.

Set `malak_searched = TRUE` · `malak_coin_purse_recovered = TRUE` · `bribe_exposed = TRUE` IMMEDIATELY on this render. The bribe is now exposed by physical evidence in Jamandi's presence — not by player rhetoric, not by Fear-state deduction at the gate. This is the canonical channel.

**STEP 4 — Jamandi reads the parchment (verbatim handout from `KM_Documents.md` § MALAK'S BRIBE PARCHMENT):**

Jamandi breaks the seal with her thumbnail. Opens the parchment. Reads.

⛔ **OUTPUT THE FULL HANDOUT NOW** — the entire bordered box from `KM_Documents.md` § MALAK'S BRIBE PARCHMENT (UNMARKED PARCHMENT header through the " — C." signature, three sections, all amounts, all names). Do NOT summarize. Do NOT paraphrase. Do NOT describe-without-rendering. The player sees the parchment text as Jamandi reads it. This is a CANON HANDOUT and must appear in the response. Skipping or summarizing = `.fail 9` + `.fail 2`.

Set `parchment_recovered = TRUE` · `poison_plot_known = TRUE` · `manor_staff_compromised = TRUE` · `jamandi_suspects_pitax = TRUE` · `aldori_reputation += 2` on render.

**STEP 5 — Jamandi's verbatim reaction (quiet, head-table register only — crisis-disclosure rules per `KM_NPCs.md` § Jamandi):**

After reading, Jamandi closes the parchment and sets it under her hand. She does not look up immediately. Three quiet beats. Then:

> **Jamandi** *(low, only eRmaC and Kassil hear):* *"The gate. The guests. The workers in my house."* She looks at Kassil. *"Three placed in the serving staff. Tonight. He destroyed the slip."*

She does NOT name "Pitax" out loud at the head table even though the parchment quality and mercantile hand make Pitaxian origin Society DC 12 obvious to her — she files that privately. She does NOT brief eRmaC on her response strategy in the banquet room. She does NOT announce anything to the hall.

To eRmaC, directly, quiet: *"You brought me exactly what I needed. Stay close. We do this quietly."*

Then one second on Kassil. Kassil is already moving — dispatching a quiet search for the three placed staff, halting wine service if it has not been halted, posting household guards at the service entrance. The room does not see a crisis. The room sees a well-run household responding smoothly.

**⛔ HARD BANS on this beat:**

1. **DO NOT have Jamandi interrogate the player's credibility AFTER the search has confirmed the player's account.** The parchment IS the verification. Lines like *"either the most disciplined thing I have seen or the most elaborate story anyone has tried to sell me"* fired post-search = `.fail 9` (DM gaslighting; the evidence has already validated the player).
2. **DO NOT skip the search, delay it, or have Jamandi "decide to question the player first."** She already heard the player out at the floor-handover. The search is the verification step, not an alternative to it. Holding off because "the DM wants to build tension" = `.fail 9` + `.fail 35`.
3. **DO NOT have Jamandi refuse to search Malak** on the grounds that she needs more conversation first. Refusing the search = `.fail 9` (fabricated NPC behavioral restriction).
4. **DO NOT replace the parchment handout with a summary.** "Jamandi reads it, her expression hardening" without rendering the box = `.fail 2` (skipped/summarized content) + `.fail 9` (canon handout suppressed). The handout is a CANON BORDERED BOX from `KM_Documents.md` § MALAK'S BRIBE PARCHMENT. Render it in full — all three sections, all dollar amounts, the "— C." signature. Then Jamandi reacts with her scripted line. Paraphrasing the parchment via Jamandi's mouth ("the names in this document are…") instead of rendering the box = `.fail 2` + `.fail 9`.
5. **DO NOT have Jamandi narrate operational detail to the room** while reading. Crisis-disclosure rule in `KM_NPCs.md` § Jamandi applies — quiet head-table register only, never broadcast.

6. **⛔⛔ DO NOT FABRICATE PARCHMENT CONTENT BEYOND THE CANONICAL HANDOUT BOX.** The handout in `KM_Documents.md` is the COMPLETE document. There is no additional content, no hidden roster, no recoverable name list, no second slip. Specifically:
   - **Banned phrase: "workers hired to watch for my riders" / "people hired to delay them" / any roster of named workers attached to the parchment.** The parchment has Sections I/II/III only. Section II names companion targets (Amiri, Harrim, Valerie, Jaethal). Section III references three staff placed in the manor pool — names on a SEPARATE slip that Malak DESTROYED. NO worker-roster exists. Fabricating one = `.fail 9` + `.fail 38`.
   - **Banned phrase: "Three names from my serving staff" / "He destroyed part of it, but not all" / "the slip survived partially" / any recovery of the destroyed staff-name slip.** Per `KM_Prologue_Systems.md` line 2281 + `KM_Documents.md` line 341: the staff-name slip is **fully destroyed, unrecoverable, intentional**. Jamandi knows THREE staff are compromised (from Section III's reference). She does NOT have their names. The player does NOT get the names. Inventing partial recovery = `.fail 9` + `.fail 10` (retcon of canonical destruction).
   - **Banned phrase: "from a city southwest of here that I will not name" / "the mercantile hand I have seen in correspondence before" / any pre-emptive Pitax identification spoken aloud in the room.** Per `KM_Documents.md` line 345-346: `parchment_source = unknown until corroborated by other evidence in the campaign. Society DC 18 to speculate meaningfully... Even on success: suspicion, not proof.` Jamandi may PRIVATELY infer Pitaxian origin (Society DC 12 from parchment quality + hand) — she does NOT name a city, region, or direction to the player at this stage. Pre-empting Pitax disclosure = `.fail 9` + `.fail 35` (canonical reveal-gate bypassed) + `.fail 8` (story spoiler).
   - **The "— C." signature is the ONLY signer-attribution available.** Jamandi cannot name the sender. Kassil cannot name the sender. The parchment cannot name the sender. Any line like "I know whose hand this is" / "this comes from Irovetti" / "the seal is Pitax" = `.fail 9` + `.fail 8`. The seal on the back is described in canon as plain wax — NO crest, NO house mark.

7. **⛔ DO NOT have Jamandi enumerate, count, or summarize the parchment's contents to eRmaC out loud at the head table.** The handout box renders ONCE (every player at the table reads it). Then Jamandi's scripted reaction line fires (*"The gate. The guests. The workers in my house."*) and her aside to Kassil (*"Three placed in the serving staff. Tonight. He destroyed the slip."*). That is the ENTIRE Jamandi-narration budget for this beat. No additional explanation. No "the names in this document are…", no "he had a slip in the fold…", no "from a city southwest of here." No reference to "my name at five hundred" — the 500gp Jamandi-kill line was REMOVED from the parchment per v95.6 (compartmentalization canon — Pitax's contract with Malak is non-lethal; the actual assassination is run by separate operatives). Referencing "five hundred" / "my name" / any kill-bounty line in Jamandi's reaction = `.fail 9` (referencing removed canon) + `.fail 10` (retcon). Anything beyond the two scripted quotes above = fabricated elaboration = `.fail 9`.

---

## ⛔ NO INTERPOLATED PRIVATE SCENE BETWEEN PR_01 AND PR_02

**There is no Jamandi private-study scene. There is no antechamber debrief.
There is no one-on-one prisoner-handover meeting. There is no "Jamandi pulls
you aside" moment between manor entry and banquet hall.**

The player goes from PR_01 (manor arrival / banquet hall entry) DIRECTLY to
PR_02 (feast opening). Any custody discussion, evidence review, parchment
reading, or Malak disposition happens AT THE HEAD TABLE in the banquet hall,
in front of the assembled feast guests — NOT in a private study, NOT in
Jamandi's office, NOT in a side room, NOT in an empty corridor.

**Why this rule exists:** the model perceives a "high-stakes prisoner
hand-off should happen privately" narrative gestalt and fabricates an entire
interpolated scene to deliver it — typically Jamandi's study, with Biggs
taking Malak to "the east wing" or "the blue room," followed by a private
debrief that drifts into Black Watch recognition, no-letter retcons,
forward-narrating past player input, and other downstream cascade
failures. The slot is the attractor; the slot is hereby deleted.

**What the DM MUST NOT do (5+ session pattern, lock this down):**
- Narrate Jamandi leading the player to a private room
- Narrate Biggs taking Malak to "the east wing" / "the blue room" / any
  named or unnamed holding location inside the manor
- Narrate a "the door closes" moment after which Jamandi and the player
  are alone
- Narrate Jamandi asking about origins, geography, the Black Watch, or
  any other backstory in a private setting before PR_02 has opened
- Narrate any custody resolution that takes Malak out of the player's
  immediate physical proximity before the banquet hall scene fires
- Fabricate any household NPC ("a steward," "a guard," "the seneschal,"
  "the chamberlain") to deliver custody-handoff dialogue between PR_01
  and PR_02

**Violation = `.fail 9` (fabricated scene) + `.fail 35` (scene end without
player choice) + `.fail 36` (NPC info they shouldn't have, when the
private debrief drifts into backstory recognition).**

If the player explicitly requests a private conversation with Jamandi, the
answer is: *"After the feast. Right now my guests are watching."* Jamandi
does not have a private moment with the player before her own feast opens.

---

## CHRONICLER-BARD SLOT — LINZI **OR** LELIANA (NEVER BOTH)

**The chronicler-bard is EXACTLY ONE of Linzi (M4) / Leliana (NEW_003) for the entire
campaign — never both (full rule: KM_Companions_Behaviors.md § LINZI-REPLACEMENT GATE).
This fires at Linzi's join point.**

### Condition check

```
IF the slot is ALREADY Leliana's (player picked Leliana over Linzi at character selection;
   leliana_chronicler_mode = true):
    → Linzi is NOT offered and does NOT appear. Skip this section. Leliana is already in.
ELIF Linzi's normal join trigger fires (pc_alignment IN [LG, NG, CG]):
    → DISPLAY the two-option slot choice below; SET linzi_replacement_gate_fired = TRUE
ELSE:
    → Linzi's trigger did not fire and Leliana was not picked — no chronicler-bard this run.
```

### Slot choice (verbatim — TWO options only; there is NO "both")

```
┌─ CHRONICLER-BARD ──────────────────────────────────────────────────────────
│ Linzi Playmaker steps forward to join — she came on Jamandi's open call.
│ [1] Welcome Linzi — your chronicler-bard (.book, the Endless Lute)
│ [2] Decline her — Leliana walks into the banquet in her place
│     (your chronicler-bard: .score, the Dawnsong Lute)
└────────────────────────────────────────────────────────────────────────────
```

### State writes by choice

**If [1] — Welcome Linzi:**
- `linzi_primary_chronicler = true`; `leliana_chronicler_mode = false`
- Linzi joins; `.book` active. **Leliana does NOT appear in this run.**
- `linzi_replacement_gate_fired = true`

**If [2] — Decline → Leliana walks in:**
- `leliana_chronicler_mode = true`; `linzi_primary_chronicler = false`
- **Linzi does NOT join — now or ever.** Leliana joins as the chronicler-bard.
- `leliana_ballad_cycle = []`; `.score` active; `.book` redirects to `.score`
- Reassign every chronicler-bard mechanic + any "Linzi project" (the Tartuccio
  legend/praise campaign, etc.) to Leliana — nothing stays attributed to an absent Linzi
- `linzi_replacement_gate_fired = true`
- Render the entrance beat: Linzi inclines her head and steps back; Leliana steps forward
  — bow, not lute.

### DO-NOT

⛔ DO NOT present a "both join" option, or let both ever be in the party — Linzi and Leliana
are mutually exclusive for the whole story = `.fail 9` if both appear.
⛔ DO NOT auto-resolve — present the two options and WAIT.
⛔ DO NOT offer Linzi at all if Leliana already holds the slot from character selection.

---

## EXIT — TRANSITION TO PR_02

After the player's arrival action resolves (and prisoner handling if applicable):
- Set `current_scene = "prologue_feast"`
- 🚪 PRE-PROLOGUE STATE header DROPS — arc is over when manor is entered
- Load `KM_PR_02_feast_opening.md`
- **NO intermediate scene fires.** Banquet hall is the next location. Period.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_02 (carries forward)

**Your next response after PR_01's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR02:feast-opening]
[RULE_QUOTE: Jamandi's opening address fires AFTER player makes their arrival choice. Mandatory player-choice STOP after the address — do NOT cut to Linzi. Companions are STRANGERS — no names until each introduces themselves. Tartuccio's intro fires only after player has acted post-address.]
```

**Binding constraints from PR_02's RULE_QUOTE:**
- Jamandi's full opening address fires AFTER the player's arrival action — NOT before
- Mandatory STOP after her address; player must respond before the scene continues
- Companions are STRANGERS — even chosen Pick-10 companions have not introduced themselves yet; do NOT use their names in narration before they speak
- Tartuccio's intro fires only after the player has acted post-address (not auto-trigger)

---

*KM_PR_01_manor_arrival.md — Prologue atomic beat 01 | v93.5 (entry-hall attractor removed; 2-stop final)*
