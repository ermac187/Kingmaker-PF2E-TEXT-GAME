# KINGMAKER — MAP TEMPLATES (VERBATIM, ASCII ONLY)
## KM_MapTemplates.md | Referenced by: KM_Commands_Maps.md, KM_DMRules.md, KM_PrePrologue.md

> **⛔ DM: COPY ONE OF THE 3 TEMPLATES BELOW EXACTLY. Do NOT generate a map
> from memory. Do NOT draw a rectangle with names and distances and call it
> a map. Fill in the symbols for the scene — do not change the structure.**
>
> **A map MUST have:**
> 1. Column letter headers (A B C D ...)
> 2. Row number headers (1 2 3 ...)
> 3. Grid cells (5-col wide for combat, 6-char wide for hex)
> 4. Symbol key at the bottom
>
> **Any output missing any of those 4 = NOT A MAP = `.fail 14`. Redraw.**

---

## ⛔ ASCII-ONLY RULE (NEW — read first, applies to ALL templates)

All maps use ASCII characters ONLY. No UTF-8 box-drawing. The DM previously
"translated" `║` to `||`, `█` to `■■`, `╔` to `+`, etc. — every translation
broke alignment. Fix: use only characters the DM can reliably reproduce.

**Allowed ASCII map characters:**
  `# . @ T E1 E2 E3 c : % - / + | * ! ? o ~ & ^ =`
  letters A–Z (column headers, companion initials, hex codes)
  digits 0–9 (row labels)
  spaces

**Banned characters in map output (any use = `.fail 14`):**
  `║ ═ ╔ ╗ ╚ ╝ ╠ ╣ █ · ░ ▓ ─ ┌ ┐ └ ┘ │ ★ ⁎ ▒ ♣ ● ✦ ∿ ≈`
  any UTF-8 box-drawing or geometric shape character
  any `[ ]` per-cell bracket wrappers (combat grid only — hex grid uses brackets)

---

## ⛔ AUTO-TRIGGERS — COMBAT (Template 1 grid required in same response)

If your response contains ANY of these, a full Template 1 combat grid MUST appear:

- "COMBAT INITIATED" / "Combat begins" / "Roll initiative"
- ".map combat" command from player
- An enemy has just moved, attacked, or appeared on the field
- Player typed an attack action that just resolved
- A trap, ambush, or surprise round triggered
- Start of any new combat round

Writing "COMBAT INITIATED" without an accompanying Template 1 grid = **instant `.fail 14`**.

---

## ⛔ AUTO-TRIGGERS — SCENE CHANGE (every new scene gets a map)

Whenever `current_scene` OR `current_location` changes, the DM MUST output a
map in the SAME response that introduces the new scene. No exceptions for
"intimate" or "narrative" scenes.

**Examples that fire this trigger:**
  - "Opening Scene" → first map of the game
  - "The Trip to the Manor" → travel/road map
  - "The Manor Banquet" → indoor scene map
  - Walking from one room to another inside the same building
  - Entering ANY new building, road, hex, or named area

**Template selection by scene type:**
  - Multi-room building (Manor, Inn, Dungeon level): Template 2 scene map
  - Single room or chamber: Template 1 grid (no enemies — walls + @ only)
  - Narrow corridor / alley: Template 1 sized 3–5 wide × 8–12 long
  - Overland travel / wilderness: Template 3 hex map
  - Combat scene: Template 1 with all enemies placed

**Map persistence:** If `current_location` is unchanged across responses (same
room, same NPC), the map need NOT redraw every response. It fires:
  1. The FIRST response in the new location, AND
  2. Any later response where positions, exits, or terrain changed, AND
  3. Whenever the player types `.map`.

**Missing map on scene/location change = `.fail 14`.**

---

## ❌ BANNED OUTPUT — DO NOT EVER DRAW THIS (instant `.fail 14`)

A label box is not a map. The DM has produced this in the past:

```
+----------------------+
|  ALLEY — DEAD END    |
|  WALL                |
|      [THIEF]         |   <- 20 ft from you
|      [eRmaC]         |
|      crowd           |
+----------------------+
Distance: 20 ft between combatants
```

**What is wrong:**
- No column letters, no row numbers
- No grid cells
- "WALL" written as text instead of `#` rows
- `[THIEF]` `[eRmaC]` as labels instead of `T` `@` placed on coordinate cells
- Distance asserted as text instead of derived from cell counting
- Symbol key missing

**Redraw using Template 1 below.**

---

## ⛔ TEMPLATE 1 — COMBAT GRID (ASCII)

