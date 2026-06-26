# CHAPTER 5 — WAR OF THE RIVER KINGS
# ═══════════════════════════════════════════

**Levels:** 16 → 18 | **Duration:** war deadline scales with Rushlight result (240 days did-well / 210 neutral / 150 bad-or-skipped)
**New region:** Pitax, the River Kingdoms, Irovetti's palace

## Overview
Castruccio Irovetti of Pitax invades, branding the player a bandit-king. The chapter has a canon spine
the player MUST clear before Irovetti is reachable — deal with the monsters and propaganda destabilising
the realm, walk Nyrissa's dream, recover the means to break Irovetti at Whiterose Abbey, then enter Pitax
itself. The kingdom war (army battles) and a direct infiltration both run alongside. Irovetti must be
defeated and his palace taken.

> ⚠️ CANON GATE: the player cannot cleanly resolve Irovetti without Whiterose Abbey (Phase 5). The dream
> (Phase 4) is what reveals the Abbey. Skipping these is the "bad" war-deadline path.

---

## Phase 1 — War Declaration

> **Herald:** *"Irovetti of Pitax declares that the Stolen Lands are an illegal territory, their ruler a
> bandit-king, and their kingdom a blight upon the River Kingdoms. He invades in the name of civilization."*

Kingdom events become war events — economy disrupted, borders threatened, monster raids begin. Two canon
problems open at once: **monsters teleporting into the realm** (Phase 2) and **Pitax propaganda / river
piracy** (Phase 3). The Rushlight Tournament invitation (Phase 6) also lands now — and how the player
performs there sets the war's deadline timer.

---

## Phase 2 — On the Trail of Monsters (The Menagerie)

Monsters are appearing inside kingdom borders. Resolve via the kingdom project, then clear the source.

```
KINGDOM PROJECT — "On the Trail of Monsters" (100 BP, 45 days)
  Completing it reveals THE MENAGERIE on the world map.

THE MENAGERIE (cave):
  A caged-beast warren where a Pitax mage teleports monsters into the player's lands.
  Objective: enter the cave and ELIMINATE THE MAGE teleporting the monsters.
  Mage: NYRD ZOTTENROPPLE (gnome conjurer). Kill him to stop the raids.
    (If the player reaches River Blades' Camp first without clearing this, Nyrd is found THERE instead.)
```

`menagerie_cleared = TRUE` | `monster_raids_stopped = TRUE`
XP: standard dungeon clear + objective bonus

---

## Phase 3 — River Blades' Camp & the Propagandists

Pitax-paid agents are stirring the River Kingdoms against the player and running piracy on the trade
routes (the Silk Road eRmaC is building — hits home).

```
RIVER BLADES' CAMP:
  Bandit/mercenary camp working for Pitax.
  Named foes: ILORA NUSKI and URTENEA.
  NYRD ZOTTENROPPLE is also here IF Phase 2 (the Menagerie) was not cleared first.
  Clearing it ends the propaganda/instigator pressure on the realm.

THE PROPAGANDISTS / INSTIGATORS:
  Pitax mouthpieces turning neighbouring River Kings against the player.
  Resolve by silencing the camp + (optionally) the Academy piracy plot in Pitax (see Phase 7,
  "The River's Justice").
```

`river_blades_cleared = TRUE` | `propaganda_silenced = TRUE`
XP: camp clear + objective bonus

---

## Phase 4 — The Path of the Dreams (reveals Whiterose Abbey)

Nyrissa's hand is on this war. The player walks her dream to learn where Irovetti's weakness lies.

```
REQUIREMENT: "The Nymph's Gift" must be in inventory (NOT the personal stash).
KINGDOM PROJECT — "A Way into Nyrissa's Dream"
  60 days / 150 BP  (or 30 days / 75 BP on the faster track)

INTO THE DREAMSCAPE:
  Talk to the STORYTELLER, say you are ready → teleported to the Dreamscape ALONE WITH LINZI
  (chronicler-of-record; if leliana_chronicler_mode, Leliana takes this beat).
  - Approach the nymphs and Nyrissa; talk to them.
  - Defeat the THREE DEFACED SISTERS (Dreamscape).
  - In the dream Throne Room: defeat the DREAM APPARITIONS — they die in one hit but strike with the
    full abilities/damage of the originals (lethal if ignored).
  - Talk to Nyrissa again → she REVEALS the location of WHITEROSE ABBEY.
```

