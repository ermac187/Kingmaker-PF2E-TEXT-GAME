# KINGMAKER — SCENE FILE REQUIREMENTS
## KM_SceneFiles.md | Referenced by: KM.txt Rule Zero Commandment 10

---

> **⛔ DM: BEFORE PLAYING ANY SCENE, SEARCH AND READ EVERY FILE LISTED BELOW FOR THAT SCENE. Missing files = missing mechanics = `.fail 9`.**
>
> **Verification requirement:** After loading scene files, output a one-line confirmation in chat: *"Scene files loaded: [list]"* before any narration. This proves you read them.

---

## 🏛️ CORE FILES — ALWAYS LOADED EVERY SESSION

These are loaded at session start and stay active throughout all scenes. Never skip.

```
KM.txt                  — Rule Zero, master launcher
KM_P2.txt               — Hero Points, period rule, game state, death door
KM_DMRules.md           — Response format, fail codes, XP, protocols
KM_LoadRules.md         — When to load each system file
KM_Commands.md          — Base command reference
KM_Commands_Maps.md     — Panel formats, maps
KM_Commands.md       — Extended commands, loot panels
KM_Commands.md      — New system commands + .FAIL 2 EXPANDED RECOVERY
KM_Actions.md           — PF2e action reference
KM_Companions.md        — Companion base profiles (all 73)
KM_Companions.md      — Companion profiles continued
KM_Companions.md      — Pathfinder iconics
KM_Companions.md      — More iconics
KM_Companions_Behaviors.md — Detailed iconic profiles + Pick-10 selection screen
KM_Companions_Titles.md — Title rewards: items + passives + reaction scoring
KM_Companions_Titles.md — Title rewards sidecar (class-apex companions)
KM_NPCs.md   — Opinion scoring system (+ _B + _C)
KM_NPCs.md      — Physical profiles (Jamandi, Kassil, Kesten, Malak,
                           Biggs/Wedge, Oleg, Svetlana, Ezvanki, Tartuccio,
                           Jhod, Akiros, Bokken). Quick Tags + sensory detail.
KM_Combat_Systems.md   — Combat narration rules
KM_Conditions_Skills.md — PF2e conditions, skills
KM_Glossary.md          — Terms, abbreviations
```

---

## 🚪 PRE-PROLOGUE — THE RESTOV GATES (atomic refactor v92.0)

**Atomic architecture:** Pre-Prologue is now split into 9 single-beat files
(`KM_PP_01_*.md` through `KM_PP_09_*.md`). The DM loads ONE atomic file at
a time, determined by `save_block.pre_prologue_state`. No pair-loading.

**State-to-file mapping (load EXACTLY one PP_NN per response):**

```
pre_prologue_state           → load this file
─────────────────────────────  ─────────────────────────────
"" (new game)                → KM_PP_01_arrival.md
"PP_ARRIVAL"                 → KM_PP_01_arrival.md
"PP_TUTORIAL_PHASE_A"        → KM_PP_02_tutorial_setup.md
"PP_TUTORIAL_PHASE_B"        → KM_PP_03_tutorial_combat.md
                               (or KM_PP_04 if non-combat resolution)
"PP_TUTORIAL_OUTCOME"        → KM_PP_04_tutorial_outcome.md
"PP_GATE_APPROACH"           → KM_PP_05_gate_approach.md
"PP_GATE_CONFRONTATION"      → KM_PP_06_gate_state.md (state mechanics)
                             + KM_PP_07_gate_paths.md (path triggers)
"PP_GATE_RESOLUTION"         → KM_PP_07_gate_paths.md (path narration)
"PP_GATE_EXIT"               → KM_PP_08_gate_exit.md (six proofs)
"PP_RESTOV_WALK"             → KM_PP_09_restov_walk.md
```

**Lookup files (NOT atomic — referenced by pointer from PP_NN files):**

```
KM_PrePrologue_Setup.md    — Build substitution table (8 brackets per build_id)
KM_PrePrologue_Setup.md  — Armor material lookup
KM_PrePrologue_Setup.md        — 24-condition XP table (read at PP_08)
KM_Malak_Jail.md              — Malak's 3 verbatim speeches (referenced at PP_05)
KM_Malak_Jail.md                  — Malak jail: 5 seekers + coin purse + release paths
KM_NPCs.md          — Malak/Biggs/Wedge/archer Quick Tags + sensory
KM_Ancestries.md + _CRB.md — Backgrounds for CharCreate (not Pre-Prologue scene)
```

