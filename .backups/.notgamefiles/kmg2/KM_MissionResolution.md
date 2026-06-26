# KINGMAKER — MISSION RESOLUTION SYSTEM
## KM_MissionResolution.md | Referenced by: KM_Rearguard.md

> **DM:** Load this file when resolving any `.scout` or `.delegate` mission.
> Defines deployment costs, skill floors, the two-phase resolution loop, injuries, gear loss, and rewards.
> Companion skill modifiers → `KM_Companions_Scaled.md`. Levels → `KM_Companions_Leveling.md`.
> `expedition_funds`, `overflow`, and `injury_status` live in the save block.

---

## I. DEPLOYMENT COSTS

**Gold Cost:**
> (PL × 100) + (Members × PL × 50) × Distance Multiplier

| Distance | Multiplier |
|---|---|
| 1–3 Hexes (Inner Circle) | ×1 |
| 4–6 Hexes (The Wilds) | ×1.5 |
| 7–10 Hexes (Deep Frontier) | ×2 |
| 11+ Hexes (Edge of Map) | ×3 |

Deduct from `expedition_funds` at departure. If funds are insufficient, Kesten warns the player before confirming.

**Plot Armor** — Spend **1 Hero Point** OR **5 Overflow** before departure:
- Prevents permanent death this mission
- +2 bonus to all Phase 1 and Phase 2 rolls

**Skill Boost** — Spend **1 Hero Point** at assignment:
- Treat one companion as Expert in the primary skill for this mission only
- No effect if companion is already Expert or Master rank
- Does not reduce the gold cost

---

## II. SCOUTING FLOOR

> **⛔ Check this BEFORE rolling. If the skill pool does not meet the floor, the mission is an Automatic Failure — gold consumed, team returns in 3 days with no intel.**

| Region | Distance | Minimum Skill Pool |
|---|---|---|
| Inner Circle | 1–3 Hexes | +5 |
| The Wilds | 4–6 Hexes | +10 |
| Deep Frontier | 7–10 Hexes | +15 |
| Edge of Map | 11+ Hexes | +20 |

---

## III. SKILL POOL CALCULATION

**Step 1 — Leader:**
The companion with the highest modifier in the primary skill leads. Base pool = their full modifier.

**Step 2 — Support (each additional companion):**
| Proficiency in primary skill | Bonus |
|---|---|
| Master or Legendary | +3 |
| Expert | +2 |
| Trained | +1 |
| Untrained | +1 |

**Step 3 — Total:**
Leader modifier + all support bonuses = Skill Pool.

*Example: Scout (Perception). Ekundayo +16 leads. Merisiel +10 trained assists.
Pool = 16 + 1 (trained) + 1 (body) = +18.*

**Combat missions** use the combat pool instead:
- Sum of all assigned companions' current levels + martial bonus (+2 per Fighter/Barbarian/Ranger/Champion/Monk/Magus/Swashbuckler/Gunslinger)
- Pool = (total levels + martial bonuses) ÷ 2, rounded down

---

## IV. MISSION TYPES & PRIMARY SKILLS

| Mission Type | Primary Skill | Notes |
|---|---|---|
| Scout / Recon | Perception | Intel level tied to outcome tier |
| Infiltrate / Steal | Stealth | Failure = detected; injuries possible |
| Negotiate / Parley | Diplomacy | Failure = no deal; no injury risk |
| Investigate / Research | Society or Lore | Failure = no intel returned |
| Wilderness Gather | Survival | Partial = half yield |
| Rescue / Retrieve | Athletics | Failure = target not recovered |
| Clear / Patrol | Combat | See combat pool above |
| Ambush / Raid | Combat + Stealth | Failure = injuries + retreat |

---

## V. PHASE 1 — SKILL CHALLENGE

**Roll:** 1d20 + Skill Pool vs Phase 1 DC (set by region and mission difficulty below).

| Region | Skill DC Range | TL Base |
|---|---|---|
| Inner Circle | 12–15 | 15 + PL |
| The Wilds | 16–19 | 18 + PL |
| Deep Frontier | 20–23 | 22 + PL |
| Edge of Map | 24–28 | 25 + PL |

DM sets DC within the range based on mission specifics (ambush risk, terrain, enemy alertness). DC is never shown to the player.

**Phase 1 Outcomes:**

| Result | Effect on Phase 2 |
|---|---|
| Success | **Tactical Advantage** — +4 to Combat Roll |
| Failure | **Ambushed** — −4 to Combat Roll |
| Critical Failure (fail by 10+) | Team **Severely Injured** regardless of Phase 2 outcome |

Non-combat missions (Negotiate, Investigate, Gather, Rescue) skip Phase 2 entirely — Phase 1 result IS the outcome. Use the outcome tier table in Section VI, comparing roll vs DC.

---

## VI. PHASE 2 — COMBAT

**Roll:** 1d20 + Combat Pool ± Phase 1 Modifier vs Threat Level.

Threat Level = region base (from table above) ± DM adjustment for specific enemies.

| Result vs TL | Outcome | Physical Status |
|---|---|---|
| Win by 10+ | **Crushing Victory** | Healthy |
| Win by 1–9 | **Pyrrhic Victory** | Injured (1 companion — roll severity) |
| Loss by 1–5 | **Tactical Retreat** | Mission fails; Severely Injured |
| Loss by 6+ | **Disaster** | Mission fails; Severely Injured + Gear Loss |

