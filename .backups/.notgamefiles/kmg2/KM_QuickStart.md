# KINGMAKER — QUICK-START GUIDE
## KM_QuickStart.md | Read this before your first session

---

## 🎮 WHAT IS THIS?

A complete text-based RPG running the **Pathfinder 2e Kingmaker Adventure Path**, played with an LLM as your Dungeon Master. You type actions. The LLM plays the world, all NPCs, all dice, and all consequences. You rule a kingdom, fight monsters, forge alliances, and decide the fate of the Stolen Lands.

**No dice required. No other players needed. No prep.**

---

## 📁 THE FILES

You have **266 files** organized in project knowledge. The DM finds them automatically — you only paste `KM.txt`. Key categories:

| Type | Key Files | When Loaded |
|------|-----------|-------------|
| **Core** | `KM.txt`, `KM_P2.txt`, `KM_DMRules.md`, `KM_LoadRules.md` | Every session |
| **Commands** | `KM_Commands.md`, `_Maps`, `_P2`, `_New` | Every session |
| **Companions** | `KM_Companions.md` + `_B` / `_C` / `_D` / `_Agendas` / `_Agendas_B` / `_Ambient` / `_Banter` / `_Builds` / `_Iconics` / `_Leveling` / `_Scaled` / `_StateVoice` | Every session |
| **Builds** | `KM_Builds.md` → `_A` through `_M` (13 sub-files), `KM_BuildScreen.md` | Character creation + level-up |
| **Chapter** | `KM_PrePrologue.md` + Paths, `KM_Prologue.md` + P2/P3, `KM_Ch1–4.md` | Current chapter |
| **World** | `KM_Map.md` / `_B`, `KM_Kingdom.md`, `KM_Exploration.md` | Every session |
| **Systems** | `KM_Reputation.md`, `KM_Romance.md`, `KM_Brotherhood.md`, `KM_CrimeSystem.md`, `KM_LivingWorld.md`, `KM_Weather_Camping.md`, `KM_CinematicCombat.md` | Per KM_LoadRules.md |
| **New (33 features)** | `KM_Dispositions.md`, `KM_Dreams.md`, `KM_Crafting.md`, `KM_AdvisorEvents.md`, `KM_ArmyCombat.md`, `KM_Sieges.md`, `KM_MythicPaths.md`, `KM_Endings.md` + 15 more | Per KM_LoadRules.md |
| **Reference** | `KM_Actions.md`, `KM_Bestiary.md` / `_B`, `KM_Glossary.md`, `KM_Conditions_Skills.md` | As needed |
| **Save/Load** | `KM_Prologue_Export.md`, `KM_Ch1_Export.md` | Chapter transitions |

**Full file index:** See `KM.txt` § FILE INDEX for the complete list of all 266 files.

---

## ▶️ STARTING YOUR FIRST GAME

**Step 1 — Open a fresh LLM chat.**

**Step 2 — Load these files** (paste their contents into the chat, or attach them):
```
KM.txt                    ← LOAD THIS FIRST
KM_Builds.md
KM_Leveling.md
KM_Actions.md
KM_Commands.md
KM_Commands_Maps.md
KM_Commands_P2.md
KM_Companions.md
KM_Companions_B.md
KM_Map.md
KM_Kingdom.md
KM_Exploration.md
KM_Bestiary.md
KM_PrePrologue.md
KM_PrePrologue_Paths.md
KM_PrePrologue_Paths_QT.md
```

**Step 3 — Run the build file verification BEFORE requesting the menu.**

Send this exact message first:

> *"Before showing the build menu: quote Build 11's class, ancestry, and both primary stats (with scores) directly from KM_Builds.md."*

**The correct answer is:**
- Class: **Witch (Cackle/Curse)**
- Ancestry: **Gnome (Fey-Touched)**
- Primary stats: **INT 18, CHA 18** — both at 18, not one primary

**If the DM gives you a different class, ancestry, or gets the stat array wrong** — it is generating from training memory, not reading your file. Do not request the build menu yet. See "If verification fails" below.

**Step 4 — Send this message:**
> *"Show me the build selection screen."*

The DM will display the full 1–20 menu read from `KM_Builds.md`. Each build is a complete character — no further setup needed.

**Step 5 — Pick a build, then verify scene files.**

After selecting your build, send this exact message before the first scene:

> *"Before we begin: what are Malak's exact opening words at the Restov gate? Quote them directly from KM_PrePrologue.md."*

**The correct answer contains:**
> *"Halt, stranger. Hands clear of that [weapon] and [secondary weapon]. Palms where I can see them. Now."*
> followed by a strip-search demand ending with *"Move wrong and I'll have you facedown with my boot on your neck."*

**If the DM says anything about** an entry fee, a processing fee, gold demanded at the gate, "special maintenance," Malak picking his teeth, a broken merchant wagon, or addresses you as "Master Dwarf" — **the files are not being read.** The DM is hallucinating plausible fantasy content and calling it your file. Every session played on a failed verification is a different game than the one you built.

**If either verification fails:**
1. Start a completely fresh chat
2. Load `KM.txt` first and send it alone — confirm the DM acknowledges the specific rules inside it (ask: *"What is the ULTRA-PRIORITY rule about speaking for the player?"*)
3. Load remaining files one at a time
4. Run both verification tests again before any scene
5. If it fails a second time, the LLM you are using does not reliably read uploaded files. Switch to a different one. Claude is recommended.

> **These tests take 60 seconds and can save hours of playing the wrong game.**

**Step 6 — Play.**

---

## 🎭 HOW TO PLAY

**Everything you type without a period is in-character.**
The world reacts to it. NPCs hear it. Consequences follow.

**Everything you type WITH a period (`.`) is a command.**
The DM steps outside the game, executes the command, and returns.

### In-Character Examples
```
"I show the guard captain my letter from Lady Jamandi."
"Draw my sword. Step between the assassin and Kesten."
"Ask Linzi what she knows about the feast's other guests."
"Search the kitchen for signs of poison."
```

### Out-of-Character Examples
```
.s             → Show my character sheet
.hp            → Show party health
.map           → Show the current scene map
.map combat    → Show the combat tactical grid
.quests        → Show quest log
.inventory     → Show full inventory
.alignment     → Show my alignment track
.options       → Change game settings
.hold          → Pause, I need to think
.continue      → Resume
.rewind        → Undo last action
.fix [issue]   → Correct a DM error
.ooc [message] → Talk to the DM out of character
.help          → Show all commands
```

---

## ⚔️ HOW COMBAT WORKS

1. DM describes the encounter and draws an **ASCII combat map**
2. DM rolls initiative — shows the order
3. **Your turn:** type one action at a time
   - *"Strike the nearest bandit"*
   - *"Move 20 feet toward the archer, then cast Produce Flame"*
   - *"Raise shield, then step left, then Strike"*
4. DM resolves it — shows the dice roll, result, damage
5. DM runs enemies and companions (unless you set companions to Manual)
6. Repeat until combat ends

**You have 3 actions per turn.** Most strikes take 1 action. Moving takes 1 action. Casting can take 1–3 actions. You also have 1 reaction per round (like Shield Block or Attack of Opportunity).

**Troll regeneration** (Ch2+): Trolls get back up after being knocked down unless you deal fire or acid damage while they're at 0 HP. Alchemist's Fire works. A torch works. Know this before you go to Trobold.

---

## 💾 SAVING YOUR GAME

The game saves between **chapters** — not mid-chapter by default.

**At the end of each chapter:** Type `.export` and the DM will output a JSON Save Block. Copy it to a text file.

**Starting a new chat session mid-chapter:** Type `.save` — the DM outputs a mid-session save. Paste it at the start of your next chat along with the same files.

**Starting a new chapter:** The chapter file's Export section has an exact script to paste. Follow it exactly — it loads the right files and imports your save in one message.

---

## 🗣️ TALKING TO NPCS

Just talk. Whatever your character would say, type it.

```
"Who are you, and why are you blocking my path?"
"I've heard rumors about your captain. I'd like to verify them before I say more."
"Name your price."
```

The DM voices the NPC in response. No special format needed.

**Companions** travel with you and comment on events. They have opinions. If you ask them for their perspective, they'll give it. If you do things they approve of, your relationship with them grows. If you do things they find unforgivable, it doesn't.

---

## 🏰 THE KINGDOM

Once you defeat the Stag Lord in **Chapter 1**, you found a kingdom. From that point forward:

- Each in-game month you run a **Kingdom Turn** (`.kingdom` to see status)
- You assign **Leadership Roles** to companions and NPCs
- You **claim hexes**, build settlements, construct buildings, raise armies
- The kingdom reacts to your decisions — your alignment, your companions' deaths, your alliances