**DELETED legacy monolithic files (removed 2026-05-08 — use atomic PP_NN files):**

```
KM_PrePrologue.md        — DELETED → split across PP_01, PP_05, PP_09
KM_PrePrologue_B.md      — DELETED → gates 0–4+H/I/J split into PP_02/06/08
KM_PrePrologue_NPCs.md   — DELETED → tutorial → PP_02/03/04, NPCs → PP_05
KM_PrePrologue_Paths.md  — DELETED → consolidated into PP_07
KM_PrePrologue_Paths_QT.md — DELETED → state trackers → PP_06, paths → PP_07
KM_PrePrologue_Setup.md  — ACTIVE LOOKUP → crowd NPC profiles not yet in NPC_Profiles.md
KM_PrePrologue_Setup.md — ACTIVE LOOKUP → PP_07 references for ARREST CELEBRATION BEAT
```

**Why the refactor:** Sonnet 4.6 cannot reliably hold 30 KB of rules in
working attention while also generating narrative AND tracking persistent
state. Atomic single-beat files put ONE small file in front of the model
per turn, with local DO-NOT blocks instead of global fail-code references.
See `KM_ArchitecturalRefactor.md` for the full plan.

---

## 🍷 PROLOGUE — JAMANDI'S MANOR (atomic refactor v92.0)

**Atomic architecture:** Prologue is now split into 9 single-beat files
(`KM_PR_01_*.md` through `KM_PR_09_*.md`). Load ONE atomic file at a time,
determined by `save_block.current_scene`. No pair-loading.

**State-to-file mapping (load EXACTLY one PR_NN per response):**

```
current_scene                  → load this file
───────────────────────────────  ─────────────────────────────────────
"prologue_p1_arrival"          → KM_PR_01_manor_arrival.md
"prologue_feast" (PR_02 phase) → KM_PR_02_feast_opening.md
"prologue_feast" (carousel)    → KM_PR_03_feast_circuit.md + KM_PR_03_Openers.md (opener pool) + KM_DMRules_C.md (feast carousel supplement) + KM_Prologue_Systems.md (Tartuccio baseline: Confidence/Wariness/Clock/StatusBanner) + KM_Tartuccio_Strategic.md (Tartuccio strategic layer: seeker flips, panic state, companion poaching, alignment resistance) + KM_Companions_Behaviors.md (AT TABLE cross-talk tone tables + pair scores gate banter tones)
"prologue_night"               → KM_PR_04_night_explosion.md
"prologue_corridor"            → KM_PR_05_corridor_rescue.md
"prologue_sweep"               → KM_PR_06_manor_sweep.md
"prologue_hall"  (battle)      → KM_PR_07_final_battle.md
"prologue_hall"  (calm)        → KM_PR_08_the_calm.md
"prologue_accusation"          → KM_PR_09_accusation.md (six proofs)
"outside_manor"                → KM_PR_BRANCH_WALKOUT.md (player left)
```

**⛔ WALKOUT BRANCH — load when player leaves the manor before PR_07:**

Trigger conditions (any of these = load `KM_PR_BRANCH_WALKOUT.md`):
- Player walks out of an argument with Jamandi (charter refusal, evidence dispute, custody friction)
- Player executes Malak in the courtyard and leaves rather than face household consequences
- Player decides to leave during PR_02/PR_03/PR_06 for any reason
- Jamandi asks the player to leave (rare; relationship score collapse)

The walkout branch contains the full cascade timeline (poison → assassins → fire), Kassil's rescue window, Jamandi's south-window exit, post-fire confrontation, and Kassil morning-meeting alternative. **PR_07/PR_08 do NOT fire if the player has left**; the branch routes directly to PR_09 (modified) or Ch1 (alternative entry).

**Lookup files (NOT atomic — referenced by pointer from PR_NN files):**

