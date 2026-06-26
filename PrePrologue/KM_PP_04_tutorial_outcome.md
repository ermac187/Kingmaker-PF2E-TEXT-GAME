# KM_PP_04_tutorial_outcome.md — Pre-Prologue Beat 04: TUTORIAL OUTCOME
## Atomic scene file | State: PP_TUTORIAL_OUTCOME
## FILE_KEY: KMPP04:sword-choice-armorer
## RULE_QUOTE: Sword choice is player-driven (A/B/C/IGNORE). Thief disposition is player-driven (STEP 1.5 menu, six options). Crew gear is player-driven (STEP 1.6 menu, four options — combat path only). Armorer Corryn stays at his bench — does NOT enter the alley. Squire Aldric witnesses every outcome silently. Armorer pays bonus gp for thief brought in (bound > unconscious > dead), thief's gear, and crew's gear (Bruiser hatchet, Cutpurse sword, both). Public reputation deltas MUST be listed in reputation_deeds[]. tutorial_pickpocket_resolved must be set before PP_05. Save offer fires before Malak gate.

---

> ⛔ DO NOT (1) auto-pick the sword option — player chooses A/B/C/IGNORE
> ⛔ DO NOT (2) place the armorer in the alley — he stays at his bench, can't abandon 12 customers' weapons
> ⛔ DO NOT (3) skip the Squire Aldric witness beat — he watches every outcome silently
> ⛔ DO NOT (4) apply public_reputation deltas without listing them in `reputation_deeds[]`
> ⛔ DO NOT (5) advance to PP_05 without setting `tutorial_pickpocket_resolved` to a non-empty value
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (7) skip STEP 1.5 (thief disposition menu) on combat/intimidated/talked_down paths — armorer bonus scaling depends on it. Auto-flee-thief = `.fail 9`.
> ⛔ DO NOT (8) hand-wave bonus rewards — output the scaling table tier explicitly in the resolution narration (e.g., *"+3 gp for the bound thief, +2 gp for his gear, +2 gp for both crew sets"*) so the player can verify the math.
> ⛔ DO NOT (9) skip STEP 1.6 (crew gear menu) on the combat path. If the Bruiser AND Cutpurse both fled (rare), the menu may be omitted; otherwise it MUST fire and `crew_gear_taken` MUST be set. Auto-leaving crew gear = `.fail 9`.

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP04:sword-choice-armorer]`
Line 2: `[RULE_QUOTE: Sword choice is player-driven (A/B/C/IGNORE). Thief disposition is player-driven (STEP 1.5 menu, six options). Crew gear is player-driven (STEP 1.6 menu, four options — combat path only). Armorer Corryn stays at his bench — does NOT enter the alley. Squire Aldric witnesses every outcome silently. Armorer pays bonus gp for thief brought in (bound > unconscious > dead), thief's gear, and crew's gear (Bruiser hatchet, Cutpurse sword, both). Public reputation deltas MUST be listed in reputation_deeds[]. tutorial_pickpocket_resolved must be set before PP_05. Save offer fires before Malak gate.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `tutorial_pickpocket_resolved` — may already be set (intimidated/talked_down/lost_chase from PP_02)
- If set to one of those: skip to "alternate outcome" handlers below
- `pre_prologue_state` — `"PP_TUTORIAL_OUTCOME"`

**WRITES:**
- `tutorial_pickpocket_resolved` — final value: won/intimidated/talked_down/kept_sword/extorted/ignored/lost_chase
- `thief_disposition` — let_go/bound/unconscious/dead (set by STEP 1.5 menu; not set if `lost_chase`/`ignored`)
- `thief_gear_taken` — true/false (set by STEP 1.5 menu)
- `crew_gear_taken` — none/bruiser/cutpurse/both (set by STEP 1.6 menu; "none" if combat path skipped crew or crew fled)
- `armorer_favor` — true/false
- `armorer_bonus_paid` — total gp paid by armorer this tutorial (for scoring + later callbacks)
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
6. ⛔ **RULE 9 ON EVERY MENU (KM.txt, overrides this file per Rule Zero).**
   Each player-facing menu in this beat — STEP 1.5 thief disposition, STEP 1.6
   crew gear, STEP 2 sword — MUST end the response with **10–30 options**. The
   featured fork ([1]–[6] disposition / [1]–[4] gear / [A][B][C][IGNORE] sword)
   LEADS the menu; then append contextual world-actions to clear the 10-option
   floor (talk to Corryn, check the thief, watch the squire, glance at the
   harper, scan the crowd, `.gear`/`.hp`/`.heropoints`, head toward the gate,
   Custom). Contextual actions resolve in-world and return to the featured
   decision — they never skip it. A bare sub-10 fork = `.fail 3`. Use only
   on-scene NPCs/objects; invent nothing (`.fail 9`). **10 is the hard floor;
   the exact count above 10 is the DM's discretion (anywhere in 10–30).** No
   obligation to maximize — just never drop below 10.

---

## STEP 1 — POST-COMBAT NARRATION (combat path only)

If combat resolved: thief alive, surrendered. Narrate the moment:

> He drops to one knee. The customer's blade hits the dirt. *"Keep it.
> Not worth dying over."* He stays kneeling. The crew is down behind
> you. He hasn't run — yet. He's watching you to see what you'll do.

(If thief KO'd unconscious: same beat — sword on the ground beside him,
thief unmoving. Skip STEP 1.5's "let go/bind" sub-choice; he is already
`unconscious` for STEP 1.5 purposes; "strip gear" sub-choice still fires.
If killed: armorer reaction shifts — see Aldric variants below; STEP 1.5
gear-strip still fires on the corpse if player chose to.)

---

## STEP 1.5 — THIEF DISPOSITION MENU (combat / intimidated / talked_down paths)

> ⛔ Output verbatim. Wait for player input. This MENU fires BEFORE the
> sword choice menu. Player picks what happens to the thief and his gear.
> If `thief_disposition` is already set (e.g., `intimidated`/`talked_down` paths
> where the thief fled with the sword — see STEP 4), SKIP this menu.

```
---
 THE THIEF IS AT YOUR FEET — what do you do?
 [1] LET HIM GO         — He flees into the alley. No gear taken.
 [2] BIND HIM           — Tie his hands. He stays put, alive and conscious.
 [3] STRIP HIS GEAR     — Take his weapon and armor. Then let him go.
 [4] BIND + STRIP GEAR  — Both. He stays put, stripped down. Full handover possible.
 [5] KNOCK HIM OUT      — Subdue him cold. (Unconscious bundle, can't testify.)
 [6] KNOCK OUT + GEAR   — Subdue + strip gear. Heaviest hand, biggest take.
---
```

Sets `thief_disposition` + `thief_gear_taken`:
- `[1]` → `thief_disposition="let_go"`, `thief_gear_taken=false`
- `[2]` → `thief_disposition="bound"`, `thief_gear_taken=false`
- `[3]` → `thief_disposition="let_go"`, `thief_gear_taken=true`
- `[4]` → `thief_disposition="bound"`, `thief_gear_taken=true`
- `[5]` → `thief_disposition="unconscious"`, `thief_gear_taken=false`
- `[6]` → `thief_disposition="unconscious"`, `thief_gear_taken=true`

(If thief was killed in combat: skip `[1][2][5][6]`. Offer only
`[3] STRIP CORPSE GEAR — yes/no`. Sets `thief_disposition="dead"`.)

Narration after pick (1–2 lines, in-world, no menu rendering):
- `[1]` / `[3]`: Thief mumbles thanks, scrambles up, disappears into the alley.
- `[2]` / `[4]`: You bind his wrists with his own belt. He sits against the wall, watching.
- `[5]` / `[6]`: One clean pommel-strike. He slumps. You sling him over your shoulder.
- Killed + gear: You roll the body, take what's useful.

---

## STEP 1.6 — CREW GEAR MENU (combat path only — fires only if crew was downed)

> ⛔ Output verbatim. Wait for player input. Fires IMMEDIATELY AFTER STEP 1.5.
> SKIP this menu if `intimidated`/`talked_down`/`lost_chase`/`ignored` (no crew
> fight happened). SKIP if the Bruiser AND Cutpurse both fled before being
> downed (rare — DM tracks `crew_resolved_status`).
> HOSTAGE PATH: if `crew_resolved_status="hostage_released"`, the crew withdrew
> alive WITH the thief but left whatever they laid down to buy {their} life — run
> the HOSTAGE VARIANT below (surrendered gear only, no bodies). If `"hostage_broke"`,
> handle whoever was downed normally and whoever fled per the fled-variant lines.

The Bruiser (hatchet, leathers) and the Cutpurse (shortsword, leathers) lie
in the alley behind you — knocked out, dying, or dead per the round-loop
resolution. Their gear is on them. The armorer at the bench buys cheap
mundane resale.

```
---
 THE CREW'S GEAR — take any of it?
 [1] LEAVE IT ALL       — Walk away. Watch can deal with the bodies.
 [2] BRUISER'S GEAR     — Hatchet + leather jerkin.
 [3] CUTPURSE'S GEAR    — Shortsword + leather jerkin + belt pouch (handful of copper).
 [4] BOTH CREW'S GEAR   — Strip both. Heaviest haul.
---
```

Sets `crew_gear_taken`:
- `[1]` → `crew_gear_taken="none"`
- `[2]` → `crew_gear_taken="bruiser"`
- `[3]` → `crew_gear_taken="cutpurse"`
- `[4]` → `crew_gear_taken="both"`

Narration after pick (1 line, in-world):
- `[1]`: You leave them where they fell. The alley's already drawing flies.
- `[2]`: You roll the Bruiser, take the hatchet and the jerkin. Heavier load.
- `[3]`: You unbuckle the Cutpurse's belt. Sword, jerkin, and a few coppers from the pouch.
- `[4]`: You strip both. Two weapons, two jerkins, the pouch. Your arms are full.

(If the Cutpurse fled mid-fight: only `[1]` and `[2]` offered.
If the Bruiser fled: only `[1]` and `[3]`. If both fled: skip menu entirely.)

**HOSTAGE VARIANT (`crew_resolved_status="hostage_released"`):** No bodies — the crew
and the thief are gone. Only what they surrendered to save {them} is in the dirt: the
laid-down weapons (and the belt pouch if they emptied it), NOT jerkins they walked off
still wearing. Offer just that, reskinned — *"They left it to buy {their} life back: a
hatchet, a shortsword, a few coppers. You scoop up what you want; the alley's already
empty."* Set `crew_gear_taken` per pick as above.

---

## STEP 2 — SWORD CHOICE MENU (combat / intimidated / talked_down paths)

> ⛔ Output verbatim. Wait for player input.
> ⛔ **RULE 9 (KM.txt) — 10–30 OPTIONS, NO EXCEPTION.** The sword fork
> `[A][B][C][IGNORE]` is the FEATURED decision but it does NOT replace the
> menu — it leads it. The full menu MUST carry the contextual world-actions
> below (the bench, the crew, the squire, the harper, the crowd, the gate
> are all present). A bare 4-option fork = `.fail 3`. The featured letters
> still set state; the numbered actions resolve in-world (1–2 lines) and
> RETURN to this choice — the sword decision must still be made before exit.

```
════════════════════════════════════════════
 What do you do with the sword? — and the moment around it
 [A] RETURN IT      — Set it on the bench, no strings. "Yours."
 [B] KEEP IT        — Pocket it. Finder's rights. Walk away.
 [C] RETURN IT, BUT — Set it down and name your price before he takes it.
 [IGNORE]           — Leave it on the ground. Walk to the gate.
 ── take a beat first (resolves, then back to this choice) ──
 [1]  Talk to Corryn the armorer — read him before you decide.
 [2]  Ask about the sword's owner — what customer, still waiting nearby?
 [3]  Ask what she's worth — is there a watch bounty, a known face?
 [4]  Ask if Corryn knows her — regular problem, or a first offense?
 [5]  Ask where the nearest watch post is — let the guard take custody, not Corryn.
 [6]  Hand Corryn the gear bundle now — let him assess it, set the sell first.
 [7]  Set the thief down somewhere stable — off your shoulder before you talk.
 [8]  Lower the thief at Corryn's feet — let the body make the ask for you.
 [9]  Check the thief — still breathing, still out?
 [10] Address the squire by the gauntlet rack — the boy who saw everything.
 [11] Glance at the young woman with the lute-case, writing in her book.
 [12] Scan the crowd — who's watching, who's pretending not to.
 [13] Examine the longsword itself — quality, markings, whose it is.
 [14] Demoralize Corryn before [C] — let the Dragon Plate and the rage set the price.
 [15] Check your haul — `.gear` / what's wrapped in the bundle.
 [16] `.hp` / `.heropoints` — take stock before you commit.
 [17] Custom — say or do something else.
════════════════════════════════════════════
```

> 10 options is the HARD FLOOR (`.fail 3` under 10). Beyond that the exact
> count is the DM's discretion — anywhere in Rule 9's 10–30 range is fine;
> the list above is a generous example, not a required length. The numbered
> options are FREE looks/actions: none advance the beat or skip the sword
> decision; after resolving one, re-present this menu. Every option must use
> someone/something already on-scene — invent NO new NPCs, objects, or exits
> (`.fail 9`).

---

## STEP 3 — RESOLUTION OUTCOMES

### [A] RETURN IT (base reward + scaling bonuses)

> The armorer takes it with both hands, turns it over once checking the
> edge. Looks up.
> *"Didn't think I'd see that again. Half the city wouldn't have bothered."*
> He counts coins without looking and presses them into your hand.

**Base reward: 2 gp**, `armorer_favor=true`.

**Scaling bonuses — apply ALL that match player's STEP 1.5 + 1.6 picks:**

| What player brought (in addition to sword) | Armorer's response | Bonus |
|---|---|---|
| Thief BOUND (alive, conscious) | *"You actually brought him? The watch will want a word. There's a bounty on that face — small one, but real."* | +3 gp |
| Thief UNCONSCIOUS | *"Out cold, eh. Watch will still take him. Less talkative, less useful."* | +1 gp |
| Thief DEAD | *"...That wasn't necessary. I'll have someone fetch the body."* (frown) | +0 gp (no penalty, no bonus) |
| Thief's GEAR (weapon + armor) | *"Resale value. Cleaned up, sold to the next desperate prentice. I'll give you a fair cut."* | +2 gp |
| BRUISER's gear (hatchet + jerkin) | *"Hatchet's worth something. Jerkin's tired but the buckles are good."* | +1 gp |
| CUTPURSE's gear (sword + jerkin + pouch) | *"Sword's a clean piece. Pouch coppers are yours — I don't count those."* | +1 gp + the copper from the pouch (~8 cp ≈ less than 1 sp; track in inventory) |
| BOTH crew sets | *"You stripped them both. Heavy work. Here."* | +2 gp total (1+1) plus pouch coppers |

**Reward total examples:**
- Sword only: 2 gp (base)
- Sword + bound thief: 5 gp
- Sword + bound thief + gear: 7 gp
- Sword + bound thief + gear + both crew sets: **9 gp + 8 cp** (max full payday)
- Sword + unconscious + gear + cutpurse only: 6 gp + 8 cp
- Sword + dead + gear + both crew: 6 gp + 8 cp

The pouch coppers go into `player.inventory` (line item: "8 cp salvaged from Cutpurse's belt pouch"); they are NOT added to `armorer_bonus_paid` (which only tracks armorer payouts).

Set `armorer_bonus_paid` to total gp paid.

**Reputation/disposition scaling:**
- Base: `public_reputation +2`, `dispositions.merciful +1` (sword returned).
- + bound thief: `public_reputation +2 more` (citizens see law-and-order win), `dispositions.lawful +1`, deed: `"+2 turned in pickpocket alive to gate-side armorer (tutorial)"`.
- + unconscious thief: `public_reputation +1 more`, `dispositions.cunning +1`, deed: `"+1 hauled unconscious pickpocket to bench (tutorial)"`.
- + dead thief: `public_reputation 0` (mixed reactions — efficient vs. brutal), `dispositions.ruthless +1`, deed: `"delivered pickpocket's body to gate-side armorer (tutorial)"`.
- + gear (any): no rep change (gear is just resale; gear-only is morally neutral).

- `tutorial_pickpocket_resolved="won"` (combat) or `"intimidated"` / `"talked_down"`.
- Base deed: `"+2 returned customer's sword (tutorial)"`. Bonus deeds appended per above.

### [B] KEEP IT
> You pocket the blade. It isn't the thief's to begin with — it's a
> customer's. The armorer watches from his bench. Says nothing.

- Reward: customer's shortsword (1d6 S, 1 gp value).
- `tutorial_pickpocket_resolved="kept_sword"`, `armorer_favor=false`.
- Deltas: `public_reputation 0`, `dispositions.ruthless +1`.
- Deed: `"kept stolen customer sword (tutorial)"`.

**Side hustle — if player brought thief / thief gear / crew gear:** The armorer still buys gear off you (he's a merchant, not a moralist) and will still pay the watch bounty for a captured thief — but at a slight discount because you're clearly not playing straight with him.

| What player brought | Reward |
|---|---|
| Bound thief (alive) | +2 gp (discounted bounty) |
| Unconscious thief | +1 gp |
| Dead thief | +0 gp (and *"Get him off my bench."*) |
| Thief's gear | +1 gp (discounted resale) |
| Bruiser's gear | +1 sp (heavily discounted — 10× less than [A] tier) |
| Cutpurse's gear | +1 sp + the pouch coppers |
| Both crew sets | +2 sp + pouch coppers |

Set `armorer_bonus_paid` accordingly. No further rep change (`public_reputation 0` already applied for [B]); add `dispositions.cunning +1` if bonus paid.

### [C] RETURN IT, BUT (extort)
> You set the blade on the bench and name your price. He looks at the
> sword, then at you, then at twelve other customers' weapons he can't
> abandon. *"...Fine. But I'll remember this."*

- **Intimidation or Deception DC 11:**
  - Success: 5 gp. `public_reputation −1`, `dispositions.ruthless +1, cunning +1`. `armorer_favor=false`.
  - Failure: *"Get away from my bench."* 0 gp. `public_reputation −1`. `armorer_favor=false`.
- `tutorial_pickpocket_resolved="extorted"`.
- Deed: `"−1 extorted gate-side armorer (tutorial)"`.

**Side hustle — if player brought thief/gear:** Same as [B] table above (he'll still buy the gear and pay the bounty, discounted). Stacks ON TOP of the extort 5 gp / 0 gp. Set `armorer_bonus_paid` accordingly.

### [IGNORE / sword on ground]
> The armorer curses once. Goes back to his bench. Life goes on.

- No changes. `armorer_favor=false`. `tutorial_pickpocket_resolved="ignored"`.
- (No reputation deed.)

---

## STEP 4 — ALTERNATE PATHS (resolved before STEP 1)

### `intimidated` / `talked_down` (from PP_02)
- Thief dropped sword and fled WITHOUT combat. Thief is GONE — no STEP 1.5 menu, no bonus options.
- Player walks the sword back to the bench.
- Armorer reaction: same as [A] RETURN IT base — 2 gp, `armorer_favor=true`.
- Deltas: `public_reputation +1` (lower than [A] post-combat — no risk taken), `dispositions.merciful +1` (talked_down) or none (intimidated).
- Deed: `"+1 returned customer's sword peacefully (tutorial)"`.
- Set `thief_disposition="let_go"`, `thief_gear_taken=false`, `crew_gear_taken="none"`, `armorer_bonus_paid=2`.

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
> His testimony fires later at the Prologue feast — see KM_Prologue_Systems.md
> § SQUIRE ALDRIC (referenced from there, not here).

His feast line varies by `tutorial_pickpocket_resolved` + `thief_disposition`:
- `won` / `intimidated` / `talked_down`, `thief_disposition="bound"`: strongest testimony — "He hauled the thief in alive. Didn't have to." (`+2` manor crowd rep)
- `won` / `intimidated` / `talked_down`, `thief_disposition="let_go"` (mercy): testifies for player (`+1` manor crowd rep)
- `won`, `thief_disposition="unconscious"`: neutral testimony — "He did the job." (`+1` manor crowd rep)
- `won`, `thief_disposition="dead"`: cautious testimony — "He finished it." (no rep change)
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
 thief_disposition            : <let_go|bound|unconscious|dead|"" if N/A>
 thief_gear_taken             : <true|false>
 crew_gear_taken              : <none|bruiser|cutpurse|both>
 armorer_favor                : <true|false>
 armorer_bonus_paid           : <gp total — base + scaling bonuses; pouch coppers tracked in inventory separately>
 squire_aldric_witnessed      : <true|false>
 public_reputation            : <prior> → <new>  (Δ <value>)
 dispositions                 : <key+N>, <key+N>, ...
 reputation_deeds[] appended  : "<deed line>", "<bonus deed if any>"
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

## 🛑 NATURAL CHAPTER BREAK — SAVE OFFER (MANDATORY — fires before exit to PP_05)

⛔ **THIS SAVE OFFER IS PP_04's FINAL PLAYER-FACING OUTPUT AND A HARD GATE.** PP_04 does
NOT exit, PP_05 does NOT load, and you do NOT render any "gate approach" menu, transition
beat, or other intervening prompt, until this save offer has been OUTPUT and the player has
answered (1 or 2). The two-option save offer below is the ONLY menu PP_04 ends on. Skipping
it — or inserting an invented intermediate menu in its place and treating that as the exit —
= `.fail 16` (scene advanced past the required break) + `.fail 9`. CONFIRMED LIVE SKIP (the
DM bundled a fabricated 10-option "approach the gate" menu into the exit and never offered
the save). Do not repeat it.

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

⛔ GATED: reach this section ONLY after the SAVE OFFER above has fired AND the player chose
[2] Keep going (if they chose [1], you output the save block and STOP — they resume in a new
chat). You may NOT arrive here by skipping the save offer or by inventing a gate-approach
menu. The player's answer to the save offer is the input that unlocks this exit.

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

*KM_PP_04_tutorial_outcome.md — Pre-Prologue atomic beat 04 | v95.2 (armorer bonus scaling + crew gear menu)*
