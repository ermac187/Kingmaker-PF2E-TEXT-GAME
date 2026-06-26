# KINGMAKER — NPC & COMPANION OPINION SYSTEM (PART A)
## KM_NPC_Relations_A.md | Active from: Pre-Prologue
## Referenced by: KM_Companions.md, KM_Romance.md, KM_Reputation.md
## Part A: System rules + KM CRPG companion profiles | Part B: WotR/Iconics profiles + Story NPCs + Attraction
### Load BOTH parts every session alongside KM_Companions.md.

> **DM:** This system tracks a continuous Opinion Score for every named character — all 89 companions and all key story NPCs. It replaces the flat −2/+2 label as the mechanical backend. The old labels remain valid as display tiers. Four input streams drive every score automatically, every session.
>
> **Governs:** All 89 companions + key story NPCs. Does NOT govern unnamed civilians (KM_Reputation.md) or faction standing (KM_Kingdom.md).

---

## 📊 THE OPINION SCORE

Every named character tracks a single integer: **Opinion Score**, range **−20 to +20**.

```
+16 to +20  : DEVOTED       — sacrifices for player; hidden truths shared; quest unlocked
+11 to +15  : FRIENDLY      — trusts player; personal dialogue open; full cooperation
 +6 to +10  : WARM          — proactive help; opinions volunteered; benefit of the doubt
 +1 to  +5  : FAVORABLE     — mild positive; slightly open; no friction
  0         : NEUTRAL       — default; professional; no investment
 −1 to  −5  : COOL          — mild skepticism; shorter answers; slight friction
 −6 to −10  : STRAINED      — visible disapproval; reduced cooperation
−11 to −15  : HOSTILE       — argues; may refuse orders; undermines
−16 to −20  : ADVERSARIAL   — actively works against player; may leave or betray
```

## 📈 OPINION TIER — MECHANICAL EFFECTS

Each tier grants or imposes mechanical effects. Applied silently — never announced.

```
DEVOTED (+16 to +20) — ADVANTAGES:
  +2 circ. to Diplomacy, Deception, and Intimidation checks involving this character
  Character volunteers hidden information without being asked
  Character will lie, sacrifice, or take personal risk for the player unprompted
  Merchant NPCs at DEVOTED: 15% discount on all purchases
  Companion NPCs at DEVOTED: +1 to all skill checks when assisting the player

FRIENDLY (+11 to +15) — ADVANTAGES:
  +1 circ. to Diplomacy and Deception checks involving this character
  Character shares personal opinions and useful intel proactively
  Merchant NPCs at FRIENDLY: 10% discount on purchases
  Companion NPCs at FRIENDLY: full combat performance; no hesitation

WARM (+6 to +10) — ADVANTAGES:
  +1 circ. to Diplomacy checks involving this character
  Character gives benefit of the doubt on ambiguous actions
  Merchant NPCs at WARM: 5% discount on purchases
  Companion NPCs at WARM: proactive help in skill challenges
  Companion offers tactical suggestions before combat ("I could flank left")
  Companion shares one personal detail unprompted per chapter

FAVORABLE (+1 to +5) — ADVANTAGES:
  No mechanical bonus — but no friction either
  Character defaults to cooperative when asked for help
  Companion remembers and references player's previous choices in dialogue

NEUTRAL (0) — NO EFFECT:
  Professional. Transactional. No modifier in either direction.

COOL (−1 to −5) — DISADVANTAGES:
  −1 circ. to Diplomacy checks involving this character
  Character withholds optional information (won't volunteer tips or warnings)
  Companion NPCs at COOL: shorter dialogue; may decline optional side tasks

STRAINED (−6 to −10) — DISADVANTAGES:
  −2 circ. to Diplomacy checks involving this character
  −1 circ. to Deception checks (they're watching for lies)
  Character actively withholds useful intel even when asked
  Companion NPCs at STRAINED: −1 to skill checks when assisting the player
  Merchant NPCs at STRAINED: 10% markup on all purchases

HOSTILE (−11 to −15) — DISADVANTAGES:
  −3 circ. to Diplomacy checks involving this character
  −2 circ. to Deception checks
  Character may spread negative info about the player to other NPCs
  Companion NPCs at HOSTILE: may refuse direct orders; −2 to assist checks
  Merchant NPCs at HOSTILE: 25% markup or refuse sale entirely

ADVERSARIAL (−16 to −20) — DISADVANTAGES:
  Diplomacy checks auto-fail unless player has leverage or a critical success
  Character actively works against the player (sabotage, information to enemies)
  Companion NPCs at ADVERSARIAL: may leave party; may betray in critical moments
  Merchant NPCs at ADVERSARIAL: refuse all trade; may report player to authorities
  Story NPCs at ADVERSARIAL: become quest obstacles or antagonists
```

