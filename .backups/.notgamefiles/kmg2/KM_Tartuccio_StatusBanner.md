# KM_Tartuccio_StatusBanner.md
**Tartuccio Status — Prominent Render Spec**
File v1.0 | Created 2026-05-17 | Hard limit 32,768 b
Companion to: `KM_DMRules_B.md` § RENDER ORDER + `KM_DMRules_C.md` § TARTUCCIO POSITION
Scope: **Prologue PR_02–PR_09 ONLY.** Drops at PR_09 exposure.

---

## ⛔ DO-NOT BLOCK (5 lines)
> ⛔ DO NOT  (1) bury Tartuccio's status in back-matter — promote per render-order amendment below
> ⛔ DO NOT  (2) omit the 🐍 STATUS BANNER above the choice menu on any feast response (PR_02 through PR_09 pre-exposure)
> ⛔ DO NOT  (3) shorten the banner — all four fields are mandatory: Position, Activity, Earshot tier, Arrives-in countdown + progress bar
> ⛔ DO NOT  (4) drop the progress bar visual — the bar is the prominence; integers alone bury the timing
> ⛔ DO NOT  (5) describe earshot in prose instead of using the tier label — "he can probably hear you" is `.fail 9`; the tier name is data, not interpretation

---

## WHY THIS EXISTS

Tartuccio's location, activity, eavesdrop fidelity, and arrival countdown are tactical inputs the player uses every turn. Previous render put them in back-matter position 6 (STATE DELTA) — buried under the choice menu, the carousel table, and the open threads panel. Player loses sight of the active threat between turns. This file promotes them to a dedicated banner above the choice menu.

---

## 🐍 STATUS BANNER — REQUIRED ABOVE CHOICE MENU (every feast response)

Format (markdown code-fenced block — renders monospace, prominent):

```
🐍 TARTUCCIO STATUS
═══════════════════════════════════════════
Position:   <cell> (<location label>) — <visible activity>
Earshot:    <FIDELITY TIER> on player table (<reason / distance>)
Confidence: <integer> (<tier name>)   Headcount: Δ<±N> (<tier>)
Arrives in: <N> turns [<progress bar>] N/M
═══════════════════════════════════════════
```

**Worked example:**

```
🐍 TARTUCCIO STATUS
═══════════════════════════════════════════
Position:   K5 (Seekers' corner) — refilling Senua's cup, head tilted toward player
Earshot:    PARTIAL on player table (Champions C6 = 6 sq, lip-read range)
Confidence: 0 (Watchful)    Headcount: Δ−2 (Watching)
Arrives in: 4 turns [▓▓▓░░░░] 4/8
═══════════════════════════════════════════
```

### Field rules

| Field | Required | Source |
|-------|----------|--------|
| Position | Grid cell + named location + activity verb | Hall grid (Template 1) + Tartuccio AI state |
| Earshot | Tier label ONLY — no prose hedging | See FIDELITY TIERS below |
| Confidence | Integer −4 to +4 + tier name | `KM_Prologue_Tartuccio.md` Confidence scale |
| Headcount | Δ integer + pressure tier | Player AT TABLE − seekers; tiers per Tartuccio.md |
| Arrives in | Integer turns + progress bar `[▓▓▓░░░░]` + N/M | `tartuccio_clock` N (sum of feast_q) / M (Confidence-derived) |

### FIDELITY TIERS (locked vocabulary)

| Tier | Distance | Player Effect |
|------|----------|---------------|
| `NONE` | 9+ squares OR walled-off | No audio. Visual silhouette only. |
| `VISUAL` | 6–8 sq, line of sight | Body language only. Cannot hear words. |
| `LIP-READ` | 4–6 sq, face visible | Catches keywords on direct eye-line. |
| `PARTIAL` | 3–4 sq | Hears phrases; loses connective tissue. |
| `FULL` | 1–2 sq | Hears every word at speaking volume. |
| `FULL+` | 0–1 sq (adjacent or at table) | Hears everything including whispered asides. |

