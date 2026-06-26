# KINGMAKER — SPLIT FORCE SYSTEM
## KM_SplitForce.md | Full-Party Tactical Combat

> **DM:** When the full party is present and encounters a large enemy force, the enemy doubles and splits. One half engages the Vanguard (player + selected companions — normal turn-by-turn combat). The other half engages the Rearguard (remaining companions — autofight, single roll resolution). Both fights happen simultaneously. The player only plays one side. This system rewards having a large party on the road and makes full-party travel feel like a military column.

---

## ⚙️ TRIGGER CONDITIONS

**Split Force activates when ALL of the following are true:**
- Party has **6+ combatants** (player + 5 or more companions)
- **Outdoor encounter** — road, camp approach, open wilderness, courtyard
- Enemy force has **4 or more combatants**
- Encounter is an **ambush or random encounter** (not a trap, not a named boss)

**Split Force does NOT activate when:**
- Encounter is indoors / dungeon (no room to flank)
- Enemy force has a named commander (Happs Bydon, scripted villain) → see **Combined Assault**
- Enemy is a single high-CR creature (boss — one group, full party)
- Player has fewer than 5 companions present
- Player types `.combined` to override

---

## 👥 FORMATION ASSIGNMENT

**These are the FIXED default assignments. Use them unless the player explicitly overrides.**

### ⚔️ VANGUARD (player's group)
| Slot | Companion | Role |
|---|---|---|
| Commander | **eRmaC** | Player |
| Striker | **Amiri** | Frontline DPS |
| Healer | **Daeran** | Mobile healing |
| Ranged | **Lann** | Ranged precision |
| Support | **Linzi** | Inspire + chronicle |
| Caster | **Ember** | Control + support |

### 🛡️ REARGUARD (autofight group)
| Slot | Companion | Role |
|---|---|---|
| **LEAD** | **Regill** | Tactical command |
| Tank | **Seelah** | Shield wall |
| Healer | **Harrim** | Sustain |
| Ranged | **Arueshalae** | Precision striker |
| Controller | **Nenio** | Area denial |
| Striker | **Jaethal** | Flanker / finisher |

**Rearguard Lead:** Highest-level Tank in the group. If no tank, highest-level companion present.

**Override commands:**
- `.rearguard [names]` — set rearguard for this encounter
- `.vanguard [names]` — set vanguard for this encounter
- `.rearguard reset` — return to the default assignments above

---

## ⚔️ COMBAT HEADER FORMAT

When Split Force activates, output this before any initiative rolls:

