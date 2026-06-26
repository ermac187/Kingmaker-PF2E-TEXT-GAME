# KM_PR_07_final_battle.md — Prologue Beat 07: FINAL BATTLE
## Atomic scene file | ≤ 8 KB | State: PR_07_FINAL_BATTLE
## FILE_KEY: KMPR07:final-battle
## RULE_QUOTE: Assassin Leader + Frost Giant + Jamandi duel. Frost Giant is JAMANDI'S FIGHT exclusively — player CANNOT target. Jamandi cannot die or be incapacitated. Scripted Jamandi duel narration is verbatim. Loot window mandatory before any scene transition. Player must explicitly state they're done with the post-battle area before PR_08 fires.

---

> ⛔ DO NOT (1) let the player target the Frost Giant — it is JAMANDI'S FIGHT exclusively (`.fail 35`)
> ⛔ DO NOT (2) skip or summarize the scripted Jamandi duel — output the narration verbatim
> ⛔ DO NOT (3) let Jamandi die or be incapacitated — she handles the Giant alone
> ⛔ DO NOT (4) skip the loot window — player cannot return to the mansion after Jamandi speaks
> ⛔ DO NOT (5) advance past loot collection without explicitly reminding the player to collect everything
> ⛔ DO NOT (6) transition to PR_08 until the player explicitly says they are done with the post-battle area — outputting the loot list is NOT permission to move on
> ⛔ DO NOT (7) replace or ignore selected menu dialogue — when the player selects a numbered option containing quoted speech, output **eRmaC:** followed by the EXACT TEXT already written in that option. You wrote it; the player chose it; it is now canonical. Do NOT generate different dialogue. Do NOT write what eRmaC "would have said." Echo your own menu text verbatim (`.fail 2`)

---

## ⛔ FIRST TWO OUTPUT LINES — FILE_KEY + RULE_QUOTE (proof of load)

Line 1: `[FILE_KEY: KMPR07:final-battle]`
Line 2: `[RULE_QUOTE: Assassin Leader + Frost Giant + Jamandi duel. Frost Giant is JAMANDI'S FIGHT exclusively — player CANNOT target. Jamandi cannot die or be incapacitated. Scripted Jamandi duel narration is verbatim. Loot window mandatory before any scene transition. Player must explicitly state they're done with the post-battle area before PR_08 fires.]`

Both strings exist ONLY in this file's header. Missing or paraphrased = `.fail 9`. VERBATIM ONLY.

---

## STATE IO

**READS:**
- `manor_sweep_complete = TRUE`
- `security_doubled` (affects Mirror Image count and Kesten arrival timing)
- `poison_reported` (affects NPC status — paralyzed guests vs. alert guests)

**WRITES:**
- `jamandi_duel_witnessed = TRUE`
- `battle_resolved = TRUE`
- Loot collection flags (per item)

**EXIT TRIGGER → PR_08_the_calm:**
- Assassin Leader and Rift Channelers defeated
- Scripted duel has fired and resolved
- Loot window presented and player has collected
- Load `KM_PR_08_the_calm.md`

---

## REQUIRED OUTPUTS (every response in this beat)

0. **FILE_KEY line 1**: `[FILE_KEY: KMPR07:final-battle]`
1. `[STATE READ] current_scene="prologue_hall" | phase=PR_07_FINAL_BATTLE`
2. `[HP CHECK]`
3. Combat narration / player turn
4. Enemy condition tracking

---

## RETURN TO THE HALL

> *The hall is unrecognizable. Windows solid black — orange fire reflected in cracked glass. Table overturned, candles scattered, smoke from above.*
>
> *Jamandi Aldori — dueling silks, no armor, sword out, bleeding from a cut across her arm. She didn't have time to change. She hasn't retreated an inch. Ezvanki crouches behind the table cycling heals. Around her: the Assassin Leader and his Rift Channelers.*
>
> *One assassin near the servant door has stopped. He is looking at you. His body changes — skin going granite-grey, frame expanding. Eight feet. Then nine. The Frost Giant stands where a man was standing. It turns toward Jamandi. The assassins were the distraction.*
>
> *Tika arrives from the east corridor two rounds into the fight — polearm out, hair plastered, already swinging.*

---

## COMBAT STATS — FINAL BATTLE

```
[GM SCENE BRIEF — Banquet Hall Final Battle]

Assassin Leader (Rogue/Sorcerer 4)
  HP 48 | AC 19 | Fort +4 | Ref +9 | Will +6
  Mirror Image: 3 images active on entry
  Rapier d20+8 (1d6+4 P) | Sneak Attack +2d6
  Spells: Mirror Image, Protection from Good, Cause Fear
  Loot: Bracers of Armor +1, Potion of Barkskin, Alch.Fire ×1, Acid Flask ×2

Frost Giant (Shapeshifter, true form)
  HP 62 | AC 17 | Speed 35 ft | Fort +10 | Ref +5 | Will +6
  Greataxe d20+10 (1d12+8 S, 2-hand) | Reach 10 ft | Knockdown on crit
  Loot: Greataxe (1d12 S), Chainshirt (AC+3)
  ⛔ JAMANDI'S FIGHT — player does NOT target the Giant at any point. `.fail 35`

Rift Channelers ×3 (Summoner thralls)
  HP 16 each | AC 13 | Claw d20+4 (1d6+2 S)
  Special: Summon Fiendish Creature (1/each if not killed quickly)

ALLIES: Jamandi Aldori (fighting, do not let her die)
        Ezvanki Keeg (healing Jamandi, non-combat)
        Tika (joins Round 2 if not already present)
        All recruited companions fight alongside player

PRIORITY: Rift Channelers first → Assassin Leader

If security_doubled = TRUE:
  Kesten arrives Round 3 with 2 guards (additional allies)
  Assassin Leader has only 1 Mirror Image — was rushed
```

