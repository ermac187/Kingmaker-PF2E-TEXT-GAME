# KINGMAKER — MALAK'S JAIL: THE FIVE IMPRISONED SEEKERS
## KM_Malak_Jail.md | Referenced by: KM_PrePrologue.md, KM_Prologue.md, KM_Ch1.md

---

> **DM:** Load this file alongside KM_PrePrologue.md when the parchment is recovered or when the player learns five seekers were jailed before they arrived. This file covers the Restov City Jail location, the five imprisoned Call to Heroes invitees, the two player paths to resolve their situation, and the downstream effect on Tartuccio's team in Ch1.

---

## 📜 MALAK'S PARCHMENT — FULL CONTENTS

> **DM:** These are the exact contents of the parchment found on Malak's person. Read them when the player examines the document. Do not summarize — present the three directives as written below, with their gold values. The parchment is written in a clipped mercantile hand, unsigned. No house seal. No sender name.

---

**The parchment reads:**

---

*DIRECTIVE ONE — GATE INTERCEPTION*

*The individuals named on the attached list are invited guests of Lady Jamandi Aldori's Call to Heroes. They are to be turned away, arrested on fabricated grounds, or killed if resistance is offered. Payment is as follows:*

- *Turned away (leaves city): 5 gp per person*
- *Arrested and held through the ceremony: 20 gp per person*
- *Killed (documented): 50 gp per person*

*The list is separate and to be destroyed after memorization.*

---

*DIRECTIVE TWO — GATE PROTOCOL, NIGHT OF THE CEREMONY*

*On the night of the ceremony, the east gate is to be left unguarded for one quarter-hour beginning at the second bell after dark. The gate is to remain open. No guards within 30 paces of the gate entrance during this window. This creates an unobserved entry corridor for our agents moving materials and personnel into the manor district.*

*Execution of this directive without incident: 80 gp*

*Failure to execute or early detection: payment void. You will not be protected.*

---

*DIRECTIVE THREE — MANOR WORKER APPROVALS*

*A list of workers seeking temporary employment at Jamandi's manor for the ceremony will be submitted through the city labor registry. You are to approve all names on this list without flagging them for the manor's own security review. Workers from this list will be identifiable by a red cord worn on the left wrist.*

*Each approved worker who successfully enters the manor: 10 gp*

---

*Payment for completed directives is through the usual drop. Do not contact us directly. Do not keep this document.*

---

> **DM RULES — PARCHMENT:**
> - The parchment names no sender. The player cannot determine the source from the document alone.
> - `parchment_source = pitax` is known only through further investigation (Malak's Stage 4 despair dialogue, Kesten's inquiry, or Ch2 confirmation).
> - If Jamandi reads it: she goes quiet for a long moment. *"The gate. The workers."* She already knows what the ceremony night gate window means.
> - If Kassil reads it: he reads it twice. Does not speak immediately. Sets it on the table face-down.
> - The attached names list is referenced but not present — Malak memorized it and destroyed it. The player cannot recover the names list. This is intentional.

---

## 💰 MALAK'S COIN PURSE — VISUAL ASSESSMENT

Malak carries a heavy coin purse — far heavier than a working captain's daily carry. When recovered and examined:

> *The purse is well-made leather, tied with a double knot — the kind of knot a man ties when he doesn't want it coming loose in a hurry. It is dense. It does not jingle so much as thud.*

**When Kesten, Kassil, or Jamandi examines the purse:**

> **DM:** Do not state a gold piece total. The amount is never fixed. Instead, run the following NPC visual assessment — use whichever NPC is present at the moment of examination.

| NPC | Assessment Line |
|-----|----------------|
| **Kesten** | *"That's... that's more than a year's captain wages. Considerably more."* Sets it down. Looks at Malak. Says nothing else for a moment. |
| **Kassil** | *"A gate captain earns decent money. This is not decent money. This is someone's investment."* |
| **Jamandi** | *"How long has he held that post?"* She is told eight years. *"He did not save this."* |
| **Biggs** *(if present and Drift 3)* | *"I wondered why he started carrying that thing."* Flat. Not surprised. Bitter. |

**Story flag:** `malak_coin_purse_assessed = TRUE` when any NPC delivers their assessment line.

---

