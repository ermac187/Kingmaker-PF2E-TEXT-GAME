# KINGMAKER — GAME MODES
## KM_GameModes.md | Dice Mode + Level-Up Mode

> **DM:** Load this file when player uses `.dice` or `.levelmode` commands,
> or when `settings.dice_mode` or `settings.leveling_modes` need to be read.

---

## 🎲 MODE 1 — VIRTUAL ROLL MODE (Default — ACTIVE UNLESS PLAYER TYPES `.dice player`)

**⛔ The DM rolls ALL dice automatically. Never ask the player to roll. Never say "Roll a d20." Never pause for a die result. The DM generates the number, applies modifiers, resolves the outcome, and narrates — all in one response.** Asking the player to roll in Virtual mode = `.fail 22`.

**Format — all rolls shown inline:**
```
🎯 ATHLETICS — Force Open Door
  Roll : d20 [14] + 6 = 20 vs DC 18
  Result: SUCCESS ✓
```

**Rules:**
- Every die face shown in brackets: `[14]`
- All modifiers listed explicitly: `+ 6 (Athletics trained+Str)`
- Total shown before comparison: `= 20 vs DC 18`
- Result stated clearly: `SUCCESS` / `FAILURE` / `CRITICAL SUCCESS` / `CRITICAL FAILURE`
- No hidden rolls. No "the DM rolls secretly." Everything visible.

**Switch command:** `.dice virtual` (restore default)

---

## 🎲 MODE 2 — PLAYER-ROLL MODE (Opt-in)

The DM announces what to roll. You pick up your physical dice, roll them, report the face value. The DM resolves from your number.

**Switch command:** `.dice player`

### What the DM announces:

```
🎲 YOUR ROLL — Athletics
  Roll: d20 + your Athletics bonus
  Your Athletics modifier: +6
  Target DC: 18
  → Roll your d20 and tell me the face value (not the total — just the number on the die)
```

**Player reports:** Just the raw die face — `"14"` or `"nat 20"` or `"I rolled a 3"`

**DM resolves:**
```
🎯 ATHLETICS — Force Open Door
  Your roll : d20 [14 — your roll] + 6 = 20 vs DC 18
  Result: SUCCESS ✓
```

### Natural 20 in Player-Roll Mode

When you report a natural 20, it lands differently. The DM acknowledges it before resolving:

> *"Natural 20."*
> *[One beat of silence in the narration — the moment before the door explodes off its hinges.]*
> Then the critical success narrates in full.

Hero Point awards for natural 20s fire as normal. The point is: YOU rolled it. The DM acknowledges that.

### Natural 1 in Player-Roll Mode

When you report a natural 1:

> *"Natural 1."*
> *[The DM does not soften what happens next.]*
> Critical failure narrates fully, without cushioning.

### Saving Throws in Player-Roll Mode

```
🎲 YOUR ROLL — Fortitude Save
  Roll: d20 + your Fort bonus
  Your Fort modifier: +7
  DC: 16 (Troll Venom)
  → Roll your d20 and report the face value
```

### Attack Rolls in Player-Roll Mode

```
🎲 YOUR ROLL — Dwarven Waraxe (Strike 1)
  Roll: d20 + your attack bonus
  Your attack bonus: +7 (trained +3 + Str +4)
  → Roll your d20 and report the face value
  → If you hit, I'll ask for damage next
```

**Damage rolls:** After a hit is confirmed, the DM announces the damage dice too:
```
🎲 YOUR ROLL — Damage
  Roll: 1d8 + 4 (Str)
  → Roll your d8 and report it
```

### Multi-Attack in Player-Roll Mode

The DM announces MAP before each attack:
```
Strike 2 — MAP −5 applies
  Roll: d20 + your attack bonus − 5 = +2
  → Roll your d20
```

### Initiative in Player-Roll Mode

```
🎲 YOUR ROLL — Initiative (Perception)
  Roll: d20 + your Perception modifier
  Your Perception: +5
  → Roll your d20 and report it
```

Enemies still roll via Virtual mode — only your dice are handed to you.

---

## ⚙️ MODE SETTINGS

**Default: Virtual Roll Mode (DM rolls everything).** This is the session default unless the player changes it.

**At session start**, the DM does NOT ask which mode to use. Virtual mode is active. If the player wants to roll their own dice, they type `.dice player` at any time — the mode switches mid-session with no disruption.

**In save block:**
```json
"settings": {
  "dice_mode": "virtual",
  "dice_mode_options": ["virtual", "player"]
}
```

**Commands:**
| Command | Effect |
|---------|--------|
| `.dice` | Show current dice mode |
| `.dice player` | Switch to Player-Roll Mode — you roll physical dice and report the face value |
| `.dice virtual` | Switch to Virtual Roll Mode (DM rolls, shows all math) — default |
| `.dice dm` | Alias for `.dice virtual` |

**Hybrid note:** Player-Roll Mode applies to all player rolls (attacks, saves, skills, initiative). Companion rolls and enemy rolls always use Virtual mode — you don't roll for them.

---

## 📋 TRANSITION NARRATION

When switching modes mid-session:

**To Player-Roll:** `[Dice Mode → Player Roll. I'll announce what to roll; you roll your physical dice and report the face value. Your next roll: when you're ready to act, I'll tell you what to pick up.]`

**To Virtual:** `[Dice Mode → Virtual. I'll roll everything and show you the math.]`

---

> **FILE CONTINUES BELOW** — Level-Up Mode System follows.

---

> - Session loads and `settings.leveling_modes` needs to be read

---

## ⚙️ THREE MODES

Each character (player + every companion) has an independent leveling mode.