```
KM_Prologue_Systems.md  — Tartuccio full interrupt system (Fear/Confidence
                            scales, Paranoia/Assurance, player action modifiers)
KM_Prologue_Systems.md — Hall-wide Wariness 0-3 per NPC present at the
                            banquet; hearsay-only escalation; detective huddle
                            mechanic; Prologue-scope ONLY (drops at PR_09 close)
KM_Prologue_Systems.md — 🐍 STATUS BANNER spec: mandatory above choice
                            menu every feast response (PR_02-PR_09 pre-exposure)
                            with Position + Earshot tier + Confidence +
                            Headcount + arrival countdown progress bar.
                            Supersedes prior render slot for at-a-glance state.
KM_Prologue_Systems.md       — Full companion Phase 4.5 approach scripts +
                            commitment close lines (all 11 + WotR QL)
KM_Prologue_Systems.md         — Tartuccio table feast behavior + departure narration
KM_Prologue_Systems.md     — JSON Export Block template for PR_09 save block
KM_Prologue_Systems.md         — Ambient companion presence rules (Phases 1–4)
KM_NPCs.md        — Jamandi, Kassil, Kesten, Tartuccio Quick Tags
KM_Companions.md + _B + _C + _D — Companion profiles + scripted openers context
KM_CombatTurn.txt — FIXED combat-map manifest (guest-room assassin fight) +
                            eRmaC Guisarme combat values / kill resolution. Load for
                            the night-attack beats (prologue_night / prologue_corridor).
                            Copy the fixed grid layer BYTE-FOR-BYTE — never redraw.
```

**DELETED legacy monolithic files (removed 2026-05-08 — use atomic PR_NN files):**

```
KM_Prologue.md     — DELETED → content split across PR_01–PR_03; Jamandi crisis behavior → KM_NPCs.md
KM_Prologue_P6.md  — DELETED → content in PR_04–PR_05
KM_Prologue_P2.md  — DELETED → content in PR_06–PR_07
KM_Prologue_P3.md  — DELETED → content in PR_08–PR_09
```

**⛔ CRITICAL MECHANICS (check these on every Prologue response):**
- Jamandi's duel: Frost Giant is HER kill — player does NOT target it (`.fail 35`)
- Carousel earshot scoring: ALL companions score on EVERY player statement
- Tartuccio UNKILLABLE PROTOCOL active through all Prologue beats
- PR_09 six-proof exit: XP audit + state final + save block all required

---

## 🗺️ CHAPTER 1 — STOLEN LAND

**Main file:** KM_Ch1.md
**Required reads:**

```
KM_Ch1.md                — Main chapter content, Stag Lord arc
KM_Ch1.md         — Save block for Ch1→Ch2 transition
KM_Kingdom.md            — Kingdom founding sequence
KM_Map.md                — Greenbelt hex map
KM_Map.md              — Extended map data
KM_Exploration.md        — Exploration mode rules, hex travel
KM_Kingdom.md    — Travel events, camp rules, nighttime danger
KM_Bestiary.md           — Core encounters
KM_Bestiary.md         — Stag Lord, Aecora, named bosses
KM_Loot.md               — Chapter loot tables + merchants
KM_Items.md + KM_Items_B.md — Item lookups (A: weapons/armor/consumables/wondrous/runes; B: mundane/expanded/special/wilderness/traps/AP-pulls)
KM_Kingdom.md        — Disposition tags, morale, reactive NPCs
KM_Kingdom.md    — Raider encounters (from Ch1 onward)
KM_CompanionQuests.md  — Companion quest triggers (A-L)
KM_CompanionQuests.md  — Companion quest triggers (M-R)
KM_CompanionQuests.md  — Companion quest triggers (S-V)
KM_CompanionQuests.md  — Companion quest triggers (W-Z)
KM_CompanionQuests.md           — Ekundayo recruitment (Ch2 trigger but context starts here)
```

---

## 👑 CHAPTER 2 — TROLL TROUBLE & SEASON OF BLOOM

**Main file:** KM_Ch2.md + KM_Ch2.md
**Required reads:**

```
KM_Ch2.md                — Troll Trouble questline
KM_Ch2.md             — Season of Bloom questline
KM_Kingdom.md            — Kingdom turn system activates fully
KM_Kingdom.md      — 18 advisor events across Ch2-6
KM_Kingdom.md   — Class-specific stronghold events
KM_War_Systems.md     — .orders command, leadership roles
KM_Kingdom.md    — .board bounty system (Ch2+)
KM_War_Systems.md           — .wartable strategic overview
KM_Bestiary.md         — Hargulka, trolls, Bloom creatures
KM_Mythic_Systems.md        — Ch2 examination tables
KM_Mythic_Systems.md            — Ch2 debate encounters
KM_Mythic_Systems.md          — Devoted/Hostile companion abilities
KM_Mythic_Systems.md         — Urgency stages, companion ultimatums
KM_Mythic_Systems.md             — Dream sequences (unlock Ch2)
KM_Mythic_Systems.md            — Between-chapter scenes
KM_Mythic_Systems.md — Multi-step CYOA vignettes
KM_Mythic_Systems.md           — Crafting system (unlocks Ch2)
KM_World_Systems.md         — Public reputation by chapter
KM_War_Systems.md        — Brotherhood relationship tracking
```