---

## VII. OUTCOME TIERS (non-combat missions)

| Roll vs DC | Tier | Effect |
|---|---|---|
| +10 or better | **Critical Success** | Full reward + 1 Overflow bonus |
| +1 to +9 | **Success** | Full reward |
| −1 to −4 | **Partial** | Half reward; no injuries |
| −5 to −9 | **Failure** | No reward; 1 companion injured (roll severity) |
| −10 or worse | **Critical Failure** | No reward; all injured (min Moderate); Gear Loss |

**Critical Success bonus (DM picks one):**
- Scout: Intel upgrades to FULL + 1 bonus detail (hidden cache, trap, patrol timing)
- Gather: +50% yield
- Combat clear: area secured +1 extra day
- Diplomacy: NPC attitude improves one step; future negotiations +2
- Any: mission completes 1 day early + **+1 Overflow**

**Partial failure setbacks (no injuries):**
- Scout: BASIC intel only
- Gather: half resources returned
- Combat: enemies driven back but not cleared; location still contested
- Diplomacy: talks stall; retry in 3 days, no cost refund

---

## VIII. INJURY SYSTEM

**On Failure / Pyrrhic Victory:** Roll 1d4 to determine which companion is injured (1 = first named, 2 = second, etc.). Roll severity below.

**On Critical Failure / Disaster / Phase 1 Critical Fail:** All companions injured. Minimum severity = Moderate.

**Severity roll (1d4):**

| Roll | Tier | Name | Recovery | Notes |
|---|---|---|---|---|
| 1 | 1 | Minor | 1–2 days | Present in camp; banter only. No combat, no missions. |
| 2–3 | 2 | Moderate | 3–5 days | Resting; unavailable for all party use. |
| 4 | 3 | Severe | 7–10 days | Bedridden; can be reduced by Medicine. |

**Critical Failure escalation:** Add one tier to each injury (Minor → Moderate, Moderate → Severe, Severe → Critical).

| Tier | Name | Recovery | Notes |
|---|---|---|---|
| 4 | Critical | 14 days (max) | As Severe + triggers Gear Loss roll. |

**Recovery options:**
- **Medicine check (DC 18):** Once per day per companion. Success = −1 recovery day.
- **Healer's kit (5 gp):** Auto −1 day, no check.
- **Restoration spell:** Removes all remaining recovery days instantly.

**Save block entry:**
```json
{
  "companion": "Merisiel",
  "injury_tier": 2,
  "injury_name": "Moderate",
  "recovery_day": 11
}
```

---

## IX. GEAR LOSS

Triggered on **Critical Failure** or **Disaster**. Roll 1d4 for the most severely injured companion:

| Roll | Loss |
|---|---|
| 1 | Armor damaged — −1 AC until repaired (50 gp) |
| 2 | Weapon degraded — −1 attack until repaired (25 gp) |
| 3 | Consumables lost — lose 1d4 potions or scrolls |
| 4 | Gold lost — lose 1d10 × 5 gp from expedition funds |

Roll once only. Multiple injuries: highest tier companion takes the roll. Ties: DM picks.
*"They came back lighter than they left."*

---

## X. REWARDS

| Reward Type | What It Gives |
|---|---|
| **Waypoint** | New location added to map with BASIC intel; can be upgraded via scout follow-up |
| **Resources** | 1d4 × (PL × 10) gp worth of materials (lumber, ore, provisions, valuables) added to `expedition_funds` |
| **Overflow** | +1 Overflow token added to save block per mission; +2 on Critical Success |

**Overflow** is a strategic reserve earned from exceptional missions.
- Spend **5 Overflow:** Grant Plot Armor to next deployment
- Spend **2 Overflow:** Reduce one companion's injury recovery by 3 days
- Spend **1 Overflow:** Re-roll one Phase 1 or Phase 2 roll (keep second result)

---

## XI. INTEL LEVELS (Scout Missions)

| Outcome Tier | Intel Returned |
|---|---|
| Critical Success | FULL + 1 bonus detail |
| Success | FULL |
| Partial | BASIC |
| Failure | NONE |
| Critical Failure | NONE + companions injured |

**BASIC intel:** Terrain type, rough enemy presence (LOW/MODERATE/HIGH/EXTREME), and whether area is safe to enter.
**FULL intel:** Everything in BASIC + patrol routes, notable landmarks, resource nodes, and ambush risk.

---

## XII. RETURN REPORT FORMAT

```
╠═════════════════════════════════════════════════════════════╣
║  CASUALTIES                                                  ║
║  [Companion] — [Injury name], off duty [X] days             ║
╠═════════════════════════════════════════════════════════════╣
║  GEAR LOSS    [item lost — or NONE]                         ║
╠═════════════════════════════════════════════════════════════╣
║  REWARD       [Waypoint / Resources Xgp / +X Overflow]      ║
╚═════════════════════════════════════════════════════════════╝
```

Omit CASUALTIES block if no injuries. Omit GEAR LOSS if none.

---

*KM_MissionResolution.md — Kingmaker PF2e Text Adventure | Mission Resolution v2.0*
*Merged: Vanguard Expedition System (v2) + original resolution rules*
*Supersedes: class-based Delegation Skill Table and ★ scout ratings in KM_Rearguard.md*
