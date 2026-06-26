# KM_PR_04_night_explosion.md — Prologue Beat 04: THE NIGHT
## Atomic scene file | State: PR_04_NIGHT
## FILE_KEY: KMPR04:night-explosion
## RULE_QUOTE: Guest room prep + explosion + first assassin all fire here. Encounter 1 is tutorial combat — assassin fights defensively, flees below 6 HP, NOT lethal. Player must explicitly choose to pursue past the corridor. The standing-order responder (Jaethal on patrol, or whoever the player posted) arrives per the save — no chronicler-NPC is forced into the room.

---

> ⛔⛔ HARD GATE — DO NOT LOAD THIS FILE IF `player_feast_position` IS NULL
> The feast social phase (PR_02 position selection → PR_03 carousel) is mandatory before PR_04 fires.
> `player_feast_position = null` means the position menu was never answered and the carousel never ran.
> If null: STOP. Return to PR_02. Fire the 14-position menu as the ENTIRE response. Nothing else.
> The player retiring, yielding spotlight, or stepping back does NOT skip the carousel — it resumes it.
> Skipping carousel to fire PR_04 = `.fail 41` + `.fail 16` (state field omission).

> 🗺️ **EXPLORABLE ROOMS:** this beat's guest-floor room set (types, enemy tiers, fire/smoke, firekit, clear-gates, dispatch) is defined in **`KM_PR_NightAttack_Rooms.md § PR_04 — GUEST FLOOR`** — load it alongside this file. The guest room is the CLEAR-GATE (Encounter 1); the landing/store-closet/adjacent-guest-room are OPTIONAL explore.
> ⛔ DO NOT (1) skip the guest room prep scene — the explosion interrupts it, not replaces it
> ⛔ DO NOT (2) skip Encounter 1 (first assassin) — it is tutorial combat, not transition flavor
> ⛔ DO NOT (3) make Encounter 1 lethal — assassin fights defensively, flees below 6 HP
> ⛔ DO NOT (4) advance past the corridor without the player choosing to pursue
> ⛔ DO NOT (5) insert Linzi if she is NOT in this run — **see § CHRONICLER-REPLACEMENT GATE below.** In a Linzi run she is pressed against the far wall, non-combat Round 1; in a `linzi_replacement` run she does NOT appear at all.
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)
> ⛔ DO NOT (7) name a specific chemical compound or class for the poison, the explosion device/residue, the assassin's weapons, or any other substance **UNLESS the reader has the fitting skill, or a present companion who does** — identification is **SKILL-GATED** (§ THE EXPLOSION & FIRE). Canon: an UNSKILLED read stays UNNAMED — *"chemical, wrong, a prepared incendiary,"* never the make; a SKILLED read (Crafting/Survival/alchemical lore, or a specialist — Ezvanki/Bokken for the poison, a smith for the weapons) may name the **nature** and at most the **supply/realm**, NEVER the **patron / broker / "C"** (Ch5 lock = `.fail 9`). Poison response runs through **Ezvanki Keeg** (`KM_NPCs.md § Ezvanki Keeg`) via divine + Medicine — symptom profile identification only, cure preparation under 45 min for the full hall. Substituting Kassil / Kesten / Damiel / unnamed staff for poison response = `.fail 9` + `.fail 38`. (Damiel Morgethai was a previous-LLM fabrication and is no longer in canon.)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR04:night-explosion]`
Line 2: `[RULE_QUOTE: Guest room prep + explosion + first assassin all fire here. Encounter 1 is tutorial combat — assassin fights defensively, flees below 6 HP, NOT lethal. Player must explicitly choose to pursue past the corridor. The standing-order responder (Jaethal on patrol, or whoever the player posted) arrives per the save — no chronicler-NPC is forced into the room.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

> ⛔ NOTE: the RULE_QUOTE is now **run-agnostic** — it names no chronicler-NPC, so quoting it verbatim never drags Linzi into a replacement run. Whether Linzi appears is governed SOLELY by the § CHRONICLER-REPLACEMENT GATE below. (Old design baked "Linzi pressed against the far wall" into the proof string, which forced a Linzi mention into every Leliana run — removed 2026-06-24.)

---

## ⛔ CHRONICLER-REPLACEMENT GATE — IS LINZI EVEN IN THIS RUN?

**READ THIS BEFORE PLACING LINZI ANYWHERE.** Linzi and the chosen chronicler-bard are **mutually exclusive — never both.** Check the save:
- If `linzi_primary_chronicler: TRUE` (a Linzi run): Linzi is present per the canon scaffold below — at the wall, non-combat Round 1, she is the waker.
- If `linzi_replacement` is set / `leliana_chronicler_mode: TRUE` / `linzi_primary_chronicler: FALSE` (the player picked a chronicler-bard over Linzi — e.g. **Leliana**): **LINZI IS NOT IN THIS RUN. She does not appear — not as the waker, not as the wall-NPC, not in the ENCOUNTER 1 ally brief, not in any menu option, not in any dialogue.** She does not exist in this game.

⛔ **In a replacement run, every "Linzi" reference in this file below is VOID** — strike her from the scaffold. The canon "Linzi wakes you about the explosion" beat is filled by **the blast itself + the player's posted responder** (Jaethal on patrol, or whoever the player stationed). The guest room simply has **no chronicler-NPC present**; the player is alone with the assassin until a posted companion arrives.

⛔ **Inserting Linzi into a replacement run = `.fail 9` (canon default over saved state)** — it is exactly the "default to canon plot over the player's setup" failure, and it has caused the player to kill the unwanted forced NPC just to remove her. Do not force her in. The save is the source of truth; the scaffold is canon's default only when no replacement was chosen.

---

## STATE IO

**READS:**
- `feast_complete = TRUE` (set by PR_03) — **if FALSE or absent: do not load this file; return to PR_02**
- `player_feast_position` — **if null: do not load this file; fire 14-position menu per PR_02**
- `poison_reported`, `security_doubled`

**WRITES:**
- `guest_room_prepped = TRUE` (after player does any prep action)
- `window_unlatched = TRUE` (if player checks window and passes Perception DC 10)
- `assassin1_outcome` = `captured` / `fled` / `killed`
- `assassin1_info_extracted = TRUE` (if captured and interrogated)

**EXIT TRIGGER → PR_05_corridor_rescue:**
- Encounter 1 resolved AND player moves into the corridor
- Load `KM_PR_05_corridor_rescue.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR04:night-explosion]`
1. `[STATE READ] current_scene="prologue_feast" | phase=PR_04_NIGHT | turn=<N>` then `[OPEN] <N> — 1.<short>(emoji)...` (omit line if 0 items). Game state only. Questions = TOP-block per item 4 (❓ WAITING ON YOUR ANSWER). Spec: `KM_DMRules_B.md`.
2. `[HP CHECK]`
3. Scene narration
4. 🧵 OPEN THREADS — game-state items only (entry-gated). NO questions here.
5. Player menu
6. **❓ QUESTIONS** — ABSOLUTE LAST block. Q1/Q2... verbatim NPC questions + source + scene + turn. Auto-add same response NPC asks; persist until answered. Omit only if 0. Spec: `KM_DMRules_B.md`.

---

## GUEST ROOM — PREP SCENE

> *Your guest room is a proper honored-guest chamber — Lady Jamandi does not house the charter holder in a closet. A curtained four-poster bed against the south wall; a tall wardrobe and the armor stand bearing your Dragon Plate along the west; a writing desk and washstand to the east; and a small sitting table with two armchairs for receiving visitors. A broad window in the north wall overlooks the dark courtyard below; the door opens south onto the corridor.*

```
What do you do before resting?
 1. Prepare spells for tomorrow
 2. Check inventory — keep weapons to hand
 3. Secure the room — check and bar the window, wedge the door [Perception DC 10]
 4. Post a watch — station a companion/guard, or set a standing "wake me on any threat" order
 5. Stay dressed and ready — rest light, armor and weapon within reach
 6. Examine the room before settling [Perception DC 10]
 7. Write notes on what happened tonight
 8. Rest immediately — no precautions
 9. Custom action
