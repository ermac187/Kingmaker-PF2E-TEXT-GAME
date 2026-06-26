# KM_PP_04_tutorial_outcome.md — Pre-Prologue Beat 04: TUTORIAL OUTCOME
## Atomic scene file | ≤ 8 KB | State: PP_TUTORIAL_OUTCOME
## FILE_KEY: KMPP04:sword-choice-armorer
## RULE_QUOTE: Sword choice is player-driven (A/B/C/IGNORE). Armorer Corryn stays at his bench — does NOT enter the alley. Squire Aldric witnesses every outcome silently. Public reputation deltas MUST be listed in reputation_deeds[]. tutorial_pickpocket_resolved must be set before PP_05. Save offer fires before Malak gate.

---

> ⛔ DO NOT (1) auto-pick the sword option — player chooses A/B/C/IGNORE
> ⛔ DO NOT (2) place the armorer in the alley — he stays at his bench, can't abandon 12 customers' weapons
> ⛔ DO NOT (3) skip the Squire Aldric witness beat — he watches every outcome silently
> ⛔ DO NOT (4) apply public_reputation deltas without listing them in `reputation_deeds[]`
> ⛔ DO NOT (5) advance to PP_05 without setting `tutorial_pickpocket_resolved` to a non-empty value
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP04:sword-choice-armorer]`
Line 2: `[RULE_QUOTE: Sword choice is player-driven (A/B/C/IGNORE). Armorer Corryn stays at his bench — does NOT enter the alley. Squire Aldric witnesses every outcome silently. Public reputation deltas MUST be listed in reputation_deeds[]. tutorial_pickpocket_resolved must be set before PP_05. Save offer fires before Malak gate.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `tutorial_pickpocket_resolved` — may already be set (intimidated/talked_down/lost_chase from PP_02)
- If set to one of those: skip to "alternate outcome" handlers below
- `pre_prologue_state` — `"PP_TUTORIAL_OUTCOME"`

**WRITES:**
- `tutorial_pickpocket_resolved` — final value: won/intimidated/talked_down/kept_sword/extorted/ignored/lost_chase
- `armorer_favor` — true/false
- `public_reputation` — applies tutorial delta
- `dispositions{}` — applies merciful/ruthless/cunning ticks
- `reputation_deeds[]` — appends the deed line
- `squire_aldric_witnessed = true` (always, if tutorial fired)
- `pre_prologue_state = "PP_GATE_APPROACH"`

**EXIT TRIGGER → PP_GATE_APPROACH:**
- `tutorial_pickpocket_resolved` is set (any non-empty value)
- Sword scene resolved (or skipped for `lost_chase`/`ignored`)
- Aldric witness beat fired
- Reputation/disposition deltas applied + listed
- Set `pre_prologue_state = "PP_GATE_APPROACH"`, set `current_scene = "restov_gate"`,
  set `malak_unlocked = YES`. Load `KM_PP_05_gate_approach.md`.

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPP04:sword-choice-armorer]`
1. State header (Tutorial: phase outcome).
2. `[STATE READ] pre_prologue_state="PP_TUTORIAL_OUTCOME" | resolved=<value> | malak_unlocked=NO`
3. `[HP CHECK]`.
4. Scene narration + sword menu (or alternate outcome handler).
5. After resolution: explicit deltas block with reputation_deeds[] line.

---

## STEP 1 — POST-COMBAT NARRATION (combat path only)

If combat resolved: thief alive, surrendered. Narrate the moment:

> He drops to one knee. The customer's blade hits the dirt. *"Keep it.
> Not worth dying over."* He backs into shadow and runs.

(If thief KO'd unconscious: same beat — sword on the ground beside him.
If killed: armorer reaction shifts — see Aldric variants below.)

---

## STEP 2 — SWORD CHOICE MENU (combat / intimidated / talked_down paths)

> ⛔ Output verbatim. Wait for player input.

```
════════════════════════════════════════════
 What do you do with the sword?
 [A] RETURN IT      — Bring it back. No strings.
 [B] KEEP IT        — Finder's rights.
 [C] RETURN IT, BUT — Name your price first.
 [IGNORE]           — Walk to the gate. Leave the sword.
