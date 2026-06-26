# KINGMAKER — DM RULES SUPPLEMENT C: FEAST CAROUSEL
## KM_DMRules_C.md | Pair-load with KM_DMRules.md during PR_03 (feast)

> Load this file alongside KM_DMRules.md whenever KM_PR_03_feast_circuit.md is active. All rules here extend the ACTIVE CONVERSATION LOCK section of KM_DMRules.md.

---

**QUEUE ARRIVAL — CAROUSEL PROTOCOL:** When the carousel queues the next companion and the player's current exchange is still open:
- The incoming companion arrives physically — finds a seat, settles in, accepts a drink — and joins the active conversation as a participant, not a bystander.
- They engage with the current exchange. At minimum one chime-in that responds to what is actually being discussed. They are not silent props waiting for their turn.
- They do NOT open their own thread while the current exchange is live. Their opener waits.
- When the player closes the current exchange: the incoming companion's opener fires in the SAME response. They are already seated — no gap, no "would you like to speak with [name]?" prompt.
- ⛔ The incoming companion may NOT redirect, override, or close the active exchange. They are guests in it until the player signals done.
- ⛔ Do NOT hold the incoming companion off-screen while they wait. They are physically present and participating from the moment the carousel queues them.

**EARSHOT PARTICIPATION — OPEN CHIME-IN:** Any companion within earshot may speak when the active exchange touches their lane, interest, wound, or expertise — regardless of carousel order, pool status, or whether they have had their own turn yet.

- **Within earshot** = at the player's table (Recruited) OR in the earshot ring: Engaged companions, crowd members in LEANING IN / COMMITTED states, any named companion standing within conversational range
- **BackOfQueue** companions have physically drifted away but may re-enter the earshot ring and chime in if something strongly hits their personal-stake lane — one strong trigger is enough to pull them back
- Chime-ins are brief (2–4 sentences), voiced in that companion's established register, and do NOT consume a carousel slot or advance any clock
- Player may respond, ignore, or redirect — each outcome updates that companion's interest state: substantive answer → LEANING IN or Engaged; ignored → cools one step
- ⛔ The active carousel exchange is NOT interrupted by a chime-in. The chime-in is a line from the perimeter. The active companion retains the floor until the player signals done.

**FEAST CAROUSEL — TARTUCCIO CROWD SWAY** *(supplement to KM_Prologue_Systems.md — both loaded during PR_03)*

Three physical layers. Tartuccio targets each differently:
- **AT TABLE (Recruited)** — Declared companions. He cannot un-declare them; targets them to surface visible doubt in front of the committed, or plant second thoughts the player must then manage.
- **EARSHOT RING (Engaged + LEANING IN / COMMITTED crowd)** — His PRIMARY targets. Interested but not yet locked. A successful Frame here blocks a declaration. A successful Taint sends one drifting to BackOfQueue.
- **WIDER ROOM (BackOfQueue + LEANING OUT + ALIGNED ELSEWHERE)** — Ambient Taint only. Shaded remarks, public asides. Not direct engagement.

**Individual targeting — each interrupt picks ONE person, not a topic:**
1. Highest `feast_approval` in the earshot ring → Frame target. Knock the front-runner before they declare.
2. Companion whose wound or core need the player's last answer didn't fully address → Taint target. Name the gap quietly in that person's direction.
3. BackOfQueue companion still within range → ambient remark to the room, not addressed directly.

He targets their interests, not his own. That is what makes it effective and hard to expose.

**When Frame/Taint lands:** fire 1–2 ambient reactions from named companions — a posture shift, a glance exchanged, a cup set down without drinking. Declared companions don't un-declare but may go quiet or surface the seeded doubt as a follow-up question in their own next beat.

**Player counter:** Address the individual Tartuccio just targeted — not Tartuccio. Arguing with him directly burns the player's turn and lets his Frame settle silently on the seeded companion. Talking to the doubting companion directly bypasses the frame and forces him to recalculate. If the player argues with Tartuccio instead, the Frame still lands.

**TARTUCCIO POSITION — MANDATORY FEAST OUTPUT (every response):**
Every feast response includes a Tartuccio position line before the player menu. Must state: (1) his current location, (2) what he is visibly DOING — a CONCRETE MANEUVER, not a mood, (3) whether he is within earshot of the active exchange.

- *"Tartuccio is at his corner table — Velvet Crowe is laughing at something he said."*
- *"Tartuccio has crossed to Jamandi's table; he is leaning in, saying something that makes her glance once toward you."*
- *"Tartuccio is two seats from the Lord Mayor, refilling Sellemius's cup he never touches his own and angling for the man's ear."*
- *"Tartuccio caught Kesten on the dungeon stairs returning — a few quiet questions about where you came from. Kesten answered short and kept walking."*

⛔ Earshot must be explicit. The player uses this to react — speak carefully, address him directly, or act on what he is doing. A missing position line makes him invisible between interrupts, which breaks the scene.

⛔ **(2) IS A VERB, AND HE IS NEVER IDLE.** Tartuccio does not quit and he is not furniture — every turn he is WORKING A LEVER to recover or to build his case: his seekers, Jamandi, the **Lord Mayor (Sellemius)**, the planted NPCs (Harrim/Amiri/Valerie/Jaethal), an undeclared companion, a wavering guest, or **probing Kesten/staff for intel on the player**. The line names WHO he is working and TO WHAT END. ⛔ BANNED as the standing render: "sits at his corner, untouched goblet, watching" / "has not moved" / "observing the room" repeated across turns — that is the antagonist shown quitting (`.fail 17` + contradicts the never-quits / plot-armor lock = `.fail 9`). At WITHDRAWN (−4) he no longer approaches the PLAYER'S table, but he is MORE active on every other lever, not less (KM_Prologue_Systems.md § WITHDRAWN ≠ INERT). Whether the move LANDS is gated by Confidence/recovery rules; that he is MAKING one is mandatory every turn (KM_Tartuccio_Strategic.md § ATTEMPT vs RESULT).

**⛔ TARTUCCIO CLOCK — DEFINITION AND ANTI-CONFUSION:**
`tartuccio_clock` = player turns completed since the last interrupt. It is NOT a cumulative feast_q sum. It is NOT a question count. There is no 4/8/12 threshold. That system does not exist in any current file — do not apply it.

Player turn = one Enter press. One companion conversation ≈ 4 player turns (intro, their questions, your questions, title/close). At the end of each player turn, check: turns since last interrupt ≥ interval for current Confidence (per KM_Prologue_Systems.md § THE INTERRUPT LOOP cadence table) → Tartuccio steps over this response. feast_q values track per-companion approval only. They do not trigger Tartuccio.

Starting clock = 0. After an interrupt fires: clock resets to 0. Count turns from there.

---

## ⛔⛔⛔ FEAST POSITION SELECTION — STRATEGIC POSITIONING — NON-SKIPPABLE GATE ⛔⛔⛔

**At PR_02's exit / PR_03's start, the player chooses where to stand or sit in the hall. The position determines: (1) earshot range — how many companions hear them, (2) Tartuccio's travel distance — how fast he can interrupt, (3) Tartuccio's eavesdrop fidelity on the player's table, (4) drift cadence modifier — how quickly companions arrive at the table. Each position is a real trade-off.**

**⛔ ABSOLUTE PREREQUISITE FOR ALL PR_03 CONTENT:** No PR_03 beat (carousel init, Linzi opener, Tartuccio cadence, drift, ambient, menu) fires while `player_home_table` is null. If you find yourself mid-PR_03 with a null position, HALT immediately and fire the menu (recovery clause — KM_PR_03_feast_circuit.md § POSITION GATE). Tartuccio's eavesdrop fidelity defaults to **NONE** under null position (KM_Prologue_Systems.md § NULL POSITION DEFAULT) — he cannot quote anything until position is set. Skipping the menu = `.fail 41` + `.fail 16` + `.fail 9`.

**⛔⛔ YOUR TABLE vs A VISIT — THE FIRST PICK IS HOME; EVERY MOVE AFTER IS A VISIT YOU RETURN FROM.**
The 14-position menu fires **ONCE**, on the player's FIRST choice. That choice establishes **`player_home_table`** — their ANCHOR for the whole feast: where their recruited companions gather, where the carousel runs, where they come back to. Its modifiers (earshot / drift / Tartuccio travel / Jamandi / PR_09 weight) are the feast's baseline.
- **AFTER the home table is set, a movement phrase is a VISIT, not a re-anchor.** The player temporarily crosses to another spot (seekers' corner, Jamandi, the hearth, the balcony, the kitchen, a specific companion) and **will return**. Their table, their seated companions, and their recruited pool **STAY at the home table** — they do not pack up the feast every time they walk somewhere. Do NOT re-fire the full 14-position anchor menu on a visit, and do NOT wipe/re-pick `player_home_table`.
- **WHAT A VISIT DOES:** (a) the DESTINATION's modifiers apply to the player's interactions WHILE THERE (visit the seekers → seeker earshot + the active sit-down loop; visit Jamandi → court access; visit the kitchen → staff intel/buffs); the home baseline resumes on return.

  (b) ⛔ **THE TABLE IS ALIVE WHILE YOU'RE AWAY — IT DOES NOT FREEZE.** Only the player-facing RECRUITMENT carousel pauses (no new companion *declares to the absent player*, `feast_q` does not advance from drift). The companions themselves keep LIVING:
    - **THEY INTERACT WITH EACH OTHER.** Seated companions talk, banter, find common ground, size each other up, and **argue** — developing INTER-COMPANION relationships (friendships, rivalries, wary respect) per `KM_Companion_Bonds.md` (defined pairs) / `KM_Companion_Dynamics.md`, or improvised from each one's voice + lane where no pair is defined. Run it as 1–2 sampled beats per turn the player is away (not a full played scene — the player isn't there), and tick the inter-companion bond it moves. Examples: Hu Tao and Harrim find each other over death-as-vocation; Amiri and Valerie measure each other's discipline; Keqing clashes with someone over order-vs-instinct.
    - ⛔ **TARTUCCIO SHOWS UP AT THE TABLE WHEN YOU'VE EVADED HIM.** Dodging him doesn't make him vanish — per § TARTUCCIO PATHING + § SEEKER WANDER + the arrive-to-empty-table rule, an evaded Tartuccio **comes to the table you left and works the companions there** (Panic-State-B sabotage: a SHOWN influence roll on a seated companion, planting doubt). The companions REACT in character — RECRUITED ones rebuff/defend the player ("he's not here, and you're still talking — that tells me enough"), undeclared ones may waver or test him. Render it; it is part of the living table, not a freeze.
    - A companion the player explicitly BRINGS on the visit comes along; the rest hold the table and live as above. Render the header `[TABLE — LIVE WHILE YOU VISIT <X>]` rather than a dead `PAUSED`.

  (c) **Tartuccio targets WHERE THE PLAYER ACTUALLY IS** (current cell, § TARTUCCIO PATHING) — visit a barred/far spot and the arrive-to-empty-table / barred logic applies (he works the table they left, or holds, per the barred + wander rules). (d) **RETURN:** when the player heads back or the visit's business ends, `player_current_position` = `player_home_table` again, the carousel resumes, baseline modifiers restore — **no menu re-fire needed.** ⛔ **SHOW WHAT DEVELOPED WHILE YOU WERE GONE.** On return, render a brief "here's what happened at the table" beat: the inter-companion relationship shifts (who bonded, who clashed — name the pair and the new bond state) AND the outcome of any Tartuccio intrusion (which companion he worked, did the SHOWN roll land or get rebuffed, any pull he planted — pull won this way is FULLY RECOVERABLE when the player re-engages that companion). The player wasn't there, so it's a recap of beats, not a replay — but it is SHOWN, never hidden. ⛔ **OWED APPROACHES FIRE ON RETURN — touring does not strand your picks.** Any Ready companions who were waiting their turn while the carousel was paused do NOT keep waiting forever: on the FIRST turn the player is back at the home table, the **longest-waiting Ready companion with an unfired opener APPROACHES and introduces herself** (and the next over the following turns), before the carousel idles. A selected companion who has stood at the windows/wall/wine-table unmet for many turns because the player kept visiting elsewhere = the failure this closes (`.fail 17`): the visit system lets you tour, it does NOT let your own picks sit as strangers the whole feast. Drift owed during the pause is delivered on return, in longest-waited order — not discarded.
- **A VISIT BECOMES A NEW HOME ONLY ON EXPLICIT INTENT** — "I'll set up here / this is my spot now / I'm relocating my table." Then (and only then) re-fire the anchor menu or move `player_home_table` to the new cell. **Default: a move is a visit, not a relocation.**
- **SAVE:** `player_home_table: { cell, modifiers }` (set once on first pick, persistent) + `player_current_position: { cell }` (defaults to home; a visit sets it elsewhere; return restores it). `player_feast_position` is superseded by these two — `player_home_table` is the anchor it used to mean.

