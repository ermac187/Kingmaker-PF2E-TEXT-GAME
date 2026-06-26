# KINGMAKER — MULTI-ROOM DUNGEON PUZZLES
## KM_DungeonPuzzles.md | Referenced by: KM_Ch2.md, KM_Ch3.md, KM_Ch4.md, KM_Puzzles.md

> **DM:** These are multi-room puzzles that span 3+ connected rooms. The player must track information across rooms (rune sequences, lever states, key fragments). Use the ASCII map to show room connections and puzzle state. Standard puzzle rules apply (KM_Puzzles.md): player solves, not skill checks. One hint per puzzle. Skill check bypass after 3 failed attempts.

---

## 🗺️ DUNGEON PUZZLE 1: THE RUNE GATE (Ch2, Old Sycamore Deep)

**Setup:** 4 rooms connected in a square. Central locked door requires 4 runes activated in correct sequence.

```
MAP:
  [A]———[B]
   |     |
  [D]———[C]
      ↓
   [GATE]
```

**Room A — The Scholar's Chamber:**
- Wall inscription: "First comes the star that guides / Then the wave that carries"
- Rune pedestal with STAR symbol. Pressing it: pedestal glows blue. Records: Rune 1 = STAR.
- Bookshelf: `.examine bookshelf` reveals faded text: "The order is written in the walls, not the books."

**Room B — The Warrior's Chamber:**
- Wall inscription: "Third stands the mountain, unmoved / Last falls the flame, consuming what remains"
- Rune pedestal with FLAME symbol. If pressed now: electric shock (2d6 lightning). Must be pressed FOURTH.
- Weapon rack: `.examine weapons` — ornamental, not real. Maker's mark matches Room A books.

**Room C — The Priest's Chamber:**
- Rune pedestal with MOUNTAIN symbol. Must be pressed THIRD.
- Altar: `.examine altar` — offerings of stone chips. Recall Knowledge (Religion DC 14): "Mountain before flame — the order of creation in Sarkorian theology."

**Room D — The Thief's Chamber:**
- Rune pedestal with WAVE symbol. Must be pressed SECOND.
- Hidden panel (Perception DC 16): Contains the sequence written plainly: ★ 🌊 ⛰️ 🔥

**Solution:** Press pedestals in order: A (Star) → D (Wave) → C (Mountain) → B (Flame)

**Correct:** Central GATE opens. +100 XP. +1 Scholarly disposition.
**Wrong order:** All pedestals reset. 1d6 force damage to player. "The runes reject your offering."
**Skill bypass (after 3 failures):** Recall Knowledge (Arcana DC 18) — DM reveals the sequence.

---

## 🗺️ DUNGEON PUZZLE 2: THE PRESSURE PLATE MAZE (Ch3, Ancient Tomb)

**Setup:** A 5×5 grid room. Some tiles are pressure plates. Walking on the wrong plate = dart trap (2d4 piercing). The safe path is encoded on a mosaic in the previous room.

```
MAP:
  [ENTRY] → [MOSAIC ROOM] → [GRID ROOM] → [TREASURE]

GRID ROOM (5×5):
  [ ][ ][ ][ ][ ]   ← Row 1 (far wall)
  [ ][ ][ ][ ][ ]   ← Row 2
  [ ][ ][ ][ ][ ]   ← Row 3
  [ ][ ][ ][ ][ ]   ← Row 4
  [E][ ][ ][ ][ ]   ← Row 5 (entry side)

  E = Entry point (bottom-left)
  T = Target (top-right, Row 1 Col 5)
```

**Mosaic Room:**
A floor mosaic shows a serpent winding through a grid. The serpent's path = safe tiles.
- `.examine mosaic` — DM describes the serpent's path clearly
- The path: E(5,1) → (4,1) → (4,2) → (3,2) → (3,3) → (2,3) → (2,4) → (1,4) → (1,5) = T

**Grid Room:**
- Player states which tile they step on: "I move to row 4, column 1"
- **Safe tile:** DM narrates: "The stone holds. No sound."
- **Trap tile:** Dart trap: 2d4 piercing, Ref DC 14 half. Player returns to last safe tile.
- **Companion warning:** If a companion with Perception +8 or higher is present, they shout a warning on the FIRST trap tile only ("STOP!"). Free retry. Not subsequent traps.

**Solution:** Follow the serpent path exactly.
**Alternative:** Fly over (if available). Acrobatics DC 20 to jump tile-to-tile (3 checks, 1 per row traversed).
**Brute force:** Take the traps. Max 4 trap tiles on a random path. 8d4 piercing total (expensive but survivable).