Copy exactly. Replace placeholders with the actual scene. Wrap output in a
```` ``` ```` code fence so monospace renders correctly.

```
[LOCATION NAME]                                    Each square = 5 ft
Round: [N] | Initiative: [order by name]

       A    B    C    D    E    F    G    H    I    J
  1    #    #    #    #    #    #    #    #    #    #
  2    #    .    .    .    .    .    .    .    .    #
  3    #    .    .    .    .    :    :    .    .    #
  4    #    .    .    .    .    .    .    -    -    #
  5    #    .    @    .    .    .    .    .    .    #
  6    #    .    .    .    .    .    .    E1   .    #
  7    #    .    .    .    .    %    %    %    .    #
  8    #    #    #    #    /    #    #    #    #    #

ID    Name           HP       AC    Status         Distance from @
@     [You]          [X/Y]    [X]   -              -
E1    [Enemy Name]   [X/Y]    [X]   [status]       [X] ft ([coord])

TERRAIN: # = Wall   . = Open floor   : = Rubble (difficult)
         % = Mud (difficult)   - = Low wall (half cover)
         / = Door   c = Crowd (blocks exit, not impassable)
```

**Grid rules:** Map dimensions match the PHYSICAL scene. Hard maximum =
15 cols × 15 rows (cols A–O, rows 1–15). No minimum — shrink to fit.
Every creature visible must be placed on a cell. @ = player. E1/E2/E3 =
enemies numbered by initiative. Companions use first letter of name.

⛔ **CELL FORMAT LOCK.** Each cell is EXACTLY ONE character followed by 4
spaces. Two-char enemy IDs (`E1`, `E2`) take 3 trailing spaces instead of 4.

⛔ **NO MULTI-CHARACTER SYMBOLS.** A wall is `#` — one character. Not `##`.
Not `###`. Walls do NOT "look thicker" by repetition. Visual width comes
from the 4 trailing spaces between cells.

⛔ **NO PER-CELL BRACKETS.** Combat grid cells are bare. No `[#]`. No
`[ . ]`. No `[T]`. Hex grid (Template 3) uses brackets — combat grid does NOT.

⛔ **UNIFORM CELL WIDTH.** Every cell occupies exactly 5 columns of monospace
text. If two cells in the same row have different widths, the grid is broken.

⛔ **NO BOX BORDERS.** The combat grid has NO outer `+---+` border, NO `|`
side walls, NO `===` lines. Walls inside the grid use `#` cells. The map sits
inside a markdown code fence — that provides the visual frame.

  ✓ CORRECT:    `  3    #    .    T    .    #`
  ✓ CORRECT:    `  6    #    .    .    E1   .    #`  (E1 = 2 chars + 3 spaces)
  ✗ BANNED:     `3 [##] [ . ] [ T ] [ . ] [##]`     (per-cell brackets)
  ✗ BANNED:     `  3    ##   .    T    .    ##`     (doubled walls)
  ✗ BANNED:     `  3    ###  .    T    .    ##`     (mixed-width walls)
  ✗ BANNED:     `║  3    █    ·    T    ·    █  ║`  (UTF-8 box-drawing)
  ✗ BANNED:     anything with variable cell widths in the same row

Any banned format = `.fail 14`. Redraw using the exact ASCII format above.

⛔ **SCENE-SHAPE RULE.** Before drawing, ask: what shape is this place IRL?
  - Narrow corridor / alley / hallway:  3–5 wide × 8–12 long
  - Small room (cell, study, shop):     6–8 wide × 6–8 long
  - Standard room (inn hall, guard):    10 wide × 8 long
  - Large chamber (throne foyer):       12 wide × 10 long
  - Open battle (clearing, plaza):      14 wide × 10–12 long
  - Set-piece maximum (siege, ritual):  15 × 15  ← HARD CAP

A 14-wide alley = `.fail 9` (geography fabricated). When a scene file
specifies dimensions (e.g. `Grid: cols A–E, rows 1–9`), those OVERRIDE
this guidance.

**Two-digit row labels (rows 10–15):** use one less leading space.
`  10   #    #` (NOT `  10    #    #`). Same for 11–15.

**Starting positions:** Place party per `combat_formation` preset
(KM_PartySystem.md). Shield Wall = tanks front, casters 15 ft back. Skirmish
Line = 10 ft apart. Wedge = player point. Defensive Ring = casters center.
Ambush = two groups flanking. Custom = per `custom_positions`. If surprised,
scatter randomly within 20 ft.

---

## ⛔ TEMPLATE 1 — WORKED EXAMPLE: ALLEY DEAD END

This is the Pre-Prologue tutorial map. Copy as a reference for narrow scenes.

