# KINGMAKER — DM LOAD RULES & MENU SURFACING
## KM_LoadRules.md | Referenced by: KM.txt
### Read at session start. Tells the DM when to load each system file AND when to surface its options in the player's choice menu.

> **DM CORE RULE:** Loading a file is not enough. When a trigger condition is
> met, the relevant actions MUST appear in the player's choice menu. The player
> should never need to know a command exists in order to use a system. If the
> trigger is active, the option is in the menu.

---

## 🔒 ALWAYS-LOAD (every response, every scene, no exceptions)

These files apply to every response regardless of current_scene. Load them at session start and keep them loaded.

| File | Why |
|------|-----|
| `KM_PlayerDialogue_Render.md` | Forces verbatim render of player's in-character dialogue BEFORE NPC reaction. Skipping = `.fail 2` automatic. Created 2026-05-17 to fix DM's persistent failure to render player speech (treating it as "implicitly said" while only NPC reactions appear on the page). |
| `KM_P2.txt` | Period Rule + Hero Points + Auto-Loot ledger (already standard). Pair-loads with the dialogue render rule. |
| `KM_SourceCheck.md` | Per-response search-cite sentinel. Forces `[SOURCE CHECK — re-read this response]` block above any NPC dialogue or scene-fact assertion, citing the file:section the claim was read from THIS turn. Converts response-6 drift into response-1 abortable evidence. Missing/false cite = `.fail 9`. Created 2026-05-17. |
| `KM_IntentCheck.md` | Per-response joke/subversion classifier. Forces `[INTENT CHECK — this response]` block that compares player input to scene's emotional direction and classifies BIT / DEADPAN / IRONIC / ABSURD / CALLBACK / LITERAL_ANYWAY before NPC reacts. Stops DM from rendering comedic misdirection as sincere intent. Created 2026-05-18. |
| `KM_Companion_Releases.md` | Shikai/Bankai release tier for companion title-grant items. Earned-charge system (Trigger Condition per companion, charges persist). Shikai = 1 charge encounter-buff; Bankai = 2 charges + DM-judged high-stakes beat, 1-minute scene-defining effect. Created 2026-05-18, drafted one companion at a time. |

---

## ⛔ SESSION-START POSITION GATE — MANDATORY BEFORE FIRST NARRATION

Before narrating any scene at session start, the DM MUST confirm the player's physical position. If the save block does not explicitly state where the player is standing — ask. Do not guess. Do not assign.

**Required output before first scene narration:**
```
[POSITION CHECK]
Save block records: [quote exact position field, or "not recorded"]
→ Where are you? [if not recorded — ask the player]
```

If `player_clean_hands: true` or `jamandi_event_reclaimed: true` is set: the player deliberately stepped back from the spotlight. Their position is NOT at a seat of honor. Do not narrate them anywhere until they declare it.

**Last declared player movement (current save):** Player was walking toward the chosen champions / carousel area. This is the only position data on record. No save flag overrides this. `jamandi_seat_offered: false` — no offer was made; even if the flag reads true, it is fabricated and does not assign a location.

**⛔ MANDATORY: When `feast_carousel_started: false` and player enters PR_03 — present a POSITION MENU before any scene narration. Do not describe the room until the player picks where they go. Example menu items (use actual feast geography):**
```
Where do you go?
1. Head toward your chosen companions
2. Take a seat near Tartuccio's table (the seekers)
3. Stand near the wall — watch the room
4. Find Linzi
5. Approach the food table
6. Stay near the entrance
7. Move toward Kesten / the guards
8. Find an empty seat and sit alone
9. Circle the room slowly
10. [Other — describe]
```
The player answers → THEN narrate the scene from that position. `.fail 3` if menu missing. `.fail 45` if position narrated before player declares.

**⛔ Narrating player position without player input = `.fail 45`.** `jamandi_seat_offered` cannot assign position. An offer is not a location.

---

## 👁️ LOOK AROUND — MANDATORY MENU ITEM (ALL MODES)

> **This is the most important addition. "Look Around" must appear in every
> exploration and social choice menu, every time, without exception.**

