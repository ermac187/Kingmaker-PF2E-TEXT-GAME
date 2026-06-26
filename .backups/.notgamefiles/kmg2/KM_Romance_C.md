# KINGMAKER — ROMANCE: GRACEFUL FADE & CAUGHT CHEATING
## KM_Romance_C.md | Sidecar to KM_Romance_B.md

> **DM:** Continuation of KM_Romance_B.md. Load alongside
> KM_Romance.md and KM_Romance_B.md whenever any companion is
> at Stage 1+.

---

## 🌅 GRACEFUL FADE

**Command:** `.fade [name]`

Voluntary wind-down. No rupture. No roll. No confrontation.
Requirements: Stage 1+. Available even during a Paused state.

### EFFECT ON USE

  Stage drops 1 immediately.
  Next 2 chapters: Stage moves −1/chapter toward Neutral (0).
  Romance heat decays to 0.
  Companion does not initiate romantic gestures, Camp Interludes,
  or flag romantic dialogue during the fade window.
  `date_awkward` flag applies for the full fade duration.

**Stage floor:** Cannot go below 0 (Neutral). Fade completes there.
  Companion does not become hostile or lose Opinion.

**Re-ignition:** Once Stage reaches 0 and fade is complete, player
  may pursue normally from Stage 0 via standard Stage progression.
  No shortcut. No penalty beyond the Stage loss.

**Acknowledgment scene:** If Stage was 3+ when `.fade` was issued,
  a brief non-confrontational acknowledgment fires at completion
  (2 chapters later). Narrative only — 2–3 beats, no player choice.
  The companion names what happened without accusation.

**Fade is not Paused.** No `.mend` needed. Fight system does not fire.
  Companion remains active in combat, plot, and agenda — fully present,
  only the romantic current withdraws.

### PER-COMPANION FADE BEHAVIOR

*Linzi:* The notes get shorter. She doesn't ask about it. The book
  stays closed when you're near.
*Goldmoon:* She prays at a different hour. Still warm at distance.
  The warmth stops reaching.
*Tika:* Goes back to business without discussion. Checks in once.
  Doesn't push it.
*Ryuko:* Adjusts her usual distance outward by exactly one step.
  Understood. Nothing said.
*Morrigan:* Accepts it as a reasonable conclusion. The occasional dry
  observation. No bitterness in it.
*Sucrose:* Shorter exchanges. Still helpful. The smile gets careful.
*Artoria:* Professional return. Treats it as a transition between
  states, not a failure of any kind.
*Olivier:* Back to the chain of command. The brevity is the only
  indication anything changed.
*Yoko:* Louder in groups. Quieter alone. You both notice. Neither
  mentions it.
*Kyoko:* Longer pauses before answering. Something she's filing away.
  She does not ask you to explain.
*Tatsumaki:* Does not acknowledge the shift. You simply see her less.

### SAVE BLOCK

Add to each companion's romance entry when fade fires:
```json
"fade_active": false,
"fade_chapters_remaining": 0
```
Set `fade_active: true`, `fade_chapters_remaining: 2` on `.fade`.
Decrement at each chapter advance. Clear at 0 or re-initiation.

---

## 💔 CAUGHT CHEATING

Fires when a companion detects the player holds concurrent Stage 1+
romances. Passive — the companion figures it out; no player action
triggers it.

### DETECTION

Detection roll fires each chapter advance when 2+ Stage 1+ romances
are active. DM rolls d20 (no modifier) per at-risk companion.

| Opinion tier | Detection DC |
|---|---|
| Friendly (+11+) | 8 |
| Warm (+6–10) | 12 |
| Favorable (+1–5) | 16 |
| Cool or lower | 20 |

Roll ≥ DC → companion confronts player that chapter.
Companions in Paused state do not roll detection.
Companions whose fade is active do not roll detection.

### THE CONFRONTATION SCENE

3–4 beats. Companion states what they know or suspect.
Player presents one option:

| Option | Skill | DC |
|---|---|---|
| **Come Clean** | — | automatic |
| **Deny** | Deception | 16 + (2 × Romance Stage) |
| **Reframe** | Diplomacy | 14 + (2 × Romance Stage) |

Stage = romance stage with the confronting companion.

