# KINGMAKER — PRE-PROLOGUE XP AWARDS
## KM_PrePrologue_XP.md | Referenced by: KM_PrePrologue_Paths_QT.md, KM_PrePrologue.md, KM_PrePrologue_Paths.md

> **⛔ DM: Award each condition inline using the XP block format from KM_DMRules.md the moment it is met.** All awards stack unless marked mutually exclusive. Check this full table at scene end for any conditions met that were not awarded mid-scene. Canon reference: KM_DMRules.md § PF2e CANON REFERENCE.

---

## ⭐ COMPLETE XP AWARD TABLE (20 conditions)

### Combat outcomes (mutually exclusive with "Never Drew Weapon")

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Won Combat — 3v1** | +300 | Path F resolved with player standing. Award when combat ends. |
| **Won Combat — Duel** | +180 | Path G resolved with player standing. Award when duel ends. |
| **Coward Exposed (no real combat)** | +80 | Path K — Malak drew and flinched. No full combat occurred. |

### Non-combat mastery

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Never Drew Weapon** | +150 | Scene resolves by any non-combat path AND player never drew or equipped a weapon at any point. Award at scene end. Mutually exclusive with combat XP. |
| **Never Used the Invitation** | +100 | Player resolved the gate scene entirely without presenting Jamandi's letter — by any path. Letter was never shown to Malak, never used as leverage, never mentioned. Award at scene end. Stacks with all other conditions. |
| **Crowd Dispersed Peacefully** | +50 | Scene ended with no civilian taking damage, no panic, no injuries among drivers/pilgrims/vendors/water boy. Crowd departed on their own timing, not fleeing. |

### Malak resolution paths

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Malak Arrested By His Own Men** | +200 | Biggs unslings manacles and detains Malak (Path E) because of player action. Biggs acting on his own without player prompting does not count. |
| **Malak Trapped — Cannot Bolt** | +125 | Player closes Malak's escape before the bolt condition triggers: blocking the road, Biggs/Wedge flanking on player's instruction, or cornering him against the gate. Must occur before Malak attempts to flee. |
| **Archers Fire on Malak** | +250 | Path V completed — wall archers turned on Malak by player action. |
| **Voice Mimic Succeeded** | +50 | Path V atmosphere bonus — player successfully mimicked Malak's voice (Deception check) and Malak's Fear state triggered immediately. `malak_voice_mimicked = TRUE` in save block. |
| **Mercy — Malak Spared** | +75 | Player deliberately chose not to kill or arrest when the situation allowed either. Must be an active choice stated by the player — letting Malak walk away from lethal force without coercion. Opposite path: if Malak was killed or arrested, this does NOT award. |
| **No Archers Killed** | +50 | Resolved Path V or any archer-engagement without killing any archer — archers stood down, switched sides, or fled. |

