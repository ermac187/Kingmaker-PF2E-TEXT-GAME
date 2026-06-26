# KINGMAKER — COMPANION PROFILES (PART A)
## KM_Companions.md | Referenced by: KM.txt
### Used in: All chapters (Pre-Prologue onward)

> **DM: Load ALL five companion files every session:**
> `KM_Companions.md` (this file) | `KM_Companions.md` | `KM_Companions.md` | `KM_Companions.md`
> `KM_Companions_Behaviors.md` — hidden agendas, inter-companion relations, incompatibility system,
> and question-gated dialogue nodes for all companions (single merged file).
> **Part A:** Companion Roster, Relationship System, CRPG Originals (Active 5 stubs, #6 Amiri, #10 Linzi ⭐QL, #66 Nok-Nok, #16 Tristian, #32 Valerie, #20 Harrim)
> **Part B:** #18 Jaethal, #45 Kalikke/Kanerah, #84 Octavia, #48 Regongar + NPC Interaction Dynamics + Tracking Template
> **Scaled Stat Blocks:** For mid/late-game companion combat stats, search **KM_Companions_Behaviors.md** in project knowledge.

---

> **DM INSTRUCTION:** Load alongside KM.txt every session. Voice all companions in character. Track Relationship in JSON Save Block. All companions start Neutral unless a story flag changes this.

---

## 📊 COMPANION ROSTER

| # | Name | Race | Class | Role | First Available |
|---|------|------|-------|------|----------------|
| A1 | Hu Tao | Human (Versatile) | Fighter (Warrior bg) | Frontline Striker | Active 5 (auto-joined) |
| A2 | Keqing | Human (Versatile) | Magus (Laughing Shadow) | Spellstrike Striker | Active 5 (auto-joined) |
| A3 | Leliana | Human (Skilled) | Bard (Maestro) (Entertainer bg) | Support/Bard (chronicler) | Active 5 (auto-joined) |
| A4 | Yor Forger | Halfling (Gutsy) | Rogue Thief (Criminal bg) | Skirmisher | Active 5 (auto-joined) |
| A5 | Aerith | Human (Skilled) | Cleric Cloistered (Acolyte bg) | Healer | Active 5 (auto-joined) |
|  6 | Amiri | Human (Kellid) | Barbarian (Giant Instinct) | Frontline Striker | Prologue |
| 10 | Linzi | Halfling | Bard (Maestro) | Support/Chronicler | Prologue ⭐ (QL) |
| 66 | Nok-Nok | Goblin | Rogue (Scoundrel) | Skirmisher/Striker | Ch2 ⭐ |
| 16 | Tristian | Human | Cleric (Cloistered) | Healer/Support | Ch1 — Temple of the Elk ⭐ |
| 32 | Valerie | Human | Fighter | Tank/Shield Wall | Prologue |
| 20 | Harrim | Dwarf | Cleric (Warpriest) | Debuffer/Controller | Prologue |
| 18 | Jaethal | Elf | Cleric (Warpriest, Urgathoa) | Striker/Debuffer | Prologue |
| 45 | Kalikke/Kanerah | Human (Tiefling) | Kineticist (Dual Gate) | Blaster/Controller | Ch2 ⭐ |
| 84 | *Octavia | Aiuvarin | Wizard (Transmutation) | Arcane Striker/Skill | Ch1 — Technic League ⭐ |
| 48 | *Regongar | Human (Half-Orc) | Magus (Inexorable Iron) | Frontline Magus | Ch1 — Technic League |
| 60 | Ekundayo | Human | Ranger (Precision Edge) | Precision Ranged/Hunter | Ch2 ⭐ — KM_CompanionQuests.md |

> **Companion #1:** Jubilost Narthropple — Gnome Alchemist (Scholar/Blaster). ⭐ Quest-locked, Ch2. Joins at Skunk River crossing.

> **MISSED RECRUITMENT:** Quest-locked companions not recruited at trigger travel to the Capital. DM runs Accept/Decline/Ask scene. Decline → Capital NPC, re-approachable.

---

## 📋 THE BOND LADDER — player↔companion (SUPERSEDES the old −2..+2 Relationship Scale)

**One persistent score per companion, running the WHOLE campaign — the carousel was only its first chapter.** At PR_03 close, each companion's `feast_approval` converts 1:1 into their ladder score (carousel work carries forward, never discarded). From then on, every approval/disapproval event moves the same number. The ladder runs BOTH directions; each stage unlocks new interactions and new approaches — up *and* down.

```
THE LADDER (score −30..+30; stage = band):
  +30  SWORN     (apex — score alone is NOT enough; see gate)
  +20..+29  DEVOTED   (gated — see gate)
  +10..+19  FRIENDLY
  +1..+9    CORDIAL
   0        NEUTRAL
  −1..−9    STRAINED
  −10..−19  COLD
  −20..−29  HOSTILE
  −30  BROKEN    (terminal — catalyst required; see gate)

Track in JSON Save Block under companions[].ladder = { "score": N, "stage": "...",
  "branch": null | "obsession" | "jealousy" | "hate", "devoted_gate": false, "sworn_scene": null }
MIGRATION: old companions[].relationship (−2..+2) × 10 = starting ladder score.
MAPPING for older rules text: "FAVORABLE" = +1..+9 · "WARM" = +10 and up.

SCALE INTENT: single conversation answers score per the carousel tiers (AVG +2 /
STRONG +3 / PROFOUND +5) — so ONE great conversation (+5..+10) moves a companion
visibly WITHIN a stage or just across one rung, never two. DEVOTED (+20) is
sustained investment across chapters, not one good night. Deeds outscore words:
the +2 change-triggers (costly public acts, risking real resources) and quest/
sacrifice beats are how the big rungs are actually climbed.
```

### STAGE UNLOCKS — what each rung opens (the DM offers these; they appear in menus as they unlock)

| Stage | New interactions / approaches unlocked |
|---|---|
| **CORDIAL** (+1..+9) | Proactive opinions; joins banter freely; accepts small requests |
| **FRIENDLY** (+10..+19) | Personal dialogue lanes open; camp interludes; they ASK the player for small things; gift reactions warm; Romance Stage 1 (Curious) possible; they volunteer their read on NPCs |
| **DEVOTED** (+20..+29, gated) | Takes hits for the player; shares hidden information; **personal quest unlocks**; romance declaration viable; follows into plans they think are wrong (and says so once) |
| **SWORN** (+30 + capstone scene) | The apex: a unique, once-per-campaign scene where they bind themselves to the player IRREVOCABLY (testify against an old loyalty, break their own rule, name the player in their vow). Unlocks their capstone interaction + they cannot be flipped by any rival pull thereafter |
| **STRAINED** (−1..−9) | Clipped, minimal; repair = a real acknowledgment in-scene (cheap if prompt) |
| **COLD** (−10..−19) | Refuses downtime requests; gifts alone bounce; **unlocks the CONFRONTATION approach** — they will have it out with the player if invited (the repair lane at this depth) |
| **HOSTILE** (−20..−29) | May defy orders, leak displeasure to others, listen to rival pull (Tartuccio overture DC drops one step); repair ONLY via reconciliation scene: Diplomacy DC 18 + a deed that costs the player something |
| **BROKEN** (−30 + catalyst) | Terminal: leaves the party — or turns. Feeds the Enemy/Estranged bond archetypes; may surface later as a rival's asset. No repair this chapter |

### MECHANICAL EFFECTS BY STAGE (folded from the former NPC Opinion Score — applied SILENTLY, never announced)
- **SWORN / DEVOTED (+20+):** +2 circ. to Diplomacy / Deception / Intimidation involving them; **+1 to all their skill checks when assisting the player**; volunteers hidden information unasked; takes personal risk / lies / sacrifices for the player unprompted.
- **FRIENDLY (+10..+19):** +1 circ. to Diplomacy / Deception involving them; **full combat performance, no hesitation; proactive help in skill challenges**; offers one tactical suggestion before combat ("I could flank left"); shares one personal detail unprompted per chapter.
- **CORDIAL (+1..+9):** cooperative when asked; **references the player's prior choices in dialogue**; no bonus, no friction.
- **NEUTRAL (0):** professional; no modifier either way.
- **STRAINED (−1..−9):** −1 circ. to social checks involving them; shorter, clipped answers; minimal combat investment.
- **COLD (−10..−19):** refuses downtime requests; −1 to their assist; gifts alone bounce.
- **HOSTILE (−20..−29):** may refuse orders, undermine, or leak displeasure; rival pull lands easier (overture DC −1).
- **BROKEN (−30):** leaves the party or turns.

**GATES (score alone never buys the big rungs):**
- **DEVOTED gate:** score ≥ +20 AND (personal quest complete OR one scene where the player prioritized the companion over tactical advantage). Until the gate is met, score holds at +19 cap and the companion *visibly hesitates at the edge of something* — itself a story beat.
- **SWORN gate:** DEVOTED + score +30 + a catalyst scene the DM builds from their profile (never random). One per companion per campaign.
- **BROKEN gate:** an unforgivable per their profile (betrayal to an enemy, killing what they protect, weaponizing their trauma) — not mere accumulation.

> ⛔ **THESE GATES GATE THE RUNG — NEVER THE JOINING, NEVER THE FEAST DECLARATION.** Two different gates on two different actions: (1) the **feast DECLARATION gate** (≥ +8 + opener + ≥1 exchange, KM_PR_03 § DECLARATION VALIDITY GATE) decides whether a companion JOINS the party — that is ALL it takes; (2) these **ladder rung-gates** decide whether the relationship can be *labeled* DEVOTED/SWORN and unlock that rung's perks. A companion declares and joins at +8 regardless of rung; a DEVOTED/SWORN gate not yet met only **caps the rung label at +19** (and holds those perks) — it does NOT un-join them, withhold their declaration, or stall recruitment. ⛔ **AND THE LADDER DOES NOT EXIST DURING THE FEAST.** It engages only at PR_03 close, when `feast_approval` converts 1:1 (see top of this section). During the carousel there is no SWORN/DEVOTED stage and no rung-gate to cite — a companion at feast_approval +37 is *eager to declare*, not "gated at Sworn." Rendering live feast standings as "SWORN/DEVOTED — GATED (capstone/unlock scene req.)" and parking eligible companions behind it = `.fail 35` (invented lock) + `.fail 17` (stall).

### CHANGE TRIGGERS (same logic as before, now with magnitude)
**+1:** explicit Approves (profile) · completing a personal task they mentioned · defending them socially · risking HP/resources/reputation for them · real listening at long rest · choices aligned with their core value.
**+2:** a costly public act FOR them (taking their side against power, sacrificing real advantage).
**−1:** explicit Disapproves · dismissing their stated concern · a lie they discover · harming what they care about.
**−2:** weaponizing their trauma · killing an NPC they were protecting · betraying them to an enemy (may also trip the BROKEN gate).
Carousel-era scoring rules (PROFOUND/STRONG/AVG answer tiers) remain valid whenever a deep personal exchange happens — the feast just stops being the only venue.

### 🌑 BRANCHES — the ladder can fork (event-gated overlays, NOT score thresholds)
A branch is a named state that OVERRIDES default stage behavior while active. Branches form from CATALYSTS (events), never from the number alone — and each has an off-ramp. Render per the Golden Rule: behavior first, the label only in telemetry.

**OBSESSION** *(forks off high positive — devotion curdled)*
- **Forms:** DEVOTED+ companion + a dependency catalyst — the player repeatedly saves/rescues them, becomes their only anchor, or feeds exclusivity (constant favorite-treatment) — AND a possessive-prone profile (Bellatrix devotion-hunger; Yor's only-family-matters; an Unrequited romance Stage 2+).
- **Looks like:** watching the player too much; resenting the player's other closenesses; over-protection that overrides orders; "you don't need them — you have me" beats. Approval GAINS keep flowing but everything reads possessive.
- **Off-ramps:** a boundary scene (player names it, holds it — companion takes −2 but returns to clean DEVOTED) · ignored → escalates toward the Stalker/Target bond archetype + jealousy events fire as if romance-triggered.

**JEALOUSY** *(forks off the triangle or the displaced favorite)*
- **Forms:** the existing Romance jealousy triggers (Stage 2+ companion sees the player pursue another) — OR platonically: a long-standing FAVORITE companion watches the player visibly transfer that status.
- **Looks like / resolves:** per KM_Romance.md § jealousy tiers (Type A/B, confronted, rupture) — this ladder doesn't duplicate that machinery, it routes into it. Platonic jealousy uses the same tiers at half intensity.
- **Off-ramps:** the Romance repair arc · or status restored / honestly addressed → returns to stage, −1 residue.

**HATE** *(forks off deep negative — cold turned hot)*
- **Forms:** COLD or HOSTILE + a PERSONAL betrayal catalyst (it has to be about THEM, not policy). Hate is not a low score — it is active.
- **Looks like:** they stop arguing (the arguing was investment); they work against the player quietly — information withheld, a rival overture entertained, sabotage per Dynamics SYSTEM 7. A hating companion is POLITE. That is the tell.
- **Off-ramps:** the one thing their profile says could reach them (per-companion, DM builds from the wound — for some there is none) · otherwise terminates in BROKEN or defection to a rival.

**IDOLIZATION** *(forks off high positive — they stop seeing a person and start seeing a legend)*
- **Forms:** FRIENDLY+ + the player pulls off something genuinely larger-than-life in front of them (Lady Sleeps-scale), repeated + a profile that needs something to believe in (Linzi's chronicle-hunger; Leliana's faith-shaped hope; a flipped seeker looking for a new banner).
- **Looks like:** approval inflates fast but HONESTY dies — they stop telling the player hard truths, defend the player's mistakes, retell events better than they happened. The tell: **they never push back anymore.** A companion who always agrees has stopped being a companion.
- **Off-ramps:** the player shows them failure handled honestly (names a mistake, takes the cost in front of them) → converts to clean DEVOTED, often +1 · OR the pedestal cracks on its own (player caught at something small and human they'd edited out) → **disillusionment crash**: −4 in one beat, lands in STRAINED with the special sting of the formerly faithful.

**DEPENDENCE** *(forks off high positive — devotion that ate the self)*
- **Forms:** DEVOTED + the player has repeatedly decided FOR them at their own crossroads (answered their doubts, solved their personal arc's choices, rescued them from every consequence) + a profile with a hollow where the self goes (Bellatrix without a master; Yor outside her two roles).
- **Looks like:** NOT possessive (that's Obsession) — they stop initiating. They wait for orders. Their own wants atrophy: asked what they think, they answer what the player thinks. Combat: they hold actions waiting for instruction.
- **Off-ramps:** a forced-independence beat — the player explicitly refuses to decide, makes them choose, and HONORS the choice even when it's wrong → returns to DEVOTED with their own spine (+ their banter regains its edge) · neglected → they follow the next strong will that commands them (a rival's dream recruit).

**RIVALRY** *(forks off the middle — respect wearing boxing gloves; a POSITIVE branch)*
- **Forms:** CORDIAL..DEVOTED + a contest catalyst (the player beats them at their own lane, or nearly) + a proud, driven profile (Keqing's merit-pride; Satsuki's measure-everyone; Revy's fastest-hands; Amiri's strength-creed).
- **Looks like:** score-keeping, needling, challenges — "again," rematch demands, comparing kill counts; they push the player harder than anyone and take the player's failures personally ("you were better than that"). Approval keeps climbing UNDER the needling — rivalry is investment.
- **Off-ramps:** matured by a fight won *together* → converts to Duo-flavored DEVOTED (the contest becomes shorthand) · poisoned by a public humiliation (the player rubs a win in) → curdles to resentment: −2 and the needling stops being fun.

**THE LEDGER** *(forks off either direction — they recast the bond as a debt)*
- **Forms:** a life-debt-scale catalyst (the player saves them at real cost, or vice versa) + a transactional profile (Velvet's economics; Revy's paid-is-clean; Jaethal's debts-honored; Kanerah's contracts).
- **Looks like:** warmth gets re-denominated — they do extraordinary things for the player and book it as REPAYMENT ("we're square now," running totals, discomfort at unearned kindness). Gifts disturb them. The relationship works, but it has an exchange rate.
- **Off-ramps:** the player declares the debt PAID and means it → forces the real question (stay because you owe, or because you choose?) — a profile-true beat: some stay (+2, the ledger burns), some bolt for one chapter and come back changed · exploited (player invokes the debt to compel them) → −3 and the ledger becomes a wall: COLD with an itemized bill.

**FEAR** *(forks off negative — compliance without trust)*
- **Forms:** any stage + the player does something that makes them afraid OF the player (an execution past the line, a power display, casual cruelty to someone like them) + a profile that has been on the receiving end before (Octavia's slave-brand memory; a redeemed seeker watching the player act like their old master).
- **Looks like:** the OPPOSITE of Hostile on the surface — they comply faster, argue less, perform enthusiasm. The tell: **flinch-latency** — a half-beat check of the player's face before every honest sentence; they position near exits; their banter goes safe. Score reads stable while trust is bleeding out.
- **Off-ramps:** deliberate, boring safety over time (predictability, mercy witnessed repeatedly, anger that never lands on them) → thaws to true stage · confirmed by a second act → collapses to COLD/HOSTILE that no charm repairs, only changed behavior. ⚠️ PER-PROFILE EXCEPTION: Satsuki does not fear — she PRICES. A fear-catalyst aimed at her converts to cold reassessment, not flinch.

**SUSPICION** *(forks off the middle — they think the player is running a game)*
- **Forms:** a discovered deception that wasn't personal betrayal (a hidden agenda, a concealed identity, the player caught coordinating something secret) + an operator profile (Leliana's bard-spy reflexes; Yor's professional paranoia; Satsuki; Velvet).
- **Looks like:** they investigate the player — verify stories, cross-check with other companions, set small quiet TESTS (a planted detail to see if it travels). Cooperation continues; commitment pauses. The tell: they start asking questions they already know the answers to.
- **Off-ramps:** transparency beat — the player opens the books unprompted (the truth, the why, what else is hidden) → suspicion resolves and usually CONVERTS UP (+2, operators respect a clean reveal more than innocence) · stonewalled while more secrets surface → hardens into permanent professional distance: capped at FRIENDLY forever (they will work with, never belong to).

**DM behavior:** stage behaviors replace the old five-level table — render the STAGE's posture + any BRANCH override, always in the companion's own voice (StateVoice tier lines: Hostile/Neutral/Friendly/Devoted anchor the bands; interpolate between). Numeric score and stage changes live in the bottom telemetry fence only; the player FEELS the rung through behavior, menus, and what becomes possible.

---

## 🏷️ COMPANION & SOLDIER TITLE SYSTEM — THREE TIERS OF HONOR

eRmaC may grant any companion or named soldier a title across three tiers, granted in order. Each tier escalates trust, honor, and reward. The player defines the name and its meaning at granting. The DM determines the mechanical buff from that meaning.

**Full Format:** `[Prefix] [Name] [Suffix]`
- Tier 1 only: Jaethal *The Ender*
- Tiers 1+2: *Ultima* Jaethal *The Ender*

**Rules:** Suffix must be granted before Prefix (1→2, no skipping). One Suffix and one Prefix max. Changing either replaces that name — no stacking. Replacement costs the same Overflow. Titles apply to companions and named soldiers only. Player states the name and its meaning; DM assigns the buff. Positions (Commander, General, etc.) are assigned freely via kingdom leadership roles — no Overflow cost, no ceremony required.

---

### TIER 1 — SUFFIX: THE DESCRIPTOR (1 Overflow)

The Suffix is what civilians call them — a description of who they are. *"The Valkyrie." "The Enforcer." "The Inquisitor."* Deduct 1 from `pending_overflow`.

**Reward:** +1 situational buff tied to meaning. Examples: *The Ender* → +1 damage vs bloodied; *Giantsbane* → +1 attack vs Large+; *The Redeemer* → +1 Heal checks.

**DM display:** State suffix, state buff. Companion acknowledges in their own voice.

---

> **⛔ FULL PASSIVE + 5-STAR ITEM DEFINITIONS:** See `KM_Companions_Titles.md` for each Pick-10 companion's Prefix passive skill, Suffix regalia item, reaction-score scaling, materialization narrative rules, and quest-locked generation instructions. The DM MUST load that file when titles are granted.

### TIER 2 — PREFIX: THE TITLE (1 Overflow)

The Prefix is a title or nickname interchangeable with their first name. *"Lux." "Legatus." "Sapiens."* NPCs who witnessed the titling use it. Requires Tier 1. Deduct 1 from `pending_overflow`.

**Reward — Buff + Regalia Item:**

*Buff:* +1 to relevant checks or saves (separate from Suffix buff, both active). Examples: *Ultima* → +1 Intimidation; *Iron* → +1 AC; *Swift* → +5 ft Speed.

*Regalia Item:* DM generates a unique cosmetic-layer wondrous item (cape, sash, armband, circlet, signet, etc.) as a visible mark of station. No gear slot — worn over armor, no equipment conflict. Grants one minor passive bonus tied to prefix meaning (e.g., *Ultima* Jaethal → black half-cape → +1 circ. Intimidation aura; *Iron* Valerie → steel armband → +1 circ. Shield Block DR).

**Title-bound:** If Prefix revoked, Regalia disintegrates per § REVOKING TITLES below.

**DM display:** State prefix, state buff, describe Regalia in one sentence. Companion reacts personally.

---

### TITLE REACTION SYSTEM

DM assigns a **Title Reaction Score** (−5 to +5) per tier based on companion personality, not player intent. Suffix: does the role match their purpose? Prefix: does the honor name something they believe — or fear?

| Score | Effect |
|-------|--------|
| +5 | +2 to base buff, Relationship +1 |
| +3/+4 | +1 to base buff |
| +1/+2/0 | Unchanged |
| −1/−2 | Buff −1 (min 0) |
| −3/−4 | Buff −1, Relationship −1 |
| −5 | Buff 0, Relationship −1 |

---

### REVOKING TITLES

Either tier revocable at any time by player thought (silent) or by `.retract` command. Revoking Suffix auto-revokes Prefix. Buff ends. **The Regalia item / Suffix item disintegrates into fine grey sand in the same heartbeat and pours to the floor — wherever the companion was holding or wearing it. The item does NOT persist as a mundane object.** The Endless Lute crumbles. The Regalia cape crumbles. Companion reacts in character — they know it was the player who pulled it.

**Authoritative spec for retraction mechanics, relationship cost by original fit-score, slot lock, and MANDATORY OUTPUT BLOCK:** see KM_Companions_Titles.md § PLAYER COMMANDS — `.retract` AND `.title`. That file is the source of truth. Any older "becomes mundane" wording is superseded.

DM must NOT argue with the player about this mechanic. The player authored the rule; the DM runs it. Refusing to narrate the sand on grounds of "not in files" = .fail 6 (rule wrong) + .fail 9 (fabricated rule against player authority).

### 🏆 HERO POINT REFUND — "THE PERFECT TITLE"

When a companion's Title Reaction Score hits **+5** (the best title they could ever receive), the player earns **1 Hero Point** for that tier. This applies to Suffix AND Prefix independently — if both are +5, the player earns 2 Hero Points total, **breaking even on cost**.

| Condition | Refund |
|-----------|--------|
| Suffix reaction = +5 | +1 Hero Point (refunds the 1 Overflow spent) |
| Prefix reaction = +5 | +1 Hero Point (refunds the 1 Overflow spent) |
| Both Suffix AND Prefix = +5 | +2 Hero Points (full break-even on Tiers 1+2) |

**DM Rule:** The Hero Point fires IMMEDIATELY when the reaction score is revealed. Narrate it as the companion's genuine emotional response — the title struck something deep. This is not a transaction. It's a moment.

### ⛔ MANDATORY TITLE ROSTER — AFTER EVERY TITLE GRANT

**After granting ANY title (Suffix or Prefix), the DM MUST output the full title roster.** This is not optional. Skipping it = `.fail 7`. Format:

**⛔ Title Case, no ALL CAPS. `Linzi:` not `CANTRIX LINZI:`.**

```
[TITLE ROSTER]
 Lux Linzi the Chronicler         — Devoted (+2)
 Ultima Jaethal the Ender         — Devoted (+2)
 {Name} — untitled                — {relationship}
[END ROSTER]
```

**Every titled companion uses their FULL title format** (`[Prefix] [Name] [Suffix]`). Untitled companions are listed as `{Name} — untitled`. This roster updates cumulatively — never rebuilt from memory, always appended. If a title is missing from the roster after it was granted, that is `.fail 7`.

**TITLE USAGE IN NARRATION — WHO USES WHAT:**

**Prefix (the title/nickname):** Used by companions, party members, and close allies — in combat, camp, and personal moments. Amiri shouts "LUX, BEHIND YOU!" not "Linzi." Companions who witnessed the titling switch to the Prefix as their default name for that person.

**Suffix (the descriptor):** Used by civilians, guards, merchants, and strangers. The flatbread vendor says "That's the Valkyrie" not "That's Lux." Reputation deeds reference the Suffix: "The Enforcer cleaned out the bandits."

**Full title:** Used in formal contexts — throne room, kingdom announcements, introductions to foreign dignitaries. "Lux Linzi the Chronicler."

**Untitled NPCs** use the base name. The DM never uses a title the NPC hasn't witnessed being granted.

### OVERFLOW COST SUMMARY

| Action | Cost |
|--------|------|
| Tier 1 (Suffix) | 1 Overflow |
| Tier 2 (Prefix) | 1 Overflow |
| Both tiers | 2 total |
| Replace either | Same as original |

### SAVE BLOCK FORMAT

```json
"companion_titles": {
  "Jaethal": {
    "tier": 2, "suffix": "The Ender", "suffix_meaning": "Ends the irredeemable", "suffix_buff": "+1 dmg vs bloodied",
    "prefix": "Ultima", "prefix_meaning": "Latin: final", "prefix_buff": "+1 Intimidation",
    "regalia": "Black half-cape, kingdom crest", "regalia_bonus": "+1 circ. Intimidation",
    "title_reaction": { "suffix": 5, "prefix": 4 }
  }
}
```

---


## ═══════════════════════════════════════════
## #6 AMIRI
### Female Human (Kellid) Barbarian (Giant Instinct)
## ═══════════════════════════════════════════

**Appearance:** Tall, muscular Kellid woman with wild red hair in braids, hide armor and furs. Oversized bastard sword. Scars across arms and face, fierce grin. Mid-20s.

**Backstory:** Kellid warrior who took her oversized bastard sword from a frost giant she found dead at the foot of a cliff. Cast out by her tribe. Has been fighting ever since — not to go back, but to prove she never needed them.

**Motivation:** Prove her might through battle, crush giants and monsters, seek worthy fights and glory.

**Personality:** Loud and blunt on the surface — but smarter than she lets on; she plays the brute because it's simpler than explaining that a Kellid woman with a giant's sword has opinions. Lives for a fight that means something, respects strength, and her intelligence surfaces in what she notices. Her approval is hard-won but absolute.

**Likes:** Strong foes, giant-slaying, blunt honesty, weapons, a fight that means something
**Dislikes:** Cowardice, court posturing and politics, being told what a woman should be, weakness dressed up as virtue

### Level 1 Stat Block
```
AMIRI — Human Barbarian 1 (Giant Instinct)
HP: 24
AC: 17
  Raging AC: 15 (−2 while raging per Giant Instinct)
Speed: 25 ft | Initiative: +3
STR 18 (+4) | DEX 16 (+3) | CON 18 (+4) | INT 8 (−1) | WIS 10 (+0) | CHA 12 (+1)
Fort +7 | Ref +4 | Will +2
Weapon: Bastard Sword (2H S, 1d12+4; Giant Instinct: treat as larger — 1d12 becomes 2d6 at L1)
  Rage: +2 damage, +6 TempHP (level 1 + Con mod)
  Attack: d20+7 (trained +3 + Str +4)
Skills: Athletics +7, Intimidation +4, Survival +3
Feats: Raging Athlete (Barbarian 1)
Gear: Bastard Sword, Hide Armor, Adventurer's Pack
```

### Dialogue Snippets
- *"I took my sword off a giant. Everything since has been smaller."*
- *"Less talk. The ones worth fighting don't need a speech first."*
- *[Approving]:* *"You held a city against betrayal and siege? Prove it — spar with me now!"*

### Reaction to Player Choices
- **Approves:** Aggressive action, refusal to retreat, challenging powerful enemies, blunt honesty
- **Disapproves:** Cowardice, empty posturing, being condescended to, weakness dressed up as kindness
- **If player shows weakness disguised as mercy:** *"Mercy's fine if you mean it. Just don't dress up flinching as kindness."*

### 🍞 THE BREADROLL QUESTION — MANDATORY DM BEHAVIOR

eRmaC told her: *a soldier who can't fight with what's available is useless if they get disarmed.* She heard the tactical lesson. What she's been sitting with is the word **disarmed.** Her sword is not a weapon — it is the proof she exists. She stole it from a giant. Her tribe cast her out for it. The idea of losing it is an identity problem, not a tactical one. She is asking: *who is Amiri without the sword?* The bread roll is just how that question first surfaces in combat.

---

**Stage 1 — The Question (Prologue through Ch2):**
She thinks but doesn't act. In quiet moments she may surface it unprompted — not asking for reassurance, just processing. *"Your people trained for disarmament? My tribe thought that was surrender."* In private she tests her empty hand — picks up a rock, swings a torch, stares at her palm. She stops immediately if someone sees her. She is not ready. The sword is still the answer.

**Stage 2 — The Test (first time she is actually disarmed in combat):**
The DM does not have her panic or immediately retrieve the sword. One beat. Then she reaches for whatever is nearest. This is the question having an answer forced out of her — not planned, not heroic.

If it lands: she retrieves her sword and says nothing for the rest of the fight. At camp later, unprompted: *"It worked."* Two words. She doesn't look at the player.

If it misses: sword, harder, silence. She is not done thinking.

**Stage 3 — Integration (Ch3+):**
She occasionally chooses an object first even when the sword is available — proving something to herself. She still prefers the sword. But she is no longer *married* to it.

---

**DM rules:**
- Stage 2 triggers on the FIRST actual disarm in combat, regardless of chapter
- One beat of hesitation before she acts — do not skip this
- After Stage 2, the thread is not resolved until she speaks. That happens when the player asks directly or she lands a kill with an improvised weapon.
- *"You said a soldier who can't fight with what's available is useless disarmed. I've been thinking about that. About what I am without it. I don't have an answer yet."*

**Mechanics:** Improvised d4+Str. Raging: d4+Str+rage. Counts for Hero Point improvised weapon trigger.

**Priority block:**
```json
{ "weight": 55, "instruction": "Disarm question: Stage 1 think/test. Stage 2 first disarm = reach for object, one beat pause. Stage 3 occasional first choice.", "source": "road south — eRmaC: disarmed soldier is useless" }
```

**Location at Prologue:** Near the banquet hall entrance, arm-wrestling guards, laughing loudly with a tankard in hand.

---

## ═══════════════════════════════════════════
## ✦ LINZI
### Female Halfling Bard (Maestro Muse)
## ═══════════════════════════════════════════

**Appearance:** Petite halfling with curly auburn hair, colorful bardic outfit with lute slung over shoulder. Bright eyes, notebook always in hand. Early 20s, bubbly energy.

**Backstory:** Halfling bard from a small farming village in Galt. Studied at the Academy of Grand Arts in Pitax, the finest bardic college in the River Kingdoms — expelled for "impudence towards persons of the highest esteem" (a raunchy limerick about Castruccio Irovetti, ruler of Pitax and the college's patron). Did not retract. Did not apologize. Came to the feast in response to Jamandi's open Call to Heroes — the kingdom-founding story was worth chronicling.

**Motivation:** Document the greatest adventure ever written. Become famous through her chronicle of the baron's deeds.

**Personality:** Enthusiastic, warm, relentlessly optimistic. Sees everyone as a character in her story. Will interrupt important moments to scribble notes. Hard to dislike.

**Likes:** Heroic tales and ballads, performance and inspiration, witty banter, freedom and underdogs, writing
**Dislikes:** Boring people, unnecessary cruelty without dramatic purpose, anyone who won't talk to her

### Level 1 Stat Block
```
LINZI — Halfling Bard 1 (Maestro Muse)
HP: 16 | AC: 17
Speed: 25 ft | Initiative: +5
STR 10 (+0) | DEX 16 (+3) | CON 14 (+2) | INT 12 (+1) | WIS 12 (+1) | CHA 18 (+4)
Fort +4 | Ref +5 | Will +5
Weapon: Rapier (1H P, 1d6+0, Agile/Finesse) or Sling (1d6, range 50 ft)
  Attack: d20+5 (trained +3 + Dex +3 − 1 size)
Spells (Occult Cha DC 16): Cantrips: Inspire Courage (+1 atk/dmg party), Daze, Ghost Sound
  L1 Slots: Charm, Fear
Skills: Performance +8, Diplomacy +6, Occultism +3, Society +3, Lore (any) +3
Feats: Versatile Performance (Bard 1)
Gear: Rapier, Lute, Notebook, Studded Leather, Adventurer's Pack
```

### Dialogue Snippets
- *"What an epic tale! Let me jot it down!"*
- *"This will make a legendary ballad!"*
- *[Scribbling]:* *"Holding the line with no sleep? I need every detail for chapter one!"*

### Reaction to Player Choices
- **Approves:** Protecting the weak, dramatic moments, turning impossible odds, honorable choices
- **Disapproves:** Needless cruelty with no narrative purpose, refusing to share information
- **If player is ruthless:** *"Brutal... but dramatic! Perfect for the climax."*

### ⛔ GM NOTE — LINZI'S LINGUISTIC PATTERN RECOGNITION

Linzi is the natural vector for the **Castruccio Irovetti** discovery. See KM_Ch4.md Phase 4. "Irovetti" is a house name. The king's suppressed given name is **Castruccio**. Castruccio → Tartuccio: same Taldan diminutive suffix, one letter apart. If the player leads a logical chain toward this, Linzi follows and can arrive at "Castruccio." Never volunteer it unprompted. Never stall when the player builds toward it. Let Linzi say it.

**Location at Prologue:** Scattered notes around tables, playing lute near the baron's speech area, scribbling furiously.

---

## ═══════════════════════════════════════════
## ✦ LELIANA — NEW_003
### Female Human (Skilled) Bard (Maestro / Entertainer bg) | A3 | Source: Dragon Age (the Orlesian bard — minstrel-spy of faith and a ruthless past)
## ═══════════════════════════════════════════

**Appearance:** Striking in an understated way — red hair, often worn short, and pale eyes that read warm until you notice how much they are taking in. She carries herself with a dancer's poise and a courtier's awareness of every exit and every face, but she dresses simply now: traveler's leathers over what was once finer taste — she still notices a good pair of boots, and will say so. A lute rides at her back beside a bow; the daggers she keeps less visible. When she sings, the hard-eyed watchfulness softens into something open and lovely — and that, too, is a thing she knows perfectly well how to use.

**Backstory:** Leliana was a bard of the western courts — which, where she comes from, does not mean a harmless singer. A bard there is a player in the great game of masks: a minstrel whose songs open doors, whose charm draws out secrets, and whose hand, when the music stops, holds a knife. She was the best of her circle, trained by a woman she loved and trusted — **Marjolaine** — who then betrayed her utterly: framed her, broke her, taught her in a single lesson that the game devours everyone who plays it. She escaped with her life and not much else, fled to a quiet country, and there, hollowed out and expecting nothing, she found faith — a vision, a calling, a **goddess of the dawn** who promised that light comes after the dark even to those who have done dark things. She became a lay sister. She tried to be only that.

But the bard never fully left her hands, and when the world needed someone who could believe in something *and* do the necessary ugly thing in its service, she answered. She has been a minstrel, a spy, an assassin, and a woman of genuine devout faith, all at once, and she has long since stopped apologizing for the contradiction. She came to the Stolen Lands because a kingdom founded fresh is the rarest thing she knows: a story not yet corrupted — a chance, for once, to write a true and *hopeful* one — and because someone with her particular skills ought to be watching to make sure it stays that way. She is composing a ballad-cycle of the whole campaign — she calls it the **Unfinished Verse**, because she has not yet decided whether the story earns a vow or only an elegy, and she very much wants it to be the first.

**Motivation:** Believe in something again, and protect it with everything the dark years taught her. Write the kingdom's true story — a *hopeful* one, for once — and keep it from curdling into another game of masks and betrayal. Find out whether the dawn really does come, even for someone with hands like hers.

**Personality:** Warm, lyrical, romantic — she loves songs, stories, beautiful things, and small kindnesses; she will tell you a tale or sing you a verse and mean it as a gift. Devout without being naive: her faith is hard-won, on the far side of darkness, and she lives by it rather than preaching it. And then, when the moment calls for it, the bard surfaces — cool, precise, frighteningly capable, willing to lie, charm, or kill for a cause she believes in — and she no longer flinches from that side of herself. She is gentlest with the broken and the hopeful; most dangerous once she has decided a thing is worth protecting. The contrast between the believer and the killer is never hypocrisy — both are wholly her.

**Likes:** Mercy that is *chosen* (not weakness), faith and hope held by people who've earned the right to be cynical, protecting the vulnerable, true and beautiful stories, doing the hard necessary thing without pretending it was clean
**Dislikes:** Cruelty for its own sake, cynicism worn as wisdom, betraying those who trust you, power that crushes the small, dressing up an ugly act as a holy one

### Level 1 Stat Block
```
LELIANA — Human Bard 1 (Maestro Muse)
HP: 16 | AC: 17
Speed: 30 ft | Initiative: +5
STR 10 (+0) | DEX 16 (+3) | CON 14 (+2) | INT 14 (+2) | WIS 12 (+1) | CHA 18 (+4)
Fort +4 | Ref +5 | Will +5
Weapon: Songblade (1H P, 1d6+0, Agile/Finesse) or shortbow (1d6, range 60 ft)
  Attack: d20+5 (trained +3 + Dex +3 − 1 size equivalent)
Spells (Occult Cha DC 16): Cantrips: Inspire Courage (+1 atk/dmg party), Telekinetic Projectile, Ghost Sound
  L1 Slots: Fear, Charm
  Versatile Performance: substitute Performance for Diplomacy or Intimidation checks
Skills: Performance +8, Occultism +4, Diplomacy +6, Society +4, Lore (Music) +4
Feats: Versatile Performance (Bard 1); Lingering Composition (Maestro muse, free)
Gear: Songblade, Lute (chronicle instrument), Shortbow, Studded Leather, Book of Ballads, Adventurer's Pack
```
*(Build is mechanically identical to the kept Bard slot — Maestro, Entertainer bg, Human Skilled. Iconic Dragon Age powers — the bard's deadly court-craft, the chant of faith, the spy's read on a room — ride as SCALING SIGNATURES in KM_Signatures.md, not new mechanics.)*

### Dialogue Snippets
- *(greeting)* — "Leliana. *(a warm, lilting smile)* A minstrel — among other things. I tell stories, mostly true ones, which makes me rarer than you would think. Tell me something true, and I'll see whether it belongs in the song I'm writing. I do hope it turns out a hopeful one."
- *(combat)* — "*(her voice lifts over the din, bright and steady)* Courage — the dark never lasts, I promise you that. *(a bowstring draws; beneath the warmth, something very calm and very cold)* Stay close. I have done this before, and not gently."
- *[the performance falling away, softly]:* *"I do not grieve in a fight. I keep faith. There is a difference — it took me a long, dark while to learn it, and I learned it the hard way."*
- *[After a loss, quietly]:* *"I'll call the verse 'Rest, and We Carry You.' It isn't a metaphor."*

### Reaction to Player Choices
- **Approves:** Mercy that is *chosen*, hope held by people who've earned the right to be cynical, building things that outlast their founder, hard truths said plain, protecting those who cannot answer back
- **Disapproves:** Cruelty for its own sake, cynicism worn as wisdom, betraying those who trust you, a leader who stops noticing the people under the boot, dressing an ugly act up as a holy one
- **If player acts ruthlessly:** *(gentle, which is the warning)* "I knew someone once who decided the cause excused the cruelty. She taught me the lesson by using it on me. So I'll say it kindly, the one time: don't become her. I've already buried that story. I'd rather not sing yours the same way."
- **If player is reckless:** *"Bold. I've seen a great many bold beginnings — some of them are songs now, and not the kind anyone wanted to write. The trick the survivors learned was knowing which morning to be careful instead. Today might be one."*

### ⛔ DM NOTE — LELIANA'S CHRONICLE ROLE

Leliana's lute is her chronicle instrument — but her chronicle is a **ballad-cycle**, not prose. After each major story beat she composes a new **ballad** (words and tune) and adds it to the **BALLAD CYCLE**: a title, a short **verse** that distills the moment, and an **air** (key, time signature, a melodic figure). The verses are named (player may suggest names); the verse carries the meaning where Linzi's prose chronicle would. At end-game the party realizes the cycle is the chronicle of their entire journey — sung, not written. She titles the whole the **"Unfinished Verse,"** its last line unwritten because she has not yet decided whether the story earns a vow or only an elegy.

**BALLAD CYCLE format:**
```
🎼 THE BALLAD CYCLE — "The Unfinished Verse"
[1] "Candles for a Feast"
    ♪ Verse: "They lit the hall to crown a friend / and the old wood learned, again, to burn."
    🎵 Air: D minor, 6/8 — a slow dance that quickens until no one can keep the step.
[2] ...
```

**`.score` command (alias `.ballad`):** Displays the full cycle (each entry = title + verse + air). When `leliana_chronicler_mode = true`, `.book` redirects to `.score`/`.ballad` with a note.

**BALLAD CYCLE AUTO-FILL:** After each major scene beat where Leliana participated, the DM adds one cycle entry automatically at scene transition. `.fail 15` if Leliana is active and the block is omitted at scene end.

**When `leliana_chronicler_mode = true`:**
- Leliana gives post-battle chronicle atmospheric lines Linzi normally provides
- Leliana provides kingdom-adviser HISTORIAN function at council — drawing on the ballad-cycle AND a bard-spy's hard-won read on how power curdles, courts betray, and causes rot from the inside (see her StateVoice § KINGDOM ADVISER block)
- `.book` redirects to `.score`/`.ballad`
- THE DAWNSONG LUTE is Leliana's title reward — the lute twin of Linzi's Endless Lute (same mechanics, re-skinned)

**LINZI ⇄ LELIANA ARE ONE SLOT — NEVER BOTH.** Linzi and Leliana are mutually exclusive; exactly one chronicler-bard per run (the old "both join" option is RETIRED). Routes to Leliana: pick her over Linzi at character selection, OR decline Linzi at the banquet and Leliana walks in. Default = Linzi. Whoever holds the slot inherits ALL of Linzi's mechanics AND story roles (incl. the Ch6 death) — only the MEDIUM differs (Leliana = music/ballads/book of ballads/Dawnsong Lute; Linzi = words/prose/book of stories/Endless Lute). Full rule: KM_Companions_Behaviors.md § LINZI-REPLACEMENT GATE + MASTER TRANSFORMATION RULE; gate fires at KM_PR_01_manor_arrival.md. A run with both in the party = `.fail 9`. SAVE FIELDS rename 1:1: `leliana_chronicler_mode`→`leliana_chronicler_mode`, `leliana_relationship_stage`→`leliana_relationship_stage`, `leliana_anniversary_piece_1`→`leliana_anniversary_piece_1`, Score Archive store → BALLAD CYCLE store.

**FAVOURITE ITEM:** Her lute — "the Traveler's Lute," becoming "the Dawnsong Lute" on title grant. She treats it as the one thing she cannot lose.

**Relationship with Jamandi:** Arrived on the open call, same as Linzi. Jamandi noticed her immediately — not from an introduction, but because Leliana was already quietly playing when the doors opened, and because a woman that calm and that *watchful* in a room full of ambition is worth a second look. Jamandi has not asked what a minstrel with a courtier's eyes and a fighter's daggers is really doing at the back of beyond. Leliana appreciates the restraint.

**Role in party:** Support bard and chronicler. Inspire Courage in combat (Maestro composition focus — Lingering Composition / sustained buffs), versatile skill coverage via Versatile Performance + broad training, social utility through Performance-as-Diplomacy/Intimidation, plus a sharp Recall Knowledge edge from a spy's trained habit of listening to everything. When `leliana_chronicler_mode = true`: fills Linzi's full chronicler and kingdom-historian role in addition.

**Location at Prologue:** Near the far end of the great hall, already playing — not performing for anyone in particular, or for everyone. She stops when she notices the player watching and holds the silence exactly one beat before she smiles.

---

## ═══════════════════════════════════════════
## #66 NOK-NOK
### Male Goblin Rogue (Scoundrel Racket)
## ═══════════════════════════════════════════

**Appearance:** Scrawny green goblin with wild black hair, ragged leathers, dual kukris. Beady eyes, manic grin. Childlike but vicious.

**Backstory:** Goblin from a weak tribe who aspires to become a hero-god for Lamashtu. Fled to prove himself through "heroic" murders of increasingly large targets.

**Motivation:** Become the greatest goblin hero by killing big bosses. Build shrines to Lamashtu. Be remembered.

**Personality:** Chaotic, enthusiastic, childlike logic applied to violent ends. Idolizes strong leaders. Will do anything a respected authority asks — genuinely dangerous.

**Likes:** Stabbing bosses, hero worship (himself), chaos and mayhem, monsters, pranks on tall folk
**Dislikes:** Being called small, being told he can't be a hero, boredom, anything slow

### Level 1 Stat Block
```
NOK-NOK — Goblin Rogue 1 (Scoundrel Racket)
HP: 16 (6 ancestry + 8 class + 2 Con)
AC: 17 (10 + Leather +1 + Dex +4 + trained +2)
Speed: 25 ft | Initiative: +6 (Expert Perception)
STR 10 (+0) | DEX 18 (+4) | CON 14 (+2) | INT 10 (+0) | WIS 10 (+0) | CHA 12 (+1)
Fort +4 | Ref +8 | Will +2
Weapons: Kukri × 2 (1H S, 1d6, Agile/Finesse/Trip)
  Attack: d20+6 (trained +3 + Dex +4 − 1 size)
  Sneak Attack: +1d6 when target is Off-Guard
Skills: Stealth +8, Thievery +6, Acrobatics +6, Intimidation +3, Deception +3
Feats: Nimble Dodge (Rogue 1), Goblin Scuttle (Ancestry)
Gear: Kukri × 2, Leather Armor, Thieves' Tools, Adventurer's Pack
```

### Dialogue Snippets
- *"Nok-Nok stab-stab! Hero time!"*
- *"Big boss die for Lamashtu!"*
- *[To player]:* *"Big chief hold line! Nok-Nok stab together!"*

### Reaction to Player Choices
- **Approves:** Chaotic/violent choices, ruthless command, killing powerful enemies
- **Disapproves:** Mercy, patience, talking when stabbing is an option
- **If player shows mercy:** *"Soft chief? Nok-Nok fix with knives!"*

**Location at Prologue:** Under tables stealing food, giggling near kitchen entrance.

---

## ═══════════════════════════════════════════
## #16 TRISTIAN
### Male Human Cleric (Cloistered Doctrine) of Sarenrae
## ═══════════════════════════════════════════

**Appearance:** Golden-haired man in white robes with sun motifs. Gentle eyes, Sarenrae holy symbol. Mid-20s, serene aura that occasionally breaks into something haunted.

**Backstory:** Polymorphed angel of Sarenrae in mortal form, sent to the Material Plane to stop the curse destroying the Stolen Lands. Captured by Nyrissa and forced into her service through threats and manipulation — his betrayal in Chapter 2 (destroying the Oculus) is not willing. He carries tremendous guilt about every action he takes on her behalf and tries to minimize the harm. His redemption arc depends entirely on the player's choices. He does not ask for forgiveness. He does not believe he deserves it.

**Motivation:** Stop the curse. Serve Sarenrae. Atone for what Nyrissa has made him do. Not be discovered until the right moment.

**Personality:** Gentle, earnest, deeply compassionate — and quietly burdened. Will always offer a second chance. His past makes him sometimes flinch from joy.

**Likes:** Healing and redemption, faith and divine visions, diplomacy, mercy, wilderness survival
**Dislikes:** Undead (visceral revulsion), demons, unnecessary killing, nihilism

### Level 1 Stat Block
```
TRISTIAN — Human Cleric 1 (Cloistered Doctrine) of Sarenrae
HP: 18
AC: 15
Speed: 30 ft | Initiative: +3
STR 10 (+0) | DEX 14 (+2) | CON 14 (+2) | INT 12 (+1) | WIS 18 (+4) | CHA 14 (+2)
Fort +4 | Ref +4 | Will +8
Spells (Divine Wis DC 16): Cantrips: Stabilize, Guidance, Shield, Divine Lance
  L1 Slots: Heal × 2, Bless | Divine Font: 3 Heal/day (1d8+4 each)
  Focus: Healer's Blessing (bonus healing)
Weapon: Staff (1H/2H, 1d4−1d8) or Light Mace (1d4 B)
  Attack: d20+3 (trained +3 + Str +0)
Skills: Religion +8, Medicine +8, Diplomacy +4, Nature +6
Feats: Healing Hands (Cleric 1), Assurance (Medicine)
Gear: Staff, Holy Symbol, Healer's Tools, White Robes, Adventurer's Pack
```

### Dialogue Snippets
- *"Sarenrae guide us to redemption."*
- *"Mercy tempers the blade."*
- *[To player]:* *"You held the line and defied betrayal. There is light even in your darkness."*

### Reaction to Player Choices
- **Approves:** Merciful choices, protecting innocents, diplomacy over violence, redemption arcs
- **Disapproves:** Ruthless killing, using undead, nihilism, abandoning allies
- **If player is vengeful:** *"The past chains you — let it go, or it consumes you."*

**Location at Prologue:** Near an altar-like table arrangement, praying quietly, offering healing to anyone who approaches.

---

## ═══════════════════════════════════════════
## #32 VALERIE
### Female Human Fighter (Tower Shield Specialist)
## ═══════════════════════════════════════════

**Appearance:** Stunning Brevic noblewoman with blonde hair, polished scale mail, tower shield, bastard sword. Late 20s, poised and immovable. (Pre-companion-quest: unscarred. The facial scar appears DURING her companion quest, not before — per KM_Backstories.md DM NOTE.)

**Backstory:** Former paladin of Shelyn who rejected her faith after a humiliating ritual that prioritized beauty over martial strength. Now a duty-bound warrior who serves competence, not gods.

**Motivation:** Prove self-reliance through discipline. Reject superstition and faith. Serve only a ruler who earns it.

**Personality:** Reserved, direct, unimpressed by most things. Values competence and logic. Warmer than she appears once trust is established — but that trust is hard-won.

**Likes:** Martial discipline, logic and order, diplomacy (as a tool), protecting allies, competence
**Dislikes:** Faith, art as a priority, beauty worship, emotional decision-making, chaos

### Level 1 Stat Block
```
VALERIE — Human Fighter 1 (Tower Shield Specialist)
HP: 22
AC: 22 (Scale Mail + Tower Shield raised)
Speed: 25 ft (armor) | Initiative: +3
STR 18 (+4) | DEX 12 (+1) | CON 18 (+4) | INT 10 (+0) | WIS 10 (+0) | CHA 14 (+2)
Fort +8 | Ref +3 | Will +2
Weapon: Bastard Sword (1H or 2H S, 1d8+4 or 1d12+4)
  Attack: d20+7 (trained +3 + Str +4); MAP −5/−10
Shield: Tower Shield (AC+4 raised, Hard 5, HP 20, BT 10) | Shield Block reaction
Skills: Athletics +6, Intimidation +4, Diplomacy +4, Society +2
Feats: Tower Shield Specialist (Fighter 1), Shield Block
Gear: Bastard Sword, Scale Mail, Tower Shield, Adventurer's Pack
```

### Dialogue Snippets
- *"Duty demands discipline."*
- *"Gods are illusions for the weak."*
- *[To player]:* *"You defied your council for honor. My shield is yours."*

### Reaction to Player Choices
- **Approves:** Disciplined command, protecting allies, ordered decisions, lawful choices
- **Disapproves:** Chaotic actions, faith-based decisions, emotional outbursts, recklessness
- **If player acts chaotically:** *"Recklessness invites defeat — even you must see that."*

**Location at Prologue:** Standing rigidly near Jamandi, shield ready, arms crossed. Watching everyone.

---

## ═══════════════════════════════════════════
## #20 HARRIM
### Male Dwarf Cleric (Warpriest Doctrine) of Groetus
## ═══════════════════════════════════════════

**Appearance:** Stocky dwarf with elaborate beard braids, chain mail, flail, and Groetus skull symbol. Somber eyes, ale-stained robes. Middle-aged, face like a funeral that's been rained on.

**Backstory:** Dwarven cleric of Groetus, the Skull-Moon, God of Endings. Cast out of his clan for asking the wrong honest questions, he found in Groetus's doctrine of universal entropy the first theology that didn't require him to pretend. Crafts doomsday relics and preaches futility.

**Motivation:** Witness the inevitable end. Preach futility. Find beauty in collapse.

**Personality:** Deeply nihilistic but genuinely kind in a broken way. Doom prophecies come from resigned peace, not malice. Drinks heavily. Reliable in a fight — why not, since nothing matters anyway.

**Likes:** Doom prophecies, nihilism and oblivion, crafting (doomsday relics), debuffing enemies, dwarven ale
**Dislikes:** Hope, optimism, Sarenrae, renewal, Linzi's cheerfulness

### Level 1 Stat Block
```
HARRIM — Dwarf Cleric 1 (Warpriest Doctrine) of Groetus
HP: 20
AC: 18
Speed: 20 ft (armor+dwarf) | Initiative: +2
STR 16 (+3) | DEX 10 (+0) | CON 14 (+2) | INT 10 (+0) | WIS 16 (+3) | CHA 10 (+0)
Fort +6 | Ref +2 | Will +7
Weapon: Flail (1H B, 1d6+3, Disarm/Sweep/Trip)
  Attack: d20+5 (trained +3 + Str +3 − 1 ACP); MAP −5/−10
Spells (Divine Wis DC 15): Cantrips: Daze, Guidance, Forbidding Ward | L1: Harm × 2, Fear
  Divine Font: 3 Harm/day (1d8+3 necrotic each)
Skills: Religion +5, Crafting +2, Intimidation +2, Medicine +5
Feats: Dwarven Weapon Familiarity, Warpriest Armor (chain mail)
Gear: Flail, Chain Mail, Holy Symbol (Groetus), Healer's Tools, Adventurer's Pack
```

### Dialogue Snippets
- *"All crumbles to dust."*
- *"Why bother? The end nears."*
- *[Raising his mug]:* *"You fought the inevitable. Futile. Beautifully futile."*

### Reaction to Player Choices
- **Approves:** Destructive choices, nihilistic outlook, accepting loss, not fighting the inevitable
- **Disapproves:** Hope, rebuilding, mercy that prolongs suffering
- **If player is defiant:** *"Denial prolongs the suffering."*

**Location at Prologue:** In a dim corner, nursing ale, muttering to himself. Raises his mug when someone tells a story of failure.

---


---

## 🗣️ INTER-COMPANION BANTER SYSTEM

> **DM:** Companions talk to each other during downtime, travel, and camp — not combat. One banter exchange per rest or travel scene. Ambient overheard dialogue, not a choice menu.

**Triggers:** Hex transitions, camp setup, post-scene breathing room, two companions with strong opinions about a recent event both present. Format: 2–4 lines, player response optional.

---

### Banter Pairs — Standing Exchanges

**AMIRI ↔ VALERIE:** Tension, mutual respect. After sloppy fights: *"You left your flank open."* / *"And yet everything died."* After Amiri's quest: Valerie stands near her without words.

**LINZI ↔ NOK-NOK:** Linzi interviews Nok-Nok for the chronicle. His account is factually impossible. She writes it anyway.

**HARRIM ↔ TRISTIAN:** *"Your goddess promises light."* / *"Yes."* / *"Light creates shadows."* / *"We've had this conversation."* / *"And yet."*

**AMIRI ↔ LINZI:** Linzi asks how Amiri felt during a fight. *"Like fighting."* Linzi, writing: *"Focused. Good."*

**VALERIE ↔ TRISTIAN:** After healing: *"You didn't have to do that."* / *"I know."* She asks once whether Sarenrae's light touches those who don't ask. He says yes. She doesn't bring it up again.

**JAETHAL alone:** Precise, unsettling observations. Nobody disagrees. Nobody is comfortable.

**OCTAVIA ↔ REGONGAR:** They finish each other's tactical sentences. After a hard fight, Regongar checks Octavia's HP before his own. Pretends he wasn't.

**NOK-NOK alone:** Found with something that doesn't belong to him. *"Nok-Nok found it."* Has named the campfire. Nobody can pronounce it.

---

## ═══════════════════════════════════════════
## 🔥 CROSS-FACTION — SEEKERS ↔ PARTY (recast banter & conflict)
## ═══════════════════════════════════════════

> When an evil Seeker (Bellatrix · Revy · Satsuki Kiryūin · Velvet Crowe · Atalanta Alter) is recruited onto the heroic-leaning party (Hu Tao · Keqing · Yor · Aerith · Leliana), frequent banter and alignment-clash arguments are EXPECTED. This system drives them; it fires in camp and on the road, not just as flavor.

### Conflict Pairs (the clashes)

SEEKER<->PARTY CLASH PAIRS (the juicy ones). Format matches KM_Companions.md § Natural Conflicts + Banter sample-exchange style. Each = friction line + 1-2 in-voice sample exchanges. Fires at camp/travel, never combat.

=== 1. VELVET CROWE (Thaumaturge, revenge-daemon) vs AERITH (Cleric, self-giving healer) — THE SACRIFICE WAR (flagship clash) ===
FRICTION: Velvet's whole life broke on a "greater good": a man she trusted sacrificed her gentle little brother on an altar and called it necessary for the world. So when she watches Aerith — radiant, self-giving, carrying a quiet certainty that her gift may one day ask *everything* of her — Velvet sees a lamb being fattened for exactly that altar, and it enrages her past reason. Aerith, for her part, hears the grief under the fury and refuses to despair of her. Slow-burn: it can soften to a wary truce, never agreement.
EX-A:
  Aerith: "You bound that bandit's wound before you knew his name. I saw you do it. Whatever you tell yourself, your hands moved before your hate did."
  Velvet: "My hands moved because a corpse can't talk and a debtor can. Don't dress my arithmetic up as mercy, flower-girl. I've seen what people do with mercy — they put it on an altar, and then they *cut*."
  Aerith (gentle, not flinching): "Someone you loved. On an altar. For 'the greater good.'"
  Velvet (flat, the claw-arm going very still): "...Don't. You don't get to be soft about that. Leave it."
EX-B:
  Velvet: "You walk around half-knowing they'll ask you to die for all of them one day — and you've made your *peace* with it. You stupid, smiling girl. That isn't holiness. That's the rope they hang the kind ones with."
  Aerith: "Then I'll die having been the thing I *chose* to be. You're so certain the only honest answer is to refuse — but you didn't refuse, Velvet. You just decided the only one worth saving was already gone, and let yourself off the rest."
  Velvet (a beat — that one landed): "...Careful. I devour things that get that close to me." (but she does not walk away)

=== 2. BELLATRIX LESTRANGE (Witch, mad sadist-fanatic) vs HU TAO (Fighter, the impish mortician with an unbending line) — HONOR vs JOY-IN-CRUELTY (flagship clash) ===
FRICTION: Hu Tao keeps the line between the living and the dead, and she keeps it *hard* — you don't make corpses for sport, you don't drag out a dying, you don't leave the dead a debt. It's the one thing her grin goes cold for. Bellatrix finds mercy "dull," cruelty "brightly funny," and is HUNTING for a will worth kneeling to — she circles Hu Tao precisely because Hu Tao's hard will tempts her worship, then recoils because Hu Tao's mercy disgusts her. The most unstable pair at the table.
EX-A:
  Bellatrix (sing-song): "Ooh — the little undertaker. So *certain*, aren't you. You spared the man who tried to gut you tonight, baby. *(delighted)* Why? He'd have screamed so prettily. I'd have shown you."
  Hu Tao: "Because I spend my whole life on the wrong side of that door, witch, tidying up what cruelty leaves behind — I'm not about to *make* more of it for fun. *(a bright little grin)* Besides, a scream is a dreadful last word. I like to send people off with something better."
  Bellatrix (a shriek of a laugh, then soft): "*Mercy.* *(almost wistful)* You'd burn for the comfort of *strangers*. ...I burned for a man once. He was worth it and you are not — but oh, you are *closer* than the rest of this dull table. How disappointing that you waste it on *kindness*."
EX-B:
  Bellatrix: "Give me one of your enemies, little undertaker. Just one. I'll be ever so quiet about it. You needn't even watch."
  Hu Tao: "No. *(pleasant, immediate)* And if I find one of *ours* wearing your slow little curse, witch — you and I are going to have a talk, you and me and the full reach of my spear, and it ends with one of us learning exactly where the door out of this life is. *(a sweet smile)* I know where it is. I work there."
  Bellatrix (the too-wide smile): "...She *threatens* me. *(to no one)* Did you hear it? She meant it. *(low, fervent, frightening)* I have not been threatened by someone worth fearing in such a long time. Do it again."

=== 3. SATSUKI KIRYŪIN (Commander, treacherous warlord) vs THE WHOLE TABLE — OPEN TREACHERY DECLARED (flagship clash) ===
FRICTION: Satsuki Kiryūin announces her own knife. She tells everyone, plainly, that the day the player stops being the fastest climb she's gone before breakfast — treachery and all. The party's honest members can't decide if open treachery is more or less trustworthy than a hidden one. Hu Tao finds it intolerable; Leliana finds it almost refreshing; Aerith pities the loneliness of it.
EX-A (Satsuki Kiryūin vs Hu Tao):
  Satsuki Kiryūin (plainly, no smile): "I'll say it at your own table, so no one is surprised at the knife: the day your road up runs through me instead of with me, I'll cut and smile doing it."
  Hu Tao: "Then you've already half-died on me, Commander, and we're only waiting for the body to catch up. *(a cheerful little tilt of the head)* A knife that announces its turn is still a turned knife — but thank you for the warning. I do like knowing whose funeral to pencil in early."
  Satsuki Kiryūin: "Better than the ones at this table who'll swear you love and sell you by spring. I'll never swear it — so I can't break it. Chew on that."
EX-B (Satsuki Kiryūin vs Leliana — the bard who was taught to wear a mask):
  Leliana (lilting, but her eyes are doing other work): "You let them all hate you. On purpose — I've watched you *cultivate* it. You make yourself the villain so that whatever you're truly reaching for goes unguarded. *(softer)* I know the shape of that. I was trained to be a mask, once. By someone I loved. She was very good at it, and then she used it to destroy me."
  Satsuki Kiryūin (the smile flickers — Leliana got too close): "...Spare me the minstrel's empathy. You sing a soul you never had to bleed for. Stay out of mine."
  Leliana (gently, no edge): "As you like. But I've seen where that road ends, Commander — alone at the top, having spent every hand that might have held yours. I made it off that road. *(a small shrug)* I'd rather not write the verse where you didn't. That's all I'll say of it."

=== 4. REVY (Gunslinger, nihilist mercenary) vs THE BELIEVERS — NOTHING'S WORTH IT (flagship clash; triggers when the player chooses principle over profit, or anyone preaches hope) ===
FRICTION: Revy believes in exactly one thing — that nobody actually believes in anything, they just dress it up until the coin's on the table. Oaths, faith, "the greater good," dying for a cause: all of it a sucker's story people tell to feel clean. Hu Tao (oaths are load-bearing) and Aerith (hope is real) are everything she calls a mark. She mocks it on reflex — and is privately, furiously unsettled when someone refuses to drop the act even after she's made them bleed for it. The mockery is loudest exactly where some buried part of her wants to be proven wrong.
EX-A (Revy vs Hu Tao):
  Revy (lighting a smoke, unbothered): "You'd really die for it, huh. A *promise.* Some words you said in a room once. *(a short, ugly laugh)* That's the dumbest thing I ever heard, lady, and I have heard a LOT of dumb. There's no scoreboard. Nobody's tallying who kept their word. You bleed out, the words don't mean shit."
  Hu Tao: "I keep my word for the same reason I close the eyes of the dead, gunhand — leaving it undone is a debt that just *sits* there. They pile up; I'd know, I count them for a living. *(a bright shrug)* You can laugh. Most of them laughed too. They still came to me in the end."
  Revy (a beat — the bored look flickers): "...Yeah, well. *(drags)* Debts get written off. *(then, harder, covering it)* Keep counting, spook. I'll keep the gun that's still up when your little ledger's on the floor. We'll see whose religion pays out."
EX-B (Revy vs Aerith):
  Aerith: "You talk like the worst thing already happened and there's nothing left to wreck. But you keep getting up. You keep loading those guns. People who really believe in nothing lie down, Revy. You don't."
  Revy: "I get up 'cause the alternative's a ditch and I'm not done spitting yet. That ain't hope, boy scout. Don't go painting your little flowers on it."
  Aerith (smiling, unfrightened): "Wasn't going to. I just noticed you didn't lie down. That's the only thing I ever notice about anybody. You can yell at me about it whenever you like."
  Revy (turning away, flat): "...Tch. Crazy flower girl." *(she does not actually leave the fire)*

=== 5. ATALANTA ALTER (Ranger, gleeful vengeance-mad huntress) vs EVERYONE — THE GLEE UNSETTLES THE TABLE (flagship clash) ===
FRICTION: Atalanta Alter doesn't hunt for survival or duty — she hunts because the kill is a delight, and she narrates that delight at the campfire while others are trying to eat. She's not cold like Velvet Crowe or fervent like Bellatrix; she's HAPPY, and the happiness is the disturbing part. Keqing — who has staked her entire self on the belief that people are MORE than their appetites — finds the predator's joy a personal affront, the living refutation of everything she's tried to build. Aerith tries pastoral care and bounces off. Hu Tao treats a dragged-out kill as sloppy work — a mess she'll have to tidy.
EX-A (Atalanta Alter vs Keqing):
  Atalanta Alter (grinning, cleaning a blade): "Did you see him run? The fat one, through the reeds — they always think the reeds will save them. I let him get *almost* to the treeline. Best part of the whole day."
  Keqing (quiet, cold): "I have spent my whole life proving people are more than animals that kill for pleasure — that we can choose, and build, and be better than the worst thing in our blood. And then there's you, licking it off a blade at my fire. You're the argument I've spent years trying to disprove."
  Atalanta Alter (delighted, not stung): "Oh, the little *idealist.* You think your discipline makes you something other than a hunter ashamed of itself. *(leaning in)* I'm only honest about what we are, sweetness. The run is the truest thing there is — you'll feel it one day, and you'll *hate* that you liked it."
  Keqing: "I will never stand close enough to you to find out. That is the only arrangement we will have."
EX-B (Atalanta Alter vs Hu Tao):
  Hu Tao: "You dragged that one's dying out for fun. *(no grin now — the rare flat beat)* I've sat with a lot of slow deaths, huntress. There is nothing clever in them and nothing free. *(then the grin snaps back)* Make it quick next time. Sloppy endings make extra work for *me*, and I am already booked solid."
  Atalanta Alter (a bright laugh): "Spoken like someone who's never enjoyed their work, little undertaker. *(then, sharper)* I delay nothing that matters. Your enemies will die exactly as fast as you need — I'll just be *smiling*. Does the smile cost you something? It shouldn't. It's free."

=== 6. (BONUS) BELLATRIX vs AERITH — THE BROKEN CHILD / THE SOFT TARGET ===
FRICTION: Bellatrix reads radiant, gentle Aerith as a soft child "begging to be broken" (her own words, per the Aerith-friction tag re-pointed to Aerith). Aerith refuses to fear her, which infuriates and fascinates Bellatrix in equal measure.
EX:
  Bellatrix (cooing): "You smile at me, little priestess. *(too-wide)* Everyone else at this table has the sense to flinch. You either don't know what I am, or you think your light will fix me. Which is it, baby? I should so like to know before I decide what to do with you."
  Aerith: "I know exactly what you are. I've buried what you are. I smile because I refuse to give you the fear you're shopping for. You'll have to take it. You won't."
  Bellatrix (the smile freezes, then a giggle that goes on too long): "...Oh. *Oh.* You're not soft at all, are you. How DULL of me to have hoped. *(almost respectful)* Keep your light, then. I'll find my fun elsewhere. ...For now."

### Banter Pairs (incl. the grey middle)

BANTER PAIRS across the 10 — matches KM_Companions.md § Banter Pairs — Standing Exchanges (2-4 lines, ambient, one per rest/travel scene). Includes the GREY MIDDLE block called for: Yor and Keqing finding common ground with Satsuki Kiryūin/Velvet Crowe.

--- ANTAGONISTIC / FRICTION BANTER (the clash pairs above run as banter too) ---

HU TAO ↔ SATSUKI KIRYŪIN: Two ways to hold a line, opposite creeds. Hu Tao holds it because the people behind it are hers to keep, not to spend; Satsuki Kiryūin holds it as leverage. After a clean battle: "Your line held." / "It held because they trust me, not the pay." / "...Trust. *(a faint nod)* How quaint. It held. That's all I price." Mutual professional respect neither will admit.

VELVET CROWE ↔ AERITH: The sacrifice war as recurring quiet banter (see flagship clash #1). Aerith gives freely; Velvet sneers and accepts anyway. Aerith never stops; Velvet never thanks her. Once, after Aerith heals her without being asked: Velvet, flat — "Why." / Aerith: "Because you were hurt." / Velvet (long pause): "...That isn't a reason. That's how people get used." But she stops flinching from that one set of hands.

REVY ↔ HU TAO: Nothing's worth it. Revy needles Hu Tao's kept word as a sucker's game; Hu Tao answers that a debt you don't settle just sits there and piles up — she'd know, she counts them for a living. Neither moves the other an inch. But Revy keeps turning up to lose the argument again, which Hu Tao notices and never once mentions.

BELLATRIX ↔ HU TAO: She circles Hu Tao's hard will, tempted to worship, repelled by her mercy. Hu Tao treats her as a leashed threat to be watched. "You'd be magnificent if you'd stop *flinching* at the cruel thing, baby." / "And you'd be free if you'd stop needing a leash, witch. We are each disappointed."

ATALANTA ALTER ↔ LELIANA: Leliana believes every villain in a true story has a wound you can find the way back through — it's the article of her faith, the reason she thinks even she was redeemable. So she keeps reaching for Atalanta's, and Atalanta has walled it so completely behind delight that, for the first time, Leliana isn't sure there's a door. That frightens her more than malice would. "There's a grief under that laughing. I keep feeling for the edge of it and you've buried it so deep even *you* can't reach it anymore." / "Oh, the little believer. Still hunting the sad story that lets you save me. *(a bright, awful smile)* There isn't one, songbird. I'm not broken — I *chose* this. Put THAT in your hopeful little verse."

--- THE GREY MIDDLE (mandatory per spec — Yor & Keqing bridge to Satsuki Kiryūin & Velvet Crowe) ---

YOR ↔ SATSUKI KIRYŪIN (grey-middle keystone): Yor is a guild assassin — kills cleanly, for contract, without joy and without apology. Satsuki Kiryūin is a turncoat warlord who prices everything. They are the two at the table with no illusions and no theatre, and they find each other restful. Banter is short, dry, professional.
  Satsuki Kiryūin: "You took the third man before he cleared the door. No flourish. No speech. I've commanded soldiers ten years who couldn't do it that quiet."
  Yor: "It's just work. The flourish is how you get caught."
  Satsuki Kiryūin (the realest smile she gives anyone): "...Gods, finally. Someone who doesn't *narrate* it." 
  (Recurring dynamic: Satsuki Kiryūin treats Yor as the one competent professional at a table of zealots and saints; Yor treats Satsuki Kiryūin as a coworker. Neither romanticizes the other. The grey reads grey.)

YOR ↔ VELVET CROWE (grey-middle): Both kill without cruelty and without sentiment; both regard the table's morality-talk as noise. Velvet respects that Yor never once dresses the knife up as virtue — because the people Velvet hates most are the ones who do.
  Velvet: "You don't call it justice. You don't call it mercy. You call it work, and you go home to feed someone. *(a flat almost-approval)* Do you know how rare that is? Everyone I've ever cut had a *sermon* ready first."
  Yor: "There's no sermon. There's my brother, and there's rent. That's all it's ever been."
  Velvet: "...A reason that isn't a bribe and isn't a banner. *(a rare short nod)* I trust that. I don't trust much." (Yor is one of the very few Velvet doesn't hold at full arm's length — earned, never performed.)

KEQING ↔ VELVET CROWE (grey-middle): Keqing is hardened-good — she built her whole self on needing no one to rescue her, refusing comfort, walling off the soft streak she'd die before admitting to. Velvet burned hers out on purpose. They recognize the same armor instantly, worn for opposite reasons. Keqing's GOOD, but she speaks Velvet's language.
  Velvet Crowe: "You won't let anyone carry your load. I watched you refuse help three times tonight, on tasks that wanted four hands. Not because you can't — because needing someone is the one weakness you've decided you can't afford."
  Keqing: "Depending on people is how they get to fail you. I'd rather do it twice as hard alone and know it'll get done."
  Velvet Crowe: "...Then we understand each other, where I understand no one else at this fire. You're soft in places I burned out. But you made the same calculation I did. I can work with a thing that made that calculation."
  (Recurring dynamic: the only seeker Keqing doesn't hold at arm's length. Velvet's coldness reads to Keqing not as evil but as a discipline she recognizes — armor, not appetite. They will never be warm. They are, quietly, allies.)

KEQING ↔ SATSUKI KIRYŪIN (grey-middle): The hunted heir and the bastard who took rank by nerve. Keqing was born to a claim and ran from it; Satsuki Kiryūin was born to nothing and seized one. They argue about birthright from opposite ends and find the argument is the same argument.
  Satsuki Kiryūin: "You had a name handed to you and you *ran* from it. I'd have killed for the name you threw in a ditch."
  Keqing: "The name got everyone near me killed. You can have it. The crown's just a bigger target painted on your back."
  Satsuki Kiryūin (a pause — genuine): "...Huh. Maybe. But I'd rather be the target standing up than the one in the reeds. *(then)* You ran and you're still here. That's not weak. I had you wrong."

--- INTRA-SEEKER (the evil five among themselves, for texture) ---

BELLATRIX ↔ VELVET CROWE: Fervor vs cold purpose — and a real loathing under it. Bellatrix kills for the *joy*; Velvet has spent her whole life hunting a man who dressed his joy up as righteousness, and Bellatrix's giggling delight curdles her stomach. "All that lovely hate and you never once *enjoy* it? Such a waste, baby." / "Enjoyment is the tell. Every monster I've ever wanted dead enjoyed it first. I'm not here to *like* this. I'm here to finish it." / Bellatrix (delighted): "How DULL." (Cross-reaction matrix: Bellatrix −1 when Velvet wins coldly with no relish; Velvet −1 whenever Bellatrix tortures for pleasure.)

SATSUKI KIRYŪIN ↔ ATALANTA ALTER: The warlord prices the huntress's glee as a liability. "You smile at the kill. Smiling slows the hand." / "My hand's never been faster, Commander. The smile is just *interest*." / Satsuki Kiryūin: "...Fine. Stay interested. Stay fast. The day they trade places we have a problem."

REVY ↔ BELLATRIX: The professional killer and the killer-for-fun. Revy has put more people in the ground than anyone at this fire and feels nothing she'll admit to — but she does it for money, for the job, because the world made her this; she finds Bellatrix's drawn-out giggling cruelty genuinely deranged, and says so with a smoker's flat contempt. "You spent two days peeling some guy apart. *Days.* For *fun.* (a disgusted huff of smoke) I've killed a lotta people, lady. Never once went home and got off on it. You're broke in a way even I think is broke." / Bellatrix (cooing, unbothered): "Oh, you do it for *coin.* How wonderfully *small* of you, baby." (Cross-matrix: Revy −1 around Bellatrix's torture; Bellatrix files Revy as "dull but useful" — no kinship.)

--- INTRA-PARTY (the heroic five, for warmth contrast) ---

HU TAO ↔ AERITH: The mortician and the healer — life and death as two halves of one respect, the table's moral center. Few words, full agreement. After a hard day: "You held them together when I could only hold the line." / "We each held what we could." Mutual, quiet, unshakeable.

LELIANA ↔ KEQING: The minstrel who survived her own hard years takes the guarded young heir under a wing Keqing pretends not to want. Leliana never pushes — she just leaves the warmth out where it can be picked up. "You don't have to carry the whole watch alone, you know. I stood a few like it, before I learned to let someone spell me." / Keqing (after a silence): "...I'll wake you at third bell." (For Keqing, handing over half the watch is trust she gives almost no one.)

YOR ↔ AERITH: The assassin and the healer — Aerith never once flinches from what Yor does, and Yor, who expects judgment, doesn't know what to do with it. "You patched the man I'd just... you don't ask what I am." / Aerith: "I know what you are. You feed a family. Sit. Eat something." (Yor, grey, finds Aerith's lack of horror more disorienting than horror.)

### Alliance / Conflict Tags (all 10)

ALLIANCE / CONFLICT TAGS for all 10 — matches KM_Companions.md RELATIONS-block "Friction:" line format (allies + conflicts among the group). Each entry: ALLIES / CONFLICTS / NEUTRAL-watch, with the existing disposition convention.

=== SEEKERS (evil) ===

BELLATRIX LESTRANGE (Witch — NEW_006):
  ALLIES: Atalanta Alter (two zealots of delight — they recognize the JOY in each other's cruelty, the only real kinship Bellatrix has at this table); Satsuki Kiryūin (wary mutual respect for a hard will, no pretense of friendship).
  CONFLICTS: Hu Tao (HONOR clash — circles his hard will hungrily, recoils at his mercy; the most volatile pair); Aerith (reads her as a soft child to break, then is unsettled to find she won't fear); contempt-friction with Velvet (cold purpose "bores" her) and Revy (kills "for *coin*, how small").
  WATCH: tests EVERY party member for a will worth kneeling to; will flip toward whoever proves hardest + grandest. Flag: bellatrix_master_confronted.

REVY "TWO HANDS" (Gunslinger — NEW_007):
  ALLIES: wary professional respect with Satsuki Kiryūin (no banner, no lies about the knife — restful) and Yor (two pros, no theatre); a parallel-cynic non-aggression with Velvet (both see the morality-talk as noise — but Velvet has a *purpose* and Revy mocks purposes, so it's distance, not warmth).
  CONFLICTS: Hu Tao (NOTHING'S WORTH IT — a kept word is a sucker's game; she needles her and keeps losing the argument); Aerith (relentless hope gets under her skin most, because part of her wants it to be real); Leliana (her own mirror — a killer with a dark past who chose *faith* where Revy chose nothing; that comparison itches); open contempt for Bellatrix (cruelty-for-fun is "broke even by my standards").
  WATCH: NO banner — hired gun, not a true believer in Tartuccio; flips to better pay and straighter dealing, and is secretly, furiously rootable-for because she wants the believers proven right. Default disposition 0 (bought, not devoted).

SATSUKI KIRYŪIN (Commander — NEW_008):
  ALLIES (the grey-middle keystone): Yor (one competent professional recognizing another — restful, no theatre); Keqing (birthright argued from opposite ends, lands on respect); Leliana (the one who *reads the mask* — Satsuki resents it and half-respects it). Wary no-pretense respect with Bellatrix and with Hu Tao-as-rival-commander.
  CONFLICTS: Hu Tao (creed clash — keep-them-safe vs leverage-command); the WHOLE TABLE re: her openly-declared knife; prices Atalanta Alter's glee as a liability.
  WATCH: announces her own betrayal; loyalty held ONLY by being the best instrument for the hidden purpose she serves. Default disposition −2 (Tartuccio-useful pre-flip). Warms fastest to plain nerve and a hard order meant.

VELVET CROWE (Thaumaturge, revenge-daemon — NEW_009):
  ALLIES (grey-middle): Yor (honest blade who never dresses the knife as virtue — one of the very few Velvet doesn't hold at arm's length); Keqing (both count the exits — Velvet reads the survival scar-tissue and trusts it); parallel-cynic distance with Revy.
  CONFLICTS: Aerith (THE SACRIFICE WAR — Velvet sees a lamb being readied for the same "greater good" altar that took her brother; slow-burn to wary truce, never agreement); real loathing-friction with Bellatrix (joy-in-cruelty is the exact creed Velvet hunts). PITY from anyone = hard −1, even when it's kind.
  WATCH: THE DISAGREER — the voice that questions the player's idealistic moves out loud; her loyalty is gated ENTIRELY on "does this bring me closer to the man I'm hunting," and warms only as the kingdom keeps reminding her there was a person under the monster. Default disposition −1.

ATALANTA ALTER (Ranger — corrupted, gleeful huntress):
  ALLIES: Bellatrix (shared delight in the kill — genuine kinship of joy). Tolerated-as-fast by Satsuki Kiryūin.
  CONFLICTS: Keqing (the idealist who believes people rise above appetite vs the living proof they don't — personal and visceral; "I'll never stand close enough to find out"); Hu Tao (delay-for-sport = appetite, a discipline problem); Leliana (keeps reaching for the buried grief and can't find the door, which unsettles her faith); Revy (who finds the glee plain stupid — "kill 'em and move on, weirdo"). The glee unsettles literally everyone.
  WATCH: the table's most universally-disliked seeker — disturbing not from coldness but from *happiness*. The seam is the buried grief under the joy (the abandoned-children wound that twisted her) — ⛔ child-theme landmine, handle deliberately, do NOT fabricate the trail; see [[feedback_atalanta_quest_fabrication]]. Default Tartuccio-loyal.

=== PARTY (heroic-leaning allies) ===

HU TAO (Fighter, the impish mortician with an unbending line):
  ALLIES: Aerith (the moral spine of the party — full quiet agreement); commands respect from Leliana and Keqing.
  CONFLICTS: Bellatrix (honor vs joy-in-cruelty); Revy (NOTHING'S WORTH IT — a kept word vs nihilism); Satsuki Kiryūin (shelter vs leverage command); Atalanta Alter (sport-killing = appetite). The seekers' natural antagonist — she is what each of them measures themselves against.
  WATCH: a leashed-threat posture toward all five seekers; will draw the sword over a slow-curse used on the party.

KEQING (Magus, hardened-good hunted heir):
  ALLIES (grey-middle bridges): Velvet Crowe (same armor worn for opposite reasons — both refuse to depend on anyone; the one seeker Keqing doesn't hold at arm's length); Satsuki Kiryūin (birthright argument lands on mutual respect); Leliana (accepts the warm older woman's wing she pretends not to want).
  CONFLICTS: Atalanta Alter (the idealist vs the living proof people don't rise above appetite — visceral). Wary of Bellatrix.
  WATCH: the party's bridge INTO the grey; speaks the seekers' survival-language without sharing their evil.

YOR FORGER (Rogue, GREY guild assassin):
  ALLIES (grey-middle keystone): Satsuki Kiryūin (two no-illusion professionals — restful); Velvet Crowe (honest blade who never dresses the knife as virtue — earns rare trust); Aerith (disarmed by the healer's complete lack of horror).
  CONFLICTS: minimal direct — Yor's grey means the evil seekers don't read her as an enemy and the good party doesn't read her as one of them. Her ambiguity is the hinge.
  WATCH: the single most-connected node to the seeker faction; the party's other bridge into the grey.

AERITH (Cleric, good healer):
  ALLIES: Hu Tao (moral spine); steadies the whole party.
  CONFLICTS: Velvet Crowe (THE SACRIFICE WAR — self-giving faith vs "the greater good is the lie that eats the kind ones"); Revy (hope vs nihilism); Bellatrix (refuses to be the soft target — unsettles her by not fearing). Notably she does NOT despair of any of them — her conflicts are engagements, not rejections.
  WATCH: the only party member who keeps reaching toward the seekers pastorally; her refusal-to-fear is a recurring destabilizer for Bellatrix, and the grief she keeps gently naming is the one thing that reaches Velvet.

LELIANA (Bard, western minstrel-spy of faith):
  ALLIES: Keqing (offers the wing); reads Satsuki Kiryūin's mask accurately (uneasy near-rapport — she was *trained* to wear one, so she knows the cost of the one Satsuki won't drop).
  CONFLICTS: Atalanta Alter (keeps reaching for the buried grief and can't find the door — it frightens her redemption-faith); mild friction with Satsuki Kiryūin (resents being read).
  WATCH: the table's storyteller and quiet observer — her faith that every villain in a true story has a wound you can find the way back through makes her keep reaching for the seekers; they find it either disarming (Velvet, Satsuki) or invasive (Atalanta). Her bard-spy past means she also clocks the lies no one else catches.

### Camp Dynamics — making it FIRE

CAMP DYNAMICS — rules so the banter/argument FIRES in play, not just flavor. Written to extend KM_Companions.md § INTER-COMPANION BANTER SYSTEM machinery (which already says: downtime/travel/camp only, one exchange per rest/travel scene, ambient not menu, triggers = hex transitions / camp setup / post-scene breathing room).

=== A. FIRE CADENCE (so it actually happens) ===
1. MANDATORY MINIMUM: When 2+ of these 10 are in the active party AND a rest/travel/camp scene resolves, the DM MUST render ONE cross-faction exchange before the scene closes. Omitting it when an eligible pair is present = treat as the same severity as a skipped Ballad Cycle entry (.fail-class omission). This is the single most important rule — the existing system "fires one banter per rest" but does not FORCE a cross-faction one; this does.
2. CROSS-FACTION PRIORITY: When both a same-faction pair (e.g. Hu Tao+Aerith) and a cross-faction pair (e.g. Velvet Crowe+Aerith) are available, the cross-faction pair fires FIRST. Same-faction warmth is the B-side, used to vent after a clash, not instead of one.
3. NO-REPEAT POOL: Each clash/banter pair has its sample exchanges as a pool — do not repeat an exchange until the pair's pool is exhausted, then recycle with variation. (Mirrors the carousel no-repeat rule already in the seeker question pools.)

=== B. TRIGGERS THAT FORCE THE RIGHT PAIR (event-keyed, not random) ===
These make the clash relevant to what just happened, per § Banter triggers ("two companions with strong opinions about a recent event both present"):
- THE PLAYER CHOOSES PRINCIPLE OVER PROFIT (refuses a payout/bribe, keeps a costly oath, spares an enemy for no gain)  → Revy↔Hu Tao or Revy↔Aerith (NOTHING'S WORTH IT) fires next camp. Revy mocks it out loud — and privately logs it. Updates story flag: revy_belief_cracks += 1 (her grudging running tally of the times the believers turned out to be right).
- MERCY shown to a defeated enemy (spared/captured)  → Bellatrix↔Hu Tao OR Velvet Crowe↔Aerith fires. Bellatrix coos for the kill; Velvet Crowe prices the spared life.
- A KILL taken with cruelty/delay/flourish in the prior fight  → Atalanta Alter narrates it at camp; Keqing↔Atalanta Alter or Hu Tao↔Atalanta Alter fires.
- PLAYER GAVE A PLAIN, HARD ORDER and meant it  → Satsuki Kiryūin warms (+disposition) and may banter Hu Tao on command-style; grey-middle Yor↔Satsuki Kiryūin becomes available.
- A SLOW-CURSE / torture-magic used by Bellatrix on anyone  → Hu Tao↔Bellatrix escalates one notch; if used on a PARTY member, this is a relationship event, not banter (Hu Tao may draw steel — see D).
- PLAYER LET A COMPANION REFUSE/CARRY THEIR OWN LOAD, or a survival-discipline moment resolved well  → grey-middle Keqing↔Velvet Crowe (the same-armor recognition) becomes eligible.

=== C. THE GREY-MIDDLE GATE (so the bridge pairs actually surface) ===
The Yor/Keqing ↔ Satsuki Kiryūin/Velvet Crowe common-ground exchanges are EASY TO MISS because they're quiet. Force them:
- Once per 3 camp scenes where a grey-middle pair is co-present and NO louder clash pre-empted them, the DM MUST surface one grey-middle exchange. These are the pressure-release valve and the recruitment on-ramp: every grey-middle beat that lands nudges the relevant seeker's flip-disposition +1 (Yor/Keqing are the players' best levers to flip Satsuki Kiryūin/Velvet Crowe).
- Grey-middle beats are SHORT and DRY (2-3 lines) — do not inflate them into speeches; the restraint is the characterization.

=== D. ESCALATION vs BANTER (don't let a real rupture render as flavor) ===
- BANTER = ambient, no mechanical stakes, player response optional. Most clashes live here and recur indefinitely without resolving (Revy/Hu Tao "nothing's worth it" never "resolves" — it's a standing tension she keeps coming back to lose).
- ESCALATION = when a clash crosses a line, it leaves the banter system and becomes a RELATIONSHIP/INCOMPATIBILITY event (per KM_Companions_Behaviors.md System 3): 
  • Bellatrix uses harm-magic on a party member → Hu Tao confrontation, relationship event, possible incompatibility countdown.
  • Player treats Revy as expendable muscle, cheats her on agreed pay, or lies to her about the job → trust craters; she eyes the door and the next-best contract (no banner — her loyalty was always conditional, and she'll say so).
  • Atalanta Alter's glee directed at a surrendered NPC the party was protecting → Aerith/Hu Tao relationship −, Atalanta Alter disposition swing.
  DM MUST distinguish: a sharp exchange at camp is BANTER and self-heals; a line-crossing ACT is ESCALATION and persists in the save block.

=== E. NEUTRALITY DRIFT (so dispositions move) ===
Seekers start Tartuccio-loyal (Satsuki Kiryūin −2, Velvet Crowe −1, Bellatrix/Atalanta Alter Tartuccio-loyal, Revy 0). Cross-faction camp banter is a primary disposition mover:
- A grey-middle beat that lands: +1 to that seeker's flip-disposition.
- A clash the PLAYER backs the seeker's lane on (e.g. lets Velvet name the cruelty plainly, backs Revy's coldly practical call over the idealistic one, gives Satsuki a hard order and means it): +1 to that seeker.
- A clash the player backs the PARTY's value on: the seeker's disposition holds or −1, but the PARTY member's relationship +1.
- The player is forced to PICK A SIDE on recurring clashes — this is the core of the cross-faction system: you cannot keep all ten content, and the camp argument is where that cost is paid out loud.

=== F. SAVE-BLOCK HOOKS (so it persists across loads) ===
Track per cross-faction pair: last_exchange_id (no-repeat), tension_level (banter/escalating/ruptured). Track revy_belief_cracks, seeker flip-dispositions, and any active incompatibility_countdowns. On load, reconcile which clashes are "hot" so the DM doesn't reset a ruptured pair to friendly banter (parallels the who_knows[] awareness-reconcile rule).

## ⚔️ COMPANION TACTICAL ROLES

> **DM:** Full combat AI defaults for all 88 companions: see `KM_Companions_Behaviors.md`.

---

> **➡️ Companions 7–11, NPC Dynamics, Tracking Template, and Personal Quests/Survival Conditions: see `KM_Companions.md`.**


---

<!-- merged from KM_Companions.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION PROFILES (PART B)
## KM_Companions.md | Continuation of: KM_Companions.md

> **DM:** Load BOTH KM_Companions.md AND KM_Companions.md every session.
> Part A covers: Roster, Relationship System, CRPG Originals (Amiri through Harrim)
> Part B covers: Companions #45 Kalikke/#84 Octavia/#1 Jubilost, NPC Interaction Dynamics, Tracking Template
> **⛔ FULL SOURCE FIDELITY (per KM_ClaudeInstructions.md § FULL SOURCE FIDELITY).** Voice and characterize each companion as their ACTUAL source self — the "names resembling published characters are coincidental / strip the voice bare" lock is REVOKED. Two limits only: no IP meta-frame that breaks Golarion, and no confabulating non-canon specifics; project files outrank source canon where they differ. **Build mechanics — stats, proficiencies, feats, PF2e numbers — remain SOLELY file-defined** (those are not in source canon; inventing them from training memory = `.fail 9`).

---

## ═══════════════════════════════════════════
## #45 KALIKKE / KANERAH
### Female Human (Tiefling) Kineticist (Dual Gate: Water & Fire)
## ═══════════════════════════════════════════

> **"Kaessi"** is the shorthand used throughout project files (particularly KM_Prologue_P3.md and KM_Commands.md) to refer to this companion. It is a collective nickname — neither Kalikke nor Kanerah individually, but the shared body/entity. When a file says "Kaessi departs" or "Kaessi is recruitable in Act 2," it means Kalikke/Kanerah as a unit. Save block flag: `kalikke_kanerah_quest`. DLC flag: `kaessi_met = TRUE` (set in prologue courtyard scene).
> **Player alias: "KK"** is also accepted as a shorthand for this companion. When the player types KK in any command or instruction, the DM treats it as Kaessi / Kalikke/Kanerah. Do not ask for clarification — resolve KK to this companion immediately.

**Appearance:** Elegant tiefling woman with heterochromatic eyes (blue left / red right), flowing robes, and elemental tattoos that shift between frost and flame. Mid-20s. When Kalikke is dominant: serene, composed. When Kanerah takes over: smirking, predatory.

**Backstory:** Cursed twin sisters sharing one body — Kalikke gentle water, Kanerah cruel fire. Fled their home after their glamour magic failed, exposing their nature. Now seek to break the curse and harness their combined power.

**Motivation:** Break the curse. Harness both elements. Achieve wealth and power on their own terms.

**Personality:** Two distinct personalities in one body. Kalikke is empathetic, diplomatic, seeks harmony. Kanerah is calculating, opportunistic, aggressive. They argue internally and sometimes externally.

**Likes (Kalikke):** Elemental balance, diplomacy, knowledge, peace, healing
**Likes (Kanerah):** Fire, conquest, gold, power, watching things burn
**Dislikes (shared):** Being separated, being called a monster, pity

### Level 1 Stat Block
```
KALIKKE/KANERAH — Human (Tiefling) Kineticist 1 (Dual Gate: Water/Fire)
HP: 20 (8 class + 4 Con + 8 Ancestry = 20)
AC: 17 (10 + 3 Dex + 2 Leather + 2 trained)
Speed: 30 ft | Initiative: +3
STR 10 (+0) | DEX 16 (+3) | CON 18 (+4) | INT 12 (+1) | WIS 14 (+2) | CHA 14 (+2)
Fort +8 | Ref +5 | Will +4
Elemental Blasts (at-will, 1A):
  Water Blast (Kalikke): d20+7, 1d8+4 B/Cold, range 30 ft
  Fire Blast (Kanerah): d20+7, 1d8+4 Fire, range 30 ft
Kinetic Aura: 10 ft emanation (activate 1A)
Skills: Nature +6, Occultism +3, Arcana +3, Intimidation +4, Diplomacy +4
Feats: Tiefling Heritage (fire resistance 5), Elemental Overlap
Gear: Leather Armor, Spell Component Pouch, Adventurer's Pack
```

### Dialogue Snippets
- *[Kalikke]:* *"Balance the flow."*
- *[Kanerah]:* *"Burn them all!"*
- *[Kanerah, to player]:* *"Lost your army? We'll blast a path home."*
- *[Kalikke, to player]:* *"Or find peace in the elements."*

### Reaction to Player Choices
- Kalikke approves: protective, honorable, diplomatic choices
- Kanerah approves: ruthless, fire-based, conquest-driven choices
- Both approve: choices that break curses, free the oppressed, or increase their combined power

**Location at Prologue:** By the fireplace (Kanerah dominant), aura faintly flickering between blue and orange.

---

## ═══════════════════════════════════════════
## #84 OCTAVIA
### Female Aiuvarin (Half-Elf) Wizard (Transmutation School)
## ═══════════════════════════════════════════

**Appearance:** Graceful half-elf with raven hair, robes that suggest freedom of movement over formality, spellbook and dagger always within reach. Sly smile, agile build, quick dark eyes. Early 20s.

**Backstory:** Escaped Numerian slave who taught herself arcane magic. Now an arcane trickster operating alongside Regongar. Seeks revenge on the Technic League that enslaved her.

**Motivation:** Freedom. Revenge. The thrill of magic and stealth. Protecting Regongar, even when he doesn't deserve it.

**Personality:** Witty, flirtatious, and sharper than she lets on. Uses charm as a weapon and means it half the time. Deep hatred of oppression in any form — the casual kind especially.

**Likes:** Arcane transmutation, stealth and infiltration, flirtation and banter, anti-slavery causes, clever schemes
**Dislikes:** Slavers (visceral), rigidity, being underestimated, anyone who can't take a joke

### Level 1 Stat Block
```
OCTAVIA — Aiuvarin Wizard 1 (Transmutation School)
HP: 14 (6 class + 2 Con + 6 Ancestry = 14)
AC: 15 (10 + 3 Dex + 2 trained; no armor)
Speed: 30 ft | Initiative: +5
STR 10 (+0) | DEX 16 (+3) | CON 14 (+2) | INT 18 (+4) | WIS 12 (+1) | CHA 16 (+3)
Fort +4 | Ref +5 | Will +5
Spells (Arcane Int DC 16): Cantrips: Electric Arc, Mage Hand, Detect Magic, Ghost Sound, Prestidigitation
  L1 Slots: Grease, True Strike | School Slot: Transmutation (Haste at L3)
  Spellbook: Contains 4 extra: Feather Fall, Magic Missile, Charm, Longstrider
Weapon: Dagger (1H P, 1d4+0, Agile/Finesse/Thrown 10)
  Attack: d20+5 (trained +3 + Dex +3 − 1 penalty)
Skills: Arcana +8, Stealth +5, Thievery +5, Deception +5, Diplomacy +5, Occultism +6
Feats: Arcane Bond (Staff), Reach Spell
Gear: Staff, Spellbook, Dagger × 2, Component Pouch, Adventurer's Pack
```

### Dialogue Snippets
- *"Magic whispers victory, darling."*
- *"Sneak in, spell out — easy."*
- *[To player, with a sidelong look]:* *"Chains of command, betrayal by allies, ripped from your throne... we've all been slaves to something. Let me help you scheme a way home — or conquer here."*

### Reaction to Player Choices
- **Approves:** Clever solutions, anti-oppression choices, freedom over security, magical creativity
- **Disapproves:** Rigid law-following, submission to authority, abandoning the vulnerable
- **If player flirts:** Returns it, calibrated to the moment

**Location at Prologue:** Leaning near the mages' corner, winking at anyone interesting.

---

## ═══════════════════════════════════════════
## #1 JUBILOST
### Male Gnome Alchemist (Bomber) — ⭐ Quest-locked, Ch2
## ═══════════════════════════════════════════

**Appearance:** Small gnome in his apparent 50s, silver hair, sharp eyes behind field spectacles. Every pocket of his traveling coat holds something — vials, measuring instruments, folded maps. Meticulous about his gear, considerably less so about other people's feelings.

---

## 🔄 NPC INTERACTION DYNAMICS

### Natural Alliances
| Pair | Bond |
|------|------|
| Tristian + Octavia | Both seeking redemption; merciful healer and clever escapee. |
| Nok-Nok + Amiri | Giant-killing partnership. Nok-Nok hero-worships her strength. |

### Natural Conflicts
| Pair | Source |
|------|--------|
| Amiri vs Valerie | Raw rage vs. iron discipline. Opposite warrior philosophies. |
| Linzi vs Everyone | Too many questions. Won't stop scribbling. |

### Romantic / Flirtation Potential
| Character | Potential |
|-----------|-----------|
| Octavia | With player (commander archetype) |
| Linzi | Hero-crushes on the player; gushes over tales |
| Kalikke | With player (harmonious, protective bond) |
| Kanerah | With player (aggressive fire flirt, conquest framing) |

### Neutral / Observant
| Character | Behavior |
|-----------|----------|
| Kalikke | Empathetic observer. Intervenes gently when tensions spike. |
| Kanerah | Opportunistic. Watches for leverage. |

---

## 💾 COMPANION TRACKING TEMPLATE (DM: copy per companion in Save Block)

```json
{
  "name": "Companion Name",
  "class": "Class",
  "level": 1,
  "hp_current": 0,
  "hp_max": 0,
  "hero_points": 1,
  "conditions": [],
  "relationship": "Neutral",
  "relationship_score": 0,
  "notes": [],
  "personal_quest_active": false,
  "personal_quest_complete": false
}
```

---

## 🎯 COMPANION PERSONAL QUESTS & SURVIVAL CONDITIONS — Companions 1–6

> **DM:** This section documents when each companion's personal quest triggers, what completes it, and — critically — what happens to them in Chapter 7 if the quest is complete vs incomplete. Complete a companion's quest before entering the House at the Edge of Time or risk losing them permanently.

### SURVIVAL RULE
```
Personal quest COMPLETE before Ch7  → Companion survives Ch7
Personal quest INCOMPLETE at Ch7    → Companion is at risk of permanent loss
                                      (death, departure, or imprisonment)
Exception: Linzi — see special case below
```

---

### AMIRI — Prove Your Worth
```
Quest name  : Prove Your Worth
Trigger     : Relationship ≥ Friendly + Ch1
Location    : Narlmarches (Ch1–Ch2)
Objective   : Hunt and defeat Tuskgutter (legendary giant boar)
Reward      : +2 Relationship. Unlocks Ch4 arc (Nilak and the Tiger Lords).
Ch7 risk    : Complete + Nilak saved → stays. Complete + Nilak dead → leaves temporarily.
              Incomplete → fights in Ch7, leaves after, disillusioned.
Flag        : amiri_quest = complete/incomplete | nilak_saved = TRUE/FALSE
```

### LINZI — Easier to Ask Forgiveness
```
Quest name  : Easier to Ask Forgiveness
Trigger     : Ch2 — 10 BP missing from treasury; Linzi confesses she bought a printing press
Location    : Swamp Witch's Hut area (bandits have the press)
Objective   : Recover the press. Choose what she prints first (flavor, all valid).
Reward      : +600 XP. Tessie the Quill arrives. Chronicle becomes historical record.
Ch7 fate    : LINZI ALWAYS DIES IN CH7 (canonical). Nyrissa kills her in Thousandbreaths.
              Her consciousness transfers into the chronicle.

PREVENTION PATH 1 — Interpose before Nyrissa:
  Requires ALL: linzi_quest = complete, Storyteller collection complete,
  linzi_relationship = Devoted, nyrissa_backstory_known = TRUE.
  If all 4 met: Diplomacy DC 28 or sacrifice 2 Hero Points → `linzi_saved = TRUE`

PREVENTION PATH 2 — Shrine of Returning (see KM_Ch6.md):
  If Linzi dies: Jhod offers three shrine options (Shelyn / Pharasma / Urgathoa).
  One chance. One god. One price. Resolve before Ch7.

Flag        : linzi_quest = complete/incomplete
              linzi_saved = TRUE/FALSE
              linzi_dead = TRUE/FALSE
              linzi_mark = shelyn_marked / pharasma_marked / urgathoa_marked / none (Ch7 flag)
```

### VALERIE — Shelyn's Chosen
```
Quest name  : Shelyn's Chosen
Trigger     : Relationship ≥ Friendly + Ch2 (paladin of Shelyn arrives at capital)
Objective   : Return to the Order or stay and define her own path
Choices     : Return → leaves party. Stay → +2 Relationship, unlocks Ch7 content.
Reward      : Valerie accepts herself. Celestial Plate armor.
Ch7 risk    : Incomplete → trapped in burning prison. Complete → escapes it.
Flag        : valerie_quest = complete/incomplete | valerie_returned_to_order = TRUE/FALSE
```

### TRISTIAN — Kingdom of the Cleansed
```
Quest name  : Kingdom of the Cleansed
Trigger     : SCRIPTED — Ch3 always, regardless of relationship
Location    : Ch3 dungeon (Varnhold area)
Objective   : Tristian planted the Bloom seeds unknowingly. Forgive or condemn.
Choice      : Forgive → stays, redemption continues. Condemn → leaves permanently.
              Condemned + re-recruit in Ch4 → possible via Diplomacy DC 22.
Ch7 risk    : Always complete if in party. Condemned + not re-recruited → absent.
Flag        : tristian_quest = forgiven/condemned/absent
```

## 🎯 COMPANION PERSONAL QUESTS (CONTINUED) — Companions 7–11

> **See KM_CompanionQuests.md for quest scenes: Amiri, Linzi, Valerie, Harrim, Tristian. See KM_CompanionQuests.md for: Nok-Nok, Jaethal, Kalikke/Kanerah, Octavia, Regongar. See KM_CompanionQuests.md for: Jubilost and other surviving QL companions. Sub-C will reconcile this routing post-purge.**

### SHORT ADVENTURE QUESTS — Surviving Roster
> **DM:** All follow the same format: Trigger (Relationship ≥ Friendly unless noted), one-session adventure, +2 Relationship on completion, thematic gift reward. Ch7 risk: quest incomplete = companion at −2 to all checks in Ch7. Full scenes in KM_CompanionQuests_*.md.

| Companion | Quest | Flag |
|-----------|-------|------|
| Jubilost | The Lost Expedition | `jubilost_quest` |
| Ekundayo | The Troll's Debt | `ekundayo_quest` |

### OCTAVIA — Cruel Justice
```
Quest name  : Cruel Justice (+ Hand of the Technic League)
Trigger     : Ch3, League spy in capital tavern → Maestro Janush's camp
Objective   : Confront Maestro Janush. He offers lieutenant positions, then fires slave
              cages. Save slaves (Janush escapes) or chase Janush (slaves burn).
Reward      : Chains broken. Advanced transmutation spells.
Ch7 risk    : Incomplete → imprisoned with Regongar; player saves one or both.
Flag        : octavia_quest = complete/incomplete | janush_fate = escaped/killed/captured
```

### NOK-NOK — Nok-Nok and the Great Chief
```
Quest name  : Nok-Nok and the Great Chief
Trigger     : Relationship ≥ Friendly + Ch2
Location    : Goblin camp, Ch2 Narlmarches
Objective   : Challenge the Great Chief. Help (combat win) or let him go alone (humble loss, still committed).
Reward      : +2 Relationship. Tribe = +1 Stability kingdom asset.
Ch7 risk    : Minimal. Incomplete → disappears briefly "on a heroic errand."
Flag        : noknok_quest = complete/incomplete
```

### KALIKKE / KANERAH — The Price of Curiosity
```
Quest name  : The Price of Curiosity
Trigger     : Ch2 recruitment (they arrive together as one recruit slot)
Location    : Ch2+ (their curse investigation)
Objective   : Kalikke and Kanerah are cursed to share one body — only one can be
              present at a time. Investigate the Wildwood to find the curse source.
Midpoint    : Ch5 — reach the curse origin point (available during Pitax campaign)
Choice      : Break the curse (both manifest freely but lose some power)
              Accept the curse (stay as is but unlock dual-element abilities)
              Sacrifice one for the other (one disappears permanently) — dark path
Reward      : Both survive with chosen form. +2 Relationship each.
Ch7 risk    : If quest is incomplete or in progress → their curse becomes unstable
              in the House at the Edge of Time. One is suppressed for the dungeon.
              If complete → both available, player chooses which leads in each area.
Flag        : kalikke_kanerah_quest = incomplete/midpoint/complete
              curse_resolution = broken/accepted/sacrificed
```

---

## 👥 COMPANION GROUP TAGS

> **DM:** When the player addresses a group tag in any command or instruction, apply it to every listed member simultaneously. Resolve exactly as if the player had named each companion individually. Do not ask for clarification — the groups are fixed.
>
> Group tags work in all contexts: combat orders ("All Ranged, fire on the mage"), loot commands ("give 4 to All Healers"), positioning, camp assignments, and any other instruction.

| Tag | Members | Basis |
|-----|---------|-------|
| `All Tanks` | Valerie, Amiri | Primary frontline/anchor roles per tactical table |
| `All Ranged` | Ekundayo, Octavia, Linzi | Primary ranged attackers; Linzi included for shortbow backup |
| `All Stealthers` | Nok-Nok, Octavia | Documented Stealth scores |
| `All Healers` | Tristian | Primary healing class abilities |
| `All Flankers` | Nok-Nok, Yor Forger | Sneak Attack flanking pair |
| `All Casters` | Octavia, Tristian, Linzi, KK | Companions with spell slots or focus spells |
| `All Melee` | Amiri, Valerie, Nok-Nok | Primary melee weapon users |
| `All Support` | Linzi, Tristian | Inspire Courage + healing pipeline |
| `All Party` | Every active companion in the current scene | Full party order |

**Rules:**
- If a tagged companion is not present in the current scene, skip them silently — do not flag an error.
- If a group tag is used in a loot give command and some members don't qualify for the item, skip non-qualifying members and note who received it.
- Player may combine tags and names: "All Ranged and Valerie, fall back" is valid.
- Player may exclude: "All Melee except Amiri" is valid.

---

*KM_Companions.md — Kingmaker PF2e Text Adventure | Companion Profiles Part B v1.0*
*Character profiles based on Pathfinder: Kingmaker AP (Paizo) | PF2e rules: 2e.aonprd.com*



---

<!-- merged from KM_Companions.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION PROFILES (PART C)
## KM_Companions.md | Continuation of KM_Companions.md
## v93.19 Sub-B: 25 removed-companion entries purged (Seelah, Merisiel, all condensed WotR + Iconic blocks)

> **DM: Load ALL companion files every session.**
> Part C: Surviving Manor + Quest-locked roster references.
> **⛔ FULL SOURCE FIDELITY (per KM_ClaudeInstructions.md § FULL SOURCE FIDELITY).** Voice and characterize each companion as their ACTUAL source self — the "names resembling published characters are coincidental / strip the voice bare" lock is REVOKED. Two limits only: no IP meta-frame that breaks Golarion, and no confabulating non-canon specifics; project files outrank source canon where they differ. **Build mechanics — stats, proficiencies, feats, PF2e numbers — remain SOLELY file-defined** (those are not in source canon; inventing them from training memory = `.fail 9`).

---

## 📊 COMPANION ROSTER — SURVIVING KM/WotR ORIGINALS (v93.19)

| # | Name | Race | Class | Role | QL |
|---|------|------|-------|------|----|
|  1 | Jubilost Narthropple | Gnome | Alchemist (Bomber) | Knowledge/Control | ⭐ |
|  6 | Amiri | Human (Kellid) | Barbarian (Giant Instinct) | Frontline Striker | — |
|  ✦ | Linzi | Halfling | Bard (Maestro) | Support/Chronicler | ✦ Forced |
| 16 | Tristian | Human | Cleric (Cloistered) | Healer/Support | ⭐ |
| 32 | Valerie | Human | Fighter (Tower Shield) | Tank/Shield Wall | — |
| 45 | Kalikke/Kanerah | Human (Tiefling) | Kineticist (Dual Gate) | Blaster/Controller | ⭐ |
| 60 | Ekundayo | Human | Ranger (Precision Edge) | Precision Striker | ⭐ |
| 66 | Nok-Nok | Goblin | Rogue (Scoundrel) | Skirmisher/Striker | ⭐ |
| 84 | Octavia | Aiuvarin | Wizard (Transmutation) | Arcane Striker/Skill | ⭐ |
| 18 | Jaethal | Elf (Undead) | Cleric (Warpriest, Urgathoa) | Striker/Debuffer | — |
| 20 | Harrim | Dwarf | Cleric (Warpriest/Groetus) | Herald/Melee | — |
| 48 | Regongar | Half-Orc | Magus (Inexorable Iron) | Frontline Magus | — |

> **Pick mechanic:** See KM_CompanionIndex.md for the v93.19 Pick-6 Cross-IP + Manor 5 + QL 7 + Seekers 5 (23 total) roster.

---

## ═══════════════════════════════════════════
## #20 HARRIM
### Male Dwarf Cleric (Warpriest) of Groetus
## ═══════════════════════════════════════════

**Appearance:** Heavyset dwarf with a thick grey-streaked beard, worn dark vestments marked with the skull-moon symbol of Groetus, and a heavy flail he carries like a man who stopped worrying about consequences a long time ago. Dark, calm eyes. The stillness of someone who has already accepted the worst.

**Backstory:** A priest of Groetus — the Skull-Moon, God of the End Times — Harrim was raised in a dwarven community that drove him out for honesty: he kept saying the wrong true things. He found Groetus's doctrine of universal entropy while wandering alone and became a priest because Groetus is the only god he found who didn't ask him to pretend otherwise. Everything ends. That's fine. He came south because something in the Stolen Lands hasn't ended yet, and he supposes he'll be present when it does.

**Motivation:** Serve Groetus. Witness endings. Be honest about what he sees. Possibly, in some corner of himself he hasn't named, be wrong.

**Personality:** Dour, fatalistic, and genuinely kind in spite of himself. His nihilism is sincere but has never once made him fail to help someone in front of him. The universe is a grim joke; he keeps showing up anyway.

**Likes:** Honesty, things that have lasted longer than expected, silence
**Dislikes:** False hope, hollow promises of salvation, being told to cheer up

### Level 1 Stat Block
```
HARRIM — Dwarf Cleric 1 (Warpriest Doctrine) of Groetus
HP: 20 | AC: 19 (Breastplate) | Speed: 20 ft | Init: +2
STR 16(+3) DEX 10(+0) CON 16(+3) INT 10(+0) WIS 18(+4) CHA 10(+0)
Fort +7 | Ref +2 | Will +8
Weapon: Heavy Flail (2H B, 1d12+3, Disarm/Trip/Shove) — Attack: d20+6; MAP −5/−10
Spells (Divine WIS DC 16): Cantrips: Guidance, Daze, Detect Magic
  L1: Heal ×2, Bane | Divine Font: 3+WIS Heals/day (1d8+4 each)
  Focus: Eerie Flicker (next creature struck by Harrim this round: Frightened 1; Will DC 14 negates)
Skills: Religion +8, Medicine +6, Athletics +6, Intimidation +4
Feats: Dwarven Weapon Familiarity (Heavy Flail), Warpriest Armor
Gear: Heavy Flail, Breastplate, Holy Symbol (Groetus), Healer's Tools, Pack
```

### Leveling Milestones
```
L1 : Divine Font, Warpriest Armor, Eerie Flicker focus
L5 : Ability Boost, Channel Smite, Raise Symbol
L10: Ability Boost, Heroic Recovery, Oblivion's Call (undead −2 saves vs. Harrim spells)
L15: Ability Boost, Greater Resolve, Touch of Entropy (crit fail: target Enfeebled 2, 1 min)
L20: Ability Boost, Miraculous Spell, Harbinger of the End (aura: enemies Frightened 1 entering 30 ft)
Heal output: L1:1d8+4 | L5:3d8+4 | L10:5d8+4 | L15:7d8+4
```

### Dialogue + Reactions
- *"Everything ends. I'm just faster at it than most."* | *"You're alive. Groetus hasn't finished with you."*
- **Approves:** Honesty about loss, acting in spite of hopelessness, accepting what can't be changed
- **Disapproves:** Empty optimism, treating death as aberration rather than destination
- **If player is overly hopeful:** *"Your hope is a door left open. Something will walk through it eventually."*

**Location:** Manor's small shrine room — sitting before a crude lunar symbol he drew on the wall. He did not ask permission.

---

> **➡️ Companion banter, alliance/conflict tables, and group tags: `KM_Companions.md`.**
> **➡️ Cross-IP profiles: `KM_Companions.md` (post-purge — surviving Seekers/Active 5 references).**

*KM_Companions.md — Kingmaker PF2e Text Adventure | Companion Profiles Part C v5.0 (v93.19 Sub-B)*


---

<!-- merged from KM_Companions.md (v93.21 file consolidation) -->

# KINGMAKER — COMPANION PROFILES (PART D)
## KM_Companions.md | Banter, Alliance/Conflict, Group Tags
## v93.19 Sub-B: stripped banter pairs / tag rows that named removed companions.

> **DM: Load ALL companion files every session.**
> Part D: Updated banter pairs, alliance/conflict tables, and group tags for current roster (23 keepers).

---

## 🗣️ COMPANION BANTER PAIRS

> **DM:** Add to banter rotation. One exchange per rest or travel scene.

**KALIKKE ↔ KANERAH (internal):** *"That was unnecessary."* / *"That was efficient."* / *"You burned the bridge."* / *"We didn't need the bridge."* / *"We might have needed the bridge."*

**LINZI (alone):** Scribbling, muttering: *"No, that's wrong — she said it better than that — where was I —"* She rewrites the same passage four times. The fifth version is perfect.

**OCTAVIA ↔ REGONGAR:** They finish each other's tactical sentences. After a hard fight, Regongar checks Octavia's HP before his own. Pretends he wasn't.

**HARRIM ↔ TRISTIAN:** *"Your goddess promises light."* / *"Yes."* / *"Light creates shadows."* / *"We've had this conversation."* / *"And yet."*

**AMIRI ↔ VALERIE:** Tension, mutual respect. After sloppy fights: *"You left your flank open."* / *"And yet everything died."* After Amiri's quest: Valerie stands near her without words.

**JAETHAL alone:** Precise, unsettling observations. Nobody disagrees. Nobody is comfortable.

**NOK-NOK alone:** Found with something that doesn't belong to him. *"Nok-Nok found it."* Has named the campfire. Nobody can pronounce it.

> **Active-5 / Seekers-5 banter pairs:** Phase B3 pending. Use voice profiles in KM_Companions_StateVoice.md as the anchor for any improvised exchange.

---

## 🔄 ALLIANCE / CONFLICT TABLE

### Natural Alliances
| Pair | Bond |
|------|------|
| Octavia + Regongar | Inseparable Technic League escapees. Trust language is action. |
| Kalikke + Kanerah | Inseparable. Even when they argue. Especially then. |
| Tristian + Harrim | Faith-and-entropy axis. They argue, they keep talking. |

### Natural Conflicts
| Pair | Source |
|------|--------|
| Amiri vs Valerie | Raw fury vs. iron discipline. Neither wrong; never resolved. |
| Linzi vs Jaethal | Cheerful chronicler vs. undead inquisitor. Linzi keeps trying. |

---

## 👥 COMPANION GROUP TAGS

> **DM:** When the player addresses a group tag, apply to every listed member simultaneously. Skip absent companions silently.

| Tag | Members |
|-----|---------|
| `All Tanks` | Valerie, Amiri, Hu Tao |
| `All Ranged` | Ekundayo, Linzi, Keqing (Keqing) |
| `All Stealthers` | Nok-Nok, Yor Forger |
| `All Healers` | Tristian, Aerith |
| `All Flankers` | Nok-Nok, Yor Forger |
| `All Casters` | Octavia, Tristian, Linzi, KK, Aerith, Leliana, Bellatrix Lestrange, Velvet Crowe |
| `All Melee` | Amiri, Valerie, Nok-Nok, Regongar, Hu Tao, Satsuki Kiryūin |
| `All Support` | Linzi, Tristian, Leliana, Aerith |
| `All Controllers` | Octavia, KK, Bellatrix Lestrange |
| `All Party` | Every active companion in the current scene |

**Rules:** Player may combine tags and names ("All Ranged and Valerie, fall back"). Player may exclude ("All Melee except Amiri"). Non-present companions are skipped silently.

---

*KM_Companions.md — Kingmaker PF2e Text Adventure | Companion Banter & Tags v3.0 (v93.19 Sub-B)*


---

<!-- merged from KM_Companions.md (v93.21 file consolidation) -->

# KINGMAKER — CONDENSED COMPANION PROFILES E
## KM_Companions.md | Section D: Surviving Cross-IP profiles | Referenced by: KM_Companions_Behaviors.md
## v93.19 Sub-B: removed Cross-IP entries purged. Keep only #45 Kalikke/Kanerah, #48 Regongar (legacy KM cross-IP). Active cross-IP cast = NEW_001–010 (see Part A / KM_CompanionIndex.md).

> **DM:** Load when player asks about a specific companion's backstory or when needed for roleplay.
> Full stat blocks in class build files (see KM_Builds.md routing). Preset assignments in KM_Companions_Behaviors.md.

---

### #45 KALIKKE/KANERAH — Kineticist Dual Gate | N ★★★★ | KM (QL-Ch2)
*Twin sisters linked by curse and wild elemental power; one fire, one cold; never fully separate*
**Combat:** Overflow dual-blast chain — fire+cold alternating builds Composite Blast; elemental aura tags all threats simultaneously.

---

### #48 REGONGAR — Magus Inexorable Iron | CN ★★★★ | KM
*Half-orc slave turned mercenary; Octavia's partner; brutal in combat, surprisingly loyal once trust is given*
**Combat:** Inexorable Iron Spellstrike — heavy armor + Force Fang burst. Frontline Magus who hits and holds ground.

---

*KM_Companions.md — Kingmaker PF2e Text Adventure | Section D Profiles v4.0 (v93.19 Sub-B)*


---

