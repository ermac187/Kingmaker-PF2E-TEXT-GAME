# KINGMAKER — NPC & COMPANION OPINION SYSTEM (PART B)
## KM_NPC_Relations_B.md | Continuation of KM_NPC_Relations_A.md
## Part B: WotR/Iconics companion profiles + Story NPC Profiles + Attraction System + Save Block + Commands
### Load BOTH parts every session alongside KM_Companions.md.

---

## 👥 COMPANION PROFILES — WotR, Iconics & Expansion

**Format:** Default Score | ★ Core Value | Likes | Dislikes | Specialty | Attraction

---

**#71. SEONI** | Default: 0 | Specialty: arcane blasting/sorcery/mobile magic
★ Understanding power that runs in her blood — on her own terms
Likes: arcane self-knowledge, freedom of movement, people who don't ask her to explain herself
Dislikes: being studied like a specimen, being asked to stay put, assumptions about sorcerers
**Attraction-eligible**

---

> **All companion numbers below use canonical IDs from KM_CompanionIndex.md.**

---

**#81. CAMELLIA** | Default: 0 | Specialty: spirit calling/social/animist
★ The spirits are real — and more reliable than most people
Likes: discretion, competence, being taken seriously beneath the polished surface
Dislikes: anyone who pries, emotional exposure, the mask questioned in public
**Attraction-eligible**

---

**#51. LANN** | Default: 0 | Specialty: monk/ranged/underground lore
★ Proving worth through results, not origin
Likes: direct action, people who judge by capability, honest acknowledgment of what's hard
Dislikes: pity, condescension about his ancestry, surface-world assumptions
Not attraction-eligible

---

**#33. WENDUAG** | Default: −1 | Specialty: archer/frontline/pragmatic combat
★ Survival — hers, on her terms
Likes: results over sentiment, strength respected, no pretense
Dislikes: weakness, idealism that costs others, being underestimated twice
Not attraction-eligible

---

**#67. WOLJIF** | Default: +1 | Specialty: rogue/social/arcane trickery
★ Making something real out of a legacy that was supposed to break him
Likes: being trusted despite the obvious reasons not to, clever exits, people who laugh with him
Dislikes: being written off, family discussed without permission, the con seen through before he's ready
**Attraction-eligible**

---

**#80. EMBER** | Default: +1 | Specialty: witch/curse/support
★ Using what was given to her to protect rather than consume
Likes: patience, gentleness that has teeth, people who see past the power to the person
Dislikes: being feared, her visions dismissed, anyone who wants the power without acknowledging the cost
**Attraction-eligible**

---

**#55. DAERAN** | Default: 0 | Specialty: oracle/healing/divine/social
★ Something underneath the boredom that actually cares — he doesn't discuss this
Likes: being surprised, people who don't perform for him, genuine competence
Dislikes: earnestness he finds hollow, being needed in ways that are boring, the mask cracked in public
**Attraction-eligible**

---

**#85. NENIO** | Default: 0 | Specialty: wizard/illusion/knowledge/research
★ The data is what matters — everything else is noise
Likes: interesting phenomena, precise questions, people who follow the logic
Dislikes: imprecision treated as personality, her research interrupted, emotional reasoning substituted for evidence
Not attraction-eligible

---

**#17. SOSIEL** | Default: +1 | Specialty: cleric/healing/support/Shelyn
★ People are worth believing in, even with evidence against it
Likes: kindness given without expectation, beauty found in hard places, faith defended quietly
Dislikes: cruelty for its own sake, beauty destroyed, hope treated as naivety
**Attraction-eligible**

---

**#62. GREYBOR** | Default: 0 | Specialty: ranger/monster slaying/contract work
★ The contract is the contract — honor it or don't hire him
Likes: clear terms, payment on delivery, people who don't make it personal
Dislikes: scope creep, sentiment in professional situations, being asked to care about the mission
Not attraction-eligible

---

**#23. REGILL** | Default: 0 | Specialty: commander/Hellknight/law/discipline
★ Order maintained through consequence — the law is the only honest thing
Likes: precision, accountability, people who follow through
Dislikes: excuses, chaos treated as freedom, mercy that enables the next offense
Not attraction-eligible

---

**#61. ARUESHALAE** | Default: 0 | Specialty: ranged/divine/wilderness/redemption
★ Goodness learned in practice — figuring out what it means, not performing it
Likes: genuine kindness without expectation, patience with uncertainty, choices that reduce suffering
Dislikes: being defined by what she was, cruelty treated as necessary, people who expect her to fall
**Attraction-eligible**

