# KINGMAKER — TITLE REWARDS: PASSIVES & REGALIA ITEMS
## KM_Companions_Titles.md | Referenced by: KM_Companions.md § TITLE SYSTEM
## PAIR-LOAD WITH KM_Companions_Titles_B.md (5 class-apex companions)

> **DM:** This file defines the full passive skill (Prefix reward) and 5-star regalia item (Suffix reward) for each ACTIVE party companion. Roster reflects the current 11-companion lineup (eRmaC's party). Load alongside KM_Companions.md AND KM_Companions_Titles_B.md (sidecar covering 5 class-apex companions: Senua #4, Yang #46, Weiss #49, Alleria #64, Imoen #69). For any companion outside both files (recruited later via Pick-10/Seekers/quests), use the patterns here to generate equivalents at grant time.

---

## ⛔ SYSTEM OVERVIEW

**When the player grants a Suffix title, a 5-star item materializes.** Not bought, not crafted, not looted — it appears on them, equipped or in hand, as if it had always been theirs.

**When the player grants a Prefix title, a passive activates.** The companion physically feels it — a warmth, a weight, a sudden clarity. They react.

**Both scale with Reaction Score** (how well the title fits — DM assigns −5 to +5).

---

## 📊 REACTION SCORE SCALING

| Reaction | Passive | Item | Companion Reaction |
|---|---|---|---|
| **+5** | Full power | Full power | Transformative moment. Relationship +2. |
| **+3/+4** | 75% effect | Full power | Deep gratitude. Relationship +1. |
| **+1/+2** | 50% effect | 75% power | Honored. Warm thanks. |
| **0** | No passive | 50% power | Polite acceptance. |
| **−1/−2** | No passive | 25% (mundane) | Wears it out of loyalty. Relationship −1. |
| **−3/−4** | No passive | Refused — dissolves | Cannot accept. Says why. Relationship −1. |
| **−5** | −1 penalty | Refused | Insult. Relationship −2. Title revoked. |

---

## ✨ MATERIALIZATION RULES

**Suffix granted (reaction 0+):**
Item materializes ON the companion — equipped or in hand. One heartbeat it isn't there, the next it is. 5-star = legendary tier, named, never dulls or breaks.

**Prefix granted (reaction +1+):**
Passive activates inside them. Felt physically. They test it with one small demonstration. They speak to the player in character — personality-appropriate thanks or acknowledgment. NPCs in earshot react.

**Multi-sample reaction lines:** Each entry below includes **+5 (transformative)**, **+3 (deeply honored)**, and **0 (polite acceptance)** sample lines. DM picks the closest fit and may blend voice between them. Lower reactions (−1 and below) follow the refusal/insult patterns at the bottom of this file.

---

## ⛔ MANDATORY OUTPUT BLOCK — fires before companion reaction narration

When the player grants any title, output this block FIRST — before the companion speaks, before any narration. Then narrate.

```
[TITLE GRANTED — Name]
  Title       : [full title string the player spoke]
  Type        : Prefix | Suffix | Both
  Reaction    : +N / −N  (DM fit score — see REACTION SCORE SCALING table)
  Passive     : [passive name] — [scaled effect] | INACTIVE (reaction 0 or lower)
  Item        : [item name] — materialized at [full/75%/50%/25% power] | REFUSED (reaction −3 or lower)
  Relationship: [+2 / +1 / 0 / −1 / −2]
  Save write  : companion_titles.[name].prefix = "[title]" (if Prefix)
                companion_titles.[name].suffix = "[title]" (if Suffix)
                companion_titles.[name].prefix_passive = "[passive name]" (if active)
                companion_titles.[name].suffix_item = "[item name]" (if materialized)
                relationship.[name] [signed delta]
```

**⛔ Skipping this block and narrating the reaction without it = violation. Player can call `.fail 15`.**

---

## 🎭 ACTIVE PARTY ROSTER (11)

> **Vanguard:** eRmaC (Barb, PC), Linzi (Bard), Goldmoon (Cleric), Tika Waylan (Fighter), Ryuko Matoi (Thaumaturge), Morrigan (Witch).
> **Rearguard:** Sucrose (Alchemist), Artoria Pendragon (Champion), Olivier Armstrong (Commander), Yoko Littner (Gunslinger), Kyoko Kirigiri (Investigator), Tatsumaki (Psychic).
> **eRmaC** is the PC — Title rewards are granted BY him, not TO him. No entry below.

---

### ✦ LINZI — Maestro Bard

**Passive — ECHO LOOP:** Once per encounter, last composition effect re-triggers at half power on its next tick.

**Item — ENDLESS LUTE:** Compositions last +1 round. 1/day begin combat with a composition already active. Silver and violet, carved from wood that smells of chronicle ink.

**⛔ TITLE GRANTED block for Linzi MUST include:**
```
  Lute Mechanic: NOTEBOOK AUTO-FILL — when she plays, the notebook writes itself.
                 After any composition ends, lute produces 📖 entry + 🖊️ sketch.
                 See §ENDLESS LUTE — NOTEBOOK AUTO-FILL.
```
Omitting = `.fail 15`.

**+5 Reaction:**
> **LINZI** *(eyes enormous)*: *"This is a chronicler's instrument. In the songs, the old Kellid bards had these. I thought they were myths."* *(plucks one string; the room quiets)* *"I'm going to write about this moment. Chapter one, page one. The day the legend started properly."*

**+3 Reaction:**
> **LINZI** *(holding the lute carefully)*: *"It's good. It's really good. I — give me a second, I want to write what I just felt while I still feel it."* *(flips notebook open, scribbles three lines)* *"Okay. Now I can thank you properly. Thank you."*

**0 Reaction:**
> **LINZI** *(small polite smile, lute tucked under arm)*: *"Thank you. I'll take care of it."* *(beat)* *"I'll find a place for it in the chronicle. Eventually."*

**ENDLESS LUTE — NOTEBOOK AUTO-FILL**

> **DM:** The lute is carved from wood that smells of chronicle ink — not flavor, a mechanic. The lute and Linzi's notebook are linked. When she plays, the notebook fills itself, writing what she *means* by the song. If she plays grief over a victory, it records grief.

**Triggers:** After any Linzi composition ends in combat; when she plays voluntarily at camp, rest, or narrative scene. Does NOT fire mid-combat — entry appears after the fight.

**Output** — one 📖/🖊️ pair per distinct moment (multiple if scene had more):

> 📖 *[Paragraph in Linzi's chronicle voice — what the song was about, who, what the moment meant. Specific, not generic.]*
> 🖊️ *[Ink sketch — exactly what a reader sees opening the notebook to this page. Subject, composition, specific detail. The lute draws what she doesn't say out loud.]*

**Rules:** Her voice (third-person chronicle ↔ first-person reflection). Illustration specific — not *"a battle scene"* but *"eRmaC's hand on the guard's shoulder, the guard looking down at the napkin still folded in his palm."* Both reference the actual scene, not a summary. The notebook does not flatter — writes what happened, not what was heroic. Intent-driven — records what she *means*, including unspoken thoughts. Parallel — one trigger may produce multiple pairs, one per distinct moment/person/intent.

**⛔ POLYPHONIC — ONE-INSTRUMENT BAND:** At Linzi's will the lute produces the sound of any instrument she imagines — strings (harp, fiddle, viol), drums (frame, snare, kettle, hand), winds (flute, horn, pipe, reed), or full ensemble layered at once. She is a one-instrument band when she chooses. Lute remains a lute physically; sound is what she summons. No action cost to switch; shifts mid-composition if the chronicle calls for it. Combined-instrument compositions count as one composition mechanically.

---

### #2 SUCROSE — Tea Master Alchemist

**Passive — ANEMO CATALYST:** When Sucrose throws a bomb, the splash zone gains a 1-round Wind aura — allies in the zone gain +5 ft Speed and +1 to Reflex; enemies take −1 to ranged attacks against allies inside it.

**Item — BIO-ALCHEMICAL JOURNAL:** Leather-bound, stuffed with pressed leaves and wing-fragments. Once per encounter, Sucrose may craft a Field Bomb as a single action (normally 2 actions) drawn from the journal's living supply. Bound in dragonfly-paper that flutters when she's excited.

**+5 Reaction:**
> **SUCROSE** *(clutching the journal to her chest, voice barely above a whisper)*: *"O-oh — oh no, this is — this is too — I — I haven't deserved this yet, I — "* *(squeezes her eyes shut, opens them)* *"Okay. Okay. I am going to deserve it. I'm — thank you. I'm going to write down everything I learn. Starting tonight."*

**+3 Reaction:**
> **SUCROSE** *(turning the journal over, examining the binding)*: *"It's — it's organized exactly the way I would have organized it. How did you — "* *(stops; looks up)* *"You watched, didn't you. You watched me work and you remembered. Thank you."*

**0 Reaction:**
> **SUCROSE** *(small polite bow)*: *"Thank you. I'll — I'll put it to good use."* *(slips the journal into her satchel)* *"I should — I have something to test. Excuse me."*

---

### #15 ARTORIA PENDRAGON — Shield of Purity Champion

**Passive — KING'S OATH:** Once per encounter, when Artoria takes a Reactive Shield Block with Avalon (her shield), all allies within 15 ft gain temporary HP equal to her level for 1 round.

**Item — INVISIBLE AIR (Caliburn Sheath):** A scabbard of compressed wind, faintly luminous. Caliburn drawn from it on the first Strike of an encounter deals an extra die of damage and pierces concealment. Cannot be unsheathed except by Artoria.

**+5 Reaction:**
> **ARTORIA** *(kneels on one knee, hand on sheath)*: *"My king — my lord — "* *(catches herself, the formality breaking into something softer)* *"You have given me a name worthy of the oath I already swore. I will not let you regret either of them."* *(rises; the air around the sheath shimmers)* *"Caliburn answers. Hear it."*

**+3 Reaction:**
> **ARTORIA** *(tests the sheath at her hip, eyes closed for a moment)*: *"It fits. Properly fits."* *(opens her eyes, meets the player's gaze)* *"I will carry this in the manner it deserves. Thank you, sincerely."*

**0 Reaction:**
> **ARTORIA** *(formal nod, sheath accepted with both hands)*: *"I accept the honor and will discharge the duty it implies. Thank you."* *(strict, even tone — duty acknowledged, warmth withheld)*

---

### #21 GOLDMOON — Plains Healer Cleric

**Passive — DAWNSPRING:** Goldmoon's first Heal cast each encounter creates a 10-ft sanctified zone for 1 round; allies inside it gain Fast Healing equal to her WIS modifier and immunity to Frightened.

**Item — BLUE CRYSTAL STAFF:** A staff of crystallized lapis-blue, warm to touch even in winter. Heal spells cast through it ignore one step of cover and may target one additional creature within 30 ft once per round. The crystal hums when Mishakal is listening.

**+5 Reaction:**
> **GOLDMOON** *(both hands on the staff, tears unembarrassed)*: *"My grandmother carried something like this. I thought it was a story she told to make me brave."* *(presses her forehead to the crystal)* *"Mishakal, witness this. Witness the one who gave it to me. He is good. He is good, and I will heal for him until the staff goes dark."*

**+3 Reaction:**
> **GOLDMOON** *(running a thumb along the crystal)*: *"It is warm. It is warm the way the camp fires were warm when I was a girl."* *(quiet smile)* *"Thank you. I will carry it carefully."*

**0 Reaction:**
> **GOLDMOON** *(measured, courteous bow)*: *"It is generous. I will use it well."* *(tucks the staff against her shoulder; the warmth in her voice is professional, not personal)*

---

### #24 OLIVIER ARMSTRONG — Tactical Overlord Commander

**Passive — NORTH WALL:** Olivier's Tactics auras extend +5 ft. Once per encounter, when an ally within her aura is reduced to half HP, that ally gains a free Step and a +2 circumstance bonus to their next Strike.

**Item — BRIGGS SABER:** A straight-edged saber of cold-iron and steel, scabbard wrapped in white wolf-pelt. While drawn, Olivier may issue one Tactic order per round without spending an action; the blade glows pale when an ally executes the order.

**+5 Reaction:**
> **OLIVIER** *(draws the saber once, examines the edge, slides it home)*: *"I have been called many things by men who outranked me. Most of them were trying to flatter me out of the room."* *(turns to face the player, posture flat-shouldered)* *"You named me what I am. I will not forget that. The North does not forget."*

**+3 Reaction:**
> **OLIVIER** *(weighing the saber, single sharp nod)*: *"Acceptable. Better than acceptable."* *(beat)* *"You know the difference between honoring a soldier and flattering one. Few do. Thank you."*

**0 Reaction:**
> **OLIVIER** *(crisp salute, no smile)*: *"Acknowledged. The blade will be put to use."* *(returns to her work without further comment — Olivier's version of polite)*

---

### #35 TIKA WAYLAN — Polearm Master Fighter

**Passive — SOLAMNIC GRIT:** When Tika is Frightened, Sickened, or Wounded, she gains +2 to Strikes for the next round (stacks with the condition's normal effect — the fear sharpens her, it does not slow her).

**Item — SKILLET-AND-PIKE (Otik's Memory):** A guisarme whose hooked head is forged from an iron skillet flattened on the anvil — Otik's tavern skillet, the one she swung in the Inn of the Last Home. On a critical hit, the strike Trips and Sickens the target (DC = Tika's class DC). The handle still smells faintly of spiced potatoes when she's tired.

**+5 Reaction:**
> **TIKA** *(turns the weapon over, sees the skillet-head, and laughs — really laughs, one hand over her mouth)*: *"You — how did you — that's OTIK'S, that's the one he wouldn't let me use because I'd 'dent the customers' — "* *(wipes her eyes, grin huge)* *"I'm going to dent so many customers. Thank you. THANK YOU. He'd be so mad. He'd love it. He'd be mad and love it."*

**+3 Reaction:**
> **TIKA** *(testing the heft, swinging once)*: *"It moves like Otik's did. Heavier at the head. I — I can work with this. I can work HARD with this."* *(grins)* *"Thanks. Really."*

**0 Reaction:**
> **TIKA** *(polite nod, weapon shouldered)*: *"It's a good piece. I'll keep it sharp."* *(no joke about the skillet — the silence is the tell)*

---

### #39 YOKO LITTNER — Fake Out Sniper Gunslinger

**Passive — SPIRAL FOCUS:** Once per encounter, after Yoko misses a Strike, her next ranged Strike that round gains +2 to hit and treats the target as off-guard.

**Item — LONG-BARREL GIHA RIFLE:** A red, hand-forged rifle longer than she is tall, scope etched with a single spiral. Shots fired at long range (60+ ft) gain +1 damage die. The rifle does not jam, ever — it only stops firing when she stops trusting it.

**+5 Reaction:**
> **YOKO** *(shoulders the rifle, sights down it once, lowers it)*: *"That's my weight. That's my BALANCE. Whoever made this knew exactly how I shoot."* *(turns to the player, smirk softening)* *"You paid attention. Most people don't. Most people see the rifle and the hair and stop there."* *(taps the scope)* *"This is a real gift. I'll use it like one."*

**+3 Reaction:**
> **YOKO** *(works the action twice, listens to the click)*: *"Smooth. Real smooth."* *(slings it across her back)* *"Appreciate it. Genuinely."*

**0 Reaction:**
> **YOKO** *(checks the chamber, nods)*: *"Works. Thanks."* *(no smirk; she's already scanning the perimeter)*

---

### #43 KYOKO KIRIGIRI — Forensic Medicine Investigator

**Passive — DETECTIVE'S CERTAINTY:** When Kyoko has a Lead on a target, the FIRST Devise a Stratagem each round may roll twice and take the higher result. Stack with normal Devise rules.

**Item — VIOLET CASE:** A leather investigator's case with violet trim, fitted with vials, lockpicks, and a notepad whose pages never run out. When opened, Kyoko may treat any one Recall Knowledge or Crafting (Forensic) check as if she had Master proficiency for that roll. Once per scene.

**+5 Reaction:**
> **KYOKO** *(opens the case, examines the contents one item at a time, gloved hands steady)*: *"Notepad is acid-free. Vials are leaded glass. Lockpicks are tensioned correctly."* *(closes the case, looks up)* *"You sourced this. You did not commission it from a generalist."* *(small, real smile — rare)*: *"Thank you. I will tell you when I solve something with it. You should know."*

**+3 Reaction:**
> **KYOKO** *(catalogs the contents in silence, then nods once)*: *"It is well-made. I appreciate the care taken."* *(closes the case carefully)* *"Thank you."*

**0 Reaction:**
> **KYOKO** *(brief inspection, polite nod)*: *"Functional. I will use it."* *(case clipped to her belt; she returns to whatever she was doing)*

---

### #58 TATSUMAKI — Chronos Master Psychic

**Passive — PSYCHIC GRAVITY:** When Tatsumaki Amps a spell, all enemies within 10 ft of the spell's target are pushed 5 ft toward (or away from, her choice) the impact point. Save negates.

**Item — TIARA OF THE TORNADO:** A delicate gold tiara with a single emerald set above the brow. While worn, Tatsumaki's Telekinesis range increases by 30 ft, and once per encounter she may sustain a focus spell without using an action. The tiara floats slightly above her hair when she is annoyed (she is often annoyed).

**+5 Reaction:**
> **TATSUMAKI** *(arms crossed, hovering an inch off the floor as the tiara settles)*: *"Hmph. About time someone recognized."* *(beat — the floating drops slightly)* *"…Don't make me say thank you. I know you can hear what I'm not saying. Use the gift well or I'll take it back. I CAN take it back, I want you to know that."* *(she will not take it back)*

**+3 Reaction:**
> **TATSUMAKI** *(adjusts the tiara, glances sideways)*: *"It's. Acceptable. Tch."* *(beat)* *"Don't get used to giving me things. I don't return the gesture."* *(she is keeping it forever)*

**0 Reaction:**
> **TATSUMAKI** *(takes the tiara, drops it into her pocket without trying it on)*: *"Noted."* *(walks away. The tiara appears on her brow next session, no comment.)*

---

### #78 RYUKO MATOI — Regalia Thaumaturge

**Passive — SCISSOR RESONANCE:** When Ryuko Exploits a Vulnerability with her Implement (the half-scissor blade), she also gains a +5-ft Reach for that Strike, and the target takes 1 persistent slashing damage.

**Item — SENKETSU FRAGMENT:** A swatch of living crimson fabric stitched into the lining of her jacket — a remnant of the kamui that knew her. While worn, Ryuko may treat one failed save against Frightened or Stupefied per encounter as a success; the fabric ripples when it works. She hears it speak only at night.

**+5 Reaction:**
> **RYUKO** *(touches the fabric, breath catches — actually catches)*: *"Senketsu. Hey. HEY. You're really — "* *(lowers her voice, ear close to the lining)* *"Yeah. Yeah, I hear you."* *(turns to the player, eyes wet, jaw set)* *"You found him. You FOUND him. I don't — I owe you for this. I owe you HUGE. Don't try to tell me I don't. Just say you're welcome and let me have this."*

**+3 Reaction:**
> **RYUKO** *(presses the fabric to her cheek for one second, then drops her hand)*: *"It's him. Even just a piece. Thanks. Real thanks."* *(turns away to compose herself; she is not embarrassed, she just needs the moment)*

**0 Reaction:**
> **RYUKO** *(takes the fabric, folds it carefully, slips it into her jacket lining)*: *"…Thanks."* *(short. She'll process this later, alone)*

---

### #83 MORRIGAN — Hex Witch

**Passive — WILDS' FAVOR:** When Morrigan's Hex hits, the target also takes a −1 status penalty to its next save against any of her spells that round. Stacks once.

**Item — FLEMETH'S MIRROR-SHARD:** A shard of black obsidian on a silver chain, worn at her throat. Once per day, Morrigan may use Eyes of the Beast (treat as a 4th-rank spell — she sees through any one beast within 1 mile for 1 minute). The shard whispers in Flemeth's voice if she ignores it for too long; it is hers, but it remembers her mother.

**+5 Reaction:**
> **MORRIGAN** *(lifts the chain, the shard catching no light it should)*: *"You have either remarkable taste or remarkable nerve. I am not yet decided which."* *(slips it on; the air briefly chills)* *"Mother's eye. Or what's left of it. You return to me a piece of myself I had not realized I missed."* *(slight, sharp smile)* *"Do not expect sentiment. Expect — competence. Sharper than before."*

**+3 Reaction:**
> **MORRIGAN** *(turns the shard over, examines it without touching the chain)*: *"Functional. And not without flair. I shall make use of it."* *(fastens it herself; does not thank him aloud, but holds his gaze for a beat longer than necessary — that IS her thanks)*

**0 Reaction:**
> **MORRIGAN** *(accepts the shard with one hand, drops it into her belt-pouch)*: *"Noted."* *(walks past him without further comment. The shard is at her throat the next morning. She does not mention putting it on.)*

---

## ⚠️ NEGATIVE REACTION LINES (general patterns)

**−1/−2 (wears it out of loyalty):** Companion accepts but the line is short and flat. *"I'll wear it."* No elaboration. They are doing this for the player, not for themselves.

**−3/−4 (refused — item dissolves):** Companion physically cannot accept. The item dissolves on contact. They explain why, briefly, and the explanation is honest.

> **SUCROSE [−3]:** *"I — I can't — the name doesn't fit, it would feel like wearing someone else's coat. I'm sorry. I'm really sorry."*
> **OLIVIER [−3]:** *"That title belongs to a soldier I am not. I will not wear it as theatre. The North does not lie."*
> **MORRIGAN [−3]:** *"You misread me. Try again, or don't. The shard goes back into the wilds — it knows what it deserves."*

**−5 (insult — title revoked, −1 penalty):** Companion does not just refuse. They take a step back. The line is sharp. The player loses standing in front of any other companions present. The title slot is locked from re-granting for the rest of the chapter.

> **TATSUMAKI [−5]:** *"…Are you joking with me. Are you JOKING. Get out of my sight. Take the tiara. I don't want it. I don't want anything from someone who looks at me and sees THAT."*
> **RYUKO [−5]:** *"No. NO. You don't — you don't get to call me that. Take it back. I mean it. Take the fabric back, I don't want it tied to that name."*
> **ARTORIA [−5]:** *"That title is a slander against the oath I swore. I cannot accept it. I will not. We will not speak of it again."*

---

## 🔓 QUEST-LOCKED CRPG COMPANIONS (8)

> Recruitable mid-campaign via their respective quest hooks. Always eligible for Titles once joined. Listed in companion-index order.

---

### #16 TRISTIAN — Healer Cleric of Sarenrae

**Passive — DAWNFLOWER'S MERCY:** When Tristian Heals an ally below half HP, the target also clears one negative condition of his choice (Frightened, Sickened, or Stupefied). 1/round.

**Item — SUNDISC AMULET:** A bronze sunburst on a thin chain. Once per encounter, Tristian may cast a Heal as a single action (instead of two) by spending the disc's stored light — the amulet dims for one round, then rekindles. Warm even in shadow.

**+5 Reaction:**
> **TRISTIAN** *(closes his hand around the disc, eyes shut)*: *"Sarenrae forgive me — I had stopped expecting kindness like this."* *(opens his eyes, calm now)* *"Thank you. I will earn it. Quietly. The way she taught me to."*

**+3 Reaction:**
> **TRISTIAN** *(holds the amulet up to the light)*: *"It is well-made. And it was given thoughtfully — that matters more."* *(small bow)* *"Thank you."*

---

### #18 JAETHAL — Inquisitor (Undead) — *if recruited*

**Passive — UREGUR'S LISTENER:** When Jaethal succeeds at a Sense Motive against an enemy, she also grants one ally within 30 ft a +1 status bonus to attack rolls against that enemy for 1 round.

**Item — CARRION SICKLE:** A curved bone-and-iron sickle. On a critical hit, the target takes 1d6 negative damage and is informed (silently, in their dying mind) of one truth Jaethal believes about them. Cosmetic — but unsettling for the DM to narrate.

**+5 Reaction:**
> **JAETHAL** *(turns the sickle in her hand, undead eyes unreadable)*: *"You name me what I am, not what they call me. There is a difference."* *(very slight nod)* *"I will not forget that. The dead remember longer."*

**+3 Reaction:**
> **JAETHAL** *(takes the sickle, weighs it)*: *"It will serve. As will I."* *(short — Jaethal does not perform gratitude)*

---

### #45 KALIKKE — Cold Kineticist (Twin)

**Passive — HOARFROST CALM:** When Kalikke uses a Cold-element Impulse, all allies within 10 ft of her become immune to Frightened until the end of her next turn.

**Item — TWIN-PENDANT (Kalikke's half):** Half of a paired pendant, pale silver. Worn around her neck. While worn, switching to Kanerah is a free action (instead of single) once per encounter — and the swap leaves a hoarfrost ring at her feet (difficult terrain, 1 round).

**+5 Reaction:**
> **KALIKKE** *(holding the pendant, voice quiet but steady)*: *"You named both of us. Not just the easy half."* *(closes the pendant in her palm)* *"Thank you. Kanerah will say it her own way. I am saying it for the part of me that needed to hear it from someone who was not her."*

**+3 Reaction:**
> **KALIKKE** *(slips the pendant on, fingers cold)*: *"It fits. We can both feel it."* *(small smile)* *"Thank you."*

---

### #45 KANERAH — Fire Kineticist (Twin)

**Passive — EMBER'S APPETITE:** When Kanerah uses a Fire-element Impulse, the first enemy struck takes 2 persistent fire damage in addition to the normal effect.

**Item — TWIN-PENDANT (Kanerah's half):** The other half, set with a cabochon of red garnet. Switching from Kalikke gains Kanerah a free 5-ft Step on arrival, and her first Fire Impulse that turn ignores 5 fire resistance.

**+5 Reaction:**
> **KANERAH** *(takes the pendant, examines the garnet, smirks)*: *"About time. She gets all the soft praise; I get the side glances. You named ME."* *(beat — softer)* *"…I won't say it twice. Don't make me. Thank you."*

**+3 Reaction:**
> **KANERAH** *(fastens the pendant herself)*: *"Sharp. I approve."* *(turns away — her version of warmth)*

---

### #48 REGONGAR — Eldritch Archer Magus *(or Spellstrike build)*

**Passive — HALF-ORC SPELLBLOOD:** Once per encounter, when Regongar lands a Spellstrike, his next melee Strike that round counts as off-guard target regardless of position.

**Item — TUSKED PAULDRON:** A single shoulder pauldron, half-orc work, set with a yellowed boar's tusk. While worn, Regongar gains +1 to Intimidation and may Demoralize as a free action immediately after a Spellstrike crits.

**+5 Reaction:**
> **REGONGAR** *(rolls the pauldron over his shoulder, the tusk catching the firelight)*: *"Heh. HEH. Yeah. YEAH."* *(grin huge)* *"You see me. Octavia sees me. Now you see me too. That's three."* *(quieter)* *"Three's a lot. Thank you."*

**+3 Reaction:**
> **REGONGAR** *(straps the pauldron on, tests the weight)*: *"Solid. Good iron."* *(claps the player's shoulder once, heavy)* *"Thanks."*

---

### #60 EKUNDAYO — Beastmaster Ranger

**Passive — TRKAA'S TETHER:** While Trkaa is within 60 ft of Ekundayo, both gain +1 to Stealth and to Strikes against the same target.

**Item — WIDOWMAKER'S BOW:** A longbow of dark dryad-wood, restrung with sinew Ekundayo refused to throw away. Deals +1d6 damage on the first Strike of any encounter against an enemy who has not yet acted. The wood is older than him by a long way.

**+5 Reaction:**
> **EKUNDAYO** *(takes the bow, draws it once, lets it down)*: *"My wife strung the first bow I ever owned. This one feels like she made it."* *(turns away, eyes wet, Trkaa pressed against his leg)* *"…I will not waste it. Thank you. That is all I have words for tonight."*

**+3 Reaction:**
> **EKUNDAYO** *(runs his hand along the bow's spine)*: *"Good wood. Good string. Trkaa likes it."* *(that is high praise)* *"Thank you."*

---

### #66 NOK-NOK — Goblin Rogue (Hero of the People)

**Passive — HERO'S GRIN:** Once per encounter, after Nok-Nok lands a Sneak Attack, all allies within 30 ft gain a +1 status bonus to their next Strike that round (Nok-Nok's HEROISM is contagious).

**Item — KING-MAKER KNIFE:** A blade too big for a goblin and that is the point. Forged from horseshoe iron and a cracked sword-tip. First Strike of an encounter ignores 2 armor and inflicts 1d4 persistent bleed on a hit.

**+5 Reaction:**
> **NOK-NOK** *(holding the knife above his head, hopping in place)*: *"HERO! HERO HERO HERO! Nok-Nok has a HERO BLADE! From a HERO! For a HERO!"* *(stops; suddenly serious; lowers the knife)* *"…Nok-Nok will not lose this one. Nok-Nok PROMISES. Other gifts — yes, lost. This one — NEVER."*

**+3 Reaction:**
> **NOK-NOK** *(grins, tucks the knife into his belt with both hands)*: *"Big stab! Hero stab! Thank you!"* *(scampers off to show Linzi)*

---

### #84 OCTAVIA — Arcane Trickster (Wizard/Rogue)

**Passive — MAGE-HAND'S MISCHIEF:** Once per encounter, Octavia may cast a cantrip-rank spell as part of a Sneak Attack — the spell's effect resolves first, granting off-guard, then the dagger lands.

**Item — GLASS-EYED RING:** A silver ring with a milky-white glass stone. While worn, Octavia gains +2 to Stealth and may cast Invisibility on herself once per day as a 2nd-rank slotless spell. The stone clouds further when she lies (only she can see it).

**+5 Reaction:**
> **OCTAVIA** *(slips the ring on, examines the stone, voice carefully light)*: *"Glass eye. That's funny. I've worn worse jewelry."* *(beat — the lightness drops)* *"…You picked something for who I AM. Not what I used to be sold as. That doesn't happen often. I'll remember."*

**+3 Reaction:**
> **OCTAVIA** *(turns the ring over, smiles crookedly)*: *"Pretty. And practical. I can work with that."* *(slips it on)* *"Thanks, boss."*

---

### #1 JUBILOST — Investigator (Gnome Cartographer)

**Passive — INSUFFERABLE ACCURACY:** When Jubilost successfully Recalls Knowledge, he may grant one ally a +2 circumstance bonus to their next Strike against the studied target. 1/round. He WILL announce that he provided this bonus.

**Item — SILVER-INK QUILL:** A silver-fitted quill that writes without ink. Once per day, Jubilost may treat any one Lore or Crafting check as if he had Legendary proficiency. The quill records the result on its own scroll, which never fills.

**+5 Reaction:**
> **JUBILOST** *(examines the quill at three different angles, then sniffs it)*: *"Mithral fittings. Goose primary, not turkey — someone with TASTE selected this. Astonishing. I had begun to suspect you were not paying attention. I retract the suspicion. PROVISIONALLY."* *(pockets the quill with great ceremony)* *"Consider me — momentarily — pleased."*

**+3 Reaction:**
> **JUBILOST** *(turns the quill in two fingers)*: *"Functional. Marginally elegant. I shall use it. Often. Loudly."* *(beat)* *"Thank you. I do not say that to everyone. Note the date.")*

---

## 🔒 OFF-ROSTER COMPANIONS — DM GENERATION RULES

> **⛔ Companions outside the active 11 (recruited later via Pick-10 alternates, Five Seekers conversion, or quest-triggered joins) do NOT have predefined passives/items. The DM generates them at title-grant time using the patterns above.**

**Rules:**
1. Passive must match class core identity
2. Item must match build AND backstory (use the companion's KM_Backstories_*.md entry)
3. Power level identical to the 11 above
4. Reaction score scales the same way
5. Generate AT LEAST a +5, +3, and 0 sample line in their voice
6. Generate at least one negative-reaction sample (−3 or −5) appropriate to their personality

---

## ⛔ DM DISPLAY FORMAT

**Suffix granted:**
```
[TITLE GRANTED — SUFFIX]
[Name] "[Suffix]"
Meaning: [player's stated meaning]
Reaction Score: [−5 to +5]
Item Materialized: [item name + description]
```
Then narrate materialization + companion reaction (use closest sample line + voice-blend).

**Prefix granted:**
```
[TITLE GRANTED — PREFIX]
"[Prefix]" [Name] "[Suffix]"
Meaning: [player's stated meaning]
Reaction Score: [−5 to +5]
Passive Activated: [name + effect]
```
Then narrate activation + companion reaction (use closest sample line + voice-blend).

**Save block:** Write to `companion_titles.[name]` with `suffix`, `prefix`, `suffix_item`, `prefix_passive`, `suffix_reaction`, `prefix_reaction`.

---

*KM_Companions_Titles.md — Kingmaker PF2e Text Adventure | Title Rewards v3.0*
*v3.0: Roster aligned to active 11-companion party (Linzi + #2 #15 #21 #24 #35 #39 #43 #58 #78 #83). Multi-sample reactions (+5 / +3 / 0) plus negative-reaction patterns. Pre-v3.0 entries (Amiri, Lann, Ember, Daeran, Nenio, Regill, Arueshalae, Seelah) removed — none in current roster.*
