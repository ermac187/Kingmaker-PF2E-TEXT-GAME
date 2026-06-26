# KINGMAKER — KINGDOM MANAGEMENT (Part 2)
## KM_Kingdom_B.md | Faction Reputation Tracks
## PAIR-LOAD WITH KM_Kingdom.md

> **DM:** Load alongside KM_Kingdom.md. This file contains all 8 faction
> reputation tracks. Track scores in save block under `"faction_reputation": {}`.

---

## 🏛️ FACTION REPUTATION TRACKS
> **Faction tracks and villain offscreen behavior** — consolidated below.

> Each faction has a Reputation score from −10 (hostile) to +10 (allied).
> Starting values and change triggers are documented here.
> Track in save block under `"faction_reputation": {}`.

### Save Block Format

```json
"faction_reputation": {
  "aldori_swordlords": 0,
  "house_surtova": 0,
  "nomen_centaurs": -2,
  "river_kingdoms": 0,
  "pitax": -5,
  "brevoy_crown": 0,
  "tiger_lords": -3,
  "first_world_fey": 0
}
```

---

### ALDORI SWORDLORDS

**Starting value:** +2 (Jamandi gave the charter — baseline goodwill)
**Allied threshold:** +7 | **Hostile threshold:** −5

| Action | Change |
|--------|--------|
| Completing the charter (Stag Lord defeated) | +2 |
| Siding with Aldori at coronation | +3 |
| Siding with Surtova at coronation | −4 |
| Declaring independence at coronation | −1 |
| Kassil Aldori in a leadership role | +1/turn |
| Player publicly credits Jamandi | +1 |
| Player insults or defies Jamandi | −2 |
| Kingdom Unrest 15+ for 2+ turns | −2 (embarrassment) |

**At +7 (Allied):** Jamandi sends 2 Aldori duelists as personal guard (Fighters L8, free). Trade agreement: +2 Economy per turn.
**At −5 (Hostile):** Charter formally reviewed. If below −7: charter revoked (see Kingdom Failure State).

---

### HOUSE SURTOVA

**Starting value:** −1 (they wanted this territory for themselves)
**Allied threshold:** +6 | **Hostile threshold:** −6

