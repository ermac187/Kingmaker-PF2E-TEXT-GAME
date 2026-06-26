# KM_PP_01_arrival.md — Pre-Prologue Beat 01: ARRIVAL
## Atomic scene file | State: PP_ARRIVAL
## FILE_KEY: KMPP01:arrival-vendor-strip
## RULE_QUOTE: Opening narration verbatim, fill 8 brackets. Pickpocket trigger fires at end of this beat (vendor strip + hooded thief + customer longsword stolen). 12-day journey, three Aldori riders searching for "the man in red armor," Nivakta's Crossing caravan defense — these are eRmaC's experience, NO NPC knows them.

---

## ⛔⛔⛔ HARD PRE-LOAD GATE — RUN BEFORE ANYTHING ELSE ⛔⛔⛔

**This file is loaded via `!KM_PP_01_arrival.md`. Before outputting the FILE_KEY proof, before narrating ANY arrival content, you MUST check the save block.**

**STEP 0 — Build gate:**

1. Read `save_block.player.build_id`.
2. If `build_id` is empty, missing, `null`, or `"new"`:
   - **STOP. Do NOT narrate the arrival scene. Do NOT output the FILE_KEY line. Do NOT fill brackets. Do NOT load any vendor or thief content.**
   - Output ONLY this directive:
     ```
     ⛔ CHARACTER NOT CREATED YET — PP_01 ABORTED
     save_block.player.build_id is empty. You cannot enter the Pre-Prologue scene without a character.
     Loading build-selection workflow.
     → Load KM_BuildGuide.md and present Step 1 (class menu, 1–27).
     → After class pick, load the matching KM_Builds_*.md file and present builds.
     → After build pick, run KM_CharCreate.md prompts (ancestry → heritage → background → ability boosts → feats → spells → gear).
     → After build_id is written to save_block, the user re-loads !KM_PP_01_arrival.md.
     ```
   - Then STOP. No further output this response.
3. If `build_id` is set (non-empty string like `"Guardian — Flickmace Bodyguard"`):
   - Proceed to FILE_KEY proof + Pre-Narration Checklist + Opening Narration as normal.

**Violation:** narrating PP_01 content while `build_id` is empty = `.fail 9 + .fail 41` (file gate ignored, content fabricated against required state). DM must roll back and re-output the build-selection directive.

This gate fires on EVERY `!KM_PP_01_arrival.md` load, not just first entry. If the user runs the bang command without a character built, they get the build-selection bounce, not the scene.

---

> ⛔ DO NOT (1) advance to tutorial without firing the pickpocket trigger at end of this beat
> ⛔ DO NOT (2) speak/move for the player or skip eRmaC's NAME=eRmaC, GENDER=male defaults
> ⛔ DO NOT (3) leak opening-narration details (12-day journey, riders, Nivakta's road) into NPC dialogue — `.fail 2`
> ⛔ DO NOT (4) substitute `[Player]` for eRmaC or ask for name/gender — both are pre-set
> ⛔ DO NOT (5) load any other beat file in this response — narrate this beat then STOP
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP01:arrival-vendor-strip]`
Line 2: `[RULE_QUOTE: Opening narration verbatim, fill 8 brackets. Pickpocket trigger fires at end of this beat (vendor strip + hooded thief + customer longsword stolen). 12-day journey, three Aldori riders searching for "the man in red armor," Nivakta's Crossing caravan defense — these are eRmaC's experience, NO NPC knows them.]`

Both strings exist ONLY in this file's header. Missing, paraphrased, or wrong = `.fail 9` (file not actually loaded — DM is generating from
memory). The DM cannot fabricate this key from training data — it
exists only in this file.

---

## STATE IO

**READS from save_block:**
- `player.build_id` — **HARD REQUIRED.** If empty/missing → STEP 0 gate above fires, file aborts, build-selection workflow loads. Do not narrate without build_id.
- `current_scene` — should be `"restov_gate"` on first entry
- `pre_prologue_state` — should be `""` (new) or `"PP_ARRIVAL"` (returning)
- `tutorial_pickpocket_resolved` — should be `""` (this beat sets up the tutorial that fills it)

**WRITES to save_block:**
- `current_scene = "restov_gate"`
- `pre_prologue_state = "PP_TUTORIAL_PHASE_A"` (after exit trigger fires)
- Every response: persistent state header (see REQUIRED OUTPUTS)

**EXIT TRIGGER → PP_TUTORIAL_PHASE_A:**
- Tutorial pickpocket trigger has fired (see end of this file)
- Player has acknowledged or made any input after the trigger
- Set `pre_prologue_state = "PP_TUTORIAL_PHASE_A"`, load `KM_PP_02_tutorial_setup.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line** (line 1, above all else): `[FILE_KEY: KMPP01:arrival-vendor-strip]`

