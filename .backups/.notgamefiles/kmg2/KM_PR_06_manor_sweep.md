# KM_PR_06_manor_sweep.md — Prologue Beat 06: MANOR SWEEP
## Atomic scene file | ~10 KB (five recruitments) | State: PR_06_MANOR_SWEEP
## FILE_KEY: KMPR06:manor-sweep
## RULE_QUOTE: Five recruitments fire here: Tika, Morrigan, Tatsumaki, Artoria, Kaessi. Armory gold choice mandatory (Tartuccio's push line, DC in PR_09 depends on it). Trap corridor Tartuccio refusal is character-defining mandatory beat. Burning building event sets lawful/chaotic alignment track. Save offer fires before final battle.

---

> ⛔ DO NOT (1) skip the armory gold choice — Tartuccio's push line is mandatory; DC in PR_09 depends on it
> ⛔ DO NOT (2) skip the trap corridor Tartuccio refusal — character-defining mandatory moment
> ⛔ DO NOT (3) skip the burning building event — it sets the lawful/chaotic alignment track
> ⛔ DO NOT (4) let Tartuccio fight in the front line or handle traps — he refuses and positions behind the player
> ⛔ DO NOT (5) skip Tika, Morrigan, Tatsumaki, or Artoria recruitments — all four join during this beat
> ⛔ DO NOT (6) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR06:manor-sweep]`
Line 2: `[RULE_QUOTE: Five recruitments fire here: Tika, Morrigan, Tatsumaki, Artoria, Kaessi. Armory gold choice mandatory (Tartuccio's push line, DC in PR_09 depends on it). Trap corridor Tartuccio refusal is character-defining mandatory beat. Burning building event sets lawful/chaotic alignment track. Save offer fires before final battle.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `corridor_cleared = TRUE`, `tartuccio_rescued = TRUE`
- `poison_reported`, `security_doubled`

**WRITES:**
- `tartuccio_gold` = `taken` / `left`
- `tika_recruited = TRUE`
- `morrigan_recruited = TRUE`
- `tatsumaki_recruited = TRUE`
- `artoria_recruited = TRUE`
- `artoria_guards_saved = TRUE` / `FALSE`
- `kaessi_met = TRUE`
- `secret_room_found = TRUE` (optional)
- `alignment_lawful_score` / `alignment_chaotic_score` (increment per choice)

**EXIT TRIGGER → PR_07_final_battle:**
- Player returns to the banquet hall from the courtyard
- Load `KM_PR_07_final_battle.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR06:manor-sweep]`
1. `[STATE READ] current_scene="prologue_sweep" | phase=PR_06_MANOR_SWEEP`
2. `[HP CHECK]`
3. Scene narration — lighting: Dim or Dark throughout (fire and window light only)
4. Player menu (include available directions/rooms)

---

## PHASE 3 CONTEXT

> **Middle of the night. Manor dark — torches out or knocked over. East wing on fire; smoke thickens by the minute. All Phase 3 scenes run in Dim or Dark lighting (firelight and window light only). NPCs react to the fire. Companions are not rested.**

---

## LIBRARY ENCOUNTER

```
ENEMIES : Assassin Rogue 2 ×2 | HP 18 each | AC 16
          Both positioned among bookshelves — partial cover
LOOT    : 12 gp, Scroll of Shield (1st level), Masterwork Dagger
```

**After combat:** Tika is here — fought the assassins alone before the player arrived. Polearm dripping. Three downed bodies at her feet.

**Tika:** *"Took you long enough! I was about to drag the bodies into a pile and start a SECOND fight just to keep busy. Three of 'em. Don't make a face about it — I waited tables ten years before I picked this up. Practice, mostly."* *(spins the polearm with the easy balance of a tray-carrier)* *"I'm following you now. Don't try to talk me out of it. I've been looking for somebody who walks INTO the fire instead of away."*

→ `tika_recruited = TRUE` (she does not formally join yet — sweeps rooms ahead through the manor)

---

## THE ARMORY

```
Thievery DC 1 to open — even a failed attempt works.
Contents: Composite Longbow + 20 arrows | Light Mace | Banded Mail (AC+6)
          Breastplate (AC+5) | Tower Shield (AC+4, Hardness 5) |
          Chest: 210 gp (guards' salaries) + Watchkeeper's Key
```

**Tartuccio:** *"We should take the money. Safeguard it from the invaders. We can return it afterward — or explain ourselves later. Either way, it's better than leaving it."*

```
Gold choice — sets Diplomacy DC for Rebuttal 2 in PR_09:
 1. Take it — all of it          [tartuccio_gold = taken — DC 15 in PR_09]
 2. Leave it — take only the key [tartuccio_gold = left  — DC 11 in PR_09]
 3. "Safeguard" it               [tartuccio_gold = taken — same DC as option 1]
 4. Give the key to Tartuccio to carry [unusual; he uses it himself next area]
 5. Examine chest for traps first [Perception DC 10 — none; thoroughness noted]
```

**Take the Watchkeeper's Key to proceed north.** (Required for trap corridor.)

---

## TRAP CORRIDOR + MORRIGAN

> *The north corridor has three pressure-plate traps.*

```
Trap 1: Spear Volley   | Reflex DC 14 or 2d8+4 Piercing
Trap 2: Electrical Arc | Reflex DC 14 or 2d6+4 Lightning
Trap 3: Blade Swing    | Reflex DC 13 or 1d12+4 Slashing
```

```
Options:
 1. Thievery (Disable Device) DC 16 each — careful disarm
 2. Recall Knowledge (Arcana/Dungeoneering DC 13) — study mechanism first
 3. Send Tartuccio first — [mandatory: he refuses, threatens to leave]
 4. Trigger carefully from range — reduced damage
 5. Perception DC 14 — no alternate path on this side
```

**⛔ TARTUCCIO REFUSAL:** If player attempts to send him first, he refuses. Character-defining mandatory moment. He does not go first through anything dangerous.

> *At the corridor end: Morrigan, leaning against the wall, watching the player handle the traps.*

**Morrigan:** *"Hmm. You actually thought through them. I had begun to lose hope."* She steps over the third trap as though it were a puddle. *"I disarmed mine an hour ago. I was waiting to see if anyone competent would arrive. [...] I am Morrigan. I am a witch. [...] if you happen to be heading to the banquet hall, I shall walk in your direction. The company will be marginally less tedious than my own."*

→ `morrigan_recruited = TRUE` | Alignment moment: pragmatism/sentimentality axis

---

## THE SECRET ROOM (Optional)

**Find it:** Perception DC 13 — north wall in upper study sounds hollow.

**Puzzle 1 — Four statues (number discs):**
Correct sequence: 4 — 5 — 1 (Arcana DC 14 for the lore: Aldori founding date glyph)
Wrong sequence: dart trap (Reflex DC 12 or 1d6 Piercing ×4)
Reward: Masterwork Longsword (1d8 S, +1 to hit) + Gold Ring (45 gp)

**Puzzle 2 — Two statues facing each other:**
Correct sequence: 6 — 1 (History/Society DC 12: heraldic pair mirror convention)
Reward: Silver Earrings (25 gp) + 35 gp in lockbox (Thievery DC 12)

→ `secret_room_found = TRUE` | XP: +75 (puzzle 1: +30, puzzle 2: +30)

---

## COURTYARD — TATSUMAKI + KAESSI

> *Three assassins dead in the courtyard — two crumpled against the far wall, one inside a circular crater where cobblestones have been pushed outward in a perfect ring. A small woman with green hair, sitting cross-legged in the air, three feet off the ground.*

**Tatsumaki:** *"Mm. There you are."* (does not look down) *"Three of them came at me. They picked the wrong courtyard."*

She lowers herself reluctantly to near-ground level. Her boots hover by half an inch.

**Tatsumaki:** *"You're going somewhere. Banquet hall. Fine. I'll come. Not because you asked. Because I'm BORED and the sky is wasting my time."*

**Check:** Diplomacy OR Intimidation DC 15 — she joins regardless; check affects Relationship score only.
→ `tatsumaki_recruited = TRUE` | Alignment moment: chaotic track

---

**Kaessi (tiefling, fire-orange eyes, water and flame at her fingertips):**
Fighting two assassins nearby — she doesn't need help, but notices the player.
After fight: *"Appreciated. Or not necessary. Either way."* — Departs on her own.
→ `kaessi_met = TRUE` (recruitable Act 2; does NOT join now)

---

## KESTEN GARESS + BURNING BUILDING → ARTORIA

**Kesten:** *"Two guards are trapped up there. I don't have anyone to send in."* He looks at the player. Not a request. An assessment.

```
══════════════════════════════════════════════════════
THE BURNING BUILDING — Alignment Track Moment
══════════════════════════════════════════════════════
LAWFUL approaches (+1 lawful):
 1. Enter immediately — duty before risk [Athletics DC 9 to navigate smoke]
 2. Organize a methodical rescue [Diplomacy DC 10]
 3. Order someone else to follow you in — structured approach

CHAOTIC approaches (+1 chaotic):
 4. Let the building burn — the guards knew the risks
 5. Loot the room while in there anyway

NEUTRAL:
 6. Evaluate structural risk first [Perception DC 11]
 7. Ask Kesten what he thinks [he defers to player]
══════════════════════════════════════════════════════
```

**Outcomes:**
- Enter + succeed → guards saved. `artoria_guards_saved = TRUE`
- Enter + fail check → guards saved, player takes 1d6 fire damage
- Don't enter → guards die. `artoria_guards_saved = FALSE`

> *Artoria emerges from a side corridor. Sword bare. Breastplate scorched. She watched the burning-building moment from cover before stepping out.*

**Artoria (guards saved):** *"That was the act of a king. Not the title — the act. The choice was correct. I will not say it twice. I have been waiting to see whether tonight was theatre or oath. It was oath. I am with you."*

**Artoria (guards not saved):** *"I observed your reasoning. I disagree with the verdict. But you carried it. You did not perform reluctance you did not feel. That is rarer than a correct decision. I will follow. We will speak of this again."*

→ `artoria_recruited = TRUE` (joins regardless of outcome; outcome affects starting Relationship score)

**ALIGNMENT TRACK NOTE:**
Cumulative lawful choices through the sweep → Artoria on player's side at Phase 5 split.
Cumulative chaotic choices → Tatsumaki on player's side. Loser follows Tartuccio initially; recruitable Chapter 1.

---

## 🛑 NATURAL CHAPTER BREAK — SAVE OFFER (fires before exit to PR_07)

Manor sweep is complete. Five recruitments resolved (Tika / Morrigan /
Tatsumaki / Artoria + Kaessi), secret room investigated, armory gold
choice made, library / trap / courtyard / burning sub-beats fired.
Companions are committed. Next beat is the final battle — Assassin Leader
+ Frost Giant + Jamandi duel, full combat, multi-round encounter.

**This is a clean place to save and continue in a fresh chat.**

Before firing the EXIT TRIGGER, output the save offer:

```
🛑 NATURAL BREAK — SAVE HERE?

Manor sweep complete: companions recruited, secret room investigated,
armory choice made. Next phase is the final battle — Assassin Leader,
Frost Giant, multi-round combat with Jamandi's duel.

This is a clean place to save and continue in a fresh chat.

 1. Save here. Output the full exhaustive save block — I'll start a new
    chat from it, with PR_07 fresh in attention.
 2. Keep going. Continue to PR_07 in this chat.
```

**If 1**: Before writing the JSON, populate `dm_resume_note` from current scene state — `player_position` (exact location and stance at this moment), `player_last_action` (what player did immediately before save), `player_intent` (what they were working toward), `room_state` (each active NPC: name → location + status), `carousel_state` (turn + which NPC fired + approval score + tartuccio_clock), `open_threads` (copy from npc_threads verbatim), `level_up` (available + whether player has declared), `weapons` (on person or stowed location). Then output the full exhaustive save block per `KM_SaveBlock_Template.md`
EXHAUSTIVE MODE rules. Set `save_label = "PR_06_sweep_complete"`. After
the block: stop. Do NOT advance to PR_07. Player resumes in a new chat.

**If 2**: proceed to EXIT TRIGGER below as normal.

---

## EXIT — TRANSITION TO PR_07

When player returns to the banquet hall from the courtyard:
- Set `manor_sweep_complete = TRUE`
- Load `KM_PR_07_final_battle.md`

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_07 (carries forward)

**Your next response after PR_06's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR07:final-battle]
[RULE_QUOTE: Assassin Leader + Frost Giant + Jamandi duel. Frost Giant is JAMANDI'S FIGHT exclusively — player CANNOT target. Jamandi cannot die or be incapacitated. Scripted Jamandi duel narration is verbatim. Loot window mandatory before any scene transition. Player must explicitly state they're done with the post-battle area before PR_08 fires.]
```

**Binding constraints:**
- Three combats: Assassin Leader + Frost Giant + Jamandi duel
- Frost Giant is JAMANDI'S FIGHT exclusively — player CANNOT target it (.fail 35 if attempted)
- Jamandi cannot die or be incapacitated in this beat
- Scripted Jamandi duel narration is verbatim from file
- Loot window mandatory before any scene transition
- Player must explicitly state done before PR_08 fires

---

*KM_PR_06_manor_sweep.md — Prologue atomic beat 06 | v92.0*
