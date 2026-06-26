# KINGMAKER — LEVEL-UP PROCEDURES
## KM_Leveling.md | Referenced by: KM_DMRules.md, KM_Ch1.md, KM_Ch2.md, KM_Ch3.md, KM_Ch4.md, KM_Commands.md, KM_Commands_Maps.md, KM_PartySystem.md, KM_Prologue_Export.md, KM_Ch1_Export.md, KM_QuickStart.md, KM_Spells_Builds.md, KM.txt, KM_P2.txt

> **DM:** This file contains XP thresholds, the player level-up procedure, and routing to companion leveling files. Load every session.

---

## 📊 XP THRESHOLDS (PF2e Standard)

| Level | XP Required | Cumulative XP |
|-------|-------------|---------------|
| 1 → 2 | 1,000 | 1,000 |
| 2 → 3 | 1,000 | 2,000 |
| 3 → 4 | 1,000 | 3,000 |
| 4 → 5 | 1,000 | 4,000 |
| 5 → 6 | 1,000 | 5,000 |
| 6 → 7 | 1,000 | 6,000 |
| 7 → 8 | 1,000 | 7,000 |
| 8 → 9 | 1,000 | 8,000 |
| 9 → 10 | 1,000 | 9,000 |
| 10 → 11 | 1,000 | 10,000 |
| 11 → 12 | 1,000 | 11,000 |
| 12 → 13 | 1,000 | 12,000 |
| 13 → 14 | 1,000 | 13,000 |
| 14 → 15 | 1,000 | 14,000 |
| 15 → 16 | 1,000 | 15,000 |
| 16 → 17 | 1,000 | 16,000 |
| 17 → 18 | 1,000 | 17,000 |
| 18 → 19 | 1,000 | 18,000 |
| 19 → 20 | 1,000 | 19,000 |

> PF2e Remaster uses a flat 1,000 XP per level. XP resets to 0 after each level-up in some tables — this project uses cumulative tracking. Both are valid; the save block uses cumulative.

---

## 🎯 PLAYER LEVEL-UP PROCEDURE

**Trigger:** Player's cumulative XP crosses the next threshold.

**Step 1 — Announce immediately (inline, mid-scene if necessary):**
```
[LEVEL UP — reached Level X!]
  XP    : [current] / [next threshold]
  HP    : +[class HP + Con mod] → [new total]
```

**Step 2 — Apply or present choices based on `player.leveling_mode` (NOT `companion_leveling_mode` — that field governs companions in the procedure below):**

**AUTO mode** (player opted in; preset builds NO LONGER auto-default to AUTO):
```
Apply all choices silently from the build map (KM_Builds_X.md row for this level):
  • Feats      : apply [PICK] feat from build map — announce inline
  • Skill inc  : apply class default signature skill
  • Ability boosts (5/10/15/20): apply in build-map priority order
  • Spell slots: apply per class table automatically
Format: append to the level-up block from Step 1 —
  Feat: [Feat Name] (auto — build map)
  Boost: [Stat] +2 → [new score]  (at L5/10/15/20 only)
Skip Step 3.
```

**ASK mode** (default when CUSTOM build; or player switched with `/mode ask`):
```
Present choices with ★ build-map recommendation marked:
  • Ability boosts (at levels 5, 10, 15, 20): four +2 boosts — list options, mark ★ priority
  • Skill increase: list eligible skills
  • Class feat: present 3–5 options from build file (see KM_Builds.md → sub-file), mark ★ pick
  • General/skill feat: at even levels
  • Ancestry feat: at 1, 5, 9, 13, 17
  • Spell slot increases: if caster, new slots per class table
```

**MANUAL mode** (player-initiated; switched with `/mode manual`):

When the XP threshold is crossed in MANUAL (or ASK) mode, the DM outputs the deferral prompt — NOT the full menu immediately:

```
[LEVEL UP — reached Level X!]
  XP : [current] / [next threshold]  (carry: [remainder])
  HP : +[X] (pending — applied when you confirm)

Level now or save it for later?
  1. Level now — show me the full menu
  2. Later — I'll type .level when I'm ready
```

If player picks **1**: fire the full menu in the next response (all choice points, `[AUTO would pick: …]` annotations on every item).
If player picks **2**: set `level_up_available: true` and continue the scene. Fire the full menu when player types `.level`.

**⛔ .fail 29 fires when:** threshold crossed and DM outputs nothing — no notification, no deferral prompt, just continues narrating. Offering the deferral prompt is correct behavior, not a violation.