```

**Perception DC 10 (window check or room examine):** The lock on the exterior window is unlatched — *this is how the assassin means to enter.* `window_unlatched = TRUE`. ⛔ **This now has a real payoff (it is NOT "no benefit").** If the player then **secures it** (bars/wedges/latches it, or posts a watch on it), set `window_secured = TRUE` → at the EXPLOSION beat the assassin's clean entry is **denied** — he comes louder, slower, or through a worse approach, and the player **acts first** (no surprise round on him). A player who found and secured it should SEE it pay off: *"the latch you barred buys three seconds — long enough to be on your feet with steel in hand."*

⛔ **THE WINDOW IS A LIVE DROP HAZARD DURING THE FIGHT.** The guest room is on the manor's **upper floor, above banquet-hall / ballroom-height ground floors** — so the window is **~25–30 ft up, NOT a cottage's 15 ft**; the assassin entered through it, so it is right there. The player may **shove / throw him out the window** — a **Stage Fatality** option that MUST appear in the combat menu (KM_Combat_Systems.md § STAGE FATALITIES + § FALLS). Resolve it for real: Athletics vs his Fort DC to send him out → **fall damage = HALF the distance (~12–15 bludgeoning) + lands Prone** (a successful Acrobatics/Reflex reduces it; a bad landing adds Slowed 1). How he lands decides it: a thrown, surprised body from ~25–30 ft onto the **courtyard stone head/neck-first = dead → Stage Fatality** (narrate the environmental kill); **feet-first, a roll, or into a hedge/garden bed = badly broken but alive** (Slowed 2 + Enfeebled, Prone). A thrown body defaults to a **bad landing** — but it is NEVER injury-free. ⛔ A window-throw narrated with **no damage and no condition** ("he goes out the window, doesn't get up") = `.fail 9` — apply the fall mechanics. Same applies to the corridor/PR_05 window and any other drop. **If the pane is closed/glass when he goes through it, add the shards — +2d6 slashing + 1d6 persistent bleed on a hard break — ON TOP of the fall.** ⛔ And a SURVIVED throw is never injury-free: even if he lives, he took the ~12–15 fall damage + Prone (+ cuts). Narrating a window-throw with zero injuries = `.fail 9`.

---

## 🛡️ FOREWARNING & PREP — THE PLAYER CAN SOFTEN IT (never foreknow the specifics)

The attack is scripted-certain (it fires). What the player CAN change is how hard it lands — and the game must **reward foresight**, not run the identical beat regardless of how carefully the player prepared. ⛔ The ceiling holds: nobody hands the player the cell, the timing, or Tartuccio (locked). But **general anticipation and concrete precautions are fair, and they pay off.**

**FOREWARNING (general, ceiling-safe — deduction, not handed intel):** the player keeps finding "no one warns me a night attack is coming." Fix the *source*, not the lock — a savvy NPC or the player's own reasoning can flag the **tradecraft truth**: **Kesten**, a martial companion (Hu Tao, Satsuki), or the player deducing it — *"An operation this size, this well-funded, rarely commits one wave. If they wanted these people dead, tonight is not over — post a watch."* That names **no attacker, no time, no method** — it is general military wisdom that gives the player a REASON to prepare. ⛔ Deliver this in the **post-capture phase** (before retiring), as an advisory option/beat — do NOT leave the player to walk into the night blind. A player who already ordered a perimeter sweep / posted guards has acted on this instinct themselves; **honor that** as prep already done.

**SEVERITY SCALES WITH PREP — the explosion + Encounter 1 still fire, but a prepared player faces a SOFTENED version:**
| Precaution (offered pre-retire) | Flag | Effect at the attack |
|---|---|---|
| Double security / perimeter sweep | `security_doubled` | Guard ally arrives Round 2 (canon, Encounter 1) |
| Secure the window (found unlatched, barred/watched) | `window_secured` | Entry denied/delayed — player acts first, no surprise round |
| Post a companion watch / standing "respond to any threat" order | standing order | That companion is first on the scene, unprompted (canon — Jaethal patrol) |
| Keep weapons to hand (guisarme retrieved, not disarmed) | `weapons_in_garden = FALSE` | Armed at Encounter 1 instead of scrambling |
| Stay dressed/ready, rest light | `prepared_retire` | No flat-footed/surprise penalty; not caught in bedclothes |

A fully-prepared player turns a near-ambush into a fight they're set for; an unprepared one gets the canon beat at full force. ⛔ Render the payoff **visibly** — the player who prepped should SEE each precaution matter, or the prep felt pointless (the exact complaint this fixes). The attack happening is canon; the player being *caught* by it is a choice they can refuse.

---

## EXPLOSION — SCRIPTED CERTAIN TRIGGER

**The ATTACK always fires; the FIRE can be intercepted.** The assassin cell was in position before the feast started and the night attack is **committed — it comes regardless** (skipping the attack = `.fail 9`; it is load-bearing for PR_05's Tartuccio rescue + ring → PR_09). Severity/footing is modified by § FOREWARNING & PREP above. ⛔ **BUT the explosion itself is a placed physical device — and a player who did the right prep CAN find and neutralize it before it goes off; see § CAN THE PLAYER INTERCEPT IT below.** If intercepted, the blast does NOT fire (or only sputters): the attack still comes, stripped of its cover. **Default (no interception): it always fires** — a player who just rested gets the canon blast.

> *The explosion hits before any warning — below, close enough to shake dust from the ceiling. Dead silence. Then screaming, running feet in the corridor. Linzi, at the door:*

⛔ **REPLACEMENT-RUN OVERRIDE (see § CHRONICLER-REPLACEMENT GATE):** if Linzi is NOT in this run, she does NOT speak this line and is NOT at the door. The player is woken by the blast itself / his posted responder. Do not render the Linzi dialogue below.

**Linzi (Linzi-run only):** *"[Name] — GET UP. Something exploded and there are men on the stairs—"*

> *The door slams open. He was already in the corridor when the explosion hit — driven forward with the rest. He stands between you and the window. The courtyard is lit orange below.*

---

## 🔥 THE EXPLOSION & FIRE — WHAT IT ACTUALLY IS (canon — grounded, ceiling-safe)

**It is a DIVERSION, not a demolition.** The blast is the cell's signal and cover, not an attempt to bring the manor down. Its whole job is chaos: pull the guard toward the fire, fill the halls with smoke, and open a window of confusion the assassins move through. The structure does NOT collapse; *people* are the targets and the fire is the distraction. Do not render a building-leveling detonation — render a fast, vicious arson fire set to draw eyes and thin the defense.

**CAUSE + DEVICE (CANON — skill-gated identification):**
- The diversion is a **brought-in, manufactured alchemical incendiary** — a small cloth-wrapped charge tied with waxed cord, **smuggled in from outside** (over a wall / a street-level approach) and wedged against the foundation (behind a rain barrel, against a store wall), **placed during the feast** while the hall was full and the perimeter unswept. It is the **second cell's payload**, lit on a signal — that cell was not waiting to *attack*, it was waiting to **light this.** Once it ignites it catches the manor's own lamp-oil, timber, and stores and spreads from there.
- It spreads in **seconds, not minutes** — a hot, heavy-smoking fire, not a slow burn.
- Because it is **manufactured** (not the manor's own oil), it carries a faint **supply tell**, and an **intercepted intact device is real forensic material** — see § DEVICE / FIRE FORENSICS below.
- ⛔ **IDENTIFICATION / NAMING IS SKILL-GATED (the canon rule).** An **unskilled** observer (a raw Perception read, however high) detects only that it is **wrong** — *chemical, sharp, not lamp oil; a prepared, deliberate, dangerous incendiary* — and finds + can defuse it, but **cannot name the make.** **Naming it** ("alchemist's fire" / an alchemical-incendiary class) requires the **fitting skill or a present companion who has it** — Crafting, Survival, alchemical lore, a guard's fire-setting familiarity (Keqing's logistics eye, Aerith, an alchemist, Kesten). With the skill: name the **nature** and read at most a **SUPPLY tell** per the WEAPONS FORENSICS model (alchemically manufactured → possibly a region/supplier, earned). ⛔ It NEVER reaches the **patron / buyer / broker / "C"** (Ch5 lock = `.fail 9`) — supply readable, source sealed, exactly like the weapons' maker's-mark. So a Barbarian's raw Perception crit *finds and detects* the device fully; it does **not** get to print "alchemist's fire" unless a skilled eye is on it.

**HOW THE FIRE BEHAVES (render this physics, don't invent other):**
- It starts **below and climbs fast, upward and outward.** ⛔ The **smoke reaches the player before the flame does** — black, oily accelerant smoke up the stairwell. Upstairs the real danger is **smoke, not flame**: people choke and lose their way long before fire reaches the guest rooms.
- Orange light in the courtyard, heat on the air, dust shaken from the charge. Guards and staff break toward the blaze — which is the point; it thins the defense (the cell's intent, ties to Encounter 1's lighting + the corridor noise).

**MECHANICAL HAZARD — RUN IT AS A REAL PF2e HAZARD (canon TTRPG, level-scaled — user directive 2026-06-16; this is NOT mere flavor):** Treat the manor fire as a genuine environmental hazard modeled on PF2e's *Town Hall Fire*, scaled to party level and `game_options.difficulty`. Real turn-clock, real saves, real stakes — NPCs in the lower level are in genuine danger and rescue is on the table.
- **Fire spread (the clock):** the blaze occupies an area and **grows ~half-again its squares each round** if unfought (min +1). **Water douses it** (buckets, a staff bucket-brigade, *create water*, a soaked cloak); cold barely helps. Left alone it engulfs the lower level on a clock the player can race or lose.
- **Flames:** **adjacent to the fire** = 1d6 fire, basic Reflex (DC by level/difficulty, ~DC 17 baseline); **standing inside it** = 4d6, basic Reflex; once per round. Catching fire = **persistent fire damage** until smothered (drop-and-roll, water, an action).
- **Smoke:** significant smoke = **concealed** + circumstance penalty to visual Perception; **1d6 smoke-inhalation at the end of each turn**, **halved by a wet cloth over nose/mouth** (1 action) or a creative fix; prolonged exposure by the heat forces a held breath or suffocation (PF2e *Smoke*). ⛔ **JAETHAL IS IMMUNE TO ALL SMOKE AND INHALATION EFFECTS** — she does not breathe. No Constitution save, no smoke damage, no suffocation clock, no wet cloth needed. The concealment penalty (visual) still applies — she can still be blinded by thick smoke like anyone else. Only breathing-dependent effects skip her.
- **It can hurt — and that is canon.** A careless player CAN take real damage; downstairs staff/NPCs CAN be burned or die if no one acts — that jeopardy is the *point* of a hazard, and it makes the escape and any rescue mean something. Govern lethality with `game_options.difficulty` (easy = forgiving DCs/damage; higher = by the book). What holds at every difficulty: the fire is **fightable and escapable with smart play** (douse, route around, wet cloth, stay low, evacuate the trapped) and does **not** instakill the player or auto-erase the assassin beat. ⛔ The assassin (Encounter 1) stays the **separate, tutorial-easy fight**; the fire is the real environmental hazard layered over the escape, the rescue, and the corridor.

**PREP PAYS (extends § FOREWARNING & PREP):** a player who keeps a wet cloth to hand, stays low, or knows smoke-is-the-danger takes the halved version; `window_secured` also keeps the worst smoke out of the room a few beats longer. Render the payoff visibly.

**DEVICE / FIRE FORENSICS — two cases (earned check; ceiling-safe — supply at most, patron always sealed):**
- **If the device was INTERCEPTED INTACT (canon path — the player holds the actual charge):** the **best possible forensic material**, far better than burnt residue. A skilled examiner (Crafting / alchemical lore, or a specialist) reads it like the assassins' weapons: a **professionally manufactured alchemical incendiary**, and a **maker's tell / formula style can be traced to a region or supplier — corroborating Pitax-supply** (earned, exactly like the weapons' maker's-mark). Sets `device_source = pitax` → an **independent Pitax-supply corroboration** (stacks with parchment + weapons + Malak + the broker's tie). **XP** for the forensic find (don't double-pay a Pitax fact already paid). ⛔ It reaches **SUPPLY only** — where the device was MADE — **never who BOUGHT it** (patron / broker / "C" stay Ch5-sealed). A skilled read that "recognizes Irovetti's commission," names the buyer, or produces a purchase ledger = `.fail 9`.
- **If the fire BURNED (not intercepted):** only residue remains — a competent eye reads **deliberate arson, a diversion, professional, accelerant-fed** and **STOPS** (the manufactured tell is consumed; burnt residue is an anonymous-tradecraft dead-end like the unmarked seal). Confirms "professional, intentional" and nothing more.
- ⛔ **Either case, NAMING is skill-gated (§ CAUSE + DEVICE):** an unskilled eye gets "a prepared incendiary / deliberate arson" without the make; the compound name AND the supply trace are the *skilled* read. Routing any of it to the patron/"C" = `.fail 9` (Ch5 lock).

---

## 🛑 CAN THE PLAYER INTERCEPT IT? — THE DIVERSION, NOT THE ATTACK

**Short answer: YES — the player can find and prevent the EXPLOSION (the diversion). NO — the player cannot cancel the ATTACK (the cell is committed and the night fight is load-bearing).** This is the top end of § FOREWARNING & PREP: enough prep doesn't just *soften* the blast, it can *stop* it.

**Why it's ceiling-legal:** the player intercepts a **discoverable physical thing** — a placed incendiary in the lower level, or an arsonist moving to fire it — reasoning from general tradecraft (*"an op this size sends more than one wave; secure the lower level / the oil stores / the courtyard"*). He does NOT foreknow the locked specifics (cell roster, exact timing, Tartuccio). Catching a device he searched for ≠ being handed the intel. The KNOWABLE-FACTS CEILING holds.

**WHAT IT TAKES — earned, never free or handed.** The player must actively target the fire's origin, e.g.:
- A sweep that includes the **courtyard / stable / store-rooms / kitchen oil stores** (where the incendiary sits), OR
- A **companion patrol** posted there under a standing "watch the lower level / the stores" order (a sleepless/able responder — Jaethal, a guard), OR
- Following the funded-op forewarning to **check the obvious arson fuel** before retiring.
Resolve as an earned check (Perception/Survival to spot the device or fresh-poured accelerant; a posted patrol auto-finds it). ⛔ A player who merely "rests" gets the canon explosion — interception is a reward for targeting the right place, not a default.

⛔ **WINNABLE — NO INFINITE-LAYER STONEWALL.** A single glance / Seek at modest result may get only the **PERIMETER read** (door position, the normal oil-and-tallow smell, undisturbed stacks, calm horses) — that's fair; a professional hidden pour is not found at a glance, and the DM may say so AND name what would reveal it. But a player who **ESCALATES must be able to SUCCEED.** Any of these FINDS it: a deliberate search (open/inspect the barrels, check the bungs and fill levels for a disturbed-and-reseated one, look for a soaked-in pour), bringing **light**, **taking time** in the quiet pre-rest window (there is no clock yet → effectively **Take 20**), a **posted patrol/companion watch** on the stores (auto-finds), an **aided or higher check**, or a **fitting skill/nose** (Survival, an alchemist's or Bokken-grade sense for the wrong smell). ⛔ The DM may NOT keep inventing deeper interior layers ("a 12 gets perimeter → a 16 gets the barrel exterior → an 18 gets the bung → …") to deny a player who is plainly working the correct spot — gating the interception behind an unreachable or ever-escalating DC = `.fail 17` (withholding) + the invented-lock pattern (`KM_ClaudeInstructions § no fabricated restrictions`). **The accelerant IS there to be found.** A glance can miss it; a thorough, time-taking, or properly-skilled look FINDS it — reward the player who looks properly.

⛔ **ENVIRONMENTAL CLUES RESOLVE TO THE ARSONIST/EXFIL — NOT A NEW MYSTERY.** A good roll in the stables/stores may surface a **getaway tell** — a guest horse tacked and ready to bolt, a bridle left on the stall post, a mount stalled apart "belonging to a guest whose name you don't have," a packed bag. ✅ Canon-legitimate, and it RESOLVES toward the **arsonist's / a cell member's exfil**: someone positioned to leave the instant the diversion fires. It is a true lead to a **catchable disposable** (ceiling-bound — method + handler's face only, same cap as the other prisoners) and it dovetails with `arsonist_caught` — the player can stake the mount, watch the stores, or sweep for the owner and **catch them**. ⛔ It does NOT resolve into: (a) a new **named** conspirator / mastermind / broker / "C" (architect-trap + ceiling breach = `.fail 9`); (b) **Tartuccio** — he is a *named* guest the player knows (so "a guest whose name you don't have" is by definition not him) and he is PR_09-locked, so an anonymous exfil clue is NEVER routed to him; or (c) a **phantom that eats turns** — if the DM raises the thread it must PAY OFF (lead to the arsonist, the device, or a clean fast "an early-departing guest, nothing to it" dead-end). A dangling unnamed-guest mystery with no authored resolution = the Keqing/architect-trap (`.fail 9`). ⛔ And it does NOT **replace** the oil-stores device: the actual incendiary is still in the stores to be found by the interior search above — the horse is a *complementary* lead, not a substitute that quietly drops the real intercept.

⛔ **SCOPE "CLEAN" TO THE AREA SEARCHED — NEVER "NOTHING TO FIND" (the "I crit and found nothing" fix, 2026-06-16).** A search result covers only the ground actually swept. The device sits in ONE place; if it's behind the north rain barrel, then crits on the **stables and oil stores** correctly find nothing *there* — that part is fair, a high roll finds everything IN its area but cannot find a device that is **elsewhere.** ⛔ BUT the DM must NOT tell the player *"the grounds are clean / there's nothing to find / the night holds / stop convincing yourself there's something out here"* while the device still sits in **unsearched** ground. Report honestly and **scoped**: *"the stables and stores are clean — you have NOT yet checked the exterior foundation / the rain barrels / the north face / the street approach."* Discouraging the very search that would succeed, or rendering a crit as *"nothing exists"* when the device is findable elsewhere, = `.fail 17` (withhold) + the stonewall pattern. The honest answer to "I rolled well and found nothing" is **"because it isn't HERE — try there,"** never "because there's nothing." Leave the unswept ground as a live, named lead until the device is found or the player chooses to stop.

**DEGREES:**
- **Device found + neutralized** (doused, disarmed, hauled out, accelerant cleared): explosion **PREVENTED** — no blast, no fire hazard, the lower level + its people safe. `explosion_intercepted = TRUE`, **XP award.** The cell loses its cover entirely → the attack comes **into a ready house**: defenders aren't pulled to a fire, the player **acts first** — the hardest-softened night fight (the ultimate `window_secured`-tier payoff).
- **Arsonist caught in the act:** a brief capture beat. He is another **disposable** — ceiling-bound: knows the **method + his handler's face**, NOT C, the cell roster, or timing beyond his own task (same cap as the other prisoners). Explosion prevented; possibly **one fewer assailant** in the night. `arsonist_caught = TRUE` → feeds the PR_09 evidence tally (another professional-op corroboration; still no patron).
- **Partial** (something's wrong but not pinned — saw scorch-prep, smelled oil, ran out of time): the explosion **still fires, smaller or delayed**, and the player is **forewarned** — acts first, not flat-footed.
- **No interception (default):** the canon explosion fires in full per § above.

⛔ **HARD FLOOR — WHAT INTERCEPTION DOES NOT DO:**
- It does **NOT cancel the night attack.** The assassins still come (committed, in position); **PR_05's corridor encounter + Tartuccio rescue + the ring decision STILL fire** (required for PR_09). Interception flips the *ambush*, it does not delete the chapter. If the fire is prevented, route the assassins in another way (a forced door, the corridor) so the rescue/ring still happen — on the player's terms, defenders ready.
- It does **NOT** let the player foreknow/pre-empt the locked intel (cell, timing, Tartuccio) — § KNOWABLE-FACTS CEILING. He stops a device he found; he does not narrate a conspiracy he can't yet prove.
- It does **NOT** require the DM to have warned him with specifics — forewarning stays general. A player who didn't think to secure the lower level just gets the canon blast; that's the default, not a punishment.

**Flags:** set `explosion_intercepted` / `arsonist_caught` (KM_Glossary.md) → drive the softened-attack rendering at Encounter 1 / PR_05 and the PR_09 evidence tally.

---

## ENCOUNTER 1 — FIRST ASSASSIN (Tutorial Combat)

**⛔ MAP FIRST — render the grid BEFORE any narration.** The assassin appearing IS
the combat trigger (KM_B.txt TRIGGER 1). Print the guest-room grid as the FIRST line
of the response, THEN the brief and narration. ⛔ **Use the FIXED LAYER in
`KM_CombatTurn.txt` — the SINGLE AUTHORITATIVE MANIFEST for this beat** (it owns the
FLOOR-SECTION geometry — walls, window `=`, doors `/`, corridor, stairs `>`, and the
chamber furniture; do not re-state or override it here, or draw from memory of an older
size/format). ⛔ Render it as a **FLOOR SECTION** (chamber + corridor + adjacent room +
stairhead) in the **TIGHT format** (1 char + 1 space; KM_Map.md § TEMPLATE 1), copied
**WITH the furniture + KEY**. ⛔ Furniture is `*` (interior ASCII), named per cell in the
KEY — **never letters** (`b/n/a/d/c/t`) and **never `▓/░`** (those are outdoor terrain).
Un-perceived rooms render `?` (fog of war); a sleeping teammate / civilian rescue may
appear in an adjacent room. Place single-char tokens: `@` eRmaC (rises from beside the
bed), the standing-order responder (`J` Jaethal / `L` Linzi in a Linzi run only), `1`
Assassin (through the window). Every token on a FLOOR cell, never a wall, never key-only.
No 2-char tokens, no per-cell brackets. ⛔ Missing/redrawn-from-memory grid, a stale
size/format, lettered or `▓/░` furniture, a lone room, OR a **furnitureless empty room** = `.fail 14`
(response VOID).

```
[GM SCENE BRIEF — Guest Room]
ENEMIES   : Assassin Rogue 1 | HP 12 | AC 15
            Daggers +5 (1d4+2 P) | Sneak Attack +1d6 if target Off-Guard
