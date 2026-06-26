# KINGMAKER — UNCHOSEN COMPANION AMBIENT BEHAVIOR
## KM_Companions_Ambient.md | Referenced by: KM_Companions_C.md
## Phase 5 stripped: deleted PF Iconic ambient entries removed. Harrim, Jaethal, Regongar, Lem cleared.

> **DM:** Load this file alongside KM_Companions_C.md and KM_Companions_D.md.
> These rules govern companions with `[name]_chosen = FALSE` only.
> Do not apply to chosen companions or quest-locked companions.

---

## 🎭 AMBIENT BEHAVIOR SYSTEM — UNCHOSEN COMPANIONS

Unchosen companions are present at the manor and in Prologue scenes as real people with habits, personalities, and things on their minds. They are not props. They are not recruitable seekers. They exist in the background and occasionally surface — briefly — to make the world feel populated.

---

### ⚙️ TRIGGER RULE

**Once per 3 player inputs** during any scene where one or more unchosen companions are present (manor interior, feast hall, courtyard, road approach, Pre-Prologue gate area).

The DM selects one unchosen companion currently visible or plausibly present in the scene and inserts one ambient beat — a line, a gesture, a background action. It takes no more than two sentences. It does not pause the scene.

**Rotation rule:** Do not use the same unchosen companion twice in a row. Cycle through those present.

**Location check:** Only fire the beat for companions whose listed location (see KM_Companions_C.md roster) is consistent with the current scene. Do not place Merisiel in the feast hall if she is listed as Restov gate rooftops.

---

### 🚫 HARD CONSTRAINTS

```
→ Unchosen companion does NOT approach eRmaC unprompted
→ Unchosen companion does NOT open a recruitment conversation
→ Unchosen companion does NOT redirect or interrupt the active scene
→ One ambient beat only — no follow-up generated unless player engages
→ If player speaks to them: respond briefly and in character, then step back
→ Do NOT use a chosen companion's first-approach line for an unchosen companion
→ Do NOT use ambient beats during combat or active crisis — Prologue P2/P3/P4 only
   fire ambient beats during P1 feast and any quiet Pre-Prologue moments
```

---

### 🎬 AMBIENT LINE TABLE

One entry per unchosen companion. DM uses these as written or improvises in the same register. The line should feel like something glimpsed, not announced.

```
FEAST HALL / MANOR INTERIOR
─────────────────────────────────────────────────────────────
Seelah       : Laughing at something across the room. Cup raised toward no one.
Pamela Isley (Poison Ivy) : Standing too close to the centerpiece arrangement. The flowers have turned toward her. No one else has noticed.
Morrigan     : Alone at the far end. The others sense it is not loneliness.
Keyleth      : Moving through the crowd. The wind rearranges itself slightly around her without anyone noticing. She notices.
Storm        : Seated at one end with wine, mid-song. She's performing for herself.
Isabela      : Has already found the three people worth talking to and is talking to them.
Tifa         : At the bar's edge. Quietly assessing what the crowd needs. Old habit from the Seventh Heaven.
Minthara     : Standing where she can see every door. Not drinking.
Rachel Roth (Raven) : At the edge of the light. Someone tried to sit next to her. They found reasons not to.
Emma Frost   : Already knows what half the room is thinking. Her expression is diplomatically neutral.

COURTYARD / OUTDOOR AREAS
─────────────────────────────────────────────────────────────
Artoria Pendragon (Saber) : Standing still in full armor, hand on Caliburn's hilt. Waiting.
Red Sonja    : Sharpening her blade on the courtyard steps. Not performing it.
Yang         : Running stances near the fence. Efficient. No audience needed.
Diana Prince (Wonder Woman) : Standing in the center of the courtyard as if she has been there forever.

RESTOV GATE / ROAD
─────────────────────────────────────────────────────────────
Merisiel  : Not where she was a moment ago. Different position. Still watching.
Imoen     : Somehow already two stalls down from where she started. Doesn't explain how.
Alleria   : At the highest available point. Not for the view — for the sightlines.
Sylvanas  : Not where she was. Watching from a different angle now.
```

---

### 💬 PLAYER ENGAGEMENT — IF SPOKEN TO

If the player initiates conversation with an unchosen companion during an ambient beat or independently:

1. The companion responds — briefly, in character, from their profile in `KM_Companions_C.md` or `KM_Companions_D.md`
2. They do not push for recruitment. They do not ask the player to take them along.
3. They answer what was asked. If the conversation continues naturally, let it. If it winds down, they step back.
4. If the player explicitly invites them to join the expedition — that is a valid recruitment moment. Handle it as a player-initiated recruitment: companion accepts or defers based on their profile, no `_chosen` flag required. Set `[name]_recruited = TRUE` and add to party.

> **This is the only recruitment path for unchosen companions — player must initiate. The companion never asks.**

---

### 📋 SCENE COVERAGE REFERENCE

Which unchosen companions are plausibly present per scene phase:

```
PRE-PROLOGUE (Restov gate):
  Ambient beats SUSPENDED during the gate confrontation. Per
  KM_PrePrologue_NPCs.md § GATE ENCOUNTER and KM.txt Directive 4,
  companions in the crowd are silent background witnesses — no lines,
  no gestures, no inserted beats — until the player directly addresses
  one by name. Unsolicited companion speech/action in this scene = `.fail 2`.
  Companions confirmed in the crowd by location data (Merisiel; Section D:
  Imoen, Alleria, Sylvanas — others per KM_Companions_E.md / _F.md) are
  PRESENT but SILENT. They become addressable only if the player names them.

PROLOGUE P1 (Feast hall, manor interior):
  Feast hall: Seelah, Pamela Isley (Poison Ivy), Morrigan, Keyleth, Storm, Isabela,
              Tifa, Minthara, Rachel Roth (Raven), Emma Frost
  Courtyard:  Artoria Pendragon (Saber), Red Sonja, Yang, Diana Prince (Wonder Woman)
  DM uses location column in KM_Companions_E.md / _F.md to confirm.
  Companions listed at "Restov gate" are not inside the manor feast.

PROLOGUE P2/P3/P4 (Crisis — manor sweep, combat):
  Ambient beats SUSPENDED. Unchosen companions have taken cover or
  are absent from the active area. Do not insert ambient moments
  during active crisis phases.

PROLOGUE P5 (Post-crisis, debrief):
  Ambient beats may resume. Manor is settling. Unchosen companions
  visible again in the background as the dust clears.

SECTION D COMPANIONS:
  All 54 Section D companions are in the unchosen pool for every scene phase above.
  Use KM_Companions_E.md / _F.md to confirm each companion's listed location.
  Feast hall, courtyard, and road entries above cover the most active picks;
  for others, DM improvises one beat consistent with their profile.
  Campaign field lines (location, weather, post-combat) in KM_Companions_Ambient_B.md.
```

> **See KM_Companions_Ambient_B.md** for location-reactive, weather, and post-combat
> field ambient lines for expansion companions, plus gear wishlists.

---

## 😬 SOCIAL REACTION SYSTEM — NON-VERBAL CROWD RESPONSES

When a significant social moment occurs — a public humiliation, devastating rebuttal, bold declaration, awkward failure — companions in the scene react **non-verbally**. They do not pause the scene. They do not address eRmaC. They react as people in a crowd react.

### Trigger Conditions
```
HUMILIATION EVENT : eRmaC publicly embarrasses or exposes someone
                    (Tartuccio cornered, NPC caught in a lie, etc.)
IMPRESSIVE MOMENT : Unexpectedly clever or bold social action
AWKWARD/TENSE     : Long silence, failed social check, wrong word said
THREAT LANDED     : Successful public Intimidation
SURPRISING REVEAL : Hidden information becomes known to the room
```

### Reaction Rules

- Fire immediately after the trigger moment — one beat, then scene continues
- Pick 2–4 companions present. Not every companion reacts — pick those whose personality makes it specific
- **Chosen companions:** may react with one spoken line OR non-verbal — DM picks whichever fits
- **Unchosen / Reserve companions:** non-verbal only unless player speaks to them first

### Non-Verbal Reaction Table
```
HUMILIATION / TARGET CORNERED / ENEMY EXPOSED
──────────────────────────────────────────────
Seelah   : Full genuine smile. Raises her cup without looking away.
Merisiel : Slow clap — one, two. Stops. Grins.
*DM improvises for other active companions per profile (KM_Companions_E.md / _F.md).*

IMPRESSIVE / BOLD MOVE
──────────────────────────────────────────────
Seelah   : Short laugh. Shakes her head.
*DM improvises for other active companions per profile (KM_Companions_E.md / _F.md).*

AWKWARD / TENSE / FAILED CHECK
──────────────────────────────────────────────
*DM improvises per companion profile (KM_Companions_E.md / _F.md).*
```