Display ALL available options. For every choice point, also surface an inline
`[AUTO would pick: X — reason]` annotation so the player has a default to compare
against or accept. Player may take the auto pick, pick anything else, or ask
for more info. Format:
```
CLASS FEAT (Level 4) — choose one:
  [1] Attack of Opportunity        — Reaction, strike a foe that triggers
  [2] Reactive Shield              — Raise shield as reaction on hit
  [3] Sudden Charge                — Stride + Strike in 1 action  [AUTO ★]
  [4] Double Slice                 — Two Strikes in 1 action
  [AUTO would pick: 3 Sudden Charge — matches Dual Slice Fighter build's mobility priority]
  Type a number, or ASK for more detail on any option.
```
Same `[AUTO would pick: …]` annotation format applies to ability boosts,
skill increases, ancestry feats, and spell prep. Never withhold auto's choice
in MANUAL — the point of the mode is to see every option **and** know which
one auto would take.

**Step 3 — Confirm with player before continuing scene. (ASK/MANUAL only — skip in AUTO.)**

**⛔ The level-up menu fires in the SAME response as the XP-threshold crossing.**
Do not announce *"level-up available"* in one response and then continue the
scene without the menu, intending to fire it later. The menu MUST be in the
same response as the threshold cross. Splitting them = `.fail 29`.

If the player wants to defer the level-up choice, they will say so in their
next input. The DM's job is to present the choices the moment the threshold
is crossed, not to wait for the player to request them.

**Step 4 — Fire ALL companion level-ups simultaneously (see below).**

> **Violation:** `.fail 29` if companions are not leveled in the same response as the player.

---

## 🤖 COMPANION LEVEL-UP PROCEDURE

**Rule:** ALL companions level up simultaneously with the player. No exceptions. See KM_DMRules.md § COMPANION LEVEL-UP.

**Leveling mode source:** Read `game_options.companion_leveling_mode` (NOT `player.leveling_mode`). Default = AUTO. Player and companions ALWAYS use independent fields — applying the player's mode to companions = `.fail 6` (rule applied incorrectly).

**Leveling modes:**
- **AUTO** (default): DM applies choices from build maps silently, announces inline
- **ASK**: DM presents choices to player for each companion
- **MANUAL**: Player makes all choices — same as ASK but player-initiated

**Required output format:**
```
[LEVEL UP — Amiri → Level X]
  HP: +[X] → [total]
  New feature: [auto feature if any]
  Feat: [feat name from build map]
[LEVEL UP — Linzi → Level X]
  HP: +[X] → [total]
  ...
[All active companions listed]
```

---

## 🔗 COMPANION LEVELING FILE ROUTER

| Companions | Source File | Notes |
|------------|-----------|-------|
| 1–12 (CRPG roster) | KM_Companions_Scaled.md | Scaled stat blocks at key levels |
| 1–12 auto-level rules | KM_DMRules.md | Generic class auto-level procedure |
| 1–12 build file lookup | KM_Companions_Builds.md | Maps each companion to KM_Builds_A–M.md |
| 13–25 (Wrath companions) | KM_Companions_Leveling.md (stubs) | Use generic class auto-level from KM_DMRules.md |
| 26–30 (extended) | KM_Companions_Builds.md | Build file lookup → KM_Builds_A–M.md |
| 31–54 (iconics) | KM_Companions_Leveling.md | Full L1–20 leveling maps |
| 55–73 (new iconics) | KM_Companions_Leveling.md (stubs) | Use generic class auto-level from KM_DMRules.md |

---

## 📋 GENERIC CLASS AUTO-LEVEL (for companions without full maps)

When a companion has no full leveling map, apply these defaults at each level:

1. **HP:** Class base HP + Con modifier
2. **Proficiency increases:** Per class table (martial = expert at 5, master at 13; caster = expert at 7, master at 15)
3. **Ability boosts (5/10/15/20):** Primary stat → secondary stat → CON → tertiary stat
4. **Class feat:** Highest-rated feat for the companion's role from the class feat list
5. **Skill increase:** Class's signature skill → Perception → secondary skill
6. **Spell slots (casters):** Per class table, prepare highest-level options available

> **Ability boost priority by archetype:**
> - Martial melee: STR → CON → DEX → WIS
> - Martial ranged: DEX → STR → CON → WIS
> - Full caster (divine/occult): WIS or CHA → CON → DEX → INT
> - Full caster (arcane/primal): INT or WIS → CON → DEX → CHA
> - Skill monkey: DEX → INT → WIS → CHA

---

*KM_Leveling.md — Kingmaker PF2e Text Adventure | Level-Up Procedures v1.0*