### Intelligence / discovery

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Directive Two Uncovered** | +125 | Player discovered the gate-window conspiracy — crowd intel, examine on Malak's parchment, or logical deduction from the shakedown being cover for something else. Flag: `directive_two_uncovered = TRUE`. |
| **Parchment Source Identified** | +100 | Player traced the bribe parchment to its origin (Pitax or Surtova or other). Must be correct per KM_Malak_Jail.md. Flag: `parchment_source != "unknown"`. |
| **Micro-Tell Caught** | +75 | Player spotted a non-obvious body-language slip (Tartuccio's table, Malak's flinch, Biggs's jaw tension) via Recall Knowledge, Perception, or Sense Motive and the DM confirms. Passive overhear does not count — must be an active call. |
| **Malak's Coin Purse Assessed** | +30 | Player examined the purse, noted the weight/origin/denomination of the coin. Flag: `malak_coin_purse_assessed = TRUE`. |

### Allies earned

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Biggs and Wedge Both Side With Player** | +150 | Both guards reach Drift 3. Requires distinct player actions that moved each — winning one by default of the other does not count. |
| **Crowd Sides With Player** | +100 | Crowd attention reaches ACTIVE and at least one member (driver, pilgrim, vendor, water boy) makes a visible act of support — spoken, gestural, or drifting toward the player. |
| **Kesten Allied** | +75 | Kesten Garess reached the gate, met the player, and actively took the player's side — searched Malak, delivered evidence, or stood against the conspiracy on the player's testimony. `kesten_sided_with_player = TRUE`. Stacks with Biggs/Wedge. |
| **Kassil Allied** | +75 | Kassil Aldori arrived during the scene, met the player, and took the player's side — either publicly or in private word. `kassil_sided_with_player = TRUE`. Stacks with Kesten. |

### Side quests / sub-paths

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Five Seekers Freed by Player** | +125 | Jail detour taken (KM_Malak_Jail.md) — player personally freed all five jailed seekers before continuing to the feast. `five_seekers_freed_by_player = TRUE`. If Jamandi freed them later, this does NOT award — player action required. |
| **Malak Broke First (Confession)** | +75 | Malak confessed under pressure without player striking, coercing by threat of arrest, or drawing a weapon. Talk-driven collapse. `malak_broke_first = TRUE`. |

### ⛔ NEW — Gate held by player

| Condition | XP | Trigger |
|-----------|-----|---------|
| **Gate Re-Guarded — Forced Return** | +150 | Player forced Malak or the guards back to their post. Counters the Directive Two gate window. Example: ordering Malak "Your post is there. Stand it." and he complies; or forcing Biggs/Wedge to plant at the gate despite Malak pulling them. `gate_remanned_by = "malak" \| "biggs" \| "wedge"`. |
| **Gate Held by Player Personally** | +150 | Player physically ran past the three guards and took up the guard post themselves — standing at the gate, checking arrivals, challenging entrants. Even briefly. This also triggers the Hero Point "Gate / post held by player personally" from KM_HeroPoints.md. Flag: `gate_remanned_by = "player"`. |

Both forms stack with **Directive Two Uncovered** (player saw the window AND closed it). They are mutually exclusive with each other unless the player first held the gate and then forced a guard to relieve them — in which case both fire.

---

## 📊 MAXIMUM POSSIBLE XP TOTALS

**Non-combat full sweep** (no weapon drawn, every ally earned, every intel found, gate personally held, Malak spared and broken, crowd and seekers handled):
- Never Drew Weapon +150
- Never Used Invitation +100
- Crowd Dispersed Peacefully +50
- Malak Trapped +125
- Archers Fire on Malak +250 (if player chose this resolution)
- Mercy — Malak Spared +75
- No Archers Killed +50
- Directive Two Uncovered +125
- Parchment Source Identified +100
- Micro-Tell Caught +75
- Coin Purse Assessed +30
- Biggs and Wedge Allied +150
- Crowd Sides with Player +100
- Kesten Allied +75
- Kassil Allied +75
- Five Seekers Freed +125
- Malak Broke First +75
- Gate Held by Player Personally +150
- Voice Mimic +50 (if Path V)

**Maximum possible (non-combat, diplomatic mastery):** ≈ **+1,930 XP**

**Maximum possible (combat-driven, 3v1 path):** Won 3v1 +300 + most non-combat conditions (invitation, crowd, allies, intel, gate) ≈ **+1,700 XP**

The XP bands are wide on purpose — a skillful non-combat run should out-earn a brute-force combat run, because this is Kingmaker and the Stolen Lands reward cleverness. Crossing 1,500 XP in the Pre-Prologue means you enter the Prologue within one scene of Level 2.

---

## 🚨 XP AWARD VIOLATIONS

- Awarding combat XP AND Never-Drew-Weapon XP: `.fail 21` + mathematical impossibility.
- Awarding Malak Arrested XP when Biggs acted without player prompting: `.fail 9` (fabricated cause).
- Awarding Mercy XP when Malak was arrested or killed: `.fail 9` (flag contradicts).
- Awarding Gate Held XP without a save-block flag set to `player`: `.fail 9`.
- Awarding any XP at scene end without listing which conditions fired: `.fail 21`.

---

*KM_PrePrologue_XP.md — Kingmaker PF2e Text Adventure | Pre-Prologue XP Award Table v2.0*
*20 XP conditions. Combat outcomes + non-combat mastery + Malak resolutions + intel + allies + side quests + gate-guard tracking.*
