# KINGMAKER — DM LOAD RULES & MENU SURFACING (PART B)
## KM_LoadRules_B.md | Pair-load with KM_LoadRules.md

> **DM:** Part B of the Load Rules. Always pair-load with `KM_LoadRules.md` (Part A covers Look Around, Romance, Brotherhood, Reputation, Crime, Living World, Banter, Agendas, Personal Chambers, Ambient, State Voice, Found Documents, Host Gathering, Master Menu Checklist, and Companion Titles & Regalia). This file covers the remaining subsystems (Dispositions through Reference Files).

---

## 🏷️ DISPOSITION TAGS (KM_Dispositions.md + KM_LivingWorld.md)

**Load trigger:** Load every session alongside KM_LivingWorld.md. Always active.

| Trigger | DM Action |
|---------|-----------|
| Player makes a choice fitting a tag | +1 to that tag silently |
| Tag reaches 3+ in any settlement | NPC dialogue references dominant tag |
| `.disposition` | Display all 5 tag values |

---

## 🔍 EXAMINATION (KM_Examination.md)

**Load trigger:** Every session. Always active.

| Trigger | Menu option to add |
|---------|-------------------|
| Any scene with examinable objects | "🔍 Examine [object]" for each visible object |
| `.examine [object]` | Fire examination procedure |

---

## ⚖️ DEBATES (KM_Debates.md)

**Load trigger:** When companions disagree, NPC negotiation stalls, or advisor conflict arises.

| Trigger | Menu option to add |
|---------|-------------------|
| Two companions disagree on action | "⚖️ Settle this with a Debate" |
| Stubborn NPC won't yield | "⚖️ Challenge them to a Debate" |
| Advisor conflict (KM_AdvisorEvents.md) | ".debate — have the advisors argue" |

---

## 💎 INFLUENCE (KM_Influence.md)

**Load trigger:** From Ch2 onward. Load every session.

| Trigger | DM Action |
|---------|-----------|
| Companion reaches Devoted (+2) | Unlock Devoted Passive, narrate scene |
| Companion reaches Hostile (−2) | Activate Dark Ability silently |
| `.influence [name]` | Show companion's influence status |

---

## ⏳ ULTIMATUMS (KM_Ultimatums.md)

**Load trigger:** When any companion quest or incompatibility countdown is active.

| Trigger | DM Action |
|---------|-----------|
| Quest/countdown at 50% | Set urgency Stage 1, narrate subtle cues |
| Quest/countdown at 75% | Stage 2, visible distress |
| Quest/countdown at 90% | Stage 3, fire ultimatum scene |
| Quest/countdown at max | Stage 4, companion acts |

---

## 🏛️ ADVISOR EVENTS (KM_AdvisorEvents.md)

**Load trigger:** During Kingdom Turns from Ch2 onward.

| Trigger | Menu option to add |
|---------|-------------------|
| Kingdom Turn Phase 4 (Events) | Present advisor event with 2-3 solutions |
| Spymaster "Monitor Advisors" order | Auto-detect advisor intrigue |

---

## 📋 STANDING ORDERS (KM_StandingOrders.md)

**Load trigger:** During Kingdom Turns from Ch2 onward.

| Trigger | Menu option to add |
|---------|-------------------|
| Kingdom Turn Phase 3 | ".orders — assign or change standing orders" |
| `.orders` | Display and modify all role orders |

---

## 📌 ADVENTURER BOARD (KM_AdventurerBoard.md)

**Load trigger:** When Adventurer's Guild building is constructed.

| Trigger | Menu option to add |
|---------|-------------------|
| In capital with Guild built | ".board — post bounties, hire parties" |
| `.board` | Display board interface |

---

## 🏴 BORDER CONFLICTS (KM_BorderConflicts.md)

**Load trigger:** From Ch2 onward during Kingdom Turns.

| Trigger | DM Action |
|---------|-----------|
| Kingdom Turn, d6 = 5-6 | Raid event fires |
| Faction at Hostile | Automatic raid |
| `.wartable` | Show active threats |

---

## 🏰 STRONGHOLD EVENTS (KM_StrongholdEvents.md)

**Load trigger:** During Kingdom Turns from Ch2 onward.

| Trigger | DM Action |
|---------|-----------|
| Kingdom Turn Phase 4, 1/chapter | Fire class-specific stronghold event |

---

## 🌙 DREAMS (KM_Dreams.md)

**Load trigger:** Every session. Check flags at Long Rest.

| Trigger | DM Action |
|---------|-----------|
| Long Rest + dream flag conditions met + cooldown passed | Fire dream sequence |
| Companion at Devoted + Long Rest | Check companion dream intrusion |
| Morale ≤ 2 or companion near-death | Check nightmare triggers |

---