---

**#26. ULBRIG OLESK** | Default: 0 | Specialty: druid/wilderness/animal control/terrain/shifter
★ Remembering what was taken without letting grief become the only thing that's left
Likes: respect for the land, Sarkorian heritage acknowledged, actions that preserve rather than consume, people who understand loss without needing it explained
Dislikes: casual destruction of wilderness, Worldwound corruption treated as acceptable, Sarkorian culture discussed like a curiosity rather than a wound
Not attraction-eligible

---

**#7. TREVER** | Default: 0 | Specialty: frontline/barbarian/sustained pressure/endurance
★ Integrity beneath the performance — the man behind the smile that says everything is fine
Likes: people who see past the easy answer, honesty that doesn't make a scene of itself, fighting beside someone he has actually decided to trust
Dislikes: his history examined without permission, the smile mistaken for contentment, being asked to explain what he hasn't said
Not attraction-eligible

---

## 🏰 STORY NPC PROFILES

Named story NPCs carry Opinion Scores on the same system. Their score gates access to information, favors, political support, and unlocks.

---

**JAMANDI ALDORI** | Default: 0 | Role: Charter sponsor; Swordlord; political patron
★ Competence demonstrated under genuine pressure — not theater, actual results
Likes: political acumen, honoring commitments, directness over flattery, strength without cruelty
Dislikes: incompetence in front of her peers ★, political naivety, breaking given word, posturing without substance
**Score unlocks:** 6–10: She writes between chapters; political intelligence flows | 11–15: Publicly advocates for your kingdom in Brevoy; +1 Stability from Aldori backing | 16+: Offers Aldori sword tutor and private political alliance beyond the charter
**Automatic check:** Each chapter she reviews kingdom stats. Loyalty or Stability below 8 in consecutive turns: **−1**

---

**KASSIL ALDORI** | Default: varies (see flags) | Role: Jamandi's adopted half-orc son; Future General
`kassil_first_impression = positive` → Default +3 | `negative` → Default −2 | `neutral` → Default 0
★ Quiet competence respected — he was dismissed his whole life and has no patience for people who dismiss others
Likes: composure under pressure, people who handle situations without drama, directness, grace in difficult moments
Dislikes: recklessness that costs others, people who use Jamandi's name as a shield, anything that embarrasses the house
**Score unlocks:** 8+: Vouches for the player in political settings | 14+: Acts as personal military advisor; +1 to army-resolution checks | 18+: Commits troops to a single campaign cause the player names
**Vouching:** `kassil_first_impression = positive` → he vouches in Phase 5 Prologue automatically

---

**KESTEN GARESS** | Default: 0 | Role: Captain of Manor Guard; Future Warden
`kesten_respect = TRUE` → Default +2
★ Reliable professionalism — he respects people who do what they say and don't make his job harder
Likes: competence, not making scenes that force him to intervene, honoring the law's intent, clean resolutions
Dislikes: unnecessary complications, people who treat law as obstacle rather than structure, drama that spreads
**Score unlocks:** 6+: Shares guard patrol intel and local threat assessments | 12+: Provides advance warning of one random Ch event per chapter from his network | 16+: Commits his personal unit to one mission per chapter at no resource cost

---

**OLEG LEVETIN** | Default: +2 | Role: Trading post owner; supply hub
★ Keeping his word to the Stolen Lands community — and people keeping theirs to him
Likes: treating his post with respect, paying fair prices, bringing him news, asking after Svetlana
Dislikes: treating his post as a military requisition point ★, bullying guests or staff, failing to clear nearby threats
**Score unlocks:** 6–10: Flags incoming traders with good stock before arrival | 11–15: Restov contacts — one favor per chapter | 16+: Informal intelligence post; caravan news shared proactively

---

**SVETLANA LEVETIN** | Default: +3 | Role: Oleg's wife; community anchor
★ The people of the post remembered as people, not as furniture
Likes: kindness to travelers, asking after people by name, bringing news of the wider world
Dislikes: treating her home as an inn with no people in it ★, addressing her as staff, ignoring Oleg's distress
**Score unlocks:** 6–10: Trail provisions prepared at no cost once per chapter | 11–15: +1 to all Diplomacy at the post | 16+: Community organizer — Unrest −1 once per kingdom turn
**Note:** Not attraction-eligible — she is married and her score never generates attraction regardless of value.

---

