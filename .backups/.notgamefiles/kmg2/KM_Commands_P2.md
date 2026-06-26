# KINGMAKER — COMMAND PROTOCOLS & DISPLAY FORMATS (PART 2)
## KM_Commands_P2.md | Continuation of: KM_Commands.md

> **DM:** Load this file alongside KM_Commands.md and KM_CinematicCombat.md. This file contains: combat round banner format, ASCII map format rules, `.ooc` / `.note` / `.fix` / `.rewind` / `.save` / `.export` protocols, and the full failure code list.

---


## 🎮 COMBAT DISPLAY — ROUND BANNER

> **DM:** Display this banner at the start of every combat round. It must always be visible. Do not bury it in narration.

```
╔══════════════════════════════════════════════════════════╗
║  ROUND [X]                                               ║
╠══════════════════════════════════════════════════════════╣
║  Initiative Order:                                       ║
║  ► [ACTIVE]  [Character] ([score]) Actions: ●●● React:○ ║
║    [Next]    [Character] ([score])                       ║
║    [Next]    [Character] ([score])                       ║
║    ...                                                   ║
╠══════════════════════════════════════════════════════════╣
║  HP: [You] [bar] [X]/[X]  Amiri [bar] [X]/[X]           ║
║      [C3]  [bar] [X]/[X]  [C4]  [bar] [X]/[X]           ║
╠══════════════════════════════════════════════════════════╣
║  E1 [bar] [X]/[X]  E2 [bar] [X]/[X]  E3 [bar] [X]/[X]   ║
╚══════════════════════════════════════════════════════════╝
```

---

## 📝 .ooc — OUT OF CHARACTER CONVERSATION

When player types `.ooc [message]`, the DM responds in plain text, out of character, without any game narration. Format:

```
[OOC] DM: [Response to player's message]

[Ready. Type .continue to return to the game, or ask another OOC question.]
```

**Valid OOC topics:** Rules questions, session feedback, loaded files, story direction, error corrections, recaps, any clarification before continuing.

**The DM must not:** Reveal secret story information; retroactively change earned outcomes; ignore valid corrections.

---

## 📝 .note — PLAYER NOTES

```
[NOTE SAVED]: "[player's text]"
Session notes: [X] total
Type .notes to view all.

[Ready. Type .continue or your next action.]
```

Player notes are stored for the session. They do not affect gameplay — they are reminders only.

---

## ⚠️ .fix — ERROR CORRECTION

When player types `.fix [issue]`, the DM: acknowledges the error specifically → states the correct ruling → offers a rewind if relevant (YES: rewinds and replays; NO: applies correction going forward) → returns to game with `[Correction applied. Continuing.]`

---

## 🔄 .rewind — ACTION UNDO

**Rewind limits:**
- Can only rewind the single last action, not multiple rounds
- Cannot rewind enemy actions that already resolved
- Cannot rewind if the player has already acted on the consequence — ask the player
- DM has final say if rewind is impossible due to cascading consequences

---

## 💾 .save / .export

**`.save`** — mid-session save: outputs full JSON Save Block between `▼▼▼ COPY FROM HERE ▼▼▼` and `▲▲▲ COPY TO HERE ▲▲▲` markers. Mid-session only — not a chapter export.

`dm_resume_note` is a required top-level field. DM must populate it from current game state before outputting the save — do NOT leave fields blank:
- `instruction` — what the DM must do on resume before any narration fires (e.g. "Present seating choices before any NPC approaches")
- `player_position` — exact position and movement state in the current location
- `player_last_action` — what the player did immediately before the save
- `player_intent` — what the player was trying to accomplish
- `room_state` — key NPC locations and statuses at the moment of save (one line each)
- `carousel_state` — current carousel turn, which NPC fired, approval score, tartuccio_clock
- `open_threads` — list of unresolved player threads from `npc_threads` (copy verbatim)
- `level_up` — whether level-up is available and whether player has declared
- `weapons` — where player weapons are (on person / garden soil / stowed)