## 🌀 LIMINAL SCENES (KM_Liminal.md)

**Load trigger:** At chapter boundaries (after export, before next chapter).

| Trigger | DM Action |
|---------|-----------|
| Chapter export completed | Fire liminal scene before next chapter loads |

---

## 📖 SCRIPTED INTERACTIONS (KM_ScriptedInteractions.md)

**Load trigger:** During exploration when party enters a hex with a scripted interaction.

| Trigger | DM Action |
|---------|-----------|
| Hex contains scripted interaction trigger | Fire the interaction (3-5 nodes) |

---

## 🔨 CRAFTING (KM_Crafting.md)

**Load trigger:** When player has known recipes and is in Downtime or at Mobile Base.

| Trigger | Menu option to add |
|---------|-------------------|
| Downtime + known recipes | "🔨 Craft an item" |
| `.craft`, `.recipes` | Display crafting interface |

---

## 🗺️ DUNGEON PUZZLES (KM_DungeonPuzzles.md)

**Load trigger:** When party enters a dungeon with a multi-room puzzle.

| Trigger | DM Action |
|---------|-----------|
| Chapter file references a dungeon puzzle | Load and run the puzzle |

---

## 🚀 MOBILE BASE (KM_MobileBase.md)

**Load trigger:** When Mobile Base is commissioned (Ch2+).

| Trigger | Menu option to add |
|---------|-------------------|
| Traveling with base | "🚀 Check base status" / "Craft on the road" |
| Every 3 hexes traveled | Roll d8 for travel event |

---

## ⚔️ ARMY COMBAT (KM_ArmyCombat.md)

**Load trigger:** From Ch4 onward when army engagement begins.

| Trigger | DM Action |
|---------|-----------|
| Army battle scripted in chapter | Load and run army combat |
| `.wartable` | Display army roster |

---

## 🏰 SIEGES (KM_Sieges.md)

**Load trigger:** When a siege event fires (Ch5+).

| Trigger | DM Action |
|---------|-----------|
| Enemy army reaches settlement | Load and run siege phases |

---

## 📊 WAR TABLE (KM_WarTable.md)

**Load trigger:** From Ch4 onward.

| Trigger | Menu option to add |
|---------|-------------------|
| `.wartable` | Display full strategic overview |
| Kingdom Turn start (Ch4+) | Auto-display war table |

---

## 🌟 PRESTIGE UPGRADES (KM_PrestigeUpgrades.md)

**Load trigger:** When player reaches Level 10 or 15.

| Trigger | DM Action |
|---------|-----------|
| Player level-up to L10 | Present L10 specialization choice |
| Player level-up to L15 | Present L15 specialization choice |

---

## 🔮 MYTHIC PATHS (KM_MythicPaths.md)

**Load trigger:** Chapter 5, at the pivotal mythic choice moment.

| Trigger | DM Action |
|---------|-----------|
| Ch5 mythic trigger scene | Present 4 path options |
| Mythic level milestones | Unlock next ability |

---

## 🏆 ENDINGS (KM_Endings.md)

**Load trigger:** Chapter 6 opening. Check all ending flags.

| Trigger | DM Action |
|---------|-----------|
| Ch6 start | Silent eligibility check |
| Final scene resolves | Fire appropriate ending narration |

---

## 🎮 CHAPTER SELECT (KM_ChapterSelect.md + KM_BestRun.md)

**Load trigger:** Session start — always loaded with KM.txt.

| Trigger | DM Action |
|---------|-----------|
| Step 4.5 complete (setup save block output) | Display Chapter Select menu |
| Player picks later chapter | Check KM_BestRun.md first, then canonical defaults for gaps |
| Player picks Pre-Prologue | Proceed to KM_PrePrologue.md normally |
| Player types `.override` after canonical block | Show skipped-decision override menu |
| Chapter export block output | Auto-score run, compare to stored best, output Best Run if new record |
| Player types `.bestrun force` | Force-save current run as Best Run regardless of score |
| Player types `.score` | Display current session Run Quality Scorecard mid-chapter |

---

## 🔁 NEW GAME+

**Load trigger:** After any ending completes.

| Trigger | DM Action |
|---------|-----------|
| Ending narration delivered | Offer NG+ or Fresh Start |

---


## ✨ COMPANION SIGNATURES (KM_Signatures_A/B/C/D/E.md)

Active-party companion → surface MOVE in combat menu. Reset per-use counters at Long Rest / 24-hr / encounter start. A/B cover Sections A/B; C covers Section C; D/E cover Section D. Not listed = preset only; no fabrication.

---

## 🧬 ANCESTRY GUIDE (KM_AncestryGuide.md)

Step 3 → show class's ancestry block (★/2-5/OK/AVOID); enforce REQUIRED picks (Giant Instinct, Ancient Elf dips, etc.); note off-list trade-off; ask about free Versatile Heritage; record both `ancestry` + `heritage`.

