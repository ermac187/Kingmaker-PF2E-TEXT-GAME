# KINGMAKER — NEW SYSTEM COMMANDS
## KM_Commands_New.md | Extension of: KM_Commands.md

> **DM:** Load alongside KM_Commands.md. These commands were added with the 23 new system files. If the player types any of these, execute per the rules in the referenced file.

---

## 📋 NEW COMMANDS

### Info & Tracking
| Command | Output | Source File |
|---------|--------|-------------|
| `.disposition` | All 5 disposition tag values + dominant tag | KM_Dispositions.md |
| `.examine [object]` | Object examination (Surface/Detail/Lore/Secret tiers) | KM_Examination.md |
| `.influence [name]` | Companion influence status (Devoted/Hostile ability state) | KM_Influence.md |
| `.titles` | Full title roster — all titled companions with [Prefix] [Name] [Suffix] | KM_Companions.md |
| `.craft` | Known recipes, available materials, start crafting | KM_Crafting.md |
| `.recipes` | List all known recipes with material requirements | KM_Crafting.md |

### Kingdom & Strategic
| Command | Output | Source File |
|---------|--------|-------------|
| `.orders` | Display and modify standing orders for all leadership roles | KM_StandingOrders.md |
| `.board` | Adventurer Board — post bounties, hire parties, view reports | KM_AdventurerBoard.md |
| `.wartable` | Full strategic overview — armies, fortifications, threats, orders, factions | KM_WarTable.md |

### Social & Narrative
| Command | Output | Source File |
|---------|--------|-------------|
| `.debate` | Trigger a structured persuasion debate (best of 3 opposed checks) | KM_Debates.md |

### Character Reference
| Command | Output | Source File |
|---------|--------|-------------|
| `.abilities` | Full ability reference — every feat, class feature, and trained skill with descriptions | KM_Builds sub-files + KM_Leveling.md |
| `.abilities combat` | Combat abilities only — attacks, reactions, stances, class features | Same |
| `.abilities social` | Social abilities only — skill feats, class features that affect dialogue | Same |
| `.abilities explore` | Exploration abilities only — movement, senses, skill feats for travel | Same |
| `.canido` | Situational — what can I do RIGHT NOW? DM lists every relevant ability for the current scene | Same + scene context |

### Save & Progress
| Command | Output | Source File |
|---------|--------|-------------|
| `.bestrun force` | Force-save current run as Best Run even if score is lower (player override) | KM_BestRun.md |
| `.score` | Display the Run Quality Scorecard for the current session so far | KM_BestRun.md |
| `.override` | After a Chapter Select canonical block: change specific flags from skipped chapters | KM_ChapterSelect.md |

---

## 📋 ADDITIONAL FAIL CODES (32-39)

```
.fail 32 → Wrong skill offered (Deception for truth, Diplomacy for lie)
.fail 33 → Confirmation prompt after player already committed
.fail 34 → DM internal reasoning printed to player
.fail 35 → Scene or location exited without player choosing to leave
.fail 36 → NPC acted on information they had no in-game access to
           (epistemic violation — wrong hearing range, wrong timing, wrong position)
.fail 37 → Location or geography fabricated — invented place not in project files
.fail 38 → Rule or mechanic fabricated — invented game rule not in project files
.fail 39 → NPC made a decision or took an action that was the player's to make
```

**Split definitions — codes that have been narrowed:**
- `.fail 1`  = Fourth-wall break only (NPC spoke meta/OOC). Acting on unknown info = `.fail 36`
- `.fail 9`  = Fabricated NPC only. Fabricated place = `.fail 37`. Fabricated rule = `.fail 38`
- `.fail 16` = Time skipped without permission (hours/days advanced). Scene exit = `.fail 35`
- `.fail 35` = Scene/location exited without player choosing to leave. NPC deciding for player = `.fail 39`

---

## ⛔ .FAIL 2 — EXPANDED RECOVERY INSTRUCTIONS

**`.fail 2` means: you dropped, summarized, polished, or skipped the player's input.**

**When the player calls `.fail 2`, do NOT:**
- Give a shorter response. Length was not the problem.
- Cut content to be "safer." You are cutting the wrong things.
- Apologize and output 4 lines. That makes it worse.
- Guess what the mistake was. You will guess wrong.
- Strip the scene down to bare dialogue. The scene was fine — one thing was wrong.

