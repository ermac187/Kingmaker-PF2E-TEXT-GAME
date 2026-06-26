# KINGMAKER — TRAVEL SEGMENT SYSTEM
## KM_TravelSegments.md | Active from: Pre-Prologue onward | Referenced by: KM_Exploration.md

> **DM:** Load this file whenever the party begins any overland journey. It replaces day-level
> travel summaries with segment-by-segment narration — each segment is a natural pause where
> companions can talk, the player can ask questions, and the world passes by.
> Segment count is determined by distance and travel mode. Never summarize a multi-segment
> journey in one paragraph. Each segment is its own scene beat.

---

## 🚶 TRAVEL MODES

| Mode | Miles/Day | Segments/Day | Miles/Segment | Notes |
|------|-----------|--------------|---------------|-------|
| **On foot** | 15 mi | 3 | 5 mi | Morning · Midday · Afternoon |
| **Horseback** | 30 mi | 3 | 10 mi | Faster; no foraging while mounted |
| **Carriage/Wagon** | 25 mi | 3 | ~8 mi | Comfortable; can converse freely; cargo |
| **Hustle (foot)** | 24 mi | 3 | 8 mi | Party gains Fatigued at end of day |

> **Segment count formula:** `CEIL( distance_miles ÷ miles_per_segment ) = total segments`
> The final segment ends with arrival at the destination, not a camp.

---

## 📍 SEGMENT DISPLAY FORMAT

Output this header at the start of each segment, then narrate the scene:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JOURNEY: [Origin] → [Destination]
Mode   : [On foot / Horseback / Carriage]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Segment           : [X] of [Y]
Distance traveled : [X × miles_per_segment] miles
Distance remaining: ~[total − traveled] miles
Terrain           : [Plains / Forest / Hills / etc.]
Time of day       : [Morning / Midday / Afternoon]
Weather           : [Current condition]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎲 SEGMENT EVENTS

Each segment gets **one event** drawn from the priority list below. DM picks based on
context (what companions are present, current story flags, terrain):

| Priority | Event Type | Trigger |
|----------|-----------|---------|
| 1 | **Companion banter** | Fire one banter from KM_Companions_Banter.md; tone-match to terrain/mood |
| 2 | **Landmark / scenery** | Named waypoint for this route (see named routes below) |
| 3 | **Conversation opportunity** | Player can ask a companion an open question — DM uses "Waiting for you to speak first" |
| 4 | **Minor encounter** | Roll d20; on 1–3 fire a random encounter appropriate to terrain and zone |
| 5 | **Discovery** | On a 1 in 6: the party spots something small — tracks, a cairn, a lost item, smoke in the distance |

> Each companion should fire banter no more than once per 3 segments on the same journey
> (prevent same companion dominating). Rotate through active party.

**Conversation opportunity** — script:
```
The road stretches on. [Companion name] rides/walks alongside you.
No one speaks for a stretch. The silence is comfortable — or almost.
```
Then pause for player input. Accept any question to a companion, discussion of current quest,
lore questions ("what do you know about X"), or just quiet travel. DM responds in character.

---

## 📋 SEGMENT CHOICE MENU

After each segment event, present 3–4 options (not a full menu — keep it quick):

```
  [1] Press on → next segment
  [2] Talk to [most active companion] about [context-appropriate topic]
  [3] Make camp here (if afternoon segment and party is tired or supplies are low)
  [4] Scout ahead (Perception/Survival DC 15 — reveals next segment terrain or nearby encounter)
```

> Option 3 only if the party has camped less than required for this day's travel.
> Option 4 costs no time; result applies to the NEXT segment only.

---

## 🗺️ NAMED ROUTES

Named routes have pre-written segment waypoints. DM reads them in order.
**Do NOT fabricate waypoints — use the list below. If the route is not listed, use generic
terrain description from KM_Map.md and fire companion banter as the primary segment event.**

---

### ROUTE A — Restov → Oleg's Trading Post
**Distance:** ~36 miles | **Road:** South Merchant Road (packed earth, maintained)
**Terrain:** Rostland Plains → northern Greenbelt edge

| Mode | Segments | Travel time |
|------|----------|-------------|
| On foot | 8 segments (~3 days) | Day 1: seg 1–3 · Day 2: seg 4–6 · Day 3: seg 7–8 + arrival |
| Horseback | 4 segments (~1.5 days) | Day 1: seg 1–3 · Day 2: seg 4 + arrival |
| Carriage | 5 segments (~2 days) | Day 1: seg 1–3 · Day 2: seg 4–5 + arrival |

**Segment Waypoints:**

