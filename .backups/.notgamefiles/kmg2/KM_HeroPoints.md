# KINGMAKER — HERO POINT TRIGGER CATALOG
## KM_HeroPoints.md | Referenced by: KM_P2.txt § HERO POINT SYSTEM

> **⛔ DM: This is the AUTHORITATIVE list of Hero Point award triggers.** Check every trigger after every player input. Max 1 award per player turn — if multiple fire, pick the strongest and name it in the inline ledger. Automatic triggers outrank judgment triggers.
>
> **See KM_P2.txt § HERO POINT SYSTEM for:** award procedure, inline ledger format, overflow rules, spend rules, cap (3/3). This file holds only the trigger tables.

---

## 🟢 AUTOMATIC TRIGGERS — no DM judgment, always award

| Trigger | Award | Notes |
|---------|-------|-------|
| Session start | +1 Hero Point | On every new chat session / save-block load. If pool already full, +1 overflow. PF2e canon. Once per session. |
| Saved a named NPC's life | +1 Hero Point | Jamandi, Kesten, any named companion or story NPC. |
| Prevented a disaster | +1 Hero Point | Poison found before it killed, ambush stopped, trap discovered, assassination interrupted. |
| Natural 20 on ANY die roll | +1 Hero Point | Every natural 20, every time, no exceptions. |
| Recruited a companion | +1 Hero Point | Every new companion, automatic. |
| Defeated a named boss or major enemy | +1 Hero Point | Every named boss, automatic. |
| Completed a quest or major objective | +1 Hero Point | On quest log update to Completed, automatic. |
| 4+ player inputs without any award (safety net) | +1 Hero Point | Prevents long stretches with nothing. Reset on any award. |
| First blood in combat | +1 Hero Point | Player lands the first hit of a combat encounter. Once per fight. |
| Survived a critical hit | +1 Hero Point | Player takes a crit and stays conscious. Once per combat. |
| Companion saved from dying | +1 Hero Point | Player stabilizes or heals a companion at Dying. Separate from "saved NPC life." |

---

## 🟡 JUDGMENT TRIGGERS — one per turn max, pick the most applicable

| Trigger | Award | Notes |
|---------|-------|-------|
| Pure logic / talk-down victory | +1 Hero Point | Entire encounter resolved through social logic. Encounter must be OVER. |
| Improvised weapon — mundane object | +1 Hero Point | Non-weapon used as weapon. First use per encounter. |
| Solo encounter clear without casualties | +1 Hero Point | Resolved alone, no named allies took damage. |
| Saved multiple lives in a single scene | +1 Hero Point | 3+ story-relevant people in one scene. |
| Pure environment / terrain kill or win | +1 Hero Point | Terrain is the primary cause of the outcome. |
| Out-thought the encounter | +1 Hero Point | Non-obvious weakness identified and exploited. |
| Creative improvisation (general) | +1 Hero Point | Action not on any menu that worked. Low bar. |
| Roleplay moment | +1 Hero Point | Genuine character voice under pressure. |
| Callback to earlier scene | +1 Hero Point | Player REFERENCES a promise, NPC thread, or detail from prior session. Memory rewarded. |
| Tactical sacrifice | +1 Hero Point | Player deliberately takes damage or disadvantage to protect an ally or achieve an objective. |
| Enemy turned or recruited | +1 Hero Point | Convinced an enemy to switch sides mid-encounter. |
| Perfect information play | +1 Hero Point | Used `.examine`, Recall Knowledge, or investigation intel for a decisive advantage. |
| Genuine humor | +1 Hero Point | Made the scene funnier without breaking immersion. Low bar — DM judgment. |
| **Kept a cross-session promise** | +1 Hero Point | Player ACTED on a promise made in a prior session — not just referenced it (which is callback). Followed through on word given to an NPC, delivered a gift, returned to help, etc. Distinct from callback: callback = mention, kept promise = action. |
| **Refused a bribe or temptation** | +1 Hero Point | Integrity under pressure. Walked away from gold, power, or advantage that would have compromised an alliance, alignment, or personal code. Not the same as talk-down — this is a choice, not a resolution. |
| **Mercy over kill** | +1 Hero Point | Spared a defeated enemy when killing was easy and arguably correct. Must be a named or distinct foe. Mercy on trivial mooks does not qualify. |
| **Signature move finishing blow** | +1 Hero Point | Player declared a signature move earlier and landed the killing blow on a boss or named foe with it. Narrative combat moment. |
| **Overcame personal weakness narratively** | +1 Hero Point | Character growth: pushed through a declared phobia, curse, trauma, or weakness to act in a scene where that weakness should have stopped them. Once per weakness. |
| **Helped an NPC outside the main quest** | +1 Hero Point | Altruism: solved a civilian problem, delivered an unrelated favor, or picked up a side-quest purely to help — not for reward. |
| **Discovered a hidden truth** | +1 Hero Point | Active skill check (Recall Knowledge, Perception, examine, Investigate) that reveals plot-advancing information the DM had gated behind the roll. Passive discovery does not qualify. |
| **Gate / post held by player personally** | +1 Hero Point | Player took over a guard post, chokepoint, or watch duty themselves (e.g. ran past Malak and stood at the gate). Pre-Prologue specific but applies anywhere. See KM_PrePrologue_XP.md for the XP award that stacks with this HP. |

**Trigger priority when multiple fire in one turn:** Automatic triggers outrank judgment triggers. Among judgment triggers, pick the one that best describes the turn's defining moment. Name it when awarding — e.g. *"Hero Point — mercy over kill."* Others are acknowledged, not awarded.

---

## 🔁 HP AWARD FLOW (reminder — full procedure in KM_P2.txt)

1. Evaluate all triggers above after every player input.
2. If one fires: pool +1 (or overflow +1 if pool at 3/3), loot_rolls_owed +1, inline ledger announces it.
3. If none fire: inline ledger still says `[HP CHECK: no trigger | pool X/3 | overflow Y]`. Skipped ledger = `.fail 7`.
4. Awards FINAL — audits do not retroactively revoke Hero Points.

---

*KM_HeroPoints.md — Kingmaker PF2e Text Adventure | Hero Point Trigger Catalog v1.1*
*11 automatic + 21 judgment triggers. PF2e Player Core-aligned with Kingmaker-specific extensions.*