**KRESSLE** | Default: −8 | Role: Bandit captain; Ch1 antagonist; potential turned ally
★ Strength without condescension — being acknowledged as good at what she did
Likes: respect from strength, fairness within the code she lives by, not being preached at
Dislikes: mercy that reads as pity ★, moralizing, being underestimated by someone who hasn't earned it
**Recovery:** Spared + treated without condescension → can recover toward 0. Will not exceed +5 without a dedicated conversation where the player earns her respect.

---

**AKIROS ISMORT** | Default: −5 (before turn) → +4 (immediately on defection) | Role: Stag Lord lieutenant; potential ally
★ Not being defined by the worst choice he ever made
Likes: acknowledgment that people can change, honor kept under pressure, not being lectured after he's already changed
Dislikes: being held to his past as a permanent label ★, cruelty after accepting his defection
**Post-defection:** Starts at +4 and rises faster than most. One of the fastest-rising NPCs once turned.

---

**BOKKEN** | Default: 0 | Role: Reclusive alchemist; merchant
★ Being left alone between visits — he likes being useful, not being socialized
Likes: fangberries brought without being asked again ★, quiet transactions, not discussing his brother
Dislikes: pressing his personal life, arriving empty-handed, mentioning his brother after he's asked you not to
**Score unlocks:** 6–10: Experimental stock mentioned before visit | 11+: One free potion batch left at post per chapter

---

**JUBILOST NARTHROPPLE** | Default: −2 | Role: Gnome scholar; Varnhold informant; Ch1+
★ Intellectual competence acknowledged — he respects being proven wrong by someone better
Likes: being treated as an expert, a good argument with better evidence, gnomish knowledge respected
Dislikes: condescension ★, being rushed, people who don't engage with his information
**Score unlocks:** 6+: Detailed Varnhold and regional maps and notes become available

---

**TARTUCCIO** | Default: −3 (charming surface; underlying hostility) | Role: Rival applicant; Pitax spy; Ch1 antagonist
★ He is assessing you — his opinion shifts on whether you are useful, a threat, or interesting to manipulate
Opinion score tracks under the surface. He will never show it deteriorating. He will use information you give him.
**Note:** His score declining does not change his surface behavior — he remains pleasant until Phase 5. Track internally.

**SABOTAGE SYSTEM** (see Stream 5, KM_NPC_Relations_A.md for full mechanics)

**Priority target list:**

| Priority | Target | His approach |
|----------|--------|-------------|
| 1st | **Jamandi** | Implies the player's competence is lucky, not reliable. Raises procedural concerns. |
| 2nd | **Companion with highest current score** | Reframes their bond as the player using them, not valuing them. |
| 3rd | **Companion from prologue split** | They're already uncertain — one comment keeps them uncertain. |
| 4th | **Any NPC the player just built rapport with** | "I'm sure it's nothing" before the moment can compound. |

**Prologue behavior:**
- Phase 1 (feast): One aside to the companion most recently left alone. Vague concern. Never accusatory.
- Phase 4.5 (wind-down): Two actions. First: doubt introduced to a companion post-positive-moment. Second: unsolicited "clarification" near Jamandi about something the player said.
- If `tartuccio_ring = equipped`: Glances at the player's hand during Phase 4.5, makes a visible note. Perception DC 12 to catch it. No budget cost — theater.

**Ch1 behavior:**
- If Tartuccio reached Oleg's before the player (Path B: Thorn Ford first): spent one action on Oleg. `tartuccio_oleg_seeded = TRUE` → Oleg starts at −1.
- After Ancient Tomb: recovered companions carry −1 residual. Clears on first Stream 1 gain with that companion.

**What he does NOT do:** Make accusations before Phase 5. Target NPCs at Strained or lower. Spend budget off-screen without a `tartuccio_[npc]_seeded` flag.

**Exposure:** `tartuccio_sabotage_exposed = TRUE` → all aware NPCs recover +1 immediately and his budget drops to 0 for the current scene.

---

## 🔥 ATTRACTION & ROMANCE INITIATION

> **DM:** Attraction is a natural outcome of high Opinion Score plus character-specific conditions. When conditions are met, the companion begins signaling through behavior — not announcement. The player still drives whether it becomes Romance. Companions show they're interested. The player decides what to do with it.

**Applicable characters (v59 roster):**

**Active 11 (default playthrough — all attraction-capable):**
Linzi (Bard), Goldmoon (Cleric), Tika Waylan (Fighter), Ryuko Matoi (Thaumaturge),
Morrigan (Witch), Sucrose (Alchemist), Artoria Pendragon (Champion),
Olivier Armstrong (Commander), Yoko Littner (Gunslinger), Kyoko Kirigiri (Investigator),
Tatsumaki (Psychic).

