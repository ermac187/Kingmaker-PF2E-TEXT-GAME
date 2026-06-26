# 🐫 THE SILK ROAD OF THE STOLEN LANDS — Trade-Empire Module
## ⛔ CH2-GATED — loaded but DORMANT until Chapter 2 (kingdom founding), with EXACTLY TWO Ch1 exceptions: (1) §1 secured-node flagging (clearing/allying a site writes `secured_nodes[]` — that IS Stage 1 of the quest spine) and (2) §1A Stage-9 rumor seeds (Candlemere hooks as ambient flavor only). Do NOT surface trade missions, roads, the quest board, or the labor system during the Prologue or Chapter 1 — there is no kingdom yet. Load registration: KM_LoadRules.md § SILK ROAD TRADE EMPIRE.
## When kingdom mode opens: this BUILDS ON the existing kingdom engine in KM_Kingdom.md (Build Roads, Trade Agreement, Send Diplomatic Envoy, the trade structures, Commodities) — it adds an OBJECTIVES layer, a ROAD-NETWORK plan, a SIGNATURE EXPORT, and a REDEEMED-LABOR system. It invents no new core actions.

---

## 0. THE VISION (player-stated, 2026-06-11)

A trade empire — *the Silk Road of the Stolen Lands* — not a fortress. The capital is the central hub that connects the **North (Brevoy)** to the **South (the Inner Sea, via Mivon and the River Kingdoms)**. Roads and bridges stitch the cleared frontier together; markets, piers, and a Mint turn position into wealth; an Envoy opens far gates; a **signature export** makes the realm famous; and the people who once preyed on the roads are **redeemed into the crews that build them.**

⛔ **ANTI-FABRICATION (applies to this whole module):** use ONLY canon Kingmaker geography and NPCs (Oleg's, Sootscale, Thorn Ford/Kressle, the Stag Lord's fort, Brevoy, Mivon, Pitax, the River Kingdoms, Restov, Akiros Ismort, Happs). Do NOT invent new nations, named brokers, or conspiracies to populate trade missions. New settlers/foremen who emerge from the labor system are minor, nameless-by-default flavor unless the player names them. Inventing a named faction or plot to drive a trade beat = `.fail 9`.

---

## 1. THE ROAD NETWORK PLAN — "connect them as we beat or ally"

**The timing truth:** roads are a *kingdom* action and cannot be built until the kingdom is founded (end of Ch1 / start of Ch2). So Chapter 1 is the **survey phase**: clearing or allying a site does not lay road — it **flags the site as a secured node.** The conquest *is* the road map. Construction begins Ch2, turn 1.

### THE CH1 → CH2 BRIDGE (the rule that delivers the player's intent)
- Whenever the player **clears or allies** a canon Ch1 site, set `secured_nodes += {site}` in the save (Ch1 export carries it forward).
- At **kingdom founding**, every entry in `secured_nodes` becomes a **queued priority road segment** on the Build-Roads board, in the order the player secured them.
- The player's stated order — Oleg's → Sootscale → the Stag Lord's old fort → Kressle's camp at Thorn Ford — resolves as the first segments laid in Ch2.

