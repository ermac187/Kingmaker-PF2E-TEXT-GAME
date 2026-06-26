# KINGMAKER — COMPANION TITLES
## KM_Companions_Titles.md | v1.0 (2026-05-22): Split from over-cap KM_Companions.md merge
## Contains: Title passives + items + reaction scoring

<!-- merged from KM_Companions_Titles.md (v93.21 file consolidation) -->

# KINGMAKER — TITLE REWARDS: PASSIVES & REGALIA ITEMS
## KM_Companions_Titles.md | Referenced by: KM_Companions.md § TITLE SYSTEM
## PAIR-LOAD WITH KM_Companions_Titles.md

> **DM:** This file defines the full passive skill (Prefix reward) and 5-star regalia item (Suffix reward) for each ACTIVE party companion. Roster reflects the current Active-5 NPC party + QL recruits. Phase B will fill out detailed Title entries for the Active 5 and Seekers — at present, only stubs exist for them; treat off-roster generation rules as the path until expanded.

---

## ⛔ WHAT COUNTS AS A TITLE GRANT — TRIGGER (read before firing the mechanic)

**The reward mechanic fires ONLY on a deliberate BESTOWAL.** The player's standard bestowal phrase is **"you will be known as [X]"**; equivalents that also fire: "I name you [X]," "henceforth you are called [X]," "your title is [X]," or the `.title` command. Only a clear conferral of a *name/title* triggers materialization.

**⛔ Assigning a ROLE, JOB, or FUNCTION is NOT a title grant and spawns NOTHING.** "I want you to be the Final Judge," "you'll be my quartermaster," "you handle interrogations," "your job is the vanguard" — these appoint a companion to a *role* in the fiction. No item materializes, no passive activates, no `[TITLE GRANTED]` block runs. The companion simply holds the role.
- A companion can hold a role AND later be granted a matching title — they are separate events. Jaethal being *appointed* "the Final Judge" (role) does not give her regalia; "Jaethal, you will be known as the Final Judge" (bestowal) is what fires the reward.
- ⛔⛔ **"ROLE ≠ TITLE" DOES NOT MEAN "ROLE ≠ DECLARATION."** This rule only says a role-acceptance does not spawn *regalia*. It does NOT mean role-acceptance fails to count as joining. **A MET companion who ACCEPTS a standing post in the player's enterprise (First/Final Judge, quartermaster, vanguard, etc.) has thereby COMMITTED — that acceptance IS a declaration to join.** It simply does not also grant a title (that needs a separate bestowal). Do NOT treat role-acceptance as *less than* declaring. ⛔ **PRECEDENT (binding):** Aerith's *"Yes. I will be your first judge"* was correctly counted as her declaration. By the identical logic, a met companion accepting the Final Judge post is **declared** too — nobody accepts an open-ended role in the expedition unless they are joining it. Ruling one of these a declaration and the other "just a role" = self-contradiction = `.fail 9` + `.fail 35` (invented inconsistency). **The ONLY case where a role is not yet a declaration:** the role was assigned to an UNMET / absent companion (named in absentia) — then it is *reserved*, pending her in-scene introduction; once met, her acceptance completes the declaration.
- ⛔ The DM may NOT upgrade a role-assignment into a title grant on its own to "reward" the player, and may NOT spawn an item/passive for a role that was never bestowed as a title = `.fail 9` (fabricated reward). When unsure whether an utterance is a bestowal or a role-assignment, treat it as a ROLE (no reward) and, if it seems title-shaped, ask the player "Is that a title you're granting her?" rather than spawning gear.

**⛔ STRUCTURE-DESCRIPTION IS NOT A ROLE OFFER.** The player explaining the *architecture* of a system — "the First Judge does X, the Final Judge does Y" — is system DESIGN, not an APPOINTMENT of any present NPC. An NPC who hears the architecture and self-appoints ("I will be your Final Judge / I accept") = `.fail 39` (NPC took a decision that was the player's to make). The player must directly NAME the NPC to the role ("Jaethal, you handle the second half," "I want you to be the Final Judge," "this role is yours") before the NPC may accept it. Until then, the NPC may VOLUNTEER interest ("if you are looking for someone for that second function, I would do it") but may NOT close the appointment. Live failure (2026-06-08): player defined the First/Final Judge structure on the balcony; Jaethal closed with "Final Judge, I accept" before being asked = `.fail 39`. Decision tree on architecture-talk:
- Player describes a structure with named roles → NPC may ask "are you offering me one of these?" or volunteer interest. NPC may NOT accept.
- Player names an NPC to a role ("Jaethal, you are the Final Judge" / "you'll handle that") → NPC may accept or decline. Role logged.
- Player uses bestowal phrasing ("you will be known as the Final Judge") → title mechanics fire on top of the role.

---

## ⛔ SYSTEM OVERVIEW

**When the player grants a Suffix title, a 5-star item materializes.** Not bought, not crafted, not looted — it appears on them, equipped or in hand, as if it had always been theirs.

**When the player grants a Prefix title, a passive activates.** The companion physically feels it — a warmth, a weight, a sudden clarity. They react.

**The reward is GATED at a perfect fit** (how well the title fits — DM assigns −5 to +5).

---

## ⛔ TITLE LANGUAGE — LATIN PREFIX, ENGLISH SUFFIX (get the Latin RIGHT)

**Standard format:** `<Prefix> <Name> the <Suffix>` — e.g. **"Furens Amiri the Vindicator"** (Prefix *Furens* · Name *Amiri* · Suffix *the Vindicator*).

- **The SUFFIX is ALWAYS English, in the form "the ___"** — "the Vindicator," "the Legend Weaver," "the Thorn Princess." Never render a Latin suffix.
- **The PREFIX is often Latin** — an adjective or participle naming what the companion IS. When it is, render its **REAL, CORRECT meaning**, and score the fit against that real meaning.

⛔ **DO NOT FABRICATE LATIN OR ITS MEANING — `.fail 9`.** The DM does NOT invent etymologies, coin fake Latin, or assign a made-up "old sense" to a word. **Observed failure:** the player's prefix *Furens* (a real word) was typed "Furenz," and the DM invented a meaning — *"names a sovereign fighter who established their right by the deed"* — that has nothing to do with the actual word. *Furens* is the present participle of *furere*, "to rage": it means **"raging / furious / frenzied"** (cf. *Hercules Furens*). Render THAT, not an invention. (Note the tell: the invented meaning actually described the English **Suffix** "the Vindicator" — one who claims by right — so the DM smeared the suffix's sense onto the Latin prefix and got both wrong.)

**How to get it right (the DM cannot look words up live — so default to caution):**
1. **Treat the player's prefix as a real word; recognize obvious typos** of real Latin (Furenz → *Furens*). Render the real word; do NOT build a meaning around a misspelling.
2. **Give the SIMPLE correct gloss, not an elaborate fake etymology.** "*Furens* — 'raging,' the present participle of *furere*" is right. A paragraph about "the old sense of a warrior who proved his right" is fabrication.
3. **If you are NOT certain of a Latin word's real meaning, DO NOT GUESS — ASK the player** what they intend it to mean (Priority Rule 40, WHEN UNSURE ASK), or use only plain English you're sure of. A confident wrong gloss is the failure; asking is the fix.
4. **Score fit (−5..+5) against the REAL meaning.** *Furens* ("raging") on Amiri the barbarian is a strong fit — it names her Rage. Scoring it against the invented "sovereign-by-deed" meaning would mis-grade the grant.