`path_of_dreams_complete = TRUE` | `whiterose_location_known = TRUE`
XP: dream sequence + Defaced Sisters

---

## Phase 5 — Whiterose Abbey (REQUIRED before Pitax)

Nyrissa directs the player here: *"the Abbey remembers what Irovetti wears — go and take back the means
to break him."* This is the canon gate to beating Irovetti cleanly.

```
ABBEY INTERIOR:
  Trapped halls (Perception / Disable Device by tier) + fey and undead mobs.
  First chamber, RIGHT WALL → RING OF CHAOS (loot).
  Hall's end — THE DRIPPING CLOCK:
    Loot beside it → SINGING EDGE (weapon).
    BREAK THE CLOCK → releases EVINDRA's memory: her tale of woe + the record of Irovetti's crimes
      (the lore that powers the TRUE-ENDING path — see Ch7).

EVINDRA (nymph; Nyrissa's estranged friend, bound here):
  Recruitable to the player's cause. ⭐ Key thread for the BEST ENDING.
  Valerie warns against trusting a fey; the choice is the player's.
  `evindra_freed = TRUE` | opens quest "The Ravenous Queen"

LAKE DEPTHS (optional):
  Interact → 5,760 XP + FOX SIGNET RING.
  Athletics DC 30 → DARKWIND (weapon).
  Knowledge (World) DC 30 → +2,160 XP (Evindra / Nyrissa lore).

RESOLUTION:
  Return to the throne room → STEFANO MOSKONI arrives and formally invites the player to treat with
  Irovetti at Pitax → opens Phase 7 (Pitax City).
```

`whiterose_complete = TRUE` | `irovetti_means_secured = TRUE` | `stefano_invite_received = TRUE`
XP: ~6,000 (abbey clear) + lake bonuses

---

## Phase 6 — The Rushlight Tournament (canon Ch5 — moved from Ch4)

Irovetti hosts the Rushlight Tournament at Rushlight Fields as a pretext to size up the player. **Leaving
the area before finishing all events FAILS the quest.** Performance here SETS THE WAR DEADLINE
(did-well 240 days / neutral 210 / poorly-or-skipped 150).

```
RUSHLIGHT FIELDS — events run by NUNZIO ARPAIA:
  • FISHER'S TRIATHLON — book event (skill-checked stages).
  • DRUNKEN BRAWL — fight 5 brawlers in sequence; the Pitax champion is the strongest.
  • Additional contests of arms/skill are offered at the fairground (compete or decline each).
  Winning well across events = "did well" → longest war deadline + Irovetti rattled.

EIMAR DESCHAMPS (playwright) is met HERE — accepting his thread opens "The River's Justice" later at
  the Pitax Academy (Phase 7).
IROVETTI appears to take the player's measure — courteous, testing. Sense Motive: he is afraid and
  covering it.
```

`rushlight_attended = TRUE` | `rushlight_result = [well / neutral / poor]` | `war_deadline_days = N`
`eimar_thread_open = TRUE/FALSE`

---

## Phase 7 — Pitax (City)

With Stefano's invitation, the player enters Pitax proper. ⛔ Avoid charging the palace gate first —
work the city to flip its leaders, which weakens Irovetti before the throne room.

```
MAIN SQUARE:
  Speak with the guard captain and the rival HOUSE LEADERS — Diplomacy/Intimidation to turn them
  against Irovetti (each flipped leader weakens his standing and the palace defence).
  The Pitax Royal Palace is reached via the NORTHEASTERN exit.

ACADEMY OF GRAND ARTS:
  EIMAR DESCHAMPS is here if his Rushlight thread was accepted.
  QUEST — "THE RIVER'S JUSTICE": dispose of the river pirates and expose the piracy plot.
    WALSH CELVOWAY and RENSHALA VASCARI (or JHOFRE VASCARI if she is dead) confront the player;
    accuse Celvoway and his men of being behind the piracy. Resolving it ends the river-route raids
    for good and earns River Kingdoms standing.

PITAX RIVER BEND:
  Riverside district (book event + encounters); approach route / side content.
```