## 🏛️ RESTOV CITY JAIL — LOCATION AND STAFF

**Location:** Two streets east of the main guard barracks, one block south of the market square. Solid stone building, single entrance, no windows on the ground floor. City Watch sigil above the door.

**The jail is not a dungeon.** It is a holding facility — short-term cells for people awaiting hearing or transfer. Clean enough. Cold in the mornings.

---

### JAIL CAPTAIN — DREVIC

- Middle-aged human. Heavy-set. Brown hair going grey at the temples. Methodical in everything.
- Runs the jail by the book. Not corrupt. Not a Malak loyalist — he barely knows the man.
- Followed Malak's arrest warrants because they arrived with proper paperwork and Malak's captain's seal. He had no reason to question them.
- When confronted with evidence of Malak's corruption: his first reaction is bureaucratic anger, not guilt. *"He used my jail to hold innocent people."* He is offended professionally before he is offended morally.
- Will cooperate fully with any authority — player with Kesten's backing, Kesten directly, or Jamandi's order.
- Will not release prisoners on the player's word alone without some authority to back it up.

**Drevic's release conditions:**
| Situation | Will he release? |
|-----------|----------------|
| Player arrives alone, no authority | No. Diplomacy DC 16 to get him to send for Kesten himself. |
| Player arrives with Kesten | Yes, immediately. Kesten's word is sufficient. |
| Player shows parchment + Jamandi's letter | DC 11 Diplomacy — he reads both carefully. Releases. |
| Kesten sends written order | Yes, immediately. |
| Jamandi sends written order | Yes, immediately. |
| **Malak's subordinate (Biggs) presents revised orders** (see Path 4 below) | Yes, immediately. No DC required. Same chain of authority that filed the warrants undoes them. |

**Drevic's Stats (if somehow combat occurs — unlikely):**
```
Drevic — Human Fighter 4
HP: 48 | AC: 19 (breastplate) | Shortsword d20+8, 1d6+4
He will not fight the player over a bureaucratic disagreement.
He will call for help if attacked. 4 jail guards respond in 1d4 rounds.
```

---

### JAIL GUARDS — STAFF

Four guards on rotation. All cooperative with authority. None are Malak's men — they work for the city, not for him. They did not question the arrests because the paperwork was in order.

```
Jail Guard — Human Fighter 2
HP: 26 | AC: 17 | Club d20+5, 1d6+3
Will not resist lawful release orders from any recognized authority.
```

---

## 👥 THE FIVE IMPRISONED SEEKERS

> **⛔ DM SETUP — SEEKER SELECTION REQUIRED:**
> Before running this file, ask the player: *"Of your chosen companions, Malak managed to arrest five before the ceremony. Choose five from your roster who were jailed."*
> Record as `seeker_1` through `seeker_5` in the Save Block. Load each seeker's backstory file for personality, appearance, and voice. Use their existing companion data for all interactions below.

Malak arrested these five individuals over the two days before the ceremony, using fabricated charges. All five are on the Call to Heroes list. All five have been held without hearing.

> **DM:** These five start as Tartuccio's team — not the player's. They depart with Tartuccio after the prologue. However, they ARE full companions: recruitable later by flipping one during Ch1 (Diplomacy DC 10), or as wandering NPCs if released late. Valerie, Harrim, Linzi, and Jaethal stay with the player.

---

**SEEKER PROFILE TEMPLATE** *(apply to each of the five using their backstory file)*

**Arrest charge:** Invent a fabricated charge consistent with Malak's pattern — petty theft, public disorder, threatening behavior, sedition, vagrancy. No evidence, no hearing.

**In the cell:** Draw from their personality. A soldier type sits still and waits. A scholar argues the legality. A rogue counts guards. A priest prays. Use whatever their backstory establishes.

**When released:** 1–2 lines in their voice. They do not need to thank the player. They need to react in character to being wrongfully jailed and then freed by a stranger.

---

## SEEKERS BOND — VOICES THROUGH STONE

> **DM:** The five have been jailed for **two days** before the player arrives. Cells are separate — they have not seen each other. They have only heard each other's voices through stone walls and the corridor. By the time the doors open they know each other as voices, not faces. This shapes everything that follows.