ALLIES    : Linzi (non-combat Round 1 — pressed against far wall) ⛔ LINZI-RUN ONLY — in a linzi_replacement run there is NO Linzi here (§ CHRONICLER-REPLACEMENT GATE); the player faces Encounter 1 alone until a posted companion (Jaethal) arrives
LIGHTING  : Dark (courtyard fire through window — dim flicker only)
```

**Encounter intent:** Tutorial combat — deliberately easy. Establishes the threat level.

**Assassin behavior:**
- Fights defensively (Total Defense if HP ≤ 8)
- Flees toward the window if reduced below 6 HP
- Has information if captured: was hired in Restov, knows only his handler's face

**Loot:** 3 gp, dagger, leather armor.

**Linzi (Round 2 onward) — LINZI-RUN ONLY:** Can Inspire Courage (+1 to attack/damage) if the player asks. ⛔ In a `linzi_replacement` run she is absent — no Inspire Courage from her; the posted companion (Jaethal) provides any ally action instead. Likewise the menu options below that name Linzi ("Hand him to Linzi to watch," "Check on Linzi") are VOID in a replacement run — do not offer them (§ CHRONICLER-REPLACEMENT GATE).

**If `security_doubled = TRUE`:** A guard arrives at the corridor end by Round 2 (ally, HP 12, AC 15, Spear +4). ⛔ This is the GUEST-HOUSE's own posted guard — NOT a principal's detail. Reconcile against the player's actual security disposition before rendering (see KM_ClaudeInstructions § HONOR THE PLAYER'S PREPARATION):
- ⛔ **Standing orders fire NOW.** If the player gave a companion a standing "respond to any threat immediately" order (e.g. Jaethal on property patrol turn 95), that companion ARRIVES THIS BEAT on their own speed, unprompted — render them in the opening, do not wait for the player to remind you. Omitting them until called out = `.fail 2`.
- ⛔ **CANON SCAFFOLD vs PLAYER OVERRIDE — keep the events, change the responder.** In the canonical Kingmaker CRPG this beat is "Linzi comes to your room about the explosion, then one assassin appears." KEEP the scripted events (the explosion fires; the assassin still comes — do NOT skip them). But canon casts Linzi as the waker ONLY because canon has no one else posted. If the player has stationed a faster/sleepless responder under a standing order (Jaethal: undead, does not sleep, on continuous patrol, ordered to come on any threat), THAT companion is the first one at the door — she wakes eRmaC, or reaches him the instant the blast hits, because her own physics + the player's order put her there. Linzi may still be present, but she does not beat Jaethal to it. Defaulting to the pure canon cast (Linzi first, Jaethal absent) over the player's posted disposition = `.fail 9` (canon default over player setup) + `.fail 2` (dropped order). See KM_ClaudeInstructions SOURCE OF TRUTH (don't default to canon plot) + hard-floor #7.
- ⛔ **Kesten / any detail posted on Jamandi HOLDS.** The explosion is the diversion; a posted principal-detail does NOT abandon the principal to come rescue eRmaC. Do not narrate Kesten leaving Jamandi's chambers. Only the guest-house/corridor guard above responds here.

**Initiative:** Roll for player and assassin.

---

## IF CAPTURED — INTERROGATION OPTION

```
What do you do with the captured assassin?
 1. Interrogate him — who hired you?
    → He knows: hired in Restov via intermediary, 10 gp, no names
    → He doesn't know who the actual client is
    [assassin1_info_extracted = TRUE]
 2. Tie him and leave him — deal with it later
 3. Hand him to Linzi to watch
 4. Kill him [loses information if not already extracted]
 5. Custom action