`pitax_entered = TRUE` | `pitax_leaders_swayed = [list]` | `rivers_justice_resolved = TRUE/FALSE`

---

## Phase 8 — Irovetti (the palace & the war's end)

The player may reach Irovetti by the city/court route above, by the **military path** (army war), or by
**direct infiltration** — all converge on the palace.

```
MILITARY PATH (army war system):
  Pitax fields 3 initial army units:
    Pitax Royal Guard: Offense +8, Defense 18, Morale 16
    River Mercenaries ×2: Offense +5, Defense 14, Morale 12
  Match with equivalent armies or better on the hex map.

  BRINEHEART SIEGE (border fortress — first major engagement):
    Army combat OR a direct party assault. Fort AC 22, HP 120. Garrison: 8 soldiers + Linxia.

INFILTRATION PATH (palace approach):
  A. Sewers (Athletics DC 16 per junction)
  B. Noble disguise (Deception DC 24; noble outfit 500 gp)
  C. Servant disguise (Deception DC 18)
  Inside: Irovetti's vault (8,400 gp, Ring of the Archmagi) + Tartuccio's note
    → `tartuccio_pitax_connection_confirmed = TRUE` (a letter: Tartuccio has reported on the player
       since Ch1).

LINXIA — Pitax Captain (Rogue 9)
  HP: 96 | AC: 22 (Studded Leather +2 + Dex) | Speed: 30 ft
  Fort +12 | Ref +18 | Will +11
  Rapier: d20+15 (1d6+8 P, Finesse) | Sneak Attack: +5d6 | Evasion | Gang Up (flanks solo)
  Persuade to defect: Diplomacy DC 28 → surrenders the fort, joins as informant (+25,000 gp reward)
  XP: 480

DARVEN MOURNE — Pitax merchant (side quest):
  Approaches during the Brineheart siege or at the capital. Not a fighter — a businessman who backed
  the wrong king.
  DARVEN: "I funded Irovetti for six years. I would prefer my head stay attached.
           I can offer something worth more than my neck."
  Offer: 25,000 gp, four Pitax supply-chain maps (army costs −10% for 2 turns), signed war-crimes
  confession (River Kingdoms diplomacy post-Ch5). In exchange: his life + safe conduct.
  - Accept → `darven_deal = accepted` → gp + maps + confession. Recurring Ch6 contact.
  - Negotiate (Diplomacy DC 18) → same + hidden palace-basement cache. `darven_cache_location = TRUE`
  - Arrest → `darven_arrested = TRUE` → +1 Loyalty, +5,000 gp seized. No maps.
  - Kill → `darven_killed = TRUE` → nothing. Slight evil tendency.
  XP: +200 any resolution except kill. +100 if negotiated.
```

> **⛔ GM EYES ONLY — IROVETTI'S FULL NAME — READ BEFORE RUNNING ANY SCENE WHERE HIS NAME COMES UP**
>
> **Full name: Castruccio Irovetti of Pitax**
> "Irovetti" is his house name. He rules exclusively as "Irovetti of Pitax" — his given name Castruccio is suppressed. He does not use it, sign with it, or acknowledge it publicly. Most of the River Kingdoms do not know it exists. Paizo buries it deliberately so players do not make the connection immediately.
>
> **THE TARTUCCIO CONNECTION — NEVER VOLUNTEER THIS:**
> Castruccio → Tartuccio. Same Taldan diminutive construction (-struccio / -tuccio). One letter apart. Same rhythm. Same origin.
> Tartuccio is named in deliberate echo of his patron's buried given name. It is a calling card legible only to someone who knows both names.
> When Tartuccio said *"my mother had aspirations"* — he was not lying. She named him after the part of the king that nobody says out loud.
>
> **DISCOVERY RULE — MANDATORY:**
> The DM never surfaces this connection unprompted. It exists to be found by the player through logical deduction: naming conventions → River Kings' full names → first name vs house name → what is Irovetti's given name → Castruccio → Castruccio/Tartuccio said aloud in the same breath.
> Linzi is the natural vector. She notices linguistic patterns. If the player leads her toward it, she can arrive at it. The DM's job is to follow the chain and let it land — not to shortcut it and not to stall when the player is clearly building toward it.
> The payoff is Linzi saying "Castruccio" out loud while Tartuccio is in the room and watching his face.

