# KM_Map_Artifact.md — Interactive Emoji Map (claude.ai ARTIFACT)
## FILE_KEY: KMMAPART:emoji-grid
## RULE_QUOTE: Render the tactical / floor map as a claude.ai HTML ARTIFACT — aligned emoji, numeric columns (no 26-letter cap), letter rows, hover tooltips (coordinate + what the tile is), fog-of-war, fill-width. The DM edits ONLY the DATA BLOCK each turn. ASCII (KM_Map.md § TEMPLATE 1) is the fallback when an artifact cannot be produced.

---

## WHY ARTIFACT (vs ASCII)
A claude.ai artifact uses a real CSS grid, so each cell is a fixed box — **emoji align
perfectly** regardless of character width (impossible in a monospace code fence). It also
gives: **color-coded terrain · numeric columns (1,2,3…N — no A–Z ceiling) · letter rows ·
hover tooltips that name every object/creature + its stats · fog-of-war that reveals on
scout · fill-width sizing**. This is the map the player asked for (2026-06-23).

## WHEN — `.art` ON DEMAND, or automatically when `map_primary: artifact` (2026-06-24)
⛔ Build this emoji artifact when: (a) the player types **`.art`** (aliases `.mapart` / `.map art`) —
a one-off; or (b) `story_flags.map_primary: artifact` is set (the player toggled the PRIMARY map to
artifact via **`.maptoggle`**), on every automatic map turn. In the DEFAULT mode `map_primary: ascii`
the automatic every-turn / every-round map is the **ASCII tight grid** (KM_Map.md § TEMPLATE 1) — do
NOT attempt the artifact automatically there, because ASCII always renders and can't dump code while a
claude.ai auto-artifact is unreliable. `.maptoggle` flips the mode (e.g. to test the artifact as
primary on Claude Code). NEVER paste this artifact's HTML as message text (code-dump = `.fail 14`) —
the output must be a RENDERED artifact.

## ⛔ USE GENEROUS DIMENSIONS — DENSE BEATS SPARSE
The cells STRETCH to fill the panel width (CSS `1fr`), so box size is set by how MANY cells you
use: **more columns/rows = smaller boxes = more detail**, and the map still fills the width.
Default to a **big, detailed FLOOR SECTION** — the room + corridor + several adjacent rooms +
terrain — not a sparse little grid. Aim for **~24–32 columns** when the scene supports it (the
boxes shrink to fit; the emoji scale with them). Don't leave the panel half-empty with an 8–16
column map when you can show the whole floor at 28. (Readability floor ≈ 35–40 columns before
emoji get too small — stay under that.) Rows can run as tall as the scene needs (the panel
scrolls vertically).

## HOW THE DM RENDERS IT
1. Output the HTML below **as a claude.ai ARTIFACT** (an HTML artifact).
2. **Edit ONLY the `KMMAP` DATA BLOCK** at the top — `ncols`, `rowL`, `rows[]`, and the
   `tiles{}` entries for THIS turn's creatures/objects. Leave the render code beneath it
   byte-for-byte.
   ⛔ **DO NOT regenerate `rows[]` from scene memory or coordinate lists.** That is the
   source of every position bug. Instead: **copy the pre-built `rows[]` block verbatim from
   the floor manifest in KM_CombatTurn.txt** (§ LOWER FLOOR → ARTIFACT DATA BLOCK for the
   corridor; § FIXED LAYER for the upper floor). When creatures move, change exactly one
   character per affected cell: `rows[rowIndex][col-1] = newChar`. Never rewrite a whole row
   from scratch.
3. **Coordinates read COLUMN-NUMBER + ROW-LETTER** — e.g. `5B` = column 5, row B. (Numbers
   across the top, letters down the side.) Reference cells this way in prose too.
4. **FOG OF WAR:** an un-perceived room's interior cells are `?` (the renderer draws ❓ on a
   dark tile). A room reveals — `?` → real contents — when the player perceives it (looks in,
   scouts, a DESTINATION CLUE, a companion reports). ⛔ Never reveal an unscouted room's
   occupants (`.fail 9`).
5. **FLOOR SECTION:** prefer room + corridor + adjacent rooms (KM_Map.md § FLOOR-SECTION),
   not a lone room — so the player sees layout, doors, rescues, where to send a companion.
6. **WIDTH:** numeric columns have NO 26-cap; size to what fits, the grid fills width and can
   scroll horizontally if huge.
