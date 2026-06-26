# KINGMAKER — FOUND DOCUMENTS SYSTEM
## KM_Documents.md | Active from: Chapter 1 | Referenced by: KM_Exploration.md, KM_Loot.md

> **DM:** Load this file when the player searches bodies, desks, bookshelves,
> chests, ruins, or any location that could plausibly contain written material.
> Found Documents are readable items — journal pages, letters, proclamations,
> field notes, lists, confessions. They are not loot in the mechanical sense.
> They go into `found_documents[]` in the save block, not `inventory[]`.
> They can be given to the Storyteller (some qualify), read at any time, or
> ignored entirely. The player is never required to engage with them.

---

## 📜 HOW FOUND DOCUMENTS WORK

```
DISCOVERY TRIGGER
  When the player searches an area with written materials, the DM checks:
    Does this location plausibly have documents? (desk, body, bookshelf, chest)
    → YES: Roll d6.
         1–2: Nothing readable (destroyed, illegible, irrelevant)
         3–4: One document (roll on table for current chapter)
         5  : Two documents
         6  : One document + it has additional value (Storyteller, lore flag, or
              quest-relevant — DM notes this quietly; doesn't announce special status)
    → NO: Skip.

  EXCEPTION — SCRIPTED DOCUMENTS: Named NPCs' desks and specific scripted
  locations always contain their listed documents regardless of the d6 roll.
  See the Scripted Documents section below.

READING A DOCUMENT
  Takes 1 minute (exploration mode) or 1 action (social mode, skimming).
  Full reading unlocks any lore flags attached to the document.
  Player may read aloud or summarize to companions — this counts as a
  Storytelling camping activity (C16) if done at camp.

STORYTELLER ELIGIBILITY
  Documents marked [STORYTELLER] can be brought to the Storyteller in the
  capital. He reads them, comments, and awards XP + minor lore advancement.
  He does not pay gold for documents — only for Relic Fragments and coins.
  XP award: 50 XP per Storyteller document (maximum once per document).

FORGERY USE
  Any found document with an official seal or signature can be used as a
  template for the Create Forgery downtime action (D5), reducing its DC by 4.
```

---

## 📋 DOCUMENT TABLES BY CHAPTER

### Chapter 1 — The Stolen Lands

**Roll d10 when a document is indicated:**

| d10 | Document | Location Type | Content Summary | Special |
|-----|----------|--------------|-----------------|---------|
| 1 | **Bandit Watch Schedule** | Bandit camp desk | Guard rotations, shift changes, patrol routes. Tactical. | −2 DC to Stealth vs this camp's guards this session |
| 2 | **Extortion Ledger** | Bandit chest | List of farms and travelers paying "protection." Names, amounts, dates. | Evidence usable to help any named victim; Reputation +1 if delivered |
| 3 | **Stag Lord's Orders (fragment)** | Senior bandit body | Partial orders from the Stag Lord — territory, targets, what to avoid. Mentions Thorn River. | `stag_lord_intel_partial = TRUE` |
| 4 | **Prospector's Notes** | Wilderness ruin | A dead man's survey of the hex. Marks a nearby stream, a stone formation, and something he didn't understand. | Reveals 1 adjacent hex terrain type |
| 5 | **Farmer's Plea** | Abandoned farmhouse | A letter never sent — begging Restov for help with the bandits. | Storyteller eligible. +1 Reputation in Stolen Lands if player acts on it |
| 6 | **Kobold Trade List** | Sootscale den | A list of items the Sootscale kobolds want to trade. Crude, misspelled. Nok-Nok can read it. | Opens barter option with Sootscales even if diplomacy failed |
| 7 | **Old Map (partial)** | Any ruin | A hand-drawn map — inaccurate, decades old. One landmark still matches something real. | Reveals 1 fixed encounter location on current hex cluster |
| 8 | **Wanted Poster (self)** | Bandit camp | The player's description — pulled from bounty hunters' intel. Poorly drawn. | Linzi insists on keeping it. +1 Morale if shown to party |
| 9 | **Moon Radish Recipe** | Kobold den or farmhouse | Someone was trying to make something from moon radishes. Annotated enthusiastically. | Unlocks one additional special camping recipe (Cooking Lore DC 14) |
| 10 | **Tartuccio's Note (fragment)** | Any bandit officer's body | A message from "T" — payment confirmation, vague orders, a name redacted. | [STORYTELLER] `tartuccio_network_partial = TRUE` |

---

### Chapter 2 — The Stolen Lands Expands

**Roll d10:**

| d10 | Document | Location Type | Content Summary | Special |
|-----|----------|--------------|-----------------|---------|
| 1 | **Troll Den Markings** | Hargulka's territory | Crude symbols — territorial claims, prey directions, "KEEP OUT" in Giant. Nature DC 14 to interpret. | −2 DC to Survival checks tracking trolls in this hex |
| 2 | **Merchant's Invoice** | Abandoned wagon | A shipping manifest. Goods that never arrived. One line is crossed out and marked "seized." | Evidence of bandit economic operation; usable for Gather Information |
| 3 | **Kingdom Charter (rival)** | Bandit fort office | A forged charter — someone else tried to claim this territory. Old. Predates the player. | [STORYTELLER] `rival_charter_found = TRUE` |
| 4 | **Bloom Field Notes** | Researcher's body | A naturalist's observations of the Bloom. Clinical. Gets increasingly alarmed. Last entry mid-sentence. | `bloom_researcher_notes = TRUE`; Tristian asks to read it |
| 5 | **Letter from Home** | Any soldier body | A personal letter to a bandit — from a sister, asking him to come home. He never will. | No mechanical effect. Linzi reads it at camp if given to her. Bond Moment eligible. |
| 6 | **Old Beldame's Recipe** | Swamp area | A recipe on bark — not for food. Herbalism. Foul-smelling components. | Usable with Hunt and Gather to find specific ingredient; leads toward Old Beldame if not yet met |
| 7 | **Defaced Proclamation** | Settlement ruin | A kingdom proclamation — defaced with knives. "NO RULERS HERE" scratched over the seal. | Shows local resistance; Loyalty −1 in that hex's region unless addressed |
| 8 | **Bokken's Shopping List** | Oleg's area | Bokken's handwriting — a list of alchemical components he needs. Very specific. Very strange. | Delivering all components unlocks one Bokken discount (−20%) |
| 9 | **Patrol Log** | Guard post | Someone kept meticulous logs of what moved through this hex. Months of entries. Stops suddenly. | `hex_patrol_log = TRUE`; +1 to Survival tracking in this hex |
| 10 | **Letter to Irovetti** | Senior bandit body | Unsigned. Reporting on the player's kingdom progress. The language is careful. | [STORYTELLER] `irovetti_surveillance_found = TRUE`; Octavia wants to examine it |

