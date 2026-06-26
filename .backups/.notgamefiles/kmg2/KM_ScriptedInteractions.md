# KINGMAKER — SCRIPTED INTERACTIONS
## KM_ScriptedInteractions.md | Referenced by: KM_Exploration.md, KM_Ch1–4.md

> **DM:** Scripted Interactions are multi-step choose-your-own-adventure vignettes triggered during exploration. Unlike normal scenes, they are self-contained — 3-5 decision points, each gated by different skills, companions present, or player resources. They handle non-combat encounters: crossing a bridge, negotiating with a spirit, navigating a trapped corridor. Present as text with numbered choices at each node.

---

## 📋 SCRIPTED INTERACTION FORMAT

```
═══════════════════════════════════════
SCRIPTED INTERACTION — {Title}
═══════════════════════════════════════
{Opening description — 2-3 sentences}

NODE 1:
 1. {Option — skill gated}  [Skill DC X]
 2. {Option — companion gated}  [Requires: {Companion}]
 3. {Option — resource gated}  [Costs: {item/gold/spell}]
 4. {Option — universal}  [No requirement]

→ Each option leads to NODE 2a, 2b, 2c, or 2d
═══════════════════════════════════════
```

### Rules
1. **3-5 nodes per interaction.** Not longer — these are vignettes, not dungeons.
2. **Every node has 3-4 options.** At least 1 universal (no requirement).
3. **Companion-gated options** require that companion in the active party AND at relationship Friendly+.
4. **Skill-gated options** use the standard PF2e check. Show the roll.
5. **Failure is not death.** Failed checks lead to harder paths or reduced rewards, not game over.
6. **XP at the end.** Award encounter XP based on the highest DC overcome.

---

## 🌉 SI-1: THE BROKEN BRIDGE (Ch1-2, Exploration)

**Trigger:** Party reaches a river crossing where the bridge has collapsed.

```
The bridge over the Shrike River is down — half the span
hangs into the water, timbers split and swollen. The river
runs fast here. Crossing on foot means waist-deep current.
The far bank has what you came for.

NODE 1 — THE CROSSING:
 1. Swim across  [Athletics DC 14] — Brute force
 2. Find another crossing point  [Survival DC 12] — Takes 4 hours extra
 3. Repair the bridge  [Crafting DC 16 + 2 hours + Lumber ×1] — Permanent fix
 4. Send a companion to scout  [Requires: Ranger or Rogue in party]
```

**Node 1 Results:**
- **Swim (Success):** Across but Wet condition. Equipment check: 10% chance one item soaked (DM rolls).
- **Swim (Failure):** Swept downstream. Takes 1d6 bludgeoning, washes up 1 hex south. Must backtrack.
- **Find crossing (Success):** Shallow ford found. Safe crossing, no penalties. +1 Scholarly.
- **Repair bridge:** Bridge permanently fixed. Future crossings instant. Kingdom map updated. +1 to trade routes using this hex.
- **Scout:** Companion finds a fallen tree crossing 200 ft upstream. DC 10 Acrobatics to cross. Safe.

```
NODE 2 — THE FAR BANK:
 1. Examine the ruins  [Perception DC 14]
 2. Search for tracks  [Survival DC 12]
 3. Set up camp and observe  [2 hours, auto-success]
 4. Push forward immediately  [No check]
```

**Node 2 Results:**
- **Examine ruins (Success):** Find carved rune. Recall Knowledge (Arcana DC 16) identifies it as a ward marker. +50 XP.
- **Tracks (Success):** Recent humanoid tracks — bandits passed 1 day ago. Direction learned.
- **Camp and observe:** See smoke from a camp 2 hexes away. Intelligence: learn enemy count (3-5).
- **Push forward:** No information gathered. Normal exploration continues.

```
NODE 3 — THE CAMPFIRE (only if Node 2 revealed camp):
 1. Approach openly  [Diplomacy DC 14]
 2. Sneak closer  [Stealth DC 16]
 3. Circle around and ambush  [Stealth DC 14 + Survival DC 12]
 4. Ignore and continue  [No check]
```

**XP Award:** 60 XP (moderate encounter equivalent).

---

## 🗿 SI-2: THE STONE GUARDIAN (Ch2-3, Dungeon Entrance)

**Trigger:** Party finds a sealed tomb/ruin entrance with a stone construct blocking the door.

