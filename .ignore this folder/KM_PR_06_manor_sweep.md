# KM_PR_06_manor_sweep.md — Prologue Beat 06: MANOR SWEEP (REJOIN)
## Atomic scene file | ~16 KB (five rejoin scenes) | State: PR_06_MANOR_SWEEP
## FILE_KEY: KMPR06:manor-sweep
## RULE_QUOTE: Five REJOIN scenes fire here — Hu Tao (Library), Keqing (Trap Corridor), Yor Forger (Courtyard), Aerith (Kitchens/Burning), Leliana (Ballroom). Active 5 are ALREADY party companions separated in PR_04 explosion + PR_05 corridor; these are reunions, NOT recruitments. Companions only know what they observed in their own corner — no overall conspiracy knowledge until PR_09. Armory gold choice mandatory (Tartuccio's push line, DC in PR_09 depends on it). Trap corridor Tartuccio refusal is character-defining mandatory beat. Burning kitchen event sets lawful/chaotic alignment track. Save offer fires before final battle.

---

> 🗺️ **EXPLORABLE ROOMS + DISPATCH:** this beat's room set is in **`KM_PR_NightAttack_Rooms.md § PR_06`** — load alongside. Each of the five corners has a FIXED encounter state (mid-battle / already-cleared / fire-crisis); helping a fighting companion = they JOIN. Your companion **force is divided across the five corners by % (§ FORCE DISTRIBUTION)** — Active 5 = fixed anchors, any extra companions distribute by weight (Ballroom/Kitchen 25% each, Library 20%, Trap/Courtyard 15%), reassignable by the player. The player may take one corner and **dispatch** groups to others (Hero-overflow cost). Library/Kitchen/Ballroom are dispatchable; Trap/Courtyard/Armory hold scripted beats needing the player.
> ⛔ DO NOT (1) skip the armory gold choice — Tartuccio's push line is mandatory; DC in PR_09 depends on it
> ⛔ DO NOT (2) skip the trap corridor Tartuccio refusal — character-defining mandatory moment
> ⛔ DO NOT (3) skip the burning kitchen event — it sets the lawful/chaotic alignment track
> ⛔ DO NOT (4) let Tartuccio fight in the front line or handle traps — he refuses and positions behind the player
> ⛔ DO NOT (5) skip any of the five rejoin scenes — Hu Tao, Keqing, Yor Forger, Aerith, Leliana all rejoin in this beat
> ⛔ DO NOT (6) treat the Active 5 as recruitments — they are ALREADY companions; these are reunions after separation
> ⛔ DO NOT (7) let any rejoining companion narrate overall conspiracy detail — each knows ONLY what they observed in their corner of the manor; PR_09 is the reveal
> ⛔ DO NOT (8) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR06:manor-sweep]`
Line 2: `[RULE_QUOTE: Five REJOIN scenes fire here — Hu Tao (Library), Keqing (Trap Corridor), Yor Forger (Courtyard), Aerith (Kitchens/Burning), Leliana (Ballroom). Active 5 are ALREADY party companions separated in PR_04 explosion + PR_05 corridor; these are reunions, NOT recruitments. Companions only know what they observed in their own corner — no overall conspiracy knowledge until PR_09. Armory gold choice mandatory (Tartuccio's push line, DC in PR_09 depends on it). Trap corridor Tartuccio refusal is character-defining mandatory beat. Burning kitchen event sets lawful/chaotic alignment track. Save offer fires before final battle.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

> ⛔⛔ **HARD GATE — DO NOT LOAD PR_06 UNLESS PR_05 IS COMPLETE** (`corridor_cleared = TRUE` AND `tartuccio_rescued = TRUE` AND `tartuccio_ring` decided). If any is missing, PR_05 was not finished — STOP and return to `KM_PR_05_corridor_rescue.md`. And ⛔ **PR_06 may NOT be skipped on the way to PR_07** — the five reunions + fire + rescues here are mandatory and PR_07 hard-gates on `manor_sweep_complete`. (This is the self-enforcing chain: PR_04→05→06→07, each beat refuses to load until the prior's clear-gates are met — the explorable-rooms design, KM_PR_NightAttack_Rooms.md.)

---

## STATE IO

**READS:**
- `corridor_cleared = TRUE`, `tartuccio_rescued = TRUE`
- `poison_reported`, `security_doubled`
- Active 5 companion flags (all `_in_party = TRUE` from PR_02): `hutao_in_party`, `keqing_in_party`, `yor_in_party`, `aerith_in_party`, `leliana_in_party`
- `linzi_in_party = TRUE` (stayed with player through PR_05)

**WRITES:**
- `tartuccio_gold` = `taken` / `left`
- `hutao_rejoined = TRUE`
- `keqing_rejoined = TRUE`
- `yor_rejoined = TRUE`
- `aerith_rejoined = TRUE`
- `leliana_rejoined = TRUE`
- `kitchen_survivors_saved = TRUE` / `FALSE` (kitchen burning outcome)
- `leliana_ballroom_rally = TRUE` (14 guests held; affects PR_07 ally backdrop)
- `yor_staging_intel = TRUE` (if player asks; affects PR_07 tactical advantage)
- `secret_room_found = TRUE` (optional)
- `alignment_lawful_score` / `alignment_chaotic_score` (increment per choice)

**EXIT TRIGGER → PR_07_final_battle:**
- All five rejoin scenes complete OR player explicitly heads to banquet hall with 5/5 rejoins recorded
- Load `KM_PR_07_final_battle.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR06:manor-sweep]`
1. `[STATE READ] current_scene="prologue_sweep" | phase=PR_06_MANOR_SWEEP`
2. `[HP CHECK]`
3. Scene narration — lighting: Dim or Dark throughout (fire and window light only)
4. Player menu (include available directions/rooms + rejoin tracker)

---

## PHASE 3 CONTEXT

> **Middle of the night. Manor dark — torches out or knocked over. East wing on fire; kitchen pantry burning; smoke thickens by the minute. All Phase 3 scenes run in Dim or Dark lighting (firelight and window light only). NPCs react to the fire. The Active 5 were separated in the PR_04 explosion and PR_05 corridor chaos — each is somewhere in the manor, holding their own corner. Companions are not rested.**

---

## OPENING — RESIDENTIAL CORRIDOR

⛔ **CHRONICLER-NPC GATE — read before rendering this opening.** The "Linzi at his shoulder / 'pick a door'" cast is **Linzi-run ONLY.** If `linzi_replacement` is set / `leliana_chronicler_mode: TRUE` / `linzi_primary_chronicler: FALSE`, **Linzi is NOT in this run** — she does not walk with eRmaC and does not speak. Note the chronicler-bard (Leliana) is one of the FIVE scattered companions being rescued this beat (Ballroom), so she is NOT at eRmaC's shoulder either — there is **no chronicler-NPC present.** Render the replacement opening: eRmaC and **Tartuccio** step out; the "five doors, pick one" prompt is **eRmaC's own read** (or Tartuccio's prod), not Linzi's line. Forcing Linzi in = `.fail 9` (canon default over saved state).

> *[LINZI-RUN] eRmaC, Linzi at his shoulder, and Tartuccio trailing behind step out of the cleared corridor into the manor's residential spine. Smoke layers along the ceiling. Somewhere east, glass cracks in heat. Five doors — five directions — five companions unaccounted for since the blast.*
>
> *[LINZI-RUN] Linzi, quill already moving: "Five places, five of them. We don't have time to wait. Pick a door."*
>
> *[REPLACEMENT RUN] eRmaC and Tartuccio step out of the cleared corridor into the manor's residential spine. Smoke layers along the ceiling. Somewhere east, glass cracks in heat. Five doors — five directions — five companions unaccounted for since the blast. No time to wait — pick a door.*

```
REJOIN TRACKER — 0 / 5
 ⬜ Library / East Study   → Hu Tao      (last seen heading toward the screams)
 ⬜ Trap Corridor (upper)  → Keqing  (last seen taking the high window)
 ⬜ West Courtyard         → Yor Forger    (slipped outside at first lockdown)
 ⬜ Kitchens / Pantry Fire → Aerith      (was passing through when it lit)
 ⬜ Ballroom               → Leliana     (was performing — guests trapped there)
```

```
Which room first?
 1. Library / East Study
 2. Trap Corridor (need Watchkeeper's Key — see Armory)
 3. West Courtyard
 4. Kitchens / Pantry Fire
 5. Ballroom
 6. Detour to the Armory first (gold + key + gear)
 7. Detour to Secret Room (Perception DC 13 — north wall in upper study)
```

**Rooms can be done in any order.** Visiting all five fires `manor_sweep_complete = TRUE`. The Armory detour is required before Trap Corridor (key gate). Secret Room is optional.

---

## THE ARMORY (detour — same as v92)

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

**Take the Watchkeeper's Key to proceed to Trap Corridor.**

---

### LIBRARY — Hu Tao

> *The study door hangs by one hinge. Inside: lamp oil pooled on the rug, one shelf collapsed across the reading table, the great east window blown inward — glass on the carpet, night air feeding the smoke through. Three assassins down. Two among the books, one across the threshold. A redhead in dented plate stands in the doorway between the study and the inner library, longsword drawn at low guard, watching the bodies behind her like she still hasn't decided whether they earned a second pass.*

**Hu Tao:** *"Good. You are alive. Three came through the window. They are no longer a problem. I have been holding this room. The shelves are intact. The household ledgers are intact. I judged them worth holding."*

She does not sheathe the sword. Her eyes move to the threshold once, in case a fourth is still coming, then back to eRmaC. Her stance is formal — the verdict-stance, weight even, blade angled down. A streak of soot crosses her cheekbone. The rest of her is composed.

**Hu Tao — what she knows / what she did:** Three assassins entered through the east window roughly four minutes after the blast. Two were rogues; one had a poisoned blade — she noted the smell. She killed all three. She has not left the library since. She does not know how many more are in the manor. She does not know who they came for. She held the room because there were people inside it when the window broke — two clerks and a steward — and they are now in the back stacks, alive and frightened.

**Reunion state:** Combat-ready. Plate dented but intact. HP near full (took one cut to the off-arm — closed it herself with a strip of curtain). 1 Action Surge expended. No spells of course. Ready to move.

```
What do you do?
 1. "Hu Tao. Status — what did you see?"
 2. "The clerks — bring them. They come with us to the hall."
 3. "Hold here. The library is a chokepoint. Keep it ours."
 4. "Walk with us. We have four more to find."
 5. Inspect the bodies (Perception DC 10 — poisoned blade noted; matches PR_04 toxin)
 6. Custom action.
```

→ `hutao_rejoined = TRUE` | mark tracker.

---

### TRAP CORRIDOR — Keqing (requires Watchkeeper's Key)

> *The Watchkeeper's Key turns; the north corridor door swings into a narrow stone passage lit by one guttering sconce. Three pressure plates along the floor, each marked by a different scuff pattern. Halfway down, three assassins lie face-up on the flagstones — one arrow each, all through the eye. Above, at the high arrow-slit window: a silhouette, longbow held loose, one arrow already nocked but not drawn. Magus-coat dark with rain off the slate roof outside.*

**Keqing:** *"Three. Window angle. They never looked up."*

She does not climb down. She speaks down, calm, fragments only — the way she always does when she is still reading the field.

**Keqing:** *"Plates live. Don't walk it. I see the wiring from here."*

**Keqing — what she knows / what she did:** When the blast hit, she pulled to the upper gallery to find sightlines. She found the arrow-slit covering this corridor and the inner courtyard wall. She has been picking off anyone moving through the corridor. Three so far. She has not been down to check them — she has been holding the angle. She does not know what the assassins want. She does know they were moving toward the residential wing in pairs and threes, never alone, and never carrying loot. They came for a target, not the silverware.

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
 5. Ask Keqing to call out the plate edges from above — Perception assist, +2 to each disarm
 6. Perception DC 14 — no alternate path on this side
```

**⛔ TARTUCCIO REFUSAL:** If player attempts to send him first, he refuses. Character-defining mandatory moment. He does not go first through anything dangerous.

**Reunion state once corridor cleared:** Keqing drops from the window in one move, silent landing. Quiver at 11/20. No Spellstrike charges remaining (she burned them on the second assassin). Combat-ready at range; sword-ready in close.

```
What do you do?
 1. "Keqing. How many more in the building, your count?"
 2. "Stay on the window. Keep covering the corridor from above."
 3. "Come down. We need you with us — close quarters from here."
 4. "Loot the bodies. Anything marked, anything tagged."
 5. Custom action.
```

→ `keqing_rejoined = TRUE` | mark tracker.

---

### WEST COURTYARD — Yor Forger

> *The west courtyard door opens onto wet flagstones, planters knocked over, a fountain running red where someone bled into it and left. The hedgerow along the wall has been recently disturbed — broken twigs at thigh height, a partial bootprint in the mulch. No bodies visible. No sound except wind in the smoke.*
>
> *A shape detaches from the hedge — small, hooded, low. Yor Forger, daggers sheathed, hands open as she steps into the courtyard light so eRmaC does not flinch first.*

**Yor Forger:** *"You're okay? You're not hit?"*

She moves to him, quick, quiet, eyes already going past him to the corridor he came from to count who is with him. Soft voice — questions first, not statements. Two fingers on her own collarbone, a tic she does when she has been counting threats for too long without speaking.

**Yor Forger — what she knows / what she did:** When the manor locked down she slipped through a servant's window and went outside to scout. She has spent the last twenty minutes moving along the back walls and through the gardens. She has found:
- Two staging points the assassins came from — one in the east orchard (rope grapnels still hanging), one behind the carriage house.
- A wounded assassin under the carriage-house overhang, alive, gagged, hands bound — she did not kill him, she wanted someone to question.
- A tally: eleven incoming bodies counted in. Three down in the library (Hu Tao). Three in the trap corridor (Keqing). She thinks four are still inside, plus whatever leadership came in last.
- No view of who hired them. No insignia she recognized. They are professional.

**Reunion state:** Uninjured. Full Hide. Sneak Attack active on next engagement. Has the prisoner — wants to know what to do with him.

```
What do you do?
 1. "Yor Forger. The prisoner — bring him to the hall, alive. Jamandi will want him."
 2. "Yor Forger. The prisoner — kill him quiet. He saw your face."  [chaotic +1]
 3. "Walk us back through the staging points. We hit the orchard rope first."
 4. "Stay outside. Keep mapping. Signal when you see leadership move."
 5. "Come inside. We need you in the hall when this finishes."
 6. Ask what insignia, what coin, what gear — Recall Knowledge (Society DC 12)
 7. Custom action.
```

→ `yor_rejoined = TRUE` | `yor_staging_intel = TRUE` if asked. mark tracker.

---

### KITCHENS / PANTRY FIRE — Aerith

> *The kitchen door is jammed half-open with a fallen beam. Past it: the great hearth roaring sideways, the pantry door blown open, dried herbs and oil-jars going up in slow orange. The back court behind the kitchen is the calm island — eight, maybe nine kitchen staff and one guest, laid out on a tarp, soot-streaked, breathing, some bandaged. Kneeling over them: a young woman in a soaked apron, a pink ribbon come half-loose from her braid, a smear of ash along one cheek, her staff laid across her knees and Sarenrae's light — a Heal cantrip — still feathering green-gold off her free hand.*

**Aerith:** *(looking up, and the relief is plain)* *"Oh — good, it's you. Help me a moment?"* *(a tired breath, a glance down the row of them)* *"They're alright. All of them — burned, some of them, breathing smoke, but alive. I got the pantry door open before it caught and pulled out who I could reach."* *(quieter, steadier)* *"There are still three inside. I'm nearly empty — I can manage one more, maybe, and not the way I'd like. So I'm very glad you came when you did."*

She is genuinely soot-streaked. She is genuinely tired — the kind of tired that has been working through it and means to keep working through it. The Heal-glow on her fingers is genuine, and her last-but-one slot. The people on the tarp are genuinely alive because of her. She is gentle about all of it, and entirely unwilling to stop.

**Aerith — what she knows / what she did:** When the cookfires went over she was passing through the back halls and felt it before she heard it. She got the pantry door open, pulled the assistant cook out by the apron, came back for two more. The pantry caught regardless. She has since pulled nine survivors out of the kitchen-and-pantry zone and stabilized them in the back court — burns, smoke, one paralytic-dart graze she neutralized with Cleanse Affliction. She has Heal slots left: 1 (×1st), 0 (×2nd). She is quiet, focused, and effective. She does NOT know who started the fire — she assumed it was the cookfires until she saw the paralytic graze.

```
══════════════════════════════════════════════════════
THE KITCHEN FIRE — Alignment Track Moment
══════════════════════════════════════════════════════
Three kitchen staff still inside the burning pantry-passage — Aerith is out
of slots to do another extraction this round. Player call:

LAWFUL approaches (+1 lawful):
 1. Go in yourself — Athletics DC 9 through smoke; pull them out
 2. Organize a chain — Diplomacy DC 10, three party members in formation
 3. Order a companion in with you — structured rescue

CHAOTIC approaches (+1 chaotic):
 4. Let the pantry burn out — staff are not your responsibility
 5. Loot the silver chest in the side pantry on the way past

NEUTRAL:
 6. Evaluate structural risk first [Perception DC 11]
 7. Hand Aerith a flask from your kit so she can keep working
══════════════════════════════════════════════════════
```

**Outcomes:**
- Enter / chain / order + succeed → staff saved. `kitchen_survivors_saved = TRUE`
- Enter + fail check → staff saved, player takes 1d6 fire damage
- Don't enter / let it burn → staff die. `kitchen_survivors_saved = FALSE`

**Reunion state:** Aerith walks with party from here. Loud. Tired. Out of high-tier slots, still has cantrips and Soothe rituals. Demands wine in PR_07 banquet hall — Jamandi will provide.

```
What do you do (after fire moment resolved)?
 1. "Aerith. Status — anyone in there I should know about?"
 2. "The paralytic graze — show me. That's important."  [unlocks PR_09 lead]
 3. "Bring the survivors with us. They're safer in the hall."
 4. "Walk with us. We need a cleric in the hall."
 5. Hand her a flask from your kit (Bag of Holding wine — she will remember this for life)
 6. Custom action.
```

→ `aerith_rejoined = TRUE` | mark tracker.

---

### BALLROOM — Leliana

> *The ballroom doors open on a wide hall lit by one surviving chandelier and the orange smear of fire through the high windows. The dance floor is debris — toppled chairs, a smashed wine fountain, three guests motionless along the far wall (paralytic afterimage — breathing, not moving). Fourteen others are seated in a tight half-circle at center, calm, attentive. Standing among them, harp case slung over one shoulder, bow held loose at her side: Leliana, concert dress torn at the hem, the last note of an Inspire Courage composition still hanging in the air like a held breath. Her chin is up. Her eyes are too bright for someone who has been awake for two hours in a burning manor.*

**Leliana:** *"The acoustics in this hall are CRIMINAL. Has no one heard of vaulted ceilings? —Don't look at me like that. I'm fine. I'm always fine. The point is, I kept them here, and they are all alive, and I would very much appreciate someone acknowledging that before asking me what happened."*

She doesn't lower the bow. The Inspire Courage aura is still live in the room — a warmth in the air, a subtle steadying of shoulders. She fires a quick, performance-bright smile at eRmaC, and the smile doesn't quite reach where the tiredness lives. She does not stop watching the gallery above.

**Leliana — what she knows / what she did:** The secondary blast hit the ballroom roughly two minutes after the first. Guests panicked; three caught a paralytic-dart fan from an assassin in the gallery (now gone — fled before she could see his face). Leliana used performance and Inspire Courage to stop the rest from scattering into the corridors, where they would have died. She has been holding the room for nineteen minutes on Inspire Courage sustained through Focus points. She knows: the paralytic is reversible (she has watched two of three twitch back). She knows the assassin in the gallery was masked. She does not know who they were after. She suspects — voiced with a dry shrug, only if asked — that the target was Jamandi, because the gallery shooter aimed first at the head table where Jamandi had been before she rose to meet the corridor.

**Reunion state (Combat-ready):** Focus pool: 1 / 2 remaining. Inspire Courage aura active. Dagger (reflavored as bow — simple weapon) at hip. Will hold the composition while the room is in danger. Walks with party once the 14 guests can be moved to a secured space (the secured library — Hu Tao's hold — is the obvious destination if Hu Tao is rejoined; otherwise the ballroom holds).

```
What do you do?
 1. "Leliana. The fourteen — move them to the library. Hu Tao is holding it."  [requires hutao_rejoined]
 2. "Leliana. Status — the paralyzed three, can they be moved?"
 3. "Stay. Hold the room. We finish the sweep and come back for you."
 4. "Walk with us. We need you in the hall."
 5. "Who fired the darts? Describe him."  [unlocks PR_09 lead]
 6. Play with her — Performance DC 10 — extends Inspire Courage one round, +1 ally
 7. Custom action.
```

→ `leliana_rejoined = TRUE` | `leliana_ballroom_rally = TRUE` | mark tracker.

---

## THE SECRET ROOM (Optional — unchanged)

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

## ALIGNMENT TRACK NOTE

Cumulative lawful choices through the sweep (kitchen save, prisoner alive, guests evacuated, traps disarmed carefully) → lawful axis weight in PR_09.
Cumulative chaotic choices (let pantry burn, kill prisoner quiet, loot during rescue) → chaotic axis weight. Active 5 voice their disapproval/approval in PR_07 banter, not here.

---

## 🛑 NATURAL CHAPTER BREAK — SAVE OFFER (fires after 5/5 rejoins, before exit to PR_07)

Manor sweep is complete. Five rejoin scenes resolved (Hu Tao / Keqing /
Yor Forger / Aerith / Leliana). Secret room investigated (optional). Armory gold
choice made. Library / trap / courtyard / kitchen / ballroom sub-beats
fired. Active 5 are reunited with eRmaC (and Linzi ONLY in a Linzi run — in a `linzi_replacement` run there is no Linzi; the chronicler-bard Leliana rejoins as one of the Active 5). Next beat is the
final battle — Assassin Leader + Frost Giant + Jamandi duel, full
combat, multi-round encounter.

**This is a clean place to save and continue in a fresh chat.**

Before firing the EXIT TRIGGER, output the save offer:

```
🛑 NATURAL BREAK — SAVE HERE?

Manor sweep complete: all five companions rejoined (Hu Tao / Keqing /
Yor Forger / Aerith / Leliana), secret room investigated, armory choice made.
Next phase is the final battle — Assassin Leader, Frost Giant,
multi-round combat with Jamandi's duel.

This is a clean place to save and continue in a fresh chat.

 1. Save here. Output the full exhaustive save block — I'll start a new
    chat from it, with PR_07 fresh in attention.
 2. Keep going. Continue to PR_07 in this chat.
```

**If 1**: Before writing the JSON, populate `dm_resume_note` from current scene state — `player_position` (exact location and stance at this moment), `player_last_action` (what player did immediately before save), `player_intent` (what they were working toward), `room_state` (each active NPC: name → location + status, INCLUDING all 5 rejoined Active companions and Linzi and Tartuccio), `carousel_state` (turn + which NPC fired + approval score + tartuccio_clock), `open_threads` (copy from npc_threads verbatim), `level_up` (available + whether player has declared), `weapons` (on person or stowed location). Then output the full exhaustive save block per `KM_SaveBlock_Template.md`
EXHAUSTIVE MODE rules. Set `save_label = "PR_06_sweep_complete"`. After
the block: stop. Do NOT advance to PR_07. Player resumes in a new chat.

**If 2**: proceed to EXIT TRIGGER below as normal.

---

## EXIT — TRANSITION TO PR_07

When player returns to the banquet hall with all five rejoins recorded:
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

*KM_PR_06_manor_sweep.md — Prologue atomic beat 06 | v93.18-C4 (rejoin rewrite)*
