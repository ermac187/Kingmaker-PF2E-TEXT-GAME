# KINGMAKER — PROLOGUE PART 5: TARTUCCIO'S TABLE (FEAST BEHAVIOR)
## KM_Prologue_P5.md | Companion file to: KM_Prologue.md (Phase 1)

> **DM:** Load this file alongside KM_Prologue.md. Despite the P5 filename, this content runs during **Phase 1 (the feast)** — it was split out of KM_Prologue_P3.md for size management. The Tartuccio departure narration referenced from Phase 5 is at the bottom of this file.

---

## 🍽️ TARTUCCIO'S TABLE — FEAST BEHAVIOR

> **DM:** Run this section alongside KM_Prologue.md Phase 1 (the feast). Tartuccio is a social butterfly but his table is his power base. Run this in parallel with the feast companion circuit — he circulates, but he always comes back.

---

### The Table

Tartuccio has claimed a corner table — not the best table, not the worst. Strategically positioned: visible from most of the hall, close enough to the main floor to circulate, far enough to be a destination rather than a waypoint. The five seekers he recruited from Restov's jail sit there.

> **DM:** The five are present at the feast ONLY if `five_seekers_freed_by_player = TRUE` or `five_seekers_freed_by_jamandi = TRUE`. If `five_seekers_released_late = TRUE`, the table exists but holds only Tartuccio and 2 hired sell-swords. Adjust narration accordingly.

**The table arrangement:**

| Seat | Companion | Behavior at the Table |
|------|-----------|----------------------|
| Head | **Tartuccio** | Rarely sitting. Present in passing. Returns often. |
| Left | **[seeker_1]** | Per their personality from backstory file. |
| Beside seeker_1 | **[seeker_2]** | Per their personality from backstory file. |
| Right | **[seeker_3]** | Per their personality from backstory file. |
| Beside seeker_3 | **[seeker_4]** | Per their personality from backstory file. |
| End | **[seeker_5]** | Per their personality from backstory file. |

---

### Why They Follow Tartuccio

These five were arrested, held without hearing, and released the night of the ceremony — either by the player's intervention or Jamandi's. Tartuccio found them first.

He did not promise them glory. He told them the truth: that they were targeted specifically, that the conspiracy that jailed them runs deeper than a single corrupt guard captain, and that Jamandi's charter gives him — and by extension them — a legal foothold in the Stolen Lands to operate from. He positioned himself as the only person who understood what was done to them and had a plan to do something about it.

He is not wrong about most of this. That is what makes him effective.

> **DM — Tartuccio's pitch to each seeker (for reference, not output):**
> Tartuccio tailors his pitch to each seeker's motivation. Read their backstory file. What do they want? He offers exactly that framed as something the Stolen Lands — and by extension he — can provide. Each pitch lands because it is specific. This is Tartuccio at his most capable.

---

### His Social Butterfly Pattern

Tartuccio circulates the feast in a specific rhythm — the STANDBY trigger mechanic in KM_Prologue.md already governs when he approaches the player's group. Between those appearances, he is working the room.

**His circuit:** Main floor greeting → Jamandi's table (brief, cordial) → player's orbit (2 questions, then exit) → back to his table. Repeat.

**At his table between circuits:** He is genuinely warm with these five. He engages each one on their own terms — matching their energy, not imposing his. This is not performance — or if it is, it is very good performance. The five have decided to trust him and he is not, in this moment, giving them reason to stop.

**His popularity is real within this group.** The feast hall as a whole finds him entertaining. His table finds him reliable. These are different things and he knows it.

---

### Player Can Observe This

The player may visit Tartuccio's table during the feast. This is not a combat scene. It is a social scene.

**If player approaches the table:**
- Tartuccio welcomes them with visible pleasure — genuine or performed, impossible to tell.
- Each seeker responds per their personality from their backstory file.
- A seeker with a lore/investigative bent may ask about the parchment if the player has it.
- A seeker with a martial/tactical bent may ask what happened at the gate if `malak_arrested = TRUE` or `malak_bribe_evidence = TRUE`.
- Quiet or cautious seekers watch the player assess the room without commenting.

**Observation without approaching (Perception DC 13):**
> *Tartuccio's table has a particular quality to it — five people who were in a jail cell three hours ago, now sitting at a feast. They are not relaxed. They are watching. The empty chair at the head belongs to the gnome who is currently working the room, but the five arranged around it have already, without being asked, picked the angles that cover the door.*

---

### Tartuccio Departure — Updated Narration

> **DM:** Replace the existing "Tartuccio gathers the 2 companions" line in Phase 5 with the following. Check `tartuccio_team` flag first. (Cross-referenced from KM_Prologue_P3.md Phase 5 § Tartuccio Departs.)

**If `tartuccio_team = five_seekers`:**
> *Tartuccio gathers his table. They move efficiently — five people who have already been through worse tonight, and who do not need to be told twice. Tartuccio pauses at the door.*

**If `tartuccio_team = mercenaries`:**
> *Tartuccio gathers two hired men in travel gear who have been standing by the far wall all evening. He pauses at the door.*

**In both cases, Tartuccio's exit line:**
**Tartuccio:** *"Well. This has been instructive. I look forward to seeing what you build, [character name]. I'll be building something too."*

> *He smiles — not pleasantly — and leaves.*

---

*KM_Prologue_P5.md — Kingmaker PF2e Text Adventure | Prologue v1.0*
*Split from KM_Prologue_P3.md for size management (2026-04-21).*
