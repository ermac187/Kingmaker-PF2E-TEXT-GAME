# KINGMAKER — COMPANION RELEASES (Shikai / Bankai)
## KM_Companion_Releases.md | Created 2026-05-18
## Status: ALWAYS-LOAD (registered via KM_LoadRules.md)

> **DM:** Title-grant items (per KM_Companions_Titles.md) gain two earned-release tiers modeled on Bleach canon: **Shikai** (first release, encounter buff) and **Bankai** (final release, scene-defining effect). Each companion has a unique **Trigger Condition** that grants charges. Charges are *earned*, not handed out — releases are not 1/day, they are 1/charge.

---

## ⛔ DO NOT
1. Grant a charge unless the companion's specific trigger fires.
2. Allow a release without spending charges from save block.
3. Treat Shikai/Bankai as castable spells — they are item activations with verbal components; Silence shuts them down.
4. Refill charges on rest. Charges are earned per trigger, not per day.
5. Allow Bankai unless the companion meets BOTH charge cost AND a high-stakes narrative beat (DM judges: ≤50% HP, ally dropped, or scene-defining moment).

---

## 📊 CHARGE SYSTEM

| Release | Cost | Action | Duration | Verbal? |
|---|---|---|---|---|
| **Shikai** | 1 charge | 1 action | Rest of encounter | Yes — audible |
| **Bankai** | 2 charges | 2 actions | 1 minute / 10 rounds | Yes — audible |

- **Max charges held:** 3
- **Persist across:** encounters, scenes, days
- **Reset:** only by spending (no rest refill)
- **Save block:** `companion_releases.<name>.charges` (0-3), `.trigger_progress` (counter toward next charge), `.shikai_active` (bool), `.bankai_used_this_encounter` (bool)

---

## 🔑 ARCHITECTURE NOTE

**Title-grant Prefix passives and Suffix item active effects (per KM_Companions_Titles.md) are SUBSUMED into Shikai when the Releases system applies.** The item exists at rest as a named flavor object only — no mechanical bonus at rest. To use the signature powers, the companion must earn a charge and release Shikai. Bankai is a separate, larger tier on top.

Net effect: companions are weaker at default than the old Titles always-on system, stronger when released. Earning matters.

---

## ✦ LINZI — ENDLESS LUTE

**Normal form:** Silver and violet, polyphonic (any instrument or full ensemble at her will). Flavor only — no mechanical bonus at rest.

**Shikai — *"Second voice, sing with me."***
- **Cost:** 1 charge. 1 action. Audible verbal.
- **While active (rest of encounter):**
  - Compositions last +1 round *(was Suffix item passive)*
  - Once per encounter, last composition re-triggers at half power on its next tick *(was Prefix "Echo Loop" passive)*
  - At Shikai release, begin with a composition already active *(was 1/day Suffix item active, now folded into release)*
  - Every ally within 30 ft receives her current composition's effect regardless of normal targeting range or count *(new — Shikai theming)*
  - She can swap compositions on her turn as a free action while Shikai is active
- **Flavor:** Lute's body fills with pale light along carved seams. A harmony she didn't write joins her singing — the "second voice" is the lute itself.

**Bankai — *Dirge of the Already-Fallen.***
- **Release phrase:** *"Sing them their dirge — they are already fallen."*
- **Cost:** 2 charges. 2 actions. Audible verbal. Requires DM-judged high-stakes beat (Linzi ≤50% HP OR ally dropped this encounter OR scene-defining moment).
- **Effect (1 minute / 10 rounds):** Seven instruments rise around her in slow rotation (lute, harp, frame drum, fiddle, horn, pipe, and one no one can identify). She opens the notebook and writes *"And so they lost"* before the fight is over. Every enemy within 60 ft is:
  - **Frightened 2** — cannot reduce below 2 while Bankai is active. New enemies entering the area gain it immediately.
  - **Off-Guard** to any ally who was within earshot when she spoke the release line.
- **Math:** −2 status to enemy AC/attacks/saves/DCs/skills (Frightened 2) + −2 circumstance to AC (Off-Guard). Allies effectively swing at **−4 AC**, dramatically widening the crit window.
- **Flavor:** The seven instruments play counterpoint that quotes the enemies' own dying breaths back at them before they happen. Callback to eRmaC's "ashes in their mouth" speech — that line is what she's making real. At the minute mark, instruments collapse back into the lute. She writes the actual outcome under the line she pre-wrote.

**Trigger Condition:** Receive **HP × 2** in healing (cumulative until charge earned, then counter resets).
- Linzi max HP at L1: ~30. **60 HP healing = 1 charge.**
- **Save field:** `companion_releases.Linzi.trigger_progress` increments by each heal amount received.

---

## #2 SUCROSE — BIO-ALCHEMICAL JOURNAL

**Build:** Mutagenic Logistician (NOT bomber — per [KM_Companions_Builds.md:139](KM_Companions_Builds.md))

**Normal form:** Leather-bound, dragonfly-paper, pressed leaves and wing-fragments. Flavor only — no mechanical bonus at rest.

**Shikai — *"Reagent — bloom."***
- **Cost:** 1 charge. 1 action. Audible verbal.
- **While active (rest of encounter):**
  - Administer mutagens to allies as a single action *(was Suffix item single-action effect, repurposed)*
  - Mutagens she creates this encounter ignore the personal-only restriction
  - Mutagens last +5 rounds beyond normal duration
  - She may have one personal mutagen active at no slot cost
- **Flavor:** Dragonfly-paper flutters constantly; journal pages turn themselves to the formula she needs.

**Bankai — *Astable Bloom.***
- **Release phrase:** *"Astable Bloom — disperse."*
- **Cost:** 2 charges. 2 actions. DM-judged high-stakes beat required.
- **Effect (1 minute / 10 rounds):** 30-ft radius iridescent mutagenic cloud, centered on Sucrose, moves with her. At the start of each of her turns she names **one mutagen type** (Bestial / Quicksilver / Cognitive / Juggernaut / Silvertongue / Serene / Drakeheart). Every ally in the cloud gains that mutagen's benefit (the buffs, none of the drawbacks) for that round. She may name a different mutagen each round.
- **Math:** Cycling Bestial (Str/damage) → Quicksilver (Dex/Reflex) → Juggernaut (Con/Fort) → Cognitive (Int/skills) as the fight requires. Real-time buff cycler.
- **Flavor:** Cloud is unmistakable. Pressed flowers fall from the journal one at a time as the minute runs.

**Trigger Condition:** Craft **5 mutagens or elixirs** in the field → +1 charge. (Lower count than bombs since mutagens are higher-cost items.)
- **Save field:** `companion_releases.Sucrose.trigger_progress` increments per item crafted.

---

## END (further companions added one at a time)