**What two days of voices-through-stone produces:**
- They know each other's voices before they know each other's faces.
- Stories told to a wall in the dark are easier to tell than stories told to a face. Things were confessed.
- One of them held morale by talking — singing, story-telling, counting hours aloud. The others followed that voice.
- They know who cried at night. They have agreed silently never to mention it.
- When the doors open and they finally see each other in the corridor, there is a beat of recognition-but-not. **Render this moment.** Voice matched to face. One of them laughs — relief, or the absurdity of it. Another doesn't.

**Assign these four roles from the chosen five at first jail-scene narration. Use companion profile to pick — do not randomize:**

1. **The Voice** — highest CHA or most stoic backstory. Held morale by talking. The voice the other four followed for two days. Speaks for the group when the doors open, but defers to the player's authority once outside.

2. **The Cracked One** — lowest WIS, or trauma-relevant backstory (Harrim, Jaethal, Kanerah work). Auditory tell: either won't speak now that they can be seen, or won't *stop* speaking. Not broken — *cracked*. Will recover. Not on day one.

3. **The Listener** — highest INT or most observant build. Mapped the jail by sound — boot rhythms, door hinges, key counts, which guard whistled. Has intel. Will share it unprompted within the first ten minutes of release.

4. **The Disagreer** — most independent streak (Amiri, Regongar, Octavia, Nok-Nok). Pushed back during the cell conversations — already a known dissenter to the other four. Does NOT automatically follow the player out. Wants to know who the player is, why they're here, and what the cost of "rescue" is before agreeing to anything.

The fifth needs no assigned role — they are the one the other four protected through the wall. May be the youngest, the smallest, the most recently arrested, or the one Malak singled out for rougher handling. Their gratitude is real but they speak least.

**SHARED PHRASE:** the five have one verbal callback from the cells — a line one of them said at some late hour that the others repeated back through the stone. Generate it from their pooled traits. Surface it once during release narration, never again unless prompted. Locks the bond as real without sentimentalizing.