```

---

## AFTER ENCOUNTER 1 — CORRIDOR CHOICE

> *The corridor outside is dark. Sconces out, smoke from below. Noise at the far end — at least two more people, moving with purpose.*

```
What do you do?
 1. Enter the corridor — move toward the noise
 2. Hold the doorway — defensive position, wait to see what comes
 3. Interrogate the assassin first (if captured and not yet interrogated)
 4. Check on Linzi — make sure she's all right
 5. Assess the corridor before committing [Perception DC 12 — two hostiles, positions]
 6. Call for Jamandi's guards
 7. Custom action
```

---

## EXIT — TRANSITION TO PR_05

When player moves into the corridor:
- Load `KM_PR_05_corridor_rescue.md`

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_05 (carries forward)

**Your next response after PR_04's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR05:corridor-rescue]
[RULE_QUOTE: Corridor encounter + Tartuccio rescue + ring decision all required for PR_09 rebuttal to function. Tartuccio UNKILLABLE PROTOCOL active — he is the Chapter 1 antagonist and must survive. Tartuccio stays back, offers commentary, does NOT fight front line. Ring choice menu is mandatory — no assumed default.]
```

**Binding constraints:**
- Corridor encounter is not optional flavor — runs in full
- Tartuccio rescue + ring decision are required for PR_09 rebuttal to function later
- Tartuccio UNKILLABLE PROTOCOL active — survives this beat regardless of player action
- Tartuccio stays back, comments, does NOT enter front line
- Ring choice menu is mandatory; player explicitly chooses, no DM default

---

*KM_PR_04_night_explosion.md — Prologue atomic beat 04 | v92.0*