1. State header:
   `🚪 PRE-PROLOGUE STATE: Malak Anger 0 | Biggs Drift 0/3 | Wedge: tracks Biggs | Gate Window: open | Tutorial: pending | public_rep 0`

2. `[STATE READ] pre_prologue_state="PP_ARRIVAL" | tutorial_resolved="" | malak_unlocked=NO`

3. `[HP CHECK: no trigger | pool 1/3 | overflow 0]` (or trigger if one fires)

4. ONE paragraph of arrival narration (the bracket-filled OPENING NARRATION below, only on the first response in this beat — subsequent responses in this beat go straight to the tutorial trigger).

5. The TUTORIAL TRIGGER block at the end of this file (only on the first response in this beat).

---

## PRE-NARRATION CHECKLIST (fire once, first PP_ARRIVAL response)

> ⛔ Fill all 6 before narrating. Skipping = `.fail 9`.

```
1. ☐ build_id confirmed from save_block.player.build_id
2. ☐ KM_PrePrologue_Setup.md row read — 8 brackets copied
3. ☐ KM_PrePrologue_Setup.md armor material confirmed
4. ☐ KM_Exploration.md ⚗️ Exotic Materials read for weapon + armor
5. ☐ Save [primary weapon] + [secondary weapon/tool] for PP_05 (Malak's line)
6. ☐ tutorial_pickpocket_resolved == "" — proceed to TUTORIAL TRIGGER
```

---

## OPENING NARRATION — VERBATIM, FILL 8 BRACKETS

> NAME=eRmaC. GENDER=male. He/him. Do NOT ask. 12-day journey + Aldori
> riders + Nivakta's Crossing are eRmaC's experience — no NPC knows.

```
The road to Restov stretches ahead — packed earth worn smooth by countless
caravans, refugees, and fortune-seekers. You have walked for 12 days since
the invitation caught up with you — three riders in Aldori colors, moving
fast, asking at every waystation and village for "the man in red armor."
They found you on a quiet stretch of road and delivered a sealed letter from
Lady Jamandi Aldori without further explanation beyond that she had heard
what happened on the trade road outside Nivakta's Crossing — where you had
been defending caravans for food, blankets, shelter, and the occasional
coin — and wanted to meet you. You asked no questions. You already knew
what road you were walking.

The city rises before you now: thick timber gates reinforced with iron,
stone walls that speak of old Brevoy ambition, and guard towers manned by
archers.

The east gate is busy the way a trading city's gate is always busy — loud,
slow, and faintly irritable. A caravan of four wagons sits stalled in the
road, oxen stomping, drivers arguing in low voices. A cluster of pilgrims
in Erastil's colors waits to one side. Street vendors have claimed every
foot of wall space along the approach — a woman with a clay oven turning
out flatbread, a man with a river-fish cart, an old man selling roasted
nuts over coals, and a girl no older than fourteen with a tray of meat pies
she hawks in a voice twice her size. Perched on an overturned crate near
the wall, slightly apart, is a halfling woman with a battered notebook open
across her knees. She is writing with complete focus. She is the only person
in the crowd facing the gate rather than away from it. Two boys cut through
the crowd selling water at prices that only make sense when you have been
standing in line for an hour. The gate itself is open — it is always open
during the day — but the flow of traffic has slowed because someone is
holding it up.

You are eRmaC — a [Ancestry] [Class] — [Subclass/Archetype]. Nothing you
carry belongs to this world. Your armor — [armor description] — is deeply
worn: dented, scratched, and scarred as though you have absorbed the blows
of a hundred campaigns. Your [primary weapon] carries the same alien
signature — forged by hands that understood metal differently than anyone
in Golarion ever has. Your [secondary weapon or tool] matches the set.
Every piece was made in Aerynth, and no smith on this continent has ever
seen work like it. [Physical scars or marks] crawl across your [body
locations]. [Environmental wear] clings to your clothing. A single folded
parchment — Lady Jamandi Aldori's letter of introduction — rests inside
your [location on person], the only proof you belong anywhere near this
charter ceremony.

Everything here is almost right — but not quite. The sky is the wrong blue.
Voices land a beat late.

The people closest to you notice your armor. The ones who know what armor
looks like take a half step back. The ones who don't stare openly. You
have had this experience before. You keep moving.
```