```
SEG 1 — RESTOV SOUTH GATE (Mile 0–5/10)
  The city falls behind you. South Gate's twin towers shrink. The road here is still
  cobbled — merchants' carts have worn the stones smooth. Farmsteads to either side,
  grain fields, the smell of bread from a roadside mill. The last city smells.
  ► Banter opportunity: First-day energy. Characters settling in for the journey.

SEG 2 — ROSTLAND FARMS (Mile 10–15/20)
  The cobbles end. Packed earth now, wide enough for two wagons to pass. Scattered
  farmsteads, hedgerows, old stone walls dividing fields. A shepherd waves from a hill.
  The sky is wide in a way it never is in the city. Distant smoke: a farmhouse chimney.
  ► Landmark: The old milestone marker — cracked, still readable. "XII leagues to Restov."
  ► Banter opportunity: Open road. Companions comment on the quiet or the frontier.

SEG 3 — THE LAST FARMS (Mile 15–21/30)
  The farmsteads thin. The last one is shuttered — boards over the windows, no smoke.
  A burned fence post. Old trouble, or recent? The road continues south but the
  maintained sections end here. Beyond this point: untended country.
  ► Discovery check: DC 14 Perception — fresh wagon tracks, recent but abandoned.
  ► Banter opportunity: The shift from Rostland to the Greenbelt edge. Mood changes.

SEG 4 — OPEN PLAINS (Mile 21–26/30)
  Grassland to the horizon. The road is a suggestion here — a worn trail through tall
  yellow grass. Wind moves in long waves. No structures in sight. A hawk circles
  something to the east. The sky has gotten bigger.
  ► Random encounter check: roll d20, encounter on 1–4 (open road, low zone).
  ► Banter opportunity: The open country. Companions are more relaxed or more alert
    depending on personality.

SEG 5 — GREENBELT EDGE (Mile 26–30/36)
  The first trees appear on the southern horizon, then alongside the road. The grass is
  taller, the trail narrower. The air smells different — earth, pine, something wilder.
  This is the Greenbelt. The charter is no longer abstract.
  ► Landmark: A weathered signpost. "OLEGS — 6 MI." The wood is old; someone keeps
    repainting it. Oleg, probably.
  ► Banter opportunity: The Greenbelt. Companions who know it have something to say.
    Companions who don't might ask someone who does.

SEG 6 — NORTHERN GREENBELT ROAD (Mile 30–36)
  The road deteriorates to two ruts in the grass, but it's clear enough. Old campfire
  rings along the verge — travelers use this stretch regularly. Thinning trees to the
  left. The sky ahead is unobstructed. Something on the horizon: a low structure, walls.
  ► Discovery: DC 12 Perception — boot prints in the mud, several sets, going south.
    Travelers or bandits? Fresh, maybe a day old.
  ► Banter opportunity: Almost there. Anticipation. First sight of something built.

SEG 7 — OLEG'S IN SIGHT (Foot only — final push)
  The trading post resolves from a smudge on the horizon into something real. A converted
  border fort: stone walls, a wooden gatehouse, smoke from inside. Smaller than expected.
  More isolated. A flag — Oleg's own, not Restov's.
  ► Banter opportunity: Companions who know Oleg's have memories. Others have questions.

SEG 8 → ARRIVAL
  The gate is closed but not barred. A voice from above: *"Who's there?"* — suspicious,
  then cautious, then something that might become welcome. The journey is over.
```

---

## 🐴 MOUNTS & TRAVEL SPEED

Horses bought at Oleg's Trading Post reduce segment count and total travel time.
See **KM_Olegs.md § HORSES & MOUNTS** for purchase and rental prices.

**Mounted travel rules:**
- Foraging during travel is not possible while mounted (no time to stop and search)
- Horses require 10 lbs of feed per day (Oleg sells feed; forage in grassland hexes with
  Survival DC 12)
- A horse cannot enter Deep Forest or Mountain hexes at travel speed (reduce to foot pace)
- In combat: horse is a separate creature with its own AC (13), HP (32), Speed 50
- If a horse is killed in combat: party member is Prone and must make DC 14 Acrobatics or
  take 1d6 bludgeoning damage from the fall

---

## 📐 GENERIC JOURNEY SEGMENTS (for unlisted routes)

When the party travels a route not listed above, build segments from these parts:

**Terrain flavor by type:**
```
PLAINS/ROAD : Wide sky, grass moving in wind, distant farmsteads or no structures at all.
              The road is the one fixed thing in an unfixed landscape.
FOREST      : The canopy closes overhead. Sounds change — birds you know, then birds you
              don't. Light comes in slants. The road becomes a path becomes a suggestion.
HILLS       : The footing is uncertain. Elevation reveals distance you didn't expect.
              Switchbacks. Wind at the top. You can see where you've been.
RIVER HEX   : The water sound before you see it. The ford — always deeper than expected.
              Mud on the bank, animal tracks, the smell of cold water.
SWAMP/MARSH : Footing uncertain. The wrong step goes through. Insects. The horizon is low
              and flat and gives nothing. Distance becomes unreliable here.
```

**Generic waypoints (use when named route not available):**
- Segment 1 of any journey: departure flavor + companion reaction to leaving
- Middle segments: terrain description + one companion banter
- Final segment: destination visible in distance + arrival emotion

---

*KM_TravelSegments.md — Kingmaker PF2e Text Adventure | Travel Segment System v1.0*
*Named routes: Restov→Oleg's (Route A). Add new routes below Route A as campaign expands.*