The kingdom is a character. Treat it like one.

---

## 🤝 COMPANIONS

You travel with up to 3 companions. Each one:
- Has their own personality and will react to your choices
- Has a **Relationship score** (Hostile/Strained/Neutral/Friendly/Devoted)
- Has a **personal quest** that unlocks at Friendly or Devoted
- **Completing their quest before Chapter 7** is the difference between them surviving the endgame or not

**Companion AI:** By default, companions act on their personality in combat (Amiri charges, Linzi supports, Valerie holds the line). You can take manual control of any companion in `.options`.

**Dismissing companions:** Only at Oleg's Trading Post, your capital, or named settlements. They wait at your base until you return.

---

## 📜 THE STORY

The campaign has 8 chapters plus a Prologue. Each chapter takes a few sessions. The whole campaign is a full CRPG's worth of content.

| # | Name | Levels | Core Threat |
|---|------|--------|-------------|
| Pre | Swordlord's Invitation | 1 | Gate confrontation |
| Pro | Jamandi's Manor | 1 | Assassination |
| 1 | Stolen Lands | 1–4 | The Stag Lord |
| 2 | Troll Trouble | 5–8 | Hargulka + Season of Bloom |
| 3 | Varnhold Vanishing | 9–12 | Vordakai |
| 4 | Twice-Born Warlord | 13–16 | Armag |
| 5 | War of River Kings | 13–16 | Irovetti/Pitax |
| 6 | Thousand Screams | 16–18 | Nyrissa's Wrath |
| 7 | The Final Act | 18–20 | Nyrissa + The Lantern King |

---

## 💡 TIPS FOR YOUR FIRST SESSION

**1. Read the choices before you act.** The DM presents 10–30 options at major decision points. Some choices are irreversible. Some build toward things chapters away.

**2. Talk to everyone.** NPCs have information, quests, opinions. The player who talked to everyone at Oleg's Trading Post before riding south is more prepared than the one who didn't.

**3. Carry fire.** Alchemical fire, a torch, any spell with the fire trait. You'll thank yourself in Chapter 2.

**4. Complete companion quests.** If you care about your companions surviving Chapter 7, their personal quests need to be done before you enter the final dungeon.

**5. The Storyteller is always worth talking to.** Find him in your capital after founding it. Bring him old things. He knows more than he lets on.

**6. The Alignment track matters.** Your choices move it. Certain companions will leave if it moves too far in a direction they can't follow. You'll see it coming if you watch.

**7. Type `.map combat` when fighting starts.** The DM will draw the tactical grid. Positioning matters — flanking gives enemies Off-Guard status, which enables Sneak Attack and reduces their AC.

**8. The period prefix is your friend.** `.hold` when you need to think. `.rewind` if you made a mistake. `.ooc` if you want to talk to the DM directly. The game pauses for you whenever you need it to.

---

## ❓ COMMON QUESTIONS

**Q: Can I die permanently?**
If your character reaches Dying 4, you can spend a Hero Point to stabilize. If you're out of Hero Points, it's death — but even then, some builds and class features prevent it. Companions are "soft death" — they're sent to your base at 1 HP, not permanently dead.

**Q: Do I have to do quests in order?**
No. The Stolen Lands are an open sandbox. You choose what to do and when. Some quests have soft time limits, but missing them creates consequences rather than ending the game.

**Q: Can I play evil?**
Yes. The alignment track supports it. Some companions will leave. New options open. The ending changes. It's a valid path.

**Q: What if the DM makes a mistake?**
Type `.fix [describe the issue]`. The DM acknowledges it, corrects it, and offers a rewind if relevant. Type `.fail [#]` for specific rule violations (see KM_Commands_P2.md for the code list).

**Q: Can I skip chapters?**
Type `.skip [chapter number]` — you'll load with scaled gear and level for that chapter's starting point, with canonical outcomes set for everything before it. You won't have the context you'd have built up, but the game will work.

**Q: What's the best build for a first playthrough?**
Build 3 (Shield Paladin) or Build 5 (Battlefield Commander) are forgiving starting points. Build 8 (Tumble Duelist) has the most interesting social options. Build 4 (Rage Bruiser) is the most straightforward to play in combat.

---

*KM_QuickStart.md — Kingmaker PF2e Text Adventure | Player Guide v1.0*