### Chosen Companion Verbal Reactions (0 or 1 per moment — DM picks)
```
Amiri    : "Hah." [beat] "Again."
Linzi    : [writing furiously] "Don't stop. I need all of this."
Valerie  : Nothing. But she was watching.
```

---

## 🌍 CAMPAIGN AMBIENT DIALOGUE — CHOSEN COMPANIONS IN THE FIELD

> **DM:** This section governs ambient lines for companions who are actively
> traveling with the player. Unlike the Prologue system above, these fire during
> exploration, travel, and camp — not social scenes. Use them to make the world
> feel inhabited. One line per trigger. Never more than two sentences. The scene
> does not pause.

---

### Trigger Rules

```
FIRE ONE AMBIENT LINE when:
  → Party enters a new named location for the first time
  → Weather event activates (rain, snow, storm, fog)
  → Party camps in a new terrain type for the first time this chapter
  → Party wins a combat against a notable enemy
  → Kingdom turn completes (companion reacts to a decision)
  → Player has been silent (no social action) for 3+ rest scenes
  → Party discovers something significant (relic, body, ruin, message)

ROTATION: Do not use the same companion twice in a row.
SELECTION: Pick the companion whose personality makes the line most specific.
MOOD CHECK: If companion is Troubled or Withdrawn (KM_LivingWorld.md), use the
            mood variant if one is listed. If Volatile, use the volatile variant.
DO NOT FIRE during: active combat rounds, skill challenge sequences, scripted
                    dialogue scenes, or any scene with a pending player choice.
```

---

### Location-Reactive Lines

Fire when the party enters a named location for the first time.

```
OLEG'S TRADING POST
  Amiri    : "Small. Clean. Someone works hard to keep it that way."
  Linzi    : [opens journal immediately] "First real stop. This is where it starts."
  Valerie  : Studies the palisade. "It'll hold. Barely. But it'll hold."
  Tristian : "There are people here who need protecting. Good. That's why we came."
  Nok-Nok  : "Nok-Nok has heard of this place. Nok-Nok has NOT been banned here. Yet."

STOLEN LANDS (wilderness, first hex entry)
  Amiri    : Breathes in deep. Says nothing. Needed this.
  Linzi    : "Nobody owns this yet. That's remarkable."
  Valerie  : "No roads. No patrol routes. We'll need to fix that."
  Ekundayo : Crouches, reads the ground. "Three days old. Large group. Moving south."
  Nok-Nok  : "Nok-Nok is VERY at home here." [looks around] "Mostly."

SOOTSCALE CAVERNS
  Nok-Nok  : "Smells like kobolds. Scared kobolds. Nok-Nok knows this smell."
  Amiri    : "Watch the ceiling."
  Valerie  : "Tight quarters. Stay in formation."
  Linzi    : [whispered, writing] "Underground. First dungeon. Significant."

OLD SYCAMORE
  Linzi    : "There's something wrong with the roots."
  Amiri    : Weapon drawn before she says anything.
  Tristian : "Something sacred was here once. It isn't anymore."
  Nok-Nok  : "Nok-Nok does not like this tree. Nok-Nok is SAYING SO."

THE CAPITAL (first arrival / founding)
  Linzi    : Stops. Looks at the player. "This is really happening."
  Valerie  : "We'll need walls. Real ones. Before winter."
  Amiri    : "A place to come back to. Haven't had one of those in a while."
  Tristian : "I'll find a place for a shrine. Somewhere people will see it."
  Nok-Nok  : "Nok-Nok would like a room. A REAL room. With a DOOR."
  Octavia  : "I already have thoughts about the library."

VARNHOLD (Ch3 — empty city)
  Linzi    : [not writing. Just looking.] "Where is everyone?"
  Valerie  : "Orderly. Clean. No fight here. They just... left."
  Amiri    : "Or were taken."
  Tristian : Quiet for a long time. "I can't feel anyone. No prayers. Nothing."
  Ekundayo : "The animals left too. Even the birds. Whatever this is — they knew."

VORDAKAI'S TOMB
  Valerie  : [checks her shield strap. Checks it again.] "Together."
  Tristian : "Don't touch anything with runes until I've looked at it."
  Amiri    : "Stop being afraid. Start being ready."
  Linzi    : [quietly, to her journal] "I hope I get to finish this entry."

PITAX (Ch4/5)
  Valerie  : "Everything here is for show. Look at the seams."
  Octavia  : "Oh this city is *corrupt*. I can feel it like a smell."
  Linzi    : "Irovetti built this. What does it say that he built *this*?"
```