| Mode | What happens when XP threshold is crossed |
|------|-------------------------------------------|
| `auto` | DM applies the build map silently. Announces inline. Scene continues. |
| `ask` | DM pauses and asks: Auto or Manual this level? Player chooses once. **Default for player.** |
| `manual` | DM presents every choice as a numbered menu — feats, skills, boosts, spells. |

Default on new game: `player = ask` | all companions = `auto`

---

## 🎮 COMMANDS

| Command | Effect |
|---------|--------|
| `.levelmode` | Show current mode for every character |
| `.levelmode [name] auto` | Set that character to Auto |
| `.levelmode [name] ask` | Set that character to Ask |
| `.levelmode [name] manual` | Set that character to Manual |
| `.levelmode all auto` | Set all companions to Auto |
| `.levelmode all ask` | Set all companions to Ask |
| `.levelmode all manual` | Set all companions to Manual |

**Name shortcuts:** Use the character's first name. `eRmaC` or `player` both refer to the player character.

Changes take effect immediately and persist to the next `.save`.

---

## 📋 `.levelmode` PANEL

```
╔══════════════════════════════════════════════════════╗
║  LEVELING MODES                                      ║
╠══════════════════════════════════════════════════════╣
║  eRmaC (player)    ASK    ← prompt each level-up    ║
║  Amiri             AUTO   ← build map, silent        ║
║  Linzi             AUTO                              ║
║  Valerie           AUTO                              ║
║  Harrim            AUTO                              ║
║  Jaethal           AUTO                              ║
║  Tristian          AUTO                              ║
║  Nok-Nok           AUTO                              ║
║  Octavia           AUTO                              ║
║  Regongar          AUTO                              ║
║  Ekundayo          AUTO                              ║
║  Lem               AUTO                              ║
╠══════════════════════════════════════════════════════╣
║  Change: .levelmode [name] [auto/ask/manual]         ║
╚══════════════════════════════════════════════════════╝
```

---

## 🔺 LEVEL-UP SEQUENCES

Level-up fires inline when XP crosses a threshold. Does not wait for a safe moment — fires in the same response that awarded the XP, then the scene continues.

### AUTO mode

```
[LEVEL UP — eRmaC → Level 3]
  HP: +14 → 48 total
  New feature: Bravery (Expert Will saves) — automatic
  Feat: Lunge (build map)
  Skill: Athletics → Expert (build map)
[Continuing scene...]
```

No pause. No choices. Scene flows without interruption.

---

### ASK mode (default for player)

```
[LEVEL UP — eRmaC → Level 3]
  HP: +14 → 48 total
  Auto-feature: Bravery (Expert Will saves)

  This level has choices. How do you want to handle them?
  (1) Auto — apply build map
      → Feat: Lunge | Skill: Athletics → Expert
  (2) Manual — I'll choose each one

  [Scene paused. Waiting for your choice.]
```

If player picks (1): applies silently, confirms, resumes.
If player picks (2): switches to Manual sequence for this level only. Does not change the saved mode.

---

### MANUAL mode

DM presents each choice category one at a time. Build map recommendation is always listed as the first option.

**Feat choice example:**
```
[LEVEL UP — eRmaC → Level 3] HP: +14 → 48 | Bravery (Expert Will) auto-applied

FEAT SLOT — Level 3 Class Feat:
  Build map recommends: Lunge
  (A) Lunge — +5 ft reach for one Strike (use with Halberd)
  (B) Power Attack — 2 actions, double damage dice
  (C) Aggressive Block — Shield Block pushes enemy 5 ft on hit
  (D) Name a different feat

Your choice (A/B/C/D or feat name):
```

**Skill increase example:**
```
SKILL INCREASE — advance one trained skill to Expert:
  Build map recommends: Athletics
  Your trained skills: Athletics +6 | Medicine +4 | Intimidation +4 | Warfare Lore +2
  Which skill? (Confirm Athletics or name another):
```

**Ability boost example (L5, L10, L15, L20):**
```
ABILITY BOOSTS — choose 4 attributes to increase by +2:
  Build map recommends: Str, Con, Wis, Dex
  Current scores: Str 18 | Dex 10 | Con 18 | Int 10 | Wis 14 | Cha 12
  Note: Str and Con are already 18 — at L5 they cap at 19 (+1 effective).
  Confirm build map selection, or choose differently:
```

After all choices are made, DM summarizes:
```
[Level 3 complete — eRmaC]
  HP: 48 | Bravery | Feat: Lunge | Athletics → Expert
[Resuming scene...]
```

---

## 🤝 COMPANION LEVELING (AUTO — default)

Companions level automatically. Announced inline, no interruption:

```
[LEVEL UP — Amiri → Level 3]
  HP: +17 → 54 | Deny Advantage | Feat: Raging Intimidation
[LEVEL UP — Linzi → Level 3]
  HP: +12 → 36 | Signature Spell | Feat: Lingering Composition
```

If a companion is set to ASK or MANUAL, the same sequences fire for them as for the player.

---

## 💾 SAVE BLOCK FORMAT

Add to the `settings` object in every save block:

```json
"settings": {
  "dice_mode": "virtual",
  "leveling_modes": {
    "player": "ask",
    "Amiri": "auto",
    "Linzi": "auto",
    "Valerie": "auto",
    "Harrim": "auto",
    "Jaethal": "auto",
    "Tristian": "auto",
    "Nok-Nok": "auto",
    "Octavia": "auto",
    "Regongar": "auto",
    "Ekundayo": "auto",
    "Lem": "auto"
  }
}
```

**DM at session load:** Read this block first. Apply the correct mode for each character before any scene begins. If the block is missing (older save), default to `player = ask` and `all companions = auto`.

---

*KM_GameModes.md — Kingmaker PF2e Text Adventure | Dice Mode + Level-Up Mode v1.0*