```
IROVETTI — see KM_Bestiary.md for full stat block (CR 13, HP 195, AC 32)

SPECIAL: Court musicians play during the fight — Performance DC 20 to silence (removes his morale buff).

RESOLUTION:
  Kill → Kingdom gains Pitax as a vassal.
  Capture → Public trial. Handed to Brevoy → Jamandi bonus.
  Recruit [Evil] → Impossible. Too vain.

LOOT: +2 Striking Rapier, Cloak of Resistance +4, Headband of Mental Perfection +4,
      Irovetti's Crown, 8,400 gp vault, 3,789 gp treasury
XP: 1,560
```

---

## Side Quest — Runaway Throne

A petty-but-flavourful Pitax-era quest: the player's own throne is stolen.

```
- Talk with HYLAND, HASSUF, VERDEL and ELINA about the thieves and stolen goods.
- Complete "Tracking the Throne Thief" → reveals INCONSPICUOUS RAVINE
  (or wander the world map for the Special Encounter: Goblin Trader).
- Visit LOSTLARN KEEP for "Heroes' Fate" → Special Encounter (Goblin Trader Lostlarn) after it.
- Talk to the GOBLIN MERCHANT about the throne (start price 100):
    Diplomacy DC 18 → +33 XP, price rises to 200;
    tell him you don't need it → price drops 100 → 50 → free.
```

`runaway_throne = [resolved / ignored]`

---

## Ch5 → Ch6 Export
```json
{
  "export_from": "chapter_5", "import_to": "chapter_6",
  "player": { "level": 0, "xp": 0, "hp_current": 0, "hp_max": 0,
               "hero_points": 1, "gold": {}, "inventory": {} },
  "companions": [],
  "kingdom": { "turn": 0, "culture": 0, "economy": 0, "loyalty": 0,
               "stability": 0, "unrest": 0, "armies": [],
               "pitax_vassal": false },
  "story_flags": {
    "irovetti_fate": "",
    "pitax_vassal": false,
    "linxia_fate": "",
    "darven_fate": "",
    "menagerie_cleared": false,
    "river_blades_cleared": false,
    "path_of_dreams_complete": false,
    "whiterose_complete": false,
    "evindra_freed": false,
    "rivers_justice_resolved": false,
    "rushlight_result": "",
    "war_deadline_days": 0,
    "runaway_throne": "",
    "tartuccio_pitax_confirmed": true,
    "tartuccio_final_fate": "",
    "military_path_used": false,
    "infiltration_path_used": false,
    "brineheart_taken": false,
    "river_kingdoms_allied": [],
    "companion_quests": {},
    "alignment_track": {}
  },
  "dispositions": {}, "companion_titles": {}, "faction_tiers": {},
  "standing_orders": {}, "crafting": {}, "mobile_base": {},
  "dream_log": [], "prestige": {}, "mythic_path": {}, "ending_flags": {}
}
```

## 📋 CH6 LOAD CHECKLIST
```
[GM CHAPTER 6 LOAD CHECK]
□ KM_Ch6.md loaded (the Chapter 6 file)
□ KM_Linzi_Shrine.md loaded — shrine quest may trigger this chapter
□ All standard files loaded (see KM.txt How to Continue)
□ Ch5 Export Block imported and parsed
□ Player level 16–18, kingdom state confirmed
□ Key flags read:
    irovetti_fate           : [value]
    pitax_vassal            : [TRUE/FALSE]
    evindra_freed           : [TRUE/FALSE — true-ending thread]
    tartuccio_final_fate    : [value — he should be resolved by now]
    all companion quests    : [status — CRITICAL for Ch7 survival]
    alignment_track         : [both axes]
    nyrissa_backstory_known : [TRUE/FALSE — affects true ending]
□ COMPANION QUEST AUDIT: list every companion and their quest status
   Any incomplete quests = risk of losing that companion in Ch6 or Ch7
□ Bloom escalation will consume hexes each kingdom turn — prepare defenses
□ Game State Header output, then begin
```

---

# ═══════════════════════════════════════════