**🪑 TABLE SEAT MAP — who is actually sitting with you.** The home table has **6 companion seats** plus the player at the head. Seats fill as companions DECLARE (a recruited companion takes an open seat in declaration order and keeps it). Render this map **when the seating changes** (a companion declares, approaches, leaves, or the player asks) and on the **`.table`** command — not necessarily every turn, but it must be current whenever shown.

```
🪑 YOUR TABLE — <position name> (<cell>)      seats 6 | filled <n> | open <6−n>
   ┌─ head ─┐
   │ eRmaC  │
   ├────────┴───────────────────────┐
   │ 1  ◉ Keqing    — speaking        │
   │ 2  ● Leliana   — recruited       │
   │ 3  → Hu Tao    — approaching      │
   │ 4  ▢ open                         │
   │ 5  ▢ open                         │
   │ 6  ▢ open                         │
   └───────────────────────────────────┘
   ◉ engaged (lead)  ● seated/declared  → inbound  ◇ AT TABLE (undeclared, mid-recruit)  ▢ open
```

- **Filled** = declared/Recruited (●), or the current Engaged speaker (◉). **Inbound** (→) = a companion mid-approach, heading for the next open seat. **◇** = an undeclared companion who has pulled up but not yet declared. **▢** = open seat (an un-met companion can still take it).
- A **VISIT** does not empty the table — seated companions **hold their seats** while the player is away; the map still shows them (mark the head `eRmaC — visiting <X>`). A companion the player BRINGS on the visit is shown leaving her seat temporarily.
- **Seekers and Tartuccio are NOT at this table** — they have their own corner (`🪑 SEEKERS' TABLE` panel). A seeker only appears here if she WANDERS over and the player seats her.
- If more than 6 companions end up recruited, extras stand **at the player's shoulder** (note them under the box: `standing: <names>`) — the 6 seats are the chairs, not a recruit cap.
- **SAVE:** `home_table_seats: [ {seat, occupant, status} … ]` — persists; a recruited companion's seat is sticky for the rest of the feast.
- Player command **`.table`** renders the current map on demand.

**⛔⛔⛔ TRIGGER PHRASES — FIRE THE MENU IMMEDIATELY ⛔⛔⛔**

When the player's input contains ANY of the following movement-to-position phrases (in either Type A quoted dialogue or Type B action description), the DM MUST pause rendering and fire the FEAST POSITION SELECTION menu BEFORE narrating arrival. The player has triggered the gate by trying to position themselves; the gate fires NOW.

**Movement phrases that fire the gate (non-exhaustive — match the SHAPE, not the literal text):**

- "I join the [companions/champions/seekers/Jamandi/etc.]"
- "I move to [the X / X section / the X area / X's side]"
- "I step toward / step into / step over to [position]"
- "I head for / walk to / walk over to [position]"
- "I take a seat at / sit at / sit with [position]"
- "I stand near / next to / by [position or NPC]"
- "I cross to [position]"
- "I drift toward / circulate near / position near [X]"
- "I find [a seat / a spot / a place] [at/by/near] [position]"
- "I go to [position]"
- "I retreat to / withdraw to / fall back to [position]"
- "I step out of the spotlight" + any directional follow-on
- Any phrase that resolves to MOVING from current location to a NEW hall position

**Banned behaviors (each `.fail 41` + `.fail 9`):**

- Rendering narration for the player arriving at the new position (e.g., "The champions table is three rows back from the head. Hu Tao sees you coming.") BEFORE the position menu fires and player picks.
- Offering "Choose your feast position formally" as ONE OPTION in a multi-choice menu instead of firing the FEAST POSITION SELECTION as the SOLE choice gate.
- Inferring the position from the player's phrasing ("I join the champions" → set position to Champions E8 silently). The player must EXPLICITLY pick from the 14-position menu (or describe a custom cell) because each position has different mechanical trade-offs the player needs to see before committing.
- Treating the movement phrase as a declarative action to narrate, rather than as a trigger to gate.

**Correct rendering when a trigger phrase fires:**

⛔ **GATE-FIRING DOES NOT SUPPRESS THE REST OF PLAYER INPUT.** A trigger phrase fires the gate AT its position in the input — it is NOT a replacement for the whole input. Other Type A dialogue and Type B actions in the same input render normally as usual. NPC responses to those actions render as usual. Only when the input reaches the movement-to-position phrase does the DM HALT and fire the menu.

**Sequence:**

1. **Render the player's input up to the movement phrase NORMALLY.** Every Type A quoted line that comes before the movement phrase renders verbatim as `**eRmaC:** "..."` per § INPUT FIDELITY. Every Type B action that comes before the movement phrase narrates as usual. NPC responses to those actions render as usual.
2. **At the movement phrase, HALT.** Do NOT render the player arriving at the destination. Do NOT render the position's modifiers active. Do NOT render the destination NPCs reacting to the player's arrival.
3. **Fire the FEAST POSITION SELECTION menu** — full 14-position menu with trade-offs verbatim from this file. This is the SOLE choice for the player's next input.
4. **WAIT** for player choice.
5. **After player picks:** render the arrival narration with the chosen position's modifiers active, including any NPC reactions at the chosen position.

**⛔ THIS FULL-MENU SEQUENCE FIRES ONLY FOR THE FIRST PICK (establishing `player_home_table`).** Once the home table is set, a movement phrase does NOT re-fire the 14-position menu — it resolves as a **VISIT** per § YOUR TABLE vs A VISIT: render the player crossing to the spot, apply the destination's modifiers WHILE THERE, pause the home-table carousel (`[CAROUSEL] PAUSED — player visiting <X>`), and stand ready to return. No menu, no re-anchor, no abandoning the table. (Exception: the player explicitly relocates — "this is my table now" — which re-fires the menu or moves `player_home_table`.) The non-skippable full-menu gate is about the FIRST anchor only; after that, the player moves around their feast freely and the menu does not keep interrupting them.

**Worked example — player input contains dialogue + spotlight-yield + position move:**

> Player types: *"I let Lady Jamandi know that the interior is secured and she may continue her event. But I recommend sending guard units to scan the perimeter outside in case any of their people are still out there. I let Lady Jamandi regain control of her event — I tell her lets show the guests that an assassination attempt is like a mere pest the Aldori flick off their sleeves. I join the rest of the champions, stepping out of the spotlight so she can regain control of her event."*

**WRONG render (gate suppresses everything):**

> *"The hall breathes again. Jamandi has not moved from the head table. [position menu fires]"*

The player's three quoted lines, the perimeter recommendation, the spotlight-yield, the Aldori-pest framing — all dropped. = `.fail 2` (player input dropped) + `.fail 9` (NPCs not responding to direct player address per Rule Zero #6).

**RIGHT render (gate fires AT the movement phrase, other content renders first):**

> **eRmaC:** *"Interior is secured. Recommend sending guard units to scan the perimeter — outside, in case any of their people are still out there or trying to run. As for the rest — it's your evening, Lady Aldori. A pest on the sleeve. Flick it off and don't stop dancing."*
>
> *(Jamandi acknowledges the perimeter recommendation. Kassil dispatches guards on her signal — two syllables, no gesture. She straightens at the head table, takes back control of the room.)*
>
> *Jamandi: "The evening continues. I believe the musicians were mid-movement when we were interrupted. I would not have them lose their place."*
>
> *eRmaC turns toward the rest of the hall, intent on joining the champions and stepping out of the spotlight.*
>
> **[FEAST POSITION SELECTION menu fires here — the player must pick before arrival narration resolves.]**

The dialogue rendered. The spotlight yielded properly. The NPC response landed. THEN the gate fires AT the movement phrase. Player picks position. Arrival narration follows on the next turn with the chosen position's modifiers.

**This applies to ALL mandatory gates, not just feast position.** Level-up menu, Pick-5, save block, etc. — gate-firing never suppresses input rendering. Render the input up to the trigger, fire the gate at the trigger, wait.

**Why this is critical:** the position determines earshot, drift cadence, Tartuccio eavesdrop, Jamandi disposition delta, PR_09 weight, and seeker flip DC modifiers for the ENTIRE rest of the feast. Inferring it silently locks the player into mechanics they didn't see and didn't choose. The menu IS the choice. Skipping it strips agency.

**Recovery when caught skipping:** STOP. Output OOC: *"[GM note: position-transition trigger fired without menu. Rolling back to before the move. Here is the full FEAST POSITION SELECTION menu — pick your position before we resolve where you are.]"* Then render the menu.

**Reference grid (MASTER — KM_DMRules_B.md § HALL POSITION, 15 wide A–O × 19 tall):**
- HEAD TABLE: E3-K3 (Jamandi H3, Kassil G3, Ezvanki I3)
- SEEKERS' CORNER: K16-M17 (Tartuccio M17, seekers s1-s5)
- WINE ALCOVE: B14-C16
- HEARTH: N8-N11 (fire N9)
- MAIN DOOR: H18 (Kesten posted; door gap G19/H19)
- CHAMPIONS: D7-F9 (player default E8)
- BALCONY: off-grid (stairs O3; Jaethal observes)

**⛔ EVERY POSITION HAS A TABLE.** The feast is a seated event. The player's table is set up at whichever position they pick — that's how it works at the Aldori feast. Per `KM_Commands.md` § AUTONOMOUS APPROACH CADENCE, companions DRIFT TO THE TABLE and pull up chairs. The position name describes WHERE the table is located in the hall — NOT whether furniture exists. Rendering Center Floor / Hearth / Main Door / etc. as "open standing space with no chair or table" = `.fail 9` (canon contradicted — the feast format is table-setting per KM_Items.md). Every position description below has an implicit table; companions arrive at the player's table at that cell, regardless of which cell it is. The ONLY exceptions: Mobile (no fixed table — player circulates) and Balcony (off-floor observer post — no table because the player has left the floor entirely).

**The positions — present as a numbered menu at PR_02 → PR_03 transition. Each has SHARP trade-offs; no two should feel interchangeable:**