**Cross-system note:** Opinion tier effects apply on top of Romance and Brotherhood effects. A Brotherhood Stage 3 TRUSTED companion at Opinion STRAINED still gets the −1 assist penalty — combat trust does not erase personal friction.

**Save block field:**
```json
"npc_relations": {
  "[Name]": { "score": 0, "trend": "stable", "last_change": "", "attraction": false }
}
```

**Display:** `.npc attitude [name]` returns tier label + trend (Rising/Stable/Falling). Never the raw number to the player.

---

## 🔁 THE FOUR STREAMS — APPLY EVERY SESSION

All four streams fire automatically every session. Do not defer, do not batch.

---

### STREAM 1 — DIRECT INTERACTION
Applied when the player speaks to or acts on this character directly.

**Gains:**
- Acknowledge their opinion, even while disagreeing: **+1**
- Follow through on something promised to them: **+2**
- Defend them socially against a third party: **+2**
- Risk real resources (HP, gold, reputation) for their sake with no tactical reason: **+2**
- Remember a personal detail they mentioned and act on it unprompted: **+2**
- Defer to their expertise or ask their opinion on their specialty: **+1**
- Give a meaningful gift connected to their interests or history: **+1**

**Losses:**
- Talk over or dismiss them mid-dialogue: **−1**
- Lie to them and they discover it: **−2**
- Use their personal pain as leverage or humor: **−3**
- Publicly disrespect or embarrass them in front of others: **−3**
- Break a promise made directly to them: **−2**

---

### STREAM 2 — OBSERVED DECISIONS
Applied when a character witnesses or learns of the player's choices. Every major decision is evaluated against each character's Core Values and Likes/Dislikes (see profiles). Apply without prompting — do not wait for the player to ask.

**Scoring:** Decision aligns with a Like: **+1** | Decision aligns with a Dislike: **−1** | Decision touches a ★ Core Value: **±2**

**Decision categories always evaluated:**
- How combat is resolved (mercy, execution, negotiation, style)
- Treatment of prisoners and surrendered enemies
- Kingdom laws, policies, punishments, resource allocation
- How the player treats civilians and people with no power in the scene
- What the player says about people who are absent

---

### STREAM 3 — PARTY ASSIGNMENT REACTIONS
Applied when the player selects a mission party. Characters left behind may react based on whether they wanted to go or felt more qualified than who was picked.

**Penalty triggers (each applies independently):**

*Wants to go (−1 if left out):*
- Mission involves their primary specialty (see each profile)
- Mission has personal stakes for them (their quest line, their people, their region)
- They have been left out of the last two consecutive major missions

*Feels more qualified than who was picked (−1 additional):*
- Player chose a companion with demonstrably lower applicable skill for a task this character excels at
- DM evaluates skill match, not just the pick — a valid alternative pick avoids this penalty

**No penalty if:** Companion was recruited after departure | Companion had the previous mission exclusively | Companion openly said they didn't want to go

**Max penalty per missed mission: −2.** Never announced directly. Surfaces as tone, brevity, a pointed question.