```
A figure carved from granite stands before the entrance.
Its eyes are empty but oriented toward you. A voice — not
from the stone, from the air around it — speaks in Hallit:

"Name the three rivers that feed the Stolen Lands."

NODE 1 — THE RIDDLE:
 1. Answer correctly  [Recall Knowledge: Geography DC 14]
 2. Bluff an answer  [Deception DC 18]
 3. Search for the answer carved nearby  [Perception DC 12]
 4. Attack the guardian  [Combat: Stone Golem level 6]

NODE 2 — (if riddle passed):
"Name the king who lost these lands."
 1. Answer correctly  [Recall Knowledge: History DC 16]
 2. "There is no king. I am the ruler now."  [Intimidation DC 16]
 3. Ask Linzi  [Requires: Linzi in party, auto-success — she knows]
 4. Examine the guardian for clues  [Perception DC 14]

NODE 3 — (if both riddles passed):
The guardian steps aside. The door opens.
"You may pass. But what you seek inside will ask
harder questions than I did."
 → Dungeon entrance unlocked. +100 XP. +1 Scholarly.

(If combat chosen at any point: guardian fights.
Victory opens the door but no riddle XP.)
```

---

## 🌿 SI-3: THE FEY NEGOTIATION (Ch3+, Exploration near First World thin spots)

**Trigger:** Party enters a hex with active fey presence (Nyrissa connection).

```
A circle of mushrooms. Inside: a satyr sitting on a
stump, drinking from a cup that refills itself. He sees
you and grins. "Ah. The mortal who thinks they own the
Stolen Lands. How delightful. Sit."

NODE 1 — THE OFFER:
"I can tell you something about the woman in the garden.
The one who plants roses that eat worlds. But I require
payment. Not gold. Something interesting."
 1. Offer a story  [Performance DC 14 — satyrs love entertainment]
 2. Offer a secret  [Player must reveal a genuine secret from their backstory]
 3. Offer a drink from your supplies  [Requires: wine, mead, or specialty alcohol]
 4. Refuse to bargain with fey  [No check — satyr shrugs, disappears]

NODE 2 — THE INFORMATION (if payment accepted):
The satyr tells you ONE thing about Nyrissa (DM selects
based on current nyrissa_backstory_known level):
 - Known 0: "She was not always what she is. Someone made her this way."
 - Known 1: "The Lantern King took something from her. Not her power. Worse."
 - Known 2: "She cannot love. Not 'will not.' Cannot. The capacity was cut from her like a limb."
 - Known 3: "The piece he cut still exists. Somewhere in the First World. She's been looking for a thousand years."

nyrissa_backstory_known +1. +80 XP.

NODE 3 — THE PARTING GIFT:
"One more thing, free of charge."
The satyr tosses you a seed.
 1. Catch it  [Free item: Fey Seed — plant in kingdom hex for +1 Culture]
 2. Let it fall  [Seed grows into a mushroom circle on the spot — mark on map]
 3. Crush it  [+1 Ruthless. Satyr: "Interesting." Disappears faster.]
```

---

## 🏚️ SI-4: THE ABANDONED MILL (Ch2, Settlement Hex)

**Trigger:** Party explores a hex with a ruined mill marked on the map.

```
A water mill, abandoned. The wheel still turns — slowly,
grinding nothing. The door hangs open. Inside: flour dust
on every surface, undisturbed. Someone left in a hurry.

NODE 1 — THE ENTRANCE:
 1. Search the main floor  [Perception DC 12]
 2. Check the millstone mechanism  [Crafting DC 14]
 3. Go upstairs to the living quarters  [No check]
 4. Examine the flour dust for tracks  [Survival DC 12]
```

**Node 1 Results:**
- **Search (Success):** Ledger under the counter. Last entry: "They come at night. Three nights now. We leave tomorrow." Date: 2 months ago.
- **Mechanism (Success):** Mill is functional. Repair would take 1 day + 2 Lumber. Could become a kingdom building (free Mill, saves 6 RP). +1 Scholarly.
- **Upstairs:** Beds overturned. Personal belongings left behind. A child's toy on the floor.
- **Tracks (Success):** Clawed prints, not animal. Humanoid but wrong. Lead to the cellar door.