**Come Clean (automatic):**
  Paused: Moderate (2 chapters). Opinion −2. Stage −1.
  `.address` (Open Arrangement) available after Paused ends — DC +2
  above standard. No penalty for honesty beyond the Pause itself.

**Deny — Success:**
  Companion accepts it. Opinion −1. No Pause. Heat cools 1.
  `deny_used_this_arc: true`. If detected again same arc: Deny
  auto-fails, add 1 severity tier to resulting Pause duration.

**Deny — Failure:**
  Companion knows you lied. Paused: Severe (3 chapters).
  Opinion −3. Stage −2. `.mend` DC +4 above standard formula.

**Reframe — Success:**
  "I wasn't sure what we were." Companion accepts the framing.
  Opinion −1. No Pause. Heat resets to 0. Stage unchanged.

**Reframe — Failure:**
  Companion doesn't accept it. Paused: Moderate (2 chapters).
  Opinion −2. Stage unchanged.

### PER-COMPANION CONFRONTATION STYLE

| Companion | Discovery and approach |
|---|---|
| **Linzi** | Stops writing mid-sentence. Sets the journal down. Asks quietly — one question. |
| **Goldmoon** | Already there when you arrive. Seated. She knows. Wants to hear it from you. |
| **Tika** | Shows up where you didn't expect her. Not an ambush — she just appeared. Waits. |
| **Ryuko** | Puts the fact on the table without preamble. States it. Waits for an answer. |
| **Morrigan** | Mildly curious about your explanation. You will not enjoy being examined like this. |
| **Sucrose** | Has documented the timeline. Shows you the notebook. Turns to the relevant page. |
| **Artoria** | Formal. "There is a matter I need to raise with you." Every word chosen. |
| **Olivier** | This is a debrief. Every inconsistency is already accounted for. She has the notes. |
| **Yoko** | Loud for three seconds. Then quiet. The quiet is the actual problem. She knows it. |
| **Kyoko** | She had a theory. Evidence confirmed it. She looks like she wishes it hadn't. |
| **Tatsumaki** | No expression. Two words: "How long." |

### SAVE BLOCK

Add to each companion's romance entry:
```json
"cheating_detected": false,
"cheating_confrontation_count": 0,
"deny_used_this_arc": false
```
Set `deny_used_this_arc: true` when player chooses Deny.
Reset at new arc (major chapter transition).
Increment `cheating_confrontation_count` each confrontation scene.

---

## 💕 LOVE SCENE SYSTEM

**Command:** `.loveScene [companion]`

Milestone intimacy scene. Not a simple beat — a scene with weight and
consequence. Completion satisfies the marriage prerequisite
(`love_scene_occurred: true`) required alongside Stage 5 before
`.propose` unlocks.

### TRIGGER CONDITIONS

Both must be true:
- Companion at **Stage 4+**
- `gesture_returned ≥ 3` this arc (tracked in romance state)

OR: `.loveScene [companion]` forces the scene check. DM validates
conditions first — if not met, scene does not fire.

### INTERRUPTION CHECK

Fires when 2+ companions are at Romance Score ≥ 2.
DM rolls d20 vs DC 14 (no modifier).

- **Roll ≥ 14:** Scene proceeds uninterrupted.
  `love_scene_occurred: true`. Done.
- **Roll < 14:** Rival walks in. The companion with the highest
  `passive_jealousy heat` is the intruder.

No interruption check if player holds only one active romance
(Score ≥ 2).

### INTERRUPTION — THREE CHOICES

---

#### [Chase after them]

Player leaves their current partner to pursue the rival.

**Love scene:** Aborted immediately. NOT resumable this arc.
  To re-trigger: rebuild to Stage 4 (`gesture_returned` resets to 0).
  `love_scene_aborted: true` until Stage 4 is re-reached.

**Partner A (abandoned mid-scene):**
  Stage −2 (floor: 0) | Opinion −4 | Paused: Severe (3 chapters)
  `.mend` required DC 18. `love_scene_aborted: true`.
  Companion voices abandonment immediately (see table below).

**Rival (chased):**
  Enters conversation mode. DM voices the rival's reaction based on
  their personality and current Romance Stage. No predetermined
  outcome — the conversation decides what happens next. Player may
  explain, apologize, or deflect. Rival's Opinion and Stage shift based
  on how the exchange resolves.