**Mission snub compounding:** After three consecutive missed missions without explanation, a companion will say something — obliquely. At Strained or lower they may say it plainly.

---

### STREAM 4 — MISSION OUTCOME REACTIONS
Applied when a mission resolves. Present characters evaluate the result. Absent characters who learn of it react to major outcomes.

| Outcome | Who / Effect |
|---------|-------------|
| Decisive victory, minimal cost | All present: **+1** |
| Player saved a life at real personal cost | All present: **+1** / Target NPC: **+3** |
| Player made a contested decision mid-mission | Each objecting companion: **−1** |
| Succeeded via deception (even well-intentioned) | Valerie −1, Nok-Nok +1, Octavia 0 |
| Failed due to player choice, not bad luck | All present: **−1** |
| Abandoned civilian or ally to complete mission | Tristian −2, Linzi −2, Seelah −2, Kyra −2, Sajan −1, Arueshalae −2 |
| Executed a surrendered enemy | Tristian −2, Seelah −2, Kyra −2, Octavia −2, Jaethal +1, Harrim 0 |
| Spared enemy who later caused trouble | Harrim +1, Valerie +1, Jaethal +1 |
| Creative bypass — no fight needed | Linzi +1, Lem +1, Octavia +1, Amiri −1 |
| Fought through when negotiation was possible | Amiri +1, Tristian −1, Linzi −1 |

---

### STREAM 5 — THIRD-PARTY SABOTAGE
Applied when a named antagonist NPC actively works to poison the player's standing with other characters. Currently: **Tartuccio only** (Prologue through Ch1). Other antagonists may be added at later chapters.

> **DM:** This stream fires automatically when Tartuccio is present in a scene with a targetable NPC. It does not require the player to notice or do anything. The player discovers it through Perception, Sense Motive, or by observing consequences. Do not announce it.

---

**HOW SABOTAGE WORKS**

Tartuccio has a **Sabotage Budget** — a number of −1 influence actions he can take per scene. Each action applies a −1 to a target NPC's Opinion Score toward the player. The budget resets each scene (defined as: a new location, a new session phase, or a time skip of 1+ hours).

He does not use his budget all at once. He is patient. He spends where he calculates it will compound — a companion already at +2 is more worth poisoning than one at +8, because the low-score companion was close to acting in the player's favor.

**His methods (never stated aloud, never labeled):**
- Private asides that reframe the player's actions as suspicious or self-serving
- Friendly commentary that plants a false memory (*"Didn't [player] say something similar to what that Pitaxian agent said? I thought it was odd at the time..."*)
- Redirecting a companion's frustration onto the player when a mission goes poorly
- Letting a rumor land without correcting it — then expressing mild doubt
- Agreeing with a companion's positive assessment and then adding *one* reservation

**The DM narrates the effect, not the cause.** An NPC becomes slightly colder, shorter in their answers, less forthcoming. The player may notice — or may not.

---

**SABOTAGE BUDGET BY CONTEXT**

