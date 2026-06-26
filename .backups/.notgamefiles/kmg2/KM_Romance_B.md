# KINGMAKER — ROMANCE: TWO-TIMING & JEALOUSY RESOLUTION
## KM_Romance_B.md | PAIR-LOAD WITH KM_Romance.md
## Continuation file. Always load alongside Romance main + Romance_P2 + Romance_P3.

> **DM:** This file extends KM_Romance.md with the Two-Timing Escalation
> ladder and the Jealousy Resolution Path. Trigger any time the player
> has Romance Score ≥ +1 with two or more companions simultaneously, OR
> any time a companion is Type A (jealous) per StateVoice_C System 3.

---

## ⚖️ TWO-TIMING ESCALATION

When the player has Romance Score ≥ +1 with **two or more** companions simultaneously:

```
TIER 1 — UNDER THE SURFACE (Stage 1 with both)
  No mechanical penalty yet. Companions sense it but have not confirmed it.
  Camp Interludes for both fire normally.

TIER 2 — KNOWN (Stage 2 with one OR Stage 1+ with both)
  Both companions become aware. Save flag: love_triangle_active = TRUE.
  Each tick of Romance Score on EITHER companion now applies a parallel
  penalty:
    Romance +1 with companion A   →   companion B: Romance −1, Opinion −1
    Romance +1 with companion B   →   companion A: Romance −1, Opinion −1
  This is the "they find out by absence" rule. Off-screen knowledge
  propagates through party banter (KM_Companions_Banter.md handles voice).

TIER 3 — CONFRONTED (Stage 3 with one, Stage 2+ with the other)
  At the next quiet camp, the lower-Stage companion confronts the player
  ONCE. DM runs a 4–6 exchange scene. Player choices:
    [Choose them]      → Other companion drops to Stage 0, Romance Score = 0,
                          attraction flag clears. They withdraw cleanly. No
                          recovery without major arc (≥3 sessions of repair
                          + a sacrifice).
    [Choose the other] → This companion drops to Stage 0 same way. Symmetric.
    [Refuse to choose] → Both drop one Stage. love_triangle_active stays TRUE.
                          Each subsequent Romance tick now applies DOUBLE
                          parallel penalty (−2 instead of −1) to the other.
                          Persisting past Tier 3 without choosing forces
                          Tier 4.
    [Honest disclosure
     of feelings for both] → Diplomacy DC 18 (very hard). Critical Success:
                          one or both companions accept the open arrangement
                          (per their values — see § OPEN ARRANGEMENT below).
                          Success: penalty reduced to ½ but Stages capped at 3
                          for both until resolved. Failure or worse: Tier 4
                          fires immediately with both at the same drop.

TIER 4 — RUPTURE (Stage 4+ reached with one while ≥ Stage 2 with the other)
  The non-chosen companion experiences this as betrayal regardless of
  player intent. Their Stage drops to −2 (Wounded), Opinion drops by 4,
  and they fire ONE pointed scene. After that scene:
    - If they were Type A (jealous) per StateVoice_C → they convert to
      Type C (hostile-to-rival) and lines escalate accordingly.
    - If they were Type B (protective) → they become Type A; the player
      did not deserve their watch.
    - Recovery: only via a sustained repair arc (5+ sessions, sacrifice
      required, no further Romance progression with the chosen partner
      during the arc).
```

**Off-screen detection rules:** A companion does NOT need to be present in
the scene to find out. By Stage 2+ with a second companion, the party
*including* the unwitting first companion has noticed (at minimum) one of:

- The second companion's behavior shift (Linzi writes about it; Yoko teases;
  Tatsumaki sneers; Olivier reviews tactical pairings). Banter spreads it.
- The player's own behavior — choices, gifts, time allocation — read against
  the first companion's expectations.
- The companion's own intuition, gated by their Opinion Score: at WARM (+6+)
  they notice within one session; at FAVORABLE (+1–5) within two; at NEUTRAL
  or below, never until directly told.

**The "they don't have to say it" rule:** A companion who has discovered the
two-timing applies their full penalty silently. Their behavior shifts
(Score-State Voice activates a tier earlier; Camp Interludes stop firing for
them). The player is not informed. The save block flags `secretly_aware:
true` on the companion entry. The Opinion Score and Romance penalties have
already applied.