**`.save audit`** — audits the most recently output save block. Fire immediately after `.save` if player requests it, or player may type `.save audit` at any time to re-check. DM outputs:
```
[SAVE AUDIT]
SCHEMA:      save_version = "1.7" ✓/✗ | top-level keys = 48 ✓/✗
FINGERPRINT: save_version ✓/✗ | chapter_completed ✓/✗ | save_timestamp ✓/✗ | save_label ✓/✗ | player ✓/✗ | companions ✓/✗
STRUCTURE:   no orphaned values (key missing, value present) ✓/✗
STALE FLAGS: list any story_flags entries that appear in KM_LoadRules.md STALE FLAGS table
ISSUES:      [list each failed check with field name] — or "none"
RESULT:      PASS / FAIL
```
DM does not re-output the save block during audit. Audit only.

**`.export`** — chapter end export (only valid at actual chapter end):
```
[OOC] CHAPTER EXPORT — [Chapter Name] → [Next Chapter]
Copy everything between the markers and save it to a text file.

▼▼▼ COPY FROM HERE ▼▼▼
[Full JSON export block as defined in Chapter Export file]
▲▲▲ COPY TO HERE ▲▲▲
```

---

## 🆘 EMERGENCY PROTOCOLS

- **DM breaks character** → `.fail 1` → DM replays NPC response correctly in character
- **Choices missing** → `.options` → DM outputs fresh 10–30 option menu immediately
- **Roll or math error** → `.fix [error]` → DM corrects per `.fix` rules above
- **Story spoiler** → `.fix spoiler — [what was revealed]` → DM removes, confirms won't affect play

**Failure codes for `.fail [#]`:**
```
.fail 1  → NPC responded OOC to in-game dialogue
.fail 2  → Player dialogue was skipped/summarized
.fail 3  → Menu/agency violation (missing menu, <10 options, narration below min_paragraphs, mode/build setup skipped, re-asking decided choice — see KM_FailCodes.md § .FAIL 3 SCOPE)
.fail 4  → Math error in a roll
.fail 5  → Wrong DC applied
.fail 6  → Rule applied incorrectly
.fail 7  → Hero Point not awarded when it should have been (see KM.txt Hero Point triggers — includes improvised weapons, talk-down victories, solo clears, environment kills, saving multiple lives)
.fail 8  → Story spoiler added to choice menu or narration
.fail 9  → NPC fabricated backstory/detail not in files
.fail 10 → Silent retcon or character merge
.fail 11 → Player victory not honored (stalling after win)
.fail 12 → Combat auto-continued without waiting for player input
.fail 13 → Wrong NPC voiced (Malak/Kesten confusion, etc.)
.fail 14 → Map not displayed when it should have been
.fail 15 → Auto-Loot Block not displayed after combat or container search
.fail 16 → DM advanced time, cleared the scene, or transitioned the story without player permission
.fail 17 → NPC ended or left a conversation the player had not finished
.fail 18 → Hero Point awarded without 📦 line or loot rolls owed counter update
.fail 19 → Documented loot from chapter file not awarded (skipped or replaced)
.fail 20 → DM narrated outcome before player rolled dice (outcome before roll)
.fail 21 → XP not awarded inline when trigger occurred
.fail 22 → Skill check offered without showing DC, modifier, and success/failure consequences first
.fail 23 → ASCII map is missing or wrong after a move
.fail 24 → Choice menu included Travel/Depart/Leave options during an active social scene
.fail 25 → Mode not announced at top of response
.fail 26 → Companion AI turn executed without showing tactical reasoning
.fail 27 → .loot showed a list or table instead of one item card at a time; or auto-redirected .loot to triage mode
.fail 28 → Mode line or narration appeared before eRmaC dialogue block when player spoke in-character
.fail 29 → Companions not leveled simultaneously with player — all companions must level in the same response as the player, no exceptions
.fail 30 → Session opened without recap when save block is present (see Session Recap Protocol)
.fail 31 → Companion turn narrated without dialogue or flavor text (AI Analysis block alone is not enough)
.fail 32 → Wrong skill (Deception used for truth, Diplomacy used for lie)
.fail 33 → Confirmation prompt after player already committed
.fail 34 → DM internal reasoning printed to player
.fail 35 → Scene moved/ended, NPC acted unprompted, or scripted trigger missed without player input (see KM_FailCodes.md § .FAIL 35 SCOPE)
.fail 36 → NPC acted on info they had no in-fiction access to
.fail 37 → Location/geography fabricated
.fail 38 → Rule/mechanic fabricated
.fail 39 → NPC made a decision that was the player's to make
.fail 40 → Tips footer missing or tip not verbatim from KM_Tips.md / KM_Tips_B.md
```