```
⚔️ SPLIT FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VANGUARD                   REARGUARD
eRmaC                      [Lead name]
[companion]                [companion]
[companion]                [companion]
...                        ...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAIN GROUP                 MIRROR GROUP
[enemy list]               [same type/tier]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REARGUARD MODIFIER: [show calculation]
  Base +5 | [roles] | [situation]
  Total: +[X]
DC: 10 + [enemy CR] = [DC]
ROLL: d20 +[X] vs DC [Y] → [result]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REARGUARD OUTCOME: [Clean Victory / Victory / Costly Victory / Overwhelmed]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Output the rearguard result **before** player combat begins. The player knows how their rear is holding before they engage.

---

## 🎲 REARGUARD AUTOFIGHT RESOLUTION

### Roll
`d20 + Rearguard Modifier vs DC (10 + enemy group CR)`

### Rearguard Modifier — Calculate Fresh Every Encounter

**DM: Before rolling, tally the modifier from the actual rearguard composition that session. Do not use a memorized number. Teams change.**

**Step 1 — Base**
| Always | +5 |
|---|---|

**Step 2 — Roles present** *(check the actual rearguard roster)*
| Condition | Modifier |
|---|---|
| 1 Tank (Regill, Seelah, Valerie) | +2 |
| 2+ Tanks | +3 (replaces +2, not added) |
| 1 Healer (Harrim, Tristian, Daeran, Seelah) | +2 |
| 2+ Healers | +3 (replaces +2, not added) |
| Striker (Amiri, Jaethal, Arueshalae, Lann) | +1 |
| Controller (Nenio, Ember, Linzi) | +1 |

**Step 3 — Situation**
| Condition | Modifier |
|---|---|
| Rearguard outnumbers their enemy group | +2 |
| All rearguard at full HP (rested) | +1 |
| Any rearguard member below half HP | −2 |
| Rearguard outnumbered (enemy 2× their count) | −3 |

**Step 4 — Show the math in the combat header**

Example calculation for Regill / Seelah / Harrim / Arueshalae / Nenio / Jaethal vs CR 4 bandits:
```
Base +5 | 2 tanks +3 | 2 healers +3 | striker +1 | controller +1 | rested +1
Total: +14 vs DC 14 → needs a 1 to fail
```

Example for Linzi / Ember / Nenio (no tank, no healer) vs same:
```
Base +5 | controller +1 | controller +1 | rested +1
Total: +8 vs DC 14 → needs a 6+ to win clean
```

**The composition determines the outcome. Show the math every time.**

### Outcome Table
| Roll vs. DC | Result | Consequence |
|---|---|---|
| DC +5 or better | **Clean Victory** | No casualties. Mirror group eliminated. Rearguard joins Vanguard after combat ends. |
| Meets DC | **Victory** | One companion at low HP (≤ 1/4 max). One healing resource spent. Mirror group eliminated. |
| DC −1 to −4 | **Costly Victory** | One companion at 0 HP (stabilized, not dead). Two healing resources spent. Mirror group eliminated. |
| DC −5 or worse | **Overwhelmed** | Rearguard collapses — see below. |

### Rearguard Overwhelmed
If the rearguard fails by 5+:
- All rearguard companions enter the **main combat** at half HP
- Mirror group **survivors** (roll 1d4 — that many remain) join the main combat
- The player now faces a merged, chaotic engagement
- Announce this as a mid-round event: *"The rearguard line breaks — [lead companion] is down, and the flanking group is coming through."*
- This is the designed failure state. It makes the choice of who to put in the rearguard matter.

---

## ⚡ VICTORY REINFORCEMENT

**When one group defeats their enemies before the other group is done, they move to assist.**

This is the standard military follow-through — a group that clears its fight doesn't stand idle while the other line still has enemies.

### Vanguard Finishes First

If the Vanguard defeats the main group before the Rearguard autofight has resolved:

**Effect:** Upgrade the Rearguard outcome by one tier.
| Without reinforcement | With Vanguard assist |
|---|---|
| Overwhelmed | → Costly Victory |
| Costly Victory | → Victory |
| Victory | → Clean Victory |
| Clean Victory | → Clean Victory (no change needed) |

Narrate: *"The main group goes down. [Companion] and the vanguard push through — hitting the mirror force from behind. The line collapses."*

**Timing rule:** This applies if the DM judges the Vanguard fight ended early (within 3–4 rounds). A long, grinding Vanguard fight means the Rearguard already resolved on its own.

---

### Rearguard Finishes First (Clean Victory Only)

If the Rearguard's autofight resolves as a **Clean Victory** (roll exceeded DC by 5+), they are in condition to push up.

**Effect:** Roll 1d4. That many Rearguard companions enter the Vanguard fight as reinforcements at the start of the next round. Player chooses which companions arrive.

**They arrive at full HP** — Clean Victory means no serious injuries.

Narrate: *"Regill's line is clean. They're coming through — [names] push up behind you."*

**If Rearguard outcome was Victory or Costly Victory:** Survivors may still assist, but arrive at low HP. DM applies −2 to their attack rolls for the remainder of combat (injured, not fresh). 1d2 companions arrive, not 1d4.

**Overwhelmed:** No reinforcement — they enter the main fight as part of the Overwhelmed collapse event (see above).

---

### The Last Few

When reinforcements arrive, they engage whichever enemies remain. They do not need to be assigned — they target the nearest living enemy. The Vanguard player may issue them a command as a free action on their turn: *Hold / Flank / Press.*

If only 1–2 enemies remain when reinforcements arrive, the DM may resolve those final combatants narratively without additional rounds: *"Seelah and Jaethal come through the gap — it's over in seconds."*

---

## 🔱 COMBINED ASSAULT (Trap / Setup / Named Enemy)

Use Combined Assault instead of Split Force when:
- The encounter is a **scripted trap** or coordinated ambush from multiple directions simultaneously
- The enemy has a **named commander** (Happs Bydon, any scripted villain)
- **Siege or defense** scenario (everyone holds together)
- Player types `.combined`

**What changes:**
- Enemy force does NOT double — same total enemy count, split into two flanks by positioning
- Both Vanguard and Rearguard fight **together** — player directs both groups
- Full turn-by-turn combat, all companions active
- Player may issue orders to Rearguard each round (one order = free action): *Hold / Press / Fall back*

**Combined Assault header:**
```
⚔️ COMBINED ASSAULT — [reason: trap/named enemy/player order]
ALL COMPANIONS ENGAGED
VANGUARD: eRmaC + [list]  ←  [enemy flank A]
REARGUARD: [list]          ←  [enemy flank B]
No auto-resolution. Full combat.
```

---

## 🗺️ ENCOUNTER EXAMPLES

### Road Ambush (Split Force)
Traveling to Oleg's Trading Post. Default rearguard that session: Regill, Seelah, Harrim, Arueshalae, Nenio, Jaethal. CR 2 bandits.

```
⚔️ SPLIT FORCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VANGUARD                   REARGUARD
eRmaC                      Regill (lead)
Amiri                      Seelah
Daeran                     Harrim
Lann                       Arueshalae
Linzi                      Nenio
Ember                      Jaethal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MAIN GROUP (6)             MIRROR GROUP (6)
4 bandits                  4 bandits
1 archer                   1 archer
1 bandit leader            1 bandit leader
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
REARGUARD MODIFIER:
  Base +5 | 2 tanks +3 | 2 healers +3 | striker +1 | controller +1 | rested +1
  Total: +14