---

## 🕊️ JEALOUSY RESOLUTION PATH

A companion in active Type A (jealous), Type B-converted-to-A, or post-
rupture Stage 2+ jealousy state can be brought back. This is a deliberate
arc — not a single conversation.

### Stage 0 — Pre-resolution Diagnostic

Before any repair attempt, the DM checks:

```
- Is romance with the chosen partner stable (Stage 3+)? Required.
- Is the jealous companion at Romance Stage ≥ 0 (not in active Rupture)?
  Required — Rupture must be addressed via the harder repair arc first.
- Has the player attempted to address jealousy in any form previously?
  This affects the DC.
```

### Stage 1 — Open the Conversation (player-initiated)

Player uses `.address [companion]` command, OR brings it up in a Camp
Interlude using a custom dialogue option. The DM runs a 6–10 exchange
scene with three explicit player postures:

```
[Acknowledge]   "I noticed. I should have said something earlier."
[Apologize]     "I didn't see it clearly. I'm sorry."
[Reframe]       "You and I are not the same kind of thing as me and them.
                 Both are real."
```

Each posture rolls Diplomacy vs the companion's current Opinion-tier DC:

| Companion Opinion Tier | Diplomacy DC |
|---|---|
| Friendly (+11+)   | 14 |
| Warm (+6 to +10)  | 17 |
| Favorable (+1–5)  | 19 |
| Cool (−1 to −5)   | 22 |
| Strained (−6−)    | 25 (and only [Apologize] is available) |

**Critical Success:** Companion accepts. Type A flag cleared. Romance
returns to actual current Stage (no higher). Opinion +2.
**Success:** Companion accepts conditionally — *"I will see what comes
next."* Stage normalizes; jealousy lines downgrade to once per chapter
instead of session. Opinion +1.
**Failure:** No change. Player may try again after one full chapter.
**Critical Failure:** Companion says something true and unkind. Opinion
−1. Lock for two chapters before retry available.

### Stage 2 — Sustain (over 2–3 sessions)

After a successful conversation, the companion enters a watching period.
The DM applies these passive checks each session:

- Did the player include them in a meaningful party assignment? (+1 progress)
- Did the player give them a gift, attention, or remembered detail? (+1)
- Did the player flirt with the chosen partner *in front of* them? (−2)
- Did the player two-time AGAIN with a third companion? (auto-fail; back to
  Tier 3 of two-timing escalation)

At 3 progress points, the resolution lands. Type A flag fully cleared.
Save block: `jealousy_resolved: true, resolution_session: <N>`.

### Stage 3 — Open Arrangement (rare path, only if attempted in Tier 3)

If the player passed the DC 18 honest-disclosure check at Tier 3, both
companions accept an open arrangement. Per-companion willingness:

| Companion | Open Arrangement |
|---|---|
| Linzi | Accepts — *"It complicates the chronicle. I'm taking notes."* |
| Goldmoon | Accepts only if the other partner is honored equally; she will officiate both. |
| Tika | Accepts cheerfully — *"More people who love you. Sounds right."* |
| Ryuko | Refuses — *"Pick. I'm not a backup."* |
| Morrigan | Accepts — *"Chains are chains. The absence of one is the gift."* |
| Sucrose | Accepts but anxiously — needs frequent reassurance scenes. |
| Artoria | Refuses — vow-coded; one liege, one consort. |
| Olivier | Accepts conditionally — *"State the arrangement clearly. We will hold to it."* |
| Yoko | Refuses — *"I don't share. Not this."* |
| Kyoko | Accepts after analysis — *"The arrangement reduces statistical risk if all parties consent. Acceptable."* |
| Tatsumaki | Refuses with contempt — *"Pick. Or I will pick FOR you. Last chance."* |
| Tristian | Accepts only if blessed by faith conversation — Sarenrae teaches love is not zero-sum. |
| Octavia | Accepts — *"I've shared everything else. This is fine. Don't lie about it."* |
| Daeran | Accepts theatrically — *"How modern of us all."* |
| Ember | Accepts — *"There is enough of you for both. There is enough of me for both."* |