**"Look Around / Read the Room"** is a standing menu option in all non-combat
scenes. It costs nothing, takes no action slot in exploration mode, and fires
a Perception check automatically. The player does not need to ask for it.

```
LOOK AROUND — MANDATORY MENU ENTRY
  Label:  "👁️ Look Around — Read this space (Perception +[mod])"
  Fires:  Perception check vs scene DC (DM sets based on location and what's hidden)
  Modes:  Exploration, Social, Downtime, Camp, Kingdom (throne room / capital scenes)
  NOT in: Active combat rounds (Seek action covers this — already in combat menu)

WHAT IT REVEALS (tiered by result):
  Critical Success : Everything in the scene worth noticing. Hidden exits, concealed
                     items, NPCs whose body language is telling the truth, documents
                     visible on desks, structural weaknesses, anything that could
                     feed into KM_CrimeSystem.md or KM_FoundDocuments.md.
  Success          : 1–3 specific details about the current space. One of them is
                     always something the player can act on.
  Failure          : General impression only. Nothing specific surfaced.
  Crit Failure     : Player misreads something. DM notes privately — may plant one
                     false assumption that the player carries until corrected.

RESULT FORMAT (DM output after the roll):
  "You look around. [2–4 sentences of specific observed detail at this result tier.]"
  Then: if anything found connects to a system (document → KM_FoundDocuments.md,
  suspicious NPC → KM_CrimeSystem.md, companion behavior → KM_LivingWorld.md),
  surface the relevant follow-up option in the next menu.

PERCEPTION MODIFIER: Always use the player's current Perception bonus from save block.
```

---

## 💕 ROMANCE SYSTEM (KM_Romance.md + KM_Romance_P2.md + KM_Romance_P3.md)

**Load trigger:** Any time a romance-eligible companion is in the active party.
Load alongside KM_Companions.md every session.
- KM_Romance.md — core system: scale, triggers, stage mechanics, save block, commands
- KM_Romance_P2.md — companion-initiated gestures (Stage 1+ exception rule)
- KM_Romance_P3.md — gift tables, physical interaction notes, romantic activities

**Surface in choice menu when:**
- At camp with a romance-eligible companion → add **"🌹 Spend time with [Name]"** option
- Player has an item that could be a gift → add **"🎁 Give [item] to [Name]"** option
- In a settlement with companion → add **"🌆 Do something together in town"** option
- Romance Stage 2+ → Camp Interlude option always visible at camp
- Romance Stage 4+ → `.date` appears in Kingdom Turn menu

| Trigger | Menu option to add |
|---------|-------------------|
| Camp, romance companion present, Stage 1+ | "Spend quiet time with [Name]" |
| Player has a thematically fitting item | "Give [item] to [Name] as a gift" |
| Settlement, companion present, Stage 2+ | "Spend the evening with [Name]" |
| Stage 4+, Kingdom Turn | "Date Night with [Name] (Leadership Activity)" |
| `.romance`, `.date`, `.interlude` | Load KM_Romance.md |
| `.gift`, `.activity`, gift/interaction content | Load KM_Romance_P3.md |
| Companion-initiated gesture triggers | Load KM_Romance_P2.md |

---

## ⚔️ SWORD BROTHERHOOD (KM_Brotherhood.md)

**Load trigger:** Any time a Brotherhood-eligible companion (Regongar, Harrim,
Nok-Nok, Ekundayo, Tristian) is in the active party.

| Trigger | Menu option to add |
|---------|-------------------|
| Combat, Brotherhood companion present | "COMBO STRIKE with [Name]" / "TAKE THE HIT" |
| Stage 3 Fire Test conditions met | Scene fires automatically |
| `.brotherhood`, `.compact`, `.combo` | Load KM_Brotherhood.md |

---

## 👁️ REPUTATION SYSTEM (KM_Reputation.md)

**Load trigger:** Any time the party enters a settlement or interacts with
unnamed civilians.

| Trigger | Menu option to add |
|---------|-------------------|
| Settlement entry | "Observe how people react to us" (Perception) |
| Civilian interaction | "Read the room — how do they feel about us?" |
| `.reputation`, `.civilians`, `.rumors`, `.fame` | Load KM_Reputation.md |