| Action | Change |
|--------|--------|
| Siding with Natala Surtova at coronation | +4 |
| Siding with Aldori at coronation | −2 |
| Exposing Surtova involvement in any plot | −3 |
| Keeping Surtova's role quiet (discretion) | +1 |
| Sending tribute to Brevoy crown | +2 |
| Kingdom reaches Size 15+ | −1 (they're watching) |

**At +6 (Allied):** Natala offers a marriage alliance (narrative, player choice). Trade route through Brevoy: +3 Economy.
**At −6 (Hostile):** Surtova begins actively funding rivals — Unrest +1/turn (scripted event, cannot be rolled away).

**Note:** Aldori and Surtova are mutually exclusive above +5. If both reach +5, the player must choose — the other drops to +3 automatically. They cannot both be full allies.

---

### NOMEN CENTAURS

**Starting value:** −2 (territorial, suspicious of human expansion)
**Allied threshold:** +5 | **Hostile threshold:** −6

| Action | Change |
|--------|--------|
| Helping Xamanthe (Ch3) | +3 |
| Solving Vordakai without centaur casualties | +2 |
| Centaur deaths during player's campaign | −1 per named centaur |
| Claiming a hex bordering centaur territory without negotiating | −2 |
| Offering centaurs a formal treaty | +2 (Diplomacy DC 22 to present) |
| Kellid War-Bread purchased from Kellid camp | +1 (word spreads) |

**At +5 (Allied):** Centaur scouts reveal 3 hidden hexes on the map. Horse trade: mounted movement +1 hex/day. Nomen warriors available as army unit.
**At −6 (Hostile):** Centaur raids begin. Treat as Ch2-level Troll Incursion events per turn until resolved.

---

### RIVER KINGDOMS

**Starting value:** 0 (neutral — you're new, they're watching)
**Allied threshold:** +6 | **Hostile threshold:** −5

| Action | Change |
|--------|--------|
| Defeating Irovetti (Ch5) | +3 |
| Allowing Irovetti to invade without resistance | −3 |
| Player kingdom reaches Size 20+ | −1 (concern about dominance) |
| Winning River Kingdom Summit (Ch4) | +2 |
| Providing military aid to a River Kingdom | +2 |
| Annexing a River Kingdom settlement | −4 |

**At +6 (Allied):** River Kingdoms recognize the player's kingdom as a legitimate River Kingdom. +1 to all Diplomacy checks in the region. 2 ally armies available in Ch5 war.
**At −5 (Hostile):** River Kingdoms coordinate with Pitax. Irovetti's Ch5 army gets +2 Attack and +10 HP.

---

### PITAX

**Starting value:** −3 (Irovetti funded Malak's bribe attempt at Restov)
**Allied threshold:** N/A (cannot be fully allied while Irovetti lives)
**Hostile threshold:** −8 (triggers early war)

| Action | Change |
|--------|--------|
| Accepting Irovetti's protectorate offer (Ch2) | +3 (temporary) |
| Refusing Stefano Moskoni politely (Ch2) | +1 |
| Exposing Pitax involvement in Malak bribe | −2 |
| Each chapter that passes without conflict | −1 (inevitable drift) |
| Defeating Pitax armies in field | −2 each |

**At −8:** Irovetti invades early — Ch5 begins regardless of chapter. Player is not ready. Army stats unchanged but player has fewer resources.

**Post-Irovetti:** Pitax can be integrated as a vassal (+5 Economy per turn) or left independent (neutral relationship, no bonuses).

---

### BREVOY CROWN

**Starting value:** 0 (they granted the charter via Jamandi — officially neutral)

| Action | Change |
|--------|--------|
| Sending annual tribute (500 gp) | +1/year |
| Kingdom reaches Size 30+ | +1 (impressive) |
| Public scandal (Unrest 15+ reported) | −2 |
| Aldori faction at +7 | +1 (reflected glory) |
| Surtova faction at −6 | −2 (their noble house embarrassed) |

**At +6:** Crown officially endorses the kingdom. Bardic tales spread — Public Reputation +10.
**At −5:** Crown begins questioning charter legality. Jamandi must defend the player.

---

### TIGER LORDS

**Starting value:** −3 (hostile to kingdom expansion into their traditional territory)
**Allied threshold:** +5 | **Hostile threshold:** −7

| Action | Change |
|--------|--------|
| Defeating Armag (Ch4) | +1 (respect for strength) |
| Negotiating with Armag rather than fighting | +3 (rare path) |
| Claiming Tiger Lord ancestral hex without diplomacy | −2 |
| Allowing Tiger Lord raids without retaliation | −1/turn |
| Warrior champion of the kingdom defeats Tiger Lord champion | +2 |

**At +5 (Allied):** Tiger Lords pledge warriors — 1 Cavalry army unit joins (free). Hunting rights in eastern hexes granted.
**At −7 (Hostile):** Armag leads a united warband assault. Treat as Ch4 boss encounter with full army backing.

---

### FIRST WORLD FEY

**Starting value:** 0 (Nyrissa's influence — unstable, watching)
**Allied threshold:** +6 | **Hostile threshold:** −6

| Action | Change |
|--------|--------|
| Returning items to Tiressia and fey allies | +1 each |
| Protecting fey groves from settlement expansion | +1 per grove |
| Cutting down a fey grove for farmland | −3 |
| Completing Nyrissa's true ending (saving her) | +5 (permanent) |
| Killing Nyrissa without pursuing the true ending | −5 |
| Bloom corruption spreading unchecked | −1/chapter |

**At +6 (Allied):** Fey blessing on the kingdom — Culture +3 permanent, one hex per turn auto-discovers. Nyrissa (if saved) becomes a kingdom advisor (Culture +5, prevents fey events).
**At −6 (Hostile):** Bloom events intensify. Fey raids add +1 Unrest/turn and cannot be resolved by normal kingdom activities — require a personal confrontation scene.

---

*KM_Kingdom_B.md — Kingmaker PF2e Text Adventure | Faction Reputation Tracks v1.0*