```
NODE 2 — THE CELLAR (if tracks found or player investigates):
 1. Open the cellar door cautiously  [Stealth DC 14]
 2. Call down  [No check — alerts whatever is there]
 3. Barricade the door and leave  [No check — safe exit]
 4. Send a companion down  [Requires: martial companion]

NODE 3 — BELOW:
 1. Fight the mites (3 Mite Warriors, CR 1 each)  [Combat]
 2. Offer food to drive them out  [Survival DC 12]
 3. Intimidate them into fleeing  [Intimidation DC 14]
```

**Resolution:** Mill cleared. Can be claimed as kingdom building. If mites driven out peacefully: Reputation +1. Families may return (Loyalty +1 in this hex if player posts notice at capital).

**XP:** 80 XP. +1 Scholarly if ledger found.

---

## ⛏️ SI-5: THE COLLAPSED MINE (Ch2-3, Mountain/Hill Hex)

**Trigger:** Party finds a mine entrance partially blocked by rockfall.

```
The mine entrance is half-buried. Timber supports visible
but cracked. Air from inside is cold and stale. Pick marks
on the rock face are old — decades, not years.

NODE 1 — ENTRY:
 1. Clear the rubble  [Athletics DC 16, 2 hours]
 2. Find a side entrance  [Survival DC 14, 1 hour]
 3. Examine the rock face  [Recall Knowledge: Mining/Geology DC 14]
 4. Leave it  [No check]

NODE 2 — INSIDE (dark, Darkvision or light needed):
 1. Follow the main shaft  [No check — leads to NODE 3]
 2. Examine the support timbers  [Crafting DC 12]
 3. Check for ore veins  [Perception DC 14]
 4. Listen carefully  [Perception DC 16]

NODE 3 — THE DEEP CHAMBER:
 1. Investigate the glowing mineral  [Arcana DC 16]
 2. Mine it  [Athletics DC 14 + Crafting DC 14]
 3. Touch it  [Fort DC 14 — cold damage if failed]
 4. Ask Harrim about the stone  [Requires: Harrim in party — auto-success]
```

**Resolution:** Mine contains a deposit of rare mineral (Arcane Dust ×3 or Gemstones ×2). If support timbers repaired (Crafting DC 12): mine becomes kingdom resource node (+1 Ore/turn). Harrim: "This stone is older than the mountain. It was here before the rock formed around it."

**XP:** 100 XP. +1 Scholarly if mineral identified.

---

## 🌳 SI-6: THE TALKING TREE (Ch3, Deep Forest Hex)

**Trigger:** Party enters a hex with an ancient oak marked as "First World Thin Spot."

```
The tree is enormous — twenty people could not circle its trunk.
Its bark has patterns that almost look like a face. As you
approach, the patterns move. The tree is looking at you.

"You are not from here." Its voice is the sound of roots
growing through stone. "Neither am I. Sit. I have time."

NODE 1 — THE CONVERSATION:
 1. Sit and listen  [10 minutes, auto — tree shares lore]
 2. Ask about Nyrissa  [Diplomacy DC 14]
 3. Ask about the Stolen Lands' history  [No check — free lore]
 4. Ask about your armor  [The tree has never seen Aerynth material]
```

**Node 1 Results:**
- **Listen:** Tree tells a story about the First World bleeding into Golarion. nyrissa_backstory_known +1 if below 3.
- **Nyrissa (Success):** "She was planted here by something that wanted to see what would grow. The Lantern King gardens with cruelty." nyrissa_backstory_known +1.
- **History:** The Stolen Lands were a fey border march. The "theft" was mortals building where the fey had not finished building.
- **Armor:** The tree goes still. "I have seen wood from ten thousand forests and metal from every mountain. I have not seen this. Where did you come from?" No answer satisfies the tree. It remembers the question.

```
NODE 2 — THE REQUEST:
"Something is wrong with my roots. The Bloom — it poisons
the deep water. I cannot move. I cannot fight. Will you
go to the spring, three hills east, and cleanse it?"

 1. Accept the quest  [Side quest added: Cleanse the Spring]
 2. Ask what's in it for you  [Diplomacy DC 12]
 3. Offer to try right here  [Nature DC 18 — partial fix only]
 4. Decline  [Tree understands — "Mortals have their own roots to tend."]
```

**Resolution:** Quest "Cleanse the Spring" added if accepted. Completing it later: tree grants a gift (Bonewood Staff — +1 Nature, +1 to healing spells in forests). If declined: tree is fine with it. Can return later and accept.

**XP:** 60 XP (conversation) + 120 XP (quest completion).