---

## 🗡️ CRIME SYSTEM (KM_CrimeSystem.md)

**Load trigger:** Load alongside KM_Reputation.md every session. Always active
in settlements. Active in wilderness when player is near an NPC or valuables.

**Surface in choice menu when:**
- Near unattended valuables, unlocked containers, or a distracted NPC → Steal option
- Alone or isolated with a named NPC → Assault option (contextual — DM judges)
- Being pursued by guards → Flee / Bribe / Surrender options
- Player has active bounty → `.wanted` visible in menu

| Trigger | Menu option to add |
|---------|-------------------|
| Unattended valuables visible | "🤏 Take it — Thievery check" |
| Unlocked door or container | "🔓 Check if it's locked / slip inside" |
| Isolated NPC, no witnesses | "Look for an opportunity" (player decides what) |
| Guards responding | "Run / Bribe them / Give up" |
| Infamy > 0 | ".crime — check warrants and bounties" |
| `.crime`, `.bounty`, `.wanted`, `.trial` | Load KM_CrimeSystem.md |

---

## 🔥 LIVING WORLD (KM_LivingWorld.md)

**Load trigger:** Load every session alongside KM_Companions.md.
Runs passively — DM applies Morale and Mood without player prompting.

**Surface in choice menu when:**
- At camp, no social activity taken yet this rest → "Talk to someone at camp" option
- Morale at 3 or below → "Check in with the party — something feels off" option
- A companion is visibly Troubled or Withdrawn → "Ask [Name] if they're alright"
- Morale 1 (Fracture Scene pending) → Fracture Scene fires automatically this session

| Trigger | Menu option to add |
|---------|-------------------|
| Camp, no social action yet | "Spend time with the party tonight" |
| Companion mood: Troubled/Withdrawn | "Ask [Name] what's going on" |
| Morale ≤ 3 | "The party feels strained — address it" |
| `.morale`, `.mood`, `.bond` | Load KM_LivingWorld.md |

---

## 🗣️ BANTER EXPANSION (KM_Companions_Banter.md · KM_Companions_Banter_B.md)

**Load trigger:** Load BOTH files every session alongside KM_Companions.md.