---

## 🗺️ DUNGEON PUZZLE 3: THE ELEMENTAL LOCKS (Ch4, Armag's Tomb Antechamber)

**Setup:** 3 rooms, each with an elemental lock. All 3 must be solved to open the inner tomb. Locks can be solved in any order. Each lock requires combining two elements using the Surface Combo system (KM_CinematicCombat.md).

```
MAP:
  [FIRE LOCK]  [WATER LOCK]  [EARTH LOCK]
       \           |           /
        \          |          /
         [INNER TOMB DOOR]
```

**Fire Lock Room:**
- A frozen brazier. The fire is encased in ice. Mundane fire doesn't melt it — magical cold.
- **Solution:** Cast a fire spell ON the ice (Fire + Frozen surface = thaw, then brazier lights)
- **Alternative:** Kineticist fire impulse, alchemist fire, or torch + bellows (Crafting DC 16)
- **Lock opens:** Brazier lights. First seal broken.

**Water Lock Room:**
- A dry fountain. The water channel leads to a sealed pipe. Above: a rain-catcher on the ceiling filled with stagnant water.
- **Solution:** Break the rain-catcher (Athletics DC 14 or ranged attack). Water flows to fountain. Fountain activates mechanism.
- **Alternative:** Create Water spell. Hydraulic Push into the channel.
- **Lock opens:** Fountain flows. Second seal broken.

**Earth Lock Room:**
- A stone column with a crack. The column must be broken to open the path — but hitting it triggers a cave-in (4d6 bludgeoning in 15 ft).
- **Solution:** Earthquake effect, Earth Kineticist blast, or place an explosive at the base and retreat (Crafting DC 16 to rig, 3 rounds to retreat).
- **Alternative:** Tunnel around it (2 hours, Athletics DC 16, partner assists).
- **Caution solution:** Examine the crack first (Perception DC 14). Reveals structural weakness — targeted strike at the weak point: no cave-in.
- **Lock opens:** Column splits. Third seal broken.

**Inner Tomb Door:** All 3 seals broken → door opens. +150 XP. +1 Scholarly.

---

## 📋 PUZZLE STATE TRACKING

DM tracks puzzle state on the grid/map using symbols:

| Symbol | Meaning |
|--------|---------|
| ✓ | Rune/lock solved |
| ✗ | Rune/lock failed attempt |
| → | Player's current position |
| ! | Trap (revealed after trigger) |
| ? | Unexamined room |

**Save block (during dungeon):** `"dungeon_state": { "dungeon_id": "rune_gate", "rooms_cleared": ["A", "D"], "puzzle_state": {"star": "activated", "wave": "activated", "mountain": "inactive", "flame": "inactive"}, "attempts": 1 }`

---

## ⚠️ DM RULES

1. **Player solves. Not skill checks.** The puzzle is the game. Skill checks are bypass only.
2. **Show the map at each step.** Update ASCII grid with current state after every player action.
3. **One hint per puzzle.** Genuine clue, not the answer. "The mosaic in the previous room showed a path."
4. **Companion contributions are flavor, not solutions.** A companion can comment ("This reminds me of Sarkorian theology") but cannot solve it for the player.
5. **Track state in save block during dungeon.** If session ends mid-puzzle, state persists.
6. **Multiple attempts allowed.** Resetting costs time (and sometimes HP from traps). The player is never permanently locked out.

---

## 🗺️ DUNGEON PUZZLE 4: THE WEIGHT BRIDGE (Ch4, Armag's Tomb Approach)

**Setup:** A bridge over a chasm. Weight sensors embedded in the stones. Too much weight = collapse. Too little = doors won't open.

```
MAP:
  [ENTRANCE] → [BRIDGE — 15 tiles, 3 wide] → [DOOR]

BRIDGE RULES:
  Total weight on bridge must be EXACTLY 4 (measured in "stones")
  Player = 2 stones. Companion = 1 stone each. Equipment = varies.
  Door opens only when bridge reads exactly 4.
  Bridge collapses at 6+.
```

**Clue (previous room):** A mural showing four figures crossing a bridge. One is large (2), three are small (1 each). But only three figures reach the other side — one stepped off midway. Total on bridge at the door: 2 + 1 + 1 = 4.

**Solutions:**
- Player (2) + 2 companions (1+1) = 4 ✓. Two companions stay behind.
- Player (2) + 1 companion (1) + drop 1 stone of equipment on the bridge = 4 ✓
- Player removes armor (drops to 1) + 3 companions = 4 ✓ (creative, risky)
- Fly/levitate across (no weight) and open door from the other side — bypasses entirely

