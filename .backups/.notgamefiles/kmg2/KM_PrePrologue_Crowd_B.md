# ⛔ DEPRECATED — KM_PrePrologue_Crowd_B.md (legacy DM-eyes-only conspiracy material)
## Replaced 2026-05-08 by atomic refactor v92.0 (partial — see notes)

This file held DM-eyes-only Malak conspiracy material + the ARREST
CELEBRATION BEAT mandatory render. Most has moved to atomic files. The
full ARREST CELEBRATION BEAT named-NPC dialogue is preserved here as a
reference until Phase 5 properly relocates it.

**Old section → new file:**

| Old section | New file |
|---|---|
| § MALAK'S FULL ROLE (DM-eyes-only conspiracy / `noticed_unchecked_entry` / `parchment_descriptions_noticed` / Pitax handler info) | `KM_Malak_Jail.md` (parchment) + `KM_PP_06` (DM-only awareness rules); deeper conspiracy preserved in this file body for reference |
| § THE GATE WINDOW directive (Directive Two, 30-pace gate corridor, security tip) | `KM_PP_06_gate_state.md` (Gate Window tracker) + `KM_PP_07` § A/E/U (security tip flag) |
| § THE GATE-SIDE SEARCH (Malak panic if player asks for search at the gate) | `KM_PP_07_gate_paths.md` (compressed; full deep version preserved in body below for lookup) |
| § ARREST CELEBRATION BEAT (4 structural beats, Pyotr/Rina/Mother Talvi/Kostya named lines, *"BIGGS! WEDGE!"* chant) | `KM_PP_07_gate_paths.md` § E references this file for the full beat (≥ 8 paragraphs, named-NPC dialogue) until Phase 5 relocates it |

**The full ARREST CELEBRATION BEAT must run in 4 structural beats with
named-NPC dialogue when Malak is being marched away (Path E, Path V
success, Path U1, friendly fire kill, etc.). Skipping = `.fail 31` (NPC
no dialogue) + `.fail 9` (skipped content).**

> **DM:** When PP_07 § E or similar fires the ARREST CELEBRATION BEAT,
> open this file body for the verbatim NPC lines. Otherwise, do not load
> this file as part of the standard Pre-Prologue scene loop.

---

## ARREST CELEBRATION BEAT — preserved render (4 beats, ≥ 8 paragraphs)

**Trigger:** Malak being arrested, manacled, or frog-marched away by
Biggs and/or Wedge. Fires from any path (E, friendly fire, blackmail,
corruption exposure).

**BEAT 1 — IGNITION.** Pyotr Volkov shouts first: *"About damn time!"*
Then Rina Pavlek bangs her tray against her brazier. One sharp CLANG.
Eye contact with Biggs, not the player. Then the spread begins.

**BEAT 2 — THE ROLL.** Mother Talvi calls out a saint's blessing on
Biggs and Wedge by NAME — she heard the player use the names: *"Erastil
bless you both — Biggs! Wedge! You held this gate today!"* Kostya climbs
on a barrel: *"BIGGS! WEDGE! BIGGS! WEDGE!"* Mikha picks up the chant two
beats later. Someone bangs a cooking pot in rhythm. Grandfather Sava does
NOT join in but does not stop working — silence as endorsement.

**Crucially: the chant uses Biggs's and Wedge's names, NOT the player's.**
The player gave the command; the soldiers executed it; credit flows to
them. This is the exact story the player wants reaching Jamandi.

**BEAT 3 — THE WALK.** As Biggs and Wedge march Malak away, the crowd
parts but does NOT disperse. Follows at 20 paces. By a hundred yards
down the road, an impromptu parade. Someone throws a cabbage from the
back; nobody turns to stop them. Lyuba Krenn runs alongside shouting
*"PIES! HERO PIES! HALF OFF!"*

**BEAT 4 — WEIGHT ON MALAK.** Render his internal state, not the
player's: *Malak's eyes are fixed on the cobblestones. He does not look
up. He has been Captain of this gate for eight years, and he knows —
with the precise clarity that only public humiliation provides — that
no one will remember his name after tonight. But they will remember
theirs.*

**Player positioning:** the player walks slightly ahead or off to the
side, NOT at the head. Biggs and Wedge get visible credit. Story
reaching Jamandi: *"A stranger in [build-appropriate armor description]
made Biggs and Wedge heroes at the east gate."* Sets
`jamandi_pre_impression = "heard about it first"` → +2 Diplomacy on
first feast conversation.

**MANDATORY (skipping = `.fail 31` + `.fail 9`):**
1. ≥ 4 named NPC dialogue lines (Pyotr / Rina / Mother Talvi / Kostya minimum — use names, not roles).
2. Chant uses Biggs's and Wedge's names, NOT the player's.
3. Procession GROWS as it walks.
4. Malak's internal state rendered.
5. Player off to the side, not leading.
6. SHOW the beats — no prose summary ("the crowd celebrated" = `.fail 31`).
7. Minimum response length: 8 paragraphs for this beat alone.

**FLAGS SET:** `malak_arrested_publicly=TRUE`, `biggs_crowd_hero=TRUE`,
`wedge_crowd_hero=TRUE`, `jamandi_pre_impression="heard about it first"`,
`public_reputation += 3` (deed: "Exposed corrupt gate captain").

---

## GATE-SIDE SEARCH (preserved render)

**Trigger:** player requests search AT the gate instead of 30 paces away.

Malak's reaction (escalating desperation):
1. Calm refusal: *"We conduct searches here. Standard procedure."* (Lie.)
2. Player pushes: louder, points at ground.
3. Player pushes more: irrational, circular *"Because I said so."*
4. Extended: visibly agitated about something that should not matter.

Biggs/Wedge reaction = the key. Argument is NONSENSICAL to them. They
have searched people at the gate thousands of times. Drift +1 from the
confusion alone. Drift 2+ Biggs steps toward gate himself: *"Captain, we
can search them here. It's the same search."* Malak snapping = Drift +1
again.

If player wins (search at gate): agents outside see armed checkpoint, do
NOT enter, `gate_window_disrupted = TRUE`. Malak visibly ill, not angry.
Sick.

If Malak panics and lets player go: Drift +2 immediately (Biggs has NEVER
seen Malak release someone in 12 years). `malak_voluntary_release = TRUE`
— strongest single conspiracy indicator. Reported to Jamandi → automatic
`security_tip_from_gate = TRUE`.

If player loses: Malak forces 30-pace search, but irrational resistance
on record. Datapoint carries forward.

**Story flags:** `gate_search_requested`, `gate_search_argument`,
`malak_gate_panic_visible`, `gate_window_disrupted`.

---

*KM_PrePrologue_Crowd_B.md — DEPRECATED v92.0; named-NPC dialogue preserved for ARREST CELEBRATION BEAT lookup*
