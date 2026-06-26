# KINGMAKER — CHAPTER 2: TROLL TROUBLE & SEASON OF BLOOM
## KM_Ch2.md | Loads after: KM_Ch1_Export.md | Loads before: KM_Ch3.md

---

> **DM:** Load with KM.txt, KM_Companions.md, KM_Companions_B.md, KM_Commands.md, KM_Commands_Maps.md, KM_Actions.md, KM_Map.md, KM_Kingdom.md, KM_Exploration.md, KM_Bestiary.md, KM_Leveling.md.
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
1. "We'll find Kargadd together."  → He joins. Build prompt fires (Ranger — KM_Builds_I.md).
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
1. "Prove it. Come with us."         → He joins. Build prompt fires (Rogue — KM_Builds_J.md).
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
                                       Build prompt fires (Alchemist — KM_Builds_A.md).
2. "I want those maps."              → Diplomacy DC 10. Success: he joins and gives 3 hex maps.
                                       Build prompt fires.
3. "You're welcome." [smug]          → He does not thank you. Relationship Neutral. Joins anyway.
                                       Build prompt fires.
```

**Capital Fallback (if hex never reached):**
See `KM_Companions_Leveling.md` — COMPANION 13 for full scene.

`jubilost_helped = TRUE` | `jubilost_build = [chosen]`

---

> **➡️ Continue in `KM_Ch2_P2.md` — Season of Bloom (Phases 5–8), Tristian's betrayal, Bald Hilltop, chapter resolution, and Ch2 Export.**

---

*KM_Ch2.md — Kingmaker PF2e Text Adventure | Chapter 2 Part 1 v1.0*
*Source: Pathfinder Kingmaker AP (Paizo) + video game (Owlcat) | PF2e rules: 2e.aonprd.com*
