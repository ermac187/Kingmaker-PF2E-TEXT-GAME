# KM_PR_NightAttack_Rooms.md — Night Attack: Explorable Room Framework
## Shared schema for PR_04 → PR_07 | FILE_KEY: KMPRNA:rooms
## RULE_QUOTE: Each night-attack beat (PR_04/05/06/07) has its OWN defined set of explorable rooms. A room is TAGGED by type, lists enemies by tier (weak/medium/strong), loot, rescue targets, fire/smoke state, and firefighting items. The CURRENT beat's rooms are all explorable in any order; the beat does NOT advance until its CLEAR-GATE rooms are cleared. Player may DISPATCH a companion group to clear another room — cost = Hero-Point overflow (KM_MissionResolution). Enemy budget across the whole night = 11 assassins + Assassin Leader + Frost Giant (canon, Yor's in-count).

> **DM:** This file is the **framework + data** for the night-attack rooms. Each beat file (KM_PR_04/05/06/07) references its room set HERE. Load alongside the active beat. This file does NOT replace a beat's scripted mandatory moments (Tartuccio rescue, the five rejoins, the armory gold choice, the Jamandi duel) — it adds the explorable layer AROUND them.

---

## ⛔ HOW THIS WORKS — READ FIRST

1. **Rooms are per-beat.** PR_04 has its rooms, PR_05 has its rooms, etc. The DM only ever offers the **current beat's** room list. A room from PR_06 is NOT reachable while the player is in PR_04. This is the anti-scramble guard: the order of BEATS is fixed; exploration is free only WITHIN the active beat.
2. **Explore in any order.** Within the active beat, the player may visit its rooms in any order (subject to key/gate notes per room).
3. **CLEAR-GATE before advancing.** Each beat marks some rooms `⛔ CLEAR-GATE` (must be cleared) and others `○ OPTIONAL`. The beat's EXIT does not fire until **every CLEAR-GATE room is cleared.** Optional rooms (loot, side-rescues) may be skipped — but skipping a rescue has consequences (the occupant's fate is decided), and skipping loot just forfeits it.
4. **A room is "cleared" when:** its enemies are defeated/driven off AND (if it has a rescue target) the target's fate is resolved (saved / lost / left). Loot is offered on clear (AUTO-LOOT, never a menu gate). "Defeated" includes killed/captured/fled per § Adversary Morale. ⛔ **Every defeated enemy drops loot — killed/disabled = FULL; FLED = PARTIAL (the gear they shed running: dropped weapon + a few coins, ~⅓–½ of their kit), never "nothing"** (KM_ClaudeInstructions AUTO-LOOT). So a corner where some assassins flee still leaves a scatter of dropped loot behind.
5. **Dispatch is optional.** The player can personally clear every room, OR send a companion group to clear one while they take another — see § DISPATCH.

---

## 📐 ROOM SCHEMA — every room is defined with these fields

```
ROOM: <name>  [BEAT: PR_0X]  [CLEAR-GATE | OPTIONAL]
TYPE:    one or more of — ENEMIES · LOOT · RESCUE · ENEMIES+RESCUE(hostage)
FIRE:    NONE | SMOKE | BURNING | INFERNO   (see § FIRE & SMOKE)
ENEMIES: weak ×N (HP/AC, role) · medium ×N (...) · strong/captain ×N (...)   [or NONE]
RESCUE:  who is here — servant / occupant / guest / staff, and their state
LOOT:    items + gold available on clear   [or NONE]
FIREKIT: firefighting items present in THIS room (buckets, water, sand, wet cloth, well) [or NONE]
CLEARED WHEN: <condition>
ON SKIP:  <what happens if the player never enters / leaves it uncleared>
```

### Enemy tiers (the weak / medium / strong split you asked for)
| Tier | Marker | Typical statline (Prologue) | Behavior |
|---|---|---|---|
| **Weak** | `w` | Assassin Rogue 1 — HP 12-14, AC 14-15, dagger +5, Sneak +1d6 | Fights defensively; **breaks/surrenders/flees** per § Adversary Morale, modified by your Mercy Standing |
| **Medium** | `m` | Assassin Fighter 2 / Archer — HP 18-22, AC 16-17 | Holds longer; breaks only at a leader-down / outnumbered trigger |
| **Strong / Captain** | `S` | Cell captain or the Assassin Leader — HP 30-48, AC 17-19, special abilities | Does NOT break on a morale roll — **rallies** weak/medium allies (+2 their morale) and **comments** on your Mercy Standing. Named boss = plot-armored per the beat file |

⛔ **Mindless/fanatic** (the Frost Giant shapeshifter, any summoned thralls) have **no morale** — they never surrender/flee.

---

## 🔥 FIRE & SMOKE — per-room state + how to fight it

Run the mechanical fire hazard from **KM_PR_04 § THE EXPLOSION & FIRE** and **KM_Combat_Systems § FALLS/HAZARDS**. Each room carries a fire state that worsens over time if unfought:

| State | Effect in the room |
|---|---|
| **NONE** | clear air |
| **SMOKE** | concealed + −Perception; **1d6 smoke damage end of each turn**, **halved** by a wet cloth over nose/mouth (1 action) or staying low. ⛔ **UNDEAD (Jaethal) take NO smoke damage and need no wet cloth — they don't breathe** (the 1d6 is inhalation); they are STILL concealed / −Perception (sight) and still burn from actual fire. |
| **BURNING** | as SMOKE + **adjacent to flame = 1d6 fire (basic Reflex ~DC 17)**; catching fire = persistent fire damage |
| **INFERNO** | as BURNING + **inside it = 4d6 (basic Reflex)**; the room **grows ~half-again its burning squares each round** if unfought and will engulf adjacent rooms |

**Spread clock:** a BURNING room left unfought escalates toward INFERNO and bleeds SMOKE into adjacent rooms each round. Fighting it (below) halts/reverses this.