7. **FALLBACK:** if an artifact cannot be produced this turn, render the ASCII grid
   (KM_Map.md § TEMPLATE 1) instead — never skip the map.

## ⛔ FULL EMOJI SET — PICK THE MOST ACCURATE EMOJI PER ENTITY
The `e:` field of each tile accepts **ANY emoji** — the whole Unicode palette is available.
Choose the one that best matches what is ACTUALLY there; do not settle for a generic
stand-in when a precise emoji exists (a wolf is 🐺, not "🗡️ enemy"). Reference set (a
STARTER, never a limit):
  CREATURES — you 🧍 · assassin 🥷 · bandit/rogue 🗡️ · soldier 🪖 · archer 🏹 · mage 🧙 ·
    wolf 🐺 · bear 🐻 · boar 🐗 · goblin 👺 · kobold 🦎 · troll/ogre 👹 · giant 🧌 ·
    zombie 🧟 · skeleton 💀 · spider 🕷️ · snake 🐍 · rat 🐀 · dragon 🐉 · boss/leader 👑 ·
    civilian 🧑 · child 🧒 · servant 🧹 · sleeping/unconscious 😴 · prisoner ⛓️
  INDOOR OBJECTS — bed 🛏️ · chair/desk 🪑 · table 🍽️ · chest 🧰 · barrel 🛢️ · crate 📦 ·
    door 🚪 · window 🪟 · stairs 🪜 (or ⬇️/⬆️) · candle 🕯️ · fireplace/hearth 🔥 ·
    armor stand 🛡️ · weapon rack ⚔️ · books/desk 📚 · altar ⛪
  OUTDOOR TERRAIN — tree 🌲 · forest 🌳 · bush/scrub 🌿 · grass 🌱 · water/lake 💧 ·
    river 🌊 · rock/boulder 🪨 · mountain ⛰️ · hill 🏔️ · road 🟫 · snow ❄️ · campfire 🔥
  HAZARDS — fire 🔥 · smoke 💨 · trap 🪤 · poison ☠️ · ice 🧊 · pit/hole ⬛ · blood 🩸
  FOG — unscouted ❓
Tiles with no emoji (`e:''`) just show their background color (walls, floor, corridor).

---

## ════════ DATA BLOCK — THE DM EDITS THIS EACH TURN, NOTHING BELOW IT ════════

Output everything from `<div id="kmmap">` to the closing `</script>` as the artifact. Edit
ONLY the `window.KMMAP = { … }` object. (Worked example = the PR_04 guest-floor section.)