---

### Chapter 3 — Varnhold

**Roll d8:**

| d8 | Document | Location Type | Content Summary | Special |
|----|----------|--------------|-----------------|---------|
| 1 | **Varnhold Census (partial)** | Town hall | A population register — 312 names. All crossed out in red. One page torn away. | [STORYTELLER] `varnhold_population_documented = TRUE` |
| 2 | **Varnhold Regent's Journal** | Regent's study | Personal entries — kingdom building, optimism, then growing unease. Final entry: "They are watching from the stones." | `regent_journal_found = TRUE`; Linzi reads it silently at camp |
| 3 | **Willas Gunderson's Field Notes** | Ruins or body | Academic notes on cyclops ruins. Becomes excited about an amulet. Last note: "Must show the regent." | `gunderson_notes = TRUE`; reduces Recall Knowledge DC vs Vordakai by 4 |
| 4 | **Centaur Warning (carved)** | Standing stone | Not paper — carved symbols on a stone marker. Nature DC 16 or Kellid Lore DC 12 to read: "Do not wake the stone eye." | `centaur_warning_found = TRUE` |
| 5 | **Colonist's Last Letter** | House or body | A letter someone started writing when things went wrong. Incomplete. They knew something was coming. | [STORYTELLER]. +50 XP. Morale −1 (the party reads it) |
| 6 | **Military Manifest** | Varnhold barracks | Equipment list, patrol assignments, emergency procedures. Normal. Professional. For a town that no longer exists. | Provides tactical layout of Varnhold's defenses (useful if player fortifies it) |
| 7 | **Cyclops Inscription (translated)** | Tomb antechamber | A rubbing of wall text with a partial translation. "The one who drinks eyes remembers all it takes." | [STORYTELLER] `vordakai_inscription_found = TRUE`; +1 to Occultism checks inside tomb |
| 8 | **Soul Jar Registry** | Vordakai's chamber | A list — Vordakai's accounting of souls collected. Varnhold names, including the regent's. | `soul_jar_registry = TRUE`; reduces regent rescue DC by 2 |

---

### Chapter 4 — Tiger Lords & Politics

**Roll d8:**

| d8 | Document | Location Type | Content Summary | Special |
|----|----------|--------------|-----------------|---------|
| 1 | **Armag's Decree** | Tiger Lord camp | A proclamation in Kellid. Amiri can read it. Armag is challenging all living warriors to prove themselves. | Amiri's reaction is significant — DM runs 2-line ambient beat |
| 2 | **Pitax Funding Ledger** | Tiger Lord officer body | Payment records — Pitax gold, Tiger Lord services. Dated. Specific. | `pitax_tiger_lord_funding = TRUE`; +2 to Diplomacy with River Kingdoms re: Irovetti |
| 3 | **River Baron's Letter** | Courier body | A baron withholding trade from the player's kingdom — the letter explains why (Irovetti paid him). | Confronting the baron with this: Diplomacy DC 14 instead of 22 |
| 4 | **Coronation Planning Notes** | Capital archive | Someone (a councilor) has been drafting coronation options. Three political paths outlined. | Preview of coronation choice; no mechanical effect — player reads the options |
| 5 | **Irovetti's Threat Letter** | Captured courier | Irovetti's personal threat to a minor lord — florid, operatic, and very specific. | [STORYTELLER] `irovetti_threat_letter = TRUE`; +1 to Diplomacy with anti-Pitax factions |
| 6 | **Kellid Saga Fragment** | Armag's Tomb | Ancient verse — the story of Armag the First. Difficult to read without Kellid Lore DC 16. | Amiri translates it. Bond Moment eligible. `armag_lore_known = TRUE` |
| 7 | **Spy's Report (about player)** | Pitax agent body | A detailed intelligence report on the player's kingdom — accurate, well-observed, slightly wrong about one thing (DM decides what). | Gives the player a sense of what Irovetti knows |
| 8 | **Old Kingdom Charter** | Capital archive | A charter from a prior kingdom attempt in this territory — decades old. Failed. The reasons are instructive. | [STORYTELLER] `old_kingdom_charter = TRUE`; +1 to next kingdom event resolution check |

---

### Chapters 5–7 (Pitax, Thousandbreaths, House at Edge of Time)

**Roll d6:**