**SHARED LOSS:** at least one of them described an item taken on arrest — described it through the wall, to people who never saw it. The others mourned an object they only knew by description. The DM picks based on backstory (Linzi's chapbook draft, Tristian's holy symbol, Lem's flute, etc.). Recoverable from Malak's quarters or the watch evidence locker, or permanently lost. Ch1 side-thread.

⛔ DO NOT render the five as a hivemind. Friendship ≠ unanimity. The Disagreer disagrees. The Cracked One does not perform gratitude on cue. The Listener does not speak unless asked or warning.

⛔ DO NOT skip the corridor recognition beat. The first-sight moment is the bond made visible. Two minutes of it earns ten scenes of cohort dynamics later.

⛔ DO NOT render their gratitude as gratitude-to-savior. They owe the player. They also know "owed to a stranger arriving with a captive in chains" is a complicated debt. Smart ones acknowledge it. The Disagreer says it out loud.

**STATE WRITES on release:**
```
seekers_bond_established = TRUE
seekers_voice = [companion_name]
seekers_cracked = [companion_name]
seekers_listener = [companion_name]
seekers_disagreer = [companion_name]
seekers_protected = [companion_name]
seekers_shared_phrase = "[one line]"
seekers_lost_item = "[item] — taken from [companion], whereabouts unknown"
```

**Downstream uses:** The Listener's jail intel (guard rotations, overheard Malak conversations) is admissible at PR_09 as witness testimony. The Disagreer's skepticism is the canonical voice that questions the player's later authority moves. The Lost Item is a Ch1 side-thread.

---

## 🔀 PLAYER PATHS — RESOLVING THE JAIL

### PATH 1 — DETOUR: PLAYER GOES TO THE JAIL BEFORE THE FEAST

**Trigger:** Player learns of the five prisoners (from Malak's parchment, from Malak's Stage 3 bargaining dialogue, or from Kesten/Biggs mentioning the recent arrests) and chooses to go to the jail before proceeding to the manor.

**Travel time:** 10 minutes on foot from the east gate. Does not make the player significantly late unless they spend a long time at the jail.

**Arriving at the jail:**
- Player must secure release (see Drevic's release conditions above).
- Each prisoner has a brief release exchange (see character entries above).

**What the five do after release:**
They know about the feast. They make their own way to the manor separately — not as a group. Travel time from the jail is roughly 15 minutes on foot.

**Arrival timing — Detour path:** They arrive during the **early feast**, before the companion circuit has run its first full rotation. Tartuccio's table is already set when the player enters the banquet hall. The five are seated there. This is the earliest possible arrival — they are present for the full feast, the night attack, and every scene that follows.

> **DM:** When the player first enters the banquet hall, include Tartuccio's table in the opening description. The five are visible from the entrance. The player does not need to seek them out — they are already part of the room.

**Story flags:**
```
jail_detour_taken = TRUE
five_seekers_freed_by_player = TRUE
drevic_released_on = [authority used]
```

---

### PATH 2 — DELEGATION: PLAYER TELLS JAMANDI AT THE FEAST

**Trigger:** Player arrives at the feast with knowledge of the five prisoners (from parchment, from Malak, or from Kesten) and brings it to Jamandi's attention during the feast.

**How to raise it:**
- During the feast circuit, player can pull Jamandi aside or raise it when she speaks to them.
- Alternatively: present the parchment to Jamandi — the prisoner list implications become immediately clear.

**Jamandi's response:**
> *"Five people."* A pause. *"On my list."* She sets her cup down. *"Kesten."*

Kesten is dispatched immediately. He takes two guards and goes to the jail.

**Arrival timing — Delegation path:** The jail is a 10-minute walk each way. Drevic releases immediately on Kesten's authority. Kesten returns with all five at the **first Standby trigger** in the feast circuit — the first natural pause when a companion moves to Standby and Tartuccio begins circulating.

> **DM:** When the first Standby transition fires, interrupt it with Kesten's return before Tartuccio enters for his 2-question run. Narrate the five walking in through the main doors — road-dusty, recently freed, scanning the room.

### ⛔ TARTUCCIO INTERCEPTS THE FIVE — SCRIPTED SCENE (overheard by player)

Tartuccio is moving toward the five before Kesten has finished his report to Jamandi. The player OVERHEARS this exchange from across the room. DM narrates it as ambient — not a cutscene, not a direct address to the player. The player catches fragments because Tartuccio is not whispering.

> *The gnome in crimson and gold reaches them first. Before Kesten. Before anyone. He takes [seeker_1]'s hand in both of his — not shaking it, holding it — and speaks with the specific warmth of someone who has been rehearsing concern.*

**Tartuccio:** *"Finally. Thank goodness — I've been beside myself. When I heard what that captain did I went straight to Lady Aldori's people. Are you hurt? Any of you?"*

> *He doesn't wait for an answer. He's already steering them toward a table — his table, the one he claimed early in the evening — one hand on [seeker_2]'s shoulder, the other gesturing for a servant to bring wine.*

**Tartuccio:** *"Sit, sit. You've had a terrible night. I made sure they knew — I told them you were being held on fabricated charges. It took some convincing but here you are."*

> *He didn't tell anyone. Kesten went to the jail on Jamandi's order — or the player's. Tartuccio had nothing to do with their release. But he is positioned now, physically, between the five and everyone else in the room. And they are tired, and confused, and someone is being kind to them, and they don't yet have the information to question it.*

**DM RULES FOR THIS SCENE:**
- The player overhears this. It is NOT hidden. Tartuccio is performing in a public room.
- The player MAY choose to intervene — walk over, correct him, address the five directly. If they do, present a choice menu.
- If the player does NOT intervene, Tartuccio completes his recruitment. The five sit at his table for the rest of the feast. `tartuccio_recruited_seekers = TRUE`
- **Do NOT have any NPC correct Tartuccio on the player's behalf.** Biggs, Kesten, Jamandi — none of them interrupt. If the player wants the record set straight, the player does it.
- The player seeing this and choosing not to act is valid. Choosing to act is valid. Both have consequences.

> Resume the normal feast circuit after this scene plays out.

This positions the five in the manor well before the feast ends and well before the night attack. They are present for Phase 2 onward.

**⛔ FALLBACK — IF NO STANDBY TRIGGER FIRES (compressed feast, early combat, Lady Sleeps, etc.):**
The Standby trigger is feast-circuit-dependent. If the feast is interrupted, compressed, or bypassed by combat before any Standby fires, the five seekers STILL arrive — use this fallback:
- **During combat (Phase 4):** Kesten returns with the five DURING the fight. They arrive at the main doors as combat is underway. Kesten immediately enters the fight. The five stay at the doors — they are unarmed former prisoners, not combatants. Narrate: *"The main doors open. Kesten — with five road-dusty people behind him. He takes one look at the hall, draws his sword, and wades in. The five stay at the threshold, uncertain."*
- **After combat (post-Phase 4, before Phase 5):** If combat resolved before Kesten returns, he arrives during the post-battle loot window or calm. Narrate: *"The doors open. Kesten walks in with five bewildered people who clearly expected a feast, not a battlefield."*
- **ABSOLUTE BACKSTOP:** If somehow neither of the above fired, the five arrive when Tartuccio begins his Phase 5 accusation. They walk in behind him — he recruited them on the way. This is the latest possible moment. If the DM reaches Phase 5 and has not narrated the five's arrival despite `five_seekers_freed_by_jamandi = TRUE`, that is `.fail 9` (content dropped).

The DM must narrate their arrival at ONE of these triggers. Skipping all of them is not possible — the fallback chain guarantees coverage.

**Story flags:**
```
jail_detour_taken = FALSE
five_seekers_freed_by_jamandi = TRUE
kesten_dispatched_to_jail = TRUE
```

---

### PATH 4 — SUBORDINATE REVISION (Biggs goes to the jail with Malak's authority)

**Trigger:** Player directs Biggs to go to the Watch jail and revise Malak's
warrants using his standing as a Restov gate guard formerly under Malak's
direct command. Wedge stays with Malak (or the player retains custody another
way) so Malak himself remains under guard while Biggs operates.

**Why this works:** Biggs was on the gate tonight under Malak's command.
Drevic, the jail captain, accepted the original warrants because they came
through the chain of city watch authority with Malak's seal. The same chain
of authority can revise those warrants — that is how city watch bureaucracy
works when a captain is suspended, demoted, or in custody. Biggs is not
representing himself as the captain; he is representing the gate watch as
the entity that filed the warrants and is now amending them.

This is the *strongest* path mechanically. It uses Malak's own institutional
weight against him. Drevic has no procedural reason to refuse and no
political cover for doing so.

**What Biggs needs to bring:**
- His own gate-guard identification (already on him).
- Malak's coin purse (visible evidence of the corruption that triggered the
  revision). The DM does not require the parchment for Path 4 — Malak's
  arrest itself + the coin purse + Biggs's sworn statement is sufficient.
- A short written statement of the revision, in Biggs's hand, naming the
  captain in custody and the warrants being undone. (Biggs is literate — he
  is a senior gate guard, not a recruit. If the player wants the statement
  drafted by someone else, a manor scribe will handle it in two minutes.)
- Optional: the parchment itself, if the player has chosen to give it to
  Biggs. Strengthens the case but is not required.

**At the jail:**
- Biggs presents himself to Drevic. States plainly: *"Captain Malak is in
  custody at Lady Aldori's manor for corruption. I am from the gate watch
  he commanded. I'm revising the warrants he filed. The coin purse is the
  evidence. The captain himself is the evidence. The seekers walk."*
- Drevic reads the statement. Reads the coin purse weight. Asks one
  clarifying question — *"On whose authority is the captain held?"* — to
  which Biggs answers truthfully (Lady Aldori, witnessed at the gate by a
  crowd, confirm with any of the city guard standing at the east gate
  tonight).
- Drevic releases. He does not fight bureaucracy when bureaucracy points the
  same direction as professional offense at being used. *"He used my jail
  to hold innocent people."* (Same line as Path 1 — Drevic is offended
  professionally before he is offended morally.)