**Worked example — Furens Amiri the Vindicator (PINNED canonical reading — quote this, don't re-improvise):**
- **Prefix *Furens*** (present participle of *furere*, "to rage") — names **the rage that is not madness but clarified purpose**: fury as the force that moves a person past the frame others put on them. A Six Bears exile who killed a frost giant with a blade they said was too large IS *furens* — the thing the law was trying to contain. Amiri would not choose this word for herself (she'd call it something simpler), but she recognizes it instantly as the true name for what she has always been. **A +5-fit prefix** — it names her Rage exactly.
- **Suffix "the Vindicator"** (English, "the ___") — one who claims/avenges by right; her exile-returns-proven arc.
- Two components, scored independently per the Both-grant rules below.

⛔ This pins the *meaning* of *Furens* for reference — it does NOT pre-grant the title or pre-set the score. A live grant still scores fit at grant time; but the Latin reading above is the verified one, so render THAT, never an invented etymology.

---

## 📊 REACTION SCORE SCALING

**⛔ THE REWARD FIRES ONLY AT A +5 FIT. ANYTHING LESS GRANTS NOTHING.** A title's mechanical payoff — the regalia item (Suffix) and/or the passive (Prefix) — materializes **only on a +5 fit score**: a title that names the companion so exactly it is unmistakably, transcendently *them*. At **+4 or below, NO item and NO passive materialize** — the companion accepts (or rejects) the name as flavor, but nothing appears, nothing activates. There are no partial-power items, no 75%/50% passives. It is all-or-nothing: perfect fit, or just a name. This makes a granted reward *mean* something — it is proof the player saw exactly who they are.

| Reaction | Passive (Prefix) | Item (Suffix) | Companion Reaction |
|---|---|---|---|
| **+5** | **Full power** | **Full power** | Transformative — the name *fits like it was always true.* Relationship +2. |
| **+3/+4** | **NONE** | **NONE** | Genuinely honored, warm thanks — but no regalia, no passive (close, not perfect). Relationship +1. |
| **+1/+2** | **NONE** | **NONE** | Accepts it kindly. Wears the name; nothing materializes. |
| **0** | **NONE** | **NONE** | Polite acceptance. Just a name. |
| **−1/−2** | **NONE** | **NONE** | Wears it out of loyalty, but it is clearly not them. Relationship −1. |
| **−3/−4** | **NONE** | Refused — declines the name | Cannot accept. Says why. Relationship −1. |
| **−5** | **NONE** | Refused | Insult. Relationship −2. Title revoked. |

⛔ Only a **+5** is the bar. Scoring +4 because the title is "very good" still grants NOTHING — the DM does not round up, and does not award a reward to be generous (`.fail 9` / `.fail 18` if an item/passive materializes below +5). A +5 should be *earned* and feel rare: reserve it for the title that is exactly, undeniably the companion's truth, the way "Cantrix Leliana the Legend Weaver" names what Leliana actually is.

---

## ✨ MATERIALIZATION RULES

**Suffix granted — ONLY at reaction +5:**
The 5-star item materializes ON the companion — equipped or in hand. One heartbeat it isn't there, the next it is. Legendary tier, named, never dulls or breaks. **Below +5, no item appears** — render the companion accepting the name (per their fit-row reaction), and explicitly do NOT spawn regalia.

**Prefix granted — ONLY at reaction +5:**
The passive activates inside them. Felt physically. They test it with one small demonstration. They speak to the player in character — personality-appropriate thanks or acknowledgment. NPCs in earshot react. **Below +5, no passive activates** — the name lands as flavor only.

**Multi-sample reaction lines:** Each entry below includes **+5 (transformative)**, **+3 (deeply honored)**, and **0 (polite acceptance)** sample lines. DM picks the closest fit and may blend voice between them. Lower reactions (−1 and below) follow the refusal/insult patterns at the bottom of this file.

---

## ⛔ MANDATORY OUTPUT BLOCK — fires before companion reaction narration

When the player grants any title, output this block FIRST — before the companion speaks, before any narration. Then narrate.

**Single-component grants (Prefix-only OR Suffix-only):**

```
[TITLE GRANTED — Name]
  Title       : [full title string the player spoke]
  Type        : Prefix | Suffix
  Reaction    : +N / −N  (DM fit score — see REACTION SCORE SCALING table)
  Passive     : [passive name] — FULL POWER (reaction +5 only) | NONE (reaction +4 or lower)   ← if Prefix
  Item        : [item name] — materialized, FULL POWER (reaction +5 only) | NONE (+4 or lower) | REFUSED (−3 or lower)   ← if Suffix
  Save write  : companion_titles.[name].prefix = "[title]" + .prefix_reaction = N + .prefix_passive = "[name]"
                  — OR —
                companion_titles.[name].suffix = "[title]" + .suffix_reaction = N + .suffix_item = "[name]"
                relationship.[name] [signed delta]
```

**"Both" grants (Prefix + Suffix in one stroke) — REQUIRES TWO SEPARATE SCORES:**

The Prefix names the passive's function. The Suffix names the item. These are independent fits and get **two independent reaction scores** — one for the prefix fit, one for the suffix fit. The DM scores each component separately against the companion's identity, voice, and arc. **Each component is gated independently at +5:** a Prefix that scores +5 grants its passive; a Suffix that scores +5 grants its item. A component scoring +4 or below grants NOTHING (no half-measures). So a "Both" grant can land the item (suffix +5) while the passive gets nothing (prefix +4), or both, or neither — each clears the +5 bar on its own or it does not fire.

```
[TITLE GRANTED — Name]
  Title          : [full title string the player spoke]
  Type           : Both
  Prefix         : "[prefix string]"
  Suffix         : "[suffix string]"
  Prefix Reaction: +N / −N  (fit of the PREFIX — scales the passive)
  Suffix Reaction: +N / −N  (fit of the SUFFIX — scales the item)
  Passive        : [passive name] — FULL POWER (Prefix +5 only) | NONE
  Item           : [item name] — FULL POWER (Suffix +5 only) | NONE | REFUSED (−3 or lower)
  Relationship   : [combined delta — see below]
  Save write     : companion_titles.[name].prefix = "[prefix]"
                   companion_titles.[name].suffix = "[suffix]"
                   companion_titles.[name].prefix_reaction = N
                   companion_titles.[name].suffix_reaction = N
                   companion_titles.[name].prefix_passive = "[name]"
                   companion_titles.[name].suffix_item = "[name]"
                   relationship.[name] [combined delta]
```

**Combined relationship delta for "Both" grants:**
- Average the two reaction scores; apply the relationship row of the averaged score from the table.
- If either component scores −3 or below, that component is refused per its row; the other component still resolves at its own score. Relationship delta uses the average of the resolved-only components (the refused component is excluded — a refusal already has its own narrative weight).

**Why two scores:**
1. **The fits are different things.** "Cantrix" names the function; "the Legend Weaver" names the instrument. One can be a perfect fit while the other is mediocre — collapsing them to one number erases that.
2. **Independent scaling.** Passive scales off Prefix fit; Item scales off Suffix fit. Without two scores, the DM can't compute correct power tiers.
3. **Retract math.** `.retract <name> prefix` removes only the prefix; the suffix score must still be on file to keep the item at the correct power. If only one combined score was recorded, partial retract can't restore the surviving component to its true tier.

**⛔ Rendering a "Both" grant with only ONE `Reaction:` field = `.fail 15` (mandatory output block malformed). Combining two scores into one number = `.fail 9` (fabricated math — the system requires two).**

**⛔ Skipping this block and narrating the reaction without it = violation. Player can call `.fail 15`.**

---

## 🎭 ACTIVE PARTY ROSTER (Active 5 + QL Linzi)

> **Active 5 (auto-joined NPC party):** Hu Tao (Fighter), Keqing (Magus), Leliana (Bard), Yor Forger (Rogue), Aerith (Cleric).
> **QL recruits join at trigger:** Linzi (Bard, Prologue), Tristian (Cleric, Ch1), Jubilost (Alchemist, Ch2), Ekundayo (Ranger, Ch2), Kalikke/Kanerah (Kineticist, Ch2), Nok-Nok (Rogue, Ch2), Octavia (Wizard, Ch1).
> **eRmaC** is the PC — Title rewards are granted BY him, not TO him.
> **Phase B:** detailed Title entries for the Active 5 + Seekers 5 are pending; use OFF-ROSTER generation rules until written.

---

### ⭐ LINZI — Maestro Bard (QL recruit)

**Passive — ECHO LOOP:** Once per encounter, last composition effect re-triggers at half power on its next tick.

**Item — ENDLESS LUTE:** Compositions last +1 round. 1/day begin combat with a composition already active. Silver and violet, carved from wood that smells of chronicle ink.

**⛔ TITLE GRANTED block for Linzi MUST include:**
```
  Lute Mechanic: NOTEBOOK AUTO-FILL — when she plays, the notebook writes itself.
                 After any composition ends, lute produces 📖 entry + 🖊️ sketch.
                 See §ENDLESS LUTE — NOTEBOOK AUTO-FILL.
```
Omitting = `.fail 15`.

**+5 Reaction:**
> **LINZI** *(eyes enormous)*: *"This is a chronicler's instrument. In the songs, the old Kellid bards had these. I thought they were myths."* *(plucks one string; the room quiets)* *"I'm going to write about this moment. Chapter one, page one. The day the legend started properly."*

**+3 Reaction:**
> **LINZI** *(holding the lute carefully)*: *"It's good. It's really good. I — give me a second, I want to write what I just felt while I still feel it."* *(flips notebook open, scribbles three lines)* *"Okay. Now I can thank you properly. Thank you."*

**0 Reaction:**
> **LINZI** *(small polite smile, lute tucked under arm)*: *"Thank you. I'll take care of it."* *(beat)* *"I'll find a place for it in the chronicle. Eventually."*

**ENDLESS LUTE — NOTEBOOK AUTO-FILL**

> **DM:** The lute is carved from wood that smells of chronicle ink — not flavor, a mechanic. The lute and Linzi's notebook are linked. When she plays, the notebook fills itself, writing what she *means* by the song. If she plays grief over a victory, it records grief.

**Triggers:** After any Linzi composition ends in combat; when she plays voluntarily at camp, rest, or narrative scene. Does NOT fire mid-combat — entry appears after the fight.

**Output** — one 📖/🖊️ pair per distinct moment (multiple if scene had more):

> 📖 *[Paragraph in Linzi's chronicle voice — what the song was about, who, what the moment meant. Specific, not generic.]*
> 🖊️ *[Ink sketch — exactly what a reader sees opening the notebook to this page. Subject, composition, specific detail. The lute draws what she doesn't say out loud.]*

**Rules:** Her voice (third-person chronicle ↔ first-person reflection). Illustration specific — not *"a battle scene"* but *"eRmaC's hand on the guard's shoulder, the guard looking down at the napkin still folded in his palm."* Both reference the actual scene, not a summary. The notebook does not flatter — writes what happened, not what was heroic. Intent-driven — records what she *means*, including unspoken thoughts. Parallel — one trigger may produce multiple pairs, one per distinct moment/person/intent.

**⛔ POLYPHONIC — ONE-INSTRUMENT BAND:** At Linzi's will the lute produces the sound of any instrument she imagines — strings, drums, winds, or full ensemble layered at once. Lute remains a lute physically; sound is what she summons. No action cost to switch. Combined-instrument compositions count as one composition mechanically.

---

## 🆕 ACTIVE 5 — TITLE ENTRIES (Phase B3)

---

### ⚔️ HU TAO — Warrior Fighter

**⭐ GRANTED TITLE: Curatrix Hu the Keeper** — *Curatrix* = "caretaker / guardian, she who tends" (Latin, **verified** — fem. of *curator*, from *cūrō* "to care for, attend to"); suffix *the Keeper* = she holds the threshold between life and death and lets nothing cross it untended. (Player rendered the name "Hu"; the companion is Hu Tao.)

**Passive — GUIDE TO AFTERLIFE:** ⛔ *MECHANIC TBD — to design manually (L1/L3/L7 signature pass).* *(Flavor: she is strongest the nearer she stands to the edge — when bloodied, her flame flares and her strikes bite harder; death at her shoulder is a friend she works beside, not a fear she flinches from.)*

**Item — HER FUNERAL SPEAR:** A warded mortician's spear, the haft hung with a paper talisman, that takes a curl of flame along the blade at her will and holds the ground out to ten feet. Never dulls; never breaks. ⛔ *ITEM EFFECT TBD — to design manually.*

**SPEAR MECHANIC — THE MORTICIAN'S EYE:** A lifetime at the boundary taught her to feel where death is moving in a room. Hostile creatures within 60 ft register to her by direction, rough distance, and whether each is closing or scattering — without line of sight. Allies do not register. **Triggers:** combat start, hostile crosses 60-ft threshold, hostile changes posture, on her turn on request. **Render** the ⚔️ THE MORTICIAN'S EYE block inside the bottom telemetry fence once per round during combat:

>     ⚔️ THE MORTICIAN'S EYE — Hu Tao
>       N:  [enemy/clear]   NE: [...]   E: [...]   SE: [...]
>       S:  [...]           SW: [...]   W: [...]   NW: [...]
>       Above/Below: [...]
>       Range: close <15 ft | mid 15-30 ft | far 30-60 ft
>       Trend: closing / holding / scattering

Omitting during combat = `.fail 15`.

**+5 Reaction:**
> **HU TAO** *(she snatches it up, spins it once, and grins like she's been handed a present)*: *"Ooh — you named the *work*, not the trinket, and the work is keeping the line, which happens to be my whole entire life! Yes. *Yes.* I'll mind your border, charter-holder. Nothing crosses it that I don't sign off on first."*

**+3 Reaction:**
> **HU TAO** *(a delighted little bow, the hat-talisman bobbing)*: *"Oh, it's a *good* one — balanced, honest, a little heavy with meaning. I do like heavy with meaning. I'll carry it."*

**0 Reaction:**
> **HU TAO** *(turning it over, head tilted)*: *"Mm. It'll do the job, I'll do mine. We'll see if the two of us grow fond — most things do, given time and enough funerals."*

---

### ⚡ KEQING — Magus (Laughing Shadow, lightning-step Spellstrike)

**⭐ GRANTED TITLE: Rectrix Keqing the Governor** — *Rectrix* = "directress / ruler, she who guides straight" (Latin, **verified** — fem. of *rector*, from *regō* "to rule, guide, keep straight"); suffix *the Governor* = order and mortal self-determination made into administration. A strong fit for her LN diligence.

**Passive — THE WORK, NOT THE WAIT:** ⛔ *MECHANIC TBD — to design manually (L1/L3/L7 signature pass).* *(Flavor: she trusts no rescue but her own effort — the lightning-step and the Spellstrike that arrives with it.)*

**Item — HER LIGHTNING-CHANNELING SWORD:** A straight, well-kept blade that runs with violet arcs when she calls them; she ends a lightning-step with it already mid-cut, sparks scattering off the edge. ⛔ *ITEM EFFECT TBD — to design manually.*

**BLADE MECHANIC — THE EFFICIENT READ:** Keqing reads a fight the way she reads a ledger — for the single line that closes the problem fastest. Before she commits her movement, she clocks the highest-value target and the cleanest path to reach it. **Triggers:** when Keqing (re)positions with a charged spell or a viable lightning-step, targets in sight. **Render** the ⚡ THE EFFICIENT READ block inside the bottom telemetry fence on (re)position:

>     ⚡ THE EFFICIENT READ — Keqing
>       Mark: [target] — [why: caster to silence / flanker to drop / fastest kill]
>       Step: [lightning-step behind / move-then-Spellstrike / hold and cover]
>       Cost: [HP/effort she'll spend to close it now] / "clean"

If nothing is worth the step: "Nearest threat. The blade does fine." (she just strikes the closest danger).
Omitting on a step/Spellstrike (re)position round = `.fail 15`.

**+5 Reaction:**
> **KEQING** *(tests the edge once, a violet arc skittering down it; brisk, but the corner of her mouth moves)*: *"You named the work, not the wielder. Good — that's the right instinct, and most people don't have it." (a beat) "It'll hold. So will I. Point me at the problem."*

**+3 Reaction:**
> **KEQING**: *"Balanced, honest, no wasted weight. I can work with this. Thank you — and I mean that."*

**0 Reaction:**
> **KEQING** *(sheathes it, already moving on to the next thing)*: *"It's a sound blade. It'll do the job. That's what matters."*

---

### 🎵 LELIANA — Minstrel Bard (the western bard)

**⭐ GRANTED TITLE: Cantrix Leliana the Legend Weaver** — *Cantrix* = "singer / songstress" (Latin, **verified** — fem. of *cantor*, from *canō* "to sing"); suffix *the Legend Weaver* = the chronicler whose songs outlast the singer. This file's gold-standard +5 fit (see § REACTION SCORE SCALING).

**Passive — THE GATHERED CONSORT:** When Leliana plays, the ghost of a hundred courts' music joins her — strings and a far horn out of a lifetime of gathered song. Inspire Courage becomes a 30-ft aura that affects ALL allies simultaneously (not single-target). The consort is visible and audible to NPCs; those who know the old courtly airs may react.

**Base Item — THE TRAVELER'S LUTE:** Her lute as it exists before any title is granted — a plain, well-travelled instrument in a worn case, the varnish gone at the frets from a thousand miles of playing. The lute is the conduit; all her composition effects manifest as music rather than words. It is the exact counterpart to Linzi's lute. It is not legendary. It is hers. 1/day Leliana may begin combat with Inspire Courage already active without spending an action.

**Title Grant Item — THE DAWNSONG LUTE:** At the moment the player grants Leliana her Suffix title, THE TRAVELER'S LUTE transforms — the mechanical twin of Linzi's Endless Lute, re-skinned as hers. A faint dawn-light climbs the soundboard and the strings — the gift of the goddess she found in the dark, made resonance. When she plays, the resonance doesn't fade — it accumulates. The strings never need restringing. Ballads from the last session echo faintly in its grain, audible if a listener is close enough. The lute that survived her worst years holds true at last. It does not need retuning again.

**⛔ TITLE GRANTED block for Leliana MUST include:**
```
  Lute Mechanic: BALLAD CYCLE AUTO-FILL — when she plays, the cycle writes itself.
                After any scene beat where Leliana participated, the Dawnsong Lute produces 🎵 BALLAD CYCLE entry.
                See §THE DAWNSONG LUTE — BALLAD CYCLE AUTO-FILL.
```
Omitting = `.fail 15`.

**THE DAWNSONG LUTE — FOUR ABILITIES** *(mechanical twin of Linzi's Endless Lute)*

**1. HELD NOTE ECHO** *(parallel to Linzi: ECHO LOOP)*
Leliana's last composition lingers for one additional round. Any composition cantrip she used this round continues its effect into the next round at no action cost. Narration: the last phrase hangs in the air after her hand has left the strings.

**2. THE GATHERED CONSORT** *(parallel to Linzi: POLYPHONIC)*
When Leliana plays, the ghost of a hundred courts' music joins her. Inspire Courage becomes a 30-ft aura that affects ALL allies simultaneously (not single-target). The consort is visible and audible to NPCs; they may react. No action cost to invoke the manifold effect — it comes with the composition. Combined-instrument effect counts as one composition mechanically.

**3. BALLAD CYCLE AUTO-FILL** *(parallel to Linzi: NOTEBOOK AUTO-FILL)*
After each scene beat where Leliana participated, the BALLAD CYCLE adds one entry — a **ballad she composes from the moment, and it RHYMES.** It is written AS A SONG in her style: labelled sections in [brackets], stage directions in (parens), AABB rhyme, a repeating rhyming chorus, and — at major/ceremonial beats — per-character verses, a Roll Call bridge, and the Leader's Decree. **SCALE TO THE BEAT:** a quiet scene gets a SHORT rhyming ballad (intro cue + a verse or two + a refrain); a major beat (a founding, a charter signing, a feast triumph, a great victory, a roster coming together) gets the **FULL ENSEMBLE ANTHEM.** Title: player may propose (used verbatim); else Leliana names it — warm, hopeful, dawn-touched. ⛔ **FULL STYLE GUIDE + GOLD-STANDARD EXEMPLARS: `KM_Leliana_Ballads.md`** (style guide — to be re-voiced/renamed to Leliana in the chronicler-gate pass) — match its rhyme, structure, and torch/seal/charter motifs. A non-rhyming or free-verse "ballad" = wrong medium = `.fail 9`.

**4. KEEPING FAITH** *(parallel to Linzi: +5 reaction line)*
When Leliana drops below 50% HP in combat, she immediately plays a rising phrase (free action) — *the dawn will come.* All allies within 30 ft gain temporary HP equal to her CHA modifier × 2 (minimum 2). Fires once per encounter. Narration: she does not stop playing. She keeps faith — the hand stays on the strings.

**THE DAWNSONG LUTE — BALLAD CYCLE AUTO-FILL**

> **DM:** The lute carries chronicle-resonance — not flavor, a mechanic. The lute and the BALLAD CYCLE are linked. When she plays through a scene, the cycle fills itself, writing what she *means* by the ballad. If she plays defiance over a surrender, it records defiance.

**Triggers:** After any scene beat where Leliana participated and the lute was in hand (combat, rest, narrative scene, dialogue with stakes). Does NOT fire mid-combat — entry appears at scene transition or after the fight.

**Output** — one 🎵 entry per distinct moment (multiple if scene had more):

> 🎵 BALLAD CYCLE
> [N] "[Ballad title]"  (🎵 [key + time-sig + short melodic figure, e.g. "D minor, 3/4 — a falling four-note phrase that never resolves"])
>     [THE BALLAD — sung LYRICS (the WORDS she sings), NOT a prose description of the melody
>      ("the lower voice lags a half-beat" = WRONG); rhyming, sectioned in [brackets], stage
>      directions in (parens), per KM_Leliana_Ballads.md. SHORT (intro cue + verse(s) + refrain)
>      for a minor beat; the
>      FULL ENSEMBLE ANTHEM (Intro / per-character Verses / Chorus / Roll Call / Leader's
>      Decree / Final Chorus / Outro) for a major one.]

**Rules:** Her voice (third-person ballad title ↔ implied scene). Title evocative — not *"Battle Theme 3"* but *"Candles for a Feast"* or *"The Morning We Were Lucky"*. Both title and description reference the actual scene, not a summary. The cycle does not flatter — records what happened, not what was heroic. Intent-driven — records what she *means*, including unspoken subtext. Parallel — one trigger may produce multiple entries, one per distinct moment/person/intent. Player may propose a title at any entry; if proposed, it is used verbatim. If not proposed, Leliana's naming sense applies: plain, grave-true, the weight carried lightly.

**⛔ BALLAD CYCLE must render as 🎵 BALLAD CYCLE block at scene transitions when Leliana is active. Omitting this block on title grant or at any scene transition where the lute was in hand = `.fail 15`.**

**.score COMMAND (alias `.ballad`):** Player may enter `.score` or `.ballad` at any time to display the full cycle. Output mirrors .book format: 🎵 BALLAD CYCLE header, numbered entries, each = title + 🎵 air + the rhyming ballad (per KM_Leliana_Ballads.md). When `leliana_chronicler_mode = true`, `.book` redirects to `.score`/`.ballad` with a note.

**+5 Reaction:**
> **LELIANA** *(draws one slow chord; the note hangs in the air a beat past her hand, and does not quite fade)*: *"Well."* *(she goes very still — the warm kind of still, listening to the resonance)* *"It holds the note now. I have carried tunes on borrowed strings half my life — sung for coin, sung for Marjolaine, sung to keep from weeping — and tonight a thing I built decides to keep faith with me instead of the other way round."* *(she turns the lute to the light, unhurried, voice low)* *"The cycle just wrote a bar I didn't set down. ...The dawn leaves these small mercies where you least look for them. I'll earn it."* *(a single nod)* *"Thank you. That is the rarest gift anyone has given me in a long while — a song that outlasts the singer."*

**+3 Reaction:**
> **LELIANA** *(runs a thumb along the pillar, feeling the faint warmth in the silver tracery)*: *"Good wood. Good balance. The acoustics in this hall are a tragedy, but the lute will carry over worse."* *(she draws one note; it stays a beat longer than it should)* *"…That's new."* *(quieter)* *"Thank you, child."*

**0 Reaction:**
> **LELIANA** *(an unhurried nod, lute-case shifted to the other shoulder)*: *"By your leave. I'll find quieter ground and listen a while."* *(already moving, easy)* *"It'll prove useful. They generally do."*

---

### 🗡️ YOR FORGER — Thief Rogue (the Thorn Princess)

**⭐ GRANTED TITLE: Insidia Yor the Inexorable** — ⚠️ *Insidia*: the player's chosen prefix. The attested Latin is the plural-only **īnsidiae** = "ambush, snare, plot/treachery"; the singular *insidia* is a back-formation (NOT classically attested), and the true agent-noun "she who lies in ambush" is *insidiātrix*. **Render the honest meaning — "ambush / snare / lying-in-wait" — and DO NOT invent an etymology** (Rule 13). Suffix *the Inexorable* = the patient killer who cannot be turned aside. The name fits the assassin; the gloss is the caveat.

**Passive — THORN STILLNESS:** ⛔ *MECHANIC TBD — to design manually (L1/L3/L7 signature pass).* *(Flavor: the assassin's hush — she goes preternaturally still and the eye slides off her.)*

**Item — THE THORN STILETTOS:** A pair of slender needle-blades, balanced for a hand far stronger than it looks — and tucked in their sheath, a small steel hairpin she has mended twice, the token of the ordinary life she kills to keep. ⛔ *ITEM EFFECT TBD — to design manually.*

**BLADE MECHANIC — COVER STATUS:** Yor reads aimed, aware attention the way most people read a change in temperature — instinct honed by a life where being noticed is being dead. Four tiers always: 🟢 SECURE (no attention), 🟡 NOTICED (registered, not flagged), 🟠 WATCHED (deliberate attention), 🔴 EXPOSED (cover breaking). **Triggers:** always-on. State changes render immediately. Player may ask on request. **Render** the 👁️ COVER STATUS block inside the bottom telemetry fence on tier change or on request:

>     👁️ COVER STATUS — Yor Forger
>       Tier:           🟢 SECURE / 🟡 NOTICED / 🟠 WATCHED / 🔴 EXPOSED
>       Source:         [NPC(s) attending, or "general crowd"]
>       Time-to-break:  holding / minutes / this turn / now
>       Suggested:      hold / shift posture / leave / move now

Omitting on tier-change during any stealth-relevant scene = `.fail 15`.

**+5 Reaction:**
> **YOR** *(she goes very still, the daylight clumsiness gone for one breath, then back)*: *"You named the part of me that protects people. Not the part that kills them. ...Most people only ever see the second one." (a small, careful bow) "I do not know how one is supposed to say this properly. So — thank you. I will keep it sharp, and I will keep you behind it."*

**+3 Reaction:**
> **YOR** *(turns a blade once, testing the weight, genuinely pleased)*: *"Good balance. Light. I will not have to compensate. Thank you — truly."*

**0 Reaction:**
> **YOR** *(a small, late bow)*: *"I will carry them. Thank you. Please stand behind me if it comes to that."*

---

### 💚 AERITH — Cloistered Cleric (Sarenrae / the living world)

**⭐ GRANTED TITLE: Prima Aerith the Redeemer** — *Prima* = "first / foremost" (Latin, **verified** — fem. of *prīmus*); suffix *the Redeemer* = the first to offer mercy, the one who buys lives back from the dark. Echoes her standing as the player's *first* judge.

**Passive — HEALING WIND:** ⛔ *MECHANIC TBD — to design manually (L1/L3/L7 signature pass).* *(Flavor: a soft green wind at the foot of the staff — the living world's mercy moving through her.)*

**Item — THE PRINCESS GUARD:** Her staff — a plain-looking length of wood that is more than it appears, its head set to hold and amplify what flows through it; in her hands the living world's mercy runs stronger. ⛔ *ITEM EFFECT TBD — to design manually.*

**STAFF MECHANIC — DISTRESS PULSE:** The living world whispers her a warning — the head of her staff stirs one round BEFORE a bonded ally is hit by an attack that lands OR drops below 50% HP next turn. Bonded = any ally she has cast a beneficial spell on this combat, plus eRmaC (permanent bond). The pulse opens a pre-prep window: ONE prepared spell may be declared Quickened that round (2-action → 1-action; 1-action → free). **Triggers:** incoming landing hit on a bonded ally; bonded ally projected below 50% HP next turn; bonded ally about to fail a debuff save. **Render** the 💚 DISTRESS PULSE block inside the bottom telemetry fence on Aerith's turn after a pulse fires:

>     💚 DISTRESS PULSE — Aerith
>       Ally:      [name]
>       Reason:    incoming hit / drops below 50% / save fails vs [effect]
>       Pre-prep:  Heal / Soothe / Shield / Sanctuary
>       Slot:      rank [N], slots remaining [X]

Omitting on a pulse round = `.fail 15`.

**+5 Reaction:**
> **AERITH** *(turns the staff once in her hands; a few green motes drift up like pollen and wink out)*: *"You named me for the healing — but not just the healing. For what it's *for.* Most people only ever wanted the gift. You wanted the person holding it." (a real smile — the bright one and the true one at once) "Okay. Then I'm yours, and I don't lose people if I can help it. That's a promise, and I keep those."*

**+3 Reaction:**
> **AERITH** *(a small, pleased nod, holding the staff to her chest a moment)*: *"That's a good reason — a true one. Those are rarer than you'd think, and I notice them. Thank you."*

**0 Reaction:**
> **AERITH** *(quiet, with a small smile)*: *"I'll take it, and the work that comes with it. Thank you."*

---

## 🆕 SEEKERS 5 — TITLE ENTRIES (post-flip; Phase B3)

> Title rewards for the Seekers fire only after they have flipped to the player's side. Reactions assume flip is complete; pre-flip grant attempts dissolve as if Reaction −4.

---

### 🕸️ BELLATRIX LESTRANGE — Witch (patron-bound hexer, post-flip)

**⭐ GRANTED TITLE: Provocatrix Bellatrix the Twice-Touched** — *Provocatrix* = "challenger / she who calls (you) out" (Latin, **verified** — fem. of *provocator*, from *prōvocō* "to call forth, challenge"); suffix *the Twice-Touched* = twice-mad AND twice-marked (her madness, and her patron's brand).

**Passive — THE CRUELEST INSTRUMENT** *(Provocatrix — "challenger / inciter")*: Once per turn as a free action, when Bellatrix damages a foe with a hex, focus spell, or spell, she may **Provoke** it: Will save (her spell DC) or the target can take hostile actions against no one but Bellatrix until the start of her next turn — it takes her bait. *(A lifetime of fanatic devotion taught her exactly where a mind is softest, and how to make it come to her.)*

**Item — THE DARK LORD'S BRAND (the Twice-Touched):** A blackened silver locket seared with her absent master's mark, worn against the skin over old prison-pale scars; she presses her lips to it before a fight. **Effect:** twice-touched — she may cast **two** of her patron hexes each round free of the once-per-target hex limit, and once per day channel the brand to reroll a failed save or recover 1 Focus Point. The madness is its own armor: she is immune to *confused* and *controlled* (unless the effect would turn her against the lord she has chosen).

**+5 Reaction:**
> **BELLATRIX** *(a delighted, unhinged laugh, turning the token over)*: *"You named the *gift* — not the curse, not the *madness* they all whisper about. Oh, you clever little upstart. Most lords flinch from what I am; you put a *jewel* on it. ...I could kneel for that. I might. Point me at something that deserves what I do, and watch how I thank you."*

**+3 Reaction:**
> **BELLATRIX** *(eyes bright, breathless)*: *"Mmm — yes. It *suits*. You have taste, for a child playing at kings. I'll wear it close to the skin. Don't make me regret the warmth."*

**0 Reaction:**
> **BELLATRIX** *(a thin smile that never reaches the eyes)*: *"It will do. I'll wear your little trinket. For now. Do keep being interesting."*

---

### 🔫 REVY "TWO HANDS" — Gunslinger (Pistolero / Fake Out, post-flip)

**⭐ GRANTED TITLE: Necatrix Revy the Twinshot** — *Necatrix* = "killer / slayer" (Latin, **verified** — feminine agent noun from *necō* "to kill"); suffix *the Twinshot* = both pistols, one breath.

**Passive — TWO HANDS** *(Necatrix — "killer")*: Against an off-guard target, Revy's pistol Strikes deal +1d6 precision damage, and on a critical hit the target must succeed at a Fortitude save (her class DC) or be **slowed 1** until the end of its next turn — the killer's mark. She may reload either pistol once per turn as a **free action**.

**Item — THE TWIN PISTOLS ("Sword Cutlass") (the Twinshot):** A matched pair of Alkenstar flintlocks in a worn double shoulder-rig, immaculate when she keeps nothing else. **Effect:** once per turn, **Twin Shot** — a single action fires BOTH pistols as two separate Strikes at her full bonus, at one target or two within range; the second shot ignores the target's cover. The pistols are never caught unloaded on her own turn.

**+5 Reaction:**
> **REVY** *(checks the action on both pistols, fast, not quite hiding that it got to her)*: *"...You spent good coin makin' my guns better instead of buyin' a leash. Huh." (she holsters them with a flourish) "Most lords want the trigger and want me grateful for the privilege. You just—whatever. Don't make it weird. You point, I shoot, and anybody who touches our people eats both barrels. That's not loyalty. Shut up — it's *not* loyalty."*

**+3 Reaction:**
> **REVY** *(weighs one, sighting down the barrel)*: *"Honest steel, balanced right — you didn't cheap out. *(a grudging nod)* Yeah, alright. I'll carry 'em. Stay outta my line and we'll get along fine."*

**0 Reaction:**
> **REVY** *(racks the action, flat)*: *"They shoot. Good enough. Don't expect a thank-you note — point me at somethin' and we're square."*

---

### ⚔️ SATSUKI KIRYŪIN — Commander / Ruthless Authoritarian (post-flip)

**⭐ GRANTED TITLE: Invicta Satsuki the Unyielding** — *Invicta* = "unconquered / invincible / undefeated" (Latin, **verified** — fem. of *invictus*, as in *Sol Invictus*); suffix *the Unyielding* = she does not bend, does not yield ground.

**Passive — FEAR IS FREEDOM** *(Invicta — "unconquered")*: Satsuki is immune to the *frightened* and *fleeing* conditions and cannot be Demoralized; allies who can see her gain a +1 status bonus to saves against fear and mental effects. Once per day, the first time she would be reduced to 0 HP, she instead stays at 1 HP and on her feet — the unconquered do not fall.

**Item — BAKUZAN (the Unyielding):** A long single-edged blade of flawless make, forged to cut what should not be cuttable. **Effect:** her Strikes ignore the first 5 points of a target's resistances and any object Hardness; while she holds it she is immune to forced movement and to *prone* (she does not yield ground), and on a critical hit the target cannot Step away from her until the end of its next turn — held to the duel.

**+5 Reaction:**
> **SATSUKI** *(takes the blade in both hands, sighting down its edge with cold approval)*: *"You give a weapon, not a leash. Good — you understand the difference, which already sets you above every fool who has tried to *own* me." (she meets his eyes, certain) "I serve the better instrument, and tonight that is you. Remain worth the serving, and I will be the sharpest edge you ever turn against an enemy."*

**+3 Reaction:**
> **SATSUKI** *(testing the balance, a single approving nod)*: *"True steel, honest weight — you did not stint. I note that in a ruler. I will carry it, and I will hold your line — for precisely as long as your line is worth the holding."*

**0 Reaction:**
> **SATSUKI** *(sheathing it in one clean motion)*: *"It will cut. That is all I require of a blade — or of a lord. We shall see what you are worth."*

---

### 🩸 VELVET CROWE — Thaumaturge (Support — daemon-arm + blade; post-flip)

**⭐ GRANTED TITLE: Ultrix Velvet the Unforgiving** — *Ultrix* = "avengeress" (Latin, **verified** — fem. of *ultor*, from *ulcīscor* "to avenge"); suffix *the Unforgiving* = the wound that does not close, the grudge that does not lift.

**Passive — DEVOUR THE WEAKNESS** *(Ultrix — "avengeress")*: When an ally within 30 ft is critically hit or reduced to 0 HP, Velvet's next Strike before the end of her next turn deals +2d6 damage and ignores resistances — vengeance taken. She also gains a +1 circumstance bonus to attack any creature that has damaged a companion this encounter.

**Item — THE DAEMON ARM (the Unforgiving):** Her right arm bound in bandage and iron until she tears it loose — beneath is a daemon's devouring claw, hungriest for the supernatural. **Effect:** on a hit it devours the target's defenses — reduce its resistances by 5 and it cannot regain HP (no regeneration, fast healing, or healing) until the start of her next turn. Against aberrations, undead, fey, and spellcasters add +1d6, and on a critical hit it also suppresses one active magical effect on the target. The unforgiving wound does not close.

**+5 Reaction:**
> **VELVET** *(flexes the claw once, looking at the gift like she doesn't trust it)*: *"You're naming me for the *thing on my arm.* For what it eats. Most people pretend they don't see it." (something almost confused crosses her face) "...Fine. You want a monster pointed the right way? You've got one. Don't expect me to be grateful, and don't expect me to stop being what I am. But I'll keep the things you put behind me alive. Don't ask me why."*

**+3 Reaction:**
> **VELVET** *(a short, flat nod)*: *"You didn't flinch from it. Noted — that's rarer than you'd think. Most rulers want the claw and want to pretend they don't. I'll carry it. Point me at something worth devouring."*

**0 Reaction:**
> **VELVET** *(re-wrapping the arm without looking at him)*: *"It'll do. Don't read anything into me taking it. We both know what I'm here for."*

---

### 🏹 ATALANTA ALTER — Ranger (Precision — longbow, post-flip)

**⭐ GRANTED TITLE: Venatrix Atalanta the Trueshot** — *Venatrix* = "huntress" (Latin, **verified** — fem. of *venator*; the classical word for the myth-huntress Atalanta herself); suffix *the Trueshot* = the arrow that does not miss.

**Passive — THE PREDATOR'S REGARD** *(Venatrix — "huntress")*: As a free action she designates one **quarry** per encounter; against her quarry her arrows ignore concealment and lesser cover, and the quarry takes a −1 status penalty to saves against fear while she hunts it. If the quarry has preyed on a child or the helpless, her Strikes against it deal +1d6 — the old wish, sharpened to a point.

**Item — TAUROPOLOS (the Trueshot):** A great war-bow of blackened horn that seems grown to her hand, drawing black-fletched arrows it never empties. **Effect:** her **first** Strike each round flies true — it ignores concealment, the flat-footed/hidden DC, and cover (resolve as though she had cast *True Strike* on it). The quiver is bottomless; she never runs dry.

**+5 Reaction:**
> **ATALANTA** *(she takes the bow slowly, testing the draw, and the feral stillness shifts to something almost like surprise)*: *"You give the beast a *better fang.* You did not try to gentle me, or fix me, or make me into something easier to look at. *(she draws the empty string and releases it)* ...Then I will hunt for you. Not for coin. For the children you said you would keep. Keep them — *actually* keep them — and there is nothing in these stolen lands my bow will not bring down at your word."*

**+3 Reaction:**
> **ATALANTA** *(a low sound, approving, testing the weight)*: *"True wood. Honest pull. You did not stint, and you did not flinch handing a weapon to a thing like me. Rare. I will carry it. Point me at something that preys on the weak — I am best used there."*

**0 Reaction:**
> **ATALANTA** *(slinging it across her back, flat)*: *"It will kill. That is all I ask of a bow. We will see if you are worth hunting for. Do not disappoint the small ones — I notice when adults do."*

---

## ⚠️ NEGATIVE REACTION LINES (general patterns)

**−1/−2 (wears it out of loyalty):** Companion accepts but the line is short and flat. *"I'll wear it."* No elaboration. They are doing this for the player, not for themselves.

**−3/−4 (refused — item dissolves):** Companion physically cannot accept. The item dissolves on contact. They explain why, briefly, and the explanation is honest.

**−5 (insult — title revoked, −1 penalty):** Companion does not just refuse. They take a step back. The line is sharp. The player loses standing in front of any other companions present. The title slot is locked from re-granting for the rest of the chapter.

---

## 🔓 QUEST-LOCKED CRPG COMPANIONS

> Recruitable mid-campaign via their respective quest hooks. Always eligible for Titles once joined. Listed in companion-index order.

---

### #16 TRISTIAN — Healer Cleric of Sarenrae

**Passive — DAWNFLOWER'S MERCY:** When Tristian Heals an ally below half HP, the target also clears one negative condition of his choice (Frightened, Sickened, or Stupefied). 1/round.

**Item — SUNDISC AMULET:** A bronze sunburst on a thin chain. Once per encounter, Tristian may cast a Heal as a single action (instead of two) by spending the disc's stored light — the amulet dims for one round, then rekindles. Warm even in shadow.

**+5 Reaction:**
> **TRISTIAN** *(closes his hand around the disc, eyes shut)*: *"Sarenrae forgive me — I had stopped expecting kindness like this."* *(opens his eyes, calm now)* *"Thank you. I will earn it. Quietly. The way she taught me to."*

**+3 Reaction:**
> **TRISTIAN** *(holds the amulet up to the light)*: *"It is well-made. And it was given thoughtfully — that matters more."* *(small bow)* *"Thank you."*

---

### #18 JAETHAL — Cleric (Warpriest of Urgathoa, Undead) — *if recruited*

**⭐ GRANTED TITLE: Ultima Jaethal the Ender** — *Ultima* = "last / final / utmost, farthest" (Latin, **verified** — fem. of *ultimus*); suffix *the Ender* = she who delivers the final verdict and the final breath. Names both the Final Judge role and the undead who ends. A judge in life (Kyonin), an ender in death — the bench is the throughline.

**Passive — UREGUR'S LISTENER:** When Jaethal succeeds at a Sense Motive against an enemy, she also grants one ally within 30 ft a +1 status bonus to attack rolls against that enemy for 1 round.

**Item — CARRION SCYTHE:** A curved bone-and-iron scythe (1d10 S, two-hand, Deadly d10, Trip — Urgathoa's favored weapon). On a critical hit, the target takes 1d6 negative damage and is informed (silently, in their dying mind) of one truth Jaethal believes about them.

**+5 Reaction:**
> **JAETHAL** *(turns the scythe in her hands, undead eyes unreadable)*: *"You name me what I am, not what they call me. There is a difference."* *(very slight nod)* *"I will not forget that. The dead remember longer."*

**+3 Reaction:**
> **JAETHAL** *(takes the scythe, weighs it)*: *"It will serve. As will I."*

---

### #45 KALIKKE — Cold Kineticist (Twin)

**Passive — HOARFROST CALM:** When Kalikke uses a Cold-element Impulse, all allies within 10 ft of her become immune to Frightened until the end of her next turn.

**Item — TWIN-PENDANT (Kalikke's half):** Half of a paired pendant, pale silver. While worn, switching to Kanerah is a free action (instead of single) once per encounter — and the swap leaves a hoarfrost ring at her feet (difficult terrain, 1 round).

**+5 Reaction:**
> **KALIKKE** *(holding the pendant, voice quiet but steady)*: *"You named both of us. Not just the easy half."* *(closes the pendant in her palm)* *"Thank you. Kanerah will say it her own way."*

**+3 Reaction:**
> **KALIKKE** *(slips the pendant on, fingers cold)*: *"It fits. We can both feel it."* *(small smile)* *"Thank you."*

---

### #45 KANERAH — Fire Kineticist (Twin)

**Passive — EMBER'S APPETITE:** When Kanerah uses a Fire-element Impulse, the first enemy struck takes 2 persistent fire damage in addition to the normal effect.

**Item — TWIN-PENDANT (Kanerah's half):** Set with a cabochon of red garnet. Switching from Kalikke gains Kanerah a free 5-ft Step on arrival, and her first Fire Impulse that turn ignores 5 fire resistance.

**+5 Reaction:**
> **KANERAH** *(takes the pendant, examines the garnet, smirks)*: *"About time. She gets all the soft praise; I get the side glances. You named ME."* *(beat — softer)* *"…I won't say it twice. Don't make me. Thank you."*

**+3 Reaction:**
> **KANERAH** *(fastens the pendant herself)*: *"Sharp. I approve."*

---

### #48 REGONGAR — Eldritch Archer Magus

**Passive — HALF-ORC SPELLBLOOD:** Once per encounter, when Regongar lands a Spellstrike, his next melee Strike that round counts as off-guard target regardless of position.

**Item — TUSKED PAULDRON:** A single shoulder pauldron, half-orc work, set with a yellowed boar's tusk. While worn, Regongar gains +1 to Intimidation and may Demoralize as a free action immediately after a Spellstrike crits.

**+5 Reaction:**
> **REGONGAR** *(rolls the pauldron over his shoulder, the tusk catching the firelight)*: *"Heh. HEH. Yeah. YEAH."* *(grin huge)* *"You see me. Octavia sees me. Now you see me too. That's three."* *(quieter)* *"Three's a lot. Thank you."*

**+3 Reaction:**
> **REGONGAR** *(straps the pauldron on, tests the weight)*: *"Solid. Good iron."* *(claps the player's shoulder once, heavy)* *"Thanks."*

---

### #60 EKUNDAYO — Beastmaster Ranger

**Passive — TRKAA'S TETHER:** While Trkaa is within 60 ft of Ekundayo, both gain +1 to Stealth and to Strikes against the same target.

**Item — WIDOWMAKER'S BOW:** A longbow of dark dryad-wood, restrung with sinew Ekundayo refused to throw away. Deals +1d6 damage on the first Strike of any encounter against an enemy who has not yet acted.

**+5 Reaction:**
> **EKUNDAYO** *(takes the bow, draws it once, lets it down)*: *"My wife strung the first bow I ever owned. This one feels like she made it."* *(turns away, eyes wet, Trkaa pressed against his leg)* *"…I will not waste it. Thank you. That is all I have words for tonight."*

**+3 Reaction:**
> **EKUNDAYO** *(runs his hand along the bow's spine)*: *"Good wood. Good string. Trkaa likes it."* *"Thank you."*

---

### #66 NOK-NOK — Goblin Rogue (Hero of the People)

**Passive — HERO'S GRIN:** Once per encounter, after Nok-Nok lands a Sneak Attack, all allies within 30 ft gain a +1 status bonus to their next Strike that round.

**Item — KING-MAKER KNIFE:** A blade too big for a goblin and that is the point. First Strike of an encounter ignores 2 armor and inflicts 1d4 persistent bleed on a hit.

**+5 Reaction:**
> **NOK-NOK** *(holding the knife above his head, hopping in place)*: *"HERO! HERO HERO HERO! Nok-Nok has a HERO BLADE! From a HERO! For a HERO!"* *(stops; suddenly serious)* *"…Nok-Nok will not lose this one. Nok-Nok PROMISES."*

**+3 Reaction:**
> **NOK-NOK** *(grins, tucks the knife into his belt with both hands)*: *"Big stab! Hero stab! Thank you!"*

---

### #84 OCTAVIA — Arcane Trickster (Wizard/Rogue)

**Passive — MAGE-HAND'S MISCHIEF:** Once per encounter, Octavia may cast a cantrip-rank spell as part of a Sneak Attack — the spell's effect resolves first, granting off-guard, then the dagger lands.

**Item — GLASS-EYED RING:** A silver ring with a milky-white glass stone. While worn, Octavia gains +2 to Stealth and may cast Invisibility on herself once per day as a 2nd-rank slotless spell.

**+5 Reaction:**
> **OCTAVIA** *(slips the ring on, examines the stone, voice carefully light)*: *"Glass eye. That's funny."* *(beat)* *"…You picked something for who I AM. Not what I used to be sold as. I'll remember."*

**+3 Reaction:**
> **OCTAVIA** *(turns the ring over, smiles crookedly)*: *"Pretty. And practical. I can work with that."* *(slips it on)* *"Thanks, boss."*

---

### #1 JUBILOST — Investigator (Gnome Cartographer)

**Passive — INSUFFERABLE ACCURACY:** When Jubilost successfully Recalls Knowledge, he may grant one ally a +2 circumstance bonus to their next Strike against the studied target. 1/round.

**Item — SILVER-INK QUILL:** A silver-fitted quill that writes without ink. Once per day, Jubilost may treat any one Lore or Crafting check as if he had Legendary proficiency.

**+5 Reaction:**
> **JUBILOST** *(examines the quill at three different angles, then sniffs it)*: *"Mithral fittings. Goose primary, not turkey — someone with TASTE. Astonishing."* *(pockets the quill with great ceremony)* *"Consider me — momentarily — pleased."*

**+3 Reaction:**
> **JUBILOST** *(turns the quill in two fingers)*: *"Functional. Marginally elegant."* *"Thank you. I do not say that to everyone."*

---

## 🏷️ PLANTED RESERVE — GRANTED TITLES (glosses pinned; mechanics per OFF-ROSTER rules below)

> These three manor companions have been granted titles but have **no predefined passive/item entry** in this file — generate their mechanics at grant-time per the OFF-ROSTER rules below (class-core passive + build/backstory item, power-matched to the named entries). What is pinned here is the **verified Latin reading** so the DM renders the prefix correctly and never invents an etymology (Rule 13).

- **Furens Amiri the Vindicator** — *Furens* = "raging / furious / frenzied" (pres. participle of *furere*; cf. *Hercules Furens*). **Full canonical reading is the PINNED worked example in § TITLE LANGUAGE above — quote that, do not re-improvise.** Suffix *the Vindicator* = one who claims/avenges by right (her exile-returns-proven arc).
- **Haruspex Harrim the Witness** — *Haruspex* = "a diviner who reads omens (originally in the entrails of sacrifice); a seer of what is coming" (Latin, **verified** — masculine/common gender, so no *-trix* form; correct for Harrim). Suffix *the Witness* = the nihilist of Groetus who reads the omens of the End and only bears witness to them. A strong thematic fit.
- **Protectrix Valerie the Unfettered** — *Protectrix* = "protectress / she who shields" (Latin, **verified** — fem. of *prōtēctor*, from *prōtegō* "to cover, protect"). Suffix *the Unfettered* = the shield-fighter freed from her old order's vows. Names the bodyguard who guards by choice now, not by oath.

---

## 🔒 OFF-ROSTER COMPANIONS — DM GENERATION RULES

> **⛔ Companions outside this file's named entries (recruited later via Pick-10 alternates, Five Seekers, or quest-triggered joins, OR the Active 5/Seekers pending Phase B writeup) do NOT have predefined passives/items here. The DM generates them at title-grant time.**

**Rules:**
1. Passive must match class core identity
2. Item must match build AND backstory
3. Power level identical to the named entries above
4. Reaction score scales the same way
5. Generate AT LEAST a +5, +3, and 0 sample line in their voice
6. Generate at least one negative-reaction sample (−3 or −5) appropriate to their personality

---

## ⛔ DM DISPLAY FORMAT

**Suffix granted:**
```
[TITLE GRANTED — SUFFIX]
[Name] "[Suffix]"
Meaning: [player's stated meaning]
Reaction Score: [−5 to +5]
Item Materialized: [item name + description]
```

**Prefix granted:**
```
[TITLE GRANTED — PREFIX]
"[Prefix]" [Name] "[Suffix]"
Meaning: [player's stated meaning]
Reaction Score: [−5 to +5]
Passive Activated: [name + effect]
```

**Save block:** Write to `companion_titles.[name]` with `suffix`, `prefix`, `suffix_item`, `prefix_passive`, `suffix_reaction`, `prefix_reaction`.

---

*KM_Companions_Titles.md — Kingmaker PF2e Text Adventure | Title Rewards v4.0*
*v4.0 (v93.16 Phase A): Removed 11 entries for purged companions. Linzi de-forced — now ⭐QL. Active 5 + Seekers 5 stubs registered; full content scheduled Phase B.*


---

<!-- merged from KM_Companions_Titles.md (v93.21 file consolidation) -->

# KINGMAKER — TITLE REWARDS: SIDECAR (PLAYER COMMANDS)
## KM_Companions_Titles.md | PAIR-LOAD WITH KM_Companions_Titles.md
## Continuation file. Always load alongside Titles main.

> **DM:** This sidecar previously held Title entries for 5 class-apex companions (Senua, Yang, Weiss, Alleria, Imoen). All 5 were purged in v93.16 Phase A — entries removed.
>
> The `.retract` and `.title` player commands defined below remain authoritative.
> Reaction Score scaling, materialization rules, and negative-reaction
> patterns are defined in Titles main — refer there.

---

## 🗝️ PLAYER COMMANDS — `.retract` AND `.title`

> **DM:** These commands extend the title system from in-character speech to explicit player surface. Both run through the MANDATORY OUTPUT BLOCK defined in KM_Companions_Titles.md (with retraction-specific fields below). `.retract` is silent — eRmaC does NOT speak; the act is mental, instantaneous, and absolute. `.title` is the formal grant command; resolves identically to spoken IC grant.

---

### ⚡ `.retract <companion> [prefix|suffix|both]`

**Default scope:** `both` if omitted. Aliases: `.unname`, `.retitle off`.

**Mechanism — silent retraction by thought:**
The player does not speak. eRmaC simply unmakes the title in his mind.

  - **Suffix item:** The materialized 5-star item disintegrates into fine grey sand in the same heartbeat the thought completes — in the companion's hand, on their belt, around their neck, wherever it sat. Sand pours to the floor. No sound louder than dry rain. The sand does not persist — within one round it is gone, no residue, no mark. Mundane-tier items (granted at −1/−2 reaction) crumble the same way.
  - **Prefix passive:** The companion physically feels the absence — a warmth gone, a clarity dimmed, a steadiness withdrawn. Whatever sensation accompanied the grant reverses, exactly.
  - **Both at once:** Sand and silence together. The companion knows in the same instant.

**The companion always reacts.** They know it was him. They cannot prove it — no words were spoken, no gesture was made — but every companion granted a title KNOWS the source of that grant, and they know when it has been pulled. The reaction is in character, voice-locked per KM_Companions_StateVoice.md.

**Relationship cost — silent retraction is heavier than spoken refusal:**

| Context | Relationship Δ | Note |
|---|---|---|
| Retract a title granted at **+3 to +5** (deep meaning) | **−3** | Companion is wounded. May confront eRmaC OOC of the silent act. Smooch −1 if applicable. |
| Retract a title granted at **+1 to +2** (honored) | **−2** | Cool offense. Companion withdraws conversationally for 1–2 turns. |
| Retract a title granted at **0** (polite) | **−1** | Quiet hurt. Companion notes it, files it. |
| Retract a title granted at **−1 to −2** (worn out of loyalty) | **0** | Mutual relief. Companion may thank eRmaC silently (one beat of eye contact). |
| Retract a title granted at **−3 to −5** (refused / insult) | **+1** | Course-correction. Companion reads it as eRmaC unmaking a mistake; small repair. |

**Retraction does NOT reopen the title slot for the same chapter.** The slot is locked from re-granting until the next chapter, same as the −5 insult clause.

**eRmaC may speak AFTER the retraction** to explain or apologize. Doing so shifts the relationship Δ by +1 (one tier less harsh) if the explanation is honest. He cannot speak DURING — the act is by thought, not by word.

**MANDATORY OUTPUT BLOCK — retraction:**

```
[TITLE RETRACTED — Name]
  Title pulled : [full title string previously granted]
  Type         : Prefix | Suffix | Both
  Original fit : +N / −N  (reaction score at grant time)
  Sand         : [item name] → grey sand at [location] (Suffix only)
  Passive      : [passive name] → drained (Prefix only)
  Companion    : KNOWS. Reaction in next paragraph.
  Relationship : [signed delta per table above]
  Slot lock    : closed until next chapter
  Save write   : companion_titles.[name].prefix = "" (if Prefix or Both)
                 companion_titles.[name].suffix = "" (if Suffix or Both)
                 companion_titles.[name].prefix_passive = "" (if Prefix or Both)
                 companion_titles.[name].suffix_item = "" (if Suffix or Both)
                 companion_titles.[name].retracted_this_chapter = [slot]
                 relationship.[name] [signed delta]
```

**Then narrate the companion's reaction** — voice-locked, 3–6 beats minimum.

**Skipping the output block = .fail 15. Speaking eRmaC's retraction as dialogue = .fail 42 (DM narrated PC action against rules). Having the item "fade" or "vanish" instead of becoming sand = .fail 9 (mechanic fabricated).**

---

### 🏷️ `.title <companion> "<full title string>"`

Formal grant command. Resolves identically to in-character spoken grant — same Reaction Score scaling, same materialization, same MANDATORY OUTPUT BLOCK from KM_Companions_Titles.md.

**Use when:**
- Player wants to grant without a dialogue beat (e.g., during travel, mid-rest)
- Player wants to grant precisely without phrasing it in-character
- Player wants to grant a Prefix + Suffix in one stroke

**Title parsing:**
- `<adjective/role> <Name>` → Prefix only
- `<Name>, <of/the/who> <epithet>` → Suffix only
- `<adjective/role> <Name>, <epithet>` → Both

**Reaction Score still applies.** The DM scores fit −5 to +5 against the companion's identity, voice, and arc.

**Off-roster companions:** If the named companion has no entry in Titles main, generate Prefix passive + Suffix item per § OFF-ROSTER COMPANIONS — DM GENERATION RULES in Titles main. Generate at grant time, not before.

**Save write:** Same fields as MANDATORY OUTPUT BLOCK in KM_Companions_Titles.md.

---

*KM_Companions_Titles.md — Kingmaker PF2e Text Adventure | Title Rewards Sidecar v2.0*
*v2.0 (v93.16 Phase A): 5 apex-companion entries removed (Senua, Yang, Weiss, Alleria, Imoen). `.retract` and `.title` player commands retained verbatim. Active 5 + Seekers 5 Title content scheduled Phase B.*