---

## 🏰 SI-7: THE RUINED WATCHTOWER (Ch3-4, Border Hex)

**Trigger:** Party explores hex containing a crumbling stone watchtower.

```
Four floors. The top two are open to the sky. The first floor
is intact but the door is barred from inside. Something scratched
"LEAVE" into the stone above the lintel. The scratching is recent.

NODE 1 — APPROACH:
 1. Call out  [No check — whoever is inside hears]
 2. Break down the door  [Athletics DC 16]
 3. Climb to the second floor  [Athletics DC 14]
 4. Circle the tower for another entrance  [Perception DC 12]

NODE 2 — INSIDE:
 A deserter from Pitax's army. Armed, scared, alone. He fled
 rather than participate in Irovetti's plans. He has intelligence.

 1. Reassure him — you're not Pitax  [Diplomacy DC 12]
 2. Threaten him out  [Intimidation DC 14]
 3. Offer asylum in your kingdom  [No check — automatic]
 4. Ask Valerie to talk to him  [Requires: Valerie — soldier to soldier]

NODE 3 — THE INTELLIGENCE:
 1. Ask about Pitax army strength  [He knows: 3 units, positions, general]
 2. Ask about Irovetti's plan  [He knows: timeline, invasion route]
 3. Ask about other deserters  [He knows: 4 more hiding in the Narlmarches]
 4. Ask all three  [Takes 2 hours, all intelligence gained]
```

**Resolution:** Full Pitax army intelligence if all questions asked (+2 to next army engagement). If asylum offered: deserter becomes minor NPC at capital (potential Spymaster agent). If other deserters found: 4 additional recruits (1 free militia unit).

**XP:** 80 XP. +1 Cunning if intelligence extracted. +1 Merciful if asylum granted.

---

## 💀 SI-8: THE BONE CAIRN (Ch4, Kamelands Hex)

**Trigger:** Party discovers a burial mound with recent disturbance.

```
Stones stacked in the old Kellid way. But the earth around
the base is freshly turned. Something dug in — or out.
The air smells of wet soil and something older.

NODE 1:
 1. Examine the disturbance  [Perception DC 14]
 2. Check for undead presence  [Religion DC 14]
 3. Dig  [Athletics DC 12, 1 hour]
 4. Leave it undisturbed  [No check — respectful exit]

NODE 2 — THE BURIAL CHAMBER:
 1. Examine the sarcophagus  [Perception DC 16]
 2. Read the Kellid inscriptions  [Society DC 14 or Linguistics DC 12]
 3. Open the sarcophagus  [Athletics DC 14 — releases occupant]
 4. Ask Harrim about the runes  [Requires: Harrim — auto-read, provides context]

NODE 3 — THE REVENANT:
 Not hostile. Not yet. A Kellid warrior, dead 200 years,
 disturbed by the Bloom's corruption of the earth. He asks
 one question: "Is my line ended?"
 1. Answer honestly  [Research or Recall Knowledge DC 16]
 2. Lie — "Your descendants live"  [Deception DC 18]
 3. Offer to find out  [Side quest: research Kellid genealogy]
 4. Destroy the undead  [Combat: Revenant CR 6]
```

**Resolution:** If answered truthfully or quest completed: Revenant rests peacefully. Grave goods: ancient Kellid weapon (+1 cold iron greataxe, historical significance). If lied to and caught (Revenant has +8 Perception): combat. If destroyed: weapon drops but Kellid faction −1. +1 Scholarly if inscriptions read. +1 Merciful if revenant laid to rest peacefully.

**XP:** 120 XP.

---

## ⚠️ DM RULES

1. **Scripted Interactions are self-contained.** Start to finish in one scene. No saving mid-interaction.
2. **Show all rolls.** Even in a narrative vignette, the dice are visible.
3. **Companion-gated options should feel valuable.** The player should think "I'm glad I brought Linzi."
4. **Create new ones for chapter-specific content.** This file provides the template and 8 examples. Chapter files can reference additional interactions using this format.
5. **1-2 per exploration session.** Don't overuse. These are special encounters, not the default.

**Save block:** `"scripted_interactions_completed": ["SI-1", "SI-3"]`

---

*KM_ScriptedInteractions.md — Kingmaker PF2e Text Adventure | Scripted Interactions v1.0*
*Inspired by Pillars of Eternity scripted interactions.*
