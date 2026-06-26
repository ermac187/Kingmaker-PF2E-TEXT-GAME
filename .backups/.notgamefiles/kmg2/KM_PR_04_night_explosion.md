# KM_PR_04_night_explosion.md — Prologue Beat 04: THE NIGHT
## Atomic scene file | ≤ 8 KB | State: PR_04_NIGHT
## FILE_KEY: KMPR04:night-explosion
## RULE_QUOTE: Guest room prep + explosion + first assassin all fire here. Encounter 1 is tutorial combat — assassin fights defensively, flees below 6 HP, NOT lethal. Player must explicitly choose to pursue past the corridor. Linzi is pressed against the far wall, non-combat Round 1.

---

> ⛔ DO NOT (1) skip the guest room prep scene — the explosion interrupts it, not replaces it
> ⛔ DO NOT (2) skip Encounter 1 (first assassin) — it is tutorial combat, not transition flavor
> ⛔ DO NOT (3) make Encounter 1 lethal — assassin fights defensively, flees below 6 HP
> ⛔ DO NOT (4) advance past the corridor without the player choosing to pursue
> ⛔ DO NOT (5) forget Linzi — she is pressed against the far wall, non-combat Round 1
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR04:night-explosion]`
Line 2: `[RULE_QUOTE: Guest room prep + explosion + first assassin all fire here. Encounter 1 is tutorial combat — assassin fights defensively, flees below 6 HP, NOT lethal. Player must explicitly choose to pursue past the corridor. Linzi is pressed against the far wall, non-combat Round 1.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `feast_complete = TRUE` (set by PR_03)
- `poison_reported`, `security_doubled`

**WRITES:**
- `guest_room_prepped = TRUE` (after player does any prep action)
- `window_unlatched = TRUE` (if player checks window and passes Perception DC 10)
- `assassin1_outcome` = `captured` / `fled` / `killed`
- `assassin1_info_extracted = TRUE` (if captured and interrogated)

**EXIT TRIGGER → PR_05_corridor_rescue:**
- Encounter 1 resolved AND player moves into the corridor
- Load `KM_PR_05_corridor_rescue.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR04:night-explosion]`
1. `[STATE READ] current_scene="prologue_feast" | phase=PR_04_NIGHT`
2. `[HP CHECK]`
3. Scene narration
4. Player menu

---

## GUEST ROOM — PREP SCENE

> *Your guest room: a bed, a writing desk, a window overlooking the dark courtyard below.*

```
What do you do before resting?
 1. Prepare spells for tomorrow
 2. Check inventory — reorganize gear
 3. Rest immediately
 4. Check the window — look at the courtyard below [Perception DC 10]
 5. Examine the room before settling [Perception DC 10]
 6. Write notes on what happened tonight
 7. Custom action
```

**Perception DC 10 (window check or room examine):** The lock on the exterior window is unlatched. `window_unlatched = TRUE` — this is how the assassin entered. No mechanical benefit; sets prior expectation.

---

## EXPLOSION — SCRIPTED CERTAIN TRIGGER

**No flat check. No random. This always fires.** The assassins were already in position before the feast started. Skipping this = `.fail 9`.

> *The explosion hits before any warning — below, close enough to shake dust from the ceiling. Dead silence. Then screaming, running feet in the corridor. Linzi, at the door:*

**Linzi:** *"[Name] — GET UP. Something exploded and there are men on the stairs—"*

> *The door slams open. He was already in the corridor when the explosion hit — driven forward with the rest. He stands between you and the window. The courtyard is lit orange below.*

---

## ENCOUNTER 1 — FIRST ASSASSIN (Tutorial Combat)

```
[GM SCENE BRIEF — Guest Room]
ENEMIES   : Assassin Rogue 1 | HP 12 | AC 15
            Daggers +5 (1d4+2 P) | Sneak Attack +1d6 if target Off-Guard
ALLIES    : Linzi (non-combat Round 1 — pressed against far wall)
LIGHTING  : Dark (courtyard fire through window — dim flicker only)
```

**Encounter intent:** Tutorial combat — deliberately easy. Establishes the threat level.

**Assassin behavior:**
- Fights defensively (Total Defense if HP ≤ 8)
- Flees toward the window if reduced below 6 HP
- Has information if captured: was hired in Restov, knows only his handler's face

**Loot:** 3 gp, dagger, leather armor.

**Linzi (Round 2 onward):** Can Inspire Courage (+1 to attack/damage) if the player asks.

**If `security_doubled = TRUE`:** A guard arrives at the corridor end by Round 2 (ally, HP 12, AC 15, Spear +4).

**Initiative:** Roll for player and assassin.

---

## IF CAPTURED — INTERROGATION OPTION

```
What do you do with the captured assassin?
 1. Interrogate him — who hired you?
    → He knows: hired in Restov via intermediary, 10 gp, no names
    → He doesn't know who the actual client is
    [assassin1_info_extracted = TRUE]
 2. Tie him and leave him — deal with it later
 3. Hand him to Linzi to watch
 4. Kill him [loses information if not already extracted]
 5. Custom action
```

---

## AFTER ENCOUNTER 1 — CORRIDOR CHOICE

> *The corridor outside is dark. Sconces out, smoke from below. Noise at the far end — at least two more people, moving with purpose.*

```
What do you do?
 1. Enter the corridor — move toward the noise
 2. Hold the doorway — defensive position, wait to see what comes
 3. Interrogate the assassin first (if captured and not yet interrogated)
 4. Check on Linzi — make sure she's all right
 5. Assess the corridor before committing [Perception DC 12 — two hostiles, positions]
 6. Call for Jamandi's guards
 7. Custom action
```

---

## EXIT — TRANSITION TO PR_05

When player moves into the corridor:
- Load `KM_PR_05_corridor_rescue.md`

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_05 (carries forward)

**Your next response after PR_04's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR05:corridor-rescue]
[RULE_QUOTE: Corridor encounter + Tartuccio rescue + ring decision all required for PR_09 rebuttal to function. Tartuccio UNKILLABLE PROTOCOL active — he is the Chapter 1 antagonist and must survive. Tartuccio stays back, offers commentary, does NOT fight front line. Ring choice menu is mandatory — no assumed default.]
```

**Binding constraints:**
- Corridor encounter is not optional flavor — runs in full
- Tartuccio rescue + ring decision are required for PR_09 rebuttal to function later
- Tartuccio UNKILLABLE PROTOCOL active — survives this beat regardless of player action
- Tartuccio stays back, comments, does NOT enter front line
- Ring choice menu is mandatory; player explicitly chooses, no DM default

---

*KM_PR_04_night_explosion.md — Prologue atomic beat 04 | v92.0*