---

## 🧭 BUILD GUIDE (KM_BuildGuide_A.md · KM_BuildGuide_B.md)

**Load trigger:** Load alongside KM_BuildScreen.md during character creation
(Mode A Preset path). Part A covers classes 1–13 (Alchemist–Inventor), Part B
covers 14–27 (Investigator–Wizard).

**Display rule:** Every time the DM shows a class's build list from BuildScreen,
it MUST also display that class's guide block (verbatim) immediately after.
This gives the player ★ recommendations, ⚠️ warnings, specialty, preferred
race, weaknesses, and alt-build pointers before they commit.

| Trigger | DM Action |
|---------|-----------|
| Player picks a class at Step 2 | Show BuildScreen list + matching BuildGuide block |
| Player asks "which build should I pick?" | Recommend ★ builds, match to stated play style |
| Player picks a ⚠️ build | One-time heads-up with ★ alternative; respect their choice |
| Player picks the alt-build pointer | Display both guide lines side-by-side to compare |
| Player's ancestry differs from preferred | Note trade-off during ancestry confirmation; do NOT block |

---

## 📈 LEVELING (KM_Leveling.md + KM_Companions_Leveling.md + KM_Companions_Builds.md + KM_Companions_Scaled.md)

**Load trigger:** Load KM_Leveling.md every session. Load the others when a level-up fires.