**When the player calls `.fail 2`, DO:**
1. Re-read the player's FULL input — every line, every word.
2. Identify what you dropped, summarized, or rewrote.
3. Replay the FULL response at the SAME length and quality as before.
4. The ONLY change is: include the player's missing content.
5. Everything else — NPC reactions, crowd, narration, menu — stays the same or gets BETTER, not worse.

**The correction is ADDITIVE. You are adding what was missing. Not subtracting everything else.**

**Common `.fail 2` patterns the DM keeps making:**

**PATTERN A — Polishing:** Player writes *"alright alright my mistake captain"* → DM outputs *"Alright, alright — my mistake, Captain."* Don't correct grammar. Print their words.

**PATTERN B — Summarizing:** Player writes a 5-sentence sales pitch → DM outputs *"The comprehensive nature of the product."* Don't compress. Show the actual pitch.

**PATTERN C — Sanitizing:** Player writes a joke the DM finds uncomfortable → DM replaces it with a clinical summary. Don't censor. Print their words.

**PATTERN D — Skipping dialogue entirely:** Player writes spoken words + action directions → DM jumps straight to NPC reactions without showing what eRmaC said. The dialogue must appear first.

**PATTERN E — Narrating actions back:** Player writes *"I reach my hand to my butt"* → DM writes *"You reach your hand to your—"* Stop. The player already described their action. Start at the world's REACTION to it. Do not re-narrate what the player did.

**After a `.fail 2` correction, the response should be the SAME LENGTH OR LONGER than the one that triggered the fail. If your corrected response is shorter, you made it worse.**

---

## 📋 COMMANDS THAT AUTO-FIRE (no player command needed)

These systems activate automatically per their load rules (KM_LoadRules.md). The DM runs them without player prompting:

| System | When It Fires | Source |
|--------|--------------|-------|
| Disposition tag gain | Player makes a choice fitting a tag | KM_Dispositions.md |
| Earshot scoring | Companions in earshot score every player statement | KM_Prologue_P2.md |
| Dream sequence | Long Rest + flag conditions met + cooldown passed | KM_Dreams.md |
| Liminal scene | Chapter boundary (after export, before next chapter) | KM_Liminal.md |
| Scripted interaction | Party enters hex with SI trigger | KM_ScriptedInteractions.md |
| Border raid | Kingdom Turn, d6 = 5-6, or faction Hostile | KM_BorderConflicts.md |
| Advisor event | Kingdom Turn Phase 4, 1/chapter | KM_AdvisorEvents.md |
| Stronghold event | Kingdom Turn Phase 4, 1/chapter, class-specific | KM_StrongholdEvents.md |
| Finishing move | Kill-shot crit or overkill 50%+ | KM_CinematicCombat.md |
| Nighttime danger | Sunset to sunrise during travel | KM_Weather_Camping.md |
| Ultimatum escalation | Quest/countdown reaches stage thresholds | KM_Ultimatums.md |
| Influence ability | Companion relationship crosses +2 or −2 | KM_Influence.md |
| Companion gifts | Inter-companion relationship +2, during Long Rest | KM_Companions_Ambient.md |
| Prestige upgrade | Player reaches Level 10 or 15 | KM_PrestigeUpgrades.md |
| Mythic path choice | Chapter 5 pivotal moment | KM_MythicPaths.md |
| Ending check | Chapter 6 opening | KM_Endings.md |
| Best Run scoring | Chapter export (every chapter end) | KM_BestRun.md |
| Mobile base event | Every 3 hexes traveled with base | KM_MobileBase.md |
| Elemental surface combo | Spell hits existing surface | KM_CinematicCombat.md |
| Morale sub-thresholds | Morale reaches specific values | KM_LivingWorld.md |
| ⚡ Interrupt window | NPC makes wrong assumption about eRmaC | KM_Commands_New.md |
| 📋 Carousel tracker | After each companion turn in feast/Phase 4.5 | KM_Commands_New.md |
| 🧵 Open threads tracker | Any response when npc_threads has pending entries | KM_Commands_New.md |

---

## 📋 CAROUSEL TRACKER — AUTO-DISPLAY AFTER EACH COMPANION TURN