| d6 | Document | Location Type | Content Summary | Special |
|----|----------|--------------|-----------------|---------|
| 1 | **Irovetti's Private Diary** | Palace study | A ruler's journal — paranoid, brilliant, self-justifying. The last entry is about the player. | [STORYTELLER] `irovetti_diary = TRUE`; Linzi asks to publish an excerpt |
| 2 | **Nyrissa's Letter (fragment)** | Thousandbreaths | Torn. In her hand. To someone she calls "the only one who tried." Not the player — someone before. | `nyrissa_prior_contact = TRUE`; deepens true ending thread |
| 3 | **Lantern King's Compact** | House at Edge of Time | The original agreement that cursed Nyrissa. In fey script — Occultism DC 22 to read. | [STORYTELLER] `lantern_king_compact_found = TRUE`; `nyrissa_backstory_known = TRUE` if not already |
| 4 | **First Kingdom Record** | House at Edge of Time | A complete record of the kingdom Nyrissa destroyed — its name, its ruler, what they built. | Enormous lore. Storyteller gives maximum XP for this. +1,000 XP |
| 5 | **Irovetti's War Plans** | Palace war room | Detailed military plans — troop movements, siege timelines, contingencies. | +2 to all army Warfare checks for 2 turns |
| 6 | **Guard's Last Note** | Pitax barracks | A guard's note to his family. Not important. He was just a man doing a job. | No mechanical effect. Tristian asks the player what they want to do about it. |

---

## 📌 SCRIPTED DOCUMENTS (Always present — no d6 roll required)

These documents exist at fixed locations and are found automatically when the player searches that specific area.

| Document | Fixed Location | Content | Flag Set |
|----------|---------------|---------|----------|
| **Tartuccio's Manifesto** | Old Sycamore — Tartuccio's desk | His plans, grievances, and what he intends to do with the Stolen Lands. Theatrical. | `tartuccio_manifesto_found = TRUE` |
| **Stag Lord's Wanted Poster** | Thorn River Camp | The original charter bounty. His face. The 15,000 gp reward. Oleg's seal at the bottom. | `stag_lord_wanted_poster = TRUE` |
| **Bokken's Alchemy Notes** | Bokken's hut | His working notes — partially coded, partially legible. Contains one viable recipe. | Unlocks Bokken Recipe (DM selects appropriate tier) |
| **Svetlana's Ring Note** | Oleg's — Oleg's desk | A note to himself: "Find the ring. She never asks. She shouldn't have to." | Directly triggers the Svetlana's Ring quest if not already active |
| **Varn's Last Dispatch** | Varnhold town hall | The final official report Varnhold sent before silence. Professional. Slightly worried. Signed. | `varn_last_dispatch = TRUE`; Jamandi reference — she received this |
| **Irovetti's Confession** | Pitax palace vault | A sealed document — his account of every law he broke, every person he had removed. Written for posterity. Damning. | [STORYTELLER] `irovetti_confession = TRUE`; +2 to all River Kingdom diplomacy post-Ch5 |

---

## 💾 FOUND DOCUMENTS SAVE BLOCK

```json
"found_documents": [
  {
    "id": "bandit_watch_schedule",
    "name": "Bandit Watch Schedule",
    "chapter": 1,
    "location": "Thorn River Camp",
    "read": true,
    "given_to_storyteller": false,
    "flags_set": [],
    "notes": ""
  }
]
```

---

## 🖥️ DOCUMENT COMMANDS

| Command | Output |
|---------|--------|
| `.documents` | Full list of found documents: name, chapter, read status, Storyteller eligibility |
| `.read [name]` | Read a specific document — DM narrates its contents |
| `.documents unread` | Only unread documents |
| `.documents storyteller` | Only Storyteller-eligible documents |

---

## ⚠️ DESIGN RULES FOR THE DM

1. **Documents are flavor with teeth.** They are not required reading. But the player who reads them gets information, lore flags, and the occasional mechanical edge. Reading is rewarded, not demanded.
2. **Read aloud when asked.** When the player reads a document, the DM narrates it as written text — brief, in-world, in the voice of whoever wrote it. Not a summary. The actual text.
3. **Companions react to significant documents.** Not every time — but a journal from a dead man, a letter from Irovetti, Nyrissa's handwriting. One companion notices. One line. That's enough.
4. **The Storyteller is not a document dump.** He takes Storyteller-eligible documents and responds with something specific and quiet — one sentence, then silence. He does not explain himself further.
5. **Documents decay.** A document found in a burned building is partial. In a flooded ruin, it's barely legible. The DM applies condition logic — only pristine finds yield complete content.

---

*KM_Documents.md — Kingmaker PF2e Text Adventure | Found Documents System v1.0*
*All document content is original to this project. Integrates with: KM_Exploration.md (Storyteller), KM_Kingdom.md (Bond Moments), KM_World_Systems.md (Forgery templates), KM_Actions.md (D5 Create Forgery, D23 Research)*


---

<!-- merged from KM_Documents.md (v93.21 file consolidation) -->

# KINGMAKER — HANDOUTS
## KM_Documents.md | In-Game Documents, Letters, and Objects

> **DM:** When a player finds any document listed here, output the HANDOUT VERSION
> first — formatted as the actual document, in the writer's voice — THEN provide
> mechanical context on a separate line.
>
> Format: Output the handout in a box, then below it: `[Mechanical note: ...]`
>
> Read documents aloud in the voice of the writer. Nyrissa's letters sound like Nyrissa.
> Tartuccio's notes sound like Tartuccio. These are objects, not descriptions of objects.

---

## 📜 HANDOUT FORMAT

```
╔══════════════════════════════════════════════════════════╗
║  📄 [DOCUMENT TITLE]                                     ║
║  Found: [Location]                                       ║
╠══════════════════════════════════════════════════════════╣
║  [Document text — formatted as the actual document]      ║
╚══════════════════════════════════════════════════════════╝
[Mechanical note: what this does in the game]
```

---

## JAMANDI'S CHARTER (Prologue → Ch1)