---

#### [Stay]

Player remains. The rival leaves.

**Love scene:** Completes. `love_scene_occurred: true`.
  Marriage prereq satisfied. Stage +1 (if below max).

**Rival (witnessed, then departed):**
  Opinion −4 | Stage −2 (floor: 0) | Paused: Severe (3 chapters)
  `.mend` required DC 18. Rupture path activates
  (see KM_Romance_B.md § Jealousy Ladder).
  Companion voices departure immediately (see table below).

---

#### [Call out — Diplomacy DC 18]

Player attempts to address both at once.

**Success:**
  Rival hears enough to step back without full rupture.
  Current partner: Strain +1 (marriage_strain if married). No Stage loss.
  Rival: Opinion −1. Heat → 0. Exits without entering Paused.
  Scene resumes. `love_scene_occurred: true`.

**Failure:**
  The moment collapses. Both companions withdraw.
  Current partner: Opinion −2. Stage −1.
  Rival: Opinion −2. Stage −1.
  Love scene aborted (not resumable this arc).
  `love_scene_aborted: true`.

---

### PER-COMPANION WALK-IN REACTION (rival entering)

| Companion | Walk-in line |
|---|---|
| **Linzi** | Drops whatever she was holding. One short syllable. Then nothing. |
| **Goldmoon** | Stops in the doorway. Doesn't move. The expression is very still. |
| **Tika** | Goes red. Backs out one step. "I — sorry. I'll —" and stops. |
| **Ryuko** | Reads the room instantly. Doesn't speak. The look says everything. |
| **Morrigan** | A beat of genuine quiet before anything else. The smile that follows is very controlled. |
| **Sucrose** | Both hands over her mouth. Eyes wide. Starts to say your name and stops. |
| **Artoria** | "My apologies." One sentence. She is already turning. |
| **Olivier** | Her jaw sets. Eyes move from you to your partner and back. "I see." |
| **Yoko** | "Oh. Oh, that's — yeah." Looks at the ceiling. Long exhale. |
| **Kyoko** | Three seconds of silence. She closes her notebook. "I'll come back." |
| **Tatsumaki** | Doesn't speak. The door closes. |

### PER-COMPANION ABANDONMENT REACTION (Partner A — player chased rival)

| Companion | Abandonment reaction |
|---|---|
| **Linzi** | Doesn't call after you. When you return, the room is empty. The journal is on the table, closed. |
| **Goldmoon** | Still there when you come back. Won't look at you for a long moment. "That's what I needed to know." |
| **Tika** | Gone by the time you return. Functional at camp. Doesn't bring it up. The distance does instead. |
| **Ryuko** | Sitting exactly where you left her. When you return: "You made your choice." That's the whole conversation. |
| **Morrigan** | By the fire when you get back. "I assume it went well." She does not mean that kindly. |
| **Sucrose** | Busy when you return. Very busy. Everything has her full attention except you. |
| **Artoria** | "I understand." She does not mean it as absolution. |
| **Olivier** | Standing. Arms crossed. "We're done here." Not a question. |
| **Yoko** | You hear her before you see her — too loud, too cheerful, talking to everyone else. |
| **Kyoko** | Gone. The observation she was saving for this moment goes into the notebook instead. |
| **Tatsumaki** | Not present when you return. When she reappears at camp: silence. You will earn every word back. |

### SAVE BLOCK

Add to each companion's romance entry when love scene triggers:
```json
"love_scene_occurred": false,
"love_scene_partner": "",
"love_scene_interrupted": false,
"love_scene_rival": "",
"love_scene_choice": "",
"love_scene_aborted": false
```

Set at resolution:
- `love_scene_occurred: true` — on completion (Stay or Call out success)
- `love_scene_partner` — companion the scene completed with
- `love_scene_interrupted: true` — if rival walked in
- `love_scene_rival` — companion who walked in
- `love_scene_choice` — "chase" | "stay" | "call_out_success" | "call_out_fail"
- `love_scene_aborted: true` — if aborted; clears when Stage 4 is rebuilt

---

*KM_Romance_C.md — Graceful Fade + Caught Cheating + Love Scene v2.0*
*Pair-load with KM_Romance.md and KM_Romance_B.md (Stage 1+ required).*