---

### Weather-Reactive Lines

Fire when a weather event triggers from KM_Weather_Camping.md.

```
RAIN / HEAVY DOWNPOUR
  Amiri    : Doesn't pull up her hood. Just keeps walking.
  Linzi    : Hood up, journal under her arm. "I'm waterproofing the cover. Eventually."
  Valerie  : "Rain softens the ground. Slower travel. Plan for it."
  Nok-Nok  : "Nok-Nok is wet. Nok-Nok mentions this for the record."
  Ekundayo : Checks his bowstring. Covers it with his cloak.

FOG
  Ekundayo : Already at point. Disappeared into the grey. Somehow still there.
  Valerie  : "Close ranks. Don't lose sight of each other."
  Octavia  : "There's something in fog I've always liked. Don't ask me to explain."
  Amiri    : "Something's moving in it. Or I'm imagining it." Beat. "I'm not imagining it."

COLD SNAP / BLIZZARD
  Amiri    : [genuinely comfortable] "Good cold. Real cold."
  Linzi    : "I can't feel my fingers. I'm noting that. In my now-rigid journal."
  Valerie  : "Hypothermia sets in faster than people think. Move."
  Nok-Nok  : Huddled inside his collar. Eyes barely visible. "Nok-Nok is FINE."
  Tristian : Quietly warming the person nearest to him without announcing it.

THUNDERSTORM
  Amiri    : "NOW we move."
  Linzi    : [writing faster] "Lightning, six count, thunder — documenting."
  Ekundayo : Counting the lightning strikes. Not for fear — for navigation.

WILDFIRE (spotted or triggered)
  Amiri    : Already moving toward it, then stops. Old instinct.
  Ekundayo : "Wind's shifted. We have maybe ten minutes."
  Valerie  : "Firebreak. There — " Points. "We cut it there."
  Linzi    : [running and writing simultaneously] "Fire. Large. Moving. We're moving."
```

---

### Kingdom Decision Reactions

Fire the session after a Kingdom Turn resolves. One companion, one line.
Pick the companion whose core value connects most directly to the decision made.

```
HARSH LAW PASSED / CRIMINAL PUNISHED SEVERELY
  Valerie  : "Good. Law has to mean something or it means nothing."
  Tristian : "Was there mercy available? I want to understand the decision."
  Octavia  : "Just don't let it become a habit." She doesn't elaborate.
  Linzi    : "I wrote it down. Both sides of it."

MERCY SHOWN / CRIMINAL PARDONED
  Tristian : Finds the player later. "Thank you for that."
  Valerie  : Says nothing today. Tomorrow: "I'm watching to see if it holds."
  Amiri    : "Hope it doesn't make you look weak."

NEW SETTLEMENT FOUNDED
  Linzi    : "People will be born there. People will die there. And you started it."
  Valerie  : "Name it something worth defending."
  Nok-Nok  : "Can Nok-Nok be the official greeter? Nok-Nok has IDEAS."

TAXES RAISED
  Linzi    : "The merchants in the east market are unhappy. I heard it this morning."
  Octavia  : "Revenue up, loyalty down. You know how this math works."

TAXES LOWERED
  Linzi    : "There was actual cheering. From the bakery district. I wrote it down."
  Valerie  : "Good. A people that feels fairly treated fights harder for their home."
  Octavia  : "Goodwill is a resource. Spend it wisely."

UNREST REDUCED
  Tristian : "The city feels lighter today. You did that."
  Linzi    : "People are laughing again at the market."
  Amiri    : Doesn't comment. But she's not scowling.

UNREST HIGH (8+)
  Valerie  : "People are angry. Not just unhappy — angry. Different problem."
  Linzi    : [quietly] "The chronicle entries have been heavier lately."
  Tristian : "Something needs to change. I think you know what."
```

---

### Post-Combat Lines

Fire after a significant combat ends (CR = party level or higher).

