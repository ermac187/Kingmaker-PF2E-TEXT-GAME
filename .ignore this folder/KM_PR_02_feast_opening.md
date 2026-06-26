# KM_PR_02_feast_opening.md — Prologue Beat 02: FEAST OPENING
## Atomic scene file | State: PR_02_FEAST_OPENING
## FILE_KEY: KMPR02:feast-opening
## RULE_QUOTE: Jamandi's opening address fires AFTER player makes their arrival choice. Mandatory player-choice STOP after the address — do NOT cut to the chronicler. Companions are STRANGERS — no names until each introduces themselves. Tartuccio's intro fires only after player has acted post-address.
## Pair-load: KM_Prologue_Systems.md (Tartuccio behavior scales)


> ⛔ DO NOT (1) fire Jamandi's address before the player makes an arrival choice (that is PR_01's job)
> ⛔ DO NOT (2) cut directly to Linzi after Jamandi speaks — mandatory player-choice stop first
> ⛔ DO NOT (3) use companion names not yet introduced — all chosen companions are STRANGERS here
> ⛔ DO NOT (4) fire Tartuccio's intro before the player has acted after Jamandi's address
> ⛔ DO NOT (5) hint at assassination or kitchen poison — player discovers this, not DM exposition
> ⛔ DO NOT (6) fire any "private debrief with Jamandi" scene before this beat — there is no such scene; player arrives directly in the banquet hall from PR_01 (see PR_01 NO INTERPOLATED PRIVATE SCENE block)
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (8) invent a *different* or more exotic poison compound, or have any NPC identify it at a chemistry-class level beyond its canonical name. Canon: the poison is **Ungol Dust variant** (a common paralytic; wide-spectrum cut for a full room, ~2hr onset, non-lethal at this dose). Poison response is TWO specialists, two jobs (full profiles in `KM_NPCs.md § Bokken` and `§ Ezvanki Keeg`): **BOKKEN identifies, EZVANKI cures.** When the player asks "who's your alchemist / who can identify this," Jamandi answers honestly — she keeps none on staff, but she has **Bokken already on-site** (the eccentric alchemist, in Restov before he settles in the Greenbelt; she keeps him at the manor for the feast as a poison precaution — NOT sent for, NOT arriving later, already here). Bokken examines the RECOVERED POISON (the tainted cask/residue the kitchen sweep finds — NOT a victim; pre-onset, ~2hr, there is nothing to read on a person) and NAMES it — Ungol Dust variant — plus what it does and the onset. (A skilled player Crafting/Medicine/Poison Lore check identifies it the same way.) Ezvanki then prepares the cure via divine + Medicine (category-level, no victim needed) in under 45 min for the full hall (40 doses). ⛔ Do NOT have Jamandi send Ezvanki to "examine the kitchen and the wine" (that conflates the search + the read + the cure into one — `.fail 9`); the search is Kesten/Kassil, the read is Bokken, the cure is Ezvanki. Substituting Kassil / Kesten / unnamed staff as the IDENTIFIER, or inventing a *different* compound name = `.fail 9`. The name reveals WHAT it is, not WHO sent it — the broker/"C" trail still dead-ends per the ceiling. (Note: Damiel Morgethai was a previous-LLM fabrication — do NOT reference him.)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR02:feast-opening]`
Line 2: `[RULE_QUOTE: Jamandi's opening address fires AFTER player makes their arrival choice. Mandatory player-choice STOP after the address — do NOT cut to Linzi. Companions are STRANGERS — no names until each introduces themselves. Tartuccio's intro fires only after player has acted post-address.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## ⛔⛔⛔ MANDATORY ❓ QUESTIONS BLOCK SCAN — EVERY RESPONSE ⛔⛔⛔

**Before finalizing ANY response in this beat, run this scan:**

1. **Did any NPC in the narration this response ask a question (`?` ending) OR issue an imperative demanding verbal answer?** Examples that AUTO-ADD: *"Tell me…"* / *"Give me the short version"* / *"Now I want yours"* / *"What do you say?"* / *"Speak"* / *"Your turn"* / *"And you?"* / *"Tell me what this is"* / Jamandi's address questions. Every one auto-adds to ❓ block this response.
2. **Did any previous response's ❓ block contain unanswered questions?** Carry forward verbatim unless current player input answered them. Answered = REMOVE (no "(Closed)" tag — full spec in `KM_DMRules_B.md`).
3. **Sum = new auto-adds + carried-forward unanswered.** If > 0, render ❓ block at ABSOLUTE LAST position. If 0, omit entirely.

**Self-audit:** If narration contains an NPC question/imperative AND the ❓ block doesn't have it as Q1/Q2/etc, STOP. Add it. Re-render. Missing = `.fail 17` + `.fail 3`.

**Form (verbatim):**
```
❓ QUESTIONS (<N>)

Q1. <NPC> asked: "<verbatim question text>"
    (<scene>, turn <N>)
```

**The resume case:** When this beat resumes from save with NPC questions pending in the recap (Jamandi mid-address, Linzi mid-introduction, Tartuccio mid-greeting), those questions MUST appear in the ❓ block on the resume response — the recap text counts as "this response's narration" for scan purposes.

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
1. `[STATE READ] current_scene="prologue_feast" | phase=PR_02_FEAST_OPENING | turn=<N>` then `[OPEN] <N> — 1.<short>(emoji)...` (omit line if 0 items). Game state only. Questions = TOP-block per item 4 (❓ WAITING ON YOUR ANSWER). Spec: `KM_DMRules_B.md`.
2. `[HP CHECK]`
3. Scene narration
4. 🧵 OPEN THREADS — game-state items only (entry-gated). NO questions here.
5. Player choice menu (minimum 10 options)
6. **❓ QUESTIONS** — ABSOLUTE LAST block. Q1/Q2... verbatim NPC questions + source + scene + turn. Auto-add same response NPC asks; persist until answered. Omit only if 0. Spec: `KM_DMRules_B.md`.

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

> Hu Tao's hand stills on her pommel. Linzi gasps and abandons her notebook mid-sentence. Keqing looks up from her plate, fork halfway. Yor Forger's eyes flick to the door and back without her head moving. Aerith's posture squares without a sound. Leliana's bow pauses mid-phrase against the strings and resumes one beat off.

---

## LINZI INTRODUCTION
*(Fires when player is in a socially neutral position — not mid-conversation with Jamandi)*
*(Fires only when `linzi_primary_chronicler = true` or `leliana_chronicler_mode = false`. If `leliana_chronicler_mode = true`, Linzi may still be present as companion but does NOT fire this intro in chronicler capacity — skip to LELIANA INTRODUCTION below.)*

**Linzi:** *(notebook already open, pen already moving)* *"You're [character name]! I've been waiting — I saw what happened at the gate, and — well, I've already started chapter one actually, I hope that's all right — I'm Linzi, I'm a bard, I chronicle things, heroic things specifically, and you are absolutely — I mean the ARMOR alone — can I follow you? I'm very useful. I can heal, I can inspire, I know twelve ballads about the Stolen Lands and none of them are accurate yet but that's going to change—"*

---

## LELIANA INTRODUCTION
*(Conditional — read gate values before firing)*

### IF `leliana_chronicler_mode = true` (Leliana is primary chronicler):

Leliana occupies the chronicler's table position — the same seat Linzi would hold: near enough to the room's center to observe everything, close enough to the player's likely path that an approach is natural. Her lute case rests on her lap, closed but unlatched. A small score notebook is open on the table beside her plate; she is writing in it with quick, precise strokes — notational shorthand, not words.

When the player enters or draws near, her bow pauses against the strings one beat. She does not close the notebook.

**Leliana:** *(not looking up from the score notebook, pen still moving)* *"The Unfinished Verse needs an overture. An overture needs a subject worth writing about. So."* *(she looks up — brief, appraising, not unfriendly)* *"You're here."*

She does not introduce herself yet. If the player speaks first, she answers. If the player waits, she returns to the notebook as if they passed inspection.

> *(DM: her chronicler position is visible to the room — Jamandi may notice she is treating this like a performance to document, not a recruitment dinner to survive. No mechanical effect yet; flag for PR_03 if player draws attention to it.)*

**⛔ DO NOT** fire Linzi's intro block in this mode. Linzi may be present elsewhere in the room (companion seat, per pick-6 position), but she does not approach in chronicler capacity.

---

### IF `leliana_chronicler_mode = false` AND Leliana in `companions_selected`:

Leliana is positioned at her Pick-6 companion seat (A3). She is not writing. Her lute case is stored under the table. She is doing what she always does in a room full of strangers with something to prove: performing attention — making eye contact at the right moments, laughing at the right intervals, being exactly as charming as the situation requires.

Her ambient reaction on player entry (already rendered in PHASE 1 NPC REACTIONS above) fires as written: *bow pauses mid-phrase against the strings and resumes one beat off.* She does not approach for introduction unprompted; she waits for the player to come to her, or for the carousel to bring her forward in PR_03.

> *(DM: in this mode, Leliana has no chronicler mechanical effects in PR_02. Her full Pick-6 opener fires in PR_03 per carousel rules.)*

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
Tartuccio holds a glass, raises it socially, NEVER swallows. He also does not eat. **Real reason (DM eyes only, never stated to the player):** he is the inside man on the poison plot. The poison was prepared in THIS kitchen and is paralytic — it puts people to sleep / paralyzes them. He has a job to do tonight (signal coordination, position-keeping, watching the room, his role in the ambush sequence). He cannot afford to fall asleep before his work is done. He doesn't know which specific cups/plates/surfaces caught contamination from the kitchen prep, so he treats EVERYTHING coming through that kitchen as a risk. The abstinence is operational, not paranoid: he's not avoiding the wine because he knows it's spiked, he's avoiding ALL food and drink because going down before he's executed his part of the plan would be a catastrophic failure. The player sees only the surface: cup held, raised, never swallowed; plate untouched. This is never stated.
**Lock holds even under player reassurance:** if the player tells Tartuccio "the wine is fine," "I tested it," "the kitchen is cleared," "Ezvanki blessed everything," or offers him a personally-poured cup, he STILL does not drink. Reasons (DM-internal): (a) he doesn't trust the player's assurance because he knows the player doesn't know what he knows, (b) he can't show the player that he distrusts the assurance without giving himself away, (c) the cost of being wrong is going down before his role is executed — unrecoverable. He thanks the player politely, raises the cup, and does not drink. Same deflection, same gesture, every time.
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

## ⛔ MANDATORY FEAST POSITION SELECTION — BEFORE LOADING PR_03

**This menu is a HARD GATE between PR_02 and PR_03.** No PR_03 content fires — no carousel init, no Linzi opener, no Tartuccio cadence, no companion approaches — until `player_feast_position` and `player_feast_cell` are written to the save block.

**⛔⛔ EXCEPTION — DO NOT FIRE THIS MENU IF THE PLAYER HAS REFRAMED THE FEAST OUT OF "SOCIAL RECRUITMENT" MODE.** This menu and the entire carousel it gates exist for the DEFAULT social feast — companions circulating, recruitment, dispositions ticking, Tartuccio working the room. If the player has turned the feast into something else — an active tactical operation, a staged ambush (e.g. the "Lady Sleeps" fake-paralysis gambit), a lockdown, a crisis response — then **the recruitment carousel does NOT apply and this menu is WRONG to render.** Forcing a player who just built an ambush to "choose a carousel spot" priced in disposition-per-turn / approach-speed / PR_09-weight terms is incoherent (there is no leisurely recruitment happening) and railroads them back into a script they deliberately left. In that case:
> - **If the player already stated a SOCIAL position** (e.g. "close to Jamandi, good view of the room" — a deliberate choice of where to be seen during the social hour), TAKE IT. Set `player_feast_position` to their described spot. Do NOT override a stated social position with a 14-option menu.
> - **⛔ A TACTICAL POSITION DURING THE OPERATION DOES NOT SATISFY THIS GATE.** Where the player stood during Lady Sleeps (e.g. "H6", "near the head table to spring the garrotte") is a combat/ambush position — it satisfies nothing about the social carousel. `player_feast_position` is a SOCIAL field: where the player chooses to anchor their recruitment table after the feast returns to normal. It cannot be back-filled from a tactical operation. "Already at H6 from Lady Sleeps staging" = `player_feast_position` still null. The gate is still live. **The carousel was NOT replaced by the Lady Sleeps operation — it was suspended and resumes.** Claiming the operation substituted for the carousel = `.fail 9`.
> - **Price the position TACTICALLY while the operation is active, not in carousel terms** — reach, sightlines, distance to Jamandi/the entrances, who's near for the spring. Drop the recruitment tradeoffs — that system is SUSPENDED during the operation.
> - **SUSPEND the carousel itself** — no companion-approach rotation, no Tartuccio interrupt clock, no recruitment openers during the ambush/crisis. Companions may still be read into the player's plan (that's the player's call), but they don't "approach for recruitment."
> - **⛔⛔ CAROUSEL RESUME TRIGGER:** When the scene returns to a normal social register — crisis resolved, attackers captured/fled, host has retaken control of the room, player is no longer in active tactical operation mode — **fire the 14-position menu immediately as the ENTIRE next response.** Not as one option inside a larger menu. Not deferred. The menu IS the response; nothing before it, nothing after it. This is the gate re-opening: `player_feast_position` is still null, so the gate is still live. A player stepping back to let Jamandi retake the room IS the resume trigger. Run the host-retakes-control narration, then fire the menu in the same response.
> - The assassins/attackers arriving is a LATER beat (PR_04→PR_07); do not fire carousel social mechanics in the gap, and do not stall the player's plan waiting for a menu they don't need.
This is the HONOR-THE-PLAYER'S-PLAN rule applied to scene structure: when the player has changed what the scene IS, the DM runs the player's scene, not the default script.

**TRIGGER:** Player has responded to Jamandi's address, the floor has loosened (people moving, drinks circulating, Linzi & Tartuccio intros delivered). The next response — BEFORE any PR_03 beat content — renders the menu below verbatim and HALTS.

**SKIPPING THIS MENU = `.fail 41` (scripted menu skip) + `.fail 16` (state field omission) + `.fail 9` (rule violation).**

**⛔ CELLS ARE FROM THE MASTER GRID** (KM_DMRules_B.md § HALL POSITION, 15 wide A–O × 19 tall). The cells below are the authoritative reference — they MUST match the master grid. Render all 14 options in order; do not drop, reorder, or invent a cell. Full trade-off detail per option → KM_DMRules_C.md § FEAST POSITION SELECTION.

**Render this block exactly, then STOP and wait for the player's pick:**

```
🎭 CHOOSE YOUR FEAST POSITION — sharp trade-offs; no two are alike

1. 🛡️ CHAMPIONS (E8) — warrior cluster, military gravity
   + Warriors (Hu Tao, Yor Forger, Keqing) +1 approach speed
   + Kassil disp +1/turn; Combat-build Diplomacy +1
   − Casters (Leliana, Aerith, Linzi) −1 approach
   − Jamandi disp +0; Tartuccio targets warriors first
   TRADE: warrior-recruitment specialist.

2. 👑 HEAD TABLE (H4) — standing alignment with host
   + Jamandi disp +1/turn; PR_09 weight ×1.3
   + Tartuccio CANNOT approach (too public)
   − Populists (Yor Forger/Leliana/Aerith) −2 approach; Aerith refuses
   − Earshot 2-sq only
   TRADE: court politics maxed.

3. 🌑 WINE ALCOVE (C15) — privacy, depth, withdrawal
   + Yor Forger +2 approach; Keqing +1; private = +2 disp swing
   + Tartuccio M+3 (half his interrupts)
   − ALL other companions −2 drift; Jamandi −1/turn; PR_09 ×0.7
   TRADE: deep one-on-one specialist. (Harrim planted here.)

4. 🔥 HEARTH (N10) — aggressive intel, contested ground
   + Tartuccio Full audio TO him; Conf floor −1; Aerith +1
   − Tartuccio Full audio FROM you; Exchange Cap +1; Headcount +1
   TRADE: intel war / Tartuccio harasser. (Amiri planted here.)

5. 🎭 CENTER FLOOR (H10) — maximum visibility
   + Full audio everywhere; +1 drift all companions; PR_09 ×1.5; Linzi +2
   − Tartuccio comes hard (M−2); losses doubled; Jamandi −1; Hu Tao/Linzi −1
   TRADE: high-reward / high-cost spectacle.

6. 🪜 MAIN DOOR (H17) — security posture, exit access
   + Kesten immediate; clean exit; Hu Tao +1
   − Companions read "ready to bolt" −2 drift; Jamandi −1; Tartuccio ignores you
   TRADE: security operator.

7. 🪑 SEEKERS' EDGE (K15) — deepest enemy territory
   + ALL 5 seekers Full earshot; Ch1 flip DC −2 per seeker tier
   − Tartuccio Full+ audio FROM you; Jamandi disp −2/turn (STRONGEST neg)
   TRADE: Ch1 seeker-flip prep. Burns Jamandi hard.

8. 🌀 MOBILE / CIRCULATING — works the room
   + +1 drift to any companion you cross; Tartuccio M+2; +1 Perception
   − Opener slots take 2 turns; Jamandi −1; Linzi −1 (chronicled "agitated")
   TRADE: breadth over depth.

9. 👁️ BALCONY (stairs O3) — observer view
   + Visual on ALL positions (+3 Perception); Jaethal thread unlocks
   − NO companion can approach (carousel HALTS); Headcount +2
   TRADE: intel maximalist / recruitment zero. (Jaethal planted here.)

10. ✦ LINZI-ANCHOR (D8) — chronicler cluster
    + Linzi +1/turn; PR_09 +20%; Linzi-led openers fire 1 turn faster
    − Hu Tao/Yor Forger −1; Jamandi reads "Linzi's pet"
    TRADE: chronicler-led RP build.

11. 🍷 KITCHEN DOOR (B10) — consumable buffs
    + Direct food/drink (free action); max 3 buffs carry to PR_04/05
    + Staff +1/turn; Ezvanki +1; Keqing +1
    − Jamandi −1/turn; Carousel −1 drift
    TRADE: buff stacker / staff intel.

12. ⚔️ KASSIL'S SIDE (F4) — military advisor
    + Kassil +2/turn; Hu Tao +2; Keqing +1; War-talk Diplomacy +2
    − Casters −2; Tartuccio Conf +1 (wants martial framing); Linzi −1
    TRADE: war-council framing. (Valerie planted here.)

13. 🐍 TARTUCCIO TAIL — wherever he goes, you go
    + Intercept every flip; Tartuccio Conf floor −2; Full+ audio always
    − Exchange Cap +2; Headcount +2; Jamandi −1; Hu Tao/Linzi −2
    TRADE: hunter mode. All-in. Catastrophic if outmatched.

14. ✏️ CUSTOM — describe any cell; modifiers from distance + zone

❓ Q: Which position?
```

**AFTER PLAYER PICKS:** write `player_feast_position = <pick>` and `player_feast_cell = <cell>` to save block. Recalculate `jamandi_in_earshot` per cell (FULL / PARTIAL / VISUAL_ONLY / ROTATING / FALSE — see KM_DMRules_C.md § JAMANDI EARSHOT MECHANIC). Set `staff_access`, `kesten_access`, `kassil_access` per cell. Apply position modifiers to companion drift and Tartuccio Confidence FROM THIS RESPONSE FORWARD (not retroactive). THEN load PR_03 and run carousel init.

**Full rule + earshot/access tables → `KM_DMRules_C.md` § FEAST POSITION SELECTION.**

---

## EXIT — TRANSITION TO PR_03

After Jamandi's address is delivered, player has responded, Linzi and Tartuccio intros have fired, the save offer has been answered, AND `player_feast_position` is written:
- Set `feast_opened = TRUE`
- Load `KM_PR_03_feast_circuit.md`

**Loading PR_03 with `player_feast_position` still null = `.fail 41`. The position menu above is non-skippable.**

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_03 (carries forward)

**Your next response after PR_02's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR03:feast-circuit]
[RULE_QUOTE: Carousel rules; 11 scripted openers verbatim. Tartuccio interrupt clock at feast_q sums 4/8/12. Single-action resolution for kitchen path detection only (contamination YES/NO). Poison = Ungol Dust variant (paralytic); Bokken (on-site) or a player Crafting/Medicine check names it, Ezvanki cures. Companion names revealed only after self-introduction.]
```

**Binding constraints:**
- Carousel runs per file rules — randomized companion-Ready selection, no DM-picks-favorite
- 11 scripted openers are verbatim from the file — do NOT improvise companion-first lines
- Tartuccio interrupt clock fires at total feast_q sum 4 / 8 / 12, exactly two exchanges, then exits
- Kitchen / poison investigation = single-action resolution for DETECTION only (contamination present YES/NO); response runs through Ezvanki per `KM_NPCs.md § Ezvanki Keeg`
- POISON RESPONSE: the poison is **Ungol Dust variant** (paralytic). **Bokken** (already on-site) or a skilled player Crafting/Medicine/Poison Lore check NAMES it + gives effect + onset, from the recovered substance; **Ezvanki** prepares the cure via divine + Medicine in under 45 min for the full hall. Kesten/Kassil/player do the search; player Medicine/Crafting checks detect contamination + recover the substance. Inventing a *different* compound name, or assigning the IDENTIFICATION to Ezvanki/Kassil/Kesten/Jamandi/unnamed staff instead of Bokken-or-a-player-check = `.fail 9` + `.fail 38`
- Companion names hidden until each one introduces themselves to eRmaC for the first time

---

*KM_PR_02_feast_opening.md — Prologue atomic beat 02 | v95.7 (2026-05-27): poison response split (Bokken identifies, Ezvanki cures). 2026-06-07: poison NAME restored to "Ungol Dust variant" per owner — the v95.7 "never named" rule was an overcorrection that deleted the established name (it was canon in the kmg2/old_2 versions, "Ungol Dust variant"). Bokken/player check names it; don't invent a different compound. Damiel Morgethai (previous-LLM fabrication) stripped.*