DC: 10 + 2 = 12
ROLL: d20 +14 vs DC 12 → [roll] → CLEAN VICTORY (needs only a 1 to fail)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

If Seelah and Harrim were elsewhere that session and the rearguard was Regill / Nenio / Arueshalae / Jaethal:
```
Base +5 | 1 tank +2 | striker +1 | controller +1 | rested +1
Total: +10 vs DC 12 → needs a 2+ (still comfortable, but not automatic)
```

**The math always reflects who's actually there.**

---

### Happs Bydon at Oleg's (Combined Assault — named commander)
Happs Bydon arrives with his collection crew. Named NPC present → Combined Assault.

```
⚔️ COMBINED ASSAULT — Named commander: Happs Bydon
Enemy doubled (full party present): 12 bandits total
Flank A (Happs + 5): Vanguard engages
Flank B (6 riders): Rearguard engages
Full combat. Player directs both lines.
```

Happs is a named NPC. His half is a real fight with real stakes — no autoresolution.

---

### Scripted Trap (Combined Assault — trap)
Enemies positioned on both sides of a canyon before the party enters.

```
⚔️ COMBINED ASSAULT — Trap
Party caught between two groups.
No splitting — everyone is already engaged.
Full combat. Both flanks immediate.
```

---

## 📋 POST-COMBAT REPORT

After every Split Force encounter, report both sides:

```
COMBAT COMPLETE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VANGUARD: [outcome + loot from main group]
REARGUARD: [Costly Victory — Lann at 0 HP, stabilized]
  Rearguard loot: [mirror group loot share]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL XP: [combined]
HEALING NEEDED: [resources consumed by rearguard]
```

Rearguard loot is the same tier as Vanguard loot. They earned it.

---

## ⚠️ DM RULES

1. **Roll the rearguard before asking the player anything about their combat.** The player sees the rear result first. Then they engage.
2. **Never skip the combat header.** The split must be visible — both groups, both enemy counts.
3. **Overwhelmed is a dramatic moment, not a punishment.** Narrate it. Name who went down. The arrival of survivors into the main fight should feel like a movie scene.
4. **Mirror group = same enemy type and tier.** Do not invent special elite units for the mirror group unless the encounter specifically calls for flanking specialists.
5. **Companions can die in the rearguard autofight** only if Overwhelmed AND a subsequent bad roll in the merged combat kills them. The autofight itself only drops them to 0 HP (stabilized). Death requires the merged combat.
6. **Full party benefit:** Having all companions together means the enemy doubles — but the rearguard handles half automatically. The system rewards full-party travel. Smaller parties fight the same enemy count but have no autofight relief.

---

## 🔗 RELATED FILES

- `KM_Tactics.md` — Companion AI tactics (what the rearguard does by role)
- `KM_CinematicCombat.md` — Cinematic resolution rules
- `KM_ArmyCombat.md` — Large-scale army combat (different from this system)

---

*KM_SplitForce.md — Kingmaker PF2e Text Adventure | Split Force System v1.0*