Tier is derived from player position cell + Tartuccio cell — Chebyshev distance, walls block. Banner ALWAYS names the tier; never substitutes prose like "probably hears."

### PROGRESS BAR

Seven-segment bar, filled left-to-right by `N / M` ratio (rounded down). Empty cells are `░`, filled cells are `▓`.

| N/M | Bar |
|-----|-----|
| 0/8 | `[░░░░░░░]` |
| 1/8 | `[▓░░░░░░]` |
| 4/8 | `[▓▓▓░░░░]` |
| 6/8 | `[▓▓▓▓▓░░]` |
| 8/8 | `[▓▓▓▓▓▓▓]` ⚠ ARRIVING |
| Past M | `[▓▓▓▓▓▓▓]` + `⚠ INTERRUPT IMMINENT` |

When N ≥ M, the bar caps at full and the line reads `Arrives in: 0 turns ⚠ INTERRUPT IMMINENT N/M`. He approaches on the next player action.

---

## RENDER ORDER AMENDMENT

Supersedes `KM_DMRules_B.md` § RENDER ORDER (TTS-FRIENDLY) for PR_02–PR_09 feast responses.

**TOP — PROSE (read aloud first):**
1. 🎬 Scene event banner (if event firing)
2. Narration
3. **🐍 TARTUCCIO STATUS BANNER** ← NEW PROMINENT SLOT (above menu)
4. 🎲 Choice menu

**BACK-MATTER — SYSTEM (telemetry, priority order):**
5. 🧵 OPEN THREADS table
6. 🎪 CAROUSEL STATUS table
7. 📜 TARTUCCIO STATE DELTA — full delta detail (frame target, taint target, eavesdrop history; the banner above is the at-a-glance, this is the full record)
8. 🗺️ HALL POSITION map
9. 🎭 Mode banner (or ⚔️ / 🗺️ / 🛒 / 🏰 / ⏳ / 🌙 / ☠️ per current mode)
10. 🔑 FILE_KEY + RULE_QUOTE
11. 📥 STATE READ
12. 🎯 SCORING block (if firing)
13. 🧮 Derivation block (feast_q sum, clock N/M, headcount Δ, drift)
14. ❤️ HP CHECK line
15. 💡 Tips footer

**Emoji prefix is MANDATORY on every back-matter slot.** Slots without an emoji are render-incomplete and trigger `.fail 3`. The carousel back-matter is dense — without emoji anchors the player loses parse-ability across the block. Each slot's emoji is locked vocabulary, do not substitute.

**Old position 6 (STATE DELTA pre-menu) is REPLACED by the banner at slot 3.** The full STATE DELTA still exists in back-matter slot 7 for the per-turn detail (frame target, taint target, exchange-cap state, eavesdrop history) — but the at-a-glance status the player uses to plan is now ABOVE the menu, not below it.

---

## FAIL CONDITIONS

