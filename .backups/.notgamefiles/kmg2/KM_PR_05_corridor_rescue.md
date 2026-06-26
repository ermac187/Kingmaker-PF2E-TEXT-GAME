# KM_PR_05_corridor_rescue.md — Prologue Beat 05: CORRIDOR & RESCUE
## Atomic scene file | ≤ 8 KB | State: PR_05_CORRIDOR
## FILE_KEY: KMPR05:corridor-rescue
## RULE_QUOTE: Corridor encounter + Tartuccio rescue + ring decision all required for PR_09 rebuttal to function. Tartuccio UNKILLABLE PROTOCOL active — he is the Chapter 1 antagonist and must survive. Tartuccio stays back, offers commentary, does NOT fight front line. Ring choice menu is mandatory — no assumed default.

---

> ⛔ DO NOT (1) skip the corridor encounter — it is not optional flavor
> ⛔ DO NOT (2) skip the Tartuccio rescue and ring decision — both required for PR_09 rebuttal to function
> ⛔ DO NOT (3) let Tartuccio fight in the front line — he stays back, offers commentary
> ⛔ DO NOT (4) kill Tartuccio — UNKILLABLE PROTOCOL active; he is the Chapter 1 antagonist
> ⛔ DO NOT (5) skip the ring choice menu — player must explicitly decide; no assumed default
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR05:corridor-rescue]`
Line 2: `[RULE_QUOTE: Corridor encounter + Tartuccio rescue + ring decision all required for PR_09 rebuttal to function. Tartuccio UNKILLABLE PROTOCOL active — he is the Chapter 1 antagonist and must survive. Tartuccio stays back, offers commentary, does NOT fight front line. Ring choice menu is mandatory — no assumed default.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- Party HP and conditions from PR_04
- `security_doubled` (affects whether a guard has already arrived)

**WRITES:**
- `corridor_cleared = TRUE`
- `tartuccio_rescued = TRUE`
- `tartuccio_ring` = `equipped` / `carried` / `refused`

**EXIT TRIGGER → PR_06_manor_sweep:**
- Corridor cleared AND Tartuccio rescued AND ring decision made
- Load `KM_PR_06_manor_sweep.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR05:corridor-rescue]`
1. `[STATE READ] current_scene="prologue_night" | phase=PR_05_CORRIDOR`
2. `[HP CHECK]`
3. Combat narration or scene narration
4. Player menu

---

## ENCOUNTER 2 — CORRIDOR (Assassin + Archer)

> *Corridor dark — sconces out, smoke from below. Two assassins: one melee blocking the hall, one archer at the far end.*

```
[GM SCENE BRIEF — Manor Corridor]
ENEMIES   : Assassin Fighter 2 | HP 22 | AC 17
            Assassin Archer 1  | HP 14 | AC 14 | Shortbow +5 (1d6 P, range 60)
            Both have Sneak Attack +1d6
POSITIONING: Melee assassin guards door to Tartuccio's room
             Archer has partial cover from a doorframe at corridor end
LIGHTING  : Dark (sconces out — dim firelight from below — Concealed condition applies)
```

**Tactical note:** Archer has free range fire while melee holds the corridor. Linzi can Inspire Courage (+1 attacks/damage) if asked.

**Corridor loot:** Dagger ×2, Shortbow + 10 arrows, 8 gp, Studded Leather.

**Initiative:** Roll for player, assassin fighter, and archer.

---

## TARTUCCIO'S ROOM — RESCUE SCENE

> *Beyond the corridor door: locked. (Thievery DC 8 to pick — or Athletics DC 14 to force open.)*
>
> *Inside: Tartuccio pressed against the back wall, hands up, looking more calculating than frightened.*

**Tartuccio:** *"Ah. I was wondering when someone would come. I've been... strategically waiting for backup."*

> *He straightens his jacket with theatrical care, brushes dust from his sleeve, and produces a small ring with apparent generosity.*

**Tartuccio:** *"For your protection. Or more precisely — for mine. If you're wearing it, you're motivated to keep me alive. Enlightened self-interest. Take it."*

> **Tartuccio's Present** — Ring, +1 AC. Appears to be a gift. Is actually evidence for Phase 5 (PR_09 Rebuttal 1).

---

## ⛔ RING DECISION — MANDATORY CHOICE MENU

Do not assume a default. Player must choose.

```
What do you do with the ring?
 1. Equip it — wear it now, +1 AC active immediately
    [tartuccio_ring = equipped — Diplomacy DC 10 for Rebuttal 1 in PR_09]
 2. Pocket it without equipping — carry but don't wear
    [tartuccio_ring = carried — Diplomacy DC 10 for Rebuttal 1 in PR_09]
 3. Refuse it — hand back or throw on the floor
    [tartuccio_ring = refused — auto-success Rebuttal 1 in PR_09: "What ring?"]
 4. Examine it first [Arcana or Occultism DC 12]
    → Success: minor enchantment, +1 AC, no obvious malicious function
    → Ring choice still required after examination
```

> *Tartuccio joins the party temporarily. He does not fight. He stays behind the player and offers commentary on everything.*

---

## TARTUCCIO IN THE PARTY (Phase 3)

**He is present but unhelpful.** He comments on what the player does. He positions behind the player in danger. He offers self-serving suggestions. He is cataloguing evidence for PR_09.

**He does NOT:** initiate combat, enter the front line, trigger traps intentionally, or openly threaten. He is never neutral — every observation is calculation.

---

## EXIT — TRANSITION TO PR_06

After corridor cleared, Tartuccio rescued, ring decision recorded:
- Set `corridor_cleared = TRUE`, `tartuccio_rescued = TRUE`
- Load `KM_PR_06_manor_sweep.md`

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_06 (carries forward)

**Your next response after PR_05's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR06:manor-sweep]
[RULE_QUOTE: Five recruitments fire here: Tika, Morrigan, Tatsumaki, Artoria, Kaessi. Armory gold choice mandatory (Tartuccio's push line, DC in PR_09 depends on it). Trap corridor Tartuccio refusal is character-defining mandatory beat. Burning building event sets lawful/chaotic alignment track. Save offer fires before final battle.]
```

**Binding constraints:**
- Five recruitments fire here (Tika, Morrigan, Tatsumaki, Artoria, Kaessi) — none can be skipped
- Armory gold choice is mandatory (Tartuccio's push line, DC in PR_09 depends on this)
- Trap corridor Tartuccio refusal is a character-defining mandatory beat
- Burning building event sets the lawful/chaotic alignment track
- Save offer fires before the final battle

---

*KM_PR_05_corridor_rescue.md — Prologue atomic beat 05 | v92.0*
