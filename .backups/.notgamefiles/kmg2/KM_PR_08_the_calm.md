# KM_PR_08_the_calm.md — Prologue Beat 08: THE CALM AFTER
## Atomic scene file | ≤ 8 KB | State: PR_08_THE_CALM
## FILE_KEY: KMPR08:the-calm
## RULE_QUOTE: Phase 4.5 player-triggered ONLY — no candles-burn-low or scene-winds-down auto-advance. No uninvited Tartuccio sits. Declared+titled companions do NOT initiate while ⏳ Waiting companions exist. Tartuccio circulates within the hall, never out of it. Save offer fires before accusation.
## LOOKUP: KM_Prologue_P2_B.md (full companion approach scripts + commitment close lines)

---

> ⛔ DO NOT (1) skip or compress Phase 4.5 — the player earned this stillness; do not rush to Phase 5
> ⛔ DO NOT (2) let Tartuccio sit without being invited — no uninvited sits (`.fail 17`)
> ⛔ DO NOT (3) let a declared+titled companion initiate dialogue while ⏳ Waiting companions exist (`.fail 17`)
> ⛔ DO NOT (4) let Tartuccio leave the hall — he circulates WITHIN it, not out of it (`.fail 17`)
> ⛔ DO NOT (5) fabricate "mandatory Phase 4.5 moments" — mandatory Tartuccio moments are Phases 1–3 only (`.fail 38`)
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR08:the-calm]`
Line 2: `[RULE_QUOTE: Phase 4.5 player-triggered ONLY — no candles-burn-low or scene-winds-down auto-advance. No uninvited Tartuccio sits. Declared+titled companions do NOT initiate while ⏳ Waiting companions exist. Tartuccio circulates within the hall, never out of it. Save offer fires before accusation.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `battle_resolved = TRUE`
- `poison_reported`, `shapeshifter_identified_at_feast`
- `companions_selected` — all chosen companions need Phase 4.5 scenes
- Recruitment flags from PR_06: `tika_recruited`, `morrigan_recruited`, `tatsumaki_recruited`, `artoria_recruited`
- `feast_approval{}` from PR_03

**WRITES:**
- `kitchen_report_delivered = TRUE` (if applicable)
- `shapeshifter_confirmed_at_debrief = TRUE` (if shapeshifter_identified_at_feast = TRUE)
- `companion_committed{}` — per companion
- `companion_titled{}` — per companion
- `phase45_complete = TRUE` on exit

**EXIT TRIGGER → PR_09_accusation:**
- Player signals readiness OR Tartuccio begins moving toward Phase 5
- Load `KM_PR_09_accusation.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR08:the-calm]`
1. `[STATE READ] current_scene="prologue_hall" | phase=PR_08_THE_CALM`
2. `[CAROUSEL 4.5]` — ✅ Spoke / ⏳ Waiting list + tartuccio_clock + current companion
3. `[HP CHECK]`
4. Scene narration
5. Player menu

---

## KITCHEN REPORT — FIRES FIRST (mandatory if `poison_reported = TRUE`)

**This scene fires before any companion approach.**

> *Kesten crosses the hall toward Jamandi. He says something brief. She listens without expression, asks one question, and he answers. Then she looks across the room — at you.*

**Jamandi** *(approaching the player directly, not addressing the room)*: *"The kitchen. You were right."*

**Jamandi:** *"Wine casks dosed through the service entrance. If you hadn't moved when you did, everyone in that hall would have been on the floor when they arrived."* A pause. *"I don't say that lightly."*

> *She returns to Ezvanki and Kassil without waiting for a response.*

Set `kitchen_report_delivered = TRUE`.

- If `shapeshifter_identified_at_feast = TRUE`: Kesten adds shapeshifter detail. `shapeshifter_confirmed_at_debrief = TRUE`

---

## PHASE 4.5 — TARTUCCIO HARASSMENT RULES

**Every 2 player inputs** — Tartuccio fires. ONE exchange per clock cycle, then MUST withdraw.

**Rhythm:**
1. Clock fires → Tartuccio approaches
2. One remark, question, or observation
3. Player responds (or doesn't)
4. **Tartuccio withdraws** — refills wine, circles to his table, steps back WITHIN the hall
5. Gap opens → next companion in queue approaches into that space
6. Companion scene runs to completion (Tartuccio clock is PAUSED while scene is active)
7. Scene closes → Tartuccio clock resets from that moment

**One exchange = done:** question + answer | statement + reaction | monologue with no response (he exits — no second attempt this slot).

**⛔ CORRIDOR BAN ≠ WITHDRAWAL CONFLICT:**
Ban = cannot leave the hall. Withdrawal = steps back within it. Both apply simultaneously.

**⛔ NO UNINVITED SIT.** Player must explicitly say yes before Tartuccio sits down.

**Violations (`.fail 17`):**
- Tartuccio delivers a second question before next clock cycle
- Withdrawal gap exists but no companion fills it
- Tartuccio clock ticks during an active companion scene
- Tartuccio exits the hall for more than 1 player input

---

## PHASE 4.5 — QUEUE FAIRNESS RULES

**Rule 1 — ✅ Spoke yields to ⏳ Waiting:**
Any companion with ✅ Spoke does not take another turn until every ⏳ Waiting companion has had at least one scene. No second approaches while others are waiting. `.fail 17` to violate.

**Rule 2 — Declared + Titled = Silent:**
After a companion commits AND receives a title:
- No unsolicited questions or interjections
- No agenda-pushing, no filling silences
- Respond only if player directly addresses them — one beat, then quiet
- They stay physically present in the player's orbit (they do NOT leave the hall)
`.fail 17` if a declared/titled companion initiates dialogue while ⏳ Waiting companions remain.

---

## COMPANION APPROACH SCENES

**The setup:** Danger is over. Jamandi has thanked the player and returned to conference with Ezvanki and Kassil at the far end. Companions come to the player — the player stays stationary. People drift to them.

**Order:** Tika finds the player first → Linzi next → then carousel in Perception initiative order.

**⛔ EARSHOT SCORING:** ALL companions in earshot score relationship shifts (−2 to +2) from EVERY player statement — not just statements aimed at them.

**⛔ GATHER RULE:** Companions approach the player, not the reverse. Player does not circulate. *Early:* 2–3 nearby. *Mid:* 5–6 gathered. *Late:* all present in orbit.

**Commitment thresholds:**
- +4 feast approval reached → `companion_committed = TRUE` (already declared; close line is a formality)
- Phase 4.5 scene completed + close line fired → `companion_committed = TRUE`
- All 11 chosen companions are ALWAYS with the player at the Phase 5 split. The close lines prove the outcome was earned.

> **LOOKUP:** Full approach scripts for all 11 companions → `KM_Prologue_P2_B.md`
> Covers: Tika / Linzi / Tartuccio / Artoria / Tatsumaki / Morrigan / Goldmoon / Sucrose / Ryuko / Olivier / Yoko / Kyoko
> Also in `KM_Prologue_P2_B.md`: commitment close lines for all 11, the window scene (player stays quiet)
> WotR QL companions (Lann / Ember / Daeran / Nenio / Regill / Arueshalae / Seelah) → fire only if `wrath_ql_enabled = TRUE`

---

## ENDING PHASE 4.5

> ⛔ DO NOT describe candles dimming, the hour being late, servants cleaning, or any
> ambient signal that the evening is winding down. The scene does not end until the
> player ends it. This is ULTRA-PRIORITY in KM_B.txt § NEVER ADVANCE TIME.

**Phase 5 triggers ONLY when:**
- The player explicitly says they are ready, done, or signals to move on, OR
- The player types `.continue`

**Tartuccio does NOT move to trigger Phase 5.** He circulates within the hall on his
clock. He does not get to end the evening by stepping forward. If all companion scenes
are complete and the player is still engaging, NPCs continue to be available. The NPC
Initiative System keeps the scene alive — another NPC approaches.

**When the player signals readiness**, THEN output:

> *Tartuccio smooths his jacket. Steps toward the center of the room.*

**Phase 5 begins.**

---

## 🛑 NATURAL CHAPTER BREAK — SAVE OFFER (fires before exit to PR_09)

Phase 4.5 is complete. Companion approaches resolved, individual
conversations closed, the calm has held as long as it can. Next beat is
the accusation — Tartuccio's claim, the six-proof rebuttal sequence,
Malak's fate, the charter signing, the Pre-Prologue arc closes here.
Substantial content with multiple high-stakes branches.

**This is a clean place to save and continue in a fresh chat.**

Before firing the EXIT TRIGGER, output the save offer:

```
🛑 NATURAL BREAK — SAVE HERE?

Phase 4.5 complete: companion approaches resolved, individual
conversations closed. Next phase is the accusation — Tartuccio's claim,
six-proof rebuttal, charter signing. Long, branchy stretch.

This is a clean place to save and continue in a fresh chat.

 1. Save here. Output the full exhaustive save block — I'll start a new
    chat from it, with PR_09 fresh in attention.
 2. Keep going. Continue to PR_09 in this chat.
```

**If 1**: Before writing the JSON, populate `dm_resume_note` from current scene state — `player_position` (exact location and stance at this moment), `player_last_action` (what player did immediately before save), `player_intent` (what they were working toward), `room_state` (each active NPC: name → location + status), `carousel_state` (turn + which NPC fired + approval score + tartuccio_clock), `open_threads` (copy from npc_threads verbatim), `level_up` (available + whether player has declared), `weapons` (on person or stowed location). Then output the full exhaustive save block per `KM_SaveBlock_Template.md`
EXHAUSTIVE MODE rules. Set `save_label = "PR_08_calm_complete"`. After
the block: stop. Do NOT advance to PR_09. Player resumes in a new chat.

**If 2**: proceed to EXIT TRIGGER below as normal.

---

## EXIT — TRANSITION TO PR_09

Only when player explicitly signals readiness:
- Set `phase45_complete = TRUE`
- Load `KM_PR_09_accusation.md`

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_09 (carries forward)

**Your next response after PR_08's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR09:accusation-exit]
[RULE_QUOTE: Six proofs on Prologue exit: XP audit + XP total + state final + save block (v1.7 exhaustive, 48 root keys) + wait-for-continue + next-scene declaration. Skipping any = cascade abandonment, .fail 16 + .fail 21 + .fail 9 STACKED.]
```

**Binding constraints:**
- PR_09 is the Prologue six-proof exit gate — same structure as PP_08 but for the Prologue arc
- All six proofs must fire in ONE response (XP audit, XP total, state final, save block, wait-for-continue, next-scene declaration)
- Skipping any proof = cascade abandonment (.fail 16 + .fail 21 + .fail 9 stacked)
- Six-proof gate is the strongest load mandate in the architecture — honor it

---

*KM_PR_08_the_calm.md — Prologue atomic beat 08 | v92.0*