### NODE TABLE (canon sites — exact hex coords live in KM_Map.md; only confirmed coords listed here)
| Node | Canon role | How it's secured (Ch1) | Hex |
|---|---|---|---|
| **Oleg's Trading Post** | Northern gateway / first hub | Clear the bandit raids (canon Ch1 start) | base (see KM_Map.md) |
| **Sootscale Caverns** | Mine / ore + kobold ally labor | ALLY the Sootscale kobolds (peace path) | see KM_Map.md |
| **Thorn Ford (Kressle's camp)** | River crossing — needs a **Bridge** | Beat or accept surrender at Thorn Ford | **(3,−1)** |
| **Stag Lord's Fort** | Future capital site | Defeat the Stag Lord (Ch1 finale) | see KM_Map.md |
| **Ancient Tomb** | Optional spur | Clear (Nature/exploration path) | **(0,−1)** |

> Do NOT assert hexes not listed above — read them from KM_Map.md at activation. If a coord is missing, route by named adjacency, not an invented number.

### THE MARITIME SPUR — Lake Candlemere ("the Maritime Silk Road")
- Build a **Pier** (8 RP, 2 Lumber, 1 Stone — Boating DC 16) on a Candlemere water-hex settlement, upgrade to **Waterfront** (90 RP, 10 Lumber — Boating expert DC 24). Per KM_Kingdom.md, **trade routes may begin/end at a Waterfront.**
- A water route across Candlemere **bypasses the road requirement** for any node on the lake — the spur that lets the empire ship the signature export south without finishing every land segment first.
- ⚠️ Candlemere is canon-haunted (the Tower). The maritime spur carries a risk hook: until the Tower threat is addressed, water-route shipments roll a hazard each kingdom turn (DM: minor loss / delay, never a fabricated new monster — use the canon Candlemere threat).

---

## 1A. 🐉 THE EPIC QUEST SPINE — "THE SILK ROAD OF THE STOLEN LANDS" (questline)

**One named, ordered questline laid OVER the engine below** — each stage is an adventure with its own gameplay verb and an immediate, visible payoff, building to a realm-defining finale. The sandbox missions (§2) stay available underneath; the spine *orders* the journey, it doesn't replace the toolbox. Structure inspiration: classic JRPG epic-quest design (staged regional arcs, a hunts board, one hidden optional epic discovered not assigned) — **structure only: all content, names, and threats stay Golarion/Kingmaker canon (anti-fab lock §0 applies; no imported IP content in-world).**

### STEP TYPES — every stage declares HOW it is played
| Type | How it resolves |
|---|---|
| 🗡️ **EXPEDITION** | The party goes. Played at the table — combat, obstacles, problems solved in scenes. NEVER resolved by fiat or summary. |
| 📨 **DISPATCH** | The player SENDS one or more companions for a time. Runs on `KM_MissionResolution.md` (`.delegate`/`.scout`: overflow cost, skill floors, two-phase resolution, injuries, rewards) with a **bounded ETA — the team reports back on a stated turn** (never an open-ended black hole). Sent companions are unavailable until return. |
| 🕊️ **DIPLOMACY** | The player's choice: **GO IN PERSON** (full played scene; +2 circumstance — the ruler came themselves) or **SEND a diplomat** (canon Send Diplomatic Envoy, or DISPATCH a high-Diplomacy companion). In person risks the player's time; sending risks the roll. Both are real paths. |
| 🛠️ **PROJECT** | Kingdom-turn work — build, fund, assign labor. Resolves on the kingdom screen across turns (§1.5 timing rules). |
| 🔍 **DISCOVERY** | NOT surfaced on any quest board. Found through play — rumors, exploration, a hook the player follows. The DM seeds the listed rumor hooks and waits. Surfacing it unearned = the DM spoiled it. |

### THE STAGES (in order; each unlocks the next; quest-log render on every completion)
| # | Stage | Type | What it takes | Stage reward (immediate + visible) |
|---|---|---|---|---|
| 1 | **The Survey** | 🗡️ | (Ch1 — already the bridge, §1) Clear/ally the canon sites; each becomes a `secured_node` | Each node = a queued priority segment; the conquest IS the road map |
| 2 | **The First Stone** | 🛠️ | Found the kingdom; complete the FIRST road link (capital ↔ nearest node) | First passive RP link online; the realm SEES it (carts, a waystation beat); +1 Stability |
| 3 | **The Sycamore Accord** | 🕊️ | TWO FACTIONS MADE PEACE: the canon kobold/mite war (Old Sycamore, Ch1). Peace/alliance resolution = credited retroactively at founding. If it ended in blood: a harder Ch2 diplomacy scene with the survivors (Sootscale chief or the remaining faction) to bind them to the road instead | Kobold labor crew (+1 hex/turn on segments near Sootscale) + the Sootscale mine feeds the silver export option; Sootscale becomes a true trade node |
| 4 | **The Wardens' Board** | 🗡️/📨 | THE HUNTS BOARD (repeatable, runs alongside all later stages): raiders and monsters threaten road hexes and villages — each posted contract names a canon-grounded threat (bandit remnants, the road's monster hexes per KM_Map/Chapters; no invented factions). Player clears it IN PERSON (🗡️) or DISPATCHES a team (📨) | Per contract: the link un-SUSPENDS / village saved (+1 Loyalty area), small loot. Board milestone (3 cleared): **Road Wardens founded** — patrols halve future degradation events |
| 5 | **The Northern Gate** | 🕊️ | Open Brevoy: travel to Restov/New Stetven yourself, or send the envoy (1–3 turns, bounded) | Northern trade route live (+2 Economy); +1 Fame; Brevoy caravans appear on the road (visible traffic) |
| 6 | **The Builders' Redemption** | 📨 | First redeemed crew reaches loyalty 3 (§5) — requires assigning a supervising companion for the turns it takes (they're WORKING it, not just named) | Akiros (or first redeemed) = named Foreman; labor effect +1; the mercy-realm identity lands (+Good credit, Unrest −1) |
| 7 | **The Signature** | 🛠️ | Specialized Artisan + work site; export goes live (§3) | Premium links begin; first foreign sale = +1 Fame; the realm has a NAME abroad |
| 8 | **The Southern Reach** | 🕊️ | Open Mivon (in person or envoy) + a Marketplace or Waterfront | Southern route live; Inner-Sea buyers for the export; the corridor's far anchor set |
| 9 | **WHAT WAITS IN THE WATER** | 🔍 | THE HIDDEN EPIC — see below. Not on the board. The maritime spur (§1) cannot be SAFE until it's done | Candlemere water corridor fully open (hazard rolls END); unique canon reward from the Tower; +2 Fame; the lake becomes the realm's inland sea |
| 10 | **THE SILK ROAD OPEN** | 🛠️ capstone | Unbroken N↔S chain: Brevoy gate + southern anchor + every corridor link complete (Thorn Ford Bridge included) | **The finale beat:** travel halved network-wide; +2 Fame; realm title ("the Silk Road of the Stolen Lands" — named on maps, spoken by foreign NPCs); a founding-festival scene; the engine is self-funding |