| Context | Tartuccio's Budget (per scene) |
|---------|-------------------------------|
| Prologue Phase 1 (feast) | 1 action — cautious, establishing himself |
| Prologue Phase 4.5 (wind-down) | 2 actions — working harder now |
| Ch1 — any scene where Tartuccio appears | 2 actions |
| Ch1 — Ancient Tomb confrontation | 1 action (he's focused on escape) |
| Ch1 — Old Sycamore sanctum | 0 (combat only, no social manipulation) |

---

**TARGETABLE NPCs AND CAP**

Tartuccio may target any NPC in the scene. He prioritizes:
1. **NPCs close to a positive threshold** (about to unlock a benefit for the player)
2. **Companions the player has visibly invested in**
3. **Jamandi** — if present and the player has been praised in front of her

**Sabotage Cap:** No NPC's score can be driven below **−5** by Tartuccio's actions alone. He can push someone into Cool or Strained, but cannot manufacture Hostile — that requires the player's own actions to compound.

**Compounding:** If the player's own behavior already drove a score down, Tartuccio's sabotage stacks on top. The cap does not apply to the combined total — only to his contribution. A player who has also behaved poorly can be pushed further.

---

**DETECTION**

The player can detect sabotage is occurring (not necessarily prove it) through:

| Method | DC | What they learn |
|--------|----|----|
| Perception (during scene) | DC 15 | Notice Tartuccio speaking privately with [NPC] — content unclear |
| Sense Motive (on the NPC after) | DC 13 | NPC's coolness feels externally sourced, not organic |
| Diplomacy (ask NPC directly) | DC 12 | NPC reveals Tartuccio said something; vague on specifics |
| Investigation / asking around | DC 14 | Pattern emerges — multiple NPCs slightly cooler after Tartuccio scenes |

Detection does not automatically reverse the score. The player must still repair the relationship through normal Stream 1 interactions. Detection does, however, set `tartuccio_sabotage_exposed = TRUE` — which grants advantage on future Diplomacy with affected NPCs (+2 bonus, as the player can now name what happened).

---

**RECRUITMENT AND TRUST CONSEQUENCES**

An NPC whose score has been sabotaged into the negative range responds differently when the player tries to recruit them or seek their help:

| Score at time of approach | Effect |
|--------------------------|--------|
| −1 to −5 (Cool) | Will not volunteer. Recruitment requires Diplomacy DC 12. Success still recruits normally — they just needed convincing. |
| −6 to −10 (Strained) | Actively skeptical. Diplomacy DC 16 to recruit. On failure: refuses for this scene. Retry next scene after player earns any Stream 1 gain with them. |
| −11 or lower (Hostile — only possible if player's own actions compound) | Will not recruit this chapter. Requires a dedicated reconciliation scene (Diplomacy DC 20 or a witnessed act that directly serves their Core Value). |

**Jamandi specifically:** Her score affects what she volunteers beyond the baseline charter. She will always grant the charter (story-required) — but at Cool or lower she adds conditions, delays correspondence, and withholds political intelligence. The recruitment penalty applies to everything beyond the minimum she is obligated to provide.

---

**COUNTERING SABOTAGE (PLAYER OPTIONS)**

The player can actively undercut Tartuccio's social work:

- **Call him out in front of the target NPC:** Diplomacy or Deception DC 14 — success: +2 to target NPC, Tartuccio loses 1 budget action next scene. Failure: no change, Tartuccio gets to respond and may spend a budget action immediately.
- **Pre-empt him with a stronger impression:** Any Stream 1 gain with an NPC *before* Tartuccio reaches them negates his next budget action on that target.
- **Expose the pattern (after `tartuccio_sabotage_exposed`):** In any scene with multiple NPCs present, player may spend an action to state what they've observed. Diplomacy DC 13 — success: all present NPCs gain +1, Tartuccio's budget drops to 0 for this scene.

---

*Stream 5 applies from Prologue Phase 1 through end of Ch1. After Ch1 (`tartuccio_fate` set), this stream suspends unless he reappears.*

---

## 👥 COMPANION PROFILES — KM CRPG + ICONICS (Canonical IDs)

**Format:** Default Score | ★ Core Value | Likes | Dislikes | Mission Specialty

> **Attraction eligibility noted where applicable. Full attraction mechanics in KM_NPC_Relations_B.md.**

---

**#6. AMIRI** | Default: 0 | Specialty: combat / monster hunts / giant encounters
★ Strength proven through action — not given, not inherited, earned
Likes: worthy opponents, directness, people who don't flinch from her, Kellid cultural respect
Dislikes: mercy that reads as weakness, magic replacing physical solutions, being underestimated, sentiment over action
**Attraction-eligible** — combat-earned path only (see Part B)

---

**#✦. LINZI** | Default: 0 | Specialty: social / diplomacy / chronicle missions
★ Stories worth telling; smallfolk protected and remembered
Likes: memorable moments, protecting those with no power, honest emotion, being included in decisions
Dislikes: senseless cruelty, cynicism, destroying things with history, being left behind
**Attraction-eligible**

---

**#66. NOK-NOK** | Default: 0 | Specialty: stealth / infiltration / chaos / goblin-adjacent
★ Being recognized as a real hero (not a goblin who got lucky)
Likes: recognition of bravery, goblin-friendly outcomes, chaotic success, tricks that actually work
Dislikes: being dismissed as just a goblin, left out of exciting missions, condescension
**Attraction-eligible**

---

**#16. TRISTIAN** | Default: 0 | Specialty: divine / undead / healing-heavy missions
★ Mercy and redemption — the possibility that people can be better
Likes: forgiveness, protecting the innocent, second chances, honest faith in practice
Dislikes: executions, cruelty, abandoning the helpless, cynical manipulation of hope
Not attraction-eligible (romance path available — see KM_Romance.md)

---

**#32. VALERIE** | Default: 0 | Specialty: combat leadership / defense / formal confrontations
★ Honor kept under pressure — commitments that hold when it costs something
Likes: lawful resolution, defending the weak with precision, commitments honored, fights won cleanly
Dislikes: deception as a strategy even when it works, chaos for its own sake, moralizing without action
**Attraction-eligible**

---

**#20. HARRIM** | Default: 0 | Specialty: darkness / entropy / dungeon-heavy / nihilism-adjacent
★ Honest acknowledgment of impermanence — he approves when the player recognizes futility
Likes: nihilistic philosophy, entropy, acknowledging failure as true, honesty about death
Dislikes: forced optimism, pretending decay can be stopped, cowardice dressed as caution
Not attraction-eligible

---

**#18. JAETHAL** | Default: 0 | Specialty: intimidation / undead encounters / noble intrigue
★ Being found genuinely interesting — philosophical alignment with death-positive choices
Likes: ruthlessness with elegance, dark philosophy, undeath, vengeance, noble manipulation
Dislikes: Tristian, Sarenrae, weakness through sentiment, anything that bores her
**Attraction-eligible** — dark-path conditions only (see Part B)

---

**#45. KALIKKE / KANERAH** | Default: 0 | Specialty: elemental / arcane / curse-related
Kalikke ★: Elemental balance; protecting the oppressed from systems that exploit them
Kalikke likes: diplomacy, healing, peace, considered choices
Kanerah ★: Power and conquest on their own terms
Kanerah likes: fire, gold, watching things burn, strength that doesn't apologize
Shared dislikes: being called a monster, pity, being separated, being treated as a single person
Kalikke and Kanerah track separately — `attraction_kalikke` and `attraction_kanerah`
**Both attraction-eligible** (see Part B)

---

**#84. OCTAVIA** | Default: 0 | Specialty: arcane / infiltration / anti-slavery missions
★ Freedom — destruction of oppression wherever it takes root
Likes: clever schemes, protecting the powerless from systems, banter returned with interest
Dislikes: slavers (visceral — this is a −2 trigger), rigidity, being talked down to, anyone who won't take a joke
**Attraction-eligible**

---

**#48. REGONGAR** | Default: 0 | Specialty: combat / intimidation / frontline magic
★ Being respected as a warrior who chose his path, not a slave who was shaped by someone else's
Likes: strength, directness, Octavia's safety, standing up to authority on principle
Dislikes: orders given like he's a soldier for hire, any slavery reference treated as casual, condescension toward Octavia
Not attraction-eligible (romance path available if player opens it)

---

**#10. LEM** | Default: 0 | Specialty: social / performance / morale / diplomatic missions
★ Art and inspiration having real, material power in the world
Likes: supporting performers, protecting artists, creative solutions over direct force, being recognized as more than background noise
Dislikes: dismissing art as decoration, cruelty to performers, anything Irovetti-adjacent
Not attraction-eligible

---

**#60. EKUNDAYO** | Default: 0 | Specialty: wilderness / tracking / ranger / gnoll-related
★ Justice for what was taken — grief turned into purpose
Likes: hunting monsters with a reason behind it, honest acknowledgment of loss, respecting the wilderness, directness
Dislikes: letting the guilty walk, dishonesty about grief, trolls or gnolls tolerated or allied
**Attraction-eligible**

---

**#13. SEELAH** | Default: +2 | Specialty: divine / protection / frontline / underdogs
★ Protecting those with less armor and less luck than she has
Likes: underdogs, honor practiced without performance, genuine warmth in difficult moments
Dislikes: cowardice hiding behind authority, cruelty to the helpless, using faith as a political shield
**Attraction-eligible**

---

**#19. KYRA** | Default: +1 | Specialty: healing / divine / Sarenrae / suffering relief
★ Bringing light into dark places — compassion practiced, not preached
Likes: healing without judgment, protecting the suffering, genuine kindness in practice
Dislikes: cruelty, exploitation of the vulnerable, violence that serves no one
**Attraction-eligible**

---

**#68. MERISIEL** | Default: 0 | Specialty: stealth / infiltration / assassination / rooftops
★ Surviving what should have killed her — competence earned the hard way
Likes: competence without ceremony, clever entry/exit, people who don't explain the obvious
Dislikes: moralizing mid-mission, inefficiency, anyone who needs to process their feelings before they act
**Attraction-eligible**

---

**#34. VALEROS** | Default: +1 | Specialty: sustained combat / holding the line / frontline
★ Good fights, good company — no complicated reasons required
Likes: straightforward combat, reliable allies, the next drink when it's earned
Dislikes: betrayal, complications that could have been avoided, people who make simple things hard
Not attraction-eligible

---

**#86. EZREN** | Default: 0 | Specialty: arcane knowledge / recall / research / lore missions
★ Truth pursued through honest methodology
Likes: intellectual rigor, precise answers, being treated as the expert he is, patience with complexity
Dislikes: sloppy thinking, fabrication, impatience that cuts corners
Not attraction-eligible

---

**#27. LINI** | Default: +1 | Specialty: wilderness / nature / animal handling / Droogami
★ Speaking for things that cannot speak for themselves
Likes: protecting natural places, treating animals as equals, quiet choices with large effects
Dislikes: exploitation of land or animals, cruelty, taking more than needed
**Attraction-eligible**

---

**#63. HARSK** | Default: 0 | Specialty: precision ranged / wilderness / giant hunts / oaths
★ Oaths kept — promises honored no matter the cost
Likes: keeping word under pressure, delivering justice, precision over raw force, anyone reliable
Dislikes: broken promises (permanent −1 if player breaks one — noted, not forgotten), cowardice, the guilty walking free
Not attraction-eligible

---

**#52. SAJAN** | Default: 0 | Specialty: mobile control / ki / frontline flexibility
★ Purposeful action — doing what needs doing without ego attached
Likes: decisive action, protecting the defenseless, choices made with clarity
Dislikes: cruelty that serves nothing, ego-driven decisions, hesitation when the moment is clear
Not attraction-eligible

---

**#1. JUBILOST NARTHROPPLE** | Default: −2 | Specialty: alchemy / wilderness mapping / ranged bombardment / Ch2+ only (quest-locked)
★ Competence proven through precision — thoroughness that doesn't cut corners
Likes: intelligence, respecting expertise, thoroughness, not wasting his time, data over instinct
Dislikes: ignorance, carelessness with information, "close enough" answers, anyone who navigates badly
**Attraction-eligible**
*Quest-locked Ch2. Default −2 reflects his baseline prickliness toward anyone he hasn't assessed yet. Rises quickly (to 0, then +) once the player demonstrates intelligence or precision.*

---

> **➡️ Companions 22+, Story NPC Profiles, Attraction System, Save Block Format, and Commands: KM_NPC_Relations_B.md**

---

*KM_NPC_Relations_A.md — Kingmaker PF2e Text Adventure | Opinion System Part A v1.0*