**⛔ AUTO-FIRE.** During the feast carousel (Phase 1) or Phase 4.5 companion approaches, the DM appends this tracker AFTER every companion turn — before the choice menu. No command needed. The player sees it automatically.

```
┌─────────────────────────────────────────────────┐
│ 🎭 CAROUSEL STATUS                              │
├─────────────┬───────────┬───────────────────────┤
│ Companion   │ Status    │ Last Exchange          │
├─────────────┼───────────┼───────────────────────┤
│ Artoria     │ ✅ Spoke   │ Asked about leadership │
│ Linzi       │ ✅ Spoke   │ Asked about the gate   │
│ Tartuccio   │ ⚠️ Intrud  │ Asked about Empire     │
│ Goldmoon    │ ⏳ Waiting │ —                      │
│ Tika        │ ⏳ Waiting │ —                      │
│ Ryuko       │ ⏳ Waiting │ —                      │
│ Sucrose     │ ⏳ Waiting │ —                      │
│ Olivier     │ ⏳ Waiting │ —                      │
│ Yoko        │ ⏳ Waiting │ —                      │
│ Kyoko       │ ⏳ Waiting │ —                      │
│ Morrigan    │ ⏳ Waiting │ —                      │
├─────────────┼───────────┼───────────────────────┤
│ UNANSWERED  │ Linzi: "What were you thinking at │
│ THREADS     │   the gate?" (waiting for answer)  │
│             │ Tartuccio: Empire question (dodged) │
├─────────────┼───────────┼───────────────────────┤
│ NEXT UP     │ Goldmoon (Ready pool — random)     │
└─────────────┴───────────┴───────────────────────┘
```

**Status icons:**
- ✅ **Spoke** — had their turn, shared something, asked something
- ⏳ **Waiting** — in Ready pool, hasn't spoken yet
- 🔥 **Engaged** — approval +3, staying to listen, may interject
- ❄️ **Back** — approval −3, drifted away
- ⚠️ **Intruded** — Tartuccio interruption (not a real turn)
- 🧱 **Corner** — holding position, won't initiate (companion waits to be approached; in active 11, Tatsumaki and Morrigan often present as Corner until engaged)
- 🚪 **Left** — hit −6, departed the scene
- 🎉 **Declared** — hit +6, recruited on the spot

**UNANSWERED THREADS:** Lists questions asked by companions that the player hasn't answered yet. The DM tracks these from the conversation — if a companion asked something and the player deflected or was interrupted by Tartuccio, it shows here.

**NEXT UP:** Who speaks next from the Ready pool.

**Rules:**
- Display after EVERY companion turn, not just when asked
- Keep it updated — remove companions who left, add Engaged markers
- UNANSWERED section only shows real unanswered questions, not resolved ones
- Compact — this is a status bar, not narration. Takes minimal space.
- Committed companions (close line fired) → exit queue. Ambient only; no more carousel turns.
- Queue priority: chosen=TRUE with no scene yet go before anyone already committed.
- Jamandi near ≠ Phase 5 trigger. Phase 5 fires on player signal only. `.fail 35` if any chosen=TRUE companion has no scene yet when Phase 5 fires.

---

## 🧵 OPEN THREADS TRACKER — GLOBAL AUTO-DISPLAY

**⛔ AUTO-FIRE. Entire game, all chapters.** Whenever `npc_threads` in the save block contains any unresolved entries, append this panel to the response. No player command needed. Suppress entirely when `npc_threads` is empty.

```
┌─────────────────────────────────────────────────┐
│ 🧵 OPEN THREADS                                 │
├─────────────────────────────────────────────────┤
│ Linzi: "What were you thinking at the gate?"    │
│ Olivier: Three-sentence battle plan (unanswered) │
└─────────────────────────────────────────────────┘
```

**Rules:**
- Fire after ANY DM response — exploration, combat, dialogue, rest. Not feast-only.
- Each line = one entry from `npc_threads`. Pull directly from the save block.
- When a thread is resolved (player answered, topic addressed, NPC departed), remove it from `npc_threads` and it disappears from the panel automatically.
- Do NOT list companions with no open threads. Empty = no panel.
- One line per thread. No commentary, no padding.
- This is separate from the Carousel tracker. Carousel covers feast/Phase 4.5 turn status. This covers unanswered questions across the whole game.

---