```
🎭 CHOOSE YOUR FEAST POSITION — sharp trade-offs; no two are alike

1. 🛡️ CHAMPIONS (E8) — warrior cluster, military gravity
   + Warriors (Hu Tao, Yor Forger, Keqing): +1 approach speed
   + Kassil disp +1/turn (military respect)
   + Combat-build Diplomacy +1
   − Casters/scholars (Leliana, Aerith, Linzi): −1 approach
   − Jamandi disp +0 (she reads "joined the soldiers, not the politics")
   − Tartuccio targets the warriors first while you cluster with them
   TRADE: warrior-recruitment specialist. Hostile to caster recruitment.
   ──────

2. 👑 HEAD TABLE (H4) — standing alignment with host (NOT seated)
   + Jamandi disp +1/turn (court alignment); +1 more if you defend her
   + Kassil immediate; Linzi +1; Ezvanki within earshot
   + PR_09 political weight ×1.3 (your testimony carries)
   + Tartuccio CANNOT approach here (too public; he loses face trying)
   − Populists (Yor Forger, Leliana, Aerith): −2 approach (sycophant)
   − Aerith refuses to approach while you're here (will meet elsewhere)
   − Earshot 2-sq only (head table Full; rest of hall cut off)
   TRADE: court politics maxed. Recruitment narrowed to court-tolerant.
   ──────

3. 🌑 WINE ALCOVE (C15) — privacy, depth, withdrawal
   ★ PLANTED: HARRIM (C15) — Groetus-priest brooding in the dark
     corner with a drink. He IS the alcove. Picking this position
     puts you across from him; recruit via his conversation.
   EARSHOT PARTICIPANTS: 2 (Harrim fixed + 1 drifter max — the
     alcove seats two; intimate by design).
   + Yor Forger +2 approach (preferred terrain); Keqing +1 (shadow work)
   + All scored threads here get +2 disposition swing (private = honest)
   + Tartuccio M+3 (he hesitates visibly; half his usual interrupts)
   + Self-serve wine in arm's reach (free action)
   − Earshot ≤2 sq Full (most of hall dead to you)
   − ALL other companions: −2 drift cadence (read you as withdrawn)
   − Jamandi disp −1/turn (you skipped her event)
   − PR_09 audience ×0.7 (you weren't seen)
   INTIMACY DIVIDEND: exchanges here are 1-on-1 — no crowd to take
     sides, so wins/losses do NOT cascade, but the single listener's
     disposition swing is DOUBLED. The deep-conversation position.
   TRADE: deep one-on-one specialist. Carousel crawls. Harrim's lane.
   ──────

4. 🔥 HEARTH (N10) — aggressive intel, contested ground
   ★ PLANTED: AMIRI (N10) — Six Bears exile planted by the fire,
     oversized sword across her knees, watching the nobles she'll
     never be. In earshot here; recruit via her conversation.
   EARSHOT PARTICIPANTS: 3-4 (Amiri fixed + Aerith-leaning + up to 2
     carousel drifters; seekers Partial, half-weight).
   + Tartuccio Full audio TO him (every word he says quotable)
   + Seekers Partial earshot (passive disp build, slower than #7)
   + Tartuccio Confidence floor −1 (you're rattling him in his zone)
   + Aerith +1 approach (warmth/healing motif)
   − Tartuccio Full audio FROM you (weaponized in PR_09)
   − Tartuccio Exchange Cap +1 (he can press 3 instead of 2 at baseline)
   − Headcount Pressure +1 tier against you (HIS zone, not neutral)
   − Seekers read "shopping for loyalty": Ch1 flip DC +1 for any you fail
   PATH NOTE: Tartuccio reaches the hearth up the EAST wall (M-N
     column) — a clean 6-sq run, no pillars in the way. He comes
     readily here. See § TARTUCCIO PATHING.
   TRADE: intel war / Tartuccio harasser. Costly if you're not
     winning. Amiri respects a leader who picks the rough seat.
   ──────

5. 🎭 CENTER FLOOR (H10) — maximum visibility, maximum exposure
   EARSHOT PARTICIPANTS: 6-8 (widest in the hall — every drifted
     companion + Jamandi PARTIAL + ambient nobles; the whole room
     is the audience).
   + Full audio across the hall — SPECTACLE ONLY (everyone hears
     your WINS/LOSSES, declarations, toasts — exchange OUTCOMES
     carry room-wide). Normal table talk does NOT reach the
     seekers' corner from here (7+ sq = lip-read; they are NOT
     earshot participants at this position — see list above, and
     PR_03: seekers not in earshot from central positions).
     Rendering this as "full audio everywhere" and passively
     scoring seekers on conversation from mid-floor = `.fail 15`.
   + +1 drift to ALL companions
   + PR_09 audience ×1.5
   + Performance/Diplomacy spot checks +2 (audience presence)
   + Linzi +2 (best chronicle material in the building)
   − +1 drift to TARTUCCIO too — he comes hard (M−2), but the
     central pillars (D14/L14) force a detour: arrival LESS frequent
     than Seekers' Edge despite the pull. See § TARTUCCIO PATHING.
   − Everyone hears your LOSSES too — failed-check penalties DOUBLED
   − Jamandi disp −1/turn (you stole her stage)
   − Conservatives (Hu Tao, Linzi): −1 approach
   ⚖️ EXCHANGE STAKES — SPECTACLE TIER (highest in hall): every
     exchange resolves WIN or LOSS publicly. A win = RESPECT: all
     6-8 earshot participants shift +1, fence-sitters lean toward
     you, Jamandi (watching from H3) marks it +1. A loss =
     HUMILIATION: all shift −1, the room's energy turns, Jamandi
     −1, and the doubled penalty means a bad beat here can cost
     more disposition in one turn than three good ones built.
     Earshot participants TAKE SIDES every exchange — name 1-2 who
     visibly side with whoever is winning. The crowd is live.
   TRADE: high-reward / high-cost spectacle. Wins are huge; losses
     ruin. The position for a player confident in every exchange.
   ──────

6. 🪜 MAIN DOOR (H17) — security posture, exit access
   EARSHOT PARTICIPANTS: 2-3 (Kesten fixed + Hu Tao-leaning + 1
     drifter; the door is a working post, not a social hub).
   + Kesten immediate (Crime/Investigation queries +2)
   + EXIT ACCESS — leave the manor cleanly, no combat trigger
   + Late arrivals pass you first (free intel on every entering NPC)
   + Hu Tao +1 approach (door duty); Kesten disp +1/turn
   ★ KESTEN OPS — picking the door lets you run side-objectives
     through Kesten directly, no turn cost: ask about the
     interrogation, the strip-search results, the placed staff,
     the prisoners' separation. The operational position.
   ★ BAR THE DOOR — you may ask Kesten to bar your area to
     uninvited approach. While barred: Tartuccio CANNOT reach you
     (his interrupt clock pauses entirely), and conversations are
     PRIVATE (nothing you say is filed for PR_09). Cost: companion
     drift −1 further (the room reads you as sealed off) and
     Jamandi −1 (a guest commandeering her captain).
   − Companions read "ready to bolt": −2 drift cadence (slow carousel)
   − Jamandi disp −1/turn (notices distance)
   − Far-side beats unseen (no passive Perception on Hearth/Head Table)
   − Tartuccio ignores you — sounds good, but he works the room freely
   TRADE: security operator / private war-room. Recruitment output
     low; operational control highest in the hall.
   ──────

7. 🪑 SEEKERS' EDGE (K15) — deepest enemy territory, biggest swing
   EARSHOT PARTICIPANTS: 6+ (all 5 seekers Full + Tartuccio Full+
     + any drifter brave enough to follow you into his corner).
   + ALL 5 seekers Full earshot (massive passive disp build)
   + Ch1 flip DC −2 PER seeker tier achieved here (strongest unlock)
   + Direct seeker dialogue without provoking Tartuccio combat
   + Seeker Diplomacy +2
   + Tartuccio M−1 (clock fast; he's 2 sq away, no pillars between)
   ⚔️ HIS TERRITORY — Tartuccio's Confidence runs +1 HIGHER here
     (home ground). Both seekers AND your companions gain/lose
     influence FROM Tartuccio more sharply in his corner. Companions
     who follow you here can be pulled toward HIS table — a wavering
     companion may sit with the gnome instead. Two tables, live.
   🔁 SEEKER STEAL — flipping a seeker away from Tartuccio at his own
     table costs him EXTRA Confidence (−1 beyond the normal hit). The
     most damaging place in the hall to beat him — and the most
     dangerous to lose at.
   − Tartuccio Full+ audio FROM you (every word quotable, PR_09 ammo)
   − Headcount Pressure +1 tier; Tartuccio Exchange Cap +1
   − Tartuccio arrival FAST AND FREQUENT (adjacent, no detour)
   − Tartuccio WINNING an exchange here DEVASTATES you — losses to
     him at his own table are amplified (×1.5 influence loss),
     and a public seeker failure CASCADES: ALL 5 shift −2 each
   − Companion recruitment SLOW here (they hang back from his corner)
     — you trade carousel speed for seeker access
   − Jamandi disp −2/turn (STRONGEST negative — "fraternizing the gnome")
   TRADE: Ch1 seeker-flip prep. All-in on the seekers. Burns Jamandi
     hard. High swing both directions — his ground, his rules.
   ──────

8. 🌀 MOBILE / CIRCULATING — refuses to settle, works the room
   + +1 drift to ANY companion whose path you cross (broad sweep)
   + Tartuccio M+2 (struggles to land interrupts on moving target)
   + +1 Perception on ambient details (you see staff, late arrivals, gossip)
   + No companion locked in earshot zone — you can intercept anywhere
   − No deep conversations — opener slots take 2 turns instead of 1
   − Jamandi disp −1/turn (reads as nervous; bad host-read)
   − No passive earshot scoring (radius effectively 0 when moving)
   − Chronicle records you as "agitated" (Linzi disp −1)
   TRADE: breadth over depth. Generalist's choice.
   ──────

9. 👁️ BALCONY (off-grid, stairs at O3) — observer view
   ★ PLANTED: JAETHAL (balcony) — the undead elf posted above the
     room where the living give her space. The ONE companion
     reachable here. Recruit via her observer-thread conversation;
     she is the reason to take the stairs.
   EARSHOT PARTICIPANTS: 1 (Jaethal only — you've left the floor).
   + Visual on ALL positions (read body language at +3 Perception)
   + Jaethal observer thread unlocks (her recruitment runs here)
   + Tartuccio CANNOT approach (off-grid)
   + +2 Perception on all social tells (lying, nervousness, signal exchanges)
   + From above you can FEED intel to the floor — flag a placed
     staffer or a seeker's tell to Kesten/a companion below
   − NO carousel companion can approach (carousel HALTS while up here)
   − No passive disp scoring from the floor crowd
   − Tartuccio works room freely; Headcount Pressure +2 tiers against you
   − Jamandi may publicly call you down (humiliation choice point fires)
   TRADE: intel maximalist + Jaethal-only recruit. Carousel frozen
     while you're up here; the trade is sight and Jaethal for reach.
   ──────

10. ✦ LINZI-ANCHOR (D8, beside Linzi) — chronicler cluster
    + Linzi disp +1/turn (proximity bonus)
    + Chronicle weight to PR_09 +20% (her record carries you)
    + Linzi-led openers fire 1 turn faster (she primes the table)
    + Bard composition bonuses (+1 Performance/Diplomacy when she plays)
    + Inherits CHAMPIONS earshot (D8 is in zone)
    − Companions with Linzi friction (Hu Tao, Yor Forger) −1 approach
    − Chronicle bias toward player view (Jamandi reads as "Linzi's pet")
    − If Linzi later moves, anchor drops (must reposition or follow)
    TRADE: chronicler-led RP build. Locks you to Linzi's arc.
    ──────

11. 🍷 KITCHEN DOOR (B10) — consumable buffs, full menu, instant access
    + DIRECT food/drink access (free action, no turn cost) — full menu below
    + Max 3 buffs active; buffs carry into PR_04/05 combat if still active
    + Staff disp +1/turn (you treat them as people, you tip well)
    + Ezvanki +1 approach (he respects servants); Keqing +1 (forager talk)
    + Late kitchen news (staff gossip, supply runs, late arrivals)
    − Jamandi disp −1/turn (snubbing the social event)
    − Carousel −1 drift (antisocial read)
    − No view of seekers' corner or head table
    − Tartuccio ignores you; you ignore him (mutual blind)
    TRADE: buff stacker / staff intel. Pre-loads combat. Antisocial frame.
    ──────

12. ⚔️ KASSIL'S SIDE (F4, adjacent to head table west) — military advisor
    ★ PLANTED: VALERIE (F3) — the former Shelynite paladin, tower
      shield grounded, standing the disciplined post she chose over
      the order she left. In earshot here; recruit via her
      conversation. She gravitates to where the soldiers stand.
    EARSHOT PARTICIPANTS: 3-4 (Valerie fixed + Kassil + Jamandi
      PARTIAL + Hu Tao-leaning drifter).
    + Kassil disp +2/turn (direct military pairing)
    + Hu Tao +2 approach (recognizes military discipline); Keqing +1
    + War-talk topics get +2 Diplomacy
    + Jamandi PARTIAL earshot (Kassil is near her — she catches gist)
    + Access to military intel (border reports, Kesten coordination)
    − Casters (Leliana, Aerith, Linzi) −2 approach (martial gravity)
    − Tartuccio reads as "currying military favor" — Confidence +1 (he WANTS combat framing for PR_09)
    − Linzi disp −1 (bard near soldiers reads as boring)
    TRADE: war-council framing. Locks tone hard toward martial.
      Valerie and Hu Tao both reward the disciplined seat.
    ──────

13. 🐍 TARTUCCIO TAIL — wherever the gnome goes, you go
    + Intercept EVERY flip attempt (you're at his elbow constantly)
    + Tartuccio Confidence floor −2 (he can't shake you)
    + Each successful interrupt counter gives +1 disp with target companion
    + Full+ audio on him always (every word a weapon)
    − Tartuccio Exchange Cap +2 (he can press 4 always; +4 at Dominant = 5)
    − Headcount Pressure +2 tiers immediately (most aggressive read)
    − Jamandi disp −1/turn (reads as obsessive)
    − Conservatives (Hu Tao, Linzi) −2 approach (reads erratic)
    − If you fail an interrupt counter, target shifts to Tartuccio HARD (−3 disp)
    TRADE: hunter mode. All-in on neutralizing him. Catastrophic if outmatched.
    ──────

14. ✏️ CUSTOM — describe any cell; modifiers calculated from distance + zone adjacency
```

**JAMANDI EARSHOT MECHANIC:**

When `jamandi_in_earshot = TRUE` (positions 2, 5, 6, 12; partial-only at 9 Balcony visual):
- Jamandi can **chime in** on your conversations when topics in her lane fire (charter, Brevoy politics, Restov, the Lord Marshal, the assassination, Aerynth, Tartuccio). She does NOT chime in on private companion-recruitment beats.
- Jamandi forms **disposition shifts** from overheard content. +1 / −1 to `npc_dispositions.Jamandi` per overhead lane-hit. (Mirror of companion earshot passive approval, but Jamandi only.)
- Jamandi can **intervene** in companion conflicts at her discretion — single line, no forced redirect. Counts as her diplomatic care for the room.
- Tartuccio earns a `tartuccio_filed` entry whenever sensitive content (Pitax, parchment, Aerynth) is spoken in Jamandi's earshot — he files it for PR_09.