```html
<div id="kmmap" style="font-family: system-ui, sans-serif;"></div>
<div id="kminfo" style="margin-top:10px; min-height:24px; font-size:14px; font-weight:600;">Hover a tile — coordinate is column-number + row-letter (e.g. 5B).</div>
<div id="kmlegend" style="margin-top:6px; font-size:13px; opacity:0.8; line-height:2;"></div>
<script>
/* ===== DATA BLOCK — EDIT ONLY THIS each turn ===== */
window.KMMAP = {
  ncols: 25,
  rowL: "ABCDEFGHIJKL",
  /* ⛔ THIS IS THE SAME 25×12 FLOOR THE ASCII FALLBACK DRAWS (KM_CombatTurn.txt manifest).
     The two maps are EQUAL — identical geometry, identical tokens, identical coordinates; the
     ONLY difference is emoji here vs glyphs there. Never let one be bigger than the other.
     ⛔ THE rows[] BELOW IS THE UPPER GUEST-FLOOR EXAMPLE ONLY. When the live scene is the LOWER
     CORRIDOR (PR_05 / after descending 4L), do NOT render this guest floor — REPLACE ncols/rowL/
     rows[]/tiles{} with the pre-built CORRIDOR ARTIFACT DATA BLOCK from KM_CombatTurn.txt
     § LOWER FLOOR (5 rows A–E, Tartuccio at 25C). Rendering the wrong floor = .fail 14. */
  rows: [
    "###=#####################",
    "#..1..#.....#?????#?????#",
    "#.@...#..K..#?????#?????#",
    "#.....#.....#?????#?????#",
    "#*...*#*....#?????#?????#",
    "###/#####/#####/#####/###",
    "#.......................#",
    "###/#####/#####/#####/###",
    "#..Y..#?????#?????#?????#",
    "#.....#?????#?????#?????#",
    "#*...*#?????#?????#?????#",
    "###>#####################"
  ],
  /* one entry per glyph used above. e = emoji (any!), d = hover tooltip text, bg = tile colour.
     ⛔ ROOMS SHARE ONE WALL — the `#` between two rooms is a SINGLE shared partition, never a
     double/triple-thick wall. Widen the map with MORE ROOMS / corridor / terrain, NEVER with
     a strip of redundant walls (wasted filler defeats the point of a bigger map). */
  tiles: {
    '#':{bg:'#39382f', e:'',   d:'Wall'},
    '.':{bg:'#dcd9cb', e:'',   d:'Floor'},
    '?':{bg:'#222019', e:'❓', d:'Unscouted — scout this room to reveal it'},
    '=':{bg:'#39382f', e:'🪟', d:'Broken window — the assassins entry'},
    '/':{bg:'#cfc7a6', e:'🚪', d:'Door'},
    '>':{bg:'#39382f', e:'🪜', d:'Stairs down — to the fire below'},
    '*':{bg:'#dcd9cb', e:'🛏️', d:'Bed — cover'},
    '@':{bg:'#dcd9cb', e:'🧍', d:'eRmaC (you) — Barbarian, guisarme in hand'},
    '1':{bg:'#dcd9cb', e:'🥷', d:'Assassin — HP 12/12 · AC 15 · flat-footed, back turned'},
    'K':{bg:'#dcd9cb', e:'😴', d:'Keqing — asleep, NW room · can be woken or rescued'},
    'Y':{bg:'#dcd9cb', e:'😴', d:'Ally — asleep teammate, SW room · can be woken or rescued'}
  }
};
/* ===== END DATA BLOCK — everything below is FIXED, do not change ===== */
(function(){
  var M = window.KMMAP, info = document.getElementById('kminfo'), mapDiv = document.getElementById('kmmap');
  var t0 = M.tiles['.'] || {bg:'#dcd9cb', e:'', d:'Floor'};
  var html = '<div id="kmgrid" style="display:grid; grid-template-columns: 26px repeat('+M.ncols+',minmax(0,1fr)); gap:2px; width:100%;">';
  html += '<div></div>';
  for (var c=0;c<M.ncols;c++){ html += '<div style="text-align:center; font-size:12px; opacity:0.6;">'+(c+1)+'</div>'; }
  for (var r=0;r<M.rows.length;r++){
    html += '<div style="display:flex; align-items:center; justify-content:center; font-size:13px; opacity:0.7;">'+M.rowL[r]+'</div>';
    for (var c2=0;c2<M.ncols;c2++){
      var ch = M.rows[r][c2], t = M.tiles[ch] || t0, coord = (c2+1)+M.rowL[r], line = coord+' — '+t.d;
      html += '<div data-info="'+line+'" title="'+line+'" style="aspect-ratio:1; background:'+t.bg+'; border-radius:3px; display:flex; align-items:center; justify-content:center; font-size:min(4.5vw,26px); cursor:default;">'+t.e+'</div>';
    }
  }
  html += '</div>';
  mapDiv.innerHTML = html;
  document.getElementById('kmgrid').addEventListener('mouseover', function(e){ if(e.target.dataset && e.target.dataset.info){ info.textContent = e.target.dataset.info; } });
  var seen = {}, leg = '';
  for (var r2=0;r2<M.rows.length;r2++){ for (var c3=0;c3<M.ncols;c3++){ var g=M.rows[r2][c3], tt=M.tiles[g]; if(tt && tt.e && !seen[g]){ seen[g]=1; leg += '<span style="margin-right:14px;">'+tt.e+' '+tt.d.split(' — ')[0]+'</span>'; } } }
  document.getElementById('kmlegend').innerHTML = leg;
})();
</script>
```

---

## NOTES
- The **legend builds itself** from whatever tiles are on the map this turn (only glyphs
  actually used appear), so the DM never maintains a separate legend.
- The **info line** under the grid updates on hover (coordinate + what the tile is); browsers
  also show the native `title` tooltip.
- Keep `rows[]` rectangular: every string is exactly `ncols` characters.
- `aspect-ratio:1` keeps cells square as they stretch to fill width; `font-size:min(4.5vw,26px)`
  scales the emoji with the panel.
- This is rendered by the in-game DM on **claude.ai** (its artifact panel) — final sizing is
  tuned from a real in-game screenshot, not a Claude-Code preview.

*KM_Map_Artifact.md — interactive emoji map template | v1.0 | 2026-06-23*