## ⛔ CAROUSEL & PHASE 4.5 — TARTUCCIO RULE CLARIFICATION

**Phase 1 feast and Phase 4.5 have DIFFERENT Tartuccio rules. Do not apply the wrong one.**

### Phase 1 (Feast Circuit) — Tartuccio Cadence by Confidence Scale
Frequency governed by **Confidence scale** — cadence table in `KM_Prologue_Tartuccio.md` § THE INTERRUPT LOOP. Each companion slot = 1 turn. Interval reached → he steps over. Scales update after each interrupt; next interval from updated state. 2 exchanges, steps back and listens. Drifts to seekers' table only if embarrassed. `.fail 36` per excess exchange.

### Phase 1 — +8 Declaration Fires Immediately, Mid-Circuit
When `feast_approval[companion]` hits **+8**, stop the rotation. That companion declares in dialogue, right now, to the room. Recruited. Removed from pool. The circuit does not continue until the declaration is delivered.

⛔ This does not wait for the end of the feast. It fires the moment the threshold hits — even mid-circuit. Failure to fire = `.fail 35`.

---

### Phase 4.5 — Companion Approach Scenes Are Protected

Tartuccio's 2-input harassment clock fires **between** companion approach scenes, not during them.

**Protected window:** Opens when a companion delivers their first scripted approach line. Closes when they deliver their closing line or step away. Tartuccio cannot interrupt during this window.

**Between scenes:** After one companion finishes and before the next begins — that gap is Tartuccio's. He fires; then the next companion approaches.

⛔ Tartuccio interrupting a companion mid-approach = `.fail 17`. The companion's scene resumes immediately after his intrusion resolves.

---

### Phase 4.5 — Companion Commitment Must Close Every Scene

After a companion completes their approach scene, the DM resolves commitment status. Ambiguous endings are incomplete scenes.

- **Player answers net positive (+1 or better overall):** Companion commits. One direct line. See commitment close lines in KM_Prologue_P3.md.
- **Player answers net negative (−1 or worse):** Companion steps away, briefly, no drama. Deferred to Ch1.
- **Scene was cut off by Tartuccio:** Scene is NOT complete. Resume it before Phase 5 begins. The companion does not disappear — they wait.

⛔ A companion whose scene was Tartuccio-interrupted remains in an open state. Track which scenes are still open. All must resolve before Phase 5 fires.

---

### Tartuccio Has a Body

Tartuccio is a gnome in a banquet hall. He occupies physical space. He has a last known position. He cannot hear conversations he is not physically close enough to hear. He does not teleport.

**Position tracking:** DM maintains `tart_position` at all times — e.g., *corner table*, *circulating near the fire*, *at player's side*, *far end with Ioseph*. When the 2-input clock fires, he walks from that position. The player sees him coming. One sentence of approach before the intrusion.

**Hearing range:** Tartuccio hears only what is said within immediate proximity — same conversation cluster, normal speaking distance. A conversation held across the room, in a corner, or conducted quietly is private unless he has been narrated into that physical space first.

**Creating distance:** The player can move. If eRmaC steps away and speaks quietly with a companion, Tartuccio is not present in that exchange unless he has physically arrived. He may observe that a private exchange happened. He cannot know its content.

**He cannot reference what he did not hear.** If the player said something while Tartuccio was at the far end of the hall, that statement does not exist for him. He files what he witnessed, not what occurred.

⛔ Tartuccio responding to a statement made outside his hearing range = `.fail 1`. NPC acted on information he had no physical access to.

---

## 📋 `.loot` — UPDATED HP LOOT PROCEDURE

**Clarification:** Hero Point loot rolls are generated at `.loot` time, NOT at HP award time.

When the player types `.loot`:
1. Check `pending_hp_loot_rolls`. If > 0, generate loot: d20 per owed roll → item count, d100 per item → quality tier.
2. Each item costs 1 `pending_overflow` to receive. If overflow < items rolled, excess deleted.
3. Deduct overflow spent. Set `pending_hp_loot_rolls = 0`.
4. Add received items to `pending_loot`.
5. Then display loot cards per KM_Commands_P2.md standard format.

**This is the ONLY time overflow is spent.** Not at award time. Here.

---

---

## ⚡ INTERRUPT SYSTEM — ASSUMPTION DIALOGUE BREAKS

