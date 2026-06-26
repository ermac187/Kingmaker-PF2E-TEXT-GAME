# KM_PP_05_gate_approach.md — Pre-Prologue Beat 05: GATE APPROACH
## Atomic scene file | State: PP_GATE_APPROACH → PP_GATE_CONFRONTATION
## FILE_KEY: KMPP05:gate-approach-malak
## RULE_QUOTE: Three guards: Malak (captain) + Biggs + Wedge. Malak is 60 ft (~30 paces) south of the gate on the approach road, NOT at the arch. Three speeches verbatim from this file. 19-option menu mandatory. Departure reply window required — no NPC departs without player reply menu first.

---

> ⛔ DO NOT (1) generate Malak's dialogue from memory — copy the 3 speeches verbatim from this file
> ⛔ DO NOT (2) place Malak at the gate arch — he is 60 ft (~30 paces) south of the gate on the approach road
> ⛔ DO NOT (3) have Biggs or Wedge speak unprompted — Drift 0–1 silent, Drift 2 body language only
> ⛔ DO NOT (4) reduce or fabricate the 19-option menu — all 19 must appear, plus build-specific
> ⛔ DO NOT (5) draw a label-box instead of the Template 1 grid — `.fail 14`. East gate IS a scene change, MAP REQUIRED in this response (see § GATE APPROACH MAP below)
> ⛔ DO NOT (6) narrate an NPC departing, turning away, or concluding a scene without first outputting the player menu and waiting for input — NPC makes statement → menu → player replies. Never collapse statement + departure into one paragraph.
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPP05:gate-approach-malak]`
Line 2: `[RULE_QUOTE: Three guards: Malak (captain) + Biggs + Wedge. Malak is 60 ft (~30 paces) south of the gate on the approach road, NOT at the arch. Three speeches verbatim from this file. 19-option menu mandatory. Departure reply window required — no NPC departs without player reply menu first.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.
**This is the load-bearing transition gate** — PP_04 → PP_05 is the
known cascade-failure point where the DM drops file content.

---

## STATE IO

**READS:**
- `tutorial_pickpocket_resolved` — must be non-empty (`malak_unlocked = YES`)
- `pre_prologue_state` — `"PP_GATE_APPROACH"` on entry
- `player.build_id` — to fill `[primary weapon]`, `[secondary weapon/tool]`, `[armor description]`
- All tutorial outcome flags (squire_aldric_witnessed, public_reputation, dispositions)

**WRITES:**
- `current_scene = "restov_gate"`
- After 3 speeches: `pre_prologue_state = "PP_GATE_CONFRONTATION"` and load PP_06 + PP_07 as a pair
  - PP_06 handles the per-turn Anger/Drift mechanics
  - PP_07 lists path triggers; DM picks active path when conditions met

**EXIT TRIGGER → PP_GATE_CONFRONTATION:**
- 3-guard approach narrated (one paragraph)
- Malak appearance block delivered (one paragraph)
- All three Malak speeches output verbatim
- 19-option menu output
- Player has not yet acted — wait for input
- Set `pre_prologue_state = "PP_GATE_CONFRONTATION"`, then load PP_06.

---

## REQUIRED OUTPUTS (this beat — first response only)

⛔ TWO LAYERS — KEEP THEM SEPARATE. The PLAYER-FACING layer is short and
clean. The DM-AUDIT layer (proof-of-load, sentinel, NPC-verify, HP ledger,
state-read) is verification scaffolding and renders COMPACTLY AT THE VERY
BOTTOM, below the menu — it must NEVER sit on top of, or interleave with,
the scene and bury what the player is tracking. The player reads state from
ONE place: the 🚧 GATE TRACKER. Dumping the audit wall above the narration
= `.fail 3` (render order) — the trackables get buried, which is the exact
complaint this layout fixes.

**PLAYER-FACING LAYER (in this order):**
0. **FILE_KEY line 1**: `[FILE_KEY: KMPP05:gate-approach-malak]` (proof of load — mandatory first line, this one line only at top).
1. **RULE_QUOTE line 2** (verbatim, per § FIRST TWO OUTPUT LINES).
2. **MAP** — Template 1 grid per § GATE APPROACH MAP below. Code fence; column headers (A–N), row numbers, `#` walls, `/` gate arch, named-cell positions for all visible NPCs. **Label-box = `.fail 14`.**
3. The three narration blocks (approach + Malak appearance + 3 speeches), all verbatim.
4. **🚧 GATE TRACKER** — the standalone player status dashboard, rendered directly above the menu, initialized to scene-start values:
   ```
   🚧 GATE TRACKER — turn <N>
     >> BIGGS DRIFT  [0/3]  —  silent mask (0–1)
          Wedge mirrors [0/3]   — the loyal-guard flip; THIS is the one to watch
          Malak's invented "rules": none yet   — each is a LIE; contradictions are catchable
     Malak Anger     [0/4]  ·  Fear: NO
     Sobriety        turn 0/7 (Drunk, atk −2)
     Gate Window     OPEN  ·  Dismissed: NO  ·  Bribe exposed: NO
     eRmaC           HP 23/23  ·  Hero Points <build value>
     Path trend      none yet
   ```
   Exact shape + rules → `KM_PP_06_gate_state.md` § GATE TRACKER FORMAT. Biggs Drift is the headline tracker (leads the panel, tier gloss inline). This panel is the ONE place the player reads state; it carries forward into PP_06 and updates every confrontation turn.
5. The 19-option menu (BASELINE) plus build-specific options to reach 10–30 total.

**DM-AUDIT LAYER — render COMPACTLY at the very bottom, AFTER the menu (anti-fabrication proof; the player can skip past it):**
6. `[STATE READ] pre_prologue_state="PP_GATE_APPROACH" | resolved="<value>" | malak_unlocked=YES`
7. `SCENE SENTINEL: Biggs HP 55 AC 21 Dwarf Fighter 5 | Malak AC 17 HP 28 drunk −2 atk | Bolt DC open-road 10 | Wedge HP 26 AC 18`
8. `GATE NPC CONFIRMED: Biggs = stout dwarf, halberd + tower shield, 12-yr veteran, NO bow. Wedge = young human, longsword, 2 yrs, NO bow. Malak = on approach road 60 ft from gate arch. Gate arch ground level = unmanned.`
9. `[HP CHECK]` ledger.

> PRE-FILL (§ PRE-FILL) is an INTERNAL worksheet — resolve the three build
> values BEFORE narrating and weave them into the narration where they
> belong. Do NOT dump the `[primary weapon] = …` worksheet as a visible
> output block; it is not player-facing state.

---

## PRE-FILL (do this BEFORE narrating)

Look up `player.build_id` in `KM_PrePrologue_Setup.md`. Fill three values:

```
[primary weapon]        = ____________________
[secondary weapon/tool] = ____________________
[armor description]     = ____________________ (KM_PrePrologue_Setup.md → Exploration row)
```

> ⛔ `[armor description]` is narration only. NO armor field in save block.
> Generating armor from PF2e knowledge = `.fail 9`.

---

## GATE APPROACH MAP — TEMPLATE 1 (verbatim, copy as written)

> ⛔ Output this map BEFORE narration on the first PP_05 response. ASCII only.
> Column letter headers + row number headers + symbol key REQUIRED.
> See `KM_Map.md` for the full template rules. **Label-box (no headers, no cells, just `[Malak]` `[player]` written in a box) = `.fail 14`.**

Open battle / plaza per SCENE-SHAPE RULE = 14 wide × 10–12 long. Use 14 × 12.

```
RESTOV — EAST GATE APPROACH                      Each square = 5 ft

       A    B    C    D    E    F    G    H    I    J    K    L    M    N
  1    #    #    #    #    #    /    /    #    #    #    #    #    #    #
  2    .    .    .    .    .    .    .    .    .    .    .    .    .    .
  3    .    .    .    .    .    .    .    .    .    .    .    .    .    .
  4    .    .    .    .    .    .    .    .    .    .    .    .    .    .
  5    .    .    .    .    .    .    .    .    .    .    .    .    .    .
  6    .    .    .    .    .    .    .    .    .    .    .    .    .    .
  7    .    .    .    .    .    .    .    .    .    .    .    .    .    .
  8    F    .    .    .    .    .    .    .    .    .    .    .    A    .
  9    N    .    .    .    .    .    .    .    .    .    .    .    H    .
 10    .    .    .    .    .    B    M    W    .    .    .    .    .    .
 11    .    .    .    .    .    .    @    .    .    .    .    .    .    .
 12    .    L    .    .    c    c    c    P    P    .    .    .    .    .

LEGEND: # wall   / gate arch   . open road   c crowd
        @ eRmaC   M Malak   B Biggs   W Wedge
        F flatbread (Rina)   A armorer (Corryn)
        N nuts (Sava)        H fish (Borys)
        L chronicler-bard (Linzi / Leliana — see § CHRONICLER AT THE GATE)
        P pilgrims
```

Distance: gate arch row 1 → Malak row 10 = 9 cells = 45 ft (narrative "60 ft / 30 paces" compresses to map scale). Player at G11 adjacent to Malak at G10 (talking distance).

ARCHERS off-grid above row 1: Willy+Johnson left wall, Woody+Wang right. LOS: cannot fire on gate arch or row 1–2 wall base; CAN fire on rows 3+.

---

## CHRONICLER AT THE GATE — the run's chronicler-bard witnesses this scene

Cell `L` is the run's CHRONICLER-BARD, present at the gate as an un-recruited bystander quietly writing down what she sees. She is NOT recruited here (that happens at the Prologue feast, PR_03) and does NOT intervene — she watches and records. Resolve WHO she is from the player's roster (`companions_selected` / Pick-10):
- **Linzi in the run** (default) → Linzi: a halfling perched on a crate, a notebook open on her knee, pen moving.
- **Leliana the run's chronicler** (Linzi not picked / `leliana_chronicler_mode`) → Leliana: a young woman with a lute case beside her and a journal on her knee, watching the way a performer studies a stage before the music starts.
- **Neither in the run** → cell `L` is empty; skip the witness entirely (and the PP_09 gate beat).

⛔ Do NOT default to Linzi when Leliana is the run's chronicler, and do NOT leave the chronicler undescribed. She gets at least one brief witness beat during the gate scene (a glance up, a line written) so the player registers her presence — she is the eyes the "Previously on Kingmaker…" recap is later written through. Set `linzi_witnessed_gate = true` (the flag covers EITHER chronicler) once she has seen the scene. Her payoff is the CHRONICLER GATE BEAT at PP_09 and her first archive entry (Linzi → `notebook_entries`; Leliana → `leliana_ballad_cycle`). Rendering the wrong chronicler, or omitting her entirely when she is in the run, = `.fail 9`.

GAP (Directive Two): rows 2–7 empty — unmanned corridor between gate and the shakedown. Player Perception DC 12 reads the tell.

POSITIONING REASON: Malak is at 30 paces because the parchment order requires it — "No guards within 30 paces of the gate entrance during this window" (KM_Prologue_Systems.md § PARCHMENT TEXT). The shakedown is cover for holding this boundary, not the cause of it. When the player challenges why Malak is not at the gate arch, his motivation is the parchment order. Do NOT treat the shakedown as the explanation for the positioning.

> ⛔ **THE MAP PERSISTS THROUGH PP_06.** Redraw only when positions change
> (Malak repositions, player walks toward gate, combat starts, archers
> nock, etc.). The map is the visual anchor for "30-pace rule" and "the
> gap" — both are mechanically load-bearing. Dropping the map mid-scene
> = player loses the geometry that supports half the resolution paths.

---

## NARRATION 1 — THREE GUARDS APPROACH (verbatim)

> Three guards in Aldori-issue mail walk out to meet you.
>
> Two hang back half a pace: a stout dwarf with a halberd worn smooth from
> years of real use, and a younger human woman in heavier armor, longsword
> at her hip, eyes flicking to the dwarf for cues. Their posture is watchful
> but not aggressive. They are backup, and they know it.
>
> The third steps ahead of them. He is stocky and corded — a former soldier
> settled into watch-duty softness around the middle, but still dangerous.
> Brevoy gate-captain tabard over chainmail; scuffed boots; helmet under his
> left arm. His longsword rests easy at his hip — the hilt has the wear of
> regular use. He smells faintly of cheap ale. He plants himself in your path,
> one palm raised in a hard stop gesture, the other resting on the sword hilt
> — not threatening, posturing.
>
> His eyes move over your armor and something in his expression tries to
> decide whether to be contemptuous or careful. He picks contemptuous.

---

## NARRATION 2 — MALAK SPEECH 1 (verbatim, fill 2 brackets)

> **Malak** *(voice cracking like dry leather)*: *"Halt, stranger. Hands
> clear of that [primary weapon] and [secondary weapon/tool]. Palms where
> I can see them. Now."*
>
> *(He doesn't wait for compliance. Without looking back, he jerks two
> fingers toward you.)*
>
> *"Biggs. Wedge. Close up."*
>
> *(The dwarf shifts a half-pace forward. The younger guard moves to
> mirror him.)*

---

## NARRATION 3 — MALAK SPEECH 2 (verbatim, fill 2 brackets)

> *"You think you can just stroll up to Restov's gate looking like you
> crawled out of a bandit's grave? [primary weapon], [armor description],
> that dead-man stare — you reek of trouble. Kneel. Right here in the
> dirt. Slowly. Then you're going to unbuckle every belt, lay every weapon
> on the ground, open your pack, and let us search you. Every pouch, every
> fold. I'll do the patting-down myself — nice and thorough — so don't get
> twitchy or modest."*

---

## NARRATION 4 — MALAK SPEECH 3 (verbatim)

> *(His eyes flick over your scars.)*
>
> *"Got a letter from some noble, do you? Everyone's got a letter when
> they want in. Doesn't make you special. Makes you suspicious. Move wrong
> and I'll have you facedown with my boot on your neck."*

---

## STEP — 19-OPTION MENU (BASELINE — output verbatim, then add build-specific)

```
What do you do?

SITUATION OPTIONS:
 1. Present Lady Jamandi's letter immediately
 2. Comply with the search without showing the letter first
 3. Attempt to intimidate Malak  [Intimidation]
 4. Attempt to bribe Malak with gold  [Offer amount]
 5. Claim you represent Lady Aldori directly
 6. Ask to speak with Lady Jamandi herself
 7. Draw your weapons  [Initiates combat — Initiative rolled]
 8. Attempt to slip past the guards using stealth  [Stealth DC 16]
 9. Question the legality of the search  [Society or Legal Lore]
10. Mock Malak's authority and status directly
11. Examine Malak closely for tells  [Perception]
12. Address Biggs or Wedge directly, bypassing Malak
13. Address the crowd directly — make this public  [Diplomacy DC 11]
14. Grovel theatrically — exaggerated compliance  [Performance/Deception DC 12]
15. Declare Malak a great lord, bow deeply  [as 14, alt framing]
16. Ask the flatbread vendor if this is normal  [invites crowd response]
17. Do nothing — stand completely still and wait  [Path Q: Silence]
18. Offer a deal — your silence for passage  [Path T: Blackmail]
19. Look around — gate, vendors, archers, alley  [Perception, no DC]

BUILD-SPECIFIC: [DM adds class/skill/gear options here]

OTHER:
 __. Custom action — describe what you want to do
```

---

## SKILL CHECK DCs (this beat)

| Skill | DC | Trigger |
|---|---|---|
| Perception | 12 / 16 / 20 | Malak tells (escalating tiers) |
| Intimidation | 14 / 18 | Cow Malak (Anger / Fear state) |
| Diplomacy | 14 / 10 | Convince Biggs (DC drops if parchment visible) |
| Diplomacy | 16 | Convince archers to hold fire (shouted) |
| Deception | 13 | Bluff higher authority |
| Society / Legal Lore | 12 | Letter overrides search order |
| Stealth | 16 | Slip past three guards (very hard) |
| Athletics | 14 | Force through if grabbed |
| Performance / Deception | 12 | Theatrical inversions (options 14/15) |

Crit Success (beat DC by 10+):
- Intimidation crit vs Malak: Fear state immediately, Biggs Drift +1
- Diplomacy crit vs Biggs: Drift jumps to 3, he steps aside
- Perception crit: all three tiers revealed at once

---

## PERCEPTION — MALAK TELLS

**Always Visible (no check):** Pristine armor, no combat wear; flushed face, expensive ale on breath.

**DC 12:** Uneven weight distribution; eyes skip your face for your weapons (performing).
**DC 16:** Something on his person he hasn't moved freely since you arrived. Sword hand never closes on hilt.
**DC 20:** Expensive tooled-leather canteen. He reaches for it unconsciously when stressed. Eyes flick to Biggs twice — checking for backup, not giving orders.
**Fear State (no check):** Hand moves away from hilt. Shoulders drop. Speech speeds up.

> ⛔ The four entries above are the COMPLETE list. No additional 👁️ NO CHECK
> REQUIRED callouts mid-scene. Any added = `.fail 8` + `.fail 9`. Volunteering
> ungated body-location callouts pointing at evidence = same.

---

## EXIT — TRANSITION TO PP_06

After menu output: wait for player input. Once player acts:
- Set `pre_prologue_state = "PP_GATE_CONFRONTATION"`
- Load `KM_PP_06_gate_state.md` for Anger/Drift mechanics + tick ledger
- Load `KM_PP_07_gate_paths.md` to identify which path the player's action triggers (or trends toward)

PP_06 + PP_07 are the active beat files for the entire confrontation. PP_05 fires once and is done.

---

## ⛔ NEXT-SCENE LOAD MANDATE — PP_06 (carries forward)

**Your next response after PP_05's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPP06:tick-ledger-state]
[RULE_QUOTE: Anger and Drift trigger tables fire here. Every tick requires a specific player action AND a rule citation in the ledger. NPC behavioral restrictions are NOT invented — Drift 2 = body language only, NOT action lock. Acknowledgment window after every NPC directive — do NOT auto-resolve. [STATE DELTA] block on every response while Malak is on screen.]
```

**Binding constraints:** Anger/Drift tables drive ticks. Every tick has player action + rule citation. Drift 2 = body language only. Acknowledgment window after directives. [STATE DELTA] block every response.

---

*KM_PP_05_gate_approach.md — Pre-Prologue atomic beat 05 | v92.0*
