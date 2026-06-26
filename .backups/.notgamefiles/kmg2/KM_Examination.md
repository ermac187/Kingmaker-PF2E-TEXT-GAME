# KINGMAKER — OBJECT EXAMINATION SYSTEM
## KM_Examination.md | Referenced by: KM_Commands_P2.md, KM_DMRules.md

> **DM:** When the player uses `.examine [object]` or describes examining something specific in the scene, this system governs the response. Object examination rewards curiosity with lore, hidden items, and Codex entries. It feeds the Scholarly disposition tag (KM_Dispositions.md).

---

## 📋 COMMAND

`.examine [object]` — Examine a specific object, surface, or detail in the current scene.

**Aliases:** `.look at [object]`, `.inspect [object]`, or natural language ("I examine the bookshelf", "I look at the stain on the floor")

---

## 🔍 EXAMINATION PROCEDURE

### Step 1 — Is the object in the scene?
- If the object was described in the Scene Brief, narration, or is a reasonable inference from the location: proceed.
- If the object was NOT described and is NOT a reasonable inference: "You don't see [object] here."
- **Do NOT invent objects.** If the player asks to examine something the files don't mention, it's not there.

### Step 2 — Determine examination tier

| Tier | DC | What It Reveals | Example |
|------|-----|----------------|---------|
| **Surface** | None (free) | Physical description: size, material, condition, visible markings | "The bookshelf is old oak, warped from damp. Three shelves. The bottom shelf is empty." |
| **Detail** | Perception DC 12 | Hidden features: scratches, stains, wear patterns, maker's marks | "The bottom shelf has drag marks — something heavy was moved recently." |
| **Lore** | Recall Knowledge DC 14 (relevant skill) | Historical, magical, or cultural significance | "The maker's mark is Aldori — this shelf was looted from a swordlord's estate." |
| **Secret** | Perception DC 18 or specific knowledge | Hidden compartments, concealed items, trapped mechanisms | "Behind a false panel: a folded map with three locations circled in red ink." |

### Step 3 — Output format
```
[EXAMINE — {Object Name}]
{Surface description — always shown}
{Detail — only if Perception check succeeds}
{Lore — only if Knowledge check succeeds}
{Secret — only if high Perception or player names the right spot}
```

### Step 4 — Tag and reward
- **+1 Scholarly** if the examination reveals Detail or Lore tier (not Surface alone)
- **Found Document:** If the object contains a readable document, add to `found_documents[]` in save block
- **Codex Entry:** If the lore is significant, add to player's Codex (KM_Glossary.md)
- **Hidden Item:** If Secret tier reveals an item, add to `pending_loot` — player must `.loot` to claim

---

## 🏠 SCENE OBJECT CATEGORIES

### Objects That Should Always Be Examinable

| Location Type | Default Examinable Objects |
|---------------|--------------------------|
| **Throne Room** | Throne, tapestries, windows, advisory table, floor stones, fireplace |
| **Tavern/Inn** | Bar counter, notice board, fireplace, kegs, patron belongings (if visible) |
| **Dungeon** | Walls (for moisture/carvings), doors (for mechanisms), floor (for tracks), ceiling (for drips/creatures) |
| **Camp** | Campfire (coals, fuel type), bedrolls (arrangement), perimeter (tracks, disturbances), sky (weather signs) |
| **Market** | Stalls (specific wares), carts (origins), vendor equipment (quality tells) |
| **Wilderness** | Trees (age, carvings), rocks (mineral type), water (clarity, flow), animal signs (tracks, scat) |
| **Battle Aftermath** | Bodies (equipment, insignia, wounds), ground (blood patterns, footprints), dropped items |

### Objects That Should NEVER Be Examinable (Fabrication Risk)
- Objects the player names that are not in the scene files
- NPC body parts or intimate details (redirect to Perception check for tells)
- Items inside locked/sealed containers the player hasn't opened
- Anything that would reveal DM-only information without a check

---

## 📖 LORE QUALITY STANDARDS

**Good examination lore:**
- Connects to something the player has seen or will see
- Reveals one specific fact, not a summary
- Creates a question the player might follow up on
- Is short: 1-3 sentences maximum

**Bad examination lore:**
- Generic flavor with no game connection ("It's an old bookshelf")
- Dumps paragraphs of history unprompted
- Reveals answers to active mysteries without a check
- Tells the player what to do with the information

---

## ⚠️ DM RULES

1. **Examination is free action in Exploration mode.** No action cost. The player is curious — reward it.
2. **In Combat:** Examining an object costs 1 action (Seek action variant). Perception check applies.
3. **Repeat examinations:** If the player examines the same object twice, give them the same info. Do NOT invent new details to fill the second look.
4. **Companion assist:** If a companion has a relevant skill (Medicine for wounds, Crafting for weapons, Religion for holy symbols), they can assist — use their modifier instead if higher.
5. **Chain examinations:** If examining object A reveals object B, the player can examine B immediately. This is how multi-step discovery works.
6. **Scene files override this file.** If a chapter file specifies what examining a specific object reveals, use that text, not generated content.