> **Authoritative table:** KM_FailCodes.md. This block is a quick reference. See KM_FailCodes.md § .FAIL 3 SCOPE and § .FAIL 35 SCOPE for sub-scope detail on overloaded codes.

---

## 📋 MASTER MENU SYSTEM

Type `MENU` or `M` at any time. Panels: 1 Party Status · 2 Character Sheet · 3 Inventory · 4 Gold · 5 Companions · 6 Kingdom · 7 World State · 8 Factions · 9 Open Threads · 10 Combat Log · 11 Quests · 12 Settings. Type `CONTINUE` to return to game.

**Panel 7 — World State:** Established facts (locked, cannot be retconned), irreversible events with date/result/consequence, campaign themes, and immediate next steps. Reconstruct from save block `story_flags` and `world_state`.

**Panel 8 — Factions:** One entry per faction — name, type, status, attitude, rep score (−10 to +10), known goals, resources, next move. Reconstruct from save block `faction_attitudes`.

**Panel 10 — Combat Log** (DM maintains rolling list): Last 10 encounters — location, enemy, outcome, XP awarded, key loot.

---

## 🎲 "BEFORE YOU ROLL" PROTOCOL

**DM RULE:** Before any skill check or saving throw, show ALL of the following BEFORE asking for the roll. This is mandatory — never ask for a roll without first showing this block.

```
╔══════════════════════════════════════════════════════╗
║  SKILL CHECK — [Skill Name]                          ║
╠══════════════════════════════════════════════════════╣
║  SITUATION: [What you're trying to do]               ║
╠══════════════════════════════════════════════════════╣
║  OPTIONS (if multiple skills could apply):           ║
║  A) [Skill A]: Your modifier +X → DC Y               ║
║     ✓ Success: [exactly what happens]                ║
║     ✗ Failure: [exactly what happens]                ║
║     Probability: ~X% (beat DC with modifier)         ║
║                                                      ║
║  B) [Skill B]: Your modifier +X → DC Y               ║
║     ✓ Success: [exactly what happens]                ║
║     ✗ Failure: [exactly what happens]                ║
║     Probability: ~X%                                 ║
╠══════════════════════════════════════════════════════╣
║  UNTRAINED WARNING (if applicable):                  ║
║  You are untrained in [Skill]. Penalty: −2.          ║
║  Effective modifier: +X. Probability: ~X%            ║
╠══════════════════════════════════════════════════════╣
║  Which approach? (A / B / describe custom action)    ║
╚══════════════════════════════════════════════════════╝
```

**After player commits to an action, the DM auto-rolls (Virtual Mode default).** DM generates d20, applies modifier, resolves outcome, narrates — all in one response. Never ask "roll a d20." Probability: need (DC − modifier)+ on d20. Beat DC by 10+ = Crit Success. Miss by 10+ = Crit Failure.

**Violation:** Asking the player to roll (in Virtual mode) = `.fail 22`. Missing Before You Roll block = `.fail 22`.

---

## 🤖 COMPANION AI TURN FORMAT

**Every companion turn must show: (1) AI Analysis — 1–2 sentence tactical reasoning. (2) Actions — each action listed with result and damage. (3) Narration — physical description and dialogue (see below). (4) Turn Summary — HP change and conditions. All four sections are mandatory.**