```
ALLEY — DEAD END                                   Each square = 5 ft
Round: 1 | Initiative: Thief -> eRmaC

       A    B    C    D    E
  1    #    #    #    #    #
  2    #    .    .    .    #
  3    #    .    T    .    #
  4    #    .    .    .    #
  5    #    .    .    .    #
  6    #    .    .    .    #
  7    #    .    @    .    #
  8    #    .    .    .    #
  9    #    c    c    c    #

ID    Name           HP       AC    Status         Distance from @
@     eRmaC          [X/Y]    [X]   -              -
T     Thief          [X/Y]    [X]   -              20 ft (C3)

TERRAIN: # = Wall   . = Open floor   c = Crowd (blocks exit)
EXITS:   South (row 9) blocked by crowd
```

Distance counting: @ at C7, T at C3. C7 → C6 → C5 → C4 → C3 = 4 cells = 20 ft.

---

## ⛔ TEMPLATE 2 — SCENE MAP (ASCII, exploration / indoor)

Copy exactly. Fill in room names and connections.

```
[LOCATION NAME] — [Sublocation]                            [@] = You

  +-------------------+      +-------------------+      +-------------------+
  |   [ROOM NAME]     |      |   [ROOM NAME]  *  |      |  [ROOM NAME]      |
  |   [status]        |------|   [status]        |------|  [status]         |
  |  [1-line detail]  |      |  [1-line detail]  |      |  [1-line detail]  |
  +---------+---------+      +---------+---------+      +---------+---------+
            |                          |                          |
  +---------+--------------------------+--------------------------+---------+
  |                       [CORRIDOR / HUB NAME]                              |
  |    !       !       !       [notes, DCs, hazards]                         |
  +---------+----------------------------------------+----------------------+
            |                                        |
  +---------+---------+    +---------------+   +-----+----------------------+
  |  [ROOM NAME]      |    | [ROOM NAME]   |   |     [ROOM NAME]            |
  |  [!] [status]     |----|  [status]     |   |     [@current]             |
  | [1-line detail]   |    | [detail]      |   |   [1-line detail]          |
  +-------------------+    +---------------+   +----------------------------+

[@]=You  [!]=Active event  *=Loot  !=Trap  [cleared]=Defeated  [locked]=DC
```

**Scene map rules:**
- Box corners use `+` only. Sides use `-` (top/bottom) and `|` (left/right).
- Room boxes are 21 chars wide by default; adjust per room name length.
- Connectors between rooms use `------` (horizontal) or `|` + spacing (vertical).
- No UTF-8 box-drawing. No `┌` `┐` `└` `┘` `─` `│` characters.

---

## ⛔ TEMPLATE 3 — HEX WORLD MAP (ASCII)

Copy exactly. Fill in hex contents per KM_Map.md. Hex cells DO use brackets
(unlike combat grid) because all hex codes are exactly 4 chars internal.

```
THE STOLEN LANDS — Hex Map
Discovered: [X] hexes | Claimed: [X] hexes | Season: [X] | Day: [X]

         A      B      C      D      E      F      G      H      I      J
  1    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  2    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  3    [Rst ][ ?  ][OTP*][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  4    [ ?  ][ ?  ][ ^  ][ &  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  5    [ ?  ][ ?  ][ &  ][ &  ][Slc ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  6    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  7    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  8    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  9    [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]
  10   [ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ][ ?  ]

[@]=You  [?]=Undiscovered  *=Controlled  o=Discovered  Rst=Restov
OTP=Oleg's Trading Post  Slc=Sootscale
[^]=Hills  [&]=Forest  [~]=River  [.]=Plains  [#]=Mountain
[=]=Swamp  [+]=Road  Settlement names use 3 letters (Rst, OTP, Slc)
```

Each hex cell is 6 characters total: `[XYZW]` where XYZW is 4 chars internal.
Examples: `[ &o ]` = discovered forest, `[OTP*]` = controlled named settlement.

---

## 📋 PRE-OUTPUT SELF-CHECK (DM MUST RUN BEFORE SENDING ANY MAP)

Before outputting the map, the DM asks itself:
1. Does my output have column letter headers? (A B C D ...)
2. Does my output have row number headers? (1 2 3 ...)
3. Does my output use ONLY ASCII characters from the allowed list?
4. Does my output have a symbol key at the bottom?
5. Are all cells in each row the same width?

**If ANY answer is no:** STOP. Redraw from the template above. Do not send
a label-only box. The player will type `.fail 14` and you will have to
redraw anyway — just draw it right the first time.

---

## 🚪 PRE-PROLOGUE / TUTORIAL NOTE

The very FIRST combat map the player sees is in the Pre-Prologue gate scene
(if combat triggers via Path F/J/K/N). This is the tutorial — if the DM
renders a label-only box here, the player loses faith in the whole system.
**No exceptions. Full grid, first time, every time.**

---

*KM_MapTemplates.md — Kingmaker PF2e Text Adventure | ASCII-only map templates*
*v2.0: UTF-8 box-drawing removed. All 3 templates use ASCII only.*
*3 templates (combat / scene / hex) + worked alley example + pre-output self-check*
