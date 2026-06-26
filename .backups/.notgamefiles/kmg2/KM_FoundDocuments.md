# KINGMAKER — FOUND DOCUMENTS SYSTEM
## KM_FoundDocuments.md | Active from: Chapter 1 | Referenced by: KM_Exploration.md, KM_Loot_Merchants.md

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

*KM_FoundDocuments.md — Kingmaker PF2e Text Adventure | Found Documents System v1.0*
*All document content is original to this project. Integrates with: KM_Exploration.md (Storyteller), KM_LivingWorld.md (Bond Moments), KM_CrimeSystem.md (Forgery templates), KM_Actions.md (D5 Create Forgery, D23 Research)*
