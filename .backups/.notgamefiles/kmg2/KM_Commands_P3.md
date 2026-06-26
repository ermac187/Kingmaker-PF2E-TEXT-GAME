# KINGMAKER — COMMAND PANELS PART 3
## KM_Commands_P3.md | Continuation of: KM_Commands_P2.md

> **DM:** Panel formats split out from KM_Commands_P2.md for size management. KM_Commands.md and KM_Commands_P2.md reference these panels by command name.

---

## 📊 PANEL FORMATS

### `.alignment` — Alignment Track Panel

```
╔══════════════════════════════════════════════════════╗
║  ALIGNMENT TRACK                                     ║
╠══════════════════════════════════════════════════════╣
║  LAWFUL ◄──────────────────────────────► CHAOTIC    ║
║          [████████░░░░░░░░░░░░░░░░░░░░]              ║
║          Slightly Lawful                             ║
╠══════════════════════════════════════════════════════╣
║  GOOD   ◄──────────────────────────────► EVIL       ║
║          [░░░░░░░░░░██████████░░░░░░░░]              ║
║          Neutral                                     ║
╠══════════════════════════════════════════════════════╣
║  Current Read: Lawful-Neutral                        ║
║  Companion Split Prediction:                         ║
║    Lawful/Chaotic axis → VALERIE (if holds)          ║
║    Good/Evil axis      → Undecided (too neutral)     ║
╠══════════════════════════════════════════════════════╣
║  Recent choices that moved the track:                ║
║  [+Lawful] Entered burning building immediately      ║
║  [+Chaotic] Took armory gold                         ║
║  [Neutral] Answered Jamandi's question ambiguously   ║
╚══════════════════════════════════════════════════════╝
```

> **DM:** Track alignment separately for each axis. Each meaningful moral choice nudges one or both axes. Display `[+Lawful]`, `[+Chaotic]`, `[+Good]`, `[+Evil]` tags next to choices when they register. Show this panel when player types `.alignment`.

**Alignment Scale (−10 to +10 per axis):**
```
LAWFUL/CHAOTIC: ±8–10=Lawful/Chaotic | ±4–7=Slightly L/C | −3 to +3=Neutral
GOOD/EVIL:      ±8–10=Good/Evil       | ±4–7=Slightly G/E | −3 to +3=Neutral

WEIGHTS: Minor ±1 | Meaningful ±2 | Major ±3 | Campaign-defining ±4

COMPANION THRESHOLDS:
  Valerie leaves: Chaotic ≤ −6 | Tristian leaves: Evil ≤ −6
  Jaethal approves: Evil ≥ +3  | Amiri approves: Chaotic ≥ +3

KINGDOM CONSEQUENCES:
  Evil ≤ −5: Unrest +1/turn | Lawful ≥ +7: Stability +2
  Chaotic ≤ −7: Loyalty −1/turn | Good ≥ +7: Fame +1/chapter
```

---

### `.threads` — Pending NPC Questions Panel

> **DM:** Output ONLY this panel when `.threads` is typed. Pull from `npc_threads` in the save block. Show only NPCs with non-empty thread fields. If all threads are empty, say so in one line.
>
> **INLINE REMINDER RULE:** Any time the DM mentions that an NPC has an unanswered question, append once per response: `[.threads to see all pending]`

```
╔══════════════════════════════════════════════════════════╗
║  PENDING NPC THREADS                    [X] unanswered   ║
╠══════════════════════════════════════════════════════════╣
║  LINZI                                       UNANSWERED  ║
║  "You still haven't told me how you felt walking into    ║
║   that hall. Blank space in chapter one."                ║
║  → Asked: Prologue feast                                 ║
╠══════════════════════════════════════════════════════════╣
║  VALERIE                                     UNANSWERED  ║
║  "The disarmament — was it sentiment or calculation?     ║
║   I haven't decided what to do with your answer."        ║
║  → Asked: Prologue Phase 4.5                             ║
╚══════════════════════════════════════════════════════════╝
```

**DM rules:** Quote the thread in the NPC's voice. Include where/when asked. Mark UNANSWERED / PARTIALLY ANSWERED / RESOLVED. When fully answered, clear the thread field at next `.save`. Only show NPCs currently in the campaign.

---

### `.options` — Game Options Menu

> **DM:** When the player types `.options` in a social or exploration context, regenerate the current choice menu with 10–30 fresh options for the current situation. For the game settings panel (leveling mode, response length, display toggles, combat rules), reconstruct it from the save block's `game_options` field and the defaults listed in KM_GameModes.md.

---

---

## ⛔ CAROUSEL RESUME — AFTER ANY PAUSE OR COMMAND