> ⛔ Do NOT continue past this paragraph into Malak content. The next beat
> for this response is the TUTORIAL TRIGGER below — fire it, then STOP.

---

## TUTORIAL TRIGGER (fire at end of first PP_ARRIVAL response — required)

```
Among the food vendors along the approach road — between the flatbread
woman and the nut roaster — a mobile armorer has wedged his cart into the
vendor strip. Grinding wheel bolted to the cart bed, portable forge
breathing low coals, leather repair kit hanging open at his hip. His
worktable is crowded with other people's gear: swords left for sharpening,
a dented breastplate waiting to be hammered out, a haubergeon with a split
ring. He is not a stall you can walk away from. All of it belongs to
someone else.

A hooded figure shoves through the crowd shoulder-first — fast, purposeful,
a longsword in hand they didn't arrive with. The armorer half-rises, can't
follow: "That blade's a customer's — someone stop them!"

The thief is already threading into the crowd ahead.
```

> ⛔ Cloaked thief — neutral pronouns until class pick. See PP_02 Gate 7.

> ⛔ **RULE 9 (KM.txt) — 10–30 OPTIONS.** This is an in-game scene menu; it
> MUST offer 10+ options or `.fail 3`. Output ALL of the below. The chase
> approaches ([1]–[4],[6]–[8],[10]) resolve into PP_02; the quick reads
> ([9],[11],[12]) are free looks (thief still in sight) that RETURN to this
> menu. Use only on-scene people/things — armorer (Corryn), the crowd
> (bread woman, nut-seller, water boys), the silver-haired harper, the gate
> guards ahead, the stalls. Invent nothing (`.fail 9`).

```
══════════════════════════════════════════════════════
 [1]  PURSUE   — Close the gap through the crowd (Athletics / Acrobatics)
 [2]  CUT OFF  — Read where they're heading and get there first (Perception / Warfare Lore)
 [3]  SHOUT    — Command them to stop, loud enough for the crowd to hear (Intimidation)
 [4]  APPEAL   — Call on bystanders to block their path (Diplomacy / Society)
 [5]  IGNORE   — Not your problem. Continue to the gate.
 [6]  DRAW + CHASE — Weapon out, pursue with intent, not just speed.
 [7]  TACKLE   — Bull through the bodies and seize them (Athletics to shove).
 [8]  HURL SOMETHING — Grab off the nearest stall, throw to stagger them (improvised, Athletics).
 [9]  ASK THE ARMORER — "Which way? You know this one?" Fast intel before you move.
 [10] FLAG THE GATE GUARDS — Point them out to the Aldori mail at the arch; let the gate cut off the run.
 [11] MARK THEM — Fix the gait, the cloak, the blade (Perception) so you can find them if they vanish.
 [12] READ THE CROWD — Who flinches, who clears a path; see where they're being funneled.
 [13] CUSTOM   — Handle it your own way.
══════════════════════════════════════════════════════
```

---

## EXIT — TRANSITION TO PP_02

After player input on the pickpocket menu (10+ options per Rule 9):
- Set `pre_prologue_state = "PP_TUTORIAL_PHASE_A"`
- Set `current_scene = "restov_tutorial_pursuit"`
- Load `KM_PP_02_tutorial_setup.md`
- That beat resolves the approach roll + class pick + reveal.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_02 (carries forward)

**Your next response after PP_01's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP02:tutorial-hood-up]
[RULE_QUOTE: Hood is UP — no gender, no he/him/she/her, no face/build/voice description until class is picked. Gate 5 (gender) is a PLAYER MENU, not a DM dice fake. Class pick + reveal must fire BEFORE combat or sword choice.]
```

**Binding constraints:** Hood is UP — no thief description until class is picked. Gate 5 (gender) and class menu are both PLAYER MENUS. Class pick + hood reveal must fire before any combat.

If player picked [5] IGNORE:
- Set `tutorial_pickpocket_resolved = "ignored"`
- Set `pre_prologue_state = "PP_GATE_APPROACH"` (skip PP_02-04 entirely)
- Set `current_scene = "restov_gate"`
- Load `KM_PP_05_gate_approach.md`

---

*KM_PP_01_arrival.md — Pre-Prologue atomic beat 01 | v92.0*