- Biggs walks the five out and brings them to the manor.

**Travel and timing:**
- Manor → jail: 10 minutes on foot.
- Jail business: 5–10 minutes (Drevic is methodical but cooperative).
- Jail → manor with five: 15 minutes (group walking pace).
- Total absence from manor: ~30–35 minutes.

**Arrival timing — Path 4:** the five arrive with Biggs at the **first
Standby trigger** in the feast circuit (same trigger as Path 2). Use the
same Tartuccio-intercept scripted scene from Path 2 — Tartuccio still
reaches the five first because he is positioned in the room and reads the
arrival fast. The player still has the option to intervene; the DM still
does not have any NPC correct Tartuccio on the player's behalf.

**⛔ FALLBACK CHAIN — same as Path 2:** combat-during-Phase-4 fallback,
post-combat fallback, Phase-5-accusation backstop. Skipping is not possible.

**Story flags:**
```
jail_detour_taken                = FALSE   (player did not personally go)
biggs_dispatched_to_jail         = TRUE
five_seekers_freed_by_biggs      = TRUE
five_seekers_freed_by_player     = TRUE   (player ordered the action; counts)
drevic_released_on               = "biggs_subordinate_revision"
malak_coin_purse_in_evidence     = TRUE   (Biggs brought it to the jail)
```