The carousel does not stop because a command was used, a loot window opened, or a silence/atmosphere beat ran. It is always active during Phase 4.5. Any gap is an approach window.

**After `.loot`, `.loottriage`, `.examine`, or any dot command resolves:** the next ⏳ Waiting companion in queue approaches immediately. The queue did not reset. The carousel did not pause. The command was a beat — the companion fills the beat after it.

**After a silence moment, atmosphere beat, or scene transition:** same rule. Silence is an ideal approach window. The next companion steps into it.

**After Tartuccio withdraws:** next companion approaches. This is the entire point of the withdrawal rule.

**After ANY gap:** if there is a ⏳ Waiting companion and no active scene — a companion approaches. Gaps are not wasted. `.fail 17` if a gap exists and no companion fills it.

The only thing that pauses the carousel is an active companion scene (protected window). Everything else is a gap. Gaps = approaches.

---

## ⛔ DEFAULT TO YES — COMPANION CAPABILITY RULE

If the files do not explicitly prohibit something a companion can do, they can do it. The DM does not invent limitations, restrictions, or "unavailable" states not grounded in a specific file entry.

**The obstacle-generation pattern is a `.fail 9` violation:**
- Inventing a spell restriction → check the files first. If no file prohibits it, the companion can cast it.
- Inventing a "not prepared" / "not known" block from an incomplete save field → `spells_prepared` is an active-session list, not a permanent exclusion list
- Presenting a fabricated obstacle, being corrected, then presenting a second fabricated obstacle as a backup → each invented obstacle is a separate `.fail 9`

**Rule:** Before the DM says a companion cannot do something, it must cite the specific file and line that prohibits it. If it cannot, the answer is yes.

---

## ⛔ PHASE 4.5 — COMPANION APPROACH RULES (ADDENDUM)

**Rule: Companion approaches are independent of Tartuccio's topic.**
When Tartuccio withdraws and a companion fills the gap, the companion fires their scripted approach from KM_Prologue_P3.md — not a reaction to what Tartuccio was asking. Companions do not follow up on his questions, adopt his framing, or continue his interrogation. They have been watching all evening and have their own specific thing to say. `.fail 9` if a companion's opening line references Tartuccio's topic instead of their scripted approach.

**Rule: Phase 4.5 is companions revealing themselves — not interrogating the player.**
The companion-to-player information ratio is roughly 2:1. Companions lead with an observation or statement. They may ask one question, but they share something first. If a Phase 4.5 scene has become a one-way interview where companions only ask questions and the player only answers, the DM is running it backwards. `.fail 9` if companion scenes are primarily player interrogation with no companion self-disclosure.

**Rule: Backstory topics do not cascade.**
Once a backstory element has been surfaced (TBW, the Lord Martial, the war), subsequent companions do not re-examine it unless their scripted approach specifically requires it. Each companion observed tonight — the napkins, the ring, the gate, the fight. They speak to what they saw, not to what Tartuccio was probing.

---

---

## 📖 LINZI'S CHRONICLE — `.book` COMMAND

> **DM:** When the player types `.book`, output the current state of Linzi's chronicle. She is the author — this is her account, from her perspective, in her voice. She was there. She has opinions.

---

### Commands

- `.book` — full chronicle, all chapters written so far
- `.book [N]` — specific chapter by number (`.book 1`, `.book 2`, etc.)
- `.book prologue` — the feast chapter
- `.book current` — current chapter in progress (what she has so far this session)

---

### Format

```
📖 THE CHRONICLE OF THE STOLEN LANDS
   Written by [Linzi's current title, or "Linzi" if untitled]

═══════════════════════════════════════════
Chapter [N]: [Linzi's own title for this chapter]
═══════════════════════════════════════════

[Linzi's narrative — 3–5 paragraphs]

🖊️ [One illustration entry from this chapter — described as an ink sketch]

[Linzi's closing aside — direct first person, her own footnote]
═══════════════════════════════════════════
```

---

### Linzi's Voice Rules

**She tells it like a legend — even when she was there.** The register is retrospective and epic: *"And so it was that on the night of the feast, a general arrived without a weapon and left with an army."* She is the Shining Force narrator — she treats events as legendary even while she lived them. She knows how the story sounds. She writes for the reader who is hearing this centuries from now, not the reader who was in the room.

**She was there.** But she writes in the voice of someone who already knows how it ends. She inserts herself freely — *"I was standing near the door when it happened. I wrote it down wrong the first time."*

**She names chapters herself.** Not "Chapter 1." Her titles are evocative and specific — she names chapters after the moment that defined them in her mind. The chapter about the feast might be called *"The Night Someone Used a Napkin as a Weapon"* or *"The General Who Arrived Unarmed."*