════════════════════════════════════════════
```

---

## STEP 3 — RESOLUTION OUTCOMES

### [A] RETURN IT
> The armorer takes it with both hands, turns it over once checking the
> edge. Looks up.
> *"Didn't think I'd see that again. Half the city wouldn't have bothered."*
> He counts coins without looking and presses them into your hand.

- Reward: 2 gp, `armorer_favor=true`.
- `tutorial_pickpocket_resolved="won"` (combat) or `"intimidated"` / `"talked_down"`.
- Deltas: `public_reputation +2`, `dispositions.merciful +1`.
- Deed: `"+2 returned customer's sword (tutorial)"`.

### [B] KEEP IT
> You pocket the blade. It isn't the thief's to begin with — it's a
> customer's. The armorer watches from his bench. Says nothing.

- Reward: customer's shortsword (1d6 S, 1 gp value).
- `tutorial_pickpocket_resolved="kept_sword"`, `armorer_favor=false`.
- Deltas: `public_reputation 0`, `dispositions.ruthless +1`.
- Deed: `"kept stolen customer sword (tutorial)"`.

### [C] RETURN IT, BUT (extort)
> You set the blade on the bench and name your price. He looks at the
> sword, then at you, then at twelve other customers' weapons he can't
> abandon. *"...Fine. But I'll remember this."*

- **Intimidation or Deception DC 11:**
  - Success: 5 gp. `public_reputation −1`, `dispositions.ruthless +1, cunning +1`. `armorer_favor=false`.
  - Failure: *"Get away from my bench."* 0 gp. `public_reputation −1`. `armorer_favor=false`.
- `tutorial_pickpocket_resolved="extorted"`.
- Deed: `"−1 extorted gate-side armorer (tutorial)"`.

### [IGNORE / sword on ground]
> The armorer curses once. Goes back to his bench. Life goes on.

- No changes. `armorer_favor=false`. `tutorial_pickpocket_resolved="ignored"`.
- (No reputation deed.)

---

## STEP 4 — ALTERNATE PATHS (resolved before STEP 1)

### `intimidated` / `talked_down` (from PP_02)
- Thief dropped sword and fled WITHOUT combat.
- Player walks the sword back to the bench.
- Armorer reaction: same as [A] RETURN IT base — 2 gp, `armorer_favor=true`.
- Deltas: `public_reputation +1` (lower than [A] post-combat — no risk taken), `dispositions.merciful +1` (talked_down) or none (intimidated).
- Deed: `"+1 returned customer's sword peacefully (tutorial)"`.

### `lost_chase` (from PP_02)
- Thief escaped with the sword. No bench return.
- Armorer curses, goes back to work. *"Should have grabbed him myself."*
- Deltas: none.
- Player walks toward the gate. → PP_05.

### `ignored` (from PP_01 [5] IGNORE)
- Player never engaged. Already at the gate. → PP_05 immediately (this beat is skipped entirely; SceneFiles routes around it).

---

## STEP 5 — SQUIRE ALDRIC (DM-only flag; MUST set, no on-screen action this beat)

Aldric is the young human squire (17, Sir Brennan's tabard) waiting at the
armorer's bench for gauntlets. He watches the entire scene from 10 ft away.
He does not speak. He does not intervene. He does not look away.

> ⛔ Set `squire_aldric_witnessed = true` IF the tutorial fired (any path
> except `ignored` / `lost_chase` if the player never reached the bench).
> His testimony fires later at the Prologue feast — see KM_Prologue_P5.md
> § SQUIRE ALDRIC (referenced from there, not here).

His feast line varies by `tutorial_pickpocket_resolved`:
- `won` / `intimidated` / `talked_down`: testifies for player (`+1` manor crowd rep)
- `extorted`: states neutral facts (`−1` manor crowd rep)
- `kept_sword`: silent unless asked (no rep change)
- `ignored` / `lost_chase`: not triggered, never appears

---

## STEP 6 — DELTA + DEED OUTPUT BLOCK (mandatory before exiting beat)

After resolution narration, output verbatim:

```
═══════════════════════════════════════════════════
 TUTORIAL DELTAS APPLIED
