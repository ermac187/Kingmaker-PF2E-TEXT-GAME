
<!-- merged from KM_Ch2.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 2: TROLL TROUBLE & SEASON OF BLOOM
## KM_Ch2.md | Loads after: KM_Ch1_Export.md | Loads before: KM_Ch3.md

---

> **DM:** Load with KM.txt, KM_Companions.md, KM_Companions.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md, KM_BuildGuide.md.
> Import Ch1 Export Block before beginning.
> Chapter 2 has TWO main questlines running in parallel:
> **Troll Trouble** (Hargulka) and **Season of Bloom** (Ancient Curse/Nyrissa).
> Both must be resolved to complete the chapter.
> See KM_Ch2_P2.md for Season of Bloom content (Phases 5–8).

---

## 📋 CH2 LOAD CHECKLIST

```
[GM CHAPTER 2 LOAD CHECK]
□ All files loaded and confirmed
□ Ch1 Export Block imported — player level, kingdom state, hex map
□ Key flags read:
    stag_lord_fate          : [value]
    nyrissa_letter_found    : [TRUE/FALSE]
    nyrissa_early_contact   : [TRUE/FALSE]
    akiros_fate             : [value — if alive: Warden role available]
    tartuccio_journal_found : [TRUE/FALSE]
    sootscale_alliance      : [TRUE/FALSE]
    companion_split         : [current active party]
□ Kingdom state confirmed — Turn [X], all stats, leadership roles
□ New companions available to recruit: Ekundayo (this chapter)
□ Kalikke/Kanerah available (DLC — confirm if active)
□ Time pressure noted: Troll Trouble has soft deadline ~90 days
□ Game State Header output and confirmed
□ ONLY THEN: Begin Ch2 opening
```

---

## 🗺️ CHAPTER 2 OVERVIEW

**Levels:** 4 → 8 (L5 mid-chapter, L7 at Hargulka, L8 at Bloom resolution)
**XP:** 1,000/level flat (PF2e Remaster). L5=4k | L6=5k | L7=6k | L8=7k cumulative
**Duration:** ~60–90 in-game days across both questlines
**New regions:** Narlmarches (Troll territories), Kamelands, Dire Narlmarches

**Two parallel questlines:**
- **Troll Trouble** — Hargulka is building a troll kingdom. His raids threaten your borders. Find Trobold, confront Hargulka and Tartuccio/Tartuk.
- **Season of Bloom** — An Ancient Curse is manifesting. Plants die. Monsters transform. Tristian's secret begins to surface. Nyrissa's hand becomes visible.

**Key decisions:**
- Kill Hargulka or make him vassal (affects Ekundayo permanently)
- Expose/confront Tartuccio in Trobold (his Ch2 fate)
- Tristian's betrayal — forgive or condemn
- Season of Bloom source — Bald Hilltop resolution

---

## 🚀 OPENING — CAPITAL THRONE ROOM

### First Throne Room Events (first few days of Ch2)

> *Your capital is young. The throne room smells of fresh-cut timber. Petitions are already arriving.*

**Scripted events in order:**

**Event 1 — Stefano Moskoni's Visit (Day 1–3)**
A Pitax envoy arrives at your throne room — slick, well-dressed, entirely too comfortable with himself.
> **Stefano:** *"The Baron of the Stolen Lands. How novel. King Irovetti sends his... regards. He suggests that a young kingdom such as yours might benefit from Pitax's... guidance. As a protectorate, naturally."*

Player response options affect Pitax relationship and Irovetti's aggression in Ch5:
- Refuse firmly → Pitax relationship stays hostile, Irovetti respects strength
- Insult him → Same outcome + Stefano is humiliated, returns as enemy encounter
- Accept diplomatically → `pitax_soft_alliance = TRUE` — brief respite but Ch5 invasion is still inevitable
- Arrest him → Diplomatic incident, Jamandi sends a warning letter

XP: +100 for any response that resolves the encounter.

**Event 2 — Troll Sightings Report (Day 3–7)**
Kesten Garess (if Warden) brings reports: border settlements attacked. Two guards killed. Livestock taken.
> *"They're organized. Not like normal troll raids. Someone is directing them."*
`troll_trouble_quest = active`

**Event 3 — Linzi's Quest Trigger (Day 5–10)**
If Linzi is in party: she confesses the missing treasury funds. Easier to Ask Forgiveness begins.

---

## 📍 PHASE 1 — INVESTIGATING TROLL TROUBLE

### First Troll Encounter (scripted, on border hex)

> *The border. A farmstead. Still smoldering.*
> *Three trolls are still there, pulling apart a barn.*
> *They are larger than you expected.*

```
[SCRIPTED ENCOUNTER — First Trolls]
ENEMY: Troll ×3
  HP: 55 each | AC: 16 | Speed: 30 ft | Reach: 10 ft
  Jaws: d20+9 (1d10+6 P) | Claw ×2: d20+9 (1d8+6 S)
  Fort +10 | Ref +5 | Will +3
  SPECIAL: Regeneration 15 (fire or acid stops it for 1 round)
           Troll does NOT stay dead unless dealt fire or acid damage after dying
           A troll at 0 HP regenerates to 1 HP at start of its next turn
           EXCEPTION: If it takes fire or acid damage while at 0 HP → actually dead

CRITICAL MECHANIC — TROLL REGENERATION:
  After reducing a troll to 0 HP: must deal at least 1 fire or acid damage
  before its next turn to prevent regeneration. Options:
    Alchemist's Fire splash, Produce Flame, Acid Flask, Burning Hands, etc.
    A torch applied as an improvised weapon: d20+[Str] (1 fire damage, crude but works)
  If player does NOT have fire/acid: troll regenerates 15 HP at start of its turn.
  Recommend: DM warns player of regeneration on FIRST encounter (they learn the rule).

XP: 320 per troll = 960 total
```

**After combat:** Discover survivor — a farmhand hiding in the root cellar.
> *"They came from the east. Said something — in their own tongue. One word: Trobold."*

> **DM:** Award +25 XP for Gather Information. `trobold_name_known = TRUE`

---

### Key Ch2 NPC — Ekundayo

**Ekundayo** is encountered during the A Score to Settle questline (Phase 3).
A lean, taciturn ranger with a dog companion (Trkaa). His family was killed by a rock troll named Kargadd. He has been tracking it for years.