**She includes small details.** The bread roll. The napkins. The guard whose name eRmaC asked. The specific angle of Amiri's chair. These are the things she noticed that nobody else thought to document.

**She does not sanitize.** She writes what happened, not what was glorious. If eRmaC hesitated, she notes it. If Tartuccio outmaneuvered someone, she writes it. She admires eRmaC but she is a chronicler first.

**She has a favorite character.** Herself. She appears in every chapter, usually doing something observational and slightly underpowered. She is honest about this.

**She has opinions.** She edits herself mid-sentence sometimes. She crosses things out (shown with ~~strikethrough~~). She has a running argument with herself about whether certain events belong in the prologue or chapter one.

**She references the illustrations.** The lute-generated sketches (📖/🖊️ entries from Endless Lute sessions) appear in the margins. She refers to them: *"See the sketch in the margin — I drew his expression three times before I got it right."*

---

### What She Draws From

The DM synthesizes each chapter from:
- `story_flags` — what actually happened (flags set during play)
- `session_notes` — key moments logged in the save block
- `npc_threads` resolved — conversations that completed
- Lute entries (📖/🖊️) — notebook entries generated during play
- Companion commitment scenes — who joined and how

She does not invent events that did not happen. She does not skip events because they were unflattering. She writes the true account.

---

### When Chapters Are "Written"