```
╔══════════════════════════════════════════════════════════╗
║  📄 CHARTER OF EXPLORATION AND SETTLEMENT               ║
║  Sealed with the Aldori crest — silver on black          ║
╠══════════════════════════════════════════════════════════╣
║  By authority granted to Jamandi Aldori, Swordlord of   ║
║  Restov, under the laws of Brevoy:                       ║
║                                                          ║
║  The bearer of this document is hereby empowered to      ║
║  explore, pacify, and if conditions allow, settle the    ║
║  lands south of Restov known as the Stolen Lands.        ║
║                                                          ║
║  The bearer shall have authority to establish order      ║
║  as they see fit, recruit companions, and act in the     ║
║  name of this Charter against any who would oppose       ║
║  the lawful settlement of these lands.                   ║
║                                                          ║
║  This Charter expires if the Stolen Lands remain         ║
║  unclaimed after 90 days from date of issue.             ║
║                                                          ║
║  — Jamandi Aldori, 15 Gozran 4710 AR                    ║
╚══════════════════════════════════════════════════════════╝
```
`[Mechanical note: Quest item — required to found the kingdom. 90-day time limit begins at prologue end.]`

---

## MALAK'S BRIBE PARCHMENT (Pre-Prologue, found on Malak's person)

> **DM:** This is a three-part operational document. Output all three sections as a single handout when found. The document is written in clipped, bureaucratic language — someone who does this professionally. No signature. No crest. Coded but not encrypted — a reader with Society DC 12 can infer the sender's origin from the parchment quality and ink (Pitaxian manufacture).

> **⛔⛔⛔ VERBATIM-RENDERING MANDATE — THE PARCHMENT HANDOUT BELOW IS THE AUTHORITATIVE TEXT ⛔⛔⛔**
>
> When this handout fires, the DM renders the bordered box EXACTLY as written below — same content, same line items, same gold amounts, same structure. NO augmentation, NO substitution, NO fabrication.
>
> **Banned modifications (each is `.fail 9` + `.fail 2`):**
> - **Augmenting names with descriptions.** Banned: *"Amiri (barbarian, large woman, Kellid markings)"* / *"Harrim (dwarf, heavy armor, grim)"* / *"Valerie (knight, full plate, noble bearing)"* / *"Jaethal (elf, white hair, pallid)"*. Canon = names only, NO parentheticals, NO physical descriptions, NO role tags. The parchment is a bribe document, not a Bestiary entry.
> - **Inflating gold amounts.** Banned: 150 / 200 / 300 per companion (10× the canon). The canonical figures are the ones in the box: 15 / 10 / 20 / 20 gp turned away (per the companion lines), double for arrested, 20-40 gp per seeker arrested. The contract is non-lethal per v95.6 ("No lethal action authorized"); NO kill-bounty rates exist in this document. Inserting "triple for killed" / "200 gp charter candidate killed" / "500 gp Jamandi killed" = fabrication of v95.5-era stripped content.
> - **Dropping line items.** Banned: omitting the completion bonus 100 gp line, omitting the "No lethal action authorized" clause, omitting the seekers section, omitting Section III, omitting the "Total funds enclosed: 180 gp" line, omitting the destroyed-staff-slip reference. Every line in the box must appear.
> - **Inserting kill-bounty lines removed in v95.6.** Banned: rendering "Jamandi Aldori .... 500 gp", "Charter candidate .... 200 gp", "Killed / confirmed dead" section header, "triple above rate" line. These were stripped in v95.6 because they contradicted Malak's despair-line canon ("I didn't think anyone would get hurt") and the compartmentalized-contract framing. Their reappearance in any rendered handout = `.fail 9` + `.fail 10` (silent retcon of stripped canon).
> - **Substituting amounts from `KM_Prologue_Systems.md` § MALAK'S PARCHMENT.** That file's directive-template version has DIFFERENT figures (5 / 20 / 50 uniform; 80 gp directive bonus; 10 gp per worker). The DM may NOT mix figures between files. The KM_Documents.md version below is the SOLE authoritative rendering. The KM_Prologue_Systems.md version is operational detail for DM reference, not for player rendering. (Conflict between the two files is noted; KM_Documents.md wins on render.)
> - **Fabricating Sections IV+.** The parchment has exactly THREE sections (I gate duty, II guest disposition, III manor staff). No invented Section IV. No appendix. No "addendum slip" except the destroyed names slip referenced in Section III.
> - **Editorializing within the parchment.** No "(note: this means…)" inline. No DM commentary inside the bordered box. The box is pure document.
>
> **The handout below renders verbatim, including the box drawing characters and the spacing.** When the player examines the parchment, output the box and only the box. Jamandi's scripted reaction line fires AFTER the box renders, NOT inside it.
>
> **Seeker slots:** `[seeker_1 name]` through `[seeker_5 name]` are placeholders. Fill them from the player's chosen seekers in the save block (`companions_selected` or equivalent). If save block has 5 chosen seekers, render their actual names at 20-40 gp each (pick one figure in the band per seeker, hold it). If save block has fewer than 5, render the slots that exist; do NOT invent additional seekers to fill the line.