| Trigger | DM Action |
|---------|-----------|
| Player XP crosses threshold | Load KM_Leveling.md; run player level-up procedure; then run all companion level-ups simultaneously |
| Save block has `level_up_available: true` at session start | Fire the full level-up menu in the FIRST response — before any scene narration or recap. Do NOT narrate, summarize, or wait for input first. See KM_DMRules_B.md § XP AWARD SYSTEM. |
| Companion level-up (Sections A/B, #1–85) | KM_Companions_Leveling.md — full maps for key companions; Quick Reference boost table for all |
| Companion level-up (Sections C/D, #86–248) | KM_Companions_Leveling_B.md — compact seeds (build + boost priorities + pick path) |
| `.respec` or custom build selection | KM_Companions_Builds.md for lore-fit table |
| `.fail 29` | Companions not leveled same response as player — violation |

---

## 🗡️ COMPANION QUESTS (KM_CompanionQuests_A.md · _B · _C · _D · KM_Ekundayo.md)

**Load trigger:** Load the relevant part file when a companion quest trigger fires. Check triggers each session for active party companions.

| Trigger | DM Action |
|---------|-----------|
| Companion relationship ≥ Friendly + chapter threshold met | Check that companion's quest entry; fire opening scene if not yet started |
| Quest scene in progress | Keep part file loaded until quest resolves |
| Ekundayo recruitment conditions met (Ch1) | Load KM_Ekundayo.md; run recruitment scene |
| `[name]_quest = incomplete` in save block | Surface quest prompt in next available menu |
| Companions A (1–6): Amiri, Linzi, Valerie, Harrim, Tristian, Nok-Nok | KM_CompanionQuests_A.md |
| Companions B (7–12): Jaethal, Kalikke/Kanerah, Octavia, Regongar, Lem | KM_CompanionQuests_B.md |
| Companions C (Section C Iconics — Seelah, Valeros, Kyra, Sajan, and others) | KM_CompanionQuests_C.md |
| Companions D (WotR #17–45 + Section C/D #86–248) | KM_CompanionQuests_D.md |

---

## ✨ SPELLS (KM_Spells_Builds.md · KM_Spells_Arcane_Primal.md · KM_Spells_Divine_Occult.md · KM_SoM_DA_Encounter.md · KM_RoE_Subsystems.md)

**Load trigger:** Load when a spellcaster is active in the party. Load the relevant sub-file when a specific spell or rule is needed.

| Trigger | DM Action |
|---------|-----------|
| Player or companion prepares/casts a spell | Load the appropriate tradition file to verify spell data |
| Arcane or Primal spell | KM_Spells_Arcane_Primal.md |
| Divine or Occult spell | KM_Spells_Divine_Occult.md |
| Build-specific spell lists (what does this build prepare?) | KM_Spells_Builds.md |
| Kineticist impulse, Secrets of Magic, or Dark Archive spell | KM_SoM_DA_Encounter.md |
| Rage of Elements impulse, undead void spell, or firearm rule | KM_RoE_Subsystems.md |
| `.spells` command | Load relevant tradition file + KM_Spells_Builds.md |

---

## 🎒 LOOT & ITEMS (KM_Loot_Items_Ref · _Merchants · KM_Items_Expanded · _Wilderness · _Traps · _Mundane · _APPulls)

**Load trigger:** When distributing loot after combat or when the player visits a merchant.

| Trigger | Menu option to add |
|---------|-------------------|
| Combat ends with lootable enemies | Run loot procedure: load KM_Loot_Items_Ref.md; apply Best Fit + Opinion Score effects |
| Player visits a merchant | Load KM_Loot_Merchants.md; display merchant inventory |
| `.loot` | Display pending loot screen; claim or treasury |
| Item distributed to non-best-fit companion | −3 Opinion best-fit; +3 recipient |
| Spellheart, eye slot, rod, staff, cursed, magical utility identified/looted | Load KM_Items_Expanded.md |
| Herbalism, river, mount, familiar, bandolier, fey, ceremonial item | Load KM_Items_Wilderness.md |
| Camping / Long Rest | Load KM_Items_Wilderness.md (herbalism + travel) |
| Kingdom Turn | Load KM_Items_Wilderness.md (Kingdom & Stronghold Gear) |
| Fey / First World content | Load KM_Items_Wilderness.md (Fey Charms) |
| Cursed item identification | Load KM_Items_Expanded.md § CURSED |
| Trap / snare detected, disarmed, or crafted | KM_Items_Traps.md |
| Mundane shop / starting gear / preset pack | KM_Items_Mundane.md |
| AP-sourced item (Stolen Fate, Sky King, Tusk, etc.) | KM_Items_APPulls.md |
| Heritage scaling query | KM_Heritages.md § SCALING |

---

## 🎭 PARTY SYSTEM & GAME MODES (KM_PartySystem.md · KM_GameModes.md)

**Load trigger:** Load both every session. These are passive rule files — no menu surfacing needed.

| Trigger | DM Action |
|---------|-----------|
| Player splits party or assigns vanguard/rearguard | KM_PartySystem.md — apply split-force rules |
| Player changes dice mode (`.dice virtual` / `.dice player`) | KM_GameModes.md — apply the selected mode |
| Session start | Both files loaded; apply defaults (Virtual dice, full party) |

---

## 📚 REFERENCE FILES (load on demand — no session trigger)

These files are looked up reactively when specific content is needed. The DM searches project knowledge for them; they do not need to be pre-loaded.

| File | Load When |
|------|-----------|
| `KM_Conditions_Skills.md` | A condition or skill rule needs verification |
| `KM_Glossary.md` | A game term needs definition |
| `KM_Armor_Appearance.md` | Player equips or examines armor |
| `KM_Handouts.md` | A scripted document is found (see Handouts list) |
| `KM_Puzzles.md` | A puzzle scene fires outside of KM_DungeonPuzzles.md |
| `KM_TableFeatures.md` | Panel layout or table format is needed |
| `KM_Backgrounds.md` | Player selects a background during character creation |
| `KM_Backstories_W/I1/I2/I3` | Player selects a backstory or DM needs NPC backstory context |
| `KM_Backstories_CRPG_B / Misc_ext` | Auto-load with parent file — voice supplements for stranded companions |
| `KM_CharCreate.md` | Player selects Custom Character (Mode B) at session start |
| `KM_CompanionIndex.md` | DM needs to look up a companion number → name mapping |
| `KM_Companions_Iconics.md` | Companion selection screen (Pick-10); iconic profiles |
| `KM_Map_B.md` | Extended map content needed beyond KM_Map.md |
| `KM_NPC_Relations_A.md · _B · _C` | Opinion scoring: _A covers KM CRPG companions; _B covers Iconics, WotR, and Story NPCs; _C covers Section D companions |
| `KM_Rearguard.md` | Rearguard assignment rules |

---

*KM_LoadRules.md — Kingmaker PF2e Text Adventure | Load Rules & Menu Surfacing v3.0*
*Updated: Added load rules for 23 new system files (Dispositions, Examination, Debates, Influence, Ultimatums, AdvisorEvents, StandingOrders, AdventurerBoard, BorderConflicts, StrongholdEvents, Dreams, Liminal, ScriptedInteractions, Crafting, DungeonPuzzles, MobileBase, ArmyCombat, Sieges, WarTable, PrestigeUpgrades, MythicPaths, Endings, NewGamePlus).*
*Updated: Added KM_CrimeSystem, KM_LivingWorld, KM_FoundDocuments, KM_Companions_Ambient,*
*Personal Chambers, Host Gathering, Romance Gifts & Activities, mandatory Look Around rule,*
*KM_Companions_Agendas + _B/_C/_D/_E (208-companion agendas, inter-companion*
*relations, and incompatibility system), and KM_Companions_StateVoice (score-state voice,*
*threshold crossing events, romance jealousy & rivalry).*

*KM_LoadRules_B.md — Kingmaker PF2e Text Adventure | Load Rules Part B v1.0*
