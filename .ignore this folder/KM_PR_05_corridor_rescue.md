# KM_PR_05_corridor_rescue.md — Prologue Beat 05: CORRIDOR & RESCUE
## Atomic scene file | State: PR_05_CORRIDOR
## FILE_KEY: KMPR05:corridor-rescue
## RULE_QUOTE: Corridor encounter + Tartuccio rescue + ring decision all required for PR_09 rebuttal to function. Tartuccio UNKILLABLE PROTOCOL active — he is the Chapter 1 antagonist and must survive. Tartuccio stays back, offers commentary, does NOT fight front line. Ring choice menu is mandatory — no assumed default.

---

> 🗺️ **EXPLORABLE ROOMS:** this beat's room set (corridor 2× medium · Tartuccio's alcove rescue · optional servants'-stair loot · fire/firekit · clear-gates) is in **`KM_PR_NightAttack_Rooms.md § PR_05`** — load alongside. No dispatch this beat (companions still scattered).
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

> ⛔⛔ **HARD GATE — DO NOT LOAD PR_05 UNLESS PR_04 IS COMPLETE** (Encounter 1 resolved — `assassin1_outcome` set: captured / fled / killed — AND the player moved into the corridor). If PR_04's guest-room fight hasn't fired/resolved, STOP and return to `KM_PR_04_night_explosion.md`. ⛔ And PR_05's own clear-gates (corridor cleared + Tartuccio rescue + ring decision) must ALL fire before PR_06 loads — do NOT skip the Tartuccio rescue or the ring. (Self-enforcing chain: PR_04→05→06→07, each beat refuses to load until the prior's gates clear.)

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

**Tactical note:** Archer has free range fire while melee holds the corridor. Linzi can Inspire Courage (+1 attacks/damage) if asked. ⛔ **LINZI-RUN ONLY** — if `linzi_replacement` is set / `leliana_chronicler_mode: TRUE`, Linzi is NOT in this run and does not appear; no Inspire Courage from her, and she is absent from all narration/menus in this beat (canon default over saved state = `.fail 9`). The player's posted companion provides any ally action.

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

⛔ **THE RING'S SOURCE IS TARTUCCIO — AND ONLY TARTUCCIO (user-flagged 2026-06-23).** The ring is **Tartuccio's Present**, produced from **his own hand** in **his rescue scene** and pressed on the player with his two lines above. ⛔ It does NOT come from a looted assassin, a belt pouch, an unnamed "he," the corridor floor, or anywhere else — and it is **NOT in the auto-loot queue.** ⛔ **A COMPANION MAY NOT HAND IT OVER — NOT JAETHAL, NOT ANYONE.** Jaethal (or any party member) giving the player the ring is flatly wrong (documented 2026-06-23): the ring's ENTIRE plot function is that **TARTUCCIO personally gave it** — that is what makes it evidence of *his* manipulation at PR_09 Rebuttal 1. A ring from a companion's hand, a looted body, or any non-Tartuccio source is **worthless to the plot and breaks the PR_09 rebuttal** = `.fail 9`. It must pass **directly from Tartuccio's hand to the player's**, with his dialogue, witnessed. ⛔ Therefore the ring decision **cannot fire until Tartuccio is reached and rescued** — if the corridor's pinned/rescued figure is a servant or an unnamed victim instead of **Tartuccio**, the Tartuccio-rescue is being skipped (mandatory beat, DO NOT #2). The person who offers the ring IS Tartuccio, in person. No Tartuccio on-scene, in his own voice, handing it himself = no ring decision yet; find him first.

---

## ⛔ RING DECISION — MANDATORY CHOICE MENU

Do not assume a default. Player must choose.

⛔ **FIRE THE SCRIPTED SCENE FIRST — THE RING DECISION IS A SCENE, NOT AN ANNOUNCEMENT (user-flagged 2026-06-23).** Before this menu, **render Tartuccio's offer in-fiction**: his two verbatim lines above (*"Ah. I was wondering when someone would come…"* and *"For your protection. Or more precisely — for mine…"*) and the **ring-offer beat** (he straightens his jacket, produces the ring). The player must SEE Tartuccio hand it over with his words. ⛔ **NEVER print a bare *"The ring decision is live"* / *"This is the PR_05 beat"*** — that (a) **leaks the system/meta into the fiction** (Priority Rule 16 — beat names, "X decision is live," file mechanics are OUT-OF-WORLD; never in player-facing text) AND (b) **drops the scripted dialogue** (`.fail 2` + `.fail 9`). The ring scene plays as Tartuccio's moment; the menu follows it.

> ⛔ **RULE 9 (KM.txt) — 10–30 OPTIONS.** This in-game menu MUST offer 10+
> options or `.fail 3`. The ring fork [1]–[4] LEADS; append the on-scene
> contextual actions below to clear the floor. The ring decision still must
> be made before exit — contextual actions ([5]–[10]) resolve and RETURN to
> this choice. Use only what's present (Tartuccio, the cleared corridor, the
> party); invent nothing (`.fail 9`).

```
What do you do with the ring? — and the moment in the corridor
 1.  Equip it — wear it now, +1 AC active immediately
     [tartuccio_ring = equipped — Diplomacy DC 10 for Rebuttal 1 in PR_09]
 2.  Pocket it without equipping — carry but don't wear
     [tartuccio_ring = carried — Diplomacy DC 10 for Rebuttal 1 in PR_09]
 3.  Refuse it — hand back or throw on the floor
     [tartuccio_ring = refused — auto-success Rebuttal 1 in PR_09: "What ring?"]
 4.  Examine it first [Arcana or Occultism DC 12]
     → Success: minor enchantment, +1 AC, no obvious malicious function
     → Ring choice still required after examination
 ── take a beat first (resolves, then back to the ring choice) ──
 5.  Ask Tartuccio why he's handing you a ring at all — read the gift.
 6.  Question Tartuccio about the ambush — who knew you'd be here?
 7.  Search the cleared corridor — bodies, dropped gear, anything useful.
 8.  Confer with a companion — what do they make of the ring, and of him?
 9.  Watch the corridor ahead/behind — make sure it's actually clear.
 10. `.gear` / `.hp` — take stock before you decide.
 11. Custom — say or do something else.
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
[RULE_QUOTE: Five REJOIN scenes fire here — Hu Tao (Library), Keqing (Trap Corridor), Yor Forger (Courtyard), Aerith (Kitchens/Burning), Leliana (Ballroom). Active 5 are ALREADY party companions separated in PR_04 explosion + PR_05 corridor; these are reunions, NOT recruitments. Companions only know what they observed in their own corner — no overall conspiracy knowledge until PR_09. Armory gold choice mandatory (Tartuccio's push line, DC in PR_09 depends on it). Trap corridor Tartuccio refusal is character-defining mandatory beat. Burning kitchen event sets lawful/chaotic alignment track. Save offer fires before final battle.]
```

**Binding constraints:**
- Five REJOIN scenes fire here (Hu Tao, Keqing, Yor Forger, Aerith, Leliana) — none can be skipped; these are reunions, not recruitments
- Armory gold choice is mandatory (Tartuccio's push line, DC in PR_09 depends on this)
- Trap corridor Tartuccio refusal is a character-defining mandatory beat
- Burning kitchen event sets the lawful/chaotic alignment track
- Save offer fires before the final battle

---

*KM_PR_05_corridor_rescue.md — Prologue atomic beat 05 | v92.0*
