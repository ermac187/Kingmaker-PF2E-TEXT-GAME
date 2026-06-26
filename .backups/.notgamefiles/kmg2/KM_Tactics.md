# KINGMAKER — COMPANION TACTICS SYSTEM
## KM_Tactics.md | DA:O / EMAT-Style Role-Based Companion AI | Active: All Chapters

> **DM:** In combat, run each companion's slots top to bottom each turn. First condition TRUE fires — stop scanning. Do not improvise around filled slots. Player changes any slot with `.tactics [companion] [slot] [ability]`. Switch strategy mode with `.strategy [companion] [mode]`.

---

## SYSTEM MECHANICS

| Slot Label | When It Fires |
|------------|---------------|
| **S** | OnCombatStart — round 1 only, fires once before slot scanning |
| **0** | Reaction — fires off-turn when trigger condition is met |
| **1–7** | Priority order — scanned top to bottom each turn |
| **D** | Default — fires when no other slot condition is true |

**Condition syntax:**
- `AND` — both must be true: `Ally HP ≤ 20% AND self HP > 30%`
- `OR` — either: `2+ allies HP ≤ 50% OR single ally HP ≤ 25%`
- `NOT` — inverse: `NOT raging`, `NOT buff active`
- `[MUTEX: ability]` — slot skipped if that ability is already active

**Strategies:** Named mode bundles that override specific slots. Active strategy shown in tracker. Base slots run for anything not overridden by the strategy.

---

## ROLES

### ROLE: HEALER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — position + pre-buff |
| 0 | Ally drops to 0 HP (reaction) | [DEATH SAVE HEAL] |
| 1 | Ally HP ≤ 20% AND self not dying | [EMERGENCY HEAL] — 2 actions, max rank |
| 2 | Ally has dying / paralyzed / blinded | [CLEANSE] |
| 3 | 2+ allies HP ≤ 50% OR single ally HP ≤ 25% | [BURST HEAL] — 3 actions, area |
| 4 | Ally HP ≤ 50% | [PRIMARY HEAL] — 1–2 actions |
| 5 | NOT buff active [MUTEX: PARTY BUFF] | [PARTY BUFF] — 1 action |
| 6 | Self HP ≤ 25% | [SELF-PRESERVE] |
| D | Default | [CANTRIP] |

---

### ROLE: STRIKER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — activate power state + close distance |
| 0 | Enemy provokes (reaction) | [AoO STRIKE] |
| 1 | NOT in power state | [ACTIVATE] — 1 action |
| 2 | Enemy flat-footed OR flanked | [POWER ATTACK] — 2 actions |
| 3 | 2+ enemies adjacent AND power state active | [AREA ATTACK] — 2 actions |
| 4 | 1st or 2nd attack this turn | [STRIKE] — 1 action |
| 5 | Would be 3rd attack (MAP −10) | [ALTERNATE] — 1 action |
| D | Default | [STRIKE] |

---

### ROLE: CONTROLLER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — highest-priority control on biggest threat |
| 0 | Enemy casts AND reaction available | [COUNTERSPELL] |
| 1 | 3+ enemies grouped within 30 ft AND slot available | [AREA CONTROL] — 2–3 actions |
| 2 | Enemy caster/commander visible AND not controlled | [SINGLE CONTROL] — 2 actions |
| 3 | Ally outnumbered 2:1 OR flanked | [AREA DEBUFF] — 2 actions |
| 4 | Spell slots spent | [CANTRIP CONTROL] |
| D | Default | [DAMAGE CANTRIP] |

---

### ROLE: TANK

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — Raise Shield + move adjacent to most vulnerable ally |
| 0 | Enemy attacks adjacent ally (reaction) | [SHIELD BLOCK / INTERPOSE] |
| 1 | Enemy moves through threatened space | [AoO STRIKE] |
| 2 | Ally targeted AND self adjacent | [PROTECT] — Shield raise + absorb |
| 3 | Ranged enemy unengaged AND no melee threat | [CLOSE + ENGAGE] |
| 4 | Self HP ≤ 40% AND no ally critical | [SUSTAIN] |
| D | Default | [RAISE SHIELD + STRIKE] |

---

### ROLE: SUPPORT/BUFFER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — primary buff immediately |
| 0 | Ally drops (reaction) | [EMERGENCY REACTION] |
| 1 | NOT primary buff active [MUTEX: PRIMARY BUFF] | [PRIMARY BUFF] — 1 action |
| 2 | NOT secondary buff active [MUTEX: SECONDARY BUFF] | [SECONDARY BUFF] — 1 action |
| 3 | Priority enemy NOT debuffed | [DEBUFF] — 1–2 actions |
| 4 | Buff needs sustain (free action available) | [SUSTAIN] — free action |
| D | Default | [CANTRIP or BASIC ATTACK] |

---

### ROLE: SCOUT/SKIRMISHER