### 🔍 STAGE 9 EXPANDED — WHAT WAITS IN THE WATER (the discoverable epic)
Candlemere is the questline's optional-epic — the thing the player *finds*, the way the great JRPGs hid their best arc behind a rumor. **Run it strictly from canon: the haunted Tower on Candlemere's isle and its canon threat (KM source material) — invent NO new entity.**
- **Rumor seeds (DM drops these, never the quest):** fishermen refuse night crossings; a shipment arrives a day late, crew won't say why; Jamandi's old line — *"what's in those waters"*; will-o'-light seen from the south shore; the §1 hazard rolls themselves ARE the breadcrumbs.
- **Arc shape (3 beats, each a real session):**
  1. **The Drowned Ledger** (📨 or 🗡️) — investigate the losses: dispatch scouts to chart where shipments vanish, or sail it yourself. Output: the isle is the source; a landing map.
  2. **The Landing** (🗡️) — expedition to the isle: the approach is an obstacle gauntlet (fog, wards, the shore itself), played at the table.
  3. **The Tower** (🗡️) — the canon threat, faced. A genuine boss-tier fight/ordeal scaled to the party.
- **Why it's worth it:** until done, every water shipment rolls the §1 hazard; after, the maritime corridor is the realm's safest artery — the optional epic permanently upgrades the economy, JRPG-superboss style.
- ⛔ The player can SKIP it forever — the land corridor alone can finish Stage 10. The lake is the better empire, not the required one.

### SPINE RULES
- **Quest-log telemetry:** `silkroad_quest: { stage: N, completed: [...], wardens_board: { posted: [...], cleared: N } }` in the kingdom save; render the active stage + next objective each Kingdom Turn (bounded — never "someday").
- **Stages 4+ can interleave** (the board runs continuously; diplomacy can start while a road builds) — but each stage's REWARD fires only on ITS completion, rendered as a scene beat, not a stat line.
- **No fiat completion:** 🗡️ stages are played; 📨 stages roll `KM_MissionResolution.md`; 🕊️ stages roll the canon action or play the scene. A stage "completing" off-screen without its system = `.fail 9` + `.fail 38`.
- **Companion cost is real:** a DISPATCHED companion is gone until the stated return turn — unavailable for expeditions, their bond beats paused. Sending your best diplomat means fighting without her.

---

## 1.5 TRADE NETWORK INCOME & SETTLEMENT GROWTH — the roads pay, the places grow

⛔ All numbers below are **TUNABLE at activation** against `KM_Kingdom.md`'s economy (RP is small-integer; keep these modest so the network *supplements*, never trivializes, the Kingdom Turn). Everything ties to EXISTING kingdom stats — RP / Economy / Consumption / settlement tier — and invents no new currency.