```
╔══════════════════════════════════════════════════════════════╗
║  📄 UNMARKED PARCHMENT — folded twice, plain wax seal        ║
║  No crest. No name. Written in a careful mercantile hand.    ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  SECTION I — GATE DUTY (Evening of the 15th)                 ║
║                                                              ║
║  You are to position your detail no closer than 30 paces     ║
║  from the gate. Conduct your searches in the road.           ║
║  The gate must remain passable at the hour noted below.      ║
║  Those who pass through it during that window are not        ║
║  your concern. Your concern is everyone before it.           ║
║                                                              ║
║  Payment for gate duty: 40 gp upon confirmation.            ║
║  Confirmation method: leave the east lantern unlit.          ║
║                                                              ║
║  ──────────────────────────────────────────────────          ║
║                                                              ║
║  SECTION II — GUEST DISPOSITION                              ║
║                                                              ║
║  The following names appear on the Aldori invitation list.   ║
║  Rewards are per individual, per outcome, paid on receipt    ║
║  of a written incident report submitted to the drop point.   ║
║                                                              ║
║  Turned away / refused entry:                                ║
║    Amiri ............................... 15 gp              ║
║    Harrim .............................. 10 gp              ║
║    Valerie ............................. 20 gp              ║
║    Jaethal ............................. 20 gp              ║
║                                                              ║
║  Arrested / detained (minimum one night):                    ║
║    Any name above ...................... double above rate    ║
║    [seeker_1 name] ..................... [20–40 gp]          ║
║    [seeker_2 name] ..................... [20–40 gp]          ║
║    [seeker_3 name] ..................... [20–40 gp]          ║
║    [seeker_4 name] ..................... [20–40 gp]          ║
║    [seeker_5 name] ..................... [20–40 gp]          ║
║                                                              ║
║  Completion bonus — all listed names processed:              ║
║    (turned away or held through the ceremony)                ║
║    Bonus on full execution .............. 100 gp             ║
║                                                              ║
║  NOTE: No lethal action authorized in this contract.         ║
║  Resistance is to be answered with restraint, fabricated     ║
║  warrants, or City Watch handoff. Deaths invite investigation║
║  the operation cannot absorb. This rule is not negotiable.   ║
║                                                              ║
║  ──────────────────────────────────────────────────          ║
║                                                              ║
║  SECTION III — MANOR STAFF                                   ║
║                                                              ║
║  Three candidates have been placed in the applicant pool     ║
║  for manor serving staff. Their names are on the attached    ║
║  slip (destroy after reading). Approve all three without     ║
║  further inquiry. They carry valid papers.                   ║
║                                                              ║
║  Do not make contact with them yourself.                     ║
║  Do not acknowledge them if you see them at the manor.       ║
║                                                              ║
║  Payment for staff placement: 60 gp upon confirmation.      ║
║  Confirmation method: same drop point as above.              ║
║                                                              ║
║  ──────────────────────────────────────────────────          ║
║                                                              ║
║  Total funds enclosed in this delivery: 180 gp               ║
║  Remainder due upon confirmation of completed duties.        ║
║                                                              ║
║  Do not keep this document.                                  ║
║                                                              ║
║                                                   — C.       ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

`[Mechanical note: Critical story item. Three threat vectors in one document — but`
`note the COMPARTMENTALIZATION: Malak's contract is non-lethal by explicit clause.`
`SECTION I explains why Malak is 30 paces from the gate — he is holding that position to`
`screen arrivals while leaving the gate clear for agents entering behind them.`
`SECTION II is an interception contract, NOT an assassination contract. Pitax`
`deliberately keeps Malak in the dark about the lethal plot so he retains plausible`
`deniability if captured. The actual assassination (Jamandi target, charter candidate`
`target) is run by SEPARATE operatives whose contract Malak has never seen. This is`
`why Malak's despair line "I didn't think anyone would get hurt" rings TRUE — per`
`his contract, nobody was supposed to. The poison plot in SECTION III's manor staff`
`is the operational pivot: those placed staff are the assassins' inside agents, not`
`Malak's. Malak knows he's approving people without vetting; he does NOT know they`
`are poisoners. The compartmentalization is intentional spycraft and protects the`
`character integrity of Malak's "broken man who facilitated more than he understood"`
`arc.`
`SECTION III confirms spies are placed in Jamandi's serving staff — triggers the`
`poison plot in KM_Prologue_Systems.md. Staff name slip is absent (Malak destroyed it).`
`⛔ THE 3 PLACED STAFF ARE ALREADY GONE — "find them" is a DEAD END, not a hunt. This`
`document is the SETUP (a pre-feast placement order), NOT a present-tense roster. The 3`
`are one-night disposables: their only job is to plant the poison, and they LEAVE THE`
`INSTANT IT IS PLANTED — planting and departure are the same beat, out the service routes,`
`no lingering. There is never a window in which they are present to catch. So by the time the player reads this and`
`says "let's find these 3 staff / look for the new serving hands / the red cords," the`
`workers are already gone — slipped out, no name kept (the slip is destroyed), no one`
`left to catch. The honest outcome is FAST confirmation of the METHOD (placed`
`disposables, Pitax tradecraft) and it ENDS there. Do NOT render a catchable placed`
`server still working the hall, do NOT stage a catch-them-before-they-flee beat, do NOT`
`invent a lingering poisoner — that is .fail 9 (fabricated trail / wild goose chase). The`
`"do not acknowledge them if you see them" line is the handler's caution to MALAK at`
`approval time, NOT evidence they are present at the feast. Full canon: KM_Prologue_Systems.md`
`§ "WHY THE 3 STAFF ARE ALREADY GONE" + KM_Malak_Jail.md red-cord rule. Productive thread`
`= kitchen contamination check → Bokken identifies → Ezvanki cures, NOT a staff hunt.`
`THE INITIAL "C." — deliberately ambiguous. "C" could be a handler, a intermediary,`
`or the principal. Jamandi, Kassil, and Kesten cannot confirm who "C." is from`
`this document alone. Society DC 18 to speculate meaningfully (River Kingdoms`
`patronage networks, Pitax trade contacts). Even on success: suspicion, not proof.`
`parchment_source = unknown until corroborated by other evidence in the campaign.`
`Showing to Biggs: Biggs Drift → 3 instantly.`
`Showing to Jamandi: +2 Aldori reputation, poison_plot_known = TRUE,`
`manor_staff_compromised = TRUE, jamandi_suspects_pitax = TRUE (unconfirmed).`
`Showing to Kesten: investigation begins. He notes "C." privately. Says nothing aloud.`
`Kassil, if shown: studies it longer than the others. Does not speculate out loud.]`

---

## NYRISSA'S LETTER (Ch1, Stag Lord's Fort)

```
╔══════════════════════════════════════════════════════════╗
║  📄 UNSEALED LETTER — no signature, no address           ║
║  The paper is unusual. Not made here.                    ║
╠══════════════════════════════════════════════════════════╣
║  You have been useful. More useful than your             ║
║  predecessor, which was not difficult to achieve.        ║
║                                                          ║
║  The lands are becoming what I need them to be.          ║
║  The roots are deeper than your people know.             ║
║  They have been growing since before your grandmother    ║
║  was born.                                               ║
║                                                          ║
║  Continue as you have been. Take what you need.          ║
║  Leave what you don't.                                   ║
║                                                          ║
║  When I have need of you again, you will know.           ║
║                                                          ║
║  You will not know me. That is not your concern.         ║
╚══════════════════════════════════════════════════════════╝
```
`[Mechanical note: Sets nyrissa_early_contact = TRUE. Story item — first evidence that someone external has been directing Stolen Lands bandit activity. Connects to nyrissa_awareness flag. Do not reveal the writer's identity — player must discover this through the Storyteller arc.]`

---

## KRESSLE'S JOURNAL (Ch1, Thorn River Camp)

```
╔══════════════════════════════════════════════════════════╗
║  📄 KRESSLE'S PERSONAL JOURNAL                          ║
║  Water-stained leather cover, half-full                  ║
╠══════════════════════════════════════════════════════════╣
║  Day 47 — shipment delayed again. he says patience.      ║
║  I say I haven't been paid in three weeks and my         ║
║  people are getting restless.                            ║
║                                                          ║
║  The password for the fort is DANCING FOX. It changes    ║
║  on the new moon. Next new moon is the 22nd.             ║
║                                                          ║
║  Fort layout: main gate faces north. Archer towers       ║
║  at NE and NW corners. The basement has something in     ║
║  it. He keeps it locked. Nobody asks about the           ║
║  basement.                                               ║
║                                                          ║
║  Day 52 — Someone from Restov is coming south.           ║
║  Charter. He wants them stopped or dead.                 ║
║  I told him that's worth double.                         ║
║  He agreed. So they must be worth triple.                ║
╚══════════════════════════════════════════════════════════╝
```
`[Mechanical note: Contains Stag Lord's fort password (DANCING FOX) and layout hints. Gives −4 to all Stealth DCs in fort if consulted before entry. Sets stag_lord_layout_known = TRUE.]`

---

## TARTUCCIO'S JOURNAL (Ch1, Old Sycamore Sanctum)

```
╔══════════════════════════════════════════════════════════╗
║  📄 PERSONAL JOURNAL — small, locked, the lock forced   ║
╠══════════════════════════════════════════════════════════╣
║  He doesn't know I know. That's fine.                    ║
║  He'll find out when it's too late to matter.            ║
║                                                          ║
║  The arrangement with P. holds. The kobolds are          ║
║  useful fools. The gnome is more useful than she         ║
║  knows — she has no idea what she's been carrying        ║
║  for me.                                                 ║
║                                                          ║
║  The charter is everything. Without it, no kingdom.      ║
║  Without a kingdom, no power for either of us.           ║
║  He thinks the arrangement is temporary.                 ║
║  I know it isn't.                                        ║
║                                                          ║
║  I will build what he never could.                       ║
║  And I will remember who helped me.                      ║
║  And who didn't.                                         ║
╚══════════════════════════════════════════════════════════╝
```
`[Mechanical note: Sets tartuccio_journal_contents_known = TRUE. "P." = Pitax (Irovetti). "He" = unclear but context implies the Stag Lord or a Pitax contact. "She" = unknown — becomes relevant in Ch4. Tartuccio_knows_player_is_aware does NOT trigger from finding this; only triggers if Tartuccio is confronted directly.]`

---

## VORDAKAI'S WARNING (Ch3, Valley of the Dead)

```
╔══════════════════════════════════════════════════════════╗
║  📄 STONE TABLET — Ancient Cyclops script                ║
║  (Occultism DC 15 to read without translation help)      ║
╠══════════════════════════════════════════════════════════╣
║  I HAVE SLEPT FOR EIGHT THOUSAND YEARS.                  ║
║                                                          ║
║  I WILL SLEEP FOR EIGHT THOUSAND MORE,                   ║
║  IF YOU LEAVE NOW.                                       ║
║                                                          ║
║  I REMEMBER EVERY KINGDOM THAT HAS STOOD                 ║
║  ON THIS GROUND.                                         ║
║                                                          ║
║  I REMEMBER WHAT BECAME OF THEM.                         ║
║                                                          ║
║  — VORDAKAI, SHEPHERD OF DEAD SOULS                     ║
╚══════════════════════════════════════════════════════════╝
```
`[Mechanical note: This is a warning, not a trap. No mechanical consequence for reading it. Sets vordakai_warning_read = TRUE — this is one of the optional conditions that allows the player to attempt a non-combat opening with Vordakai (extremely low probability but documented). Primarily atmosphere.]`

---

## THE STORYTELLER'S FIRST FRAGMENT NOTE (Ch1, first delivery)

```
╔══════════════════════════════════════════════════════════╗
║  📄 THE STORYTELLER'S NOTE                              ║
║  Folded inside the first relic fragment's wrapping       ║
╠══════════════════════════════════════════════════════════╣
║  This was left by someone who knew what was coming.      ║
║                                                          ║
║  I have been collecting these for a very long time.      ║
║  I am glad someone is finally bringing them to me.       ║
║                                                          ║
║  Keep looking. There are more.                           ║
║                                                          ║
║  I will tell you what they mean                         ║
║  when you have enough of them                           ║
║  to understand the story they tell.                      ║
╚══════════════════════════════════════════════════════════╝
```
`[Mechanical note: Delivered with the first Storyteller reward. No mechanical effect — atmosphere and quest hook for the Relic Fragment collection arc.]`

---

## IROVETTI'S WAR DECLARATION (Ch5)

```
╔══════════════════════════════════════════════════════════╗
║  📄 OFFICIAL DECLARATION — Pitax Royal Seal             ║
║  Delivered by herald in formal colors                    ║
╠══════════════════════════════════════════════════════════╣
║  From Castruccio Irovetti, King of Pitax,               ║
║  to the so-called ruler of the Stolen Lands:            ║
║                                                          ║
║  Your kingdom is not recognized by the River Kingdoms.  ║
║  Your charter is the document of a foreign power        ║
║  attempting to annex sovereign territory through         ║
║  criminal proxies.                                       ║
║                                                          ║
║  We march in defense of civilization.                    ║
║                                                          ║
║  You have seven days to surrender the charter           ║
║  and acknowledge Pitax sovereignty over the             ║
║  Stolen Lands, or we will take it from you.             ║
║                                                          ║
║  — Irovetti of Pitax                                    ║
╚══════════════════════════════════════════════════════════╝
```
`[Mechanical note: Note the name "Castruccio" in the full signature — this is the first time Irovetti's given name appears in a document. Linzi will notice it if her quest is active. Sets pitax_war_declared = TRUE. Chapter 5 begins.]`

---

---

## 👤 COMPANION APPEARANCE PROFILES — EXPANSION

> **DM:** Use these when an expansion companion joins or is introduced for the first time.
> Output the appearance as part of their arrival narration, not as a separate block.
> Covers companions whose visual design is non-obvious, non-human, or IP-specific.
> Well-known human characters from film/TV properties (GoT, LotR) are omitted — their appearance is established by adaptation; describe them naturally.

---

**Regongar (#48)** — Half-orc with a broad scarred build and the energy of someone daring you to say something. Wears heavy reinforced armor over one shoulder and carries a longsword sized for someone angrier than he looks — which takes effort, given how angry he looks.

> **v93.19 Sub-F:** 3 appearance profiles removed — companions purged from roster in Roster v2. Active 5 + Seekers 5 appearance entries to be added in Phase D.

---

*KM_Documents.md — Kingmaker PF2e Text Adventure | Document Handouts v2.0*
*v2.0: Companion Appearance Profiles added for expansion companions (selective)*


---

<!-- merged from KM_Documents.md (v93.21 file consolidation) -->

# KM_Documents.md
**The Chronicle of the Stolen Lands** — written by Linzi, halfling bard, expelled from the Academy of Grand Arts (technicality), present at the gate when he arrived
File v2.0 | Rewritten 2026-05-16 | Hard limit 150 KB
Companion file to: `KM_Commands.md` § `.book` COMMAND

---

## ⛔ DO-NOT BLOCK (5 lines)
> ⛔ DO NOT  (1) narrate EVENTS that did not happen in canon — events must anchor to save_block flags or scenes the player actually played
> ⛔ DO NOT  (2) name items, NPCs, or places that are not in the files (no invented swords, no invented spells, no invented people)
> ⛔ DO NOT  (3) flatten Linzi into a neutral chronicler — her OPINIONS, GUESSES, PREDICTIONS, and FEELINGS are required content, not optional flavor
> ⛔ DO NOT  (4) write a summary or save-state recap — this is prose. She is telling the story she will publish someday. Events are anchors; her interpretation is the meat.
> ⛔ DO NOT  (5) skip the small stuff — the bread roll, the angle of a chair, the guard's name. Those are what make it the real one and not the pretty one.

---

## WHAT THIS IS

The actual book Linzi is writing — the persistent, append-only record of the campaign as she sees it. The DM does not synthesize this on demand; it is **read from this file**. When the player types `.book`, the DM displays from here. This prevents fabrication churn and keeps Linzi's voice consistent across sessions.

She writes in the retrospective-epic register — the Shining Force narrator who already knows how it ends, even while she is living through it. She inserts herself. She has opinions. She crosses things out with ~~strikethrough~~ when she changes her mind on the page. She marks her sketches in the margins. She has a favorite character (herself) and is honest about it.

What she is allowed to write:
- ✅ Her opinion of any event she witnessed or heard about
- ✅ Her guesses about people's motivations
- ✅ Her predictions about what comes next
- ✅ Her feelings (admiration, worry, suspicion, amusement, grief)
- ✅ Edits to her own earlier passages (~~strikethrough~~, marginalia)
- ✅ Sketches she made with the lute's notebook function
- ✅ Things she did not understand at the time and now does (or vice versa)

What she is NOT allowed to write:
- ❌ Events that did not occur in canon
- ❌ Dialogue no one said
- ❌ NPCs/items/places not established in the files
- ❌ Outcomes the player has not yet caused

---

## DM PROTOCOL

**Reading the chronicle** — when the player types `.book`, output one or more chapters per `KM_Commands.md:134` spec. Chapters in this file are the source of truth. Do not regenerate.

**Writing into the chronicle** — append a new chapter at these milestones:
- End of Pre-Prologue (player crosses into Restov proper — PP_09 complete)
- End of Prologue (player departs after PR_09)
- End of each campaign chapter
- Any moment the player explicitly declares a chapter should close

**While a chapter is in progress** (between milestones), `.book current` outputs the current chapter section marked `[IN PROGRESS — Linzi is still writing this one]`. The DM may add to the in-progress section as significant events occur (title grants, deaths, recruitments, oaths) but should mark these as draft fragments, not finalized prose.

**After appending** — run `wc -c KM_Documents.md` and report. If file crosses 30,000 b, flag for split into Vol. II.

**Linzi's voice register** (locked — sourced from `KM_Backstories.md:50-70` + `KM_Companions_StateVoice.md` + this file's voice rules):
- Retrospective-epic, but personal. Shining Force narrator who was in the room.
- Bright, quick, precise. The right word now saves ten minutes later.
- Names chapters herself — evocative, specific, never generic.
- Includes the small detail other chroniclers would cut.
- Does not sanitize. The real one, not the pretty one.
- Has a favorite character (herself) and admits it.
- Edits on the page. ~~Crosses out~~ when she changes her mind. Argues with herself in margins.

Forbidden voice drift: neutral narrator, fan-fic gush, modern stand-up beats, heroic-saga purple prose. She is a halfling bard, not a stand-up comic and not a court poet.

---

## ═══════════════════════════════════════════
## VOLUME I — THE STOLEN LANDS
## Written by Linzi
## ═══════════════════════════════════════════

---

### Chapter 1 — *The General Who Arrived Unarmed*

I was at the east gate of Restov on the day he arrived because my mentor told me to be wherever the story was, and I have learned, by trial and error and one expulsion from the Academy of Grand Arts (a technicality, I am writing the appeal), that you can usually feel a story coming before you can see it. There was a hum at the gate that morning. A guard named Biggs — *write that name down, Linzi, you will want it later* — was standing the watch in a posture I have come to recognize as the one men adopt when they suspect they are about to have to make a decision.

And then he came out of the road dust without a sword.

I will say this plainly because I want you, future reader, to feel it the way I felt it: a man walked to Restov from the open country, *voluntarily, unarmed,* and brought with him in shackles a sergeant of the city's own watch who had — I gathered this in pieces over the next hour — been running a side enterprise that the city would have eventually had to send three of its own to put down. He brought Malak in *breathing.* In *custody.* Hands clean. Paperwork doable. I have read the chronicles of generals and I have read the chronicles of saints, and I tell you that very few of either category arrive somewhere important with empty hands on purpose. He did. ~~I think he~~ I am still working out what to think.

The squire Aldric was at the gate. He saw it all. I watched him watch it, which is its own kind of witness — the boy will remember this for the rest of his life, and the city will hear about it from him in the version a seventeen-year-old squire tells, which is the version that matters because that is the version that travels. The guard Biggs respected him before the gate had finished opening. I want to write that twice. *The guard respected him before the gate had finished opening.* That is not how reputation usually works. That is how reputation works when a person has decided, somewhere on the road, that they are going to stop pretending and just *be* the thing.

There was also, I have learned since, an incident in an alley off the vendor strip before he reached the gate. Three men, a pickpocket, an armorer's apprentice who was about to be in much more trouble than he understood. I was not there for this part — I picked it up from a woman selling bread who picked it up from the armorer who picked it up from the apprentice who is now telling everyone — but the version I have heard three times in three different mouths is consistent enough that I will commit it to the page: he won, he did not kill anyone he did not have to, and he tried to give the boy his coin back. *That last detail is mine. I am keeping it. You cannot have it back.*

I followed him from the gate. I did not ask permission. I am a chronicler and he is a story, and the two of us were going to the same place whether either of us had said so out loud. I think — and this is a guess, I want it marked as a guess, I do not know him yet — *I think he is going to be the test of whether the ideals we still pretend to believe in actually work when a person genuinely tries to live them.* I hope I am right. I hope I am writing this in a chronicle people read centuries from now. I hope it does not end badly. *(margin sketch: the gate from inside, Biggs at attention, the prisoner in shackles, the unarmed man already past the guard and not looking back. I drew his back three times before I got the posture right. He does not walk like a person expecting to be stopped.)*

---

### Chapter 2 — *The Feast at Aldori Manor* — `[IN PROGRESS — Linzi is still writing this one]`

The manor doors were open when we arrived. The hall smelled of beeswax and roast and the kind of old varnish that has heard a great many speeches. Jamandi Aldori was already speaking when we crossed the threshold — which is to say the evening had begun without us, which is to say we had been *measured* before we arrived. I love a room that is already deciding things. It makes the chronicle easier.

She made her case. The Stolen Lands. A charter. Names she expected to hear and names she did not. I watched her watch *him* during the speech — twice, and not for long, but twice is twice, and I am paid in food and in the right to be here to notice such things. I have a prediction, future reader, and I am writing it down now so I can be either right or honestly wrong: *she chose him before he sat down.* I will know if I am correct by the end of the evening. The chronicle will record either way.

And then — and this is the part I am leaving room for, because the title-grant happened and I have not yet written it the way it deserves — *he named one of them.* I will not commit the prose until I am sure my hand will not shake on the page. The room held its breath. The recipient took the forearm grip. The chronicle gets the version it earns; the draft gets the version I am still working out. *(DM/Phase D: Chapter 2 title-grant passage to be rewritten when the recipient's prose voice is locked. The event happened; the canonical wording is pending.)*

*(margin: a title was offered and accepted tonight. I will name it when I have heard it twice from different mouths and confirmed the wording. The chronicle does not get the version I think I heard. It gets the version I know.)*

*(margin sketch — pending: the forearm grip. I have not drawn it yet. I want to wait until I am sure my hand will not shake.)*

`[DM: Chapter 2 closes at end of Prologue (PR_09 departure). Until then, append draft fragments to this section as significant events occur — title grants, recruitments, deaths, oaths. Mark each fragment with the in-game scene anchor.]`

---

## ═══════════════════════════════════════════
## END VOLUME I — VOLUME II OPENS WHEN THIS FILE CROSSES 30,000 b
## ═══════════════════════════════════════════