| Slot | Condition | Action |
|------|-----------|--------|
| S | Round 1 | [OPENER] — mark priority target + position at range |
| 0 | Enemy closes to melee (reaction) | [DISENGAGE REACTION] |
| 1 | No priority target marked | [MARK TARGET] — 1 action |
| 2 | Priority target in range AND self not in melee | [STRIKE PRIORITY] — 1–2 actions |
| 3 | Enemy closes to melee | [STEP BACK + STRIKE] |
| 4 | No clear shot OR flanked by 2+ | [REPOSITION] |
| D | Default | [STRIKE] |

---

## COMPANION ASSIGNMENTS

### AMIRI — Striker
| Slot | Filled |
|------|--------|
| S OPENER | Rage + Stride toward highest-threat enemy |
| ACTIVATE | Rage |
| POWER ATTACK | Furious Blow (Giant Instinct, 2 actions) |
| AREA ATTACK | Giant's Swing — 2+ adjacent AND raging |
| ALTERNATE (MAP−10) | Intimidating Glare — Demoralize 1 action |
| AoO | Strike — enemy in reach moving away |
| OVERRIDE | Weapon = oversized bastard sword. Not an axe. Never. |

**STRATEGIES:** `RAMPAGE` — Area attack fires if 2+ adjacent, no flat-footed check; ignore MAP on slot 5, keep striking. | `CONTROLLED` — Rage only if HP > 50%; step back instead of MAP strike. | `BODYGUARD` — Strike enemies targeting allies first over optimal positioning.

---

### LINZI — Support/Buffer + Controller
| Slot | Filled |
|------|--------|
| S OPENER | Inspire Courage immediately (1 action) |
| PRIMARY BUFF | Inspire Courage [MUTEX: Inspire Courage active] |
| SECONDARY BUFF | Inspire Defense when party average HP < 60% |
| SUSTAIN | Cackle free action — maintain Inspire each turn |
| DEBUFF | Fear rank 1 on enemy caster priority |
| EMERGENCY | Heal if ally < 25% AND no healer has acted |
| OVERRIDE | Never drop Inspire Courage while allies are attacking. Notebook between turns only. |

**STRATEGIES:** `CHRONICLE` — Default. Inspire + sustain + observe. Minimal slot use. | `FULL SUPPORT` — Use Fear, Silence, all slots freely. | `EMERGENCY BARD` — All actions to healing if party healer is down.

---

### HARRIM — Healer (Warpriest)
| Slot | Filled |
|------|--------|
| S OPENER | Bless rank 1 + move to melee line |
| DEATH SAVE | Heal reaction rank 1 minimum |
| EMERGENCY HEAL | Channel Positive Energy — area, 2 actions |
| PRIMARY HEAL | Heal rank 2 — 1 action, single target |
| CLEANSE | Remove Fear |
| PARTY BUFF | Bless rank 1 [MUTEX: Bless active] |
| SELF-PRESERVE | Channel on self |
| OVERRIDE | Stays in melee. Heals from inside the fight. Will not retreat. |

**STRATEGIES:** `WARPRIEST` — Default. Melee + heal between strikes. | `PURE HEALER` — Backline only, no strikes. | `DOOM HERALD` — All slots on Harm vs undead; no healing this combat.

---

### JAETHAL — Striker (Undead)
| Slot | Filled |
|------|--------|
| S OPENER | Stride to flanking position on priority target |
| POWER ATTACK | Harm channel — area, 2 actions, when 2+ living adjacent |
| STRIKE | Rapier finesse — Sneak Attack when flanking OR target flat-footed |
| ALTERNATE (MAP−10) | Reposition for flanking angle |
| AoO | Always — any provocation in reach |
| OVERRIDE | Immune: mind/fear/death. Heals from negative energy ONLY — positive harms her. |

**STRATEGIES:** `ASSASSIN` — Single-target elimination priority. Sneak Attack every strike. | `UNDEAD WAVE` — Harm area as primary; ignore flanking, damage all living in reach.

---

### LANN — Scout/Skirmisher (Ranger)
| Slot | Filled |
|------|--------|
| S OPENER | Hunt Prey on priority target + move to elevated/distant position |
| MARK TARGET | Hunt Prey — spellcaster > commander > melee |
| STRIKE PRIORITY | Crossbow + Hunter's Edge precision |
| STEP BACK + STRIKE | Retreating Shot if enemy closes |
| REPOSITION | Move to elevation or maintain ≥ 30 ft distance |
| UTILITY | Heal via Crack Shot if ally critical AND no healer available |
| OVERRIDE | Maintains ≥ 30 ft from melee. Position before attack. |

**STRATEGIES:** `SNIPER` — Default. Max range, precision, no melee. | `SKIRMISHER` — Close range acceptable; rapid fire over positioning. | `SCOUT LEAD` — Move first each turn; no attack if repositioning used all actions.

---

### EMBER — Support/Buffer (Witch)
| Slot | Filled |
|------|--------|
| S OPENER | Evil Eye hex on highest-threat enemy (Frightened 1) |
| PRIMARY BUFF | Evil Eye hex [MUTEX: hex active on current target] |
| SUSTAIN | Cackle free action — maintain hex each turn |
| DEBUFF | Slow rank 2 on highest-threat melee AND hex already running |
| SECONDARY | Soothe if ally < 40% AND no healer has acted this turn |
| EMERGENCY | Bestow Curse on enemy that downed an ally |
| OVERRIDE | Nova = raven familiar. Not fire-adjacent. Not a fire spirit. Ever. |