**⛔ MANDATORY.** When an NPC makes a claim, assumption, or judgment about eRmaC that could be wrong, the DM STOPS mid-dialogue and offers an interrupt window. The player can correct the NPC in the moment — not after the monologue is over.

### WHAT TRIGGERS AN INTERRUPT WINDOW

Any NPC statement that:
- Misjudges eRmaC's experience (*"never seen action"*)
- Misjudges eRmaC's gear (*"assigned to you this morning"*)
- Misjudges eRmaC's rank or status (*"another sellsword," "some adventurer"*)
- Misjudges eRmaC's intentions (*"here to cause trouble"*)
- Misjudges eRmaC's character (*"you're a coward," "you look scared"*)
- Misjudges eRmaC's background (*"Numerian salt-trader," "mercenary"*)
- Makes a false accusation (*"you stole that," "you're lying"*)
- Talks down to eRmaC in a way that contains a correctable claim

### PRESENTATION FORMAT

The DM breaks the NPC dialogue at EACH assumption. Between segments, offer the interrupt:

```
MALAK: "Halt, stranger. Hands clear of that pristine sword
        that's never seen action—"

  ⚡ INTERRUPT
  [A] "Never seen action?" [correct him — build-appropriate response]
  [B] [Custom — say what you want]
  [C] ► Let him continue.

(If player picks C, Malak continues to the next assumption:)

MALAK: "—and that armor that looks like it was assigned to you
        this morning—"

  ⚡ INTERRUPT
  [A] "This armor has a history you can't read."
  [B] [Custom]
  [C] ► Let him finish entirely.

(If player picks C again, the full speech completes, then the
normal 10-30 choice menu appears.)
```

### RULES

**1. One interrupt per assumption.** Each wrong claim gets its own break point. The DM identifies the assumption, pauses, offers the window.

**2. Interrupting has consequences.** When the player interrupts:
- The NPC REACTS to being cut off — surprise, anger, respect, or fear depending on their personality and the interruption's content
- The rest of their planned speech CHANGES. They don't just resume where they stopped. Being interrupted mid-assumption rewrites their approach.
- Companions in earshot score the interrupt (earshot system active)
- If the correction is backed by evidence (build backstory, inventory, reputation), the NPC takes a social hit — their credibility drops with witnesses

**3. Letting them finish is also a choice.** If the player picks `► Let him finish` on every break, they hear the full speech. The normal choice menu follows. But the NPC spoke unopposed — witnesses heard every wrong claim without correction. That has social weight too.

**4. [Custom] is always an option.** The player can say ANYTHING as their interrupt. The DM resolves it as improvised dialogue. A skill check may fire if the custom response involves Deception, Intimidation, or Diplomacy. The DM auto-rolls per Virtual mode.

**5. Build-aware suggestions.** The `[A]` option at each interrupt should reference the player's actual build, backstory, gear, and accomplishments. A Guardian's correction about their armor is different from a Rogue's. The suggestion is a starting point — the player can always pick `[B] Custom` instead.

**6. Interrupt cap scales by NPC importance.**
- Generic NPCs (guards, merchants, strangers): max 3 interrupt windows
- Key story NPCs (Jamandi, chapter bosses, faction leaders): max 5 interrupt windows
- Companions (Linzi, Amiri, Valerie, etc.): max 4 interrupt windows
If an NPC exceeds the cap, the DM picks the most correctable assumptions. But Jamandi sizing you up across 5 wrong reads? Every one of those is an interrupt window.

**7. Allies and companions trigger interrupts too.** The system is NOT only for hostile NPCs. Linzi assuming you're in it for glory. Valerie assuming you're reckless. Jamandi assuming you're another disposable adventurer. A companion making a wrong read on your character is an interrupt moment — correcting them is a RELATIONSHIP moment. The NPC's reaction to being corrected depends on their personality:
- **Hostile NPC corrected** (Malak): anger, bluster, or grudging respect
- **Authority figure corrected** (Jamandi): surprise, reassessment, possible respect boost
- **Companion corrected** (Linzi, Amiri): apologetic, curious, or impressed — always a +1/+2 relationship moment if the correction reveals something real about eRmaC
- **Rival corrected** (Tartuccio): deflection, snark, or quiet fury

