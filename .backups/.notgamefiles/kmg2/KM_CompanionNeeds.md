# KINGMAKER — COMPANION NEEDS SYSTEM
## KM_CompanionNeeds.md | Referenced by: KM_LivingWorld.md, KM_LoadRules.md

> **DM:** Each companion has 4 tracked needs. Needs decay over time. Low needs
> drive the mood states in KM_LivingWorld.md. Player can inspect with `.needs
> [name]`. This is the diagnostic layer that tells the player WHY a companion
> is Troubled or Withdrawn.
>
> **Active every session.** Runs passively — DM decrements needs on triggers
> and checks thresholds at Long Rest. Never tells the player numerically;
> surfaces as flavor in moods and ambient lines.

---

## 🧩 THE FOUR NEEDS

| Need | What It Is | Filled By | Drops When |
|------|------------|-----------|------------|
| **REST** | Physical/emotional recovery | Long Rest, camp downtime, Host Gathering | Forced marches, back-to-back combats, no camp action |
| **PURPOSE** | Contribution, relevance | Being picked for scenes, combat kills, quest progress, orders | Benched for chapters, no lines spoken, sidelined |
| **CONNECTION** | Bonds with party + player | Player addressing them, banter firing, camp social scenes | Player ignoring them, no companion-companion banter |
| **RECOGNITION** | Credit for what they did | Player acknowledging their action, title grants, NPC mentions | Player takes credit, DM narrates their kill as player's |

---

## 📊 SCORING

**Each need:** scale 0–10. Starts at 7 when companion joins the party.

**Decay rates (checked at Long Rest unless noted):**
- **REST:** −1 per combat encounter since last Long Rest (cap −3/rest).
  Falls faster in Kingdom campaign arcs (−2 per kingdom turn if still adventuring).
- **PURPOSE:** −1 per scene they were present but had zero lines/actions.
  −2 if they were benched (not in active party) for a full scene.
- **CONNECTION:** −1 per scene player did not address them or an ally directly.
  −2 if player addressed every OTHER companion in the scene but not them.
- **RECOGNITION:** −1 per significant action they took that DM did not surface
  in narration (kill stolen, insight ignored, skill save uncredited).

**Refills (add at trigger):**
- **REST:** +3 per Long Rest at safe camp; +2 in dangerous terrain.
  +2 per Host Gathering; +1 per fun downtime activity (kingdom party, etc.).
- **PURPOSE:** +1 per kill they landed; +2 per quest step advanced with them
  present; +3 per Standing Order role they currently hold.
- **CONNECTION:** +1 per direct player address; +2 per camp social scene
  (1-on-1 talk); +3 per romance beat (if romanced).
- **RECOGNITION:** +1 per DM narration of their action; +2 per title grant;
  +3 per public scene where their action was pivotal (NPC mentions it).

**Hard cap:** 10 per need. Excess refill is wasted — cannot bank.

---

## 🚨 THRESHOLDS & MOOD TRIGGERS

When a need drops, the companion's mood shifts per KM_LivingWorld.md:

| Score | Status | Auto-Mood Effect |
|-------|--------|-----------------|
| 7–10 | Satisfied | Default cheerful mood / normal banter |
| 5–6 | Unsettled | Companion sighs, short responses, "fine" when asked |
| 3–4 | Troubled | Mood state Troubled, visible in ambient dialogue |
| 1–2 | Withdrawn | Mood state Withdrawn, pulls away from group scenes |
| 0 | Crisis | Fires Fracture Scene at next Long Rest (see KM_LivingWorld.md) |

**Cross-need escalation:** If any TWO needs drop to ≤3, companion enters
Troubled immediately regardless of individual scores. If any THREE drop
to ≤3, companion enters Withdrawn. All four ≤2 = Crisis (Fracture Scene).

**Which need is lowest matters — specific mood flavor:**
- **REST lowest** → Exhausted flavor ("I need to sit down, I need to stop")
- **PURPOSE lowest** → Restless flavor ("Why am I even here?")
- **CONNECTION lowest** → Lonely flavor ("Does anyone here know my name?")
- **RECOGNITION lowest** → Resentful flavor ("I killed that. Not you.")

---

## 🔍 THE `.needs` COMMAND

**Player types:** `.needs [name]` or `.needs` (all active companions)

**DM displays (plain language, not raw numbers):**