### ⏳ ROAD CONSTRUCTION — a road is a PROJECT; distance = duration
Roads are NOT laid instantly. A link between two settlements is a **multi-turn project** whose length scales with the **distance** between them:
- **Span** = the number of hexes on the path between the two settlements (from the hex map). A neighbor is 1–2 hexes; the far corners of the realm are many.
- **Build rate** = the kingdom lays **2 road-hexes per Kingdom Turn** by default (each hex still pays its **2 RP + 1 Lumber** per the canon Build Roads action, and the turn's **Engineering DC 14** must succeed — a fail stalls THAT turn's segment, RP/Lumber held, retry next turn). A **D-hex** road takes **⌈D ÷ rate⌉ turns**.
- **Redeemed labor accelerates it (§5):** each assigned labor crew adds **+1 hex/turn** to the rate (cap +2 over base → up to 4 hexes/turn), on top of labor's RP discount. This is the concrete payoff of turning bandits into builders — the Silk Road rises faster the more of them you've redeemed.
- **Terrain slows it:** rough hexes (mountain, deep forest, swamp, the Candlemere shore) count **double** toward the span (or halve the rate through them). A **river crossing** (e.g. Thorn Ford) needs a **Bridge** first — its own sub-project (6 RP + Lumber/Stone, Engineering DC 16) that must finish before the road continues past it.
- **No income until complete (§1.5A):** a half-built road pays nothing and grants no travel-time benefit — it is a line on the map and a standing commitment of RP. Plan the order: corridor priority, which link unlocks the next settlement's upgrade, where the labor crews go.
- Track `road_project{ from, to, hexes_total, hexes_built, rate, eta_turns }`; render a **bounded ETA** each Kingdom Turn (never an open-ended "someday" — see [[feedback_delegated_order_dropped]]). On the turn `hexes_built = hexes_total`, it becomes an active trade link and the income begins.

### A. TRADE LINKS PAY PASSIVE INCOME (every Kingdom Turn)
A **trade link** = a COMPLETED road (or Candlemere water route) connecting two settlements / secured nodes. Each active link yields passive income at the Kingdom Turn's Income step, into Treasury (RP).