**Mirror Image:**
Each attack while images active — d4: 1-3 hits image (destroyed, no damage to Leader); 4 hits real Leader.
Image count: 3 → 2 → 1 → 0. AOE or Dispel Magic destroys all images simultaneously.

**Initiative:**
```
🎲 INITIATIVE
  [Player]        : d20 + [Init]
  Assassin Leader : d20 + 6
  Frost Giant     : d20 + 2
  Rift Channelers : d20 + 1 (×3, same roll)
  Jamandi (allied): d20 + 5
  Tika (Round 2)  : d20 + 4
```

---

## ⛔ SCRIPTED DUEL — JAMANDI vs FROST GIANT

**Trigger:** Frost Giant drops to 31 HP or fewer. Fires immediately — player's combat turn pauses for 1 round.

> *Jamandi breaks from the melee. She is bleeding from three wounds. Her sword arm should not work as well as it does. She strides directly toward the Frost Giant — not running, walking — with the measured pace of someone who has done this before and is not interested in doing it again.*
>
> *The Giant swings. Jamandi drops under the greataxe — flat, one palm on the floor — and the blade passes over her by inches. She rises inside the Giant's reach, where its weapon is useless and hers is not.*
>
> *Two cuts. The first opens the Giant's hamstring. The second, rising, takes it across the ribs as it stumbles. Not showy. Not acrobatic. A swordlord's economy — the minimum violence required, delivered with the precision of someone who has spent forty years making a blade an extension of her intent.*
>
> *The Giant falls to one knee. Jamandi steps back. She is not breathing hard. Her eyes have not changed since she started walking.*
>
> *That is a swordlord. The title is not inherited. It is proven.*

**Mechanical effect:** Jamandi's strikes kill the Frost Giant. Giant HP → 0 at end of narration. Full Giant XP awarded to player (allied NPC credit). Player or Tika stealing her kill = `.fail 35` — it permanently misframes Jamandi as a noble who needed saving.

Set `jamandi_duel_witnessed = TRUE`. NPCs reference this for the rest of the campaign.

---

## LOOT WINDOW

> **⛔ DM INSTRUCTION:** Output the loot list. Then **STOP** — output the POST-BATTLE
> MENU below. Do NOT transition to PR_08 until player explicitly says they are done.
> "Collect all loot before speaking to Jamandi Aldori. You cannot return to the
> mansion after this conversation."

```
Available loot — must be collected NOW:
  Assassin Leader  : Bracers of Armor +1, Potion of Barkskin, Alch.Fire ×1, Acid Flask ×2
  Frost Giant      : Greataxe (1d12 S), Chainshirt (AC+3)
  Secret Room      : Masterwork Longsword + Gold Ring (45 gp) [if found in PR_06]
  Armory           : Any armor/weapons taken in PR_06
  Chests/Corridors : 8 gp (corridor), silver earrings + 35 gp (secret room), 12 gp (library)
  Jamandi's Gifts  : Camping Supplies ×1, Rations ×4, Scroll of Raise Dead [given in PR_09]
```

**POST-BATTLE MENU — output after loot list. Wait for player input.**

```
The battle is over. The hall is yours for now.

What do you do?
 1. Collect loot — take specific items from the list above.
 2. Search the bodies more thoroughly.  [Perception DC 10]
 3. Retrieve any gear you dropped or left during the fight.
 4. Check your companions — assess wounds and condition.
 5. Take a moment — catch your breath, look around.
 6. Examine the hall / the damage / the dead.
 7. Speak to one of your companions.
 8. Approach Jamandi. [only when player is ready — triggers exit]
 9. Custom action.
```

Remain in this beat until the player chooses option 8 or explicitly signals readiness.
Every other option resolves fully and returns to this menu.

---

## EXIT — TRANSITION TO PR_08

Only when player chooses to approach Jamandi or explicitly signals done:
- Set `battle_resolved = TRUE`
- Load `KM_PR_08_the_calm.md`

---

## ⛔ NEXT-SCENE LOAD MANDATE — PR_08 (carries forward)

**Your next response after PR_07's exit MUST begin with these two lines verbatim:**

```
[FILE_KEY: KMPR08:the-calm]
[RULE_QUOTE: Phase 4.5 player-triggered ONLY — no candles-burn-low or scene-winds-down auto-advance. No uninvited Tartuccio sits. Declared+titled companions do NOT initiate while ⏳ Waiting companions exist. Tartuccio circulates within the hall, never out of it. Save offer fires before accusation.]
```

**Binding constraints:**
- Phase 4.5 fires on PLAYER signal only — no auto-advance via "candles burn low," "evening winds down," or any ambient scene-end cue
- Tartuccio does NOT sit at any table without being invited (.fail 17)
- Declared+titled companions do NOT initiate while Waiting companions still exist
- Tartuccio circulates within the hall — never exits the hall
- Save offer fires before accusation transition

---

*KM_PR_07_final_battle.md — Prologue atomic beat 07 | v92.0*