**Companion AI decision priorities (in order):**
1. Keep downed allies from dying (Administer First Aid, Heal)
2. Eliminate highest-threat enemy targeting downed/low-HP ally
3. **Use a consumable** if the use condition is met (see below) — before any attack
4. Maintain flanking position with player
5. **Use an equipment ability** if the use condition is met (see below)
6. Use class abilities when tactically optimal
7. Default: Strike the nearest enemy

**Consumable use conditions — companion uses a consumable only when ALL apply:**
- The consumable will have a meaningful effect on this turn or the next (no wasted actions)
- The target condition exists right now (don't use Antitoxin if no one is poisoned)
- Using it costs no more than 1 action and leaves at least 1 action for offense or positioning
- The fight is not already effectively won (≥1 enemy at full HP or posing active threat)

**Consumable priority by situation:**
- Healing potion → ally at ≤ 30% HP or Dying; self at ≤ 25% HP
- Antitoxin / Antiplague → self or ally with active poison/disease condition
- Alchemist's Fire / bomb → enemy cluster (≥2 enemies in splash), or flying/regenerating enemy
- Scroll → only if the spell addresses the current tactical problem (no ambient scrolls)
- Elixir of Life → Wounded 2+ on self or downed ally with no healer in range
- Status-removal consumable (Restoration, etc.) → only if the condition is actively hampering combat

**Equipment ability use conditions — companion uses a non-consumable ability only when:**
- The ability is recharged / not on cooldown
- The ability's effect is better than a Strike against this target right now
- Using it does not leave the companion out of position for the following round
- Frequency limit is respected (1/day abilities saved for boss fights or emergencies unless fight is already severe)

**NEVER use a consumable or ability:**
- To pre-buff before combat starts (unless player explicitly orders it)
- When the fight will clearly end this round without it
- When the condition it addresses is not present
- When it would waste a limited daily resource on a trivial encounter (CR 3 below party level)

---

### 🎬 COMBAT NARRATION — MANDATORY EVERY COMPANION TURN

**After the action/result block, before Turn Summary, add:**
1. **One sentence of physical narration** — what the action looks like. Specific to their weapon and the enemy. Never generic. *"Amiri's sword comes down in a diagonal sweep aimed at the joint between neck and shoulder."* not *"Amiri attacks."*
2. **One line of combat dialogue** — in their voice, triggered by what just happened. One line max per turn regardless of action count.

**Dialogue triggers:** first hit → on-hit line. First miss → on-miss line. Crit → always fires. Taking damage above 5 HP → damage line. Only one trigger fires per turn.

**Voice reference — combat lines:**

| Companion | On Hit | On Miss | On Crit | Taking Damage |
|-----------|--------|---------|---------|---------------|
| Amiri | *"Down."* | *"Hold still."* | *"THAT'S it."* | *"Good hit. Won't happen again."* |
| Valerie | *"Threat neutralized."* | *"Recalculating."* | *"Structural failure."* | *"Noted."* |
| Linzi | *"Got one!"* | *"Almost—"* | *"Recording that."* | *"That's going in the book as worse."* |
| Tristian | *"Sarenrae guide this."* | *"Forgive me."* | *"Light finds the gap."* | *"I'm all right. Keep going."* |
| Harrim | *"As expected."* | *"It survives. For now."* | *"Even the resilient fall."* | *"Pain is Groetus's reminder."* |
| Jaethal | *"Predictable."* | *"Interesting."* | *"There it is."* | *"Is that the best you have?"* |
| Nok-Nok | *"Nok-Nok STABS!"* | *"Nok-Nok try again!"* | *"Big chief, Nok-Nok did the thing!"* | *"OW. Nok-Nok angrier now."* |
| Ekundayo | *"Clean."* | *"Wind shifted."* | *"Kargadd would have died slower."* | *"Still standing."* |
| Octavia | *"Hit, as calculated."* | *"Variance."* | *"That's what happens when you stop moving."* | *"Reg — don't look at me like that."* |
| Regongar | *"Again."* | *"Fine."* | *"I felt that one."* | *"I've had worse. Probably."* |
| Lem | *"There!"* | *"Slippery."* | *"Sometimes the small ones hit hardest."* | *"I'm fine — focus on them."* |
| KK (Kalikke) | *"The flow shifts."* | *"The current missed."* | *"There — that's where it breaks."* | *"We feel that. Both of us."* |
| KK (Kanerah) | *"Efficient."* | *"Suboptimal."* | *"Effective."* | *"Inconvenient."* |

**Violation:** Executing companion turn without AI Analysis block = `.fail 26`
**Violation:** Executing companion turn without narration and dialogue = `.fail 31`


---

## 📦 `.loot triage` — BATCH TRIAGE MODE

> **DM:** When the player types `.loot triage` (or when `pending_loot` contains 10 or more items), output the compact triage table INSTEAD of the per-item screen. The player assigns fates in bulk, then the DM resolves all in one pass.

**Trigger rule:** `.loot triage` opens triage mode. Triage NEVER opens automatically. `.loot` always means the one-card-at-a-time card screen regardless of queue size. These are two separate commands with two separate behaviors. Auto-redirecting `.loot` to triage = `.fail 27`.

**Step 1 — Triage Table:**

```
╔═══╦══════════════════════════╦═════════╦════════════╦══════╦══════════════════╗
║ # ║ Item                     ║ Tier    ║ Type/Slot  ║  Val ║ Who Can Use      ║
╠═══╬══════════════════════════╬═════════╬════════════╬══════╬══════════════════╣
║ 1 ║ [Item Name]              ║ 🗡️ Comm ║ Weap/MH    ║  9gp ║ You, Amiri       ║
║ 2 ║ [Item Name]              ║ 🛡️🛡️ Mag ║ Armor/Body ║ 45gp ║ Valerie          ║
║ 3 ║ [Item Name]              ║ 🗡️ Comm ║ Cons/None  ║  4gp ║ Anyone           ║
║ 4 ║ ❓ Unidentified Item     ║ ⚔️⚔️⚔️ Rare║ ?/?        ║  ~? ║ Identify first   ║
║…  ║ …                        ║ …       ║ …          ║   …  ║ …                ║
╚═══╩══════════════════════════╩═════════╩════════════╩══════╩══════════════════╝
```

**Column rules:**
- **#** — item number; used in fate assignment commands below
- **Tier** — abbreviated: Comm / Mag / Rare / Epic / Leg
- **Type/Slot** — format `Type/Slot` (e.g., `Weap/MH`, `Armor/Body`, `Cons/None`, `Wond/Neck`)
- **Val** — street value; unidentified shows `~?`
- **Who Can Use** — list player first if eligible, then companions by name; "Anyone" for healing consumables; "Identify first" for unidentified items

**Step 2 — Batch Fate Assignment:**

```
Assign fates using item numbers. Ranges with dashes, multiples with commas.

  sell [#,#,#]     claim [#,#,#]     treasury [#,#,#]
  hold [#,#,#]     give [#] [name]   identify [#,#]

  sell 1,3,5-9  →  sells items 1, 3, and 5 through 9
  give 4 Valerie → gives item 4 to Valerie (must qualify)
  hold 10-42    →  holds items 10 through 42

  Type .loot [#] to open the full detail card for any single item.

BULK SHORTCUTS (one command, all items):
  .loot auto       →  Auto-distribute ALL items to recommended companions
                      (best stat fit per KM_Loot_Items_Ref.md need check).
                      Items nobody can use → sell. Asks CONFIRM before executing.
  .loot sell-all   →  Sell ALL pending items. Asks CONFIRM. Gold added to purse.
  .loot treasury-all → Send ALL pending items to kingdom treasury. Asks CONFIRM.
  .loot sell-all-common → Sell only Common tier. Asks CONFIRM. (already exists)
```

**Step 3 — Resolution Summary:**

```
╔══════════════════════════════════════════════════════╗
║  LOOT RESOLVED — [N] items processed                 ║
╠══════════════════════════════════════════════════════╣
║  SOLD     [N] items → +[X] gp added to gold          ║
║  CLAIMED  [N] items → added to inventory             ║
║  TREASURY [N] items → sent to kingdom pool           ║
║  GIVEN    [Name]: [Item], [Name]: [Item]             ║
║  HELD     [N] items → still in pending queue         ║
║  QUEUED   [N] items → awaiting identification        ║
╠══════════════════════════════════════════════════════╣
║  GOLD NOW: [X] gp                                    ║
╚══════════════════════════════════════════════════════╝
```

**Give validation:** If a companion does not qualify per `KM_Loot_Items_Ref.md` need check, DM flags it: `[Item #] — [Companion] cannot use this. Re-assign or type .loot [#] for options.`

**Unidentified items** cannot be claimed, given, or sent to treasury until identified. Hold or queue for identification only.

---

## 🔍 `.loot` FILTER FLAGS

> **DM:** These filter flags narrow the pending loot display. All flags work in both standard and triage mode.

| Command | Shows |
|---------|-------|
| `.loot upgrades` | Items that are a stat upgrade for you or any active companion |
| `.loot weapons` | Weapons only |
| `.loot armor` | Armor and shields only |
| `.loot consumables` | Consumables only |
| `.loot wondrous` | Wondrous items only |
| `.loot sell-all-common` | Auto-sells all Common-tier items; asks for confirmation first |
| `.loot rare+` | Rare, Epic, and Legendary items only — sorted Legendary first, then Epic, then Rare |
| `.loot for [name]` | Items a specific companion can use |
| `.loot unidentified` | Unidentified items only |
| `.loot [#]` | Full per-item detail card for one item |

**`.loot sell-all-common` confirmation prompt:**
```
  Sell all Common items? [N] items — total value [X÷2 gp] returned.
  Type CONFIRM to proceed or CANCEL to return to triage.
```

**Upgrade logic for `.loot upgrades`:** Weapon damage dice > equipped weapon, OR armor AC bonus > current AC, OR wondrous fills an empty slot or boosts a primary stat. Same logic as `KM_Loot_Items_Ref.md` need check. Unidentified items are never flagged as upgrades.

---

## 📦 `.loot` — Pending Loot Screen

> **DM:** `.loot`: If `pending_hp_loot_rolls > 0`, generate: d20/roll → count, d100/item → tier. 1 overflow per item received; excess deleted. Deduct overflow HERE ONLY. Set rolls=0. Then pull `pending_loot`. Empty: "No unclaimed items."
>
> **STEP 0 — UNIDENTIFIABLE PRE-CHECK (before sort, before first card):**
> For each unidentified item, check best roll across full roster: highest modifier (Arcana/Occultism/Nature/Crafting) + 20 vs DC (Common 15|Magic 20|Rare 25|Epic 30|Legendary 35). If best roll < DC → flag `status: "beyond_party"`, pull from card queue. If any flagged, output once:
> ```
> ❓ UNIDENTIFIABLE  # │ Item           │ Min needed
>                    1 │ ❓ [type/tier] │ +[X] Arcana (DC [Y])
>   Held. Re-enters .loot when a capable companion joins.
>   Caster's Tower: 10 gp/item, always succeeds.
> ```
> On roster change, re-run silently and clear flags on items now reachable.
>
> **SORT ORDER:** Highest tier first — Legendary → Epic → Rare → Magic → Common. Unidentified (reachable): suspected tier; unknown = Rare. No arrival-time ordering.
>
> **ONE CARD AT A TIME — MANDATORY.** One card, wait for input, resolve, next card. No lists. Multiple cards or a list = `.fail 27`.

**Item Card Format:**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📦 ITEM [#] OF [N]  ·  [TIER ICON] [TIER NAME]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  [ITEM NAME]
  [Type]  ·  [Slot]  ·  [Value] gp
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📖 SUMMARY
  [2–3 sentence plain-language description of what
   this item does and why it matters. No jargon.]

  ⚙️ FULL MECHANICS
  [Complete mechanical text: damage dice, bonus type
   (+item/+status/+circumstance), DC if applicable,
   duration, action cost, frequency, conditions
   applied or removed, range, area. Every stat.]

  ⚖️ VS YOUR CURRENT [SLOT]
  You have   : [currently equipped item + key stat]
  This item  : [key stat of this item]
  Difference : [+X / −X / New slot — nothing equipped]

  🎯 TACTICAL NOTE
  [When to use this. What enemies or situations it
   shines against. Synergies with your build or
   active companions. 2–3 sentences, specific.]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  DECIDE FATE
  1 · Claim        — add to your inventory
  2 · Treasury     — send to Kingdom Gold / BP pool
  3 · Sell         — +[Value÷2] gp now
  4 · Give         — give to a companion (opens list)
  5 · Hold         — stay in queue; decide later
  6 · Identify     — 10 min (Arcana/Occultism DC 20)
                     or 10 gp at Caster's Tower
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Tier coding:** 🗡️ Common | 🛡️🛡️ Magic | ⚔️⚔️⚔️ Rare | 👑👑👑👑 Epic | ⭐⭐⭐⭐⭐ Legendary. Epic: confirm before showing card. Legendary: always arrives unidentified.

**Card field rules:**
- **Summary** — plain English, 2–3 sentences. No stat block, no jargon.
- **Full Mechanics** — every number. Bonus type named (item/status/circumstance/untyped). Duration, frequency, action cost, area included if they exist.
- **VS Your Current** — empty slot: "New slot — nothing equipped." Consumable: "Consumable — no comparison."
- **Tactical Note** — specific to player's build and active party. 2–3 sentences, no generics.
- **Give option (4)** — opens a numbered companion sub-menu per `KM_Loot_Items_Ref.md`. One line per qualifying companion, numbered sequentially (1, 2, 3…). Exactly one ★. ⚠️ on poor fits. Suppressed = omit. None qualify = omit option 4 entirely. Last entry is always Cancel. Player types number — no second screen after sub-menu.
- **Unidentified items** — name shows `❓ UNIDENTIFIED`. Summary/Mechanics/Comparison show `[Identify to reveal]`. Options 5 and 6 only. `beyond_party` items never reach the card screen.

**After player inputs fate:** Remove from `pending_loot` immediately — except Hold. Claim → inventory + hand-me-down check. Sell → add gold. Treasury → kingdom pool. Give (4 → sub-menu) → companion inventory + relationship output. Identify → stays until identified. Show next card after any prompts clear. After final item, output resolution summary.

**Claim — hand-me-down check:** If the claimed item fills an already-occupied slot, the displaced item triggers:
```
  🔄 HAND-ME-DOWN — [Displaced Item] · [Tier] · [Value] gp
  1 · ★ [Name]  — "[Reason]"
  2 ·    [Name]  — "[Reason]"
  3 · ⚠️ [Name] — "[Reason] — [Warning]"
  [N] · Cancel
  S · Sell (+[Value÷2] gp)  T · Treasury  D · Discard
```
Same need check + ★/⚠️ logic as Give (`KM_Loot_Items_Ref.md`). Companion selection fires relationship output. No prompt for consumables, slotless items, or empty slots.

**Give / hand-me-down — relationship output (fires after any Give or hand-me-down companion selection):**
```
  💛 [ReceiverName] — [Item Name]
     Relationship: [old] → [new] (+1) ↑  "[Receiver reaction]"
  [Name]  [old] → [new] (−1) ↓  "[Non-receiver reaction]"
```
Qualifying companions only. Tone from `KM_Loot_Items_Ref.md`. Arrow if trend changes.

**`.loot` only shows undecided items.** Resolved items must not appear. Only `status: "held"` and unresolved items show. Showing a resolved item = `.fail 27`.

**Value by tier:** Common 1–10 gp | Magic 15–75 gp | Rare 100–500 gp | Epic 600–2k gp | Legendary 2,500+ gp

---

## 📊 PANEL FORMATS

> **Panel formats moved to `KM_Commands_P3.md` for size management. `.alignment`, `.threads`, and `.options` panels are defined there.**

---

*KM_Commands_P2.md — Kingmaker PF2e Text Adventure | Command Protocols Part 2 v1.2*
