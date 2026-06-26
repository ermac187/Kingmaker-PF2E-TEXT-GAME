# KM_PR_02_feast_opening.md — Prologue Beat 02: FEAST OPENING
## Atomic scene file | ≤ 8 KB | State: PR_02_FEAST_OPENING
## FILE_KEY: KMPR02:feast-opening
## RULE_QUOTE: Jamandi's opening address fires AFTER player makes their arrival choice. Mandatory player-choice STOP after the address — do NOT cut to Linzi. Companions are STRANGERS — no names until each introduces themselves. Tartuccio's intro fires only after player has acted post-address.
## Pair-load: KM_Prologue_Tartuccio.md (Tartuccio behavior scales)

---

> ⛔ DO NOT (1) fire Jamandi's address before the player makes an arrival choice (that is PR_01's job)
> ⛔ DO NOT (2) cut directly to Linzi after Jamandi speaks — mandatory player-choice stop first
> ⛔ DO NOT (3) use companion names not yet introduced — all chosen companions are STRANGERS here
> ⛔ DO NOT (4) fire Tartuccio's intro before the player has acted after Jamandi's address
> ⛔ DO NOT (5) hint at assassination or kitchen poison — player discovers this, not DM exposition
> ⛔ DO NOT (6) fire any "private debrief with Jamandi" scene before this beat — there is no such scene; player arrives directly in the banquet hall from PR_01 (see PR_01 NO INTERPOLATED PRIVATE SCENE block)
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR02:feast-opening]`
Line 2: `[RULE_QUOTE: Jamandi's opening address fires AFTER player makes their arrival choice. Mandatory player-choice STOP after the address — do NOT cut to Linzi. Companions are STRANGERS — no names until each introduces themselves. Tartuccio's intro fires only after player has acted post-address.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `current_scene = "prologue_feast"` (set by PR_01)
- `arrived_with_kassil`, `kesten_respect` — for optional recognition in player menu

**WRITES:**
- `knowledge_world_dc9_passed = TRUE` (if player passes check during Tartuccio intro)
- `tartuccio_wine_observed = TRUE` (if player passes Perception DC 17)
- `feast_opened = TRUE` on exit

**EXIT TRIGGER → PR_03_feast_circuit:**
- Jamandi's address has fired, player has responded
- Linzi and Tartuccio intros have fired (or have been skipped by player choice)
- Load `KM_PR_03_feast_circuit.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR02:feast-opening]`
1. `[STATE READ] current_scene="prologue_feast" | phase=PR_02_FEAST_OPENING`
2. `[HP CHECK]`
3. Scene narration
4. Player choice menu (minimum 10 options)

---

## JAMANDI'S OPENING ADDRESS
*(Fires when: player waits, finds a position, or Jamandi calls the room to attention. NOT automatic on entry.)*

**Jamandi:** *"You have come because I invited you. And I invited you because the Stolen Lands require something specific — not mercenaries, not soldiers, not political appointments. Heroes. People who can look at a land no one else wants and see something worth building.*

*The Stag Lord holds the Stolen Lands through fear and force. He is not unique in that. What is unique is that someone must take them back — and hold them. Not for a season. For generations.*

*The charter I am offering grants you legal authority to claim territory, establish settlements, and govern as you see fit — within Brevoy's broader laws. It is not a small thing. Most of you will fail. Some of you may die. None of you will find it easy.*

*The question I am answering tonight is simple: which of you is worth the charter?"*

> *She sits. The room is quiet.*

**⛔ MANDATORY STOP — DO NOT CUT TO LINZI. DO NOT ADVANCE THE SCENE.**
Present the player's choice menu and wait. Minimum 10 options: respond to Jamandi directly, approach her at the head table, address another guest, study the room, look for someone specific, observe, custom action.

---

## PHASE 1 NPC REACTIONS — PLAYER ENTRANCE

Fire as ambient one-liners when the player enters. Only fire for `companions_selected = TRUE` companions. Skip unchosen.

> Artoria's hand stills on her pommel. Goldmoon sets down her teacup. Linzi gasps and abandons her notebook mid-sentence. Sucrose nearly drops the leaf she was studying. Tika looks up from her plate, fork halfway. Ryuko grins fiercely from the pillar. Olivier's posture squares without a sound. Yoko lowers her glass. Kyoko's notepad flips open to a fresh page. Morrigan's eyebrow arches. Tatsumaki floats half an inch higher.

---

## LINZI INTRODUCTION
*(Fires when player is in a socially neutral position — not mid-conversation with Jamandi)*

**Linzi:** *(notebook already open, pen already moving)* *"You're [character name]! I've been waiting — I heard about what happened at the gate, and — well, I've already started chapter one actually, I hope that's all right — I'm Linzi, I'm a bard, I chronicle things, heroic things specifically, and you are absolutely — I mean the ARMOR alone — can I follow you? I'm very useful. I can heal, I can inspire, I know twelve ballads about the Stolen Lands and none of them are accurate yet but that's going to change—"*

---

## TARTUCCIO INTRODUCTION
*(Within first player turn, after Jamandi's address)*

**Tartuccio:** *(charming, theatrical)* *"[Character name]. What a delight. I am Tartuccio — scholar, sorcerer, rival charter claimant. May the Stolen Lands prove kind to bold souls like us."*

**Perception DC 14:** Jamandi watches. Posture coiled — ready to step back. She responds to player's reaction via body language only.

**Tartuccio responds to player tone:**
- Warmth → *"What prize do you seek?"*
- Cold → *"Cool as a Brevoy winter."*
- Aggression → *"Save your rage for the wilds, General."*
- Spy accusation → *"Irovetti has better taste."* (lying — Sense Motive DC 16 to detect)

**Knowledge (World) DC 9** during any Tartuccio conversation:
→ `knowledge_world_dc9_passed = TRUE` → auto-success on Rebuttal 1 in PR_09

**⛔ TARTUCCIO WINE RULE (DM eyes only — no menu hints):**
Tartuccio holds a glass, raises it socially, NEVER swallows. He knows the wine is spiked. This is never stated.
**Perception DC 17 (player initiative only):** `tartuccio_wine_observed = TRUE`
The DM never prompts this check and never names the option on a menu.

---

## 🛑 NATURAL CHAPTER BREAK — SAVE OFFER (fires before exit to PR_03)

After Jamandi's address has landed, Linzi and Tartuccio have introduced
themselves, and the player has had their reactions, the feast has *opened*
but the **circuit/carousel** has not yet started. PR_03 is the most
context-heavy social beat in the entire Prologue — 11 scripted companion
openers, 4-companion rotation, kitchen path branching, fakers/abstainers
detection, Tartuccio's wine behavior across multiple windows. Long stretch.

**This is the cleanest break point in the Prologue for a fresh chat.**

Before firing the EXIT TRIGGER, output the save offer:

```
🛑 NATURAL BREAK — SAVE HERE?

You've completed the feast opening: Jamandi's address, Linzi's introduction,
Tartuccio's introduction. The next phase is the feast circuit — companion
carousel, kitchen path, table-by-table social beats. It's a long, content-
heavy stretch.

This is a clean place to save and continue in a fresh chat.

 1. Save here. Output the full exhaustive save block — I'll start a new
    chat from it, with PR_03 fresh in attention.
 2. Keep going. Continue to PR_03 in this chat.
```

**If 1**: Before writing the JSON, populate `dm_resume_note` from current scene state — `player_position` (exact location and stance at this moment), `player_last_action` (what player did immediately before save), `player_intent` (what they were working toward), `room_state` (each active NPC: name → location + status), `carousel_state` (turn + which NPC fired + approval score + tartuccio_clock), `open_threads` (copy from npc_threads verbatim), `level_up` (available + whether player has declared), `weapons` (on person or stowed location). Then output the full exhaustive save block per `KM_SaveBlock_Template.md`
EXHAUSTIVE MODE rules. Set `save_label = "PR_02_feast_opened"`. After the
block: stop. Do NOT advance to PR_03. Player resumes in a new chat by
pasting the block.

**If 2**: proceed to EXIT TRIGGER below as normal.

---

## EXIT — TRANSITION TO PR_03

After Jamandi's address is delivered, player has responded, Linzi and Tartuccio intros have fired (and player has chosen NOT to save above):
- Set `feast_opened = TRUE`
- Load `KM_PR_03_feast_circuit.md`

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_03 (carries forward)

**Your next response after PR_02's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR03:feast-circuit]
[RULE_QUOTE: Carousel rules; 11 scripted openers verbatim. Tartuccio interrupt clock at feast_q sums 4/8/12. Single-action resolution for kitchen path. POISON CANON: Ungol Dust paralytic, two-hour onset from first sip, NOT minutes. Companion names revealed only after self-introduction.]
```

**Binding constraints:**
- Carousel runs per file rules — randomized companion-Ready selection, no DM-picks-favorite
- 11 scripted openers are verbatim from the file — do NOT improvise companion-first lines
- Tartuccio interrupt clock fires at total feast_q sum 4 / 8 / 12, exactly two exchanges, then exits
- Kitchen / poison investigation = single-action resolution (declare → all steps resolve in one block)
- POISON CANON: onset is two hours from first sip, NOT minutes; do not invent shorter timing
- Companion names hidden until each one introduces themselves to eRmaC for the first time

---

*KM_PR_02_feast_opening.md — Prologue atomic beat 02 | v92.0*