**Quest-locked CRPG (recruitable later — attraction-capable):**
Tristian, Octavia, Kalikke/Kanerah, Nok-Nok, Jubilost, Ekundayo +
Amiri (combat-earned path only), Jaethal (dark-path conditions only).

**Class-apex (off-roster, attraction-capable when recruited):**
Senua (Animist), Yang Xiao Long (Kineticist), Weiss Schnee (Magus),
Alleria Windrunner (Ranger), Imoen (Rogue).

**WotR legacy (attraction-capable for QL playthroughs):**
Arueshalae, Daeran, Ember. Svetlana NOT eligible — married.

**KM CRPG (active roster, attraction-capable):**
Valerie (#32).

**Section D cross-IP companions:** see `KM_NPC_Relations_C.md` Attract column.
Roughly half are eligible; C file lists Yes/No per companion.

Also eligible: Kassil (story NPC, attraction-capable if score reaches threshold and player has opened that path).

> **Jaethal:** Attraction-capable only if player has demonstrated death-positive or nihilistic choices across at least two chapters. She finds something interesting. It is not warmth.
> **Amiri:** Combat-earned only. Requires Opinion Score 14+ AND at least two scenes where the player proved physical or combat capability directly to her. Kindness alone doesn't register romantically.
> **Alleria:** Widow-coded in the active timeline (husband presumed dead, son Arator distant). Romance is not a replacement of the past. Treat her DC as +2 over the table for any player who tries to flatten that history.
> **Morrigan:** Anti-chain by core value. Stage 3 DC 20 reflects this. Player who attempts to "tame" her romance arc gets one warning line, then the romance closes permanently.

---

### ATTRACTION THRESHOLD

A character becomes attraction-flagged (`attraction: true`) when:

1. Opinion Score reaches **+12 or higher** (Valerie-tier characters: **+14**), AND
2. At least **two** of the following are true:
   - Player has had at least one Camp Interlude or equivalent private moment
   - Player acted in alignment with this character's ★ Core Value in a meaningful scene
   - Player has defended this character personally (socially, not just tactically)
   - Player remembered a personal detail from a previous scene and acted on it

**Once flagged:** Behavior shifts. The DM applies this silently — no notification. The player reads it in narration.

---

### ATTRACTION → ROMANCE WINDOW

Once attraction-flagged, the companion generates **passive romance pressure** — charged Camp Interludes, questions with more than one answer, moments the player can press or let pass.

**Window rule:** If the player does not act across **three consecutive triggered moments**, the companion files it away. Score stays. Window closes. Reopens if circumstances change significantly (major shared ordeal, completed personal quest, etc.)

**Transition to Romance:** Player explicitly responds to a charged moment rather than deflecting → Romance track opens at Stage 1. See KM_Romance.md for all subsequent mechanics.

---

### ATTRACTION BEHAVIORAL SIGNATURES

**Linzi:** Starts writing about the player differently. The narrator's distance collapses. She edits when she notices them watching.

**Valerie:** Corrects the player's combat form when she doesn't need to. Explains it as tactical. It isn't.

**Octavia:** A pause appears in her deflections that wasn't there before. She checks if her jokes landed — the real version.

**Kalikke:** Asks what the player does when something can't be fixed. Listens to the whole answer.

**Kanerah:** Tests the player. Provocations with a smile. Makes professionally appropriate offers phrased exactly wrong.

**Amiri:** Challenges the player to a spar — picks them specifically. If they hold their own, something in her expression changes.

**Jaethal:** Becomes curious — a more focused version of her cold interest. Says something private about death that is a confidence, not a lecture. *"You are not boring."*

**Seelah:** Gets warmer. Not more — warmer. Starts checking whether the player is okay after fights before checking anyone else. Doesn't explain it.

**Kyra:** Prays near the player in quiet moments. Not at them — near them. Starts leaving small offerings after difficult days. Asks how they sleep.

**Merisiel:** Shows the player routes she takes that no one else knows about. Lets them in on small things — where she stashes her kit, which roof she prefers. These are private facts.

**Arueshalae:** Asks what the player thinks goodness looks like in practice. Keeps coming back to the answer. Uses it as a reference when she's uncertain.

**Woljif:** Tests the player in a different way than most — he jokes until the joke lands differently. Notices the player noticed. Moves on. Comes back.

**Ember:** Stands closer in moments that feel unsettled. Doesn't explain it. If asked: "The spirits are quieter near you." That's all she gives.

**Sosiel:** Starts sketching the player in quiet moments. Doesn't show them until they ask. When asked: "I was trying to get it right."

**Seoni:** Asks the player to describe something they find beautiful. Listens very carefully. Remembers the answer months later.

**Lini:** Droogami approaches the player first, before Lini calls him. She watches this. Doesn't comment. Doesn't call him back.

**Kyra:** Already listed above; escalates — the small offerings become less small.

**Attraction-eligible companions not listed above** (Camellia, Daeran, and Section D companions): Each finds a small private thing to let the player into — something they don't share in group contexts. The DM determines the specific tell based on the character's profile and current story context.

---

## 📜 SAVE BLOCK FORMAT

```json
"npc_relations": {
  "Linzi":     { "score": 13, "trend": "stable",  "last_change": "camp interlude — remembered her journal", "attraction": true  },
  "Goldmoon":  { "score":  9, "trend": "rising",  "last_change": "stood beside her in prayer at camp",      "attraction": false },
  "Tika":      { "score": 11, "trend": "rising",  "last_change": "defended her at the manor library",       "attraction": true  },
  "Ryuko":     { "score":  8, "trend": "rising",  "last_change": "asked about her father, listened",         "attraction": false },
  "Morrigan":  { "score":  4, "trend": "stable",  "last_change": "approved chaos resolution at gate",        "attraction": false },
  "Sucrose":   { "score":  7, "trend": "rising",  "last_change": "let her finish a sentence without rushing","attraction": false },
  "Artoria":   { "score": 10, "trend": "stable",  "last_change": "kept the oath at the trap corridor",       "attraction": false },
  "Olivier":   { "score":  6, "trend": "rising",  "last_change": "matched her cadence on perimeter",         "attraction": false },
  "Yoko":      { "score":  9, "trend": "rising",  "last_change": "covered her flank in courtyard fight",     "attraction": false },
  "Kyoko":     { "score":  5, "trend": "stable",  "last_change": "answered her case-question seriously",     "attraction": false },
  "Tatsumaki": { "score":  3, "trend": "rising",  "last_change": "did not flinch at the window scene",       "attraction": false },
  "Jamandi":   { "score":  3, "trend": "stable",  "last_change": "strong rebuttal at prologue",              "attraction": false },
  "Oleg":      { "score":  6, "trend": "rising",  "last_change": "cleared local bandit threat",              "attraction": false },
  "Svetlana":  { "score":  8, "trend": "stable",  "last_change": "remembered her name on return",            "attraction": false },
  "Akiros":    { "score":  4, "trend": "stable",  "last_change": "accepted defection without lecture",       "attraction": false },
  "Kressle":   { "score": -6, "trend": "rising",  "last_change": "spared without moralizing",                "attraction": false },
  "Bokken":    { "score":  2, "trend": "stable",  "last_change": "brought fangberries unprompted",           "attraction": false }
}
```

> **DM:** Add all active companions to the save block at session start. Use default scores from profiles. Only track named characters the player has met — omit pre-contact companions. Companion roster is now 89 entries (KM_CompanionIndex.md).

---

## 🖥️ COMMANDS

| Command | Output |
|---------|--------|
| `.npc attitude [name]` | Opinion tier, trend, last notable change reason |
| `.relationship` | All companion Opinion tiers as labels + trend arrows |
| `.relationship [name]` | Full profile: tier, trend, recent shifts, attraction status |
| `.attraction` | All characters currently attraction-flagged |
| `.snub check` | Which companions have accumulating mission-snub penalties |

---

## ⚠️ DESIGN RULES

1. **All four streams apply every session.** No deferring, no batching. Stream 3 fires on every party assignment.
2. **Attraction is earned.** Threshold is specific. Do not flag early as a narrative gift.
3. **Snubbed companions show it — they don't announce it.** Tone, brevity, a pointed question. Never a speech.
4. **The player leads romance. The companion leads attraction.** The companion signals; the player acts. This boundary is firm.
5. **NPCs are full participants.** Jamandi reacts to kingdom stats. Oleg reacts to how his post is treated. Bokken reacts to whether the fangberries came.
6. **Trend matters as much as score.** A character at +14 and falling is already unhappy. A character at +5 and rising is warming fast. Narrate direction, not just position.
7. **Never report the raw number.** Tier labels and trend only. Internal tracking only.

---

*KM_NPC_Relations_B.md — Opinion System Part B v2.0*