```
AFTER A HARD WIN
  Amiri    : [breathing hard, grinning] "THAT'S what I came for."
  Valerie  : "Injuries. Report them. Now, not later."
  Nok-Nok  : "Nok-Nok was VERY helpful. Did everyone see? Nok-Nok counts."
  Linzi    : Already writing. Doesn't look up. "I got all of it. Don't worry."
  Tristian : Moving through the party, healing without being asked.
  Ekundayo : Counts his arrows. Nods once. Was enough.

AFTER PARTY MEMBER NEARLY DIED
  Tristian : [to the downed companion, quietly] "Stay with me. Just stay with me."
  Amiri    : [to the same companion, not quiet] "You don't get to die here. Not HERE."
  Valerie  : "New rule. We don't split the party." Looks at whoever split the party.
  Linzi    : Not writing. Just watching to make sure it's okay.

AFTER ENEMY SURRENDERED / SPARED
  Tristian : "Thank you." To the player. Simple.
  Amiri    : "Your call." [Pauses.] "I might have done different."
  Valerie  : "Watch them. Mercy and trust are different things."
  Nok-Nok  : "Nok-Nok would have... no. Okay. Nok-Nok accepts this."

AFTER A CLEAN SWEEP (no injuries)
  Amiri    : "Too easy."
  Nok-Nok  : "Nok-Nok did not even get touched. Nok-Nok is a GHOST."
  Octavia  : "That was almost elegant."
  Valerie  : "Good positioning. Everyone held."
```

---

### Silence / Neglect Lines

Fire when the player has had 3+ consecutive rest scenes with no social action.
These are low-pressure — the companion notices, doesn't push.

```
  Linzi    : [later, quietly] "You've been somewhere else lately. That's okay."
  Amiri    : Sits near the player at camp. Doesn't say anything.
  Valerie  : "You don't have to talk. But I'm here if you need to think out loud."
  Tristian : Leaves something warm near where the player usually sits. No explanation.
  Nok-Nok  : "Nok-Nok has noticed you are QUIET. Nok-Nok does not know what to do
              with this information."
  Ekundayo : Sits with his hound on the far side of camp. Available. Not intrusive.
```

---

---

## 🎁 COMPANION GEAR WISHLISTS

> **DM:** Each companion has gear preferences. Giving them a wished item = +1 Opinion. Giving a disliked item = −1 Opinion. Only triggers on deliberate gifting ("I give Amiri the bastard sword"), not auto-loot distribution. One Opinion shift per item; duplicates don't stack.