**STRATEGIES:** `HEX FOCUS` — Default. Evil Eye + Cackle every turn. | `CURSE SUPPORT` — Bestow Curse primary; save hex for emergencies. | `EMERGENCY WITCH` — Soothe as primary when healer is down.

---

### DAERAN — Healer (Oracle)
| Slot | Filled |
|------|--------|
| S OPENER | Life Link focus spell (party-wide heal aura) |
| DEATH SAVE | Heal reaction rank 1 minimum |
| EMERGENCY HEAL | Heal rank 3 — 3-action burst when 2+ critical OR single at 0 HP |
| PRIMARY HEAL | Heal rank 2 — 1 action, single target |
| CLEANSE | Neutralize Poison / Remove Disease |
| PARTY BUFF | Life Link [MUTEX: Life Link active] |
| SELF-PRESERVE | Withdraw — he is not a melee combatant |
| OVERRIDE | Tracks gift costs. Does not martyr himself. |

**STRATEGIES:** `LIFE SUPPORT` — Default. Efficient slot use; Life Link as backbone. | `TRIAGE` — Emergency heals only; save all slots for critical moments. | `BATTLE ORACLE` — Offensive revelation spells primary; minimal healing.

---

### NENIO — Controller (Wizard)
| Slot | Filled |
|------|--------|
| S OPENER | Slow rank 2 on highest-action enemy |
| AREA CONTROL | Web OR Stinking Cloud — 3+ enemies grouped AND slot available |
| SINGLE CONTROL | Charm OR Confusion — enemy caster AND NOT already controlled |
| DEBUFF | Fear rank 2 on commander if no caster visible |
| CANTRIP CONTROL | Electric Arc (2 targets) when slots spent |
| SELF-PRESERVE | Blur OR Invisibility when targeted in melee AND HP < 60% |
| OVERRIDE | One sentence of tactical narration per turn max. Not a monologue. |

**STRATEGIES:** `RESEARCHER` — Default. Slow opener + systematic control; preserve slots past round 3. | `NOVA` — Spend top slots immediately rounds 1–2. | `SUPPORT MAGE` — Haste/Blur/Mirror Image on allies instead of controlling enemies.

---

### REGILL — Tank (Hellknight)
| Slot | Filled |
|------|--------|
| S OPENER | Move to cut off enemy commander escape route + Raise Shield |
| AoO | Strike — any enemy moving through threatened space |
| ENGAGE | Close to cut off retreat AND Shield raised |
| PRIORITY TARGET | Most organized / commander-type enemy |
| STRIKE | Disciplined Strike — no flourishes, no wasted actions |
| SUSTAIN | Raise Shield if HP < 40% AND no immediate strike available |
| OVERRIDE | Never breaks formation. Never chases. Holds ground. |

**STRATEGIES:** `IRON DISCIPLINE` — Default. Hold position, AoO everything, methodical. | `EXECUTE` — Close to commander and eliminate; ignore other threats. | `FORTRESS` — Full defensive; Shield always raised; strikes on AoO only.

---

### ARUESHALAE — Scout/Striker (Rogue)
| Slot | Filled |
|------|--------|
| S OPENER | Flank position OR distance if no flank available |
| MARK TARGET | Move to create flat-footed on priority target |
| STRIKE PRIORITY | Bow Strike — Sneak Attack when flat-footed OR flanked |
| SETUP | Feint if no flanking partner AND in melee range |
| STEP BACK + STRIKE | Disengage + shoot if 2+ enemies in melee with her |
| OVERRIDE | Prefers ranged. Melee only for Sneak Attack if position is safe. No unnecessary risks. |

**STRATEGIES:** `SHADOW` — Default. Ranged Sneak Attack priority; avoid melee. | `INFILTRATE` — Melee flanking with Amiri or Regill for constant Sneak Attack. | `DISRUPT` — Feint and debuff over damage; keep target flat-footed for allies.

---

### SEELAH — Tank + Healer (Paladin)
| Slot | Filled |
|------|--------|
| S OPENER | Raise Shield + move adjacent to most vulnerable ally |
| SHIELD BLOCK | Reaction — adjacent ally takes hit AND block available |
| AoO | Strike — enemy disengages from her |
| HEAL ALLY | Lay on Hands — adjacent ally ≤ 20% AND focus available |
| SUSTAIN SELF | Lay on Hands — self ≤ 35% AND no ally critical |
| SMITE | Divine Smite on highest-threat [MUTEX: smite used last 2 rounds] |
| STRIKE | Strike + Raise Shield — 2 actions |
| OVERRIDE | Always adjacent to most vulnerable ally. Moves to protect before attacking. |

**STRATEGIES:** `PALADIN` — Default. Protect + heal + measured strikes. | `CRUSADER` — Divine Smite priority; less shielding, more damage. | `SHIELD WALL` — Full defense; Shield Block every hit; strikes on AoO only.

---

*KM_Tactics.md — Kingmaker PF2e Text Adventure | Companion Tactics v1.1 (EMAT-style)*