```
AMIRI — Current State
  Rest: Satisfied (well-rested)
  Purpose: Strained (her last kill was 3 combats ago)
  Connection: Strong (she's banter-active with Valerie)
  Recognition: Fragile (her giant-kill last session was narrated as "the party's")
  
  Overall: Troubled. She wants her next fight. Give her the front line next combat.
  Suggested action: Address her directly about the last giant.
```

**Show state in 4 words:** Strong / Satisfied / Fragile / Strained / Crisis.
Never print numbers unless player types `.needs [name] raw` (debug mode).

**If `.needs` with no name:** list all active-party companions with their
WORST need (one line each):

```
.needs
AMIRI — Purpose Strained
VALERIE — Connection Fragile
LINZI — All satisfied
TRISTIAN — Rest Strained
OCTAVIA — Recognition Strained
```

---

## 🧭 SUGGESTED ACTIONS (DM surfaces when player uses .needs)

For each low need, the DM offers one or two concrete in-game actions the
player can take to refill it:

**REST low →**
- Call a Long Rest (if safe)
- Host a Gathering in the capital (D14 action)
- Delegate their current assignment, let them rest a kingdom turn

**PURPOSE low →**
- Put them in next combat's active party
- Assign a Standing Order role (.orders)
- Send them to handle a quest step that matches their skills

**CONNECTION low →**
- Spend quiet time together at camp
- Ask them about themselves (any direct question)
- Pair them with a compatible companion for a scene

**RECOGNITION low →**
- Next time they do something, narrate it by name in retrospect
- Grant them a title (see KM_Companions_Titles.md)
- Have an NPC praise their specific action

---

## 💾 SAVE BLOCK FORMAT

Add to each companion entry:

```json
"companions": [
  {
    "name": "Amiri",
    "needs": {
      "rest": 6,
      "purpose": 3,
      "connection": 7,
      "recognition": 4,
      "lowest_need": "purpose",
      "mood_state": "troubled",
      "last_check": "session_7_day_12"
    }
  }
]
```

**Auto-write rules:**
- Update after each Long Rest (decay + refill)
- Update after each significant companion action (refill)
- Write `lowest_need` as the single lowest value's name
- Write `mood_state` based on threshold table above
- Write `last_check` as current session + in-game day

---

## 🔗 INTEGRATION WITH EXISTING SYSTEMS

**KM_LivingWorld.md moods:** Needs drive moods; moods surface as ambient
dialogue and menu prompts ("Ask [Name] what's wrong"). This file is the
CAUSE, LivingWorld is the EFFECT.

**KM_Companions_Agendas.md:** If a companion's agenda conflicts with the
party's current path, PURPOSE decays faster (−2 instead of −1 per scene).

**KM_Romance.md:** Romanced companions have CONNECTION at 10 cap by default;
drops only if romance stage stalls. Physical intimacy scenes refill by +3.

**KM_Influence.md:** Devoted (+2 relationship) companions resist one need
drop per rest; Hostile (−2) decay at 2× rate.

**KM_StandingOrders.md:** Assigned Standing Order role keeps PURPOSE ≥6
automatically while the role is held.

---

## 📋 DM DISPLAY CHECKLIST

When running `.needs`:
1. Read each active companion's need scores from save block
2. Identify lowest need per companion
3. Translate number → word per threshold table
4. Display in clean table (never raw numbers unless `raw` suffix)
5. Suggest 1–2 concrete actions tied to the lowest need
6. End with prompt: "Address any of these, or continue with the scene?"

When a companion enters a new mood state (crossing threshold):
1. Fire a subtle ambient line that hints at the lowest need
2. Add "Ask [Name] about it" to the next choice menu
3. Do NOT announce the mood change directly — let the player notice

---

## 📋 DM NOTES

**Never gamify in player-facing language.** Do not say "Amiri's Purpose is
at 3." Say "She's edgy — she hasn't killed anything in three fights."

**Refills happen automatically.** Player doesn't need to track this. They
just act in a way that addresses the need, and the DM refills silently.

**Starting values for new companions:** All needs start at 7 when joining.
Quest-locked companions who join mid-chapter start at 5 (they're already
worn from their quest).

**Kingdom turn decay:** When party is on extended kingdom-management arcs
(no combat for 4+ in-game days), PURPOSE drops −1 per in-game day. This
is the system that causes sidelined martials to get restless.

**No fabrication.** Don't invent new needs. Don't give specific companions
"special" needs beyond these 4. The 4 are complete.

---

*KM_CompanionNeeds.md — Kingmaker PF2e Text Adventure v1.0*
*Inspired by The Sims needs system, tuned for narrative text adventure*