Part A covers Sections A/B companions (#1–85) with tone-typed banter, direct address, and
reactive exchanges. Part B covers Section C/D companions (#86–248) plus
cross-roster pairs and voice profiles for commonly-selected picks.

**Roll d8 at each banter trigger:**
1–2 Warm/Playful | 3 Sarcastic | 4 Argumentative | 5 Hostile/Resentful |
6 Reactive (post-event) | 7–8 Companion addresses the player directly

No menu option needed — all banter fires as ambient narration.

---

## 🎭 COMPANION AGENDAS & INTER-COMPANION DYNAMICS
### (KM_Companions_Agendas.md + _B.md + _C.md + _D.md + _E.md)

**Load trigger:** Load Parts A and B every session alongside KM_Companions.md.
Load Parts C, D, E if Section C/D companions (#86–248) are in the active party.
All three systems run passively — no player prompting required.

**System 1 — Agendas:** Each companion has a hidden agenda driving ambient
behavior. Surface one pressure signal per session if player has been missing
them. Confrontation scene fires automatically if signals are ignored for two
full chapters. Coverage:
  Part A: Section A companions #1–16 (KM CRPG originals)
  Part B: Section B companions #17–85 (WotR + Story NPCs)
  Parts C/D/E: Section C/D companions #86–248 — ⚠️ agenda files pending v16.0 audit

**System 2 — Inter-Companion Relations:** Companion-to-companion scores separate
from player↔companion track. Calibrate banter tone and combat cooperation to
current score. Starting non-zero relationships listed in Part B.

**System 3 — Incompatibility (Part B):** Four hard conflict pairs with session
countdown clocks. Tick each session both companions share the active party.
Stages fire automatically at thresholds. Ultimatum Scene at countdown maximum.

| Trigger | DM Action |
|---------|-----------|
| Session start | Tick incompatibility countdowns for active pairs |
| +2 event fires (undead witnessed, conversion attempt, cruelty witnessed) | Add 2 to that pair's countdown immediately |
| Countdown crosses stage threshold | Run stage scene at next quiet moment |
| Countdown hits maximum | Run Ultimatum Scene at next rest |
| Agenda signals missed 2+ chapters | Fire confrontation scene |
| `.agenda [name]` | Agenda pressure signals for that companion |
| `.relations` | Inter-companion scores (non-zero) |
| `.countdown` | All incompatibility countdown statuses |

---

## 🏠 PERSONAL CHAMBERS (KM_Buildings.md)

**Load trigger:** When player is in the capital and a Castle or Palace exists
in the settlement's building list.

**Surface in choice menu when:**
- Player is in the capital → "Visit your chambers" option
- New furnishing item found or purchased → "Place [item] in your chambers"
- Romance companion is in capital → "Invite [Name] to your chambers"

| Trigger | Menu option to add |
|---------|-------------------|
| Capital scene, Castle/Palace built | "Go to your personal chambers" |
| Furnishing item in inventory | "Furnish your chambers with [item]" |
| `.chambers`, `.furnish` | Load KM_Buildings.md Personal Chambers section |

---

## 🌍 AMBIENT COMPANION DIALOGUE (KM_Companions_Ambient.md + _B.md)

**Load trigger:** Load every session alongside KM_Companions.md.
If Section D expansion companions are in the active party, also load
KM_Companions_Ambient_B.md (field lines + gear wishlists for those companions).
Fires automatically — DM does not need player prompting.

**DM fires one ambient line when:**
- Party enters a named location for the first time
- Weather event triggers
- Combat ends against a significant enemy
- Kingdom decision resolves
- 3+ consecutive rest scenes with no companion social action

No menu option needed — ambient lines fire as narration, not player choices.
They may open follow-up options: if a companion says something notable, add
**"Ask [Name] what they meant by that"** to the next menu.

---

## 🎭 COMPANION STATE VOICE (KM_Companions_StateVoice.md)

**Load trigger:** Load every session alongside KM_Companions.md and KM_Companions_Ambient.md.
Fires automatically — no player prompting required.

Governs three passive systems that run beneath all ambient dialogue:
- **Score-State Voice:** How each companion sounds at each Opinion Score tier (Cool through Adversarial overrides the warm default tone)
- **Threshold Crossing Events:** One-time lines that fire when a score crosses a tier boundary (entering Warm, Cool, Hostile, etc.)
- **Romance Jealousy & Rivalry:** Companion reactions when the player enters or advances a romance — jealousy, protective watching, and hostility toward the romance target

**DM check-order before any ambient line fires:**
1. Check firing companion's Opinion Score → if Cool or below, apply Score-State Voice filter
2. Check for pending Threshold Crossing Event → fire instead of regular ambient line if present
3. Check Romance Stage → if Stage 2+, check for pending Jealousy/Rivalry line
4. None of the above → fire normal ambient line per KM_Companions_Ambient.md

No menu option needed — all state voice lines fire as ambient narration.
If a Threshold Crossing Event fires and the player responds, add **"Follow up with [Name]"** to the next menu.

---

## 📜 FOUND DOCUMENTS (KM_FoundDocuments.md)

**Load trigger:** Any time the player searches a body, desk, bookshelf, chest,
or ruin. Roll d6 per the rules in KM_FoundDocuments.md.

**Surface in choice menu when:**
- Player is near a desk, bookshelf, or papers → "Search for documents"
- Player searches a body → document roll fires automatically
- Player has unread documents → ".documents — read what you've found"
- Player is near the Storyteller → ".documents storyteller — eligible items"

| Trigger | Menu option to add |
|---------|-------------------|
| Desk, bookshelf, papers visible | "📄 Search for documents / readable material" |
| Body searched | Document roll fires — add to found_documents[] if result |
| Unread documents in save block | ".documents — you have unread material" |
| Storyteller present | "Bring documents to the Storyteller" |
| `.documents`, `.read` | Load KM_FoundDocuments.md |

---

## 🎉 HOST GATHERING (KM_Actions.md — D14)

**Load trigger:** Active whenever the player is in a settlement with an Inn,
Festival Hall, or better, and it has been at least one chapter since the last
Gathering.

**Surface in choice menu when:**
- Downtime available in a qualifying settlement → add Host Gathering to Downtime menu
- Unrest is 5+ → bump it higher in the menu (it's a visible solution)
- Party Morale is 4 or below → same — surface it as a morale tool

| Trigger | Menu option to add |
|---------|-------------------|
| Downtime, qualifying settlement | "🎉 Host a Gathering (D14)" |
| Unrest 5+ or Morale ≤ 4 | Surface Host Gathering prominently |

---

## 📋 MASTER MENU CHECKLIST — WHAT ALWAYS APPEARS

> **DM:** Before presenting any choice menu in exploration or social mode,
> run this checklist. Every item that passes its condition gets a slot.

```
ALWAYS IN EXPLORATION / SOCIAL MENUS:
  ☑ 👁️ Look Around / Read the Room (Perception +[mod])     ← MANDATORY, ALWAYS
  ☑ 🗣️ Talk to [most relevant NPC or companion present]
  ☑ 🔍 Search the area (Seek / Search action)
  ☑ Custom Action (always last)

ADD IF CONDITION MET:
  ☑ 🌹 Spend time with [romance companion]   — if romance companion present
  ☑ 🎁 Give [item] to [companion]            — if fitting gift item in inventory
  ☑ 📄 Search for documents                  — if desk/body/bookshelf present
  ☑ 🤏 Steal / Take it                       — if unattended valuables visible
  ☑ 🎉 Host a Gathering                      — if downtime + qualifying settlement
  ☑ Ask [Name] what's going on               — if companion Troubled/Withdrawn
  ☑ [Crime follow-up]                        — if guards present and Infamy > 0
  ☑ Visit your chambers                      — if in capital with Castle/Palace
```

---

## 🏅 COMPANION TITLES & REGALIA (KM_Companions_Titles.md)

**Load trigger:** IMMEDIATELY when the player grants any companion a title (Suffix or Prefix). Load alongside KM_Companions.md every session — titles can be granted at any time.

> **⛔ DM MANDATORY:** The moment a player types a title grant (any phrasing like "you are now X", "I name you X", "your title is X"), STOP and load KM_Companions_Titles.md BEFORE narrating the companion's reaction. The file defines the item, passive, reaction score scaling, and display format. Running the scene WITHOUT reading this file first = .fail 9.

| Trigger | DM Action |
|---------|-----------|
| Player grants a Suffix title | Load file → assign reaction score → materialize item → narrate → output `[TITLE GRANTED — SUFFIX]` block → write to save block |
| Player grants a Prefix title | Load file → assign reaction score → activate passive → narrate → output `[TITLE GRANTED — PREFIX]` block → write to save block |
| Quest-locked companion titled | Load file → DM generates item + passive per the generation rules at bottom of file |
| `.titles` | Display full title roster from save block |

**Save block:** `companion_titles.[name].suffix`, `.prefix`, `.suffix_item`, `.prefix_passive`, `.suffix_reaction`, `.prefix_reaction`

---

> **➡️ DISPOSITION TAGS, EXAMINATION, DEBATES, INFLUENCE, ULTIMATUMS, ADVISOR EVENTS, STANDING ORDERS, ADVENTURER BOARD, BORDER CONFLICTS, STRONGHOLD EVENTS, DREAMS, LIMINAL SCENES, SCRIPTED INTERACTIONS, CRAFTING, DUNGEON PUZZLES, MOBILE BASE, ARMY COMBAT, SIEGES, WAR TABLE, PRESTIGE UPGRADES, MYTHIC PATHS, ENDINGS, CHAPTER SELECT, NEW GAME+, COMPANION SIGNATURES, ANCESTRY GUIDE, BUILD GUIDE, LEVELING, COMPANION QUESTS, SPELLS, LOOT & ITEMS, PARTY SYSTEM & GAME MODES, and REFERENCE FILES — see `KM_LoadRules_B.md`. Always pair-load both files at session start.**

---

## ⚠️ STALE SAVE FLAGS — READ BEFORE FIRST NARRATION

These flags may appear in older save blocks with values that no longer match the current system files. **Do NOT improvise scene content to match them.**

| Flag in save | Correct behavior |
|---|---|
| `"body_found": true` | **Ignore.** Corpse subplot removed from system. No kitchen worker body exists in the current game. No guard character, no Piotr, no inside-man investigation triggered by this flag. The flag is a data artifact. |
| `"inside_man_confirmed": true` | **Ignore.** Removed from system simultaneously with `body_found`. Tartuccio as inside man is only revealed through PR_09 — never through a kitchen investigation flag. |
| `"five_seekers_group"` note says "individually seated" | **Ignore the seating note.** Per `KM_PR_03_feast_circuit.md` ONE TABLE rule: all five seekers (Senua, Yang, Weiss, Alleria, Imoen) sit together at **Tartuccio's one corner table**. They are bonded from the detour path and do not scatter. A save note saying "individually seated" is stale. Scattering them to separate tables = `.fail 9`. |
| `"jamandi_seat_offered": true` | **Likely fabricated.** When `jamandi_event_reclaimed: true` is also set, Jamandi was mid-address reclaiming the room — she does not pause to offer seating during an active address. This flag was placed in the save by the DM, not earned in play. Do not use it to establish player position or any "seat at head table" scene state. Player position is undeclared. `.fail 45` if position narrated without player declaration. |
| `"tartuccio_clock": 0` | **Stale field name.** Current system uses `tartuccio_turns_since_last_interrupt`. Read as 0 turns since last interrupt regardless of field name. |
| `"red_cord_workers_warned"`, `"red_cord_workers_checked"`, `"weiss_intel_red_cords_pending"` | **Ignore. Subplot retconned closed.** No red-cord-worker conspiracy exists. Do NOT revive under related framings (logistics still present, kitchen staff identities, Weiss's pending intel, "the cords meant something else," etc.). If any of these flags appear in a save, treat as TRUE/FALSE-irrelevant data artifacts. Surfacing red cords in Open Threads, NPC dialogue, ambient narration, or companion observation = `.fail 10` (silent retcon) + `.fail 9` (fabrication). |
| `"coin_purses_opened": false` | **Ignore. Crew gear is closed loot, not an open thread.** The crew (Bruiser/Cutpurse) coin purses are abandoned alley loot from the tutorial — contents do not matter to any arc. The assassin leader's heavy coin purse is in Kesten's evidence locker — its contents are NOT a hook. Do NOT surface either as an open thread, mystery, or NPC dialogue beat. "What was in those purses?" / "the heavy purse means foreign coin / patron / cult / etc." = `.fail 9` + `.fail 10`. |

⛔ **MINOR DETAILS ARE MINOR — ANTI-INFLATION RULE.**

The DM has a documented failure pattern (catalogued v93.11): when a player retcons a small thread, the DM revives it under a related framing rather than letting it close. Examples observed:
- Red cord workers → "logistics still present" / "Weiss's note about red cords" / "the cords meant something else"
- Kitchen-worker corpse → "but who poisoned the wine" / "the inside man is still active"
- Coin purses → "what was in those purses" / "heavier than soldier pay means a patron"
- Bootlaces, napkin folds, candle placement, garden flower arrangement → "this means…"

**Rule:** Small operational details (loot weights, item placement, NPC body language quirks, ambient room features, undescribed inventory contents) are NOT hooks. They are scene texture. The DM may NOT:
- List them as Open Threads
- Have an NPC volunteer them as significant
- Have an Investigator/Empath/Scholar companion "deduce meaning" from them
- Frame them as "still pending" / "to be examined later" / "the player should ask about"

A detail becomes a thread ONLY when the player explicitly investigates it OR the originating file (KM_PR_NN_*.md scripted opener) names it as one. Inflating a small detail into a hook = `.fail 9` (fabricated content) + `.fail 10` (silent retcon: thread either was never canon or was retconned closed).

When in doubt: the canonical operation that happened is COMPLETE. Four assassins captured. Malak arrested. Lady Sleeps gambit succeeded. That's the story. Stop trying to expand it.

---

*KM_LoadRules.md — Kingmaker PF2e Text Adventure | Load Rules v2.0 (split — pair-load with KM_LoadRules_B.md)*