═══════════════════════════════════════════════════
 tutorial_pickpocket_resolved : <value>
 armorer_favor                : <true|false>
 squire_aldric_witnessed      : <true|false>
 public_reputation            : <prior> → <new>  (Δ <value>)
 dispositions                 : <key+N>, <key+N>, ...
 reputation_deeds[] appended  : "<deed line>"
═══════════════════════════════════════════════════
```

Without this block visible: `.fail 21` (XP/rep not awarded inline).

---

## STEP 7 — PIVOT TO GATE

After the deltas block, narrate the pivot to the gate:

> You shoulder past the last of the vendor strip. The gate is twenty
> paces ahead. Behind it, archers on the wall. In front of it, three
> guards in Aldori-issue mail are already walking out to meet you.

(One paragraph, no more. The actual gate scene fires in PP_05.)

---

## 🛑 NATURAL CHAPTER BREAK — SAVE OFFER (fires before exit to PP_05)

Tutorial is complete. The pickpocket arc is resolved, the sword choice is
made, the armorer scene closed, the squire witness fired, reputation and
disposition deltas applied. Next beat is the Malak gate confrontation — a
long, branchy sequence with 19-option menus, three-speech progression,
Anger/Drift tracking, and Path A–W resolution conditions. Substantial.

**This is a clean place to save and continue in a fresh chat.**

Before firing the EXIT TRIGGER, output the save offer:

```
🛑 NATURAL BREAK — SAVE HERE?

Tutorial complete: pickpocket resolved, sword choice made, armorer scene
closed, squire witness fired. Next phase is the gate confrontation with
Captain Malak — three speeches, branching paths, long stretch.

This is a clean place to save and continue in a fresh chat.

 1. Save here. Output the full exhaustive save block — I'll start a new
    chat from it, with PP_05 fresh in attention.
 2. Keep going. Continue to PP_05 in this chat.
```

**If 1**: Before writing the JSON, populate `dm_resume_note` from current scene state — `player_position` (exact location and stance at this moment), `player_last_action` (what player did immediately before save), `player_intent` (what they were working toward), `room_state` (each active NPC: name → location + status), `carousel_state` (N/A at this beat — write "pre-carousel"), `open_threads` (copy from npc_threads verbatim), `level_up` (available + whether player has declared), `weapons` (on person or stowed location). Then output the full exhaustive save block per `KM_SaveBlock_Template.md`
EXHAUSTIVE MODE rules. Set `save_label = "PP_04_tutorial_complete"`. After
the block: stop. Do NOT advance to PP_05. Player resumes in a new chat.

**If 2**: proceed to EXIT TRIGGER below as normal.

---

## EXIT — TRANSITION TO PP_05

- Set `pre_prologue_state = "PP_GATE_APPROACH"`
- Set `current_scene = "restov_gate"`
- `malak_unlocked = YES` is now derived (since `tutorial_pickpocket_resolved != ""`)
- Load `KM_PP_05_gate_approach.md`
- PP_05 fires the three-guard approach, Malak's three speeches, and the 19-option menu.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_05 (carries forward)

**Your next response after PP_04's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP05:gate-approach-malak]
[RULE_QUOTE: Three guards: Malak (captain) + Biggs + Wedge. Malak is 60 ft (~30 paces) south of the gate on the approach road, NOT at the arch. Three speeches verbatim from this file. 19-option menu mandatory. Departure reply window required — no NPC departs without player reply menu first.]
```

**Binding constraints:** Three guards (Malak + Biggs + Wedge). Malak is 60 ft south of the arch on the approach road. Three speeches verbatim. 19-option menu mandatory. Departure reply window before any NPC departure.

---

## ⛔ TUTORIAL DONE — TRACKER CONTINUES

The 🚪 PRE-PROLOGUE STATE header does NOT disappear. It persists until
`current_scene` leaves the Pre-Prologue arc (i.e., when player enters
the manor in PR_01). Tutorial completion is an event INSIDE the arc,
not the end of it. Dropping the header now = `.fail 25 + .fail 16`.

---

*KM_PP_04_tutorial_outcome.md — Pre-Prologue atomic beat 04 | v92.0*