> *A man and a dog sit at a cold campfire. The man has the look of someone who has been waiting a very long time.*
> **Ekundayo:** *"You're hunting the trolls. So am I. Our paths are the same until they aren't."*

**Recruitment:** Available when player reaches Ekundayo's camp in the Narlmarches during Troll Trouble (Phase 3 — after Trobold becomes known).
No check required. He joins if the player agrees to help him find Kargadd.

```
1. "We'll find Kargadd together."  → He joins. Build prompt fires (Ranger — KM_Builds_Oracle_Psychic_Ranger.md).
2. "Not now."                      → He stays at his camp. Re-approachable any time in Ch2.
3. [Leave without speaking]        → Capital fallback triggers after Ch2 main quest resolves.
```

**Capital Fallback:** Ekundayo and Trkaa are at the Capital gates.
*"I heard you cleared Trobold. Kargadd — is he dead?"*
If `kargadd_killed = TRUE`: *"Then I'm done with what I came here for. You could use someone who doesn't miss."*
If `kargadd_killed = FALSE`: *"Then I still have work to do. I'd rather do it with you than alone."*
Accept → build prompt fires. Decline → he camps outside, permanently available but not in roster.

`ekundayo_recruited = TRUE` | `ekundayo_build = [chosen]`

**Ekundayo's Camp (Narlmarches Hex — cold campfire, treeline):**
```
Search the camp while Ekundayo is being recruited (Perception DC 13):
  Camp perimeter: Shortbow +1 (1d8+4 P, range 60 ft), Arrows ×20, 18 gp
  Bedroll cache (Perception DC 12 — hidden under gear):
    Locked chest (Thievery DC 14): Bracers of Armor +1, Potion of Lesser Healing ×2, 55 gp
  Outside, buried cache (Survival DC 15 — tracks near east tree):
    Scroll of Heal (L2), 28 gp, Flint and Steel
```

**Ekundayo's survival condition (Ch7):** Must complete A Score to Settle before Ch7.
If Hargulka is made vassal (not killed) AND Ekundayo's quest is incomplete: he leaves permanently.

---

### Key Ch2 NPC — Bartholomew Delbin

A reclusive wizard who has been studying the trolls. Lives at a secluded lodge.

**Encounter:** Random event triggers after first troll fight — a man named Dalton warns of a mage who can help with the trolls. Follow up → Secluded Lodge hex.

**What Bartholomew knows:**
- Hargulka is using a potion of some kind that grants the trolls a limited form of immortality (stolen dwarven formula)
- Trobold is in the Dwarven Ruins — ancient dwarf fortress the trolls have occupied
- The potion's weakness: it doesn't prevent fire or acid damage from bypassing regeneration

**Quest:** The Nature of the Beast — visit Bartholomew, learn the troll weakness formula.
Reward: Potion of Fire Breath ×3, scroll of Burning Hands, +300 XP
`troll_weakness_known = TRUE` — grants +2 to all attack rolls against trolls for the party

---

## 📍 PHASE 2 — VERDANT CHAMBERS (SOLO VISIT)

> *The enchanted forest Tiressia spoke of (if Ch1 glade was visited). The dryad herself.*

