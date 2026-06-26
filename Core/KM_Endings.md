# KINGMAKER — SECRET & ALTERNATE ENDINGS
## KM_Endings.md | Split from KM_Mythic_Systems.md (v95.9 file-size remediation, 2026-05-29)

<!-- merged from KM_Endings.md (v93.21 file consolidation) -->

# KINGMAKER — SECRET & ALTERNATE ENDINGS
## KM_Endings.md | Active from: Chapter 6 (final chapter) | Referenced by: KM_MythicPaths.md

> **DM:** The game has 5 ending variants based on accumulated flags. The DM tracks ending eligibility silently — the player doesn't know which ending they're building toward until the final scenes unfold. Each ending requires a flag checklist. Check at the start of Chapter 6.

---

## 🏆 ENDING VARIANTS

### ENDING 1 — THE RULER'S ENDING (Default)
*The kingdom survives. The Bloom is stopped. Nyrissa is destroyed. The Stolen Lands endure under eRmaC's rule.*

**Requirements:** None (this is the default if no other ending's flags are met).

**Final scene:** Throne room. The kingdom stretches before you. The Bloom is gone. Nyrissa is gone. What you built remains.

---

### ENDING 2 — THE TRUE ENDING (Save Nyrissa)
*Nyrissa's capacity to love is restored. The Bloom dissolves. The Lantern King's curse is broken.*

**Requirements (ALL must be TRUE):**
- [ ] `nyrissa_saveable ≥ 3` (from dream choices in KM_Dreams.md)
- [ ] `nyrissa_backstory_known ≥ 4` (from scripted interactions and dream sequences)
- [ ] `true_ending_path = TRUE` (from Dream D7)
- [ ] `merciful ≥ 5` (disposition tag)
- [ ] Mythic Path = Fey Champion OR First World Sovereign
- [ ] Player physically finds the "briar" (Nyrissa's love) in the final dungeon

**Final scene:** The briar — a thorn that contains everything Nyrissa lost — is returned to her. She remembers. The Bloom dies. The Lantern King screams from a dimension away. Nyrissa is not the same person she was before the curse. She is something new. Whether she stays is her choice.

---

### ENDING 3 — THE GOLDEN ENDING (Perfect Kingdom + Save Nyrissa)
*Everything you could save, you saved. Everything you could build, you built.*

**Requirements (ALL of True Ending PLUS):**
- [ ] Kingdom Size ≥ 25
- [ ] Unrest ≤ 3 at chapter 6 start
- [ ] All 12 CRPG companions alive and in kingdom
- [ ] No companion at Hostile relationship
- [ ] `scholarly ≥ 5` AND `merciful ≥ 5`
- [ ] `golden_ending_eligible = TRUE` (from Dream D7, option 4)
- [ ] Faction reputation ≥ Honored with at least 2 factions
- [ ] Zero unanswered border raids

**Final scene:** As the True Ending — but the kingdom also transforms. The Stolen Lands were never stolen. They were waiting. The First World boundary thins into permanence: a place where both worlds coexist. The companions each find what they were looking for. Nyrissa plants a garden that grows real flowers.

---

### ENDING 4 — THE CONQUEST ENDING (Domination)
*The kingdom survives through absolute force. Enemies are destroyed, not redeemed.*

**Requirements:**
- [ ] Mythic Path = Sword Saint
- [ ] `ruthless ≥ 7`
- [ ] All enemy factions at Hostile or destroyed
- [ ] Nyrissa destroyed (not saved)
- [ ] Army victories ≥ 5

**Final scene:** The throne room is full of trophies. Pitax's banner hangs inverted. Armag's sword is mounted above the throne. The Stolen Lands are no longer stolen — they are conquered. Nobody challenges eRmaC. Nobody dares. The question the ending doesn't answer: is this what you wanted?

---

### ENDING 5 — THE TRANSCENDENCE ENDING (Between Worlds)
*eRmaC understands why they crossed from Aerynth. The answer was never the kingdom.*

**Requirements:**
- [ ] Mythic Path = Shadow Walker
- [ ] `scholarly ≥ 7` OR `cunning ≥ 7`
- [ ] `nyrissa_backstory_known ≥ 3`
- [ ] Player examined ≥ 10 objects across the campaign (KM_Examination.md tracking)
- [ ] Found the Aerynth artifact (quest item in Ch5)

**Final scene:** The portal network you built reveals its purpose — not military logistics, but a map. A map of every world connected to the space between. Aerynth. Golarion. Others. You stand at the bridge. The kingdom continues — your companions, your advisors, your people will carry it forward. But you were never meant to stay. The question is: do you step through? (Player choice: Stay or Go. Both are valid endings.)

---

## 📋 ENDING CHECK — CHAPTER 6 OPENING

At the start of Chapter 6, the DM checks all ending flags silently:

```
[DM INTERNAL — ENDING ELIGIBILITY CHECK]
Ending 2 (True):    [X conditions met / Y total] — {eligible/not eligible}
Ending 3 (Golden):  [X conditions met / Y total] — {eligible/not eligible}
Ending 4 (Conquest): [X conditions met / Y total] — {eligible/not eligible}
Ending 5 (Transcendence): [X conditions met / Y total] — {eligible/not eligible}

Highest eligible ending: {N} — track remaining conditions
If no special ending eligible: Default Ending 1
```

**Do NOT reveal to the player.** The ending unfolds naturally based on their final chapter choices.

---

---

## 📜 ENDING NARRATION — SCRIPTED TEXT

> **⛔ Read these EXACTLY when the ending fires. Do not improvise endings.**

### ENDING 1 NARRATION — THE RULER'S ENDING

> *The Bloom dies the way a fire dies — not all at once, but in patches, retreating from the edges inward until there is nothing left to consume. Where it touched the land, scars remain: circles of dead earth, trees bent at angles that will never straighten, water that tastes of roses for a generation.*

> *Nyrissa is gone. Whether she was destroyed or simply ceased — the distinction matters to scholars, not to the people pulling weeds from their fields. The Lantern King's laughter fades to an echo, then to a memory, then to a story parents tell children who won't sleep.*

> *You stand in a throne room you built with choices. Every stone was a decision. Every corridor was a consequence. The kingdom stretches before you — imperfect, scarred, alive.*

> *The Stolen Lands are no longer stolen. They are yours. What you do with them is the only story left to tell.*

### ENDING 2 NARRATION — THE TRUE ENDING

> *The briar is small — a thorn no longer than your thumb. It weighs nothing. It contains everything Nyrissa lost.*

> *You place it in her hand. She closes her fingers around it and goes still — the kind of still that precedes either collapse or transformation. For three heartbeats, nothing happens.*

> *Then she opens her eyes. They are different. Not the color — the depth. Something that was absent is present. Something that was mechanical is alive.*

> *"I remember," she says. Not what she remembers. Just that she can.*

> *The Bloom doesn't die — it dissolves. Not retreating. Releasing. As if it was holding its breath for a thousand years and Nyrissa just exhaled.*

> *The Lantern King screams from a dimension away. It is the sound of a game ending that was never supposed to end. He will not forget. But today, he lost.*

### ENDING 4 NARRATION — THE CONQUEST ENDING

> *The throne room is full of trophies. Pitax's banner hangs inverted above the door. Armag's sword is mounted above your seat — not a decoration, a warning. The crown sits heavy, and you have learned that this is what crowns do.*

> *Nobody challenges you. The roads are safe because the consequences of unsafe roads are known. The fields are tended because the alternative is clear. Justice is swift, and if it is sometimes harsh, it is never arbitrary. You promised order. You delivered it.*

> *Your companions stand where they chose to stand — some close, some at the edges, some gone entirely. The ones who remain did so with open eyes.*

> *The Stolen Lands are no longer stolen. They are conquered. History will record you as the ruler who tamed them. Whether that is a compliment depends on who is writing.*

### ENDING 5 NARRATION — THE TRANSCENDENCE ENDING

> *The portal network hums — a sound below hearing, felt in the teeth and the chest. You built it for logistics. It became something else.*

> *Standing at the central node, you can see them: threads connecting worlds. Aerynth — distant, broken, the place you came from. Golarion — close, scarred, the place you built something in. And others. Unnamed. Waiting.*

> *Your companions are here. Your kingdom is here. Both will continue without you — not because they don't need you, but because you built them to survive. That was the point. You just didn't know it was the point until now.*

> *The question is simple: stay or go.*

> *If you stay: the portal closes. You are a ruler. The kingdom is your answer.*

> *If you go: the kingdom continues. Your companions carry what you taught them. And you step onto a bridge between worlds that no one has walked before, toward an answer to a question you have carried since Aerynth — why you, why here, why now.*

> *Either choice is the right one. That is the last thing the Stolen Lands taught you.*

---

## 📊 COMPANION EPILOGUES

After the ending narration, the DM presents a brief epilogue for each companion based on their final relationship, quest completion, and choices made:

| Companion | Devoted Epilogue | Hostile Epilogue |
|-----------|-----------------|-----------------|
| **Amiri** | Stays. Becomes the kingdom's war chief. Never stops fighting. Never stops choosing to. | Leaves. Returns to the wilds. Heard of occasionally — a woman with an oversized sword, still running. |
| **Linzi** | Publishes the chronicle. It becomes the definitive account. She stays to write the sequel. | Publishes a different version. Less flattering. More honest. She calls it a warning. |
| **Leliana** *(if chronicler-mode)* | Lived (quest complete): performs the finished Verse at the founding — it becomes the kingdom's anthem; if romanced, she names it for the player and plays it "until I can't." Died (quest complete): the party performs the final movement from the Ballad Cycle, dedicated to the expedition. | The Verse stays unnamed and unfinished. The Ballad Cycle is shelved, unperformed — a kingdom that owns the songs and never plays them. If she died estranged, a single unsigned page is all that survives, and no one is certain it was hers. |
| **Valerie** | Founds a new knightly order. Not Shelyn's. Hers. | Returns to Brevoy. The Order takes her back. She never speaks of the Stolen Lands. |
| **Tristian** | Builds a cathedral in the capital. It faces east. He is at peace. | Wanders. Seeking redemption in places that don't know his name. |
| **Jaethal** | Remains. Undying sentinel of the kingdom. She has found her purpose in service. | Disappears. The undead do not leave trails. Years later, rumors from the south. |
| **Regongar** | Commands the army. Fights with controlled fury. He learned it from you. | Burns something. Starts over. Octavia goes with him or she doesn't. |
| **Octavia** | Runs the academy. Freedom is no longer a dream — it's curriculum. | Returns to her network. The liberation work continues, just not here. |

**DM Rule:** Keep epilogues to 2-3 sentences each. The player has been playing for hours. End clean.

---

## ⚠️ DM RULES

1. **The player does NOT choose an ending from a menu.** Endings emerge from accumulated flags.
2. **Multiple endings can be eligible.** The one that fires depends on the player's final choices in Ch6.
3. **Ending 3 (Golden) is deliberately hard.** It requires near-perfect play across all systems. Use Ending 2 narration + append the Golden paragraph below:

> *And then — something none of them expected. The boundary between worlds thins. Not breaks — thins. The First World and Golarion overlap here, in this kingdom, in this place. Real flowers grow next to fey flowers. The seasons make sense and also don't. Animals speak, sometimes, if you catch them at the right moment. It is strange. It is beautiful. It is the only place on either plane where both worlds chose to coexist.*

> *Nyrissa plants a garden. It grows real roses.*

4. **Ending 5 (Transcendence) is the lore ending.** It answers why eRmaC is from Aerynth.
5. **After the ending:** Output companion epilogues, then the final save block with `"ending": "{ending_name}"`.

**Save block:** `"ending_flags": { "nyrissa_saveable": 0, "true_ending_path": false, "golden_ending_eligible": false, "conquest_eligible": false, "transcendence_eligible": false }`

---

*KM_Endings.md — Kingmaker PF2e Text Adventure | Secret & Alternate Endings v2.0*
*5 endings with full scripted narration + companion epilogues.*