---

## 📋 CHAPTER-SPECIFIC EXAMINABLE OBJECTS WITH LORE PAYOFFS

### PROLOGUE — Jamandi's Manor

| Object | Location | Surface (free) | Detail (Perc DC 12) | Lore (Know DC 14) | Secret (Perc DC 18) |
|--------|----------|----------------|---------------------|--------------------|--------------------|
| Jamandi's sword | Banquet hall, on display | Aldori dueling blade, well-used | The edge has been resharpened hundreds of times — this is not ceremonial | Aldori Swordlords train from age 7. This blade has 40+ years of muscle memory in its wear | Hidden inscription on the pommel: a name. Not Jamandi's. |
| The feast wine | Any table | Red, Rostland vintage, served in silver | Faint residue on the rim — slightly cloudy | Paralytic agent. Tasteless. Takes 10 minutes to take effect. | The serving staff didn't pour from the same casks — kitchen staff used a different barrel. |
| Tartuccio's ring | If given to player | Gold, ornate, warm to the touch | Faint arcane aura. Not dangerous — but not simple jewelry | Tracking enchantment. Low-power. Someone wants to know where the wearer goes. | The maker's mark is Pitaxian. Tiny, inside the band. |
| Manor walls | Any corridor | Thick stone. Old construction. Aldori banners. | Scratches on the floor — furniture has been moved recently to create choke points | The manor was built as a fortress first. The feast hall was an armory. | Behind one banner: a sealed passage (leads to secret room). |

### CHAPTER 1 — The Stolen Lands

| Object | Location | Surface | Detail (DC 12) | Lore (DC 14) | Secret (DC 18) |
|--------|----------|---------|----------------|-------------|----------------|
| Oleg's palisade | Oleg's Trading Post | Wooden walls, recently reinforced | The reinforcement is amateur — Oleg did this himself | This was originally a Brevic border checkpoint. The foundation stones have garrison markings. | A buried cache under the south wall: 50 gp + a map fragment (hex reveal). |
| Stag Lord's helmet | Stag Lord's Fort | Antlered helm, crude | The antlers are real — grafted onto a metal frame | Pre-dates the Stag Lord by centuries. This was a religious artifact repurposed as armor. | Fey-touched. Detect Magic: faint transmutation. The antlers grow 1mm per year. |
| Old Sycamore tree | Old Sycamore hex | Massive, ancient, hollow | The trunk has been carved — tunnels inside are shaped, not natural | First World thin spot. The tree exists partially in both planes. | At midnight, the tree hums. Nature DC 16: it's communicating with something underground. |
| Tartuccio's journal | Old Sycamore, after defeat | Leather-bound, coded entries | The code is simple substitution cipher. Decryptable with Linguistics DC 12 or 10 minutes. | Contents: payment records, contact descriptions, references to "P." (Pitax) | A page torn out. The torn edge has blood on it. Not Tartuccio's blood type. |

### CHAPTER 2-3 — Kingdom Building

| Object | Location | Surface | Detail (DC 14) | Lore (DC 16) | Secret (DC 20) |
|--------|----------|---------|----------------|-------------|----------------|
| Throne (when built) | Capital throne room | Whatever materials the player chose | The craftsmanship reflects who built it — dwarven joints, elven filigree, or rough frontier carpentry | A throne is a symbol before it's furniture. The first ruler to sit in it defines what it means. | If eRmaC's Aerynth armor contacts the throne: faint resonance. The materials recognize each other across worlds. |
| Bloom roses | Any Bloom hex | Beautiful. Wrong colors. Sweet smell with decay undertone | The petals are warm. Plants shouldn't be warm. | First World corruption. Not natural growth — forced manifestation. Something is pushing reality aside. | The roots go deeper than any plant's should. They're not feeding on soil. They're feeding on the boundary between planes. |
| Kingdom banner | Capital or army | Whatever the player designed | The fabric is mundane. The symbol is not — people react to it before they read it. | Symbols acquire power through association. This one is acquiring it fast. | Merchants from other kingdoms have started copying the design. Imitation is the first stage of cultural influence. |

---

## ⚠️ DM RULES

1. **Examination is free action in Exploration.** In Combat: 1 action (Seek).
2. **Repeat examinations:** Same info. Do NOT invent new details.
3. **Companion assist:** Use their modifier if higher.
4. **Chain examinations:** Examining A reveals B → player can examine B immediately.
5. **Scene files override this file.**
6. **These tables are EXAMPLES.** DM generates examination results for objects not listed here using the same tier system (Surface/Detail/Lore/Secret).

**Save block:** Examination discoveries feed into `found_documents[]` and Codex entries.

---

*KM_Examination.md — Kingmaker PF2e Text Adventure | Object Examination System v2.0*
*Rules + chapter-specific examination tables with lore payoffs.*