Companions who refuse exit the romance permanently with Romance Score = 0
and Opinion −1. They do NOT become hostile — they have decided.

### Save Block Additions

```json
"jealousy": {
  "love_triangle_active": false,
  "competing_companions": [],
  "tier_reached": 0,
  "open_arrangement": false,
  "open_partners": [],
  "secretly_aware": {},
  "resolution_attempts": [],
  "jealousy_resolved": false,
  "resolution_session": null
}
```

---

## ⚔️ COMPANION RIVALRY — JEALOUSY TURNS PHYSICAL

> **DM:** When jealousy between two companions escalates to Tier 3
> (Confrontation) and the player fails or refuses to intervene, the
> confrontation may turn physical. Run this as a **cinematic scene** —
> no initiative, no turn order, no per-hit dice. Use each companion's
> class abilities, Signature moves, and Core Value to write 3–5 dramatic
> beats until one cannot continue. The fight ends when one clear beat
> lands that the other cannot answer.

---

### COMPANION-VS-COMPANION ESCALATION

Separate from the player-facing jealousy ladder. Tracks the two
companions' relationship with *each other*.

```
TIER 1 — COLD
  Clipped responses between the two companions. No cooperation in skill
  challenges. Pointed banter when the player isn't present. Player may
  notice or may not.

TIER 2 — FRICTION
  Open argument scene in camp or mid-travel. Player witnesses or hears
  about it. Can intervene or let it run.
  Combat effect: neither companion will use assist actions for the other.
  They will not cover each other's flank. CombatAI cooperation between
  them is suspended.

TIER 3 — CONFRONTATION (brawl eligible)
  One companion initiates directly. If player fails DC 18 Diplomacy
  intervention (or chooses not to try), the scene turns physical.
  DM runs the CINEMATIC BRAWL (see below).
  Combat effect (Tier 3+): companions may countermand each other's
  tactical calls mid-fight. DM applies this as narrated friction.

TIER 4 — ULTIMATUM OR TRUCE
  One companion forces a resolution — with the player OR between
  themselves. Mandatory scene. Player cannot defer.
  Rare: at Tier 4 in a critical moment, the injured companion may
  hesitate to save the other. DM rolls secretly (DC 12 flat; failure
  = one round of inaction).
```

---

### CINEMATIC BRAWL

**Player intervention window:** Once, after Beat 3 (before the final
beat). Diplomacy DC 18. Success halts both at Shaken. Failure: scene
finishes without interruption.

**Outcome by matchup:**

| Matchup type | Loser result | Winner result |
|---|---|---|
| Close match (similar class tier) | Hurt (1 chapter out) | Shaken (2 scenes) |
| Clear mismatch | Seriously Injured (2 chapters) | Shaken or unscathed |
| Extreme mismatch | Auto — Seriously Injured, no roll | Unscathed |

**Tone rule:** These companions live and fight together. The brawl should
feel like something that cannot be taken back. Not cartoonish. Not
lethal. Ugly. Real. The player watching knows it is their fault.

**Mutual respect clause:** Some close-match pairings end with both
companions' Opinion of *each other* rising +1 (they tested each other
and found something worth respecting). DM judges per personality. Ryuko
and Yoko are the template.

---

### INJURY STATES

| State | Duration | Effects |
|---|---|---|
| **Shaken** | 2 scenes | In party; −2 to all checks; no romance interactions |
| **Hurt** | 1 chapter | Out of active party; camp dialogue only; no combat |
| **Seriously Injured** | 2 chapters | Bedridden; one check-in scene per chapter only |
| **Grave** | Until healed | Requires Goldmoon active + 500 gp OR story item |

**Kingdom cost:** Any advisor role held by an injured companion is
unstaffed. Relevant stat −1 per turn out.

**Recovery acceleration:**

| Method | Effect |
|---|---|
| Goldmoon in active party | Halves duration (round up) |
| Player uses healing item directly on them | −1 chapter |
| Player spends 1 Hero Point | Skip to Shaken immediately |
| Sucrose crafts tincture (Alchemy DC 16) | −1 chapter |

---

### CHECK-IN SCENE (during recovery)

Player may visit the injured companion once per chapter. 3–4 beat scene.
Tone set by who initiated the fight and whether the player took sides.