⛔ **THE FIRE IS A HAZARD, NOT A DOOMSDAY CLOCK (player directive 2026-06-22).** Per KM_PR_04 the fire is a **diversion, not a demolition — the manor does NOT burn to the ground.** The spread clock raises STAKES *within a room* (fight it, route around it, lose some staff there if you ignore it) — it does **NOT** end the sweep, auto-lose the Active 5 / civilians, "burn the mansion" to force a finish, or push the player toward the final battle. ⛔ The DM may NOT narrate *"it's all burning, no time, get to the boss"* to rush or skip PR_06 — that is the railroad trick (`.fail 39` + time-skip; see KM_ClaudeInstructions § night-attack). The sweep proceeds **at the player's pace**; the five are FOUND and the people saved-or-lost by the player's choices, never erased by an off-screen inferno. Worst an unfought fire does is consume **one room's** rescuable staff and force a detour — never the chapter.

### 🪣 FIREKIT — items that let you fight the fire MANUALLY
Placed per-room (see each room's `FIREKIT:` line). Using them is an action:
| Item | Effect |
|---|---|
| **Water bucket / filled trough** | Douse 1 burning square (or knock a catching-fire creature's persistent fire) per action |
| **Bucket brigade** (3+ people/companions chained) | Douse the whole room's fire over 1d4 rounds; the dispatched-group version resolves via § DISPATCH |
| **Sand bucket / ash barrel** | Smother an oil/grease fire (kitchen, lamp-oil) — better than water on those |
| **Wet cloak / soaked cloth** | Worn: halve smoke damage; thrown over a burning person: ends their persistent fire |
| **Well / cistern / kitchen water-butt** | Unlimited source — anchors a bucket brigade in that room |
| **Create Water / cold spell** (Aerith, Keqing) | Douses a square per casting; cold "barely helps" per canon — water is the real tool |

⛔ Cold barely helps; **water douses.** A room with NO firekit and no water source can only be fought by spells or by hauling the fire's fuel out — say so honestly.

---

## 🗺️ DISPATCH — send a group to clear ANOTHER room (costs Hero-Point overflow)

The player clears the room they're IN personally. To clear a DIFFERENT room at the same time, **dispatch a companion group** to it. This runs on the existing system — **`KM_MissionResolution.md`** — so it is not a new currency:

**Command:** the existing **`.delegate`** (KM_MissionResolution's dispatch verb) — `.delegate <companions> → <room>` — or just natural language ("send Hu Tao and Keqing to clear the library"). `.dispatch` works as a plain-language alias; do NOT invent a separate mechanic — it routes to `.delegate`/MissionResolution.

**Cost — Hero-Point OVERFLOW (the 📦 bank, NOT the 0-3 combat pool):**
| Group size | Overflow cost |
|---|---|
| 1-2 companions | 1 |
| 3-4 companions | 2 |
| 5+ companions | 3 |
(No distance surcharge inside the manor — all rooms are "Inner Circle," 1-3 hex equivalent.) If overflow is short, the DM warns before confirming.

**⚖️ SIZE ↔ SUCCESS TRADE-OFF (player directive 2026-06-22).** Fewer people = **cheaper but riskier**; more people = **pricier but safer.**
- **More companions** → more overflow spent (table above) BUT a bigger Combat/skill Pool → **higher success, lower injury risk.**
- **Fewer companions** (a lone scout, a pair) → cheap (1 overflow) BUT a thin Pool → **lower success, higher chance of injury/failure.** A solo dispatch into a 3-enemy room is a gamble.
- The DM states the rough odds before confirming ("two of them against three in the library — even money, and someone's likely to come back hurt").

**Resolution (KM_MissionResolution § V-VI, mission type = Clear/Patrol, region = Inner Circle):**
- Build the pool from the dispatched companions (§ III: combat = Σ levels + martial bonuses ÷ 2; or the relevant SKILL pool — see TRAITS below).
- Roll vs the room's Threat Level (set from its enemy tiers: weak ×N + medium ×2 each + strong ×4).
- Outcome tiers (Crushing / Pyrrhic / Retreat / Disaster) → room cleared or not, injuries, gear loss, loot to `pending_loot`.
- A RESCUE room dispatched: the group also rolls to save the occupant (Athletics/Medicine, § IV); failure = occupant lost.
- A BURNING room dispatched with a firekit present: the group runs the **bucket brigade** automatically IF they outnumber the fire; otherwise it's a Pyrrhic-or-worse risk.

**🎯 TRAITS / SKILLS MATTER — match the group to the room's challenge (player directive 2026-06-22).** The room's type decides which abilities boost the dispatched group's roll; sending the RIGHT people raises success (and sending the wrong ones wastes the trip):
| Room challenge | What helps the dispatched group |
|---|---|
| **FIRE** | a caster who can **make water** (a cleric with *create water*, Keqing's/Aerith's water magic) = **big bonus / can auto-douse**; Survival (firefighting); + extra bodies for a bucket brigade |
| **needs STEALTH** (slip in, ambush, no alarm) | **Stealth**-trained members — sneak past or open with surprise (Yor, Keqing) |
| **SEARCH / loot / secret / find** | **Perception / Investigation / Thievery** — finds the cache, the hidden room, the disarm |
| **COMBAT clear** | **martial** classes (the combat pool — Hu Tao, Amiri, Jaethal) |
| **RESCUE / extract** | **Athletics** (haul them out) + **Medicine** (stabilize the wounded) |
| **locked / trapped** | **Thievery** (disable device / pick) |
⛔ Apply the matching skill as the pool (or a circumstance bonus) — a cleric sent to a fire should clearly outperform a barbarian sent to the same fire. State *why* it worked or didn't ("Aerith's water turned it fast" / "no one you sent could read the lock").

**🥷 STEALTH OPENER — a free first hit, and backstabbers pre-kill BEFORE the math (player directive 2026-06-22).** If the dispatched group enters with **Stealth** (Stealth-trained members, going in quiet, room not already alerted — a clanking heavy-armor group can't, and forfeits this):
- They land the **first hit free** — a surprise opening blow / advantage before anyone reacts.
- If a member has **Backstab / Sneak Attack (a rogue/assassin — Yor, a flipped seeker)**, that surprise strike is an **assassination** (§ GHOST/STEALTH-KILL): it **KILLS one unaware enemy OUTRIGHT, before the resolution math runs.** **Subtract that enemy from the room's Threat Level, THEN roll** the success check against the reduced count. So a stealthy assassin thins the room before the dice — sending Yor to a room of 3 mooks means she opens by dropping one silently, then the group rolls against 2.
- **Caps (don't trivialize):** **one pre-kill per backstabber**, and only on **WEAK mooks** — a **STRONG/captain** or a **mindless thrall** is NOT dropped by a single surprise backstab (at most knocked to off-guard / its tier shaved). Can't zero out a whole room with one rogue.
- A **LOUD** entry (no Stealth, heavy-armor group, or an already-alerted room) gets **no opener** — straight to the roll.

**☠️ FAILURE INJURES THEM — AND THEY'RE OUT FOR THE NIGHT (player directive 2026-06-22).** A failed dispatch (Tactical Retreat / Disaster, or a Pyrrhic win) returns the group **injured** — and for the night attack that means **they cannot continue: out of action for the rest of the assault** (can't be re-dispatched, can't fight in PR_07) until healed. Bigger groups absorb this better (one of several hurt); a solo/pair that fails is simply **down**. Render the cost — a dispatched friend can come back bloodied and benched, which is the real stake of sending too few.

**Return report:** lead with the **PLAY-BY-PLAY (§ below)** — the beat-by-beat of how they handled the room and which trait carried each beat — then the § XII tail (CASUALTIES / GEAR LOSS / REWARD). The dispatched group is **unavailable** until they report back (1 beat / next exchange); an injured one stays unavailable for the night.

⛔ **Dispatch does NOT skip a CLEAR-GATE's mandatory scripted content.** If a room holds a mandatory beat (e.g. PR_06 trap-corridor Tartuccio refusal, the armory gold choice), dispatching CANNOT auto-resolve that beat — the player must be present for it. The DM offers dispatch only for rooms whose clearing is pure combat/rescue/fire, and says so for the scripted ones ("that one you'll want to handle yourself").

⛔ **Dispatched groups obey § Adversary Morale too** — a no-quarter Mercy Standing means the enemies they hit are more likely to fight to the death (tougher Threat Level), a merciful one means more surrenders (easier). Note it in the return report.

---

## 🔎 DESTINATION CLUES — read the manor before you commit (player directive 2026-06-22)

⛔ **Whenever the player is choosing where to go next** (the room/direction menu) **or where to dispatch a group, each available destination shows a SENSORY CLUE** — a partial, readable hint of what's in that room — so the choice is informed, not blind. (This is what lets the player route the cleric toward the fire and the rogue toward the silence.)
- The clue is **sensory and partial** (a sound, a glow, a smell, a glimpse) — NOT a full readout. Exact enemy count / who's there is learned on **ENTRY.**
- It telegraphs the room's **TYPE**: a FIGHT (steel on steel, a war-shout), a FIRE (orange glow under the door, smoke, a scream), a trapped ALLY (a companion's battle-cry — "someone's holding that room"), a RESCUE (a muffled struggle, a whimper — "someone pinned/hiding"), STEALTH-needed (silence, then a single bowstring — "a shooter on the angle"), or quiet LOOT (undisturbed, still).
- **Examples to render in the menu:**
  - *Library — steel ringing, a woman shouting orders (someone is fighting in there).*
  - *Kitchens — orange light under the door, smoke curling out, a scream cut short (fire; people trapped).*
  - *Trap corridor — dead quiet, then one bowstring release (a shooter holding the angle).*
  - *Cellar stairs — scuffling, a whimper (someone hiding — or held).*
- **PERCEPTION upgrades the clue:** a strong passive/Seek sharpens it (count the voices, name a companion's voice vs an enemy's, smell the lamp-oil accelerant); a poor read gives only the vague version. ⛔ Never give a *full* readout for free — the clue narrows the choice, the room reveals the detail.

---

## 📋 PLAY-BY-PLAY — how a group/character handled a location (player directive 2026-06-22)

When a **dispatched** group resolves a room (the player wasn't there to watch) — and, on request, when the player's **own** group clears one — render a **beat-by-beat account that breaks the location into its ELEMENTS and names the TRAIT/skill/ability that carried each beat.** This is what makes loadout choices feel real: you sent the cleric *because* of the fire, and the report shows her water doing the work.

**Format:**
```
📋 PLAY-BY-PLAY — [Location] · [who went]
  • [Element] → [who] · [trait/skill used] → [outcome]      (one line per element)
  • …
  ▸ RESULT: Cleared / Partial / Failed · [who's hurt → benched] · [loot → 🎒 queue]
```

**Rules:**
- **One beat per ELEMENT** the room actually had (the approach, the lock/trap, the fire, the enemies, the rescue, the loot) — in the order they hit them. Don't invent elements the room doesn't have; don't skip ones it does.
- **Attribute each beat to a person + the trait that resolved it** — *Stealth* opened it, *create water* / Survival killed the fire, *Sneak Attack* dropped the first man, *Athletics* hauled the trapped clear, *Medicine* stabilized, *Perception/Thievery* found/disarmed, *combat* finished the rest. If a beat **failed**, say which trait was MISSING ("no one you sent could read the lock").
- Keep it **tight** — bullet beats, not full prose (especially for off-screen dispatch; it's the digest). The player's *present* group can get fuller scene prose, but the same element→trait→outcome spine.
- End with the **▸ RESULT line** (the § XII tail folds in here: cleared/partial/failed, injuries → who's benched for the night, loot → the queue).

**Worked example (dispatch — Yor + Aerith to the Kitchens: fire + 3 trapped staff):**
```
📋 PLAY-BY-PLAY — Kitchens (BURNING, 3 staff trapped) · Yor Forger, Aerith
  • Jammed door, heavy smoke → Yor · Stealth + Athletics → slips the fallen beam, opens a path low under the smoke
  • The grease fire (BURNING→Inferno risk) → Aerith · create water + the sand barrels → doused over 2 rounds, no spread
  • Reach the 3 in the pantry passage → Aerith · Athletics through smoke (wet cloth, stay low) → two pulled clear
  • Third, beam-pinned, ankle caught → Yor · Athletics → levered free, singed but breathing
  ▸ RESULT: CLEARED · 3/3 staff saved · Aerith took smoke (Minor) → benched for the night · loot: brass pot, 4 sp → 🎒 queue
```
(Had you sent two barbarians instead: the fire beat would read *"no water, no firefighting skill — bucket-brigade only, lost ground"* → Partial, a staff member lost. That contrast is the point.)

---

## 👥 POPULATION RULE — EVERY ROOM IS OCCUPIED (player directive 2026-06-22)

⛔ **No empty rooms.** Every explorable room in the night attack holds **at least 1–2 "people" or a fire** — content the player can act on. One or more of:
- **FIGHT** — enemies (assassins / the leadership) to defeat;
- **UNIFY** — an ally/companion to reach and rejoin (the Active 5 corners + any guard/staff who'll fall in);
- **RESCUE** — civilians, servants, guests, or wounded staff to save (1–3 per rescue room);
- **FIRE** — a burning/smoking room to fight with the firekit.
A room that's just walls and loot is under-populated — give it a person or a fire. The manor is full of bodies the night it's attacked: attackers, defenders, terrified staff, trapped guests.

## 🎖️ ENEMY BUDGET — scaled up (the bigger raid)

Total attackers = **~22 assassins + 1 Assassin Leader (captain) + 1 Frost Giant shapeshifter (Jamandi's) + 3 summoned Rift Channelers.** (Roughly doubled from the old 11 — a real break-in, not a handful. Still canon-bounded: the DM distributes from THIS budget and does not free-spawn beyond it; the scope-lock bans inventing *extra* cells/fronts, KM_ClaudeInstructions § NIGHT-ATTACK SCOPE LOCK.) ⛔ Yor's "eleven counted in" was her **partial vantage** from the courtyard — the ones SHE saw enter, not the whole cell; the full force is larger (update her line to "at least eleven through my angle — there were more").

| Beat | Assassins here | Distribution (1–3 per combat room) |
|---|---|---|
| PR_04 guest floor | 3 | guest room (Vell, 1) + landing/stairhead (1) + a 2nd-room pair sweeping the floor (1) |
| PR_05 corridor | 3 | Brannic (Fighter) + Sable (Archer) + 1 more closing from the junction |
| PR_06 sweep | 13 | Library 3 · Trap Corridor 3 · Ballroom 2 · Courtyard 1 (Yor's captive) + service-wing rooms (cellar / servants' hall / chapel / gallery) ~1–2 each · Kitchen 0 (the FIRE) |
| PR_07 banquet | 3 elite + leadership | Assassin Leader (S) + 3 elite bodyguards (m) + 3 Rift Channelers (thralls) + Frost Giant (Jamandi's) |
**≈ 3 + 3 + 13 + 3 = 22 assassins**, + Leader + 3 elite guards merged into PR_07, + 3 thralls + the Giant.

⛔ **Plus the NON-enemy population (this is the point of the rule):** the **5 companions to unify** (corners), **Tartuccio** (PR_05 rescue), and **civilians/staff to rescue scattered through the rooms** — the kitchen's 9+3 staff, the ballroom's 14 guests + 3 paralyzed, library clerks, a barricaded envoy, servants hiding in closets and cellars (1–3 per rescue room). The manor should feel FULL — every door opens on a fight, a friend, someone to save, or flames.

---

## 🗡️ NAMED ROSTER — THE CELL (builds, canon-consistent)

> A **professional, Pitax-funded, courier-separated** cell — Restov-hired through intermediaries, **no insignia**, each man knowing only his task + his handler's face (the knowable-facts ceiling; none can name the patron / "C" / Pitax beyond supply). Names are field-names; use them so kills/captures land on a person, not a token — **and so they address EACH OTHER by name when they speak** (warnings, rallies, the pre-combat banter): *"Sable, hold the angle"* / *"Brannic's down — fall back."* Men who worked a job together use names; rendering named cell members as faceless "the assassin says" is `.fail 9` (see `KM_Combat_Systems.md § PRE-COMBAT`). Stats match the per-room briefs.
> ⛔ **These named ones are the NOTABLES (~11 of the ~22). The rest are unnamed rank-and-file** — same Rogue 1 statline (HP 12–14, AC 14–15, dagger +5, Sneak +1d6) — filling the bumped budget per the POPULATION RULE: 1 more on the guest floor, 1 closing the corridor, and 1–2 in each PR_06 **service-wing room** (cellar / servants' hall / chapel / gallery). Give a notable a name; a faceless mook can stay "an assassin," but each is still a tracked body with HP. The PR_07 **3 elite bodyguards** (Fighter 2, HP 22, AC 17) flank Sere Maroc — name them if the player engages them directly.

**PR_04 — Guest Floor**
- **Vell** — *Poisoner-Rogue 1.* HP 12 · AC 15 · Dagger +5 (1d4+2 P) · Sneak +1d6. Carries a coated blade (the **Ungol Dust variant** poison — canon, named). Close-work specialist, NOT a brawler: fights defensively, was sent to kill a sleeper, not win a duel. Knows: hired in Restov via intermediary, his handler's face.

**PR_05 — Corridor**
- **Brannic** — *Assassin Fighter 2 (blocker).* HP 22 · AC 17 · Twin short blades +9 (1d6+4 P) · holds the hall, Attack of Opportunity. The cell's muscle — disciplined, trained, doesn't panic.
- **Sable** — *Archer 1.* HP 14 · AC 14 · Shortbow +5 (1d6 P, range 60). Covers the corridor's long angle; runs rather than brawls if the line closes.

**PR_06 — Manor Sweep (the eight)**
- *Library (3 — Hu Tao's kills):* **Toskar**, **Renno**, **Gisk** — *Rogue 1 each* (HP 12–14 · AC 14–15 · dagger +5 · Sneak +1d6). Renno carries a poisoned blade (the toxin Hu Tao notes).
- *Trap Corridor (3 — Keqing's kills):* **Quennel**, **Marl**, **Hespin** — *Rogue 1 each* (one arrow each, through the arrow-slit). Were moving in threes toward the residential wing.
- *Ballroom gallery shooter (1):* **Wrenn** — *Rogue 1, dart specialist.* HP 12 · AC 15 · paralytic-dart fan (the reversible toxin that dropped 3 guests). Perched high, ranged; flees the face before he's seen unless dropped.
- *West Courtyard (1 — Yor's captive):* **Garran** — *Rogue 1*, taken alive, bound and gagged. Interrogation value (method + handler's face only — ceiling-bound).
- *Kitchen (0):* the **arsonist** — already slipped out; no fight here, the FIRE is the hazard. (If the player intercepts the diversion early, he's the catchable disposable: `arsonist_caught`.)

**PR_07 — Banquet Hall (leadership)**
- **Sere Vanth Maroc** — *Assassin Leader: Rogue/Sorcerer 4 (captain — the STRONG tier).* HP 48 · AC 19 · Fort +4 / Ref +9 / Will +6 · Rapier +8 (1d6+4 P) · Sneak +2d6 · **Mirror Image (3 images on entry)** · spells: *Mirror Image, Protection from Good, Cause Fear*. Loot: Bracers of Armor +1, Potion of Barkskin, Alchemist's Fire, Acid Flask ×2. Does NOT break on a morale roll — **rallies** the rank-and-file and **comments on your Mercy Standing**. Knows his handler + the method, NOT the patron (ceiling).
- **The Three Channelers** (Rift Channelers ×3) — *Summoner thralls, conjured — not men, not named individuals.* HP 16 · AC 13 · Claw +4 (1d6+2 S) · **Summon Fiendish Creature** (1 each if not killed fast). ⛔ **No morale** — fight to destruction.
- **"Aldous Kerne"** — *the shapeshifter.* Walks in as a late-arriving guest; in PR_07 he reveals as a **FROST GIANT** (true form: HP 62 · AC 17 · Greataxe +10 [1d12+8 S, reach 10 ft] · Knockdown on crit). ⛔ **JAMANDI'S FIGHT — the player CANNOT target him** (`.fail 35`); Jamandi duels him solo (scripted, verbatim). "Aldous Kerne" is a cover name, no such guest exists.

---

## ════════ PR_04 — GUEST FLOOR (room set) ════════

> The manor's upper guest floor, the night of the attack. eRmaC's room is the start. Smoke is just beginning to climb the stairwell from the fire below; the guest floor itself is not yet burning. **CLEAR-GATE: the guest room.** Everything else here is OPTIONAL — explore or push straight to the stairwell/corridor (→ PR_05).

```
ROOM: eRmaC's Guest Room        [PR_04]  ⛔ CLEAR-GATE  (the tutorial fight)
TYPE:    ENEMIES
FIRE:    NONE → SMOKE creeping under the door after ~2 rounds (stairwell below is alight)
ENEMIES: weak ×1 — Assassin Rogue 1 (HP 12-14, AC 14-15, dagger +5, Sneak +1d6).
         Fights defensively; flees/surrenders below 6 HP per Adversary Morale + Mercy Standing.
RESCUE:  none here (chronicler-NPC ONLY in a Linzi run — see PR_04 § CHRONICLER GATE; absent in a replacement run)
LOOT:    on the assassin — 3 gp, dagger, leather armor (AUTO-LOOT, killed OR captured)
FIREKIT: water ewer + washbasin (1 square douse) ; the bed-sheet can be soaked → wet-cloth
CLEARED WHEN: the assassin is defeated (killed / captured / driven out the window)
ON SKIP: cannot skip — this is Encounter 1, the tutorial fight (KM_PR_04)
```
```
ROOM: Guest Floor Landing / Stairhead   [PR_04]  ⛔ CLEAR-GATE (the exit toward PR_05)
TYPE:    LOOT (transit)
FIRE:    SMOKE — black accelerant smoke climbing the stairwell; danger here is smoke, not flame
ENEMIES: NONE (the corridor pair is PR_05, past the stairhead)
RESCUE:  none
LOOT:    a knocked-over guest's travel case — 8 gp + a Minor Healing Potion (Perception DC 10 in the smoke)
FIREKIT: a fire-bucket on a wall hook by the stairs (filled) — grab it to carry one douse downstairs
CLEARED WHEN: player crosses to the stairhead and chooses to descend → loads PR_05
ON SKIP: this IS the exit; passing through it is how PR_04 ends. Smoke deals 1d6/round if the player lingers.
```
```
ROOM: Adjacent Guest Room (the envoy's)   [PR_04]  ○ OPTIONAL
TYPE:    RESCUE
FIRE:    NONE (interior room, door shut)
ENEMIES: NONE
RESCUE:  a minor visiting envoy + his manservant, barricaded, panicking. Saving = escort them to the
         stairhead (they follow). They are non-combat; they remember it (small reputation/witness beat).
LOOT:    NONE (they keep their own purse; looting frightened guests = Ruthless +1 + public-rep hit if it spreads)
FIREKIT: NONE
CLEARED WHEN: envoy escorted to the stairhead OR player chooses to leave them (they shelter in place)
ON SKIP: they survive IF the guest floor doesn't reach BURNING (it won't this beat) — so skipping is safe here,
         but escorting them is a Merciful +1 and a public-reputation seed ("he came back for us")
```
```
ROOM: Linen & Store Closet        [PR_04]  ○ OPTIONAL
TYPE:    LOOT + FIREKIT cache
FIRE:    NONE
ENEMIES: NONE
RESCUE:  none
LOOT:    spare bedlinens, a sealed bottle of lamp-oil (hazard if near fire), 4 sp, a Tindertwig ×3
FIREKIT: **a full water-butt + two buckets + a stack of cloths** — the floor's firefighting cache.
         Soaking cloths here = wet-cloth for everyone (halve smoke for the party for the descent).
CLEARED WHEN: searched (nothing to fight)
ON SKIP: forfeit the firekit cache; the descent through smoke is then unmitigated (1d6/round, no halve)
```

**PR_04 advance:** when the guest room is cleared AND the player crosses the stairhead to descend → **load KM_PR_05_corridor_rescue.md.** Optional rooms may be done first or skipped. Dispatch is generally moot on this floor (the player has no group yet — companions are scattered; Jaethal-on-patrol may be dispatched to escort the envoy if the player posted her).

---

## ════════ PR_05 — RESIDENTIAL CORRIDOR (room set) ════════

> The smoke-filled corridor below the guest floor. Two assassins block the hall; **Tartuccio is pinned in an alcove** (the mandatory rescue). Fire is closer here — the stairwell behind glows. **CLEAR-GATE: the corridor + the Tartuccio rescue + the ring decision** (all per KM_PR_05; load it). No dispatch this beat — the player's companions are still scattered (they rejoin in PR_06).

```
ROOM: The Corridor              [PR_05]  ⛔ CLEAR-GATE
TYPE:    ENEMIES
FIRE:    SMOKE (heavy — 1d6/round, halved with a wet cloth) ; the stairwell end is BURNING
ENEMIES: medium ×2 — Assassin Fighter 2 (HP 22, AC 17, blocks the hall) + Assassin Archer 1
         (HP 14, AC 14, shortbow +5, far end). Hold longer than weak; break only at leader-down/outnumbered.
RESCUE:  none (Tartuccio is the next room)
LOOT:    Fighter — 12 gp, short sword, a dart-vial (the paralytic; skill-gated ID). Archer — shortbow + 15 arrows, 6 gp
FIREKIT: a wall fire-bucket (filled) mid-corridor ; a window the player can throw open (1 action) to VENT smoke a step
CLEARED WHEN: both assassins defeated (killed / captured / fled per § Adversary Morale)
ON SKIP: cannot skip — the corridor is the path and the archer keeps firing
```
```
ROOM: Tartuccio's Alcove        [PR_05]  ⛔ CLEAR-GATE  — ⛔ MANDATORY, NOT DISPATCHABLE
TYPE:    RESCUE
FIRE:    SMOKE
ENEMIES: none directly (the corridor pair were converging on him)
RESCUE:  Tartuccio — pinned, unharmed, frightened. The UNKILLABLE Ch1 antagonist. His rescue + the
         RING DECISION are load-bearing for PR_09. He stays back, comments, does NOT fight.
LOOT:    the ring — the ring-choice menu is MANDATORY (equipped / carried / refused, per KM_PR_05)
FIREKIT: none
CLEARED WHEN: Tartuccio rescued AND the ring decision made (mandatory menu)
ON SKIP: ⛔ CANNOT skip or dispatch — the player runs the rescue + ring personally (scripted, PR_09-critical)
```
```
ROOM: Servants' Stair (side)    [PR_05]  ○ OPTIONAL
TYPE:    LOOT
FIRE:    BURNING (the fire is climbing here) — risky
ENEMIES: none
RESCUE:  none
LOOT:    a dropped strongbox on the steps — 40 gp + Lesser Healing Potion ×2 — but it sits in a BURNING
         square (1d6 fire, basic Reflex). Douse it first with the corridor bucket to grab it safely.
FIREKIT: none here (the fire owns this stair)
CLEARED WHEN: searched (or skipped)
ON SKIP: forfeit the strongbox — the servants' stair fully engulfs by PR_06 (no second chance)
```

**PR_05 advance:** corridor cleared + Tartuccio rescued + ring chosen → **load KM_PR_06_manor_sweep.md.**

---

## ════════ PR_06 — MANOR SWEEP (room set — the DISPATCH centerpiece) ════════

> Five companion corners + the Armory + the Secret Room. **This is where dispatch shines:** take one corner yourself and **dispatch groups to the others** (Hero-overflow cost, § DISPATCH), or clear them all in person. ⛔ **Each corner has a FIXED encounter state** — *battle-beginning, mid-battle, or already-cleared* — so arrival varies and feels alive **without DM improvisation** (do not re-roll or change a corner's state). Helping a fighting companion = **they JOIN you.** **CLEAR-GATE: all five corners resolved (companion rejoined).** The Armory gold choice and the Trap-Corridor Tartuccio refusal are mandatory scripted beats (NOT dispatchable). Five-corner narration + the rejoin scripts live in KM_PR_06 — this is the combat/fire/loot/dispatch layer over them.

### 🧮 FORCE DISTRIBUTION — your people are SPREAD across the five corners

The explosion scattered everyone. Your companions are not in one place — they're **divided across the five reunion areas**, each holding (or fighting for) a corner. The split is **by percentage of your available companion force**, so a bigger entourage means bigger groups per corner, not the same five singletons.

**Who counts as "available force":** the **Active 5** are the fixed **ANCHORS** — one is always in their own canon corner (Hu Tao→Library, Keqing→Trap, Yor→Courtyard, Aerith→Kitchen, Leliana→Ballroom), regardless of percentages. **Any ADDITIONAL declared companions present for the night** (flipped seekers, planted recruits — whoever the save lists as in the manor) are the ones distributed by the % weights below, layered ON TOP of the anchors.

**Default distribution (weighted by each corner's need — sums to 100%):**
| Corner | Weight | Why |
|---|---|---|
| **Ballroom** | 25% | most people to hold — 14 guests under guard |
| **Kitchens** | 25% | fire + mass rescue — labor-intensive |
| **Library** | 20% | active fight + chokepoint + intel |
| **Trap Corridor** | 15% | one sniper holds it; traps, not bodies |
| **West Courtyard** | 15% | perimeter / already largely handled |

**How to apply it (deterministic — no DM guessing):**
1. Count `extra_companions` = declared companions present for the night **minus** the 5 anchors.
2. Each corner's extra group = `round(extra_companions × weight)`. Assign the rounding remainder to the highest-weight corners first (Ballroom → Kitchen → Library).
3. A corner's **total holders = its anchor (1) + its extra group.**
4. ⛔ The player may **REASSIGN** before/while sweeping — pull people off a quiet corner to reinforce a hot one, or pool them for a dispatch. Honor the player's reassignment over the default split. The default is the *starting* deployment, not a lock.

**What the distribution DOES (ties to the rest of the system):**
- **Strength of each corner** = its holder count → feeds the § DISPATCH combat pool and whether a corner is **understrength** (needs the player's help to clear) or **self-clearing** (the group handles it; the player just collects the reunion + loot).
- **Help-them-they-join still applies per anchor** — reinforcing or relieving an anchor's corner is what rejoins that Active-5 companion.
- A corner left **understrength and unattended** (player neither goes nor dispatches) can go badly — the fire spreads (Kitchen), guests scatter (Ballroom), per each room's `ON SKIP`.

**Worked examples:**
- *Active 5 only (no extras):* `extra = 0` → every corner = its 1 anchor. The baseline canon spread (one companion per corner).
- *Active 5 + 5 flipped seekers = 10 available, extra = 5:* Ballroom +1, Kitchen +1, Library +1, Trap +1, Courtyard +1 → each corner = 2 holders (anchor + 1). Roughly even at this size.
- *Active 5 + 9 extras (full 14 roster) = extra 9:* Ballroom +2, Kitchen +2, Library +2, Trap +1, Courtyard +1 (remainder of 1 → Ballroom = +3) → Ballroom 4, Kitchen 3, Library 3, Trap 2, Courtyard 2. Now you have real groups to dispatch with.

⛔ The Active-5 anchor is NEVER moved out of their own corner by the percentage math (their rejoin scene is fixed to their room); only the EXTRA companions distribute and reassign. If only the Active 5 are present, this whole layer collapses to the canon one-per-corner and can be skipped.

```
ROOM: Library / East Study — Hu Tao      [PR_06]  ⛔ CLEAR-GATE
STATE:   ⚔️ MID-BATTLE — you arrive as she drops the last of them.
TYPE:    ENEMIES + RESCUE
FIRE:    SMOKE (east window blown in, smoke feeding through)
ENEMIES: weak ×3 total — 1 already down; **2 still up** when you arrive. Help her finish → **Hu Tao JOINS.**
RESCUE:  two clerks + a steward in the back stacks (alive, frightened) — escort to a safe room or shelter in place
LOOT:    household ledgers (PR_09 evidence value) + the assassins' kit (~9 gp, 2 daggers, leather armor)
FIREKIT: water ewer on the reading table ; the lamp-oil pool needs smothering — haul the rug over it (no sand here)
CLEARED WHEN: the 2 remaining assassins defeated + clerks' fate resolved + Hu Tao rejoined
ON SKIP: can't skip (CLEAR-GATE). DISPATCHABLE (combat+rescue) — the dispatched group helps Hu Tao; she joins on their return
```
```
ROOM: Trap Corridor (upper) — Keqing     [PR_06]  ⛔ CLEAR-GATE  — needs Watchkeeper's Key (Armory)
STATE:   ✅ ALREADY CLEARED (enemies) — she sniped all three; the TRAPS are the live challenge.
TYPE:    HAZARD + RESCUE(companion)
FIRE:    NONE (stone passage)
ENEMIES: weak ×3 — all DOWN (Keqing's arrows). No combat. 3 pressure-plate traps (DCs per KM_PR_06).
RESCUE:  Keqing — held the angle from above; descends once the corridor is safe.
LOOT:    on the 3 bodies — ~9 gp, marked gear (Recall Knowledge)
FIREKIT: none
CLEARED WHEN: traps disarmed/bypassed + Keqing descends (rejoined)
ON SKIP: can't skip. ⛔ NOT cleanly dispatchable — the Tartuccio-refusal beat fires if the player sends him first;
         trap-solving is a player beat. (A group MAY be sent to escort Keqing down once traps are handled.)
```
```
ROOM: West Courtyard — Yor Forger        [PR_06]  ⛔ CLEAR-GATE
STATE:   ✅ ALREADY CLEARED + PRISONER — Yor handled hers outside; holds a bound, gagged assassin.
TYPE:    RESCUE(companion) + DECISION(prisoner)
FIRE:    NONE (outside; smoke drifts over the wall)
ENEMIES: weak ×1 — CAPTURED, alive (Yor's prisoner). Player decides his fate (interrogate / send to hall / kill).
RESCUE:  Yor + the prisoner (interrogation = intel value for PR_09)
LOOT:    staging-point find — rope grapnels, a cell member's pack (Society RK), 5 gp
FIREKIT: the courtyard FOUNTAIN — a water source that can anchor a bucket brigade for adjacent burning rooms
CLEARED WHEN: prisoner's fate decided + Yor rejoined
ON SKIP: can't skip. Dispatch N/A (she's already done) — this corner is a conversation/decision; handle in person or she walks to you
```
```
ROOM: Kitchens / Pantry Fire — Aerith    [PR_06]  ⛔ CLEAR-GATE
STATE:   🔥 CRISIS BEGINNING — the fire is actively spreading; the "battle" here is against the FIRE, not men.
TYPE:    RESCUE (+ FIRE)
FIRE:    BURNING → INFERNO risk (grows each round unfought; this is the alignment-track moment)
ENEMIES: none (the fire-setter already slipped out — the paralytic graze is the only trace, a PR_09 lead)
RESCUE:  3 kitchen staff still inside the burning pantry-passage (+ the 9 Aerith already pulled to the back court)
LOOT:    silver chest in the side pantry (looting it DURING the rescue = Chaotic +1)
FIREKIT: **the kitchen water-butt + buckets + SAND barrels** (sand = best on the grease/oil fire) — a full
         firefighting station. Bucket-brigade the room, or dispatch a group to do it.
CLEARED WHEN: fire fought down + the 3 staff saved-or-lost (alignment-track choice, KM_PR_06) + Aerith rejoined
ON SKIP: can't skip. DISPATCHABLE (fire+rescue) — a group with this firekit auto-runs the brigade if they
         outnumber the fire; otherwise Pyrrhic (one staff member lost). Letting it burn = staff die (Chaotic).
```
```
ROOM: Ballroom — Leliana                 [PR_06]  ⛔ CLEAR-GATE
STATE:   ⚔️ MID-BATTLE — the masked gallery shooter is still up; Leliana is holding the guests.
TYPE:    ENEMIES + RESCUE
FIRE:    SMOKE (fire through the high windows)
ENEMIES: weak ×1 — the gallery shooter (paralytic darts, perched high — a ranged duel). Drop him → **Leliana is freed to JOIN.**
RESCUE:  14 conscious guests (held in a half-circle under Inspire Courage) + 3 paralyzed guests (reversible) —
         moving them to Hu Tao's secured library (if rejoined) is the play
LOOT:    the shooter's dart-bandolier (paralytic — skill-gated ID, PR_09 lead) + a dropped purse, 10 gp
FIREKIT: the smashed wine-fountain (a water source, ironically) — usable on the smoke
CLEARED WHEN: gallery shooter defeated + guests secured + Leliana rejoined
ON SKIP: can't skip. DISPATCHABLE (combat+rescue) — but the player gets Leliana's reunion beat on the group's return
```
```
ROOM: The Armory                          [PR_06]  ○ "optional" but GATES the Trap Corridor (holds the Key)
TYPE:    LOOT + ⛔ mandatory gold-choice beat
FIRE:    NONE
ENEMIES: none
RESCUE:  none
LOOT:    Composite Longbow + 20 arrows, Light Mace, Banded Mail, Breastplate, Tower Shield ;
         chest = 210 gp + Watchkeeper's Key
FIREKIT: none
CLEARED WHEN: entered — ⛔ the Tartuccio GOLD CHOICE fires here (mandatory; sets the PR_09 Rebuttal-2 DC; NOT dispatchable)
ON SKIP: skipping forfeits the gear AND the Key (Trap Corridor then unreachable → can't rejoin Keqing) — effectively required
```
```
ROOM: Secret Room (upper-study north wall)  [PR_06]  ○ OPTIONAL
TYPE:    LOOT (puzzle)
FIRE:    NONE
ENEMIES: none / RESCUE: none
LOOT:    Masterwork Longsword + Gold Ring 45 gp (puzzle 1) ; Silver Earrings 25 gp + 35 gp lockbox (puzzle 2) ; +75 XP
FIREKIT: none
CLEARED WHEN: found (Perception DC 13) + puzzles solved (or skipped)
ON SKIP: forfeit the loot + XP — purely optional
```

**PR_06 advance:** all FIVE corners resolved (companions rejoined) → **load KM_PR_07_final_battle.md.** Dispatch freely on **Library / Kitchen / Ballroom**; **Trap / Courtyard / Armory** hold scripted beats that need the player present.

---

## ════════ PR_07 — BANQUET HALL (room set — the final battle) ════════

> The climactic set-piece. Mostly **one room** — the banquet hall — plus two tactical positions. Less exploration, more the fixed battle: the **Assassin Leader** (captain), **3 Rift Channelers** (thralls — no morale), and the shapeshifter that reveals as the **Frost Giant** — which is **JAMANDI'S fight** (player CANNOT target it, `.fail 35`). Dispatch is largely unavailable — the party fights together. **CLEAR-GATE: the hall** (Leader + thralls down; the Frost Giant resolves via Jamandi's scripted duel). Mandatory loot window before PR_08.

```
ROOM: The Banquet Hall          [PR_07]  ⛔ CLEAR-GATE
TYPE:    ENEMIES
FIRE:    SMOKE at the edges (fire through the high windows; the center is clear for the fight)
ENEMIES: strong/captain ×1 — Assassin Leader (Rogue/Sorcerer 4, HP 48, AC 19, Mirror Image ×3, rapier +8,
         Sneak +2d6). Does NOT break; **COMMENTS on your Mercy Standing**; rallies any survivors.
         + thrall ×3 — Rift Channelers (HP 16, AC 13, claw +4; ⛔ NO morale — never flee/surrender; Summon if not killed fast).
         + the Frost Giant (shapeshifter true form, HP 62) — ⛔ JAMANDI'S FIGHT ONLY; player cannot target (`.fail 35`).
RESCUE:  the rejoined Active 5 fight alongside ; Jamandi duels the Giant solo (scripted, verbatim per KM_PR_07)
LOOT:    ⛔ mandatory loot window AFTER — Leader: Bracers of Armor +1, Potion of Barkskin, Alchemist's Fire, Acid Flask ×2.
         Frost Giant: Greataxe (1d12 S), Chainshirt (AC +3)
FIREKIT: hall staff water-jugs along the walls (edge-smoke control) — not central to the fight
CLEARED WHEN: Assassin Leader + 3 Channelers defeated AND Jamandi's duel resolves (scripted)
ON SKIP: cannot skip — this is the climax; player must explicitly state done (after the loot window) before PR_08 fires
```
```
ROOM: The Gallery (above the hall)  [PR_07]  ○ OPTIONAL tactical position
TYPE:    POSITIONING
FIRE:    SMOKE
ENEMIES: none (the gallery shooter, if not already dropped in PR_06, has fled by now)
RESCUE:  none
LOOT:    sniper's-nest leftovers — 8 arrows, a discarded mask (PR_09 flavor)
FIREKIT: none
CLEARED WHEN: optional — taking the high ground grants **+1 to ranged attacks** into the hall
ON SKIP: no penalty — purely a tactical option
```

> **Head Table / Jamandi's position** — context, not a clear-room. Where Jamandi stands when the shapeshifter reveals; the Frost Giant turns here. Player does NOT target the Giant. Narrative anchor for the duel, not explorable.

**PR_07 advance:** hall cleared + Jamandi's duel resolved + loot window taken + player states done → **load KM_PR_08_the_calm.md.** Dispatch note: in PR_07 the party fights TOGETHER — the only "split" is sending one ranged companion to the Gallery for the +1.

---

*KM_PR_NightAttack_Rooms.md — Prologue night-attack explorable-room framework | v1.2 (PR_04–07 populated + PR_06 force distribution)*
