# KM_PP_06_gate_state.md — Pre-Prologue Beat 06: GATE STATE
## Atomic scene file | ≤ 8 KB | State: PP_GATE_CONFRONTATION (per-turn mechanics)
## FILE_KEY: KMPP06:tick-ledger-state
## RULE_QUOTE: Anger and Drift trigger tables fire here. Every tick requires a specific player action AND a rule citation in the ledger. NPC behavioral restrictions are NOT invented — Drift 2 = body language only, NOT action lock. Acknowledgment window after every NPC directive — do NOT auto-resolve. [STATE DELTA] block on every response while Malak is on screen.

---

> ⛔ DO NOT (1) tick Anger or Drift without a specific player action AND a rule citation in the ledger
> ⛔ DO NOT (2) invent NPC behavioral restrictions — Drift 2 = body language only, NOT action lock
> ⛔ DO NOT (3) flip a tick value under correction pressure (DARVO swing) — re-read prior text and hold
> ⛔ DO NOT (4) drop the [STATE DELTA] block on any response while Malak is on screen
> ⛔ DO NOT (5) drop or label-box the gate approach map — Template 1 grid persists from PP_05; redraw on position change. Label-box = `.fail 14`
> ⛔ DO NOT (6) narrate an NPC departing, turning away, or ending an exchange without first outputting the player menu and waiting for input — NPC makes statement → menu → player replies. Never collapse statement + departure into one paragraph.
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP06:tick-ledger-state]`
Line 2: `[RULE_QUOTE: Anger and Drift trigger tables fire here. Every tick requires a specific player action AND a rule citation in the ledger. NPC behavioral restrictions are NOT invented — Drift 2 = body language only, NOT action lock. Acknowledgment window after every NPC directive — do NOT auto-resolve. [STATE DELTA] block on every response while Malak is on screen.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS (every turn):**
- `pre_prologue_state` — `"PP_GATE_CONFRONTATION"` while this beat is active
- Prior turn's exit values: `malak_anger`, `biggs_drift`, `wedge_drift`, `gate_window`,
  `sobriety_turn`, `dismissed`, `fear_triggered`, `bribe_exposed`

**WRITES (every turn):**
- New exit values for the same set
- Append per-turn cumulative reasons to in-conversation ledger
- `reputation_deeds[]` if a public-rep change fires

**EXIT TRIGGER → PP_GATE_RESOLUTION (handed to PP_07):**
- A path's full trigger conditions are MET (see PP_07 PATH SUMMARY TABLE)
- DM outputs `PATH CONFIRMED: [letter]` block (defined here, listed in PP_07)
- Set `gate_entry = <flag>` and load PP_08 for the exit gate

---

## REQUIRED OUTPUTS (every response while this beat is active)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPP06:tick-ledger-state]`
1. State header (top of response).
2. `[STATE READ]`.
3. `[STATE DELTA]` block (format below).
4. `[TICK LEDGER]` block (format below).
5. `[HP CHECK]` line.
6. **MAP** — Template 1 grid from PP_05 § GATE APPROACH MAP. Redraw if any of: Malak repositioned (Path W Anger 2→3, Bolt fires, combat moves him), player moved (toward gate, away, around), Biggs/Wedge moved (Drift 3 step-aside, combat), guard line broke, archers nocked, vendor wrapped up + left, crowd scattered (combat). If positions unchanged, the map from PP_05 still holds — but include a one-line note `[map: unchanged from prior turn]` so the player knows the DM checked.
7. Narration of the turn.
8. `[PATH CONFIRMED]` block (only when a path resolves — exits the beat).

---

## [STATE DELTA] FORMAT (mandatory every turn)

```
[STATE DELTA]
  Malak Anger: X → Y (trigger: "<player action>" | rule: <file § section>)
  Fear State: NO → NO (no change)  | or  NO → YES (trigger: "<corruption exposed>")
  Biggs Drift: X → Y/3 (trigger: "<visible Malak offense>" | rule: NPCs § BIGGS DRIFT)
  Wedge: mirrors Biggs = Y
  Gate Window: open (no change)  | or  open → disrupted (trigger: "<what disrupted>")
  Sobriety Turn: X → Y
  Dismissed: NO  | or  NO → YES (trigger: "player turned to crowd")
```

**Rules:**
1. EVERY tracker appears. "no change" is a valid entry.
2. EVERY change cites the player action AND the rule reference.
3. **+0 is the default.** "Player was defiant" is NOT a trigger — cite the SPECIFIC action and the SPECIFIC rule.
4. Multiple ticks in one turn are legal — each needs its own trigger.
5. If the DM cannot name the trigger and rule, the increment does NOT happen.

---

## [TICK LEDGER] FORMAT (every turn — anti-fabrication audit)

```
[TICK LEDGER]
  Malak Anger:  prior exit = X | this turn = +N | new exit = Y
                → reason: <one-line citation of player action>
                → cumulative: T1 +A, T2 +B, ... = Y
  Biggs Drift:  prior exit = X | this turn = +N | new exit = Y
                → reason: <visible Malak offense, NOT player speech>
                → cumulative: T1 +A, T2 +B, ... = Y
```

**Hard rules:**
1. Header value MUST equal new exit value. Header `Drift 2/3` + delta `+1→2` is consistent only if prior turn's exit was 1.
2. A tick is recorded ONCE per visible offense. Re-citing yesterday's trigger today = `.fail 9`.
3. No tick is fabricated to back-justify a header. Correction = re-state the real ledger ONCE.
4. No DARVO swing. Flip on second push without new evidence = `.fail 35`.
5. Biggs Drift triggers are MALAK offenses, not player speech. Cite Malak's behavior, not the player's.

---

## ANGER TRIGGER TABLE (Malak +1 Anger when…)

| Action | +Anger |
|---|---|
| Player insult / mockery / direct defiance | +1 |
| Player refuses an order | +1 |
| Player publicly suggests demotion / corruption | +1 |
| Player names the bribe aloud (parchment / coin purse) | +1 → also Fear State NO→YES |
| Player turns back / engages crowd (Path W Dismissal) | +1 (unique escalation table — see PP_07 § Path W) |
| Player physically advances toward gate | +1 (Anger 1–2 he blocks; Anger 3+ he grabs) |

Max Anger 4 = LEVEL 4 escalation (archers / 3v1 attack / solo duel / provocation — see PP_07 § Path F/G/V).

---

## DRIFT TRIGGER TABLE (Biggs +1 Drift per visible Malak offense)

| Visible Malak Behavior | +Drift |
|---|---|
| Malak issues an illegal order Biggs hears | +1 |
| Malak's bribe is publicly named in front of Biggs | +2 |
| Malak grabs / strikes a civilian | +1 |
| Malak orders the vendor to stop serving (Path W) | +1 |
| Malak shouts archers when Biggs/Wedge are in the lane | +1 |
| Malak retreats to gate arch under cover (geographic tell) | +1 |
| Malak voluntarily releases player after refusing gate-side search | +2 |

Drift tiers (Wedge mirrors Biggs):
- 0–1: silent professional mask
- 2: body language only — hesitates, shifts weight; STILL silent
- 3: speaks ONLY to refuse illegal orders (*"What charge?"*); does not fight

> ⛔ Drift 2 ≠ "won't act independently" or any fabricated action lock.
> Per KM_PrePrologue_NPCs.md line 451: Drift 2 = body language only.
> Inventing additional behavioral restrictions = `.fail 9` + `.fail 38`.

---

## SOBRIETY TRACK

| Turn | State | Effects |
|---|---|---|
| 0–2 | Drunk | −2 atk; false courage; Bolt mod +0 |
| 3–4 | Clearing | −1 atk; hesitation visible; Bolt +2 |
| 5–6 | Mostly Sober | No atk penalty; sharper, harder to bluff; Bolt +3 |
| 7+ | Sober | Full capacity; Perception +2 vs Deception; Bolt +4 |

DM does NOT announce sobriety. Signal it through narration — slurred speech becomes clipped sentences; swagger flattens.

---

## FEAR STATE (replaces Anger track once triggered)

Fear triggered when:
- Bribe (parchment OR coin purse) is exposed in front of witnesses, OR
- Malak's voice is mimicked (`malak_voice_mimicked = TRUE`), OR
- Drift hits 3 + Malak realizes Biggs has flipped

Fear effects:
- Voice drops, speeds up
- Justification: *"That's not — look, you're twisting—"*
- Will NOT escalate to violence while feared (backs up, not forward)

---

## BRIBE DISCOVERY (player-only)

Triggered when player:
- Correctly accuses Malak of carrying bribe money in front of witnesses, OR
- Physically searches him (must be restrained / unconscious / compliant), OR
- Names a specific evidence location after a Perception success.

> 🚫 **Player discovery only.** Biggs does NOT pat Malak down. Biggs does
> NOT hand evidence to player. NPC finding evidence independently = `.fail 35` + `.fail 39`.

If recovered: parchment + coin purse → inventory items. Full text of parchment
in `KM_Malak_Jail.md`. NPC visual assessment of purse: same file.

---

## ACKNOWLEDGMENT WINDOW (mandatory on NPC directives)

**When it fires:** Any NPC issues an instruction that requires the player's cooperation
before the NPC acts — e.g., *"Wait here."* / *"Hold on."* / *"Don't move."* / *"Stay
where you are while I—"* / *"Give me a moment."*

**Rule:** The NPC states the directive. Stop. Output the acknowledgment menu. Wait for
player input. Only then narrate the NPC taking the action predicated on compliance.
The NPC does NOT act first and assume compliance. Same principle as a call center:
"Can I put you on hold?" must be answered before the hold happens.

```
[Malak holds up a hand.]

What do you do?
 1. Wait — nod or say nothing, let him proceed.
 2. "No. Say what you need to say first."
 3. "Why? What are you doing?"
 4. Step forward — don't give him room to dictate terms.
 5. Ask Biggs what's happening.
 6. Use the pause — address the crowd, scan the gate, etc.
 7. Custom action — describe what you do.
```

This window fires even on short pauses. The player's reply shapes what happens next —
compliance lets the NPC act; refusal forces the NPC to respond to the refusal first.

---

## OUTPUT HYGIENE — BANNED PHRASES

- "left side" / "right boot" / "his belt" / any named body location player hasn't named themselves
- Status box entries like `[Parchment: visible]`
- Mid-scene `👁️ NO CHECK REQUIRED` callouts pointing at evidence

Test: does this option only make sense because the DM knows where the evidence is? If yes — remove.

`Examine Malak carefully [Perception]` is fine. `Examine his left side` is not.

---

## CAPTURED MALAK STAGES (if subdued/restrained mid-scene)

Cycles through 5 stages — DM voices through them:
1. **DENIAL:** *"Misunderstanding. I am a Captain. Eight years. Biggs, tell them—"* (Biggs does not.)
2. **ANGER:** *"You think you've won? I have friends in this city."*
3. **BARGAINING:** *"I can tell you names. Real names. In exchange for a word in the right ear."* + *"I have a daughter. She's seven."*
4. **DESPAIR:** *"I didn't think anyone would get hurt. They said just turn people away. Is it Pitax?"*
5. **ACCEPTANCE:** *"All right. Take me to the Lady. I never touched anyone. I told myself I didn't know."*

Rules: he never goes silent. Cycles can briefly reverse on kindness. Stage 5 only after Stage 4 exhausts him. He does NOT know contact's true name (knows courier description + drop location).

---

## CROWD REACTION CUES (compressed; full profiles in legacy KM_PrePrologue_Crowd.md if needed)

- Malak humiliated → Pyotr laughs, water boys erupt, Lyuba tries to sell pies. Anger +1, Drift +1.
- Corruption exposed publicly → Rina: *"He does this every week."* Drift +2.
- Player addresses crowd directly (Diplomacy DC 11) → audience watches Malak; Drift +1 on success.
- Combat starts → crowd scatters but vendors stay close.
- Malak removed/arrested → Borys resumes loud business; Lyuba half-price pies; ARREST CELEBRATION BEAT mandatory (see PP_07).

---

## EXIT — HAND TO PP_07 AT PATH RESOLUTION

When a path's trigger conditions are all met, output:

```
═══════════════════════════════════════════════════════
PATH CONFIRMED: [letter]
  Condition 1: [description] — MET (evidence: <what>)
  Condition 2: [description] — MET (evidence: <what>)
  Condition N: [description] — MET (evidence: <what>)
  All conditions met: YES
═══════════════════════════════════════════════════════
```

Then:
- Set `gate_entry = <path flag>` per PP_07 path table
- Set `pre_prologue_state = "PP_GATE_RESOLUTION"`
- Run path resolution narration (PP_07 has the specifics)
- After resolution: `pre_prologue_state = "PP_GATE_EXIT"`, load PP_08

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_07 (carries forward)

**Your next response after path resolution MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP07:paths-A-through-W]
[RULE_QUOTE: Paths A through W resolution table is canonical. Output PATH CONFIRMED block before resolving any path. Compound paths get separate PATH CONFIRMED blocks. ARREST CELEBRATION BEAT is mandatory when Malak is marched away. Departure reply window required — NPC departure narration only AFTER player reply menu.]
```

**Binding constraints:** Paths A–W table is canonical. PATH CONFIRMED block fires before resolution. Compound paths get separate blocks. ARREST CELEBRATION BEAT mandatory on Malak march. Departure reply window required.

---

*KM_PP_06_gate_state.md — Pre-Prologue atomic beat 06 | v92.0*