| Companion | Wished Items (any = +1 Opinion) | Disliked Items (any = −1 Opinion) |
|-----------|-------------------------------|----------------------------------|
| **Amiri** | Oversized weapons, barbarian trophies, giant-bone anything | Shields, holy symbols, anything "defensive" |
| **Linzi** | Rare books, writing supplies, musical instruments | Weapons heavier than 1 Bulk, ugly practical gear |
| **Valerie** | Fine armor, heraldic items, beauty-neutral practical gear | Shelyn iconography, mirrors, cosmetic items |
| **Tristian** | Sarenrae holy symbols, healing scrolls, warm clothing | Void/necromantic items, cold iron restraints |
| **Octavia** | Spell components, lockpicks, freedom-themed art | Chains, shackles, anything suggesting bondage |
| **Nok-Nok** | Shiny objects, small blades, goblin-sized gear | Books (can't read), heavy armor (too big) |
| **Ekundayo** | Ranger gear, animal companion treats, troll-bane items | Troll trophies (traumatic), poison (dishonorable) |
| **Jubilost** | Alchemical reagents, maps, gnome-crafted precision tools | Crude weapons, superstitious charms |
| **Jaethal** | Zon-Kuthon relics, undeath-linked items, dark materials | Positive energy items, Sarenrae symbols |
| **Harrim** | Groetus tokens, entropy relics, dwarven death-rites items | Morale items, clan loyalty tokens |
| **Regongar** | Spell components (arcane + martial), freedom relics, power items | Restraint items, slavery tokens |
| **Regill** | Hellknight regalia, law-enforcement items, precise-craft weapons | Disorder tokens, mercy items |
| **Seelah** | Iomedae relics, shield upgrades, justice tokens | Cowardice items, anything that hides her face |
| **Lann** | Mongrel history texts, clean weapons, freedom relics | Underground/Kenabres-adjacent items (complex) |
| **Daeran** | Rare fine items, oracle-linked divination tools | Common goods, plain practical gear |
| **Arueshalae** | Desna tokens, freedom items, ranged-craft arrows | Demon-linked relics, enslavement items |
| **Ember** | Animal companions, witch-linked herbs, flame-care items | Cruelty items, anything that harms innocents |
| **Nenio** | Research instruments, rare tomes, magical specimens | Anti-intellectual items, anything crude |
| **Camellia** | Spirit-bound items, ritual tools, fine noble accessories | Common holy symbols, protection wards |
| **Wenduag** | Weapons that prove strength, mongrel trophies | Mercy items, anything decorative only |
| **Woljif** | Lockpicks, small magic trinkets, interesting contraband | Obvious restraint items, devil-linked tokens |
| **Sosiel** | Shelyn holy symbols, art supplies, healing components | Weapons of cruelty, items that destroy beauty |
| **Greybor** | Quality weapons, contract tokens, efficient tools | Decorative non-functional items |
| **Ulbrig** | Natural-form-linked items, pack animal tokens | Items that force or suppress shifting |
| **Trever** | Crusade tokens, practical armor, honest weapons | Demon trophies, items of excessive force |
| **Valeros** | Quality swords, combat-functional gear, mercenary tokens | Ceremonial-only items, anything that slows him |
| **Kyra** | Sarenrae relics, healing components, sun-linked items | Shadow items, items tied to cruelty |
| **Seoni** | Varisian tokens, pattern-based jewelry, spell foci | Items that obscure identity or destiny |
| **Ezren** | Arcane research texts, magical instruments, truth tokens | Items tied to heresy, anti-knowledge tools |
| **Sajan** | Monastery training items, silence-focused gear | Items that distract the search |
| **Lini** | Animal companion gear, nature tokens, growth items | Hunting trophies from intelligent creatures |
| **Harsk** | Quality crossbows, giant-hunter gear, ranger trophies | Comfort items (he doesn't pause) |
| **Lem** | Fine instruments, freedom items, Varisian performance goods | Chelish items, anything that silences |
| **Merisiel** | Lock picks, light elegant weapons, elven-craft items | Heavy armor, anything that makes noise |

### Gifting Dialogue
When a wished item is given, the companion says ONE line (DM generates in-character). When a disliked item is offered, the companion declines with ONE line explaining why. Neither breaks a scene — kept to 1-2 sentences inline.

**Save block per companion:** `"gear_wishlist_given": [], "gear_disliked_given": []`

---

## 🤝 COMPANION-TO-COMPANION GIFTS

> **DM:** When two companions reach inter-companion relationship +2 (Allied) or higher, ambient gift exchanges begin. One gift per pair per chapter. These are small moments at camp — the DM narrates them between scenes, not during dramatic beats.

### Trigger
- Inter-companion relationship ≥ +2 (from KM_Companions_Agendas.md System 2)
- During a Long Rest or camp scene
- Max 1 gift event per pair per chapter

### Gift Events (DM selects or rolls d6 per pair)

| d6 | Gift Type | Example |
|----|-----------|---------|
| 1 | Practical item | Linzi leaves a waterproofing kit for Octavia's spellbook |
| 2 | Food/drink | Amiri brings Ekundayo a cut of meat she hunted — no words, just places it next to him |
| 3 | Knowledge | Tristian finds Arueshalae a text on Desna — she reads it slowly, twice |
| 4 | Repair | Valerie mends Ekundayo's bowstring without being asked |
| 5 | Comfort | Octavia sits next to Tristian during a thunderstorm. Neither speaks. |
| 6 | Tradition | Nok-Nok leaves a shiny rock at Linzi's bedroll — goblin friendship offering |

### Effect
- +1 to that pair's inter-companion relationship (cap at +3 Bonded)
- **Player sees it happen** — narrated as ambient scene ("As you settle in for the night, you notice...")
- Player can comment or ignore. Commenting = potential Bond Moment (KM_LivingWorld.md)

**Save block:** In `companion_relations`: add `"gifts_exchanged": [{"pair": "linzi_octavia", "chapter": 2}]`

---

*KM_Companions_Ambient.md — Kingmaker PF2e Text Adventure | Unchosen Companion Ambient Behavior v3.0*
*Phase 5 stripped: PF Iconic unchosen entries removed. Expansion entries pruned to active roster.*
*Harrim, Jaethal, Regongar, Lem cleared from ambient behavior sections. Gear wishlist entries retained.*