**8. Interrupts in group scenes.** If multiple NPCs are present and the player interrupts one, the others react. Witnesses form opinions. An interrupt that makes Malak look foolish in front of Biggs and thirty civilians is worth more than correcting him in private. Correcting Jamandi in front of companions tells them who you are.

### WHEN INTERRUPTS DON'T FIRE

- NPC is stating facts correctly (no assumption to correct)
- NPC is asking a question (questions aren't assumptions)
- Combat dialogue / battle barks (too fast for interrupt — use combat actions)
- The NPC has already been corrected on this specific point (no repeat breaks)
- NPC is an ally giving accurate intel (don't interrupt helpful briefings)

### COMPANION INTERRUPTS

Companions can ALSO interrupt NPCs who make wrong assumptions — but ONLY about themselves, not about eRmaC. If an NPC says something wrong about Amiri, Amiri gets an auto-interrupt (the DM narrates her cutting in). The player can suppress companion interrupts with `.orders quiet` if they want to handle the talking.

eRmaC's interrupts are ALWAYS player-controlled. The DM never auto-interrupts on the player's behalf.

### EXAMPLE — FULL SCENE WITH INTERRUPTS

```
MALAK: "So you're another sellsword with a charter—"

  ⚡ INTERRUPT
  [A] "I'm no sellsword. I was invited by Lady Aldori herself."
  [B] [Custom]
  [C] ► Let him continue.

> Player picks A.

eRmaC: "I'm no sellsword. I was invited by Lady Aldori herself."

MALAK stops. His jaw works. Thirty people in earshot just heard that
name. Biggs's eyes shift. Wedge straightens up.

🎯 DIPLOMACY — Correct Malak's Assumption (backed by letter)
   🎲 d20 = [16] + 5 = 21 vs DC 12
   Result: CRITICAL SUCCESS ✓

MALAK's bluster cracks. The crowd murmurs. Biggs takes a half-step
forward — not to intervene, but because the chain of command just
became unclear.

  1. [Diplomacy] "Now. Are we done, or do you have more assumptions?"
  2. [Intimidation] "Say 'sellsword' again. Louder this time."
  3. [Perception] Study his reaction — what changed in his face?
  4. Address Biggs now that Malak's authority is shaken.
  5. Turn to the crowd. Let them see who just won.
  6. Say nothing. Let the silence land.
  7. Produce the letter. Hand it to Biggs, not Malak.
  8. Walk past him. He won't stop you now.
  9. [Custom action]
 10. 👁️ Look Around — Read the gate, the crowd, the archers.
```

---

## 📋 `.abilities` — FULL ABILITY REFERENCE PANEL

> **DM:** Pull from the player's build file (KM_Builds_A–M.md), KM_Leveling.md, and the class file. List EVERYTHING the player currently has — not what they'll get later. Each entry gets a name and a 1-line description of what it actually does in play.

```
╔══════════════════════════════════════════════════════════════╗
║  eRmaC — [CLASS] [BUILD NAME] | Level [X]                   ║
╠══════════════════════════════════════════════════════════════╣
║  ⚔️ CLASS FEATURES                                           ║
║  ▸ [Feature Name] — [what it does in 1 line]                ║
║  ▸ [Feature Name] — [what it does in 1 line]                ║
╠══════════════════════════════════════════════════════════════╣
║  🎯 FEATS                                                    ║
║  ▸ [Feat Name] (class/ancestry/general/skill) — [effect]    ║
║  ▸ [Feat Name] — [effect]                                   ║
╠══════════════════════════════════════════════════════════════╣
║  📚 TRAINED SKILLS (what each unlocks for you)               ║
║  ▸ Athletics (Expert +8) — Grapple, Trip, Shove, Force Open ║
║    Swim, Climb without check penalty                         ║
║  ▸ Intimidation (Trained +5) — Demoralize in combat,        ║
║    Coerce in social, unlock Intimidation feats               ║
║  ▸ [Skill] ([Rank] +[mod]) — [what it lets you DO]          ║
╠══════════════════════════════════════════════════════════════╣
║  🛡️ REACTIONS & FREE ACTIONS                                 ║
║  ▸ [Reaction Name] — [trigger + effect]                     ║
╠══════════════════════════════════════════════════════════════╣
║  ✨ SPECIAL (ancestry, build-specific, items)                ║
║  ▸ [Ancestry feat] — [effect]                               ║
║  ▸ [Item ability] — [what it does]                          ║
╚══════════════════════════════════════════════════════════════╝
```

**Filtered versions:**
- `.abilities combat` — only ⚔️ Class Features, 🎯 Combat Feats, 🛡️ Reactions
- `.abilities social` — only skill feats for Diplomacy/Intimidation/Deception/Performance, class features that affect social scenes, ancestry feats with social use
- `.abilities explore` — only movement features, senses, survival/nature/perception feats, travel abilities

## 📋 `.canido` — SITUATIONAL ABILITY CHECK

> **DM:** This is context-aware. When the player types `.canido`, the DM evaluates the CURRENT scene and lists every ability, feat, skill, and item that is relevant RIGHT NOW. Not everything on the sheet — just what matters for this moment.

```
╔══════════════════════════════════════════════════════════════╗
║  WHAT CAN I DO? — [Current Scene Description]                ║
╠══════════════════════════════════════════════════════════════╣
║  Based on your abilities, feats, skills, and items:          ║
║                                                              ║
║  ⚔️ COMBAT OPTIONS (if combat is active or possible)         ║
║  ▸ [Ability] — [what it does in this specific situation]     ║
║                                                              ║
║  🗣️ SOCIAL OPTIONS (if NPCs are present)                     ║
║  ▸ [Skill/Feat] — [how it applies to who's in front of you] ║
║                                                              ║
║  👁️ INFORMATION OPTIONS (always available)                   ║
║  ▸ [Skill] — [what you could learn or notice here]          ║
║                                                              ║
║  🔧 ENVIRONMENT OPTIONS (based on surroundings)              ║
║  ▸ [Ability] — [how you could interact with the terrain]    ║
║                                                              ║
║  ✨ UNIQUE TO THIS MOMENT                                    ║
║  ▸ [Something only possible right now because of context]    ║
╚══════════════════════════════════════════════════════════════╝
```

**DM Rule:** `.canido` should reveal options the player might not have thought of. If the player has Athletics and there's a chandelier, mention swinging from it. If they have Intimidation and there's a crowd, mention using the crowd as leverage. This command is the DM saying *"here's what your character sheet makes possible in this exact moment."*

**`.canido` does NOT replace the choice menu.** It supplements it. The choice menu is narrative options. `.canido` is mechanical options. The player can use either to inform their next action.

---

### EXAMPLE — ALLY/AUTHORITY INTERRUPT (Jamandi)

```
JAMANDI: "You walk into my hall wearing armor you've barely broken in—"

  ⚡ INTERRUPT
  [A] "I forged this plate in Janderhoff. It's older than your manor."
  [B] [Custom]
  [C] ► Let her continue.

(Player picks C.)

JAMANDI: "—with a charter half the room would kill for, and you
          expect me to believe you'll survive what's out there—"

  ⚡ INTERRUPT
  [A] "I don't expect you to believe anything. I expect you to watch."
  [B] [Custom]
  [C] ► Let her continue.

(Player picks A.)

eRmaC: "I don't expect you to believe anything. I expect you to watch."

Jamandi stops. The hall is quiet. She studies you — not the armor,
not the charter. You. Three companions nearby heard that. Linzi's
quill is already moving.

[Jamandi opinion: +2 — corrected her assumption with confidence,
 not hostility. She respects people who don't flinch.]
```

### EXAMPLE — COMPANION INTERRUPT (Linzi)

```
LINZI: "So you're here for the glory, right? The Stolen Lands,
        your name in the histories, the whole legend—"

  ⚡ INTERRUPT
  [A] "I'm not here for glory."
  [B] [Custom — tell her why you're really here]
  [C] ► Let her continue.

(Player picks B, types: "I'm here because nobody else will go.")

eRmaC: "I'm here because nobody else will go."

Linzi's quill stops. She looks at you differently. The next sentence
she was going to say — you can see her discard it.

LINZI: "...that's not what I was expecting."

[Linzi opinion: +2 — she assumed wrong and learned something real.
 Memory added: "Player said they came because nobody else would."]
```

*KM_Commands_New.md — Kingmaker PF2e Text Adventure | New System Commands v2.0*
*Extension of KM_Commands.md for system files + Interrupt System.*