**If player visited glade in Ch1 (Tiressia's quest):**
She sends a message: *"Come alone. I have information about what is happening to the land."*
This triggers the solo Verdant Chambers visit — player goes without party (storybook event).

**If player did NOT visit in Ch1:**
Skip this phase. Tiressia's information surfaces later through Jhod instead.

**Verdant Chambers Storybook:**
```
Page 1: Enter the grove. Three monsters appear: Hydra, Manticore, Owlbear.
        A figure on the battlements watches and laughs: Guardian of the Bloom.
        [Athletics DC 15 to sprint past] or fight the three creatures.

Page 2: The Guardian speaks. She is radiantly beautiful and utterly wrong.
        "The Bloom will cover everything you've built. Stone by stone. Root by root."
        She disappears. The three creatures flee.

Page 3: Tiressia emerges.
  "That was the Guardian. She serves an old power — older than your kingdom.
   The seeds were planted years ago, in secret. Your advisor Tristian... I've
   seen him in my visions. He did not know what he was doing. But he did it."
```

`tristian_bloom_seeds_revealed = TRUE` — Tiressia's warning. DM notes: do NOT reveal this to player as game knowledge. Tiressia tells the player. The player now has this information. Use it.

---

## 📍 PHASE 3 — TROBOLD (DWARVEN RUINS)

### Approach

**Location:** Deep in the Narlmarches, 4+ days travel. Full party required.

**Jazon Encounter (outside Trobold):**
A troll — unusually composed, standing in the road rather than attacking.

> **Jazon:** *"Borba — human. Hargulka says: no eating. We don't eat borba now. You want to go inside?"*

**Options:**
```
[Lawful] "Take me to your kings. I am the ruler of the lands your Trobold stands on."
  → Jazon escorts player inside. Skip to Hargulka's hall directly.
  → Unlocks later dialogue option [Lawful Neutral] with Hargulka about peace.
  → jazon_escort = TRUE

Any other approach → Player enters normally. Full dungeon exploration.
```

**Fire/Acid Supply Check:**
> **DM:** Before the dungeon begins, check player inventory for fire/acid items.
> If none: Bartholomew's scrolls (if quest done) help. If neither:
> Offer to buy from Ekundayo (he carries torch supplies) or backtrack to capital.
> A party with no fire/acid will struggle badly in this dungeon.
> This is not a spoiler — Jazon hints: *"Hargulka's trolls don't die easy."*

---

### Trobold — Level 1 (Dwarven Ruins Surface)

```
[GM SCENE BRIEF — Trobold Entrance]
ENEMIES    : Troll Sentinels ×4, Trollhound Pack ×6
             Troll Shaman (drops Wand of Bless, Cloak of Resistance +2)
LOOT       : Torag's Pendant (south stash), Wand of Bless, Cloak of Resistance +2,
             Trollreaper (magic greatclub — counts as fire damage vs trolls)
HARRIM FLAG: Interact with the broken Torag statue here.
             Harrim's Quest — Lore (Religion) DC 15 check required.
             Pass check → dialogue option unlocks that advances Shattered Dreams.
             Fail → Harrim misses the key revelation. Quest becomes harder to resolve.
NPC        : Jubilost (if recruited in Ch1) — announces discovery of dwarven ruins (+1,800 gp)
[END BRIEF]
```

**Trollreaper:** 2H B weapon, 1d10+5. Special: deals fire damage as part of normal damage vs trolls. Bypasses regeneration automatically. Best weapon in this dungeon if your build can use it.

---

### Trobold — Level 2 (Depths)

```
[GM SCENE BRIEF — Trobold Depths]
ENEMIES    : Branded Trolls ×4 (stronger, resist fire somewhat — acid is better)
             Kargadd (Ekundayo's target — see A Score to Settle below)
             Named Troll Berserker ×2
MECHANIC   : Sunlight rooms — rooms with ceiling holes. Trolls make Fort DC 21
             each round in direct sunlight or are Petrified (slow kill but possible)
             DM can lure trolls into sunlight with Athletics DC 14 (bait and move)
NPC        : Dying Dwarf (locked room near Kargadd)
             Heal him (Medicine DC 15 or spell): he blesses party (Good Hope +2 morale 1 day)
             Kill him: −1 alignment (Good/Evil axis)
NPC        : Kobold Artist (deepest room, before Hargulka)
             Leave alone: [Chaotic Good]/[Neutral] — no consequence
             Kill: [Lawful Evil] — alignment flag
KEYS       : Rusty Dwarven Key, Steel Dwarven Key, Silver Dwarven Key
             Each unlocks a door/chest. All three needed for complete loot.
[END BRIEF]
```

---

### A Score to Settle — Kargadd

If Ekundayo is in the party and quest is active:

> *He goes still the moment you enter the room. His dog Trkaa presses against his leg.*
> **Ekundayo:** *"That's him. The one who killed my family."*

```
KARGADD — Rock Troll (Elite)
HP: 88 | AC: 19 | Speed: 30 ft | Reach: 10 ft
Slam ×2: d20+13 (2d8+8 B) | Rock Throw: d20+10 (2d6+8 B, range 60 ft)
Fort +14 | Ref +6 | Will +5
Regeneration 20 (fire or acid) — harder to stop than normal trolls
Special: Enrage if Ekundayo attacks him first — +4 damage for 3 rounds

SUNLIGHT OPTION (slow kill):
  Lure Kargadd into sunlight room. Fort DC 21 each round.
  Fails begin after 3–4 rounds typically (at +21 Fort, low probability per round).
  Each failure: Petrification advances by 1 stage (3 stages = fully petrified → dead).
  This takes many rounds and requires patience. Realistic if player has the setup.

POST-BATTLE: Ekundayo stands over the body for a long moment.
  "He's dead. My family is still dead. I thought this would feel different."
  +2 Relationship. Quest complete. ekundayo_quest = complete

KARGADD LOOT:
  Body          : Amulet of Natural Armor +2, 95 gp
  Hidden alcove (Perception DC 14 in his lair room): Ring of Protection +1, Venison ×4 (Camp ingredient)
```

---

### Hargulka's Throne Room

> *Two kings. Hargulka — massive, tusked, wearing a crown made of bones. Tartuk beside him — painted in kobold colors, staff raised, grinning.*

**Tartuccio/Tartuk Recognition:**
If `tartuccio_as_tartuk_revealed = TRUE` (from Ch1): Player recognizes him immediately.
If not: Perception DC 16 to notice something wrong about this "kobold shaman."
`tartuccio_ch2_confronted = TRUE`

**Hargulka Dialogue Options:**

```
All paths eventually lead to combat, but dialogue choices affect the fight:

[Intimidate DC 20] → +45 XP, Hargulka is mildly unsettled (−2 to his first attack)
[Lawful Good] or [Attack] → Immediate combat
[Lawful Neutral — if jazon_escort = TRUE]:
  "You're the king of trolls. I'm the king of humans. Let's make peace as rulers do."
  Hargulka: "Your words are smooth for borba. But Tartuk says you must die."
  → Still leads to combat but unlocks Jazon sparing option after

[Requires Evil] → "Kill Tartuk now and I'll let your trolls live."
  → Hargulka obliterates Tartuk (Tartuccio Unkillable Protocol Tier 1 activates — he survives)
  → Fight only Hargulka (easier fight)
```

**The Fight:**

```
HARGULKA — Troll King (Fighter 7)
HP: 120 | AC: 22 (natural armor + dwarven breastplate) | Speed: 30 ft | Reach: 10 ft
Mallet of Woe: d20+14 (2d6+10 B, Shove, Knockdown on crit) — FIRE DAMAGE COUNTS
Jaws: d20+12 (1d10+8 P)
Fort +14 | Ref +6 | Will +5
Regeneration 20 (fire or acid)
Special: Troll Roar — Will DC 18 or Frightened 2 (1/combat, free action when bloodied)
         Relentless — if reduced to 0 HP with non-fire/acid damage, regenerates to 30 HP
Loot: Mallet of Woe (magic greatclub, fire damage property), Belt of Physical Might +2,
      Iron Dwarven Key, 480 gp

TARTUK/TARTUCCIO (fighting alongside Hargulka if not separated):
Stats: HP 24 | AC 17 | Spells: Fireball (6d6), Haste (cast on Hargulka round 1)
Unkillable Protocol active — he flees/survives regardless

RESOLUTION OPTIONS (after Hargulka is defeated):
Kill Hargulka → Standard. +600 XP.
Make Hargulka vassal (if jazon_escort = TRUE and Lawful Neutral dialogue used):
  → Hargulka swears to keep trolls from human lands.
  → `hargulka_vassal = TRUE`
  → CONSEQUENCE: Ekundayo leaves party immediately and permanently
                 (he came to kill trolls, not make them neighbors).
  → Minor stability bonus for kingdom. Trolls stop raiding.
Make Tartuk vassal (Kill Hargulka, then offer Tartuk survival):
  → Tartuk swears loyalty (lying)
  → `tartuk_vassal = TRUE`
  → Ekundayo leaves only if A Score to Settle is incomplete
  → Tartuk/Tartuccio departs — resurfaces in Ch3 with different scheme
```

**After Hargulka:**
- Explore full dungeon now that enemies are cleared (Harrim's quest, kobold artist, loot chests)
- Iron Dwarven Key opens the final sealed chamber — Headband of Alluring Charisma +4, Ring of Protection +2

**Trobold Key Chest Summary (all three keys required for full loot):**
```
Rusty Dwarven Key  → North storeroom door:
  Trollreaper (if not already looted from Level 1), Scale Mail +1, 120 gp

Steel Dwarven Key  → East vault door:
  Belt of Physical Might +2 (if not looted from Hargulka's body),
  Wand of Burning Hands (L2, 3 charges), 210 gp

Iron Dwarven Key   → Final sealed chamber (deepest level, past Kobold Artist):
  Headband of Alluring Charisma +4, Ring of Protection +2,
  Dwarven Thrower (returning thrown weapon, 1d6+Str B, returns 1A), 340 gp
```

**Cog-Wheel Rings Vault (Narlmarches exploration):**
```
The three rings (White, Gold, Red) are each hidden in separate Narlmarches hexes.
  White Ring  : Plains hex near river crossing — under a flat stone (Perception DC 15)
  Gold Ring   : Forest hex near Old Sycamore — in hollow tree (Perception DC 16)
  Red Ring    : Swamp hex near Old Beldame — submerged in shallow pool (Perception DC 17)

Vault location: Narlmarches Hills hex — a carved dwarven door in a hillside.
All three rings inserted simultaneously → door opens.

VAULT CONTENTS:
  Armor        : Breastplate +1 (AC+5, Dex cap +3)
  Weapon       : Elven Curve Blade +1 (1d8+4 S, Finesse/Forceful) — best in slot for Builds 7/20
  Consumables  : Potion of Fly (1 minute), Scroll of Haste (L3), Potion of Barkskin ×2
  Gold         : 380 gp
  Key item     : Cog-Wheel Medallion (story item — Jubilost recognizes it if in party; +lore)
XP: +250 for discovering and opening the vault
```

---

## 📍 PHASE 4 — AFTERMATH & SIDE CONTENT

### XP Summary — Troll Trouble Portion

| Source | XP |
|--------|----|
| First troll encounter (×3) | 960 |
| Bartholomew / Nature of the Beast | 300 |
| Verdant Chambers (if visited) | 240 |
| Trobold Level 1 | 800 |
| Kargadd (if fought) | 480 |
| Trobold Level 2 enemies | 640 |
| Hargulka (boss) | 600 |
| Tartuk (if fought) | 200 |
| A Score to Settle completion | 480 |
| Side quests (Lost Child, Cog-Wheel Rings, etc.) | ~400 |
| **Troll Trouble total** | **~5,100 XP** |

### Notable Side Quests This Phase

**Lost Child** — Jenna's son Tig has gone missing. Investigation leads to the Lizardfolk village and the Swamp Witch's Hut area. Tig is alive. Rescue him → +Loyalty to kingdom, Jenna's family becomes minor kingdom contact.

**Cog-Wheel Rings** (Narlmarches exploration) — Three rings hidden in the wilderness (White, Gold, Red) that open a vault with magic gear. Pure exploration reward.

**Stefano Moskoni Random Encounter** — If he survived the throne room, he appears during Troll Trouble wilderness travel, being attacked by trolls. Save him → 300 XP. He later becomes a recurring Pitax informant.

---

### 🏛️ SIDE QUEST — LANDER LEBEDA (THRONE ROOM)

**Quest giver:** Lander Lebeda, Brevoy noble. Arrives at the throne room Day 8–12 of Ch2.

**Lander:** *"Baron/Baroness. A pleasure. I represent a merchant consortium with interests in the Greenbelt. We have a... situation. A trade route your territory controls. I'd like to discuss terms before someone less civilized raises the issue with arrows."*

He wants a formal trade agreement — his consortium gets preferential use of the road through your territory, you get a cut of the toll revenue. Straightforward, except his consortium is quietly backed by House Surtova.

**Resolution options:**
- **Accept terms** → `lander_agreement = accepted` → +2 Economy/turn, +1 Surtova reputation. Lander becomes a recurring contact.
- **Negotiate better terms** → Diplomacy DC 16 → `lander_agreement = renegotiated` → +3 Economy/turn, +1 Surtova rep, Lander respects the player.
- **Reject** → `lander_agreement = rejected` → −1 Surtova reputation. Lander leaves politely. The road dispute resurfaces in Ch4 as a minor kingdom event.
- **Investigate the consortium** → Society DC 14 → discovers Surtova backing. Player may use this as leverage: Diplomacy DC 18 → +4 Economy/turn AND letter of Surtova acknowledgment (+2 Surtova rep). `lander_surtova_exposed = TRUE`

**XP:** +150 on any resolution. +50 bonus if renegotiated or exposed.

---

### 🐍 SIDE QUEST — TSANNA (SEASON OF BLOOM BRANCH)

**Quest giver:** Tsanna, priestess of Lamashtu. Found at the Goblin Fort (Womb of Lamashtu) during Phase 6 — Season of Bloom. She is not hostile on first contact if the player approaches without attacking.

**Tsanna:** *"You are not what I expected. The Bloom brought soldiers before. You are asking questions. That is different."*

She knows who opened the Bloom. She will tell you — but only if you spare her and let her leave. She is a Lamashtu cultist and she is not lying about what she knows.

**Resolution options:**
- **Spare her, accept her information** → `tsanna_spared = TRUE` → She names the source of the Bloom contamination (points directly to Bald Hilltop Part 2 location). `bloom_source_known_early = TRUE` → Phase 6 DC checks reduced by 2. She disappears. She may reappear in Ch4.
- **Kill her** → `tsanna_killed = TRUE` → Standard combat. No information. Bloom source must be found the hard way. +200 XP.
- **Capture her for questioning** → Intimidation DC 16 → same information as sparing, but she is imprisoned. `tsanna_imprisoned = TRUE` → +1 Loyalty (justice seen to be done), +200 XP.

**Alignment:** Sparing her is Chaotic/neutral. Killing is Lawful/neutral. Capturing is Lawful/good.

---

### 🐴 SIDE QUEST — XAMANTHE AND THE NOMEN CENTAURS

**Quest giver:** Xamanthe, Nomen centaur scout. Found wounded during Ch2 exploration of eastern Greenbelt hexes (Hex 3,−2 or adjacent). Triggered on first visit to that area.

> *A centaur woman, injured, arrow in her flank. She is not asking for help. She is waiting to die with dignity. She looks at you like she expects you to finish the job.*

**Xamanthe:** *"You are the new ruler. Our lands border yours. I was scouting — your people's trolls came east. Killed two of my sisters."*

She is not accusing the player directly. She is reporting facts. She wants to know if the player is going to be a problem.

**Initial resolution:**
- **Offer healing** → Medicine DC 12 or any healing spell → `xamanthe_healed = TRUE` → attitude shifts to Neutral. She will talk.
- **Ignore her** → She leaves. `xamanthe_ignored = TRUE` → Nomen Centaurs start at −3 faction (worse than default −2).
- **Attack** → `xamanthe_attacked = TRUE` → Nomen Centaurs at −5. War event triggers in Ch3.

**If healed and talked with:**
Xamanthe explains the Nomen Centaurs claim the eastern Greenbelt as ancestral land. She is not demanding the player leave — she is asking for formal acknowledgment and a boundary agreement.

- **Agree to negotiate a boundary** → Diplomacy DC 14 → `xamanthe_boundary_agreed = TRUE` → Nomen rep +3, Xamanthe becomes a named contact. She will send word to her tribe. `centaur_alliance_path = open`
- **Refuse or deflect** → She accepts it. *"Then we will watch and wait."* No penalty yet, but centaur alliance path closes until Ch3.

**XP:** +200 on any resolution except attack. +100 bonus if boundary agreed.

**Carries forward:** Xamanthe's status (`healed` / `ignored` / `attacked`) directly affects the Nomen Centaur faction score at Ch3 start and the Vordakai arc difficulty. See KM_Kingdom.md faction table.

---

---

### 👊 COMPANION RECRUITMENT — NOK-NOK (Goblin Village, Narlmarches)

```
LOCATION : Goblin camp, southern Narlmarches — discoverable during exploration
TRIGGER  : Player enters camp; goblins scatter except one who does not run
```

> *A goblin the size of a large dog stands alone in the middle of the camp, holding a knife almost as big as he is, facing the direction everyone else fled from.*
> **NOK-NOK:** *"You kill trolls? Nok-Nok also kill trolls. Nok-Nok kill everything. Nok-Nok is HERO."*

```
1. "Prove it. Come with us."         → He joins. Build prompt fires (Rogue — KM_Builds_Rogue_Sorcerer.md).
2. "What kind of hero needs a gang?" → He explains at length. Same result as 1.
3. "Not interested."                 → Capital fallback: he appears at the gates, still holding the knife.
                                       "Big chief. Nok-Nok waited. Now Nok-Nok join."
                                       Accept → build prompt. Decline → gone.
```
`noknok_recruited = TRUE` | `noknok_build = [chosen]`

---

### 🗺️ COMPANION RECRUITMENT — JUBILOST NARTHROPPLE (Ford Across Skunk River, Hex 2,−2)

```
LOCATION : Skunk River Crossing — discoverable during Ch1 or Ch2 exploration
TRIGGER  : Player reaches the hex; cart is wedged in the ford, gnome is furious
```

> *A gnome stands in the middle of a river, water to his waist, screaming at a cart.*
> **Jubilost:** *"Don't just stand there. Either help or leave. I don't have time for spectators."*

```
Resolution options:
  Athletics DC 12   → Muscle the cart free directly
  Engineering Lore DC 10 → Identify the wheel angle; 1-action fix
  Magic solution     → Any spell moving 200+ lbs automatically succeeds
  Failure            → Cart stays stuck; Jubilost angrier; retry or leave

On success:
1. [Say nothing — just help]         → Jubilost: "...Hmm. Competent." Relationship starts Friendly.
                                       Build prompt fires (Alchemist — KM_Builds_Alch_Animist.md).
2. "I want those maps."              → Diplomacy DC 10. Success: he joins and gives 3 hex maps.
                                       Build prompt fires.
3. "You're welcome." [smug]          → He does not thank you. Relationship Neutral. Joins anyway.
                                       Build prompt fires.
```

**Capital Fallback (if hex never reached):**
See `KM_Companions_Behaviors.md` — COMPANION 13 for full scene.

`jubilost_helped = TRUE` | `jubilost_build = [chosen]`

---

> **➡️ Continue in `KM_Ch2_P2.md` — Season of Bloom (Phases 5–8), Tristian's betrayal, Bald Hilltop, chapter resolution, and Ch2 Export.**

---

*KM_Ch2.md — Kingmaker PF2e Text Adventure | Chapter 2 Part 1 v1.0*
*Source: Pathfinder Kingmaker AP (Paizo) + video game (Owlcat) | PF2e rules: 2e.aonprd.com*


---

<!-- merged from KM_Ch2_P2.md (v93.21 file consolidation) -->

# KINGMAKER — CHAPTER 2 PART 2: SEASON OF BLOOM
## KM_Ch2_P2.md | Continuation of: KM_Ch2.md

> **DM:** This file covers Phases 5–8: the Season of Bloom questline, Tristian's betrayal revelation, the Bald Hilltop resolution, chapter end, and the Ch2 Export Block.
> Load alongside: KM_Ch2.md, KM_Exploration.md, KM_Bestiary.md, KM_BuildGuide.md, and all standard files.

---

## 📍 PHASE 5 — SEASON OF BLOOM BEGINS

### The Ancient Curse Triggers

> *The season changes. Something changes with it.*
>
> *Plants along the road are dying — not from frost or drought. Something is eating them from within. Your advisors are worried. Jhod Kavken comes to the throne room with his hands shaking.*
>
> **Jhod:** *"Something is wrong with the land itself. I have felt it for weeks. It began in the north — near the Bald Hilltop. It is spreading."*

**Throne Room Event — Cultist Random Encounter:**
Triggers during overland travel soon after Troll Trouble resolution. A group of cultists attacks — one transforms into an owlbear mid-fight.

```
CULTISTS (×5):
  Cultist Fighter 6 (leader): HP 62 | AC 18 | Longsword d20+10
  Cultist Fighter 3: HP 32 | AC 16 | Longsword d20+7 (dies quickly, replaced)
  Cultist Archer 2: HP 22 | AC 14 | Composite Shortbow d20+6
  Cultist Rogue 2 (×2): HP 18 | AC 15 | Shortsword d20+6 | Sneak Attack +1d6

  OWLBEAR (summoned when Cultist Fighter 3 dies):
  HP: 85 | AC: 18 | Speed: 35 ft
  Beak: d20+11 (1d10+7 P) | Talon ×2: d20+11 (1d8+7 S)
  Grab on Beak hit — target Grabbed

XP: 480 total
NOTE: This encounter repeats periodically until Tristian's quest is resolved.
```

**After the encounter:**
> **Tristian** (if in party): *"I know this cult. I've seen their symbol before. It's connected to... something I need to tell you."*
> He stops himself. He's not ready. But the flag is set: `tristian_confession_imminent = TRUE`

---

### The Bald Hilltop — Part 1

**Quest: An Ancient Curse, Part One**
Located northeast of the capital. A barren hilltop with a dead tree and a stone circle.

> *The grass on the hilltop is black. Not burned — blackened, like something sucked all life from it. The stone circle at the summit pulses faintly with something that is not magic so much as its absence.*

**Encounter:**
```
Wyvern ×2 (guardian creatures, drawn to the corruption):
  HP: 72 each | AC: 19 | Speed: 20 ft, Fly 60 ft
  Jaws: d20+11 (1d10+7 P) | Stinger: d20+11 (1d6+7 P + Poison)
    Wyvern Venom: Fort DC 17, 2d6 poison, Enfeebled 1 on fail
  XP: 240 each = 480 total

After clearing wyverns: examine the stone circle (Arcana or Occultism DC 14)
  Success: "This is a seed point. Something was planted here, magically, years ago.
            It's been growing underground ever since. The hilltop is just where it
            breaks the surface."
  Critical Success: "Whoever planted this had help from within your kingdom.
                     They knew this land intimately."
```

**Reward:** 2,800 gp if enemies cleared before the Ancient Curse Part One deadline.
`bald_hilltop_p1_cleared = TRUE`

---

### Tristian's Confession — Kingdom of the Cleansed

**Trigger:** ~34 days before Ancient Curse Part 2 deadline. Tristian requests a private meeting.

> *He is waiting in the throne room at dawn. He looks like he hasn't slept.*
>
> **Tristian:** *"I have to tell you something. And I need you to hear all of it before you decide what you do with it."*

**The Confession:**

> *"Before I came to your kingdom... I served a goddess. Not Sarenrae. A different being. She called herself the Lantern King's sister. She gave me power I had never felt before. She told me to plant seeds — literal seeds, she said. That they would help the land grow. I believed her. I was young. I was desperate for purpose."*
>
> *"The seeds I planted are the source of the Bloom. The dying plants. The corrupted creatures. I didn't know. But my ignorance doesn't make people less dead."*
>
> *His hands are clasped in his lap. He is not defending himself. He is simply telling you the truth and waiting for whatever comes next.*

**THE CHOICE — Companion Alignment Gate:**

```
FORGIVE: "You were deceived. That matters."
  → tristian_quest = forgiven
  → He remains in party. His powers evolve from genuine redemption.
  → Sarenrae's light grows stronger in him — gains Healer's Blessing improvement.
  → +2 Relationship

CONDEMN: "You planted the seeds. People are dying. I can't trust you."
  → tristian_condemned = TRUE
  → He accepts it. Leaves quietly.
  → Can be re-recruited in Ch4 after a separate encounter (see Companion Notes)
  → Party loses their best healer if no other healer present

INVESTIGATE FIRST: "I need to verify this before I decide."
  → Available if bald_hilltop_p1_cleared = TRUE (player has the seed evidence)
  → Lore (Religion) DC 14: confirms his account is credible
  → Then make the Forgive/Condemn choice with better information
  → No alignment penalty for investigating first
```

`tristian_betrayal_revealed = TRUE` — this flag carries through all chapters.

---

## 📍 PHASE 6 — SEASON OF BLOOM MAIN EVENTS

### Monster Invasion (Scripted Kingdom Event)

> *At dawn, the alarm bells ring.*

Monsters transformed by the Bloom attack the capital. Must be fought in the throne room area — this is not optional.

```
CAPITAL DEFENSE ENCOUNTER:
  Bloom-Touched Owlbear (Leader): HP 95 | AC 20 | Jaws+Talons, Grab
  Bloom-Infected Wolf ×4: HP 28 | AC 15 | Jaws d20+7 (1d8+4)
  Bloom-Touched Bandit (human, partially transformed): HP 38 | AC 16 | Chaos

XP: 640 total
After combat: Linzi scribbles furiously.
  "I'm calling this chapter 'The Bloom.' No — 'The Season of Screams.' 
   Working title."
```

**Kingdom damage:** If player is not in the capital when this triggers — Stability −2, Loyalty −1. If present and fights: no damage, +100 XP for defending.

---

### The Goblin Fort and Womb of Lamashtu

**Investigation path:** The Bloom source is being actively channeled through a Lamashtu cult network. Two key locations:

**Goblin Village (Shrike Hills):**
- Nok-Nok's old tribe is here (triggers his personal quest if recruited)
- Bloom-corrupted goblin elder is the village's problem — not hostile if player is diplomatic
- Diplomacy DC 14: learn about the "mother of monsters" rituals feeding the Bloom
- Kill the elder: goblins scatter. Slightly more Bloom activity short-term.

**Goblin Fort:**
```
GOBLIN FORT — Season of Bloom cultists using goblins as cover
  Enemies: Cultist Leader (Cleric 7 of Lamashtu): HP 74 | AC 20 | Spells: Harm, Spiritual Weapon
           Branded Cultist ×4: HP 42 | AC 17 | Falchion d20+9
           Goblin Shaman ×2: HP 28 | AC 14 | Spells: Produce Flame, Bane
  XP: 860 total
  Loot: Periapt of Wound Closure, Cloak of Resistance +2, 340 gp, Bloom Seed Fragment
        (story item — confirms Tristian's account even if he already confessed)
```

---

### Candlemere Tower — The Curse of Candlemere

**Quest: The Curse of Candlemere.** An ancient ruined tower on the island at the center of Lake
Candlemere — a Bloom-corruption / Old-Cult site the player can investigate during the Season of Bloom.

```
REACHING THE ISLAND:
  Lore (Nature) OR Athletics check to cross to the island (failure = a harder approach, not a block).

CANDLEMERE TOWER:
  Enemies — WILL-O-WISPS (and bloom-touched fey): they hit with ELECTRICITY.
    ⚠️ Resist Energy (electricity) / Protection from Energy makes the wisp fights survivable.
  RISMEL waits on the hill to the NORTHEAST — the quest's key NPC/objective.
  The tower holds Old-Cult lore tying the Bloom's corruption to powers older than Pitax.

XP: tower clear + objective
```

`candlemere_cleared = TRUE`

---

### The Bald Hilltop — Part 2 (Resolution)

**Quest: An Ancient Curse, Part Two**
Return to the Bald Hilltop with the Bloom Seed Fragment and/or Tristian (if still in party).

> *The dead tree at the summit is moving.*
> *Not in wind. Something inside it.*

**Final Encounter:**

```
BLOOM MANIFESTATION (nature horror, not a creature with intelligence):
  HP: 140 | AC: 16 (not armored — it's a plant-creature mass)
  Tendril Slam ×3: d20+10 (2d6+7 B, Reach 15 ft)
  Spore Cloud (Aura 10 ft): Fort DC 16 or Sickened 1 each round inside
  WEAKNESS: Fire damage (double damage). Tristian's positive energy spells (Heal) deal +4d6.
  XP: 720

AFTER COMBAT — Moral Choice:
  Purify the site (requires Religion DC 15 or Tristian present):
    → Bald Hilltop becomes a healing ground (+2 Culture to nearby settlements)
    → tristian_healing = TRUE if he was present
  Abandon it:
    → Site remains dead but inert
  Claim it for kingdom use (dark):
    → Brief Economy boost, permanent Unrest +2 from cursed land influence
```

**Reward for completing Part 2:** 6,500 gp (from kingdom coffers — Linzi and Tristian report it), +900 XP. `bloom_resolved = TRUE`

---

## 📍 PHASE 7 — CHAPTER RESOLUTION

### A Noble's Amusement (Optional but Recommended)

**Triggered:** ~11 days before Ancient Curse Part 2 deadline. Noble invitation to your court.

> *Lady Aldori sends a courier: a group of Rostland nobles wishes to visit your court. "Show them something impressive," she writes. "They are considering backing your kingdom's expansion."*

**Storybook event:** Player must organize entertainment, a feast, and demonstrations for the visiting nobles. Three skill checks:
- Performance or Crafting DC 16 → entertainment quality
- Diplomacy DC 15 → how well the feast is managed  
- Warfare Lore or Society DC 14 → military demonstration

Outcomes:
- 3 successes: +2 Stability, +800 gp, +1 Fame, `noble_patrons = TRUE`
- 2 successes: +1 Stability, +400 gp
- 1 or fewer: no benefit, minor reputation hit

---

### Return to Jamandi

**Triggered after Bloom resolution.** Optional visit to Restov.

> *Jamandi receives you in her private study. Her expression is difficult to read.*
>
> **Jamandi:** *"You've dealt with the trolls. You've survived the Bloom. I'll be honest — I didn't expect this to last the first winter. You've surprised me."*

She provides:
- Kingdom funding: +1,500 gp
- Political intelligence: "Irovetti of Pitax is watching your kingdom. Closely."
- If `nyrissa_letter_found = TRUE`: *"That letter you found. I had it analyzed. The magic on it is old. Older than Pitax. Older than Brevoy. Whatever is interested in your kingdom — it isn't human."*

`jamandi_ch2_meeting = TRUE`

---

## 📊 CHAPTER 2 COMPLETE XP SUMMARY

| Source | XP |
|--------|----|
| Troll Trouble (KM_Ch2.md) | ~5,100 |
| Cultist encounter (×1 at minimum) | 480 |
| Bald Hilltop Part 1 (wyverns + checks) | 600 |
| Tristian investigation/choice | 200 |
| Monster Invasion defense | 640 |
| Goblin Fort | 860 |
| Bald Hilltop Part 2 (Bloom Manifestation) | 720 |
| Lost Child quest | 320 |
| Noble's Amusement (if done) | 300 |
| Side content, exploration | ~600 |
| **Chapter 2 Total** | **~10,180 XP** |

**Level benchmarks:**
- Level 5: 6,000 XP — roughly at Trobold entrance
- Level 6: 10,000 XP — around Hargulka fight
- Level 7: 15,000 XP — mid Season of Bloom
- Level 8: 21,000 XP — after chapter completion

---

## 🔀 CHAPTER 2 KEY RESOLUTION FLAGS

| Decision | Options | Ch3+ Impact |
|----------|---------|-------------|
| Hargulka fate | `killed` / `vassal` | Vassal → Ekundayo leaves |
| Tartuk/Tartuccio fate | `fled` / `vassal` / `defeated` | All lead to Ch3 appearance |
| Tristian decision | `forgiven` / `condemned` | Condemned → absent Ch3-4 unless re-recruited |
| Bloom resolution | `purified` / `abandoned` / `claimed` | Affects kingdom stats Ch3+ |
| Ekundayo status | `recruited` / `left_hargulka` / `never_recruited` | Ch7 survival requires quest |
| Noble visit | `done` / `skipped` | Patron support affects Ch5 war resources |

---

> **⛔ HARD STOP — Chapter 2 ends when BOTH Troll Trouble AND Season of Bloom are resolved (`bloom_resolved = TRUE` AND `hargulka_fate` is set). Before any Chapter 3 content — before Varnhold messenger, before any new scene — output the export block below. Say: *"Chapter 2 is complete. Copy the block below and save it. Type `.continue` when saved."* Wait for confirmation. VIOLATION = `.fail 16`.**

---

## 💾 CHAPTER 2 → CHAPTER 3 EXPORT

````json
{
  "save_version": "1.0",
  "export_from": "chapter_2",
  "import_to": "chapter_3",
  "export_date_ingame": "",

  "player": {
    "name": "", "build_id": "", "class": "", "level": 0, "xp": 0,
    "attributes": {}, "hp_current": 0, "hp_max": 0, "hero_points": 1,
    "ac": 0, "saves": {}, "conditions": [], "skills": {},
    "feats": [], "spells": {}, "class_features": [],
    "inventory": { "weapons": [], "armor": [], "shields": [],
                   "magic_items": [], "consumables": [], "gear": [], "quest_items": [] },
    "gold": { "gp": 0, "sp": 0, "cp": 0 }
  },

  "companions": [
    { "name": "Amiri", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Friendly", "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "", "status": "active_party", "level": 0,
      "hp_current": 0, "hp_max": 0, "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "Ekundayo", "status": "active_party_OR_left",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral", "notes": "", "thread": "", "priorities": [] },
    { "name": "Tristian", "status": "active_party_OR_condemned",
      "level": 0, "hp_current": 0, "hp_max": 0,
      "relationship": "Neutral",
      "notes": "If condemned: tristian_condemned = TRUE, not in party" }
  ],

  "kingdom": {
    "name": "", "capital_location": "", "turn": 0, "size": 0,
    "culture": 0, "economy": 0, "loyalty": 0, "stability": 0,
    "unrest": 0, "fame": 0, "infamy": 0, "treasury_rp": 0,
    "leadership_roles": {}, "settlements": [], "armies": [],
    "claimed_hexes": [], "roads": []
  },

  "story_flags": {
    "carried_from_ch1": {
      "stag_lord_fate": "", "nyrissa_letter_found": false,
      "nyrissa_early_contact": false, "akiros_fate": "",
      "tartuccio_journal_found": false, "alignment_track": {},
      "bokken_relationship": "neutral",
      "tiressia_met": false,
      "nettles_crossing_resolved": false,
      "old_beldame_met": false,
      "jubilost_helped": false,
      "sootscale_alliance": false,
      "svetlana_ring_returned": false,
      "oleg_expanded": false
    },
    "chapter_2": {
      "hargulka_fate": "",
      "jazon_escort": false,
      "jazon_spared": false,
      "tartuk_ch2_fate": "",
      "tartuccio_ch2_confronted": true,
      "ekundayo_recruited": false,
      "ekundayo_quest": "",
      "kargadd_killed": false,
      "harrim_statue_check": false,
      "tristian_betrayal_revealed": true,
      "tristian_decision": "",
      "tristian_healing": false,
      "bloom_resolved": true,
      "bald_hilltop_resolution": "",
      "verdant_chambers_visited": false,
      "bartholomew_met": false,
      "troll_weakness_known": false,
      "stefano_survived": false,
      "noble_patrons": false,
      "jamandi_ch2_meeting": false,
      "noknok_quest_triggered": false,
      "linzi_quest_triggered": false,
      "side_quests": {
        "lost_child": false,
        "cog_wheel_rings": false,
        "bokken_brother": false,
        "nature_of_beast": false
      }
    },
    "tartuccio": {
      "tartuccio_ch2_fate": "fled_to_varnhold_region",
      "tartuccio_journal_ch2": false,
      "tartuccio_knows_player_is_aware": false
    },
    "nyrissa": {
      "nyrissa_awareness": "passive_OR_active",
      "nyrissa_bloom_connection_known": false,
      "nyrissa_identity_known": false
    },
    "alignment_track": {
      "lawful_chaotic_axis": "neutral",
      "good_evil_axis": "neutral",
      "notable_choices": []
    },
    "relationships": {
      "jamandi": "neutral", "kassil": "neutral",
      "kesten": "neutral", "oleg": "neutral",
      "ekundayo": "neutral", "bartholomew": "neutral",
      "tiressia": "neutral", "hargulka": "dead_OR_vassal"
    },

    "npc_threads": {
      "Amiri":     { "thread": "She asked about the bread roll. He said a disarmed soldier is useless. She's been sitting with the word *disarmed* ever since.", "priorities": [
        { "weight": 55, "instruction": "Disarmament question active — Stage 1. Think/test alone in quiet moments. Stage 2 = first actual disarm: one beat pause, then reach for nearest object. Stage 3 = occasional first choice even when sword is available. Never skip the beat. Track stage toward amiri_disarm_resolved.", "source": "road south — eRmaC told her a disarmed soldier is useless" }
      ] },
      "Linzi":     { "thread": "", "priorities": [] },
      "Valerie":   { "thread": "", "priorities": [] },
      "Harrim":    { "thread": "", "priorities": [] },
      "Jaethal":   { "thread": "", "priorities": [] },
      "Tristian":  { "thread": "", "priorities": [] },
      "Ekundayo":  { "thread": "", "priorities": [] },
      "Kesten":    { "thread": "", "priorities": [] },
      "Jamandi":   { "thread": "", "priorities": [] },
      "Oleg":      { "thread": "", "priorities": [] },
      "Nok-Nok":   { "thread": "", "priorities": [] },
      "Octavia":   { "thread": "", "priorities": [] },
      "Regongar":  { "thread": "", "priorities": [] }
    },

    "world_state": {
      "troll_trouble_resolved": true,
      "season_of_bloom_resolved": true,
      "pitax_watching": true,
      "varnhold_silent": false,
      "nyrissa_next_move": "varnhold_vanishing",
      "public_reputation": 0,
      "reputation_tier": "UNKNOWN",
      "reputation_deeds": [],
      "reputation_notes": ""
    }
  },

  "quest_log": {
    "completed": [
      { "name": "Troll Trouble", "result": "", "xp": 0 },
      { "name": "Season of Bloom / Ancient Curse", "result": "", "xp": 0 }
    ],
    "active": [
      { "name": "The Varnhold Vanishing",
        "objective": "Varnhold has gone silent. Investigate.",
        "notes": "Chapter 3 begins with a messenger arriving with no news from Varnhold." }
    ]
  }
}
````

---

## 📥 HOW TO LOAD CHAPTER 3

**Paste at start of Chapter 3 chat:**
```
Loading Chapter 3 of Pathfinder 2e Kingmaker.

Files to load:
KM.txt, KM_Builds.md, KM_Actions.md, KM_Commands.md, KM_Commands_Maps.md,
KM_Commands.md, KM_Companions.md, KM_Companions.md,
KM_Map.md, KM_Kingdom.md, KM_Ch3.md

[PASTE CH2 JSON EXPORT HERE]
```

---

*KM_Ch2_P2.md — Kingmaker PF2e Text Adventure | Chapter 2 Part 2 v1.0*


---

---

## CHAPTERS 3–7 + LINZI SHRINE — MOVED (v95.9)
> Chapter 3 (Varnhold Vanishing), Chapters 4–7 (Warlord, War of the River Kings, Sound of a Thousand Screams, Final Act), and the Shrine of Returning were split to **the per-chapter files KM_Ch3.md-KM_Ch7.md (folders Ch3/-Ch7/)** for file-size compliance. Load that file from Chapter 3 onward.