**Wrong:** Player + 3 companions = 5 → bridge groans, warning. Player + 4 = 6 → collapse (4d6 fall damage, Ref DC 18 to grab edge).

**XP:** 100 XP. +1 Scholarly if mural clue used.

---

## 🗺️ DUNGEON PUZZLE 5: THE MIRROR MAZE (Ch5, Pitax Palace Basement)

**Setup:** A 4×4 grid of rooms. Each room has a mirror on one wall. Mirrors can be rotated. A beam of light enters from the top-left. The beam must reach the bottom-right to open the vault.

```
MAP (4×4, beam enters A1, must exit D4):
  [A1→]  [A2]  [A3]  [A4]
  [B1]   [B2]  [B3]  [B4]
  [C1]   [C2]  [C3]  [C4]
  [D1]   [D2]  [D3]  [D4→EXIT]

Mirrors: each room has 1 mirror, angled / or \
Rotate mirror: player specifies room + angle
Beam travels in straight line, bounces off mirrors
```

**Starting mirror positions (DM tracks):**
- A1: \ (redirects beam down to B1)
- B1: / (redirects beam right to B2)
- B2: empty (beam passes through)
- B3: \ (redirects beam down to C3)
- All others: random angles

**Solution:** Multiple valid paths. Player must trace the beam through rotations. DM describes: "The beam hits the mirror in B3 and redirects downward. It passes through C3 (no mirror) and hits D3. The mirror in D3 is angled \ — the beam goes right, into D4. The vault clicks."

**Hint:** A diagram of the grid scratched into the wall of A1 with the beam drawn — but the mirrors have been moved since the diagram was made. One mirror is correct, the rest need adjusting.

**XP:** 120 XP. +1 Scholarly.

---

## 🗺️ DUNGEON PUZZLE 6: THE BLOOD OATH DOORS (Ch5-6, Nyrissa's Approach)

**Setup:** Three doors. Each requires a sacrifice — not HP, but something the player has earned. The doors test what the player values.

```
MAP:
  [HALL] → [DOOR 1] → [DOOR 2] → [DOOR 3] → [INNER SANCTUM]

Each door has an inscription. Each demands a price.
All three must be opened. The order doesn't matter.
```

**DOOR 1 — THE DOOR OF TITLES:**
*"Give a name you gave. One who carries your honor must return it."*
- **Price:** Revoke one companion title. The companion loses their Suffix and Prefix. Relationship −1. The title burns away on the door.
- **Alternative (Arcana DC 22):** Create a false title — an illusion of sacrifice. Door accepts it. No companion loses anything. +1 Cunning.
- **Refusal:** Door remains shut. Must find another way (Athletics DC 24 to force, or Thievery DC 22 to pick the magical lock).

**DOOR 2 — THE DOOR OF MEMORY:**
*"Give a moment that made you. One that you would relive if you could."*
- **Price:** The player names a Bond Moment from the Bond History Log. That moment is consumed — the companion and player both forget it happened. Remove from save block.
- **Alternative (Diplomacy DC 22):** Argue that all moments are equal. Door: "Interesting. Pass." No sacrifice.
- **Refusal:** Same as Door 1.

**DOOR 3 — THE DOOR OF POWER:**
*"Give what makes you strong. One ability you earned must be unearned."*
- **Price:** Lose one Prestige Upgrade ability (L10 or L15). Ability deactivates permanently.
- **Alternative (Will DC 24):** Resist the door's demand through sheer willpower. "I earned this. You cannot take what I chose to become."
- **Refusal:** Same forcing options.

**Design intent:** The Alternatives exist so the player never HAS to sacrifice. But the sacrifices are real — and Nyrissa, watching from beyond the door, judges what the player chose. If the player sacrificed all three: `nyrissa_saveable +2` (she saw someone give up what they valued). If zero sacrifices: +0, but +1 Cunning or +1 Blunt.

**XP:** 150 XP. +1 Scholarly if alternatives found.

---

## ⚠️ DM RULES

1. **Player solves. Not skill checks.** Skill checks are bypass only.
2. **Show the map at each step.** Update ASCII grid with current state.
3. **One hint per puzzle.** Genuine clue, not the answer.
4. **Companion contributions are flavor, not solutions.**
5. **Track state in save block during dungeon.**
6. **Multiple attempts allowed.** Resetting costs time (and sometimes HP).

---

*KM_DungeonPuzzles.md — Kingmaker PF2e Text Adventure | Multi-Room Dungeon Puzzles v2.0*
*6 dungeons across Ch2-6. Inspired by Icewind Dale.*