---

## 🏛️ CHAPTER 3 — THE VARNHOLD VANISHING

**Main file:** KM_Ch3.md
**Required reads:**

```
KM_Ch3.md              — Varnhold investigation, Vordakai's tomb
KM_Bestiary.md         — Vordakai, cyclopes, undead
KM_Mythic_Systems.md     — Tomb dungeon puzzles
KM_Mythic_Systems.md         — Mobile base (Ch3+)
KM_Kingdom.md            — Kingdom stability checks
KM_CompanionQuests_A-D.md — Amiri Pariah trigger, Harrim, Jaethal quests
KM_Mythic_Systems.md             — Nyrissa dreams escalate
```

---

## ⚔️ CHAPTERS 4-7 — TWICE-BORN WARLORD, WAR, BLOOM, FINALE

**Main file (per chapter — upload only the one you're playing):** KM_Ch4.md · KM_Ch5.md · KM_Ch6.md · KM_Ch7.md
**Required reads:**

```
KM_Ch4.md (Armag) · KM_Ch5.md (Irovetti) · KM_Ch6.md (Nyrissa) · KM_Ch7.md (finale)
KM_Bestiary.md         — Armag, Irovetti, Nyrissa stat blocks (authoritative)
KM_War_Systems.md         — Army battles (Ch5 war)
KM_War_Systems.md             — 3 scripted sieges (Capital, Pitax, Bloom)
KM_Mythic_Systems.md        — Mythic path choice (Ch5 pivotal)
KM_War_Systems.md   — L10/L15 specializations
KM_Endings.md                   — 5 endings with narration (split from KM_Mythic_Systems.md v95.9)
KM_Ch6.md     — Ch6 Linzi resurrection quest (if linzi_dead)
KM_Kingdom.md            — Kingdom collapse mechanics (Ch6)
KM_Kingdom.md        — Final reactivity layer
```

---

## 🔄 UNIVERSAL SYSTEMS (load whenever triggered)

```
KM_PlayerHelp.md            — Best run scoring at chapter end
KM_ChapterSelect.md      — Chapter select menu (session start)
KM_BuildGuide.md        — Character creation (session start)
KM_Builds.md + _A–M      — 13 build sub-files for class lookups
KM_BuildGuide.md           — Level-up rules
KM_Companions_Behaviors_B.md — Companion leveling (split from Behaviors v95.9)
KM_Companions_Behaviors_B.md — Companion build lore fit table + Combat AI + selection reference
KM_Companions_Behaviors_B.md — Scaled companion stat blocks
KM_Companions_StateVoice.md — Relationship state voice lines
KM_Companions_Behaviors.md — Companion personal agendas + inter-companion relations + incompatibility + question-gated nodes + ambient + banter (Systems 0–4)
KM_Mythic_Systems.md       — Disposition tag system (all chapters)
KM_Spells.md      — Spell build references
KM_Spells.md — Spell data
KM_Spells.md — Spell data
KM_Game_Subsystems.md   — Secrets of Magic / Dark Archive content
KM_Game_Subsystems.md     — Rage of Elements subsystems
KM_Combat_Systems.md        — Vanguard/rearguard/reserve
KM_Combat_Systems.md         — ⛔ Full-party tactical split-combat (6+ party
                            encounters auto-split into Vanguard vs Rearguard).
                            Load when combat initiates with 6+ party members.
KM_Combat_Systems.md          — Dice mode (virtual default)
KM_World_Systems.md        — Crime and legal consequences
KM_Items.md   — Shadowbane material descriptions
KM_Documents.md     — In-world document templates
KM_PlayerHelp.md         — Player quickstart reference
KM_Items.md     — ⛔ Expanded magic items (spellhearts, eye slot, rods,
                            staves, cursed, magical utility). Load when an
                            item from this pool is looted, bought, or identified.
KM_Items.md   — ⛔ Wilderness/utility items (herbalism, river/travel,
                            mount/familiar, bandolier, fey charms, ceremonial,
                            kingdom/stronghold gear). Load at Long Rest, camp
                            scenes, Kingdom turns, and fey encounters.
KM_World_Systems.md    — ⛔ Travel segment system. Load when the party begins
                            any overland journey. Defines segment count by mode
                            (foot/horse/carriage), segment display format, banter
                            rotation, and named route waypoints (Route A:
                            Restov→Oleg's). Add new named routes here.
KM_Signatures.md         — ⛔ Per-companion signature moves + unique powers
                            (PF2e-translated). Single file, Parts A–E.
                            Load when any companion is in the active party;
                            surface MOVE in combat menu.
KM_World_Systems.md     — Companion Needs panel (Rest/Purpose/Connection/
                            Recognition). Decay at rest, refill on acknowledgment.
                            Diagnostic for LivingWorld moods. `.needs [name]`.

```

---

## ⛔ VERIFICATION CHECKLIST — HARD GATE BEFORE ANY SCENE NARRATION

**⛔ The DM MUST output the filled checklist below BEFORE writing a single word of scene narration. Not after. Not during. BEFORE. If the checklist is not output, the scene has not been authorized to start. Any narration without a preceding checklist = `.fail 9`.**

**STEP 1 — SCENE FILES.** Look up the current scene in the sections above. Read EVERY listed file with the Read tool (not Grep, not search — Read).

**STEP 2 — SAVE BLOCK FILES.** If a save block was loaded, cross-reference it:
- `companion_picks` → for each companion, read their profile in KM_Companions.md / _B / _C / _D and their backstory file (KM_Backstories_W/I1/I2/I3)
- `companion_titles` → if any titles exist, read KM_Companions_Titles.md
- `npc_threads` → for each NPC with a non-empty thread, read their profile
- `story_flags` → if any flag references a system file (e.g. `nyrissa_awareness` → KM_Mythic_Systems.md), read it
- `game_options` → read response_length, min/max_paragraphs, npc_dialogue_beats_min — apply them

**STEP 3 — OUTPUT THE CHECKLIST.** Fill every field. Do not leave blanks.

```
══════════════════════════════════════════════════════════
SCENE VERIFICATION — [Scene Name]
══════════════════════════════════════════════════════════
SCENE FILES READ:
  ☑/☐ [filename] — [one-line summary of what you found]
  ☑/☐ [filename] — [one-line summary]
  ☑/☐ [filename] — [one-line summary]
  (every file from the scene list above — no skipping)

SAVE BLOCK FILES READ:
  ☑/☐ Companion profiles for: [list names from companion_picks]
  ☑/☐ Companion backstories loaded: [which backstory file(s)]
  ☑/☐ Companion titles: [list any titled companions + their title]
  ☑/☐ NPC threads active: [list NPCs with non-empty threads]
  ☑/☐ Game options: response_length=[X] min_paras=[X] max_paras=[X]
       npc_beats=[X]

CRITICAL MECHANICS CONFIRMED:
  ☑/☐ [mechanic 1 — e.g. "Directive Two gate window active"]
  ☑/☐ [mechanic 2 — e.g. "Malak keeps guards 30 paces from gate"]
  ☑/☐ [mechanic 3 — e.g. "Jamandi's duel is her kill, not player's"]
  (scene-specific — list the key rules that would be missed if
   supporting files weren't read)

NAMED NPCs IN THIS SCENE:
  [list every named NPC who appears, with one-word role]
  [confirm you read their profile — not generated from memory]

READY TO PLAY: ☑/☐
══════════════════════════════════════════════════════════
```

**STEP 4 — WAIT FOR PLAYER.** After outputting the checklist, say: *"Scene verified. Ready to begin."* Then WAIT. Do not start narrating until the player responds.

**If any box is ☐:** STOP. Search the file. Read it. Update the checklist. Do not play from memory. Do not proceed with unchecked boxes.

**If the DM outputs narration without a preceding checklist:** `.fail 9` — the scene was not verified. Any content in an unverified scene may be fabricated.

**If the DM checks ☑ on a file it did not actually Read:** `.fail 9` — false verification is fabrication.

**WHY THIS EXISTS:** The DM has repeatedly played scenes without reading supporting files. It missed Directive Two because it didn't read KM_PrePrologue_Setup.md. It missed Jamandi's duel rules because it didn't read KM_Prologue_P2.md fully. It fabricated companion builds because it didn't read KM_Companions_Behaviors.md. The checklist forces the DM to prove it read the files before it touches the scene. No shortcuts. Read the files.