Per-link income = **+1 RP base**, plus:
| Factor | Bonus |
|---|---|
| Each linked end that is a **Town** (tier 2) | +1 RP |
| Each linked end that is a **City+** (tier 3+) | +2 RP |
| Link carries the **signature export** (origin produces it → a market dest) | +1 RP + counts toward Fame |
| Link is part of a **completed corridor** (unbroken N↔S chain) | +1 RP per link in the chain (through-route premium) |
| Link to an **external partner** via an open Trade Agreement (Brevoy / Mivon) | +2 RP (the Agreement's own Economy bonus applies on top) |
| Road **degraded / unguarded** (bandit hex, unrest at a linked end) | −1, or SUSPENDED until cleared |

- A settlement with **3+ links** becomes a **TRADE HUB**: goods flow *through* it — each of its links gains +1, and it gains +1 Economy. The emergent reward for building a spider, not a line.
- ⛔ Income requires the road **COMPLETE** and **both ends settlements** — a road into an empty hex pays nothing (it's only travel time). Redeemed-labor (§5) speeds the *building*, not the income.
- Track `settlement.trade_links` and a running `trade_rp_cumulative` per settlement (drives growth, below).

### B. SETTLEMENTS UPGRADE AT THRESHOLDS — connections grow the place
A settlement's tier (Village → Town → City → Metropolis, per `KM_Kingdom.md` settlement table) rises as trade flows through it. Upgrade fires when ALL of a row's conditions are met — connections + cumulative trade + a key structure, never one alone:

| Upgrade | Threshold (all required) | Unlocks |
|---|---|---|
| Village → **Town** | ≥2 links + a Market/General Store + 200 cumulative trade RP earned here | +building slots; Town structures (Marketplace, Bank, Pier); +1 Economy |
| Town → **City** | ≥4 links (or 2 + a Waterfront) + a Marketplace + 600 cumulative trade RP | City structures (Mint, Luxury Store, Embassy, Magic Shop); +2 Economy; can anchor a corridor end |
| City → **Metropolis** | TRADE HUB (≥6 links) + a Mint + 1500 cumulative trade RP + signature export shipping | apex structures; +3 Economy; a Fame landmark; named hub on the map |

- On upgrade: render it as a BEAT (the place visibly swells — stalls, traffic, the redeemed-labor crews raising new lots), grant the slots/Economy, log it. The upgrade is **earned by the network**, not bought with a lump — but the player still pays the new structures' own RP/Commodity costs.
- ⛔ **Settlements can DOWNGRADE too.** If links are cut (roads fall to bandits, a linked settlement is lost) and a place sits below its tier's threshold for a full chapter, it slides a tier, +Unrest. The network is alive — neglect it and it shrinks. (Same philosophy as the Tartuccio recovery/erosion logic: standing is never permanent.)

### C. THE LOOP (how it feels)
Clear a site (Ch1) → secured node → found the kingdom (Ch2) → build a road linking it to the capital → that link pays RP every turn → the RP funds more roads → more links → the settlement hits a threshold and **upgrades** → the bigger settlement makes each of its links worth more → a HUB forms → a corridor completes → the Silk Road becomes a **self-funding engine.** Redeemed-labor crews (§5) build it faster; the signature export (§3) makes the premium links; the trade missions (§2) chain it to the wider world. Save: `settlement{ tier, trade_links, trade_rp_cumulative }` + `trade_network{ corridors[], hubs[] }`.

---

## 2. TRADE OBJECTIVES — the missions/objectives layer (THIS is what "hex mode needs added")

The base **actions** exist; these give them mission framing. Each is a **Kingdom Mission**: trigger → requirement (built from existing actions/structures) → reward. Surface them on the kingdom screen as available objectives; never auto-complete. **Most are now WOVEN INTO the §1A quest spine** (Northern Gate = Stage 5, Southern Reach = Stage 8, Lay the Corridor = Stage 10, Maritime = Stage 9, Signature = Stage 7) — completing the spine stage completes the mission and vice versa; rewards are the SAME entry, never double-paid.

| Mission | Trigger | Requirement (existing systems) | Reward |
|---|---|---|---|
| **Open the Northern Gate** | Ch2, Brevoy reachable | Send Diplomatic Envoy → Brevoy (Stability DC 16) + 1 Trade Agreement | +2 Economy/turn route; +1 Fame |
| **The Southern Reach** | road or water link toward the Inner Sea | Envoy → Mivon + a Marketplace OR Waterfront | +2 Economy route; unlocks Inner-Sea buyers for the export |
| **The River Kingdoms Accord** | adjacency to 2+ River Kingdom factions | 2 Trade Agreements (Diplomacy/Commerce) | +1 Economy each; Pitax tension flag (ties to [[project_pitax_leech_kingdom_debuff]]) |
| **Lay the Corridor** | all `secured_nodes` road-linked N↔S | Build Roads across the network + 1 Bridge at Thorn Ford | Travel time halved network-wide; +2 Fame; "Silk Road open" title |
| **The Maritime Silk Road** | Waterfront on Candlemere | Pier→Waterfront + 1 water Trade Agreement | A second trade corridor immune to land-route disruption |
| **The Signature Export** | see §3 | Specialized Artisan + chosen work site | Export commodity goes live (premium trade value) |

**Mission reward stacking note:** route bonuses are the canon Trade Agreement / faction-route values already in KM_Kingdom.md — these missions *frame and chain* them, they do not invent new economy numbers. A completed corridor is the sum of its real route bonuses plus the Fame/title flavor.

---

## 3. THE SIGNATURE EXPORT — "a thing everyone else wants"

Pick ONE signature export at the first Specialized Artisan (player choice; locks the realm's identity):
- **Stolen Lands Silk** — rare spider/fey-silk weave (ties to First World / Candlemere fey).
- **Silverwork & silver ore** — Sootscale mine → Foundry → Specialized Artisan silversmithing.
- **Rare magical herbs** — wilderness work sites + an Herbalist/Magic structure.

**Mechanic (built on existing pieces):**
- Production: a **Specialized Artisan** (+1 to one specific Commodity, +1 Earn Income for that craft) feeding off the matching **work site** (mine/ranch/lumber/wilderness). The export is tracked as a premium commodity: `signature_export: {type, units_per_turn}`.
- Value: a Trade Agreement that *includes the signature export* gets **+1 to its Economy bonus and +1 Fame the first time each partner buys it** (it's prestige, not bulk).
- Scaling: a **Mint** or **Luxury Store** in the export's home settlement adds +1 unit/turn. At high renown the export becomes a `.codex` entry and a diplomatic gift the Envoy can carry.

---

## 4. THE ENVOY — opening far gates

Uses the canon **Send Diplomatic Envoy** action (Stability DC 16; +1 from Embassy, +1 from Castle) framed as a *mission with travel*:
- The player dispatches an envoy (a companion or a named agent) on a multi-turn diplomatic mission to a far capital (Brevoy / Mivon / a River Kingdom).
- Resolve over 1–3 kingdom turns with a **bounded ETA** (per [[feedback_delegated_order_dropped]] — never an open-ended black hole; the envoy REPORTS back on a set turn).
- Outcome ladder: crit success = trade route + alliance lean; success = trade route opens; failure = no route, retry next turn; crit fail = a slighted partner (−1 relationship, a Pitax-style rival gets there first).
- ⛔ The far court's people are canon or nameless functionaries — the Envoy does NOT discover a new named conspiracy abroad (anti-fab).

---

## 5. ⛒ REDEEMED LABOR — bandits become the builders of the realm (NEW SYSTEM)

The soul of the playstyle: the people who preyed on the roads are redeemed into the crews that build them. Canon already seeds it — bandits **surrender** (Happs), and **Akiros Ismort defects and seeks redemption.** Akiros is the template and the first foreman.

### THE LABOR POOL
- **Sources:** captured bandits who surrender; defectors (Akiros); convicts from Crime-event resolutions where the player chooses *redemption over execution/exile.*
- Track: `redeemed_labor: { pool: N, in_redemption: [ {id, loyalty, assigned_to} ] }`.

### THE REDEMPTION TRACK (a captured criminal is not instantly trusted)
- New captives enter at **loyalty 0** (`in_redemption`). Each kingdom turn assigned to supervised work, roll a redemption check (the supervising leader's Diplomacy/Society vs a DC that drops as a settlement gains Justice/relevant structures).
- **Success → loyalty +1.** At **loyalty 3** the worker is **Redeemed**: joins the stable `pool`, grants a one-time **+Good alignment credit** and **Unrest −1** (the realm visibly chose mercy that worked).
- **Failure / neglect / overwork** → loyalty −1; at loyalty −2 a **recidivism event**: escape, theft, or sabotage → **+1 Crime/Ruin and +1 Unrest** (and the freed bandit may turn up as a future encounter).

### THE LABOR EFFECT (why you want them)
Assign Redeemed labor units to construction:
- **Build Roads:** each 2 labor units = **−1 RP per road hex** OR **+1 road hex this turn** (player's choice), to a cap of the settlement's supervising capacity.
- **Infrastructure (Bridge, Pier, work sites):** 1 labor unit = **+2 circumstance to the construction skill check**, max +2 per project.
- Labor does NOT reduce *Commodity* costs (you still need the Lumber/Stone) — it reduces RP and time. It is muscle, not material.

### BALANCE & ALIGNMENT GATES
- **Supervision cap:** a settlement can supervise (Redeemed + in_redemption) up to its Justice-related structure count (Jail/Town Hall/Castle). Exceed it → recidivism risk rises; the realm is overextending its mercy.
- **The fork is alignment-real:** *redeeming* labor = Good and lowers Unrest; **forcing unredeemed labor (penal road-gangs, no redemption track)** is the Evil path — it builds faster short-term but **+1 Unrest/turn** and **caps Fame** (a realm built on chains). The player chooses which empire this is; the system prices both honestly.
- **The Akiros payoff:** the first Redeemed worker to hit loyalty 3 (default Akiros, if recruited) becomes a **named Labor Foreman** — a minor standing NPC who grants +1 to the labor effect and a recruitment hook. Other redeemed workers stay nameless settlers unless the player names one.

---

## 6. INTEGRATION & ACTIVATION CHECKLIST (do at Ch2 founding)
1. ✅ DONE 2026-06-12 — registered in `KM_LoadRules.md` § SILK ROAD TRADE EMPIRE (two-phase: Ch1 bridge-only, Ch2+ full module).
2. Add to the kingdom JSON: `secured_nodes[]`, `signature_export{}`, `redeemed_labor{}`, `trade_missions{}` (status per mission), `silkroad_quest{ stage, completed[], wardens_board{} }` (§1A spine), per-settlement `{ tier, trade_links, trade_rp_cumulative }`, and `trade_network{ corridors[], hubs[] }`. At the Kingdom-Turn Income step, sum every active trade link's per-link income (§1.5A) into Treasury, then check each settlement against the upgrade/downgrade thresholds (§1.5B).
3. Carry `secured_nodes[]` through the **Ch1 Export Block** so the road network reflects what was actually cleared/allied.
4. Cross-link: Pitax tension → [[project_pitax_leech_kingdom_debuff]]; envoy ETA discipline → [[feedback_delegated_order_dropped]].
5. Size: kept as its own file (NOT folded into the ~148 KB `KM_Kingdom.md`, which would risk the 200 KB hard limit).

---

*KM_SilkRoad.md — trade-empire module, authored 2026-06-11. Builds on KM_Kingdom.md canon (PF2e Kingmaker kingdom rules). Dormant until Chapter 2 kingdom founding.*