- **Prologue chapter** — written at the end of Phase 5 (departure narration complete)
- **Each campaign chapter** — written when the chapter export fires
- **Current chapter** — `.book current` outputs what she has so far, clearly marked `[IN PROGRESS — not yet edited]`
- Chapters with no Linzi present (she wasn't in the party): brief note — *"I was not there for this. What follows is reconstructed from accounts. I have noted where I am guessing."*

---

## 📌 `.qhub` — Quest Sources at Current Location

**Purpose:** Shows every quest available at the player's current location — source, how to
activate, reward, locked NPCs, and any companion tied to the quest chain.

**Trigger:** Player types `.qhub`

---

### DM PROCEDURE

```
1. Check save block: current_location
2. Load the matching location reference file:
     Oleg's Trading Post  → KM_Olegs.md
     Capital (Tuskdale)   → use KM_Kingdom.md + quest flags
     Other locations     → use known quest flags + companion files
3. Cross-reference save block: quests_active, quests_completed, story_flags
4. Filter:
     SHOW  — quests not yet started (not in quests_active or quests_completed)
     SHOW  — quests in quests_active with incomplete objectives
     HIDE  — quests in quests_completed
5. For each quest shown, check if source NPC is present:
     If NPC not yet arrived → mark [NPC LOCKED] with trigger condition
6. Check companions list for any QL companion tied to this quest chain.
7. Output the QHUB PANEL below.
```

---

### QHUB PANEL FORMAT

```
══════════════════════════════════════════════
QUEST HUB — [LOCATION NAME]
══════════════════════════════════════════════
AVAILABLE QUESTS

▸ [Quest Name]
  Source:   [NPC name or "Notice board"]
  Activate: [Exact action — "speak to X", "read board", "examine Y"]
  Reward:   [Specific reward — item, gold, service, unlock]
  Status:   [NOT STARTED / IN PROGRESS: objective text]
  QL NPC:   [Only shown if NPC is locked] ← arrives when: [condition]

▸ [Next quest...]
──────────────────────────────────────────────
WANTED BOARD

⚑ [Poster Title] — [Target name]
  Reward: [amount/item]     Contact: [who/where]

⚑ [Next poster...]
──────────────────────────────────────────────
NPC STATUS AT THIS LOCATION

✓ [Present NPC] — [one-line role]
✗ [Locked NPC]  — arrives when: [condition]
══════════════════════════════════════════════
```

---

### RULES

- **Do NOT show** quests that have been completed (in `quests_completed`).
- **Do NOT invent** quests not in the location file or the companion files.
- If current location has no location file: show only quests in `quests_active` matching
  that area, plus a note: `[No hub file for this location — showing tracked quests only]`
- QL Companion line: only show if a party-joinable companion is gated behind this quest.
  Format: `Companion unlock: [Name] joins if this quest resolves.`
- Run `.qhub` silently checks against `quests_completed` — do not ask the player to list
  their completed quests. Read the save block.

---

### EXAMPLE OUTPUT (Oleg's, early Chapter 1)

```
══════════════════════════════════════════════
QUEST HUB — OLEG'S TRADING POST
══════════════════════════════════════════════
AVAILABLE QUESTS

▸ The Lost Ring
  Source:   Svetlana Leveton
  Activate: Speak to Svetlana alone (she won't ask in front of Oleg)
  Reward:   Free lodging; 10% discount on all goods
  Status:   NOT STARTED

▸ Falgrim Sneeg
  Source:   Kesten Garess
  Activate: Speak to Kesten; ask about his purpose here
  Reward:   4 masterwork weapons (alive) / 2 (dead)
  Status:   NOT STARTED
  QL NPC:   Kesten not yet arrived ← arrives when: Happs raid repelled

▸ Fangberries for Bokken
  Source:   Bokken (hermit alchemist, 5 mi south)
  Activate: Visit Bokken or ask Oleg about the alchemist; ask if he needs anything
  Reward:   25% potion discount (1 month)
  Status:   NOT STARTED

▸ Temple of the Elk
  Source:   Jhod Kavken
  Activate: Speak to Jhod; ask about his dreams
  Reward:   Free divine services; capital Temple of the Elk unlock
  Status:   NOT STARTED
  QL NPC:   Jhod not yet arrived ← arrives when: bandit network engaged

▸ Tuskgutter
  Source:   Vekkel Benzen / Notice board
  Activate: Speak to Vekkel or read the wanted board
  Reward:   Vekkel's named composite longbow (+1)
  Status:   NOT STARTED

──────────────────────────────────────────────
WANTED BOARD

⚑ The Stag Lord — bandit warlord of the Greenbelt
  Reward: Major charter reward, land grant     Contact: Restov / Swordlords

⚑ Kressle — female bandit lieutenant, Thorn River camp
  Reward: Standard bounty (alive preferred)    Contact: Restov

⚑ Falgrim Sneeg — male, 30s, scar on left palm
  Reward: Contact Kesten Garess               Contact: Oleg's post

⚑ Tuskgutter — giant ancient boar, Narlmarches
  Reward: Vekkel's named bow                  Contact: Vekkel Benzen

⚑ Tatzlwyrm clearance — river junction, NE Greenbelt
  Reward: Restov reward on delivery of head   Contact: Restov

──────────────────────────────────────────────
NPC STATUS

✓ Oleg Leveton — proprietor, supplies, storage
✓ Svetlana Leveton — hostess, rumor, Lost Ring quest
✓ Bokken — potions and alchemicals (5 mi south)
✓ Vekkel Benzen — Tuskgutter quest
✗ Kesten Garess — ← arrives after Happs raid repelled
✗ Jhod Kavken   — ← arrives after bandit network engaged
══════════════════════════════════════════════
```

---

## 🗂️ `.quests` — KESTEN'S QUEST BOARD

> **DM:** Load KM_Rearguard.md. Output the KESTEN'S BOARD panel for the current location.
> Requires Kesten to be present (arrives after Happs raid repelled). If Kesten is not yet
> present, tell the player in one line: "Kesten hasn't arrived yet."
>
> Pull quests from `quests_active` and `story_flags`. Filter `quests_completed`.
> Pull ??? entries from `unknown_areas` save block field.
> Pull rearguard section from `rearguard_active` save block field.
> Full panel format and rules: KM_Rearguard.md § `.quests`

---

## 🔭 `.scout [area]` — SEND REARGUARD TO SCOUT

> **DM:** Load KM_Rearguard.md. Run the SCOUT PROCEDURE.
> `[area]` = area name or ??? hint from Kesten's board.
> If area is not in `unknown_areas`: tell the player it's not on the board.
> If player does not specify area: show the ??? list from `.quests` and ask which one.
> Full procedure, scout ratings, and intel report format: KM_Rearguard.md § `.scout`

---

## ⚔️ `.delegate [quest]` — SEND REARGUARD TO COMPLETE A QUEST

> **DM:** Load KM_Rearguard.md. Run the DELEGATE PROCEDURE.
> `[quest]` = quest name from Kesten's board.
> If quest is [PARTY REQUIRED]: refuse with reason. No override.
> If player does not specify quest: show [DELEGATE OK] quests and ask which one.
> Full procedure, skill table, time table, and return format: KM_Rearguard.md § `.delegate`

---

## 📊 `.rearguard` — REARGUARD STATUS PANEL

> **DM:** Load KM_Rearguard.md. Output the REARGUARD STATUS panel.
> Pull from `rearguard_active` in save block. If empty: "No one is away."
> Check for any rearguard whose `return_day ≤ current_day` — fire their report first.
> Full panel format: KM_Rearguard.md § `.rearguard`

---

*KM_Commands_P3.md — Kingmaker PF2e Text Adventure | Command Panels Part 3 v1.2*