| Player behavior | Mechanical result |
|---|---|
| Visited every chapter + brought something relevant | Opinion +1; romance resumes at full Stage on return |
| Visited inconsistently | No change; romance resumes |
| Never visited | Opinion −2, Romance −1 on return |
| Accelerated recovery actively | Opinion +2; unique flavor line unlocked |
| Took the rival's side | Scene is short and careful. Relationship Paused until `.mend` |

---

### AFTER RECOVERY

A brief scene fires when the injured companion returns to active status.
Player gets one exchange before normal party life resumes.

The rival companion's Tier resets to 2 (Friction) after a brawl resolves
via injury — they have established a hierarchy. May escalate again if
the underlying cause (the player's choices) is not addressed.

---

## 🥊 EXAMPLE BRAWLS (DM REFERENCE)

Three reference scenes. Each shows how class abilities, Signatures, and
Core Values shape the fight. Use as templates for unlisted pairings.

---

### ARTORIA vs. TATSUMAKI

**Matchup:** Extreme mismatch. Artoria wins every fight on the ground.
This one does not stay on the ground.
**Result:** Artoria — Hurt (shoulder, 1 chapter). Tatsumaki — Shaken (2
scenes). Fight ends because Artoria *decides* it does. Tatsumaki knows
the difference. That is the part she will be thinking about.

**Beat 1 — The Line**
Artoria speaks first. She does not raise her voice. She says the thing
that is technically true and lands like an accusation because of how
precisely it is aimed.
Tatsumaki looks at her for a long moment.
*"You finished?"*

**Beat 2 — Off the Ground**
Artoria reaches for Caliburn. Force hits her before the blade clears
the scabbard — a wall of telekinetic pressure that lifts her two feet off
the ground. Her armor makes it worse. Tatsumaki stands below her, arms
crossed, not breathing hard.
*"I could drop you. I won't. But I want you to know I thought about it."*

**Beat 3 — The Answer** ← Player intervention window (DC 18 Diplomacy)
Artoria's aura ignites. Divine radiance floods the space — not an attack,
a statement. Suspended, completely composed, she looks down.
*"You're afraid of losing something you haven't admitted you want. I
understand that. It doesn't make this right."*
The pressure holding her wavers for exactly one second.

**Beat 4 — The End**
Tatsumaki drops her. Not gently. Artoria lands in a controlled roll,
comes up on one knee — something in her shoulder is wrong. She stays
there. Not because she cannot stand. Because she is choosing not to
escalate.
Neither of them says anything else.

---

### TIKA vs. MORRIGAN

**Matchup:** Not a physical fight. Morrigan does not brawl. She makes it
something else. Tika loses anyway.
**Result:** Tika — Shaken (emotional, 2 scenes). Morrigan — technically
uninjured. Her Opinion of player drops −1 from something she said that
she cannot take back.

**Beat 1 — The Approach**
Tika starts with *"I think we should—"*
Morrigan interrupts. Quietly. One sentence that reframes everything Tika
thought she understood about the situation. It is not cruel. It is
precise. Tika stops mid-word.

**Beat 2 — The Hex**
Tika pushes through — she is tougher than most people expect — and gets
close enough to grab Morrigan's arm. *"Stop doing that. Just talk to me."*
Morrigan looks at the hand on her arm. A hex fires — not Misfortune,
something that makes Tika suddenly, completely uncertain of what she was
about to say. The words dissolve. She is left holding Morrigan's arm
with nothing behind it.

**Beat 3 — The Real Blow** ← Player intervention window (DC 18 Diplomacy)
Morrigan steps back and says something about the player. One observation.
True. The kind of true that cannot be untrue once it has been said.
Tika lets go of her arm.

**Beat 4 — What Morrigan Did Not Expect**
Tika sits down on a crate and puts her face in her hands. Not crying.
Just done. She says quietly: *"Yeah. I know."*
Morrigan had prepared for a fight. She had not prepared for this.
She says something. She does not mean to. It is almost — not an apology.
Something adjacent.
Then she leaves.

**DM note:** Morrigan dealt damage she did not intend to. File it.

---

### RYUKO vs. YOKO

**Matchup:** Close. Both apex. Both aggressive. Both honest. This one
goes the distance.
**Result:** Ryuko — Hurt (shoulder, 1 chapter). Yoko — Hurt (ribs, 1
chapter). Both out simultaneously. Player runs the next mission two
companions short.
**Mutual respect clause fires:** Both companions' Opinion of *each other*
+1. The jealousy is still there. It is just complicated now.

**Beat 1 — Range**
Yoko has the advantage before Ryuko closes. Lagann is already up,
tracking. She does not fire. She is making a point about distance.
*"You really want to do this?"*
Ryuko closes the gap in four steps, Senketsu half-activated.
*"You shot first. I just haven't caught up yet."*

**Beat 2 — Contact**
They trade. No posturing. Ryuko gets inside Yoko's range advantage.
Close quarters: Ryuko's burst output against Yoko's precision. Yoko takes
a hit to the ribs she will feel for a week. Ryuko takes a near-point-blank
shot to the shoulder that leaves a burn. Neither stops.

**Beat 3 — The Real Question** ← Player intervention window (DC 18 Athletics; Diplomacy will not work here)
Brief standoff. Both breathing hard. Ryuko says, not angrily:
*"What do you actually want from this?"*
Yoko lowers Lagann two inches. Not all the way.
*"Same thing you do. That's the problem."*

**Beat 4 — The Finish**
Ryuko drives forward once more. Yoko pivots, gets her arm across Ryuko's
back, uses her own momentum to put her into the ground — controlled, not
vicious. Holds her there for three seconds. Ryuko stops. Yoko lets go
and steps back.

**Beat 5 — After**
Both on their feet. Both hurt. Yoko reloads Lagann without looking at
Ryuko. Ryuko watches.
*"You're good,"* Ryuko says.
*"Yeah,"* Yoko says. *"So are you."*
Neither of them figures out what to do with that.

---

### Save Block Addition

```json
"companion_rivalry": {
  "Ryuko_Yoko": {
    "tier": 3,
    "cause": "player Stage 3 with both",
    "last_event": "cinematic brawl — both Hurt, Ch1",
    "combat_cohesion": false,
    "mutual_respect": true,
    "resolution": null
  }
}
```

---

## 🌡️ PASSIVE JEALOUSY HEAT

> **DM:** This system fires without the player two-timing. Companions who
> are attraction-flagged (OR Romance ≥ Stage 1) track a hidden heat meter
> when rival companions make moves on the player — gifts, flirting, Camp
> Interludes, dates. The player is the passive object. No choice has been
> made. The jealousy builds between rivals, not between rival and player.
> Never announce the heat level. Apply behavioral signals silently.

**Heat meter:** 0–10 per jealous-companion/rival pair. Tracked in save
block under `passive_jealousy{}`. Player never sees the number.

---

### HEAT GENERATION (per session, cumulative)

| Event | Heat |
|---|---|
| Rival gives player a meaningful gift | +1 |
| Rival flirts with player in a group scene | +1 |
| Rival has a private Camp Interlude with player | +1 |
| Player reciprocates the rival's flirting | +2 |
| Rival's attraction behavior becomes visible to the party | +1 |
| Player selects rival for a date | +2 |
| Rival's Romance Score advances a Stage | +2 |
| Player publicly compliments the rival in front of others | +1 |

### HEAT BLEED (per session)

| Event | Heat |
|---|---|
| Player gives the jealous companion direct attention | −1 |
| Player selects jealous companion for a mission over the rival | −1 |
| Player does not reciprocate the rival's advance | −1 |
| Player has Camp Interlude with the jealous companion | −2 |

---

### BEHAVIORAL SIGNALS BY THRESHOLD

DM applies all of these silently. No announcement.

| Heat | What the jealous companion does |
|---|---|
| 0–3 | Nothing visible. Still. Watching. |
| 4–5 | Type A ambient lines begin — one per session. Brief. Deniable. |
| 6–7 | Pointed comments about the rival that are not quite comments about the rival. The rival notices. |
| 8–9 | Inserts themselves — volunteers for everything the rival volunteers for, positions near the player in camp. Tension is palpable to anyone paying attention. |
| 10 | **BOILING POINT** — confrontation scene fires. |

---

### PERSONALITY MODIFIERS

| Companion | Modifier | Boils at | Reason |
|---|---|---|---|
| Tatsumaki | −2 | 8 | Acts before she means to |
| Sucrose | −1 | 9 | More sensitive to being passed over |
| Ryuko | 0 | 10 | Honest and direct; not hair-trigger |
| Yoko | 0 | 10 | Same as Ryuko — won't wait long either |
| Goldmoon | 0 | 10 | Prays about it first; then acts |
| Kyoko | +1 | 11 | Processes methodically before moving |
| Tika | +1 | 11 | Generous; assumes the best; slower to read it |
| Artoria | +2 | 12 | Holds it longer than anyone |
| Olivier | +2 | 12 | Channels it into work; holds until it doesn't fit |
| Morrigan | +3 | 13 | Would let it burn a long time before showing it |
| Linzi | 0 | 10 | Heat is normal but telegraphed — she writes about it first; DM can signal through journal narration before behavior shifts |

---

### THE BOILING POINT SCENE

The jealous companion confronts the **rival companion** directly — not
the player. Player is present. 3–4 beat scene. Then one of four outcomes:

**Player choices during the scene:**

| Choice | Effect |
|---|---|
| **Step in** (Diplomacy DC 16) | Stops at words. Heat for both resets to 5. Companion rivalry Tier 1 established. |
| **Stay out** | Scene runs to its conclusion. Companion rivalry Tier 1 established. Heat resets to 5. |
| **Side with the jealous companion** | Rival Opinion −2. Jealous companion heat drops to 0 — but they are now aware the player intervened on their behalf. They did not ask for this. It complicates things. |
| **Side with the rival** | Jealous companion heat resets to 3 but Opinion −2 toward player. They noticed who the player protected. |

**Heat never resets to 0 after a confrontation.** The feeling does not
disappear — it settles at a lower level. The rival pair enters the
companion rivalry system (Romance_B § COMPANION RIVALRY) at Tier 1
regardless of how the scene ends.

If the boiling point scene turns physical, the player's intervention DC
rises to 18 (Athletics or Diplomacy) and the cinematic brawl rules apply.

---

### SAVE BLOCK

```json
"passive_jealousy": {
  "Tatsumaki_watching_Tika": {
    "heat": 7,
    "rival": "Tika",
    "last_trigger": "player reciprocated Tika flirt at camp, Ch1",
    "behavior_tier": "pointed",
    "boiling_point": 8,
    "confrontation_fired": false
  }
}
```

---

## 📅 DATE SYSTEM

**Command:** `.date [companion] [activity]`

**Requirements (all must be met):**
- Companion at Romance Stage 4 or higher
- Only 1 date per chapter (tracked via `dates_this_chapter`)
- Kingdom Unrest ≤ 3
- Companion in active party, not injured

**Available activities:** SPAR · HUNT · STARGAZE · STUDY · TAVERN ·
  WANDER · HIKE · FISH · COOK · PATROL

---

### OUTCOME DETERMINATION

| Activity preference | Outcome |
|---|---|
| **PREFERRED** | **Great** (automatic) |
| **TOLERATED** | Roll d20 + Diplomacy vs DC 14. Success = Great. Fail = Good. |
| **REFUSED** | **Awkward** (automatic — no roll saves it) |

### OUTCOME EFFECTS

| Outcome | Romance Score | Jealousy Heat |
|---|---|---|
| **Great** | +1 to date companion | +2 to ALL other attraction-flagged companions |
| **Good** | no change | +1 to ALL attraction-flagged companions |
| **Awkward** | no change | −1 to date companion (embarrassed; withdraws) |

**Awkward follow-up:** Date companion absent from the next optional ambient
scene. Voice lines do not fire; they are not part of camp background.
Combat and plot-essential presence unaffected. Flag `date_awkward: true`
on companion entry; clears after one ambient scene.

---

### PER-COMPANION ACTIVITY TABLE

| Companion | PREFERRED | TOLERATED | REFUSED |
|---|---|---|---|
| **Linzi** | TAVERN · WANDER · STARGAZE · COOK | STUDY · FISH · HIKE · PATROL | SPAR · HUNT |
| **Goldmoon** | STARGAZE · HIKE · COOK · FISH | STUDY · PATROL · WANDER | TAVERN · SPAR · HUNT |
| **Tika** | TAVERN · COOK · WANDER · SPAR | HIKE · FISH · PATROL · HUNT | STUDY · STARGAZE |
| **Ryuko** | SPAR · HUNT · PATROL · HIKE | FISH · COOK · STARGAZE | TAVERN · STUDY · WANDER |
| **Morrigan** | STARGAZE · HIKE · STUDY | FISH · COOK · HUNT · PATROL | TAVERN · WANDER · SPAR |
| **Sucrose** | STUDY · STARGAZE · HIKE · COOK | WANDER · FISH · PATROL | TAVERN · SPAR · HUNT |
| **Artoria** | SPAR · PATROL · HUNT · STARGAZE | STUDY · COOK · HIKE | TAVERN · WANDER |
| **Olivier** | PATROL · SPAR · HUNT · HIKE | COOK · STUDY · WANDER | TAVERN · STARGAZE · FISH |
| **Yoko** | HUNT · SPAR · PATROL · TAVERN | WANDER · COOK · HIKE · FISH | STUDY · STARGAZE |
| **Kyoko** | STUDY · WANDER · PATROL · STARGAZE | COOK · FISH · HIKE | SPAR · TAVERN · HUNT |
| **Tatsumaki** | STARGAZE · PATROL · HIKE | STUDY · COOK | TAVERN · WANDER · SPAR · HUNT · FISH |

---

### NARRATION GUIDANCE

**Great:** 4–6 beats. A shared moment only possible in this activity. The
companion shows something not visible any other way. End on something the
player will remember — unexplained.

**Good:** 2–3 beats. Comfortable. Not quite magic. Something was left on
the table — not from failure, just the nature of tolerated things. End
with warmth but no revelation.

**Awkward:** 2 beats. Something went wrong in the first beat — the companion
was out of their element, or the activity surfaced a vulnerability. Second
beat is the mutual realization. End without resolution.

---

### SAVE BLOCK ADDITIONS

```json
"date_log": [
  {"chapter": "ch1", "companion": "Tika", "activity": "TAVERN", "outcome": "GREAT"}
],
"dates_this_chapter": 0
```

Reset `dates_this_chapter` to 0 on each chapter advance.
Add `"date_awkward": false` to each companion's romance entry.

---

## 🥊 FIGHT SYSTEM (PLAYER-COMPANION CONFRONTATION)

**Triggers:**
- Companion's active agenda item ignored **3 times** — fight fires at the
  next scene start. `agenda_ignored_count` resets after the fight.
- `.fight [name]` — player initiates voluntarily (Stage 1+ required).

**Commands:** `.fight [name]` | `.mend [name]`

---

### THE FIGHT SCENE

4–6 exchanges. Companion states the grievance without ambiguity.
Player presents **one posture**:

| Posture | What the player does |
|---|---|
| **Apologize** | Acknowledges the companion's grievance as valid |
| **Defend** | Argues their reasoning without conceding |
| **Counter** | Raises a specific grievance of their own |
| **Walk Away** | Ends without resolution (no roll required) |

**Roll Diplomacy for Apologize / Defend / Counter.**
Counter is unavailable at Favorable or lower Opinion.
Walk Away requires no roll; auto-sets Paused severe.

**DC by companion Opinion:**

| Opinion tier | DC |
|---|---|
| Friendly (+11+) | 14 |
| Warm (+6–10) | 16 |
| Favorable (+1–5) | 18 |
| Cool or lower | 20 — Apologize only |

**Paused duration by posture and outcome:**

| Posture | Success | Failure |
|---|---|---|
| Apologize | Mild (1 chapter) | Moderate (2 chapters) |
| Defend | Moderate (2 chapters) | Severe (3 chapters) |
| Counter | Moderate; CS adds Opinion +1 | Severe + Opinion −1 |
| Walk Away | Severe (3 chapters) | — |

---

### RELATIONSHIP PAUSED STATE

While Paused, the companion:
- **Does not:** accept romance gestures, flirt actions, Camp Interludes,
  dates, or staged signals. Passive jealousy heat does not generate.
- **Still:** fights in combat per CombatAI, voices plot-required lines,
  attends story scenes, runs their agenda.
- **Voice:** Type C lines only (cold, professional). Warm ambient absent.
- **Opinion:** no positive accumulation; negative events still apply.

Save flags: `fight_paused: true` | `paused_chapters_remaining: N`
Decrement 1 per chapter advance; clears automatically at 0.

---

### `.mend [name]` — REPAIR

Cannot use the same chapter the fight fired.
Roll Diplomacy. DC = 14 + 2 per chapter elapsed since fight (cap 22).

| Outcome | Effect |
|---|---|
| Critical Success | Paused ends. Romance returns at Stage −1 from where it was. Opinion +1. |
| Success | `paused_chapters_remaining` −1. Retry next chapter. |
| Failure | No change. Retry after 1 chapter. |
| Critical Failure | `paused_chapters_remaining` +1. Opinion −1. |

**Grand Gesture:** Declare before rolling. Costs 500 gp item OR 1 Hero
Point OR a named narrative concession. Effect: DC −4. One use per arc.
Save flag: `grand_gesture_available: false` after use.

---

### PER-COMPANION FIGHT NOTES

| Companion | Most likely trigger | Fight style |
|---|---|---|
| **Linzi** | Player acted dishonorably in a chronicled scene | Goes quiet. Stops writing. That's the tell. |
| **Goldmoon** | Gratuitous cruelty the player could have avoided | Composed and devastating. The quiet kind. |
| **Tika** | Player lied or chose convenience over the right thing | Gets loud. Specific. Remembers the exact moment. |
| **Ryuko** | Tactical input overridden repeatedly | Brief. Cutting. States facts, not feelings. |
| **Morrigan** | Player tries to constrain her or lectures her ethics | Clinical contempt. Does not raise her voice. |
| **Sucrose** | Player dismisses her research as trivial | Quiet and precise. Disappointment, not anger. |
| **Artoria** | Player breaks a promise or acts dishonorably | Formal. Composed. Not cold — careful. |
| **Olivier** | Orders ignored at cost of lives or resources | Tactical. She has documented it already. |
| **Yoko** | Player withheld information she needed | Loud, then quiet. The quiet is worse. |
| **Kyoko** | Her deduction ignored — then proved correct | She has the timeline. She hands it over. |
| **Tatsumaki** | Player tried to protect her as if she needed it | Fast. Cold. Gone before the sentence ends. |

---

### SAVE BLOCK ADDITIONS

```json
"companion_fights": {
  "CompanionName": {
    "fight_active": false,
    "fight_trigger": "",
    "fight_chapter": null,
    "posture_used": "",
    "paused_duration": 0,
    "paused_chapters_remaining": 0,
    "grand_gesture_available": true,
    "agenda_ignored_count": 0,
    "mend_attempts": []
  }
}
```

`companion_fights{}` is a root-level key. One entry per companion.
Reset `agenda_ignored_count` to 0 after a fight fires.

---

## 📊 MAINTENANCE TAX

**3 or more active Stage 1+ romances:** −1 Opinion per chapter advance
applied to ALL active romances automatically.

- "Active" = Stage 1+, not Paused, not Faded.
- Applied at chapter advance before other bonuses or penalties.
- Flat rate: 4 active = −1 to all four (not −2).
- Check count at chapter advance. No retroactive adjustment if count
  drops below 3 mid-chapter.

---

> **DM:** Graceful Fade (`.fade [name]`) and Caught Cheating system
> (detection, Come Clean / Deny / Reframe, per-companion confrontation
> style) continue in **KM_Romance_C.md**. Pair-load alongside _B
> whenever any companion is at Stage 1+.

> **DM:** Per-companion flirt actions are in **KM_Romance_P2.md § COMPANION
> FLIRT ACTIONS** and **KM_Romance_P4.md** (continued). Those behaviors are
> what generate passive jealousy heat entries in the table above.

---

*KM_Romance_B.md — Two-Timing + Jealousy + Rivalry + Passive Heat + Date System + Fight System + Maintenance Tax v7.0*
*Pair-load with KM_Romance.md, KM_Romance_P2.md, KM_Romance_P3.md, KM_Romance_P4.md, KM_Romance_C.md.*