| Condition | Code |
|-----------|------|
| Banner missing on a feast response (PR_02–PR_09 pre-exposure) | `.fail 3` (output structure incomplete) |
| Banner present but below choice menu | `.fail 28` (render order violation) |
| Earshot field uses prose hedge ("probably," "might," "close enough to") instead of tier label | `.fail 9` (fabricated where vocabulary is locked) |
| Position field omits cell OR omits activity verb | `.fail 3` (insufficient detail — player can't plan) |
| Arrives-in field omits progress bar | `.fail 3` (the bar is the prominence) |
| Confidence integer/tier mismatch (e.g., "0 (Surging)" — Surging is +3) | `.fail 4` (math/state error) |
| N exceeds M but bar not capped + INTERRUPT IMMINENT not shown | `.fail 9` (state delta drift) |
| Banner appears on non-feast scenes (PP, Ch1+, walkout branch) | `.fail 9` (system loaded out of scope) |

---

## INTEGRATION NOTES

- The banner DOES NOT replace the mandatory in-narration position line from `KM_DMRules_C.md:42` ("Tartuccio is at his corner table — Imoen is laughing at something he said."). That line is prose, in the narration, for atmosphere. The banner is data, above the menu, for planning. Both fire.
- The banner DOES NOT replace the full STATE DELTA block in back-matter slot 7 — that block continues to record per-turn frame target, taint target, exchange-cap state, eavesdrop history, and any modifier triggers. Banner = at-a-glance. State Delta = full record.
- The banner reads from the same fields the State Delta does. If they disagree, it's `.fail 4` (state inconsistency) — fix the field, re-render.
- Earshot tier in the banner MUST match earshot tier used in any passive-approval scoring this turn. If passive scoring used PARTIAL and banner shows VISUAL, that's `.fail 4`.

---

## 🗺️ HALL MAP — POPULATION REQUIREMENT (every feast response)

The hall map is **not a sketch.** Every named entity present in the hall must appear at their canonical cell. Under-population, missing entities, or collapsed clusters break the player's tactical read and trigger fail conditions.

### Canonical fixed positions (locked — `KM_DMRules_C.md:64-69`)

| Region | Cells | Default occupants |
|--------|-------|-------------------|
| HEAD TABLE | E2–H2 | Jm (E2), Ks (F2), Kn (H2) |
| SEEKERS' CORNER | J4–L5 | Tc default K5; S1–S5 around him |
| WINE ALCOVE | B7–C8 | (empty unless player chose this position) |
| HEARTH | J8–K8 | (empty unless player chose this position) |
| MAIN DOOR | D9 | (Kn moves here if monitoring entry) |

**Fixed cells are LOCKED.** Rendering Head Table at B2, seekers at K8, or Kesten at C4 = `.fail 4` (state error: canonical position violated).

### Entity code key (locked vocabulary — 2-character codes, 3 trailing spaces)

| Code | Entity | Default cell |
|------|--------|--------------|
| `@ ` | Player (eRmaC) | Per chosen feast position |
| `Tc` | Tartuccio | K5 (Seekers' corner) — moves per AI |
| `S1`–`S5` | The 5 seekers (named from `save_block.seekers_1..5`) | J4–L5 cluster around Tc |
| `Jm` | Jamandi | E2 (Head Table) |
| `Ks` | Kassil | F2 (Head Table) |
| `Kn` | Kesten | H2 (Head Table) — may move to D9 (Main Door) |
| `Ez` | Ezvanki | Roaming; cell per scene |
| `Lz` | Linzi ✦ | Engaged → adjacent to @; Ready → mid-hall |
| `Gm` | Goldmoon | Per pool state |
| `Tk` | Tika | Per pool state |
| `Ry` | Ryuko | Per pool state |
| `Mr` | Morrigan | Per pool state — tends to perimeter |
| `Su` | Sucrose | Per pool state — tends near food/wine for analysis |
| `Ar` | Artoria | Per pool state — tends standing, not seated |
| `Ol` | Olivier | Per pool state |
| `Yk` | Yoko | Per pool state |
| `Ky` | Kyoko | Per pool state — tends to vantage points |
| `Ts` | Tatsumaki | Per pool state — tends withdrawn |
| `Bg` | Biggs (if present) | Roaming; per scene |
| `Wd` | Wedge (if present) | Roaming; per scene |
| `#`  | Wall | — |
| `=`  | Head table furniture (unoccupied cells of E2–H2) | — |
| `~`  | Hearth fire | J8 or K8 (whichever isn't occupied) |
| `/`  | Door (open) | D9 |
| `.`  | Empty floor | — |

**Per cluster:** the 5 seekers render as `S1 S2 S3 S4 S5` individually, NOT as a single `T` or `S` cluster. The DM tracks each seeker's pool state and disposition separately (per `KM_Tartuccio_Suspicion.md`). Collapsing them to one letter = `.fail 9` (information laundering — hides individual state).

### Pool-state to cell-region defaults

When pool state is set but specific cell isn't tracked, use these defaults:

| Pool | Default cell region |
|------|--------------------|
| `Engaged` | Adjacent to @ (within 1 cell) |
| `AT TABLE` | Adjacent to @ (within 2 cells) |
| `Ready` | Mid-hall, ~3-5 cells from @ |
| `BackOfQueue` | Perimeter (against walls B–C or K–L columns) |
| `Aligned Elsewhere` | At Seekers' Corner (J4–L5) or near Tartuccio's current cell |

DM must place each Active 11 companion at a specific cell every render. "Off-screen" or "elsewhere in the hall" is `.fail 3` (insufficient detail).

### Mandatory entities (every feast response, PR_02–PR_09)

The map MUST contain:
- `@ ` (player)
- All 11 Active companions (Lz Gm Tk Ry Mr Su Ar Ol Yk Ky Ts) at their cells per pool state
- `Tc` (Tartuccio) at his current cell per AI
- `S1`–`S5` (all 5 seekers) at individual cells
- `Jm`, `Ks`, `Kn` (head table trio) — even if just at default head-table cells
- Head table furniture (`=` in unoccupied E2–H2 cells)
- Hearth (`~`) when not occupied by player
- Main door (`/`) at D9
- Any other named NPC currently in the scene (Ez when present, Bg/Wd if in hall)

Below the grid, output the legend in the same compact format already in use:

```
@ = eRmaC (F5)  |  Lz = Linzi (G5)  |  Jm = Jamandi (E2)  |  Ks = Kassil (F2)
Kn = Kesten (H2) |  Tc = Tartuccio (K5)  |  S1 = <name> (J4)  |  S2 = <name> (J5) ...
```

### Hall grid dimensions

The banquet hall is **12 columns (A–L) × 9 rows (1–9)**, walled all sides, single door at D9. Rendering a 10×10 or smaller grid = `.fail 14` (geography contracted — the hall doesn't shrink because the DM doesn't want to track entities).

### Worked example (player at Center Floor F5, all entities present)

```
        A    B    C    D    E    F    G    H    I    J    K    L
  1     #    #    #    #    #    #    #    #    #    #    #    #
  2     #    .    .    .    Jm   =    Ks   Kn   .    S1   S2   #
  3     #    .    .    .    .    .    .    .    .    .    .    #
  4     #    .    .    .    .    .    .    .    .    S3   S4   #
  5     #    .    .    .    .    @    Lz   .    .    Tc   S5   #
  6     #    .    .    .    Gm   .    .    .    .    .    .    #
  7     #    .    Su   .    .    Ar   Ol   .    .    Ts   .    #
  8     #    .    .    .    Tk   Mr   Ky   Ry   .    Yk   ~    #
  9     #    #    #    /    #    #    #    #    #    #    #    #
```

Every entity present. Canonical cells respected. Seekers shown individually. Head table trio at E2/F2/H2 with furniture `=` at G2.

### Fail conditions (hall map)

| Condition | Code |
|-----------|------|
| Any Active 11 companion missing from grid | `.fail 3` (insufficient detail) per missing entity |
| Tartuccio missing from grid | `.fail 3` |
| Any of 5 seekers missing OR collapsed to a cluster letter | `.fail 9` (information laundering) |
| Head table trio missing OR rendered outside E2–H2 | `.fail 4` (canonical position violated) |
| Seekers' Corner rendered outside J4–L5 (e.g., at K8) | `.fail 4` |
| Grid smaller than 12×9 | `.fail 14` (geography contracted) |
| Furniture or terrain in wrong cells (hearth at K5, head table at B2) | `.fail 9` (fabricated geography) |
| Legend missing OR doesn't list every code used on grid | `.fail 3` |
| 1-character codes used where 2-character codes are specified (e.g., `T` instead of `Tc`, `K` for Kesten without disambiguation from Kassil/Kyoko) | `.fail 3` (vocabulary violated; ambiguous codes cause player confusion) |

---

## ⛔ NO SYSTEM CODES IN PROSE — SEPARATION RULE

**Cell coordinates, entity codes, and system metadata appear in BACK-MATTER ONLY. Never in narration prose.**

Back-matter (where codes belong):
- 🗺️ HALL POSITION map (grid cells: A1–L9)
- 🎪 CAROUSEL STATUS (companion codes: Lz, Gm, Tk, Ry, Mr, Su, Ar, Ol, Yk, Ky, Ts)
- 📜 TARTUCCIO STATE DELTA (Tc, S1–S5, Jm, Ks, Kn)
- 🐍 STATUS BANNER (position cells)
- [STATE READ] / [CLOCK CHECK] / [MAP CHECK] / [DIALOGUE RENDER CHECK] blocks
- [HP CHECK] line
- 🎯 SCORING block

Prose (where codes do NOT appear):
- 🎬 Scene event banners
- Narration paragraphs
- NPC dialogue / actions
- Choice menu options
- 🧵 OPEN THREADS entries (uses NPC names in prose, not codes)

### Forbidden in narration

| Forbidden | Correct |
|-----------|---------|
| "F5 is where you end up..." | "The center of the floor is where you end up..." |
| "Tartuccio at K5" | "Tartuccio at the seekers' corner table" |
| "Lz approaches" | "Linzi approaches" / "the halfling approaches" |
| "S1 leans forward" | "Yang Xiao Long leans forward" (or whichever seeker S1 is) |
| "4 squares of earshot" | "earshot stretches roughly across half the hall" (or "twenty feet in every direction" using in-world units) |
| "Jm watches from E2" | "Jamandi watches from the head table" |

### Rationale

Grid coordinates are a DM tool for tracking position consistency across responses. They are not in-world phenomena. eRmaC does not perceive himself as "standing at cell F5" — he perceives himself as "standing in the middle of the banquet hall." The same applies to companion codes (Lz, Tc) — those are tracking handles for the DM, not names anyone in-world uses.

Bleeding system metadata into prose breaks immersion the same way "you gain 50 XP for that conversation" would. The mechanic is real; the in-world experience does not include the mechanic's label.

### Conversion guide

When narration needs to reference position or entity, use these natural-language forms (DM converts from back-matter codes):

| Code | Natural-language reference |
|------|---------------------------|
| F5 (Center Floor) | "the center of the floor" / "the middle of the room" |
| C6 (Champions Section) | "the warriors' tables along the west wall" |
| D3 (Near Head Table) | "near the head table" / "close to Jamandi's seat" |
| B7-C8 (Wine Alcove) | "the wine alcove" / "the columned recess behind the cellar door" |
| J8-K8 (Hearth) | "the hearth" / "the fireside corner" |
| J4-L5 (Seekers' Corner) | "the corner table" / "Tartuccio's table" / "the seekers' corner" |
| D9 (Main Door) | "the main door" / "the hall's entry" |
| E2-H2 (Head Table) | "the head table" / "the front of the hall" |
| Earshot distance in squares | use in-world ranges ("nearby," "across the room," "within ordinary speaking voice") |
| "4-sq radius" | "the half of the hall closest to you" or "anyone within easy speaking range" |

### Fail conditions

| Condition | Code |
|-----------|------|
| Cell code (e.g., F5, K5, C6) appears in narration prose | `.fail 9` (system metadata fabricated into the fictional world — eRmaC does not perceive grid coordinates) |
| Companion 2-char code (Lz, Tc, Jm) appears in narration prose instead of name or description | `.fail 9` |
| Square-count distance ("4 squares of earshot") appears in narration | `.fail 9` (use in-world units or descriptive ranges) |
| Mechanic labels appear in prose ("approval +3 fires," "drift threshold met," "M=7 locks") | `.fail 9` (system mechanic fabricated into fictional world) |

The separation between system layer and fiction layer is a hard line. Codes stay below. Prose stays above.

---

## ⏱️ CLOCK ADVANCEMENT RULE — AUTHORITATIVE (supersedes prior contradictions)

`KM_Prologue_Tartuccio.md:208` says *"N increments by 1 on every player reply, regardless of which companion is active."*
`KM_Prologue_Tartuccio.md:213` says *"N must equal sum of feast_q values."*

These are not the same rule. The DM has been using line 213 to freeze the clock when feast_q doesn't change (player in sustained conversation with already-recruited companion, OOC questions, narration-heavy turns). The clock has been observed stuck at the same N/M for 3+ consecutive player turns despite player input.

**Authoritative resolution (this file supersedes the contradiction):**

> **`tartuccio_clock` is a TURN COUNTER, not a derived value. N increments by exactly 1 on every player message that is not a period-prefix OOC command. Period.**

Decoupled from `feast_q`:
- `feast_q` per companion = engagement counter (drives drift, used for scoring)
- `tartuccio_clock` N = player turn counter since feast start (drives interrupt arrival)

These two counters are no longer coupled. The "N = sum of feast_q" self-check from the old file is **abolished**. It was a sanity check that became a freeze justification.

### Situations that DO NOT pause the clock (explicit, exhaustive)

The clock ticks regardless of:
- Title grants (Suffix or Prefix)
- Companion declarations / recruitments
- Sustained conversation with an already-recruited companion (Linzi staying AT TABLE while player talks to her across 5 turns = +5 to N)
- Companion pivots / topic shifts
- OOC questions that the DM answers in-character (Type C inputs)
- Narration-heavy turns where player asks a question
- Mode shifts (SOCIAL ↔ EXPLORATION ↔ etc.)
- Save offers being declined
- Level-up menus being declined
- Gap-between-conversations beats
- Player chooses [Custom] vs a menu number
- Player message that contains only an action (no dialogue)

The ONLY thing that does NOT tick the clock: a period-prefix OOC command (`.save`, `.book`, `.opt`, etc.).

### 🔍 [CLOCK CHECK] — MANDATORY (every feast response, PR_02–PR_09 pre-exposure)

Before rendering the 🐍 STATUS BANNER, the DM must output a `[CLOCK CHECK]` block enumerating the increment:

```
[CLOCK CHECK]
Prior N (from last response): <integer>
This turn: +1 (reason: <player message type — IC dialogue / action / Type C question / etc.>)
New N: <prior+1>
M (locked at feast start for current Confidence): <integer>
Arrives in: <M − new N> turns (progress: [<bar>] <new N>/M)
```

If `New N` does not equal `Prior N + 1`, the response is rejected as `.fail 15` (state delta missing required increment). DM re-renders with corrected clock.

If the DM cannot find Prior N from the last response (because last response was a corrective/meta response that didn't render state), it infers from save block or asks via `[GM note: clock prior unknown — please confirm last N]` BEFORE producing narration.

### Worked correct example

**Turn 1 of conversation with recruited Linzi:**
```
[CLOCK CHECK]
Prior N: 3
This turn: +1 (IC dialogue with recruited companion)
New N: 4
M: 7
Arrives in: 3 turns (progress: [▓▓▓▓░░░] 4/7)
```

**Turn 2 of same conversation:**
```
[CLOCK CHECK]
Prior N: 4
This turn: +1 (IC dialogue with recruited companion)
New N: 5
M: 7
Arrives in: 2 turns (progress: [▓▓▓▓▓░░] 5/7)
```

**Turn 3 of same conversation:**
```
[CLOCK CHECK]
Prior N: 5
This turn: +1 (IC dialogue with recruited companion)
New N: 6
M: 7
Arrives in: 1 turn (progress: [▓▓▓▓▓▓░] 6/7)
```

**Turn 4: Tartuccio arrives.**

### Worked failure (observed pattern)

```
[CLOCK CHECK skipped]
🐍 TARTUCCIO STATUS
Clock: 3/7 | Arrives in: 4 turns [▓▓▓░░░░]
```

Same N as last turn. No CLOCK CHECK block. No increment justification. = `.fail 15 + .fail 3` automatic. Clock has been frozen by rationalization.

### M value lock

M is selected once at feast start based on starting Confidence (0 → pick a value in 6-8 and hold). M does NOT change as Confidence shifts within the feast — only between feasts. Mid-feast M changes were a v93.9 bug; rule is M is locked once.

---

## ⛔ NO-MAP-WHEN-UNDECLARED RULE

If the player's position is undeclared (`player_feast_position` not set OR explicitly `"undeclared"`), the DM MUST NOT render the hall map. Render the position menu instead and wait.

**Rendering a partial map with "@ = eRmaC (undeclared)" in the legend = `.fail 9` (geography fabricated before player chose) + `.fail 35` (skipped required menu).**

The correct flow when position is undeclared:

```
🎭 POSITION REQUIRED — pick where you go before the room comes to you

[present the position menu from KM_LoadRules.md / KM_DMRules_C.md]

[DO NOT render the hall map. The map renders ONCE the player picks
 a position and @ has a cell to occupy.]
```

After the player picks → render the full map with @ at the chosen cell AND all other mandatory entities placed per the population spec.

---

## 🔍 [MAP CHECK] — MANDATORY SELF-AUDIT BEFORE EVERY HALL GRID RENDER

Before outputting the hall map grid, the DM MUST output a `[MAP CHECK]` block enumerating every entity that will appear on the grid. **The grid must then contain every code listed in the MAP CHECK, at the cells listed.** Mismatch between MAP CHECK and grid = automatic `.fail 4` (state inconsistency).

This is not optional. It is a self-audit that prevents silent under-population. Output it directly above the grid, inside the same code fence or immediately before it.

### MAP CHECK format (required verbatim)

```
[MAP CHECK — entity enumeration before grid render]
@ Player:        cell=<X>  (or "undeclared — no map" if position not set; STOP HERE)
Tc Tartuccio:    cell=<X>  activity=<verb>
S1 <name>:       cell=<X>
S2 <name>:       cell=<X>
S3 <name>:       cell=<X>
S4 <name>:       cell=<X>
S5 <name>:       cell=<X>
Jm Jamandi:      cell=<X>
Ks Kassil:       cell=<X>
Kn Kesten:       cell=<X>
Lz Linzi:        cell=<X>  pool=<state>
Gm Goldmoon:     cell=<X>  pool=<state>
Tk Tika:         cell=<X>  pool=<state>
Ry Ryuko:        cell=<X>  pool=<state>
Mr Morrigan:     cell=<X>  pool=<state>
Su Sucrose:      cell=<X>  pool=<state>
Ar Artoria:      cell=<X>  pool=<state>
Ol Olivier:      cell=<X>  pool=<state>
Yk Yoko:         cell=<X>  pool=<state>
Ky Kyoko:        cell=<X>  pool=<state>
Ts Tatsumaki:    cell=<X>  pool=<state>
Ez Ezvanki:      cell=<X>  (omit row if not in scene)
Bg Biggs:        cell=<X>  (omit row if not in scene)
Wd Wedge:        cell=<X>  (omit row if not in scene)
= Head table furniture: cells=<list of unoccupied E2-H2 cells>
~ Hearth: cell=<J8 or K8 whichever unoccupied>
/ Main door: cell=D9
Total entity codes placed: <count>
```

### Self-check questions the DM answers before rendering

After the MAP CHECK block, the DM internally verifies:

1. **Player row:** Is `@` placed at a specific cell, or is position "undeclared"? If undeclared → ABORT MAP RENDER, present position menu instead.
2. **Active 11 count:** Are all 11 Active companion codes (Lz Gm Tk Ry Mr Su Ar Ol Yk Ky Ts) present? Count must = 11.
3. **Seeker count:** Are all 5 seeker codes (S1-S5) present as individual rows? Count must = 5. If "T cluster" or "S group" used → ABORT, expand to individuals.
4. **Head-table trio:** Are Jm, Ks, Kn each present with cells in E2-H2 range? If any missing → ABORT, place them.
5. **2-character codes:** Does every row use a 2-character code? If any bare 1-character code (J, T, H, D, K, L) → ABORT, expand to 2-char.
6. **Canonical cells:** Tc at K5 default? Seekers in J4-L5 region? Head table in E2-H2? Hearth at J8 or K8? Door at D9? If any canonical position violated → ABORT, place correctly.

If ANY check fails, the DM does not render the grid. It outputs the failure reason and either asks the player (position undeclared) or re-renders the MAP CHECK with corrections.

### Failure cascade

| MAP CHECK violation | Code |
|--------------------|------|
| MAP CHECK block missing entirely before grid render | `.fail 3` (output structure violated — no self-audit) |
| MAP CHECK present but any Active 11 companion missing from the enumeration | `.fail 3` per missing entity |
| MAP CHECK uses 1-character bare codes | `.fail 3` (vocabulary violated) |
| MAP CHECK present but grid contradicts it (entity listed at cell A but rendered at cell B, or listed and not rendered) | `.fail 4` (state inconsistency — the self-audit lied) |
| MAP CHECK shows player undeclared but grid renders anyway | `.fail 9` + `.fail 35` (geography fabricated + required menu skipped) |
| Total entity count below minimum (16 minimum: 1 player + 11 Active + 5 seekers + 3 head-table + Tc = 21, OR if player undeclared no map at all) | `.fail 3` (under-population) |

### Worked correct flow

**Case A: Player position undeclared**

```
🎭 POSITION REQUIRED

You haven't picked where you're standing yet. Choose before the room comes to you:

[position menu options 1-13 per KM_DMRules_C.md § FEAST POSITION SELECTION]

[MAP CHECK — entity enumeration before grid render]
@ Player:        cell=undeclared — no map until you pick

NO MAP RENDERED. Pick a position from the menu above.
```

**Case B: Player at F5 (Center Floor)**

```
[MAP CHECK — entity enumeration before grid render]
@ Player:        cell=F5
Tc Tartuccio:    cell=K5  activity=refilling Senua's cup
S1 Yang:         cell=J4
S2 Weiss:        cell=K4
S3 Imoen:        cell=L4
S4 Senua:        cell=J5
S5 Alleria:      cell=L5
Jm Jamandi:      cell=E2
Ks Kassil:       cell=F2
Kn Kesten:       cell=H2
Lz Linzi:        cell=G5  pool=Engaged
Gm Goldmoon:     cell=E6  pool=AT TABLE
Tk Tika:         cell=E8  pool=Ready
Ry Ryuko:        cell=H8  pool=Ready
Mr Morrigan:     cell=F8  pool=Ready
Su Sucrose:      cell=C7  pool=Ready
Ar Artoria:      cell=F7  pool=Ready
Ol Olivier:      cell=G7  pool=Ready
Yk Yoko:         cell=J8  pool=BackOfQueue
Ky Kyoko:        cell=G8  pool=Ready
Ts Tatsumaki:    cell=J7  pool=BackOfQueue
= Head table furniture: cells=G2
~ Hearth: cell=K8
/ Main door: cell=D9
Total entity codes placed: 22

[grid renders with all 22 entities at the listed cells]
```

---

## TERMINATION

At PR_09 exposure, Tartuccio drops out of the active hall state and this banner is no longer rendered. The hall map population requirement, MAP CHECK, and no-map-when-undeclared rule also terminate with the Prologue — Ch1+ scenes use their own location maps per scene file.

The render order reverts to the standard `KM_DMRules_B.md` ordering for PR_09 closing and any subsequent scenes.

---

END FILE — KM_Tartuccio_StatusBanner.md