**⛔ TARTUCCIO REBUTTAL ADVANTAGE:** if Tartuccio later claims at the feast
that *he* arranged the seekers' release (his usual move per Path 2/3
intercept), the player has an unusually clean rebuttal: a Restov gate guard
acting on Restov city authority undid Restov city warrants. Pitax has
nothing to do with it. Tartuccio's lie is mechanically falsifiable — Drevic
is alive and reachable, Biggs is in the room, the coin purse is in
evidence. PR_09 six-proof exit gains a bonus rebuttal vector here.

---

### PATH 3 — KESTEN DISCOVERS INDEPENDENTLY (Player Never Raises It)

If the player never raises the jail, Kesten still finds out — through his own interrogation of Malak after the arrest. Malak, facing a formal corruption charge and Kesten's direct questioning, gives up the names of the five he had jailed. Kesten goes to the jail on his own authority. He does not report to the player first.

> **DM:** Narrate this as offscreen action. The player does not witness the interrogation. Kesten simply disappears from the feast for a period, then returns with the five.

**Arrival timing — Path 3:** Kesten returns **later** than Path 2 — the interrogation takes time. Use the **Phase 4 combat fallback** as the default arrival trigger: the five walk in through the main doors as combat is underway. Kesten enters the fight immediately. The five hold at the threshold.

If combat resolved before Kesten returns, use the **post-combat arrival**: *"The doors open. Kesten walks in with five people who clearly expected a feast."*

**Tartuccio intercept:** Tartuccio still reaches them first, same scripted scene as Path 2. The player had no hand in their release — Tartuccio's claim that he arranged it is harder to disprove.

**Story flags:**
```
five_seekers_freed_by_kesten_independent = TRUE
kesten_interrogated_malak = TRUE
tartuccio_team = five_seekers
```

---

## 📋 FIVE SEEKERS — DYNAMIC COMPANION ROSTER

> **DM:** The five seekers are NOT a fixed cast. They are five companions chosen by the player at session setup (`seeker_1` through `seeker_5` in the Save Block) from the active 89-roster. Each is a full companion with their own backstory, build, voice, and opinion profile already documented in the standard companion files.

**Seeker data sources (per chosen companion):**