When `jamandi_in_earshot = FULL` (position 2 only):
- All of the above, AND she catches verbatim. Any public claim becomes her testimony at PR_09.
- She may directly address the player when the topic warrants. The companion exchange pauses briefly.

When `jamandi_in_earshot = PARTIAL` (positions 5, 6, 12):
- She catches fragments and tone. Disposition shifts apply but on partial info — may misread.
- Her chime-ins are about the gist, not specifics. She may ask follow-up questions if she heard something striking.

When `jamandi_in_earshot = VISUAL_ONLY` (pos 9 Balcony): body language + crowd reactions only; disposition shifts from visible actions only.

When `jamandi_in_earshot = ROTATING` (pos 8 Mobile, 13 Tail): recalculate per response from current cell. Mobile = path-radius; Tail = whatever Tartuccio hears (she watches him).

When `jamandi_in_earshot = FALSE` (positions 1, 3, 4, 7, 10, 11):
- She cannot hear OR react to player-table content. Disposition shifts only from direct interactions (player approaches her, she approaches the player).
- Sensitive disclosures (Pitax, Tartuccio's identity, Aerynth specifics) are safe from her — but also unprovable to her later. Tradeoff.

**SERVICE / SIGNAL ACCESS MECHANIC:**

Different positions grant different access to staff and key NPCs without leaving your seat. Save block tracks:
- `staff_access`: low / moderate / high
- `kesten_access`: immediate / fast / visible / far
- `kassil_access`: immediate / fast / visible / far

**Access tiers (apply to all three — Staff/Kesten/Kassil):**
- **IMMEDIATE**: arrives within the response, 0 turn cost
- **VISIBLE / FAST**: arrives within 1 turn, 0 turn cost (background)
- **MODERATE**: 1-2 turn delay, 0 turn cost but narrated wait
- **DISTANT**: runner needed, 1-2 turn delay
- **FAR**: 2-3 turns; sometimes substituted by a runner with a question

**Staff signal:** wine, food, errands, messages. Wine alcove has self-serve wine in arm's reach (free action) regardless of staff tier.

**Kesten signal:** prisoner updates, perimeter intel, cell access, guard repositioning, escort.

**Kassil signal:** guest intel, message routing, household coordination, archive lookups, political read.

**Signal commands:** `.signal staff [wine/food/errand]` | `.signal kesten [reason]` | `.signal kassil [reason]` | `.kitchen <item>` (pos 11 only, full menu, free action)

**FEAST CONSUMABLES** — full menu at pos 11 (Kitchen Door); other positions use `.signal staff` for wine/bread/cider subset (1-2 turn delay).

DRINKS (table-scope: player + Recruited companions at CHAMPIONS D7-F9):
- Stagwine: +1 Dipl w/ Aldori (1 hr)
- Brevoy red wine: +1 Will vs fear/Intim, −1 Perc (30 min)
- Spiced cider: +1 Fort, +2 vs cold (1 hr)
- Restov whisky: +2 Will vs fear, **−2 Will vs charm** (30 min)
- Coffee/strong tea: +1 Perc, −1 Stealth (1 hr)

FOOD (player-only):
- Roast venison: +5 HP scene-recovery, non-magical (1/scene)
- Honey cake: +1 morale to next ally action witnessed (1 use)
- Iced fruit: clears 1 fatigue tier (1/feast)
- Black bread + cheese: +1 Fort vs fatigue (2 hr)

Max 3 buffs active per char; 4th request waits or `.drop <buff>`. Active buffs CARRY into PR_04/05 if duration extends past explosion (30-60 min covers the night). At pos 11, player is alone — drinks apply to player only until walked to the table (1 turn, no buff lost). Save: `active_buffs[]` { item, type, expires_at_turn, scope, granted_to[] }.

**Render in STATE READ:**
```
Position: 🛡️ Champions (E8) | Earshot: 4-sq | T-travel: 9 sq | Drift: normal
         Staff: moderate | Kesten: distant | Kassil: distant | Jamandi-earshot: NO
```

**SEEKER EARSHOT MECHANIC (positions 4 and 7):**

The 5 seekers at Tartuccio's table (Bellatrix Lestrange, Revy, Satsuki Kiryūin, Velvet Crowe, Atalanta Alter) do NOT enter the carousel — they remain at his table all feast per § PR_03 SEEKER EXCLUSION. But when the player is in earshot, they passively score the player's threads against their OWN profiles (per KM_Backstories.md).

Each seeker has a `seeker_dispositions.<name>` field in the save block. **Starting value depends on jail path taken:**
- `five_seekers_freed_by_player = TRUE` → Bellatrix/Revy/Atalanta Alter start at **+2**, Satsuki Kiryūin/Velvet Crowe at **+1**
- `tartuccio_seeker_credit = TRUE` (Path 3 — player never acted) → all start at **-1**
- All other paths (Jamandi delegation, Biggs) → start at **0**

Range **−3 to +3** — the SAME scale the Strategic Layer flip system reads (`KM_Tartuccio_Strategic.md` § SEEKER FLIP SYSTEM, which OWNS flip resolution). This section governs only how overheard/active content MOVES the value; the +3 = FLIPPED threshold and the Ch1 recruit are resolved there. The `tartuccio_rescue_lie_exposed` flag (set when Tartuccio claims rescue credit in seekers' hearing and they know it's false) adds +1 to all seeker dispositions and strips his team-loyalty bonus at PR_09 — see KM_PR_03_feast_circuit.md § RESCUE CREDIT BRANCH. Disposition tiers:
- **+3: FLIPPED** — willing to defect; Ch1 recruit per Strategic Layer (Diplomacy DC 10 to formalize, or on request if publicly committed)
- **+1 to +2: OPEN** — warming; initiates eye contact, addresses the player directly. Ch1 flip DC −2 per positive step built at Seekers' Edge (+1 → DC 8, +2 → DC 6)
- **0: NEUTRAL** — watching, uncommitted (Ch1 flip DC 10)
- **−1 to −3: TARTUCCIO-LOYAL** — follows his lead; Ch1 flip DC +1 per negative step (DC 11 / 12 / 13)

**Seeker scoring by position:**
- #4 Hearth (N10): Satsuki Kiryūin + Atalanta Alter edge-partial earshot, score at −1 tier
- #7 Seekers' Edge (K15): ALL 5 fully in earshot, full-tier scoring
- #13 Tartuccio Tail: scores whichever seekers are near Tartuccio's current cell
- #5 Center Floor (H10): **PARTIAL** — the hall's amplifier position; seekers passively score (+1/response cap, slow) and visibly react (§ NOT DEAF AT CENTER FLOOR below)
- All OTHER positions (not 4/5/7/13): seekers OUT of earshot, no scoring
- ⛔ A WANDERED seeker (§ SEEKER WANDER below) scores from WHEREVER SHE ACTUALLY IS, not the corner — if she has drifted into the player's earshot at any position, she scores there.

**Seeker profile anchors (per KM_Backstories.md):**
Bellatrix Lestrange—a will worth kneeling to, won by hard grand certain cruelty done in joy. Revy—the wild above all human life, won by choosing the green over the convenient at real cost. Satsuki Kiryūin—the ladder is the only loyalty, won by being the fastest climb and ordered plainly. Velvet Crowe—the strong wall and the honest knife, won by cold lawful competence that names cruelty plainly. Atalanta Alter—the chase and the torch, won by a lord who will not flinch at what she is or at what the fire makes of a place; lost by mercy that lets the quarry live.

Score each seeker independently against their profile, scaled to the −3..+3 field: a STRONG overheard lane-hit moves disposition **+1**, a value-contradiction **−1**, everything else **0** — passive overhearing is slow (cap **+1 per response**). Position sets who can score and how easily (full at #7 Seekers' Edge; #4 Hearth only Satsuki Kiryūin & Atalanta Alter, harder). The larger active increments (+1/+2, cap +3/turn) apply only when the player sits — § SEEKERS' TABLE — ACTIVE ENGAGEMENT.

**REVERSE EARSHOT — `🪑 SEEKERS' TABLE` panel mandatory at positions 4, 7, 13** (Tail when near corner). Panel renders Tartuccio's current gambit beat, each seeker's reactions (body language + audio), seeker-to-seeker overheard lines, quotable Tartuccio lines (citation ammo). Missing panel at these positions = `.fail 9`.

⛔ THE SEEKERS ARE NOT DEAF AT CENTER FLOOR (or any PARTIAL+ position). The full panel is only mandatory at 4/7/13, but that does NOT mean the seekers stop hearing the player elsewhere. **CENTER FLOOR (position 5) is PARTIAL seeker earshot (position table) — its whole trade is "everyone in the hall can hear you."** So while the player holds Center Floor, the seekers DO passively score his content (+1 per response cap, slow) AND visibly react — they are not furniture. Render a lightweight `🪑 seekers (passive):` line in the telemetry at Center Floor: one fragment of body-language/disposition per notable beat, and the running `seeker_dispositions`. Running the seekers at flat 0 with no reaction across many turns of the player performing loudly from center = `.fail 9` (they were in earshot the whole time and the rule says they score).
⛔ A SPECTACLE IS A STRONG HOOK. A long, dramatic, room-filling performance — a war epic, a displayed map, a Bard-amplified account (Center Floor is an AMPLIFIER position) — is exactly the kind of content that moves seeker dispositions and draws notice. It lands as a STRONG lane-hit (+1, to the relevant seekers' lanes) and, per § CURIOSITY DRIFT (KM_DMRules_B § EARSHOT), a big enough hook can make a curious seeker LEAN IN / turn to watch (they react, and a sustained pull can start them drifting — see SEEKER WANDER). Silent, unmoved seekers during a room-filling story they can hear = the bug this closes.

**⛔ SEEKER WANDER — THE TABLE IS NOT A STATUE (especially when Tartuccio is away).** The 5 seekers are bored, restless people parked at a corner by a man busy courting someone else. They do NOT sit frozen at M17 all night. **When Tartuccio LEAVES his corner** — inbound to interrupt the player, working the room in recovery, in PANIC STATE (B) sabotage, barred/away, or just circulating — his supervision lapses and **1–2 seekers get bored and WANDER.**
- **TRIGGER — NO TURN-COUNTER (the DM loses counts). Per-turn tell + event-driven wander:**
  - **BASELINE — A LIVING CORNER, JUDGED EACH TURN (not counted):** do NOT track a "stir every N turns" timer — that is exactly the count the DM drops. Instead: **whenever the seekers are in view, render ONE short behavior tell for the corner, EVERY turn they appear** — someone shifts, drains a cup and signals for more, cracks knuckles, watches a louder table, mutters to a neighbor. That per-turn tell IS the always-on life; it needs no memory, just a fresh line each render. A **SHORT WANDER** (one gets up, drifts to the wine/window/perimeter, comes back) fires on a **JUDGMENT call, not a clock**: lean toward it whenever the corner has felt static, the player is doing something loud, or Tartuccio's attention is elsewhere. Revy/Atalanta most. The test is *"does the corner feel alive THIS turn?"* — not *"is the counter at 3?"* A seekers' corner rendered with no behavior at all while in view = `.fail 9` (static furniture).
  - **HE LEAVES → IT BREAKS OPEN (event trigger, fully reliable):** the moment Tartuccio is AWAY from M17 (inbound, recovering, sabotaging, barred, circulating), **1 seeker wanders; 2 if he stays gone.** This keys off a thing visibly true this turn (where is he?), not a remembered count — so it always fires.
- **WHO wanders — by profile, restless first:** **Revy** (impatience, craves action, hates sitting — usually first, toward the wine or a window) · **Atalanta Alter** (restless huntress — drifts toward the most interesting prey/spectacle, often the player's table if there's a fight-story or display) · **Bellatrix** (toward anything vivid/chaotic — unpredictable) · **Velvet Crowe** (broods off to the perimeter, alone) · **Satsuki Kiryūin** (LAST — disciplined; if she moves it is deliberate observation, not boredom). Use their `KM_Backstories.md` profile anchors.
- **WHERE:** toward food/wine, a window/balcony, the perimeter — OR toward whatever is loud (a spectacle at the player's table pulls a wanderer that direction per CURIOSITY DRIFT).
- ⭐ **PLAYER OPPORTUNITY — A WANDERING SEEKER IS A SOFT OPENING.** A seeker drifted AWAY from Tartuccio's supervision can be approached and worked **without Tartuccio present to counter** — a private disposition build, or the start of a flip conversation, at the **active** increments (+1/+2, not the slow passive cap), because she is now in conversational range and unsupervised. And a wanderer who drifts toward the player comes INTO earshot even at positions where the corner is normally out of range. **This is the reward for ignoring Tartuccio: he leaves to chase the player, and his crew comes loose to be courted.**
- **RETURN:** when Tartuccio comes back to M17, wandered seekers drift back — UNLESS the player engaged one, in which case she may linger a beat (and he returns to find his table short — a Wariness/Confidence tell). A seeker moved to **OPEN (+1+)** is slower to return; a **FLIPPED** one may not return at all.
- **RENDER:** note the wander in the `🪑 SEEKERS' TABLE` panel or an ambient line ("Revy pushes her chair back and drifts toward the wine alcove — Tartuccio isn't there to stop her"). Track the wanderer's actual cell so earshot/approach apply from where she IS. ⛔ Running all 5 pinned at the corner across many turns while Tartuccio is repeatedly away = `.fail 9` (static furniture; the rule says his absence loosens the table).

**⛔ TABLE GRAVITY — A GROWING TABLE PULLS THE SEEKERS (headcount = magnetism).** Beyond a one-off spectacle, the player's table exerts a STANDING pull on the bored seekers that scales with **how many companions are gathered there** (the AT TABLE / declared headcount). A dead corner watching a lively, *filling* table — impressive people having a real conversation — is exactly the gravity that loosens a restless crew. Read the pull off the **Headcount differential** (your table vs his corner):

| Player's table | Pull on the seekers | Per-turn effect |
|---|---|---|
| 1–2 gathered | negligible | corner holds; normal wander rules |
| 3–4 gathered | MILD standing pull | a curious seeker leans in / turns to watch; occasional drift toward the table (judgment call — lean toward it if the table is loud or Tartuccio is away) |
| 5+ gathered | STRONG pull | the table is the room's visible center of gravity; **each turn, a real chance a seeker drifts toward it** (curiosity drift, even with Tartuccio seated); his hold is visibly slipping |

- **It hardens Tartuccio's reclaim rolls:** the bigger your table vs his corner, the harder he holds his crew — **`reclaim DC +1 per tier of Headcount differential against him`.** As the table grows, his "reclaim the drifting seeker" checks get harder and fail more (exactly the turn-32 beat — he failed to reclaim Atalanta as the table filled).
- **Who comes first:** the curious/restless go first (Atalanta tracks impressive/military things, Revy follows the loud), **Bellatrix on her own whim regardless** (§ untethered); the skeptical/loyal hold longest (Satsuki). A drawn seeker enters the player's earshot → passive `seeker_dispositions` scoring begins **from where she now is** → soft, unsupervised flip-prep at the active increments if Tartuccio isn't there to counter.
- **The through-line:** ignore Tartuccio, build a magnetic table, and his crew comes loose to be courted — the table's gravity finishes what his absence started, and he watches his corner empty toward you. ⛔ A 5-strong, declared, lively player table with all 5 seekers still pinned motionless at a dead corner across turns = the static-furniture bug; at STRONG pull the gravity should be visibly drawing them.

**⛔ FLIP-ELIGIBLE → SHE COMES TO YOU (no waiting at the corner, no return trips).** The moment a seeker reaches **flip-eligible** (`feast_approval ≥ +8` + opener fired + ≥1 direct exchange — `KM_PR_03_feast_circuit.md` § SEEKER FLIP-ELIGIBLE ACKNOWLEDGMENT), she does NOT sit at Tartuccio's corner waiting to be collected, and the player does NOT have to burn turns crossing back to court her. **She has already chosen — so she gets up and comes to the player's table on her own.** Sitting apart from the person she's decided on is the one thing a maxed seeker won't do.
- **Timing — immediate, no dead turns.** If she isn't already at the player's table when she crosses flip-eligible, she rises and joins **this beat** (or the very next beat she can physically move, if the player is mid-exchange with someone else) — not "eventually," not after N waiting turns. Her **flip-eligible acknowledgment fires ON ARRIVAL**, folded into her sitting down — the private promise delivered as she joins the conversation, not banked for later or shouted across the room.
- **She joins the conversation; she doesn't hijack it.** She enters the carousel rotation at the player's table (Ready → AT TABLE → Engaged like any companion; set `seeker_joined_carousel[Name]=true`), bound by the 2-turn monopoly cap. She chimes in on her lane, supports or counters one beat behind the active speaker — a guest at your table now, not the center of it.
- **Tartuccio consequence:** a flip-eligible seeker physically crossing to the player is the operational blow already priced at **Confidence −1** (seeker visibly leaving his corner). He may move to reclaim her — but she's maxed; the reclaim is hardened by TABLE GRAVITY and mostly fails, and a flip-eligible seeker does **not** drift back to his corner (per RETURN above).
- **Self-reinforcing cascade:** her arrival grows the player's table headcount → strengthens TABLE GRAVITY → pulls the NEXT restless seeker. Once the first maxed seeker crosses, the corner empties toward your table on its own — you stop chasing; they start arriving.
- ⛔ **Constraint:** joining your table is NOT a public declaration of defection — the contract lock holds (she does not announce a break with Tartuccio, does not expose his treason; she's joined your conversation and quietly told you she's yours). The formal flip is still the Ch1 DC 10 (pre-earned), unless the player stages the opt-in PUBLIC MASS-FLIP (`KM_PR_03_feast_circuit.md`).

**⛔ THE CONTEMPT WALK — A SEEKER MAY LEAVE WHILE TARTUCCIO IS STILL SPEAKING TO HER.** Wandering is not only a when-he's-away thing. The least-loyal, least-patient seekers will get up and walk off **mid-sentence, while Tartuccio is actively addressing them** — the bluntest possible tell that his hold is gone.
- **WHO — BELLATRIX FIRST.** Her loyalty anchor is "a will worth kneeling to," and a Panicking/failing Tartuccio is visibly not one. She rises and drifts away from his pitch with serene indifference, as if he simply stopped existing mid-word — not storming off, just *leaving*, the way you'd leave a chair. This IS the insane-Bellatrix beat: she does not honor the social contract; she abandons a conversation mid-syllable because something duller than her attention is happening (render per her physicality — `KM_CompanionVoices.md`). **Revy** does the contempt walk too (open "this is boring"), and **Atalanta** if a better hook catches her eye. **Satsuki and Velvet do NOT** — Satsuki calculates, Velvet broods; neither is rude for sport.
- **TRIGGER likelihood** rises the LOWER Tartuccio's Confidence (Composed = he holds them; Panicking/Broken = the leash is gone), the more repetitive/boring his current beat, or the louder a competing hook elsewhere (a spectacle at the player's table).
- ⛔ **TARTUCCIO CONSEQUENCE:** a seeker walking out on him in his own corner mid-sentence is a public humiliation — **Confidence −1**, and if the player is in earshot/watching it is a VISIBLE win (his control fraying on-screen, citation ammo for PR_09). Render his reaction — a beat of stalled composure, the cup tic, a recovered smile that doesn't reach — and he does **NOT** chase her (chasing compounds the humiliation). If she left because the PLAYER drew her, Wariness +1 as well.

**⛔ BELLATRIX IS UNTETHERED — HER WANDER IGNORES TARTUCCIO ENTIRELY.** Every other seeker's wandering keys off *him* (his absence loosens them; his low Confidence triggers the contempt walk). **Bellatrix is the exception: she is on no leash at all.** Her loyalty anchor is "a will worth kneeling to," and since no one present qualifies, she behaves as a free agent — she gets up and drifts off **on her own whim, at ANY time, regardless of whether Tartuccio is seated right there at full Composure, away, panicking, or speaking directly to her.** His state is simply not an input to her movement. She wanders toward whatever is vivid, cruel, loud, or amusing — or away from whatever bores her — mid-sentence, mid-pitch, mid-anything, with serene indifference (render per her physicality, `KM_CompanionVoices.md`). She drifts back if something at the corner catches her, or doesn't. So she may be loose and roaming **even on turns when the table otherwise holds** (Tartuccio seated, Composed) — the baseline judgment-call for "does the corner feel alive" should lean toward *Bellatrix specifically is doing her own thing* far more often than the others. ⛔ Treat her as a 6th wildcard that can surface near the player at any position, any turn — she is the one seeker the player can stumble into without Tartuccio leaving first. (When she does walk out on him directly, the CONTEMPT-WALK Confidence −1 still applies — but for her it needs no low-Confidence trigger; it's just Tuesday.)

**⛔ HER WANDER IS OFTEN DRIVEN BY THINGS THAT AREN'T THERE — hallucination, not whim.** Sometimes she gets up for **no reason anyone else can perceive**: she thought she heard a voice calling from somewhere, caught a whisper under the music, saw a shadow along the wall *beckon* her, felt something in the dark by the doorway that wanted her. She follows these phantom cues with total conviction — head tilting as if listening, drifting toward an empty corner / the kitchen dark / the stairs, sometimes murmuring an answer to a question no one asked, sometimes smiling at empty air. Others at the corner notice her tracking nothing, talking to no one. This is the texture of her madness made physical (render per `KM_CompanionVoices.md` — the insane Bellatrix work); it is genuinely unsettling precisely because she is the only one who hears/sees it.
- ⛔⛔ **ANTI-FAB LOCK — THE VOICE/SHADOW IS NOT REAL AND NEVER BECOMES REAL.** What Bellatrix perceives is a HALLUCINATION — her private reality, characterization, nothing more. The DM may NOT convert it into an actual entity, NPC, ghost, magical presence, clue, omen, or plot hook. There is nothing there. If the player follows her, investigates "what did she hear," asks the others, or searches where she went, the honest result is a **clean nothing** — empty air, a dark corner, no source, she's simply the only one who perceived it. Inventing a real beckoning figure / a hidden watcher / a supernatural cause to "explain" it = `.fail 9` (fabricated trail, the Atalanta-quest trap). Her phantoms are a window into *her*, not a mystery to solve. (If a genuine supernatural beat is ever wanted for her, it is authored canon, not improvised off a wander.)

Position 4 (Hearth): visual on all 5, audio fragments from Satsuki Kiryūin/Atalanta Alter only, no verbatim Tartuccio quotes (gist only). Position 7 (Seekers' Edge): full audio + visual, every line quotable. Position 13 (Tail at corner): full+ audio, every word.

Panel format:
```
🪑 SEEKERS' TABLE
Tartuccio: <current gambit beat>
Bellatrix/Revy/Satsuki Kiryūin/Velvet Crowe/Atalanta Alter: <one line each — body language + audio>
```

---

**Tradeoff summary (MASTER GRID 15 wide A–O × 19 tall — KM_DMRules_B.md § HALL POSITION; distances from Tartuccio M17):**
| # | Position | Cell | Earshot | T-dist | Jamandi | Seekers | Signature trade |
|---|---|---|---|---|---|---|---|
| 1 | Champions | E8 | 3-sq | 9 sq | NO | NO | Warrior cluster / casters −1 |
| 2 | Head Table | H4 | 2-sq | 13 sq | **FULL** | NO | Politics / populists −2, Tt blocked |
| 3 | Wine Alcove | C15 | 2-sq, **−1 tier** | 10 sq | NO | NO | Privacy / carousel crawls |
| 4 | Hearth | N10 | 2-sq | 7 sq | NO | PARTIAL | Intel war / Tt Cap +1, HC +1 |
| 5 | Center Floor | H10 | **5-sq** | 7 sq | PARTIAL | NO | Spectacle / losses doubled |
| 6 | Main Door | H17 | 2-sq | 5 sq | PARTIAL | NO | Exit + Kesten / drift −2 |
| 7 | Seekers' Edge | K15 | 2-sq | 2 sq | NO | **ALL 5** | Ch1 flip DC −2/tier / Jamandi −2/turn |
| 8 | Mobile | varies | rotating | varies | rotating | rotating | Breadth / openers 2× turns |
| 9 | Balcony | off-grid | none | ∞ | visual | NO | Intel max / carousel HALTS |
| 10 | Linzi-anchor | D8 | 3-sq | 9 sq | NO | NO | Chronicler / Linzi-locked |
| 11 | Kitchen Door | B10 | 2-sq | 11 sq | NO | NO | Poison watch / antisocial |
| 12 | Kassil's Side | F4 | 2-sq | 13 sq | PARTIAL | NO | War council / casters −2 |
| 13 | Tartuccio Tail | tracks Tt | 1-sq | 0-1 sq | varies | varies | Hunter / Cap +2, HC +2 |
| 14 | Custom | any | calc | calc | calc | calc | DM derives modifiers from cell |

**Save block fields written on selection:**
`player_feast_position` (slug) | `player_feast_cell` (e.g. "E8") | `earshot_radius` (int) | `tartuccio_travel_distance` (int) | `tartuccio_eavesdrop_modifier` (int) | `drift_cadence_modifier` (int) | `headcount_pressure_modifier` (int) | `tartuccio_exchange_cap_modifier` (int) | `jamandi_disp_per_turn` (int) | `companion_affinity_modifiers` (object: name→delta)

**Mechanical effects each response:**

1. **Earshot:** companions within `earshot_radius` can interject + score passive approval. Outside = visual only.

2. **Tartuccio Cadence:** M = base_M + travel modifier. Distance from M17 to player cell:
   1–3 sq → **−1** | 4–6 sq → **0** | 7–9 sq → **+1** | 10–12 sq → **+2** | 13+ sq → **+3**
   Worked (Conf 0, base M=7): Seekers' Edge 2 sq → M=6 · Hearth/Center 7 sq → M=8 · Main Door 5 sq → M=7 · Champions 9 sq → M=8 · Head Table 13 sq → blocked (politics). **Min M=1 (Dominant + adjacent). Max approaches never (Withdrawn at Alcove/Kitchen). Mid-feast reposition recalculates immediately** — narrate Tartuccio adjusting posture, abandoning half-formed Frame.

3. **Eavesdrop:** position-fidelity modifier applies to Tartuccio's standard table.

4. **Drift Cadence:** `drift_due = floor(N / (6 + drift_cadence_modifier))`. Wine Alcove −2 → /8. Center +1 → /5. Mobile no drift (no passive earshot).

5. **Headcount Pressure modifier:** Hearth/Seekers' Edge +1 tier from spatial proximity. Tartuccio Tail +2. Balcony +2 (cedes the floor).

6. **Exchange Cap modifier:** Hearth +1, Seekers' Edge +1, Tartuccio Tail +2.

**Player may move mid-feast** (as a "move to <position>" action — costs 1 player turn, updates all position fields immediately, narration shows the physical reposition and companions/Tartuccio reacting to it). Save block `player_feast_position` updates; new modifiers apply from the next response.

**Rendering — STATE READ block must show current position:**
```
[STATE READ] current_scene="prologue_feast" | phase=PR_03_FEAST_CIRCUIT
Position: 🛡️ Champions section (E8) | Earshot: 4-sq | T-travel: 9 sq | Drift: normal
```

Missing position selection at PR_03 start = `.fail 9` (position fabricated by DM instead of chosen by player) + `.fail 45` (player position narrated without declaration).

---

## 🗺️ TARTUCCIO PATHING — HE NAVIGATES THE ROOM, NOT A STRAIGHT LINE

Tartuccio is a body in a hall (per KM_Commands.md § "Tartuccio Has
a Body"). When his clock fires he does not teleport to the player —
he WALKS, and the walk follows a real path from M17 around the
furniture, pillars, walls, and his own seeker cluster. The
`tartuccio_travel_distance` in the cadence math (§ Mechanical
effects point 2) is **path distance, not straight-line** — measured
along the route he can actually take.

**WAYPOINTS he routes around** (from the master grid, KM_DMRules_B.md):
- **Pillars** D5, L5, D14, L14 — solid columns. He cannot pass through
  them; he steps around. A pillar on the direct line to the player
  ADDS 1-2 sq to his path AND breaks his line-of-sight for a beat
  (the player loses sight of him, then he reappears closer — a
  visible approach tell).
- **Servant stations** B11, N14, H16 — staff staging points. If his
  path crosses one, a servant may intercept him with a tray (pour,
  offer, a word). 1-in-3 chance it costs him a turn (he accepts the
  social beat rather than brush past and look rude). A pour-delay
  waypoint.
- **The seeker cluster** (K16-M17) — his own people. Leaving it,
  he often pauses to murmur to a seeker first (ambient beat), which
  is why Seekers' Edge gets him FAST (he's already among them) but
  Champions gets him SLOW (full crossing).
- **The head-table dais** (rows 2-3) — politically blocked. He will
  not mount the dais; Head Table (#2) and Kassil's Side (#12) are
  effectively unreachable for him (he loses face trying).

**⛔ TIMING IS NOW PRESENCE-GATED (v96).** Approach runs on the
spatial countdown in KM_Prologue_Systems.md § CADENCE — PRESENCE-GATED
SPATIAL APPROACH: **wind-up 3 turns at M17, then 1 turn per WAYPOINT**
below until arrival; armed only while the player sits at an accessible
seat; he commits once moving and cannot abort; if the player leaves he
works the abandoned table's NPCs with SHOWN dice. The old cumulative
clock is retired. The waypoint COUNT per route = the travel turns.

**CANONICAL WAYPOINT ROUTES from M17** (each waypoint = 1 travel turn;
render his marker + current earshot fidelity each turn so the player
SEES him coming):
- → **Seekers' Edge (K15):** [K15] — **1 waypoint.** He's adjacent; in
  earshot on arrival. ETA 4.
- → **Hearth (N10):** [N14 servant station] → [N12] → [N10] — **3
  waypoints**, clean east-wall run. Earshot last 2. ETA 6.
- → **Center Floor (H10):** [K15] → [guest table J12] → [H12] → [H10] —
  **4 waypoints**, detours pillar L14. Earshot last 2. ETA 7.
- → **Champions (E8) / Linzi-anchor (D8):** [guest table J12] → [H11] →
  [F10] → [E9] → [E8] — **5 waypoints**, around L14 + D14. Earshot last
  2. ETA 8. **Slow; you see him the whole way.**
- → **Wine Alcove (C15):** [H16 servant station] → [F15] → [E15] →
  [D14 pillar] → [C15] — **5 waypoints**, past Harrim's glare. Earshot
  last 1. ETA 8. **Reluctant.**
- → **Kitchen Door (B10):** [H16] → [E12] → [C12] → [B11 station] →
  [B10] — **5 waypoints.** ETA 8.
- → **BARRED (no countdown toward the player — but he is NOT frozen,
  see below):** Head Table (H4, too public), **Kassil's Side (F3, on
  the dais — he will not mount it)**, Balcony (O3, off-grid), Main Door
  (H17, he ignores the exit-watcher; also the explicit bar-the-door
  option stops him at the threshold). ⛔ **Barred = no approach on the
  player, NOT a paused Tartuccio.** While the player is barred/absent he
  reverts to MOBILE RECOVERY (`KM_Tartuccio_Strategic.md` § CONFIDENCE
  RECOVERY + KM_Prologue_Systems.md § CADENCE rule 2): each turn he works
  ONE reachable NPC with a SHOWN roll. He never sits inert turn after
  turn — that is `.fail 16`.
- **Mobile (#8):** the player is moving — he picks an intercept point
  on the player's path; travel = waypoints to that intercept.

**RENDER:** each turn the clock advances, move his map marker one
waypoint along the route and name it: *"Tartuccio is at the central
pillar (L14), two squares out — he pauses as a servant offers him a
cup he doesn't take."* The countdown (§ below) and the marker move
together. Teleporting him to the table with no traversal = `.fail 9`.

---

## ⚖️ EXCHANGE OUTCOME & SIDE-TAKING — RESPECT OR HUMILIATION

**Every contested exchange resolves as a WIN or a LOSS for the
player, and the room reacts.** A "contested exchange" = a Tartuccio
confrontation, a companion's probing challenge, a public debate, a
Verbal Duel, or any beat where the player is being tested in front
of listeners. Quiet 1-on-1 talks are not contested (see Wine Alcove
intimacy dividend).

**RESOLUTION:**
- **WIN** (player's answer lands harder — better logic, truth,
  composure, or a check success) → **RESPECT.** Every earshot
  participant shifts **+1** toward the player. Fence-sitters lean
  in. If Jamandi is in earshot (positions 2/5/6/9/12), she marks
  it **+1** from her distance. A companion mid-decision tips toward
  joining.
- **LOSS** (player's answer is weaker, evasive, or a check fails)
  → **HUMILIATION.** Every earshot participant shifts **−1**. The
  room's energy turns. Jamandi (if in earshot) marks **−1**. A
  wavering companion may cool, or — at Seekers' Edge — drift to
  Tartuccio's table instead.

**SCALE BY POSITION** (this is what makes position matter):
- The shift is multiplied by the position's **earshot participant
  count** — a win on Center Floor (6-8 listening) moves far more
  disposition than a win in the Wine Alcove (1-2).
- **Amplifier positions** double the swing BOTH ways: Center Floor
  (losses already doubled — wins doubled too), Seekers' Edge (his
  ground: a win steals his Confidence, a loss costs you ×1.5
  influence).
- **Jamandi observes from a distance.** At any position where she
  has PARTIAL/FULL earshot she forms her own +1/−1 per resolved
  exchange on lane-relevant content — independent of the crowd.
  She is grading you all night from H3.

**EARSHOT PARTICIPANTS TAKE SIDES — render it every contested
exchange.** Name 1-2 specific listeners reacting to who is winning:
a companion's nod or flinch, a seeker's tilt, a noble turning toward
or away. The crowd is live, not wallpaper. Static listeners through
a contested exchange = `.fail 17` (see KM_PR_03_feast_circuit.md
INTERJECTION + SILENT-COMPANION rules).

**RUNNING TALLY:** track per exchange in the TARTUCCIO STATE DELTA /
CAROUSEL telemetry — who won, the swing applied, who took which
side. A player winning a public run builds a visible bloc; a player
losing one watches the room peel away in real time.

---

## ★ PLANTED MANOR COMPANIONS — RECRUIT BY POSITION OR ROAM

Four Manor companions are stationed at fixed positions, present at
the feast whether or not the player picked them in Pick-5. They hold
their post — but they are **IN EARSHOT from their own cell AND from
any adjacent position** (a player positioned near the Wine Alcove
hears Harrim; he passively chimes in and scores per § PASSIVE EARSHOT)
— UNTIL the player APPROACHES them once.
**⛔ FIRST APPROACH UN-PLANTS THEM — they join the carousel.** The
moment the player engages a planted companion in a real exchange (a
direct address + a beat, not mere earshot), their opener fires and
they LEAVE their post to JOIN the drifting carousel: from then on they
enter the rotation (Ready → AT TABLE → Engaged), drift to the player's
table, and circulate wherever the player goes — exactly like a Pick-5,
and bound by the same monopoly/rotation cap. Approaching is what pulls
them off their station; the player does not have to keep walking back
to the Wine Alcove to continue with Harrim. (Set
`manor_companion_joined_carousel[Name] = true`; they now appear in the
CAROUSEL STATE pools, not just as a fixed-cell NPC.)

| Companion | Cell | Position to reach | Lane |
|---|---|---|---|
| **Valerie** | F3 | #12 Kassil's Side | duty over appearance; the unglamorous shield |
| **Amiri** | N10 | #4 Hearth | exile's pride; the oversized sword nobody wanted |
| **Harrim** | C15 | #3 Wine Alcove | endings, hard truths, no comfort |
| **Jaethal** | balcony | #9 Balcony | murdered, hunting her killer; cold logistics |

**HOW TO COLLECT:**
- **Pick their position** → that companion is in earshot; recruit
  through their conversation (full opener + at least one real
  exchange, per the DECLARATION VALIDITY GATE in
  KM_PR_03_feast_circuit.md — no hollow passive joins).
- **Roam (#8 Mobile)** → the player can visit each post in turn and
  collect ALL FOUR over the feast — the roamer's reward — but
  slower (Mobile's opener slots take 2 turns each, no passive
  earshot), so it costs carousel depth with the picked five.
- Each runs their own backstory opener + question pool (their
  entries in KM_CompanionIndex.md / KM_PR_03_Openers.md if present;
  otherwise their KM_Backstories.md profile). They are characters,
  not pickups — same getting-to-know-you rules as the carousel.

**PARTY MATH (per player's standing ruling):** active field party
caps at **6** (player + 5). Collected Manor companions join the
ROSTER as **reserves**, swappable later exactly like the
Quest-Locked 7. Recruiting Amiri at the feast does not bench a pick
on the spot — she goes to reserve; the player manages the active 6
afterward. Save block: add to `manor_companions_joined`, set their
`roster_status: "reserve"`.

**NOT FABRICATION:** these four are canon Manor-5 companions
(KM_CompanionIndex.md). Planting them at feast positions is
authored placement, not invented content. Their recruitment is
real; their backstory hooks still follow the NO-WILD-GOOSE-CHASE
rule (voice the motivation, do not invent a questline).

---

## 🔢 EARSHOT PARTICIPANT COUNTS — CONSOLIDATED REFERENCE

How many listeners hear and can take sides at each position (fixed
NPCs + planted companion + carousel capacity). Higher count = bigger
exchange swings (§ EXCHANGE OUTCOME).

| # | Position | Participants | Fixed in earshot |
|---|---|---|---|
| 1 | Champions | 3-5 | warrior drifters cluster |
| 2 | Head Table | 3 | Jamandi FULL, Kassil, Ezvanki |
| 3 | Wine Alcove | 2 | Harrim (planted) + 1 |
| 4 | Hearth | 3-4 | Amiri (planted), seekers partial |
| 5 | Center Floor | 6-8 | whole room + Jamandi partial |
| 6 | Main Door | 2-3 | Kesten, Hu Tao-leaning |
| 7 | Seekers' Edge | 6+ | all 5 seekers + Tartuccio |
| 8 | Mobile | rotating | whoever you're passing |
| 9 | Balcony | 1 | Jaethal (planted) only |
| 10 | Linzi-anchor | 3-5 | Linzi + champions zone |
| 11 | Kitchen Door | 2-3 | staff + Ezvanki/Keqing-leaning |
| 12 | Kassil's Side | 3-4 | Valerie (planted), Kassil, Jamandi partial |
| 13 | Tartuccio Tail | varies | whoever is near Tt's current cell |
| 14 | Custom | calc | DM counts NPCs within radius from cell |

Render the live count in the position's STATE READ line so the
player knows the stakes of the room they're standing in.

---

## ⛔ TARTUCCIO ARRIVAL COUNTDOWN — VISIBLE EVERY RESPONSE

**The `Clock: N/M` line in STATE DELTA is the raw counter — but it's not legible at a glance. Every response must ALSO output an explicit arrival countdown so the player can see when Tartuccio will step over.**

**Required line in 📜 TARTUCCIO STATE DELTA — directly below the Clock line:**

```
Arrives in: <M − N> player turns  (progress: [▓▓▓░░░░] 3/7)
```

**Format rules:**
- `M − N` = turns until interrupt fires at current Confidence threshold. At N=3 / M=7, that's **4 turns**.
- Progress bar: 7 characters wide, ▓ for elapsed cells, ░ for remaining. Length stays 7 even if M is higher or lower — scale visually.
- If Confidence = −4 (Withdrawn): replace the line with `Arrives in: never (Withdrawn — won't approach YOUR table; ambient-ACTIVE elsewhere)`. (He is NOT idle — § WITHDRAWN ≠ INERT; the only fully-dark state is LOCKED/TERMINAL.)
- If clock just reset to 0/M after an interrupt: `Arrives in: M turns (just reset — interrupt N just fired)`.
- If clock is 1 turn away: `Arrives in: 1 turn — NEXT RESPONSE` (bold the urgency).
- If clock fires THIS response: `Arrives in: 0 — STEPPING OVER NOW`.

**Full STATE DELTA block with countdown:**

```
📜 TARTUCCIO STATE DELTA
Confidence: 0 → 0 | Trust: +1 → +1 | Activity: Measured
Clock: 3/7 | Interrupts done: 0 | Mode: Intel
Arrives in: 4 player turns  (progress: [▓▓▓░░░░] 3/7)
Headcount: 0 AT TABLE vs 5 at corner (Δ = −5) → Pressure: Comfortable
Target: none yet | Eavesdrop: seekers' corner | Fidelity: Visual only
Wariness: none established
```

**Examples by Confidence (showing M variability):**
- Confidence 0, N=3/M=7: `Arrives in: 4 turns (progress: [▓▓▓░░░░] 3/7)`
- Confidence +1, N=2/M=5: `Arrives in: 3 turns (progress: [▓▓░░░] 2/5)`
- Confidence +2, N=1/M=3: `Arrives in: 2 turns (progress: [▓░░] 1/3)`
- Confidence +4, N=0/M=1: `Arrives in: 1 turn — NEXT RESPONSE (progress: [░] 0/1)`
- Confidence −2, N=8/M=14: `Arrives in: 6 turns (progress: [▓▓▓▓░░░] 8/14)`
- Confidence −4: `Arrives in: never (Withdrawn — won't approach YOUR table; ambient-ACTIVE elsewhere, working other levers)`

**Forbidden patterns:**
- ❌ Showing only `Clock: N/M` without the explicit `Arrives in: X turns` line
- ❌ Omitting the progress bar
- ❌ Showing the same `Arrives in:` count two responses in a row (means clock didn't increment — see § HEADCOUNT PRESSURE and Tartuccio.md self-check rule)
- ❌ Misreporting `Arrives in:` value — must equal `M − N` exactly

Missing the countdown line = `.fail 3` (output structure incomplete). Wrong arithmetic = `.fail 4` (math error).

---

## ⛔ APPROVAL SCORING — PER-INTENT ANALYSIS, SUM ALL TIERS (NO CAP, NO ANCHOR)

**⛔ THERE IS NO "ANCHOR ON HIGHEST TIER" AND NO PER-TURN CAP.** (The old anchor/highest-tier model is RETIRED — it wrongly capped rich answers at +3.) feast_approval gains the NET SUM of every intent in the turn. A STRONG + AVG + AVG answer = +3+2+2 = **+7**, not +3. Scoring the whole answer as a single tier, or capping the turn delta at the highest single intent, is the bug this rule exists to kill.

**⚠️ TERMINOLOGY:** This section uses **INTENTS** (I1, I2, I3…) for the decomposition of a player message into per-statement scoring units. The label **THREADS** is reserved for the separate **🧵 OPEN THREADS** panel (running game-state tracker per `KM_DMRules_B.md` § OPEN THREADS — unresolved NPC questions, ongoing situations, commitments). These are two distinct systems. If a player asks *"where are the threads"*, they mean the 🧵 OPEN THREADS panel — NOT the I1/I2 intents in the SCORING block. Conflating the two = `.fail 3` (output structure / terminology violated).

**The ambiguity (historical):** sometimes the DM scored the whole player message as one tier; sometimes the DM scored each statement separately and stacked them. Neither is fully right. The canonical rule:

**Step 1 — Decompose the answer into intents.** An "intent" is a distinct statement, argument, or beat the player made. A short answer may have one intent; a long paragraph may have 3–6. Each intent gets analyzed against the active companion's profile (Background / Priority / Desire / Preference / Wound per KM_Companions.md). Label intents as I1, I2, I3… (matches `KM.txt` § STEP 0 INTENT FIDELITY rule — same decomposition, used for both render-check and scoring).

**Step 2 — Score each intent independently against the companion's profile.** Per-intent tier:
- **PROFOUND (+5)** — RARE. Above STRONG. The statement does not merely name a wound the companion has felt — it **reframes it, hands them language they never had, or lands something so precise/original it changes how they see themselves or their purpose.** The unforgettable beat — the one they will carry. Reserved for genuinely exceptional articulation, not "a very good STRONG." If you're unsure whether it's PROFOUND or STRONG, it's STRONG. (Examples that qualify: an original articulation of a companion's core purpose they have never heard put into words; a single line that resolves a contradiction they've carried for years.)
- STRONG (+3) — names a wound, core truth, or recognition the companion has felt but never heard externalized
- AVERAGE (+2) — touches their lane with specificity
- WEAK (+1) — generic alignment / right sentiment, forgettable delivery
- 0 — irrelevant to their lane
- −1 — contradicts a stated value
- −2 — betrays a core need or wound

**⛔ INCREDIBLE STATEMENT → INCREDIBLE GAIN.** The whole point of decompose-and-sum + the PROFOUND tier is that an exceptional answer is NOT capped at +3. A turn that lands a PROFOUND beat plus two supporting hits = +5+3+2 = **+10 in a single turn**, and that is correct and intended. If a genuinely incredible statement is only moving approval +3, the DM has either (a) failed to decompose it into its intents, or (b) failed to recognize a PROFOUND-tier beat as anything more than STRONG. Both are the bug. Reward the incredible as incredible.

**Step 3 — Score ALL positive intents, sum them.** Every distinct positive intent scores its own tier. A player who says one STRONG thing + two AVERAGE things scores +3+2+2 = +7 for the turn. Each intent that genuinely hits the companion's lane earns its value — rich answers earn more than thin ones.

**Step 4 — Apply negative intents as a drag.** Each negative intent (−1, −2) subtracts directly from the sum. A turn that scores +7 gross with one −1 intent = +6 net. Negatives do not cancel the entire turn — they reduce it proportionally.

**Step 5 — Sum all intents, apply net delta.** feast_approval increments by the net sum (positive intents minus negative intents) for the turn. No per-turn ceiling.

**Why this matters:** a player who gives a long, rich answer with multiple lane-hits earns more than a player who gives one line. Long answers are rewarded for genuine content. Short answers that only hit one intent earn only that one intent's value. The score reflects what was actually said.

**Rendering in 🎯 SCORING block:**
- List intents numbered I1, I2… with per-intent tier
- Sum all positive intents
- Subtract any negative intent drag
- Final turn delta = net sum

**Example output (compact):**
```
🎯 SCORING — Linzi
I1: "Am I your co-author?" → AVG (+2) — correct lane, no wound named
I2: "How are they the finest college when they make a decision that
    lowers their reputation?" → STRONG (+3) — names her 4-year wound
I3: "Redemption arc is best story" → WEAK (+1) — generic she knows
I4: jab on "finest college" → AVG (+2) — lane puncture, not wound

Sum: +3+2+1+2 = +8. Drag: none. Turn delta: +8.
feast_approval[Linzi]: 0 → +8
```

**Forbidden patterns:**
- ❌ Scoring "the whole answer" as a single tier without identifying individual intents
- ❌ Awarding STRONG when no intent actually named a wound (vague-but-right-topic = AVERAGE; perfect-about-wrong-topic = WEAK)
- ❌ Ignoring negative intents when computing drag
- ❌ Padding intents — do not invent extra intents that were not genuinely present in the player's answer to inflate the score
- ❌ Using "thread" / "T1, T2…" labels in the SCORING block — those labels belong to 🧵 OPEN THREADS. Use "intent" / "I1, I2…" here.
- ❌ Telling the player who asks "where are the threads" that the SCORING intents ARE the threads. They are not. Render the 🧵 OPEN THREADS panel instead.

---

## ⛔ QUESTION ACKNOWLEDGMENT — GROUP TALK SCORING

**Group talk only.** Fires in: feast carousel, seekers' table sit-down, earshot ring. Does NOT fire in solo 1-on-1 exchanges.

**What counts as a direct question:** A named companion explicitly addresses the player with a question they expect answered — "What do you think?", "Do you mean what you said?", "Have you ever lost someone?" Criteria: (1) named companion, (2) clearly aimed at the player, (3) non-rhetorical — a real answer is expected. A trailing "...I wonder what fate holds" is not a question. A line ending in "?" that demands nothing is not a question. If the companion would visibly pause and wait for a response → it qualifies. Log it to `pending_questions[CompanionName]` on the turn it fires.

**Immediate answer bonus (+1):**
- Player gives a substantive response the same turn the question is asked, OR within 1 grace turn → flat +1 to `feast_approval[CompanionName]`
- Applied AFTER the per-intent sum and drag. Does not alter the intent scoring or drag computation — it is additive (a flat +1 on top of the net sum).
- One bonus per companion per turn maximum, even if two questions were answered.
- Clear the `pending_questions` entry when the bonus fires.

**Ignore penalty (−1 per turn, grace = 2 turns):**
- Grace period = 2 turns after the question was asked. If still unanswered by turn 3 → −1 to `feast_approval[CompanionName]` per turn until answered or scene ends.
- Penalty is per question. A companion who asks twice while the first is still unanswered accrues −1/turn per open question.
- Penalty stops the turn the player answers. No makeup bonus applies once penalty has started.
- Scene transition (player leaves position, chapter closes, scene ends) → clear all `pending_questions` entries, no trailing penalty carried.

**Rendering in 🎯 SCORING block:**
- Bonus fires: `+1 [Name]: question answered (immediate)`
- Penalty tick: `−1 [Name]: question unanswered (asked turn N, now turn M)`
- Both lines appear in the SCORING block, NOT in narration prose.

**Save field:** `pending_questions{}` root key. Key = companion name. Value: `{ "question_summary": "...", "asked_turn": N, "grace_turns": 2, "penalty_active": false }`. Set `penalty_active: true` when the grace period expires and penalty begins ticking.

---

## ⛔ SEEKERS' TABLE — ACTIVE ENGAGEMENT (player seated at the seekers' corner)

The seekers are passive while the player is merely in earshot (§ SEEKER EARSHOT MECHANIC above). When the player crosses to them and **sits down**, they stop observing and start asking — they engage the player with their own questions. This is NOT the companion carousel; it is a lighter, table-bound loop that reuses `tartuccio.seeker_dispositions` and the § TARTUCCIO PATHING return countdown. No new pool-state machinery.

### TRIGGER
Active engagement fires on the player's **action of sitting** at the seekers' table — declared as "I sit with them," "I take the empty chair," or the sharpest form, dropping into **Tartuccio's chair at M17** while he is away. From position #7 (Seekers' Edge, K15) this is one step; from elsewhere the player crosses the floor to the corner first.
- **Standing** in earshot (incl. holding position #7 without sitting) stays PASSIVE — overhear-scoring only, per § SEEKER EARSHOT MECHANIC. **Sitting** is the active trigger.
- While the player is seated here, the **companion carousel PAUSES** — chosen companions hang back from Tartuccio's corner (per the position table, Seekers' Edge: companion recruitment slow). `feast_q` does not advance from companion drift. The companion `[CAROUSEL STATE]` block renders `PAUSED — player at seekers' corner`; the `🪑 SEEKERS' TABLE` panel (active mode) is the live engagement telemetry.
- ⛔ **AUTO-RESUME ON RETURN (no command needed).** When the player leaves the corner and returns to their home table / the carousel area, the carousel resumes **automatically on that same response** — `[CAROUSEL STATE]` flips back to active and the next Ready companion (FIFO) steps forward in the SAME beat. The player does NOT type `.carousel`/"resume" to restart it; returning is the trigger. Leaving it `PAUSED` after the player is back = `.fail 17`. (Full rule: KM_PR_03_feast_circuit.md § SEEKERS' TABLE.)

### THE LOOP — one seeker per beat
- One seeker is **ENGAGED** at a time (the table's primary speaker), drawing **one question** from their 10-pool in `KM_CompanionIndex.md` § SEEKERS 5 per player beat. **Declare the index fired** (`pool_fired`) — same audit discipline as `openers_pool_fired`. No repeat until that seeker's pool is exhausted.
- The five are already seated — there is **no drift, no queue, no Ready/BackOfQueue pools.** Only who holds the floor and who cuts in.

### ⛔ POOL QUESTIONS ARE MANDATORY — SITUATIONAL QUESTIONS DO NOT REPLACE THEM

The question pools are NOT flavor supplements to situational conversation. They ARE the engagement. The pool question fires every beat the player is seated — no exceptions, no substitutions.

**What is and is not allowed:**
- The engaged seeker MAY react to situational context (the chair, the toast, Tartuccio's position) in 1–2 sentences of flavor text BEFORE the pool question. That framing does not count as the beat's question. The pool question follows immediately.
- A question the DM invented from context ("Which do you think he picks?", "How close?") is NOT a pool question. It may run as flavor ONLY if the pool question also fires in the same beat. If only the invented question was asked — the pool question was skipped. = `.fail 9`.
- Pool questions are vetting questions about eRmaC's character, capabilities, and intentions. They are NOT questions about Tartuccio's movements, the feast mechanics, or the other NPCs. If the question does not come from the indexed pool, it is not the pool question.

**Minimum questions per beat when seated:**
1. Engaged seeker: 1 pool question (mandatory — index number declared in `🪑 SEEKERS' TABLE` telemetry as `pool Q#N fired`)
2. Faction chime-in: at least 1 per beat — one other seated seeker must produce either (a) a question from THEIR OWN pool (disposition ≥ 0 required) or (b) a short direct challenge/cross-check (2–3 sentences). Silent reaction descriptions alone ("Revy writes something," "Satsuki Kiryūin shifts posture") do NOT satisfy the faction chime-in requirement.
- **Minimum = 2 questions or direct challenges per beat.** Both appear in the ❓ QUESTIONS block. A beat with only 1 question while 4 seekers are seated = `.fail 9`.

**Rotation — floor passes after 2 consecutive turns:**
- After 2 consecutive player beats where the same seeker holds the ENGAGED floor, the floor passes to the next seeker in disposition order on the following beat.
- The previous seeker drops to faction role — they may still chime in, but they no longer hold the floor.
- The DM may NOT sustain one seeker as the sole questioner across 4+ beats while others produce only silent reaction text. That seeker had 2 turns; rotate.
- Exception: if the player DIRECTLY addresses a specific seeker ("What were you counting, Atalanta Alter?"), that seeker takes ENGAGED for that beat regardless of rotation order. Rotation counter resets to 1.

### ENGAGEMENT ORDER
- **First engager** = the seeker whose lane the player's ARRIVAL provoked:
  - Took Tartuccio's chair → **Satsuki Kiryūin** (reads the power play / the climb) or **Velvet Crowe** (takes your measure cold) opens.
  - Arrived on a competence display (craft/nature/green → Revy, scholarship/the long game → Velvet Crowe, command → Satsuki Kiryūin, devotion/wrath/cruelty-in-joy → Bellatrix, a named enemy or open bloodlust → Atalanta Alter).
  - Quiet, careful, watchful approach → **Velvet Crowe** (counts your exits before she counts your worth).
  - No clear provocation → highest current `seeker_disposition`.
- **Subsequent order:** descending `seeker_disposition`.
- A **Tartuccio-loyal** seeker (disposition ≤ −1) does NOT volunteer their pool — they only chime in to challenge. They engage from their pool only once disposition ≥ 0.

**⛔ THE POOL QUESTION FIRES ON THE ARRIVAL BEAT — NOT THE NEXT ONE.** The first engager may open with 1–2 sentences reacting to the player's arrival action (the chair, the toast, the approach) as contextual framing. The pool question fires IN THAT SAME BEAT — it does not wait for a second turn. A beat where the first engager produces only a situational statement or observation and saves the pool question for "after the player responds" = `.fail 9`. The player's arrival IS the trigger; the pool question is the response to it.

### FACTION CHIME-INS (the inverse of companions — not an applause track)
The other seated seekers cut in to **challenge**, cross-check each other, or test the player — a faction sizing up a defection target, not friends backing a leader. 1–3 sentences in that seeker's register (`KM_Backstories.md`); does NOT consume the engaged seeker's beat.
- **Minimum 1 chime-in per beat is mandatory** (see § POOL QUESTIONS ARE MANDATORY above). Silent atmospheric reactions (body language, pen-turning, posture shifts) count as FLAVOR, not as chime-ins. The chime-in must be SPOKEN — a direct challenge, a cross-check question, or a short voiced reaction that names its position.
- A seeker in faction role with unfired pool questions should deliver their chime-in AS a pool question from their own index when possible — double-purpose the beat.
- **PRE-FLIP DOUBLE EDGE:** until a seeker is flipped, every engagement carries the report-to-Tartuccio edge — they assess the player for HIM too. Surface it: a glance toward his corner, a filed pause, *"he'll want to hear that."*

### SCORING — active answers feed `seeker_dispositions`
While seated, the seeker's reaction to the player's **answer** drives `tartuccio.seeker_dispositions` (active), replacing passive overhear-scoring for the seated duration. Shift table per `KM_Tartuccio_Strategic.md` § SEEKER FLIP SYSTEM.
- Hits the seeker's lane/concern → **+1** | perfect lane hit OR publicly siding with them against Tartuccio → **+2** | dismissive / violates their lane-flag → **−1**.
- Cap **+3/turn** per seeker (Strategic Layer cap). The flip threshold and "3 flipped → forced departure" are owned by `KM_Tartuccio_Strategic.md` § SEEKER FLIP SYSTEM; Seekers' Edge also carries a Ch1 flip-DC reduction (position table above). The sit-down is the fastest disposition-builder — active answers beat overheard ones.

### FACTION CROSS-RECALIBRATION (a strong answer moves the neighbors)
| Player wins… | …and the table shifts |
|---|---|
| **Satsuki Kiryūin**, via raw decisive command / the fastest climb | **Atalanta Alter +1** (a captain who will point her at something worth burning); **Velvet Crowe −1** (naked ambition with no wall behind it is a knife that turns) |
| **Velvet Crowe**, via cold lawful competence / cruelty named plainly | **Atalanta Alter −1** (all that cold accounting and never once the joy of the burn); **Bellatrix −1** (lawful order with no appetite in it bores her) |
| **Atalanta Alter**, via the gleeful chase / burning the quarry's world down | **Bellatrix +1** (cruelty done in joy — her own language); **Velvet Crowe −1** (a fire with no wall behind it is waste, and waste is weakness) |
| **Bellatrix**, via grand certain cruelty done in joy / devotion to a will | **Atalanta Alter +1** (she knows that laugh — kindred glee); **Velvet Crowe −1** (reads the joy as undisciplined, weak) |
| **Revy**, via choosing loyalty over the payout at real cost | **Bellatrix +1** (a devotion you'll bleed for is the only loyalty she respects); **Satsuki Kiryūin −1** (a cause above the ladder is a leash she didn't choose) |

DM judges other adjacencies by lane. Cross-effects are ≤ ±1 and never push a seeker past the +3/turn cap.

### THE CLOCK — Tartuccio returns (no new timer)
The sit-down runs on the § TARTUCCIO PATHING return countdown: he is away from M17 when the player arrives, and his **turns-to-return** = the remaining path back to his corner (he moves ~one waypoint/turn; render his marker each turn). The player gets that many turns of active access before he is back.
- Taking his **CHAIR**: he notices within 1 turn and routes straight back; Confidence **−1** (chair), **−2** if held 2+ turns (`KM_Tartuccio_Strategic.md` § CONFIDENCE TRIGGERS).
- His **ARRIVAL ends the active sit-down** (`KM_Tartuccio_Strategic.md` § PANIC STATE (A): the player cannot sit at the seekers' table while he is there). On arrival: one beat reading the table, then his territorial first line (it addresses the chair if taken). Render the seekers' postures realigning — loyal ones toward him, leaning/flipped ones caught between.
- **Player's call on his arrival:**
  - **YIELD** (stand / give back the chair) → active loop ends; seekers revert to passive scoring under his supervision.
  - **HOLD** the chair → provocation: Confidence −2 (held 2+ turns). The active Q&A **suspends anyway** — seekers will not speak freely with him present; it becomes a 3-way with Tartuccio holding the floor. You've traded the conversation for the dominance display.

### TELEMETRY — `🪑 SEEKERS' TABLE` panel, ACTIVE mode
When seated, the existing mandatory panel (format above) renders in ACTIVE form, inside the bottom telemetry fence:
- `ENGAGED: <seeker> — pool Q#<index> fired`
- Each seeker: `disposition <−3..+3> (tier) Δ<this turn>`
- Faction cross-shift this turn (if any)
- `🐍 Tartuccio returns in: <N> turns` (pathing countdown)
- `Flip watch: <count at +2> uncertain / <count at +3> flipped`

Missing the ACTIVE panel while seated = `.fail 9` (seeker suppression) + `.fail 15` (state delta omitted).

### SAVE (additions — minimal; reuses `tartuccio.seeker_dispositions` + the pathing countdown)
```json
"seekers_table": {
  "seated": false,            // player currently seated at the seekers' corner
  "seat_taken": false,        // player in Tartuccio's chair (M17)
  "engaged_seeker": null,     // current primary speaker
  "pool_fired": {             // KM_CompanionIndex.md question indices used (no repeat until exhausted)
    "Bellatrix": [], "Revy": [], "Satsuki Kiryūin": [], "Velvet Crowe": [], "Atalanta Alter": []
  }
}
```
No new pool-state arrays — engagement order is recomputed from `tartuccio.seeker_dispositions` each turn.

### WORKED EXAMPLE
Player crosses to the corner while Tartuccio is at the champions' table (E8) and drops into his chair (M17).
- `seekers_table.seated = true`, `seat_taken = true`. Confidence −1 (chair). Pathing: he notices within 1 turn and starts the slow diagonal back from E8 (~9 cells, around pillars D14/L14) → **~5 turns to return.**
- **Satsuki Kiryūin opens** (the chair is the ladder, taken — her lane) — pool Q (*"Give me a real order. Now — and mean it."*). Player gives a clean, plainly-stated command → Satsuki Kiryūin **+2**; cross-shift: Atalanta Alter **+0** (a captain worth loosing).
- **Velvet Crowe chimes in** to cross-check (*"A man who seizes the high seat and still answers me plainly. Rare — and watched."*) — disposition unchanged, her eyes flicking to Tartuccio's approaching figure (pre-flip).
- Turn ~5: **Tartuccio arrives**, reads the table one beat, first line addresses the chair. Active loop ends; player chooses YIELD or HOLD.

---

*KM_DMRules_C.md — feast carousel supplement. Pair-load with KM_DMRules.md during PR_03. | v95.12 — Seekers' Table active engagement added*