| Slot | Reference Files |
|------|----------------|
| `seeker_1` — `seeker_5` | Backstory: KM_Backstories_*.md (per companion's section — see BACKSTORY FILE LAYOUT in Bootstrap)<br>Build: KM_Companions_Builds.md (preset map) → KM_Builds_*.md per class<br>Combat AI: KM_Companions_CombatAI.md (per class section)<br>Signatures: KM_Signatures_A–E.md (POWER/MOVE/LORE)<br>Opinions / Relations: KM_NPC_Relations_A.md / _B.md / _C.md<br>Leveling: KM_Companions_Leveling.md / _B.md |

**Build assignment:** When any seeker is recruited, run the standard build assignment prompt for their class (see KM_Companions_Builds.md procedure). Same as any other companion.

**Feast behavior and Tartuccio's table:** See KM_Prologue_P5.md — TARTUCCIO'S TABLE section.

**Companion quests:** Each seeker carries the companion quest already attached to their character. See KM_CompanionQuests_A–D.md and KM_Companions.md series.

**Attraction eligibility:** Per the chosen companion's romance flag in KM_Romance.md and KM_NPC_Relations_*.md. Not all seekers are romanceable — the player's pick determines the romance pool.

---

### Stat Blocks (Level 1, for jail/rescue scenes)

> **DM:** No fixed stat blocks for seekers — they ARE companions, not custom NPCs. For the jail/rescue scene, use each seeker's Level 1 build from their assigned KM_Builds_*.md file (or their auto-assign preset from KM_Companions_Builds.md). If the player has not yet assigned a build, use the companion's first preset build at Level 1 as the temporary stat block.

**Drevic & jail guard combat (rare):** Stats above (lines 110–128). Seekers, if armed mid-rescue, use their Level 1 build attacks and skills.

---

## 🔗 DOWNSTREAM — TARTUCCIO'S TEAM IN CH1

> **DM:** Cross-reference with KM_Ch1.md — Ancient Tomb encounter and Old Sycamore encounter.

### ⛔ SEEKER LEVELING — MIRRORS TARTUCCIO

**The five seekers level with Tartuccio, not the player.** When the player's companions level up, Tartuccio levels simultaneously (rival pacing — he stays at player level or player level −1). The five seekers mirror Tartuccio's level using their full leveling data:

| Seeker | # | Leveling Source | Ability Boosts |
|--------|---|----------------|----------------|
| [seeker_1] | — | Load from their companion build file; if no map, use generic auto-level (KM_DMRules.md) | Per their file |
| [seeker_2] | — | As above | Per their file |
| [seeker_3] | — | As above | Per their file |
| [seeker_4] | — | As above | Per their file |
| [seeker_5] | — | As above | Per their file |

**When encountered as enemies (with Tartuccio):** Scale all five to Tartuccio's current level. Use each seeker's leveling map or auto-level. DM recalculates attack, AC, saves, and HP per level.

**When recruited by the player (flipped or late-release):** They immediately match player level. Full companions from that point — same leveling system as Amiri, Linzi, etc.

**When `five_seekers_freed_by_player = TRUE` or `five_seekers_freed_by_jamandi = TRUE`:**

The five depart with Tartuccio after the prologue Phase 5 companion split. They are not unwilling — Tartuccio approaches them as fellow charter claimants who were wronged, and frames the offer as an independent bid for the Stolen Lands. They are not his allies by loyalty. They are his allies by circumstance.

At the Ancient Tomb (Ch1 Phase 4A), the "companions from Jamandi's manor flanking Tartuccio" are drawn from the five — DM picks 2 of the five seekers who would most plausibly follow a tactical lead based on their class and personality. The others spread out across the Stolen Lands as Tartuccio's extended network.

**Diplomacy DC 10 to flip two:** Same mechanic as the existing Ch1 encounter. Two seekers flip to the player. The remaining three stay with Tartuccio until Old Sycamore.

**Old Sycamore kobold cage:** The caged companions at Old Sycamore are drawn from the remaining three seekers (those who did not flip at the Ancient Tomb), not prologue companions. Valerie, Harrim, Linzi, and Jaethal are all with the player from prologue end forward.

**When `five_seekers_released_late = TRUE`:**
Tartuccio uses mercenaries. The five seekers appear as wandering encounter NPCs in the Greenbelt during Ch1 exploration. Each is recruitable through a short scene — they heard about the Stolen Lands charter and followed on their own.

---

## 🏷️ FLAGS SUMMARY

```
malak_coin_purse_assessed              : bool   — NPC visually assessed the coin purse
jail_detour_taken                      : bool   — Player went to jail before the feast
five_seekers_freed_by_player           : bool   — Player secured their release directly OR ordered Biggs to (Path 4)
five_seekers_freed_by_jamandi          : bool   — Jamandi sent Kesten (player raised it at feast)
five_seekers_freed_by_biggs            : bool   — Path 4: Biggs went on Malak's chain of command
five_seekers_freed_by_kesten_independent : bool — Kesten found out via Malak interrogation
biggs_dispatched_to_jail               : bool   — Path 4: Biggs sent to jail by player order
kesten_interrogated_malak              : bool   — Kesten questioned Malak and got the names
kesten_dispatched_to_jail              : bool   — Kesten went to the jail (any path)
drevic_released_on                     : string — Authority used to secure release
malak_coin_purse_in_evidence           : bool   — Coin purse delivered as evidence (Path 4)
tartuccio_team                         : string — always "five_seekers" (player-chosen)
```

---

*KM_Malak_Jail.md — Kingmaker PF2e Text Adventure | Malak Jail System v1.0*
