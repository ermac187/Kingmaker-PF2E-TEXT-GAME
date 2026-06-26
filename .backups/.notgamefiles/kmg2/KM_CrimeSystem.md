# KINGMAKER — CRIME SYSTEM
## KM_CrimeSystem.md | Active from: Chapter 1 | Referenced by: KM_Reputation.md, KM_Kingdom.md, KM_Actions.md

> **DM:** Load this file whenever the player enters a settlement, interacts with
> named NPCs in private spaces, or takes any action that could constitute theft,
> assault, murder, trespass, or fraud. This system uses only existing PF2e skill
> mechanics — no new stats are invented. It feeds directly into KM_Reputation.md
> (civilian reputation) and KM_Kingdom.md (Infamy, Unrest). It does not override
> alignment tracking — it feeds it.

---

## ⚖️ CRIME CATEGORIES

| Category | Examples | Base Severity |
|----------|----------|---------------|
| **Petty** | Pickpocket, trespass, minor fraud, vandalism | 1 |
| **Moderate** | Burglary, assault, arson (small), extortion | 2 |
| **Serious** | Armed robbery, grievous assault, grand theft | 3 |
| **Capital** | Murder, massacre, arson (major), treason | 4 |

Severity scales consequences: fines, pursuit intensity, Infamy gain, and companion reactions.

---

## 👁️ THE WITNESS SYSTEM

Every criminal act has a **Witness Check**. The DM resolves this secretly.

```
WITNESS CHECK PROCEDURE

Step 1 — Establish the scene:
  Is anyone present?
    NO WITNESSES POSSIBLE → skip to Step 4 (evidence only)
    WITNESSES POSSIBLE → proceed

Step 2 — Count potential witnesses:
  Isolated (wilderness, locked room alone):   1 flat check DC 18 (random passerby, animal, spirit)
  Low traffic (back alley, late night):       1d3 witnesses, each rolls Perception vs player's Stealth
  Normal traffic (market, tavern, road):      1d6 witnesses, Perception DC = player's Stealth result
  High traffic (public square, feast, court): Automatic — 1d4 witnesses notice regardless of Stealth

Step 3 — Witness Perception check (DM rolls secretly):
  Each witness rolls Perception vs the player's Stealth or Deception check.
    Witness succeeds:   They saw it. Proceed to Witness Type table.
    Witness fails:      They noticed nothing. No report.
    Witness crits:      They saw it AND can describe the player accurately (+1 to all pursuit checks).

Step 4 — Physical Evidence:
  Even with no witnesses, crime leaves traces.
    Body not hidden:        Evidence = OBVIOUS (found within 1d4 hours)
    Item stolen, no body:   Evidence = SUBTLE (found within 1d6 days on successful Investigation DC 18)
    No physical trace:      Evidence = NONE (e.g., pickpocket with no dropped items, clean kill)
  If player takes steps to conceal evidence: Survival or Thievery vs DC 18 to reduce one tier.
    OBVIOUS → SUBTLE on success | SUBTLE → NONE on critical success only
```

### Witness Type Table

| Witness Type | Immediate Action | Report Speed |
|---|---|---|
| Child | Runs to parent; describes poorly | 1d4 hours |
| Civilian adult | Avoids player; reports to guards | 1d6 hours |
| Merchant | Locks up; reports and posts reward | 1 hour |
| Guard (off-duty) | Challenges player immediately | Immediate |
| Guard (on-duty) | Arrest attempt immediately | Immediate |
| Companion (party) | Reacts per personality — see below | Immediate |
| Named NPC (friendly) | Private confrontation; no report unless pushed | 1 session |
| Named NPC (neutral) | Reports unless bribed or intimidated | 1d4 hours |
| Named NPC (hostile) | Reports and embellishes | 30 minutes |

---

## 🎭 CRIME ACTIONS & SKILL DCS

### THEFT

**Pickpocket** — Thievery vs target's Perception DC
- Target is unaware: DC = Perception modifier + 10
- Target is distracted: DC −2
- Target is alert/suspicious: DC +4
- **Crit Success:** Item taken; target unaware anything happened
- **Success:** Item taken; target notices something felt wrong but can't place it (50% chance they check pockets in 1d10 minutes)
- **Failure:** Attempt failed; target is now Suspicious (Perception checks vs you at +2 for this scene)
- **Crit Failure:** Caught in the act; Witness Check triggers at +4

**Burglary** — requires bypassing locks and avoiding guards
- Pick Lock: Thievery vs lock DC (see KM_Conditions_Skills.md)
- Avoid Guards: Stealth vs guard Perception DC (base 14, +2 per guard tier above standard)
- Time pressure: each lock attempt = 1 minute of exposure; flat check DC 12 per minute for a patrol to pass
- **Getting away clean:** Must succeed on both lock pick and stealth; failure on either triggers Witness Check

**Loot a Body** — no check if unwitnessed; Stealth vs DC 14 if in a populated area

**Rob a Merchant (armed)** — Intimidation vs Will DC 16 (base)
- Success: merchant complies; reports immediately after player leaves
- Failure: merchant resists; combat or retreat

---

### ASSAULT & MURDER

**Assault (non-lethal)** — Standard combat with nonlethal damage flag
- Witness Check triggers if anyone is present
- Target recovers and can report — treat as a live witness

**Murder (hidden kill)** — Requires player to be Hidden or Undetected first
- Stealth approach: Stealth vs target Perception DC
- Kill action: standard Strike — target is off-guard if Undetected
- Post-kill concealment: Survival or Thievery DC 18 to hide body
  - Success: body found in 1d6 days
  - Failure: body found in 1d4 hours
  - Crit Success: body may never be found (DM rolls flat check DC 14 per week)

**Public Murder** — No stealth possible; automatic Witness Check at maximum traffic tier
- Companion reactions fire immediately (see below)
- Reputation: −2 in current region, propagates per KM_Reputation.md rules
- If player is the ruler: Infamy +2, Unrest +1 next Kingdom Turn

**Assassination** — Planned murder of a named NPC
- Requires a Planning Check before execution: Society or Intrigue Lore DC 18 to case the target
- Success on planning: +2 to all checks during the attempt; evidence tier reduced by one step
- The DM runs this as a mini-sequence: approach → access → act → escape
- Named NPCs with significant political weight (nobles, faction leaders) trigger faction reputation hits on death — see KM_Kingdom.md faction tables

---

### FRAUD & DECEPTION

**Impersonate an Official** — Deception vs observer Perception DC
- With forged documents: DC −4
- Without: DC as written
- Failure in a settlement: Witness Check immediately

**Forge Documents** — Society DC 20 (common document) to DC 30 (official writ)
- Player must have materials: ink, paper, a sample to copy (−2 DC if sample available)
- Forgery is not detected until someone examines it (Society DC 20 to spot)

**Extortion** — Intimidation vs Will DC; target's wealth tier determines payout
- Common civilian: 1d6 gp per severity level extorted
- Merchant: 2d10 gp
- Noble: 5d10 gp — but noble has resources to pursue
- Every extortion: flat check DC 14; success = someone reported it

---

## 🚨 GETTING CAUGHT — RESPONSE TIERS

When a crime is witnessed or reported, the response scales with severity and the player's status.

```
RESPONSE MATRIX

              | No Prior Infamy | Infamy 1–3 | Infamy 4–6 | Infamy 7+ |
Petty         | Fine offered    | Fine + watch| Detention  | Arrest    |
Moderate      | Detention       | Arrest      | Arrest+    | Hunt      |
Serious       | Arrest          | Hunt        | Hunt+      | Kill order|
Capital       | Hunt            | Kill order  | Kill order | Kill order|

Fine:         Pay Severity × 5 gp or face escalation
Detention:    Held for 1d4 hours; gear held; escorted out of settlement
Arrest:       Full custody; trial scene triggers; see Trial section
Hunt:         Bounty posted; bounty hunters spawn in the region
Kill order:   No trial; any guard or bounty hunter may kill on sight
```

### GUARDS — RESPONSE BEHAVIOR

**Standard Guard (L2 Fighter)**
- Will not pursue beyond settlement boundary unless bounty is active
- Can be Intimidated (DC 18) to back down — but they report it afterward
- Can be Bribed: 5 gp × severity to look the other way (flat check DC 12; failure = they take the money AND arrest you)
- Three guards = automatic arrest attempt unless player flees

**Guard Captain (L5 Fighter)**
- Personally pursues fleeing suspects for 1d4 rounds beyond settlement
- Cannot be Intimidated without a crit success
- Bribe DC 18 (flat); costs 20 gp × severity

**Bounty Hunters (L = party level)**
- Spawn 1d4 days after bounty is posted
- 1–2 hunters for petty/moderate; 3–4 for serious; full squad (4–6) for capital
- Have player description and last known location
- Will track across regions; do not stop at settlement boundaries
- Can be negotiated with (Diplomacy DC 22) if player surrenders or pays bounty value

---

## 🏃 GETTING AWAY — ESCAPE OPTIONS

### Flee the Scene
- Chase subsystem triggers (see KM_RoE_Subsystems.md)
- Player must clear 3 obstacles to escape settlement; 5 obstacles if bounty hunters are involved

### Disguise
- Deception DC 18 to change appearance enough to avoid casual recognition
- Requires at least 10 minutes and a change of visible clothing
- Named witnesses who got a crit on their Perception check can still identify you at DC 22

### Alibi
- Diplomacy or Deception DC 20 to establish a false alibi with a willing NPC
- Willing companion can vouch: DC 14 (they are trusted). Companion relationship must be Friendly or better.
- False alibi breaks if the NPC is pressed with evidence: Society DC 18 for investigators

### Bribery (after the fact)
- Can suppress a report if player reaches the witness before they report
- Cost: Severity × 10 gp per witness
- Intimidation instead of gold: Coerce action, DC 16 + Severity × 2
  - Success: they stay quiet this session
  - Failure: they report AND mention the intimidation attempt (+1 Severity to response tier)

### Leave the Region
- Crimes do not follow the player to new regions unless Severity 4 (capital) or Infamy 5+
- Infamy 5+: crimes propagate to adjacent regions within 1 week
- Infamy 7+: crimes propagate across all known regions within 2 weeks

---

## 📊 INFAMY TRACK

Separate from Reputation. Infamy measures how widely known the player is as a criminal — not just feared, but **wanted**.

```
Infamy 0:   Unknown criminal record
Infamy 1–2: Minor incidents on record; some merchants wary
Infamy 3–4: Wanted poster in 1d3 settlements; guards alert
Infamy 5–6: Wanted poster everywhere in region; bounty active
Infamy 7–8: Multi-region manhunt; faction bounties stack
Infamy 9:   Kill-on-sight in all known regions
Infamy 10:  National incident; Brevoy or River Kingdoms sends forces
```

**Gaining Infamy:**

| Crime | Infamy Gained |
|-------|--------------|
| Petty crime, caught | +0 (logged, not infamous) |
| Moderate crime, caught | +1 |
| Serious crime, caught | +2 |
| Capital crime (murder of commoner), caught | +2 |
| Capital crime (murder of noble/official), caught | +3 |
| Crime witnessed publicly by 5+ people | +1 additional |
| Crime in own kingdom as ruler | +1 additional (subjects watch) |

**Reducing Infamy:**

| Action | Infamy Reduced |
|--------|---------------|
| Pay all outstanding fines and bounties | −1 |
| Publicly perform a heroic act in affected region | −1 |
| Kingdom: Repair Reputation action (K23) | −1 per success |
| Full chapter passes without new crimes | −1 (natural fade) |
| Bribe or eliminate all witnesses (risky) | −1 per tier of evidence removed |

**Infamy and the Kingdom:**
- Infamy 3+: Infamy bleeds into kingdom Infamy stat at +1 per chapter if player holds a leadership role
- Infamy 5+: Faction reputation hits begin — Aldori Swordlords −1 per chapter, Brevoy Crown −2
- Infamy 7+: Jamandi sends a formal letter. If unresolved: charter review triggers

---

## ⚖️ TRIAL SCENE

Triggered when player is arrested and cannot escape custody.

**Trial Structure:**
1. Player is brought before a magistrate or settlement authority
2. Evidence is presented (witnesses, physical evidence tier)
3. Player may speak in their own defense: Diplomacy or Deception vs DC 18
4. Player may call a companion as character witness: companion must be Friendly or better; adds +2
5. Player may reveal their ruler status (if applicable): automatic DC reduction of 4 — but Infamy gain +1 for the abuse of position

**Verdicts by evidence tier:**

| Evidence | Player Defense Success | Verdict |
|----------|----------------------|---------|
| NONE | Any | Acquitted; Reputation +1 (wrongful arrest) |
| SUBTLE | Crit Success | Acquitted; fine waived |
| SUBTLE | Success | Guilty; fine only |
| SUBTLE | Failure | Guilty; fine + 1d4 days detained |
| OBVIOUS | Crit Success | Guilty; reduced sentence (fine only) |
| OBVIOUS | Success/Failure | Guilty; sentence per severity |
| OBVIOUS + witness crit | Any | Guilty; full sentence |

**Sentences by severity:**

| Severity | Sentence |
|----------|----------|
| Petty | Fine: 10–50 gp |
| Moderate | Fine: 50–200 gp + banned from settlement 1d4 weeks |
| Serious | Fine: 200–500 gp + imprisoned 1d6 days + Infamy +1 |
| Capital | Execution (player may attempt escape) OR life imprisonment (escape arc) |

**Execution path:** Player has one chance to escape before sentence is carried out — Chase subsystem, 5 obstacles, guards are L = party level +2. Success: fugitive status. Failure: character death (or player accepts fate for narrative reasons).

---

## 🗡️ COMPANION REACTIONS TO CRIME

Companions who witness crimes react immediately and persistently.

| Companion | Petty | Moderate | Serious | Capital |
|-----------|-------|----------|---------|---------|
| **Valerie** | Disapproves silently | States objection formally | −1 Relationship; refuses to assist | −2 Relationship; may leave party |
| **Linzi** | Notes it; doesn't report | Writes about it; troubled | −1 Relationship; asks why | −2 Relationship; threatens to publish |
| **Tristian** | Asks if it was necessary | Prays openly; disapproves | −1 Relationship; refuses healing until apology | −2 Relationship; leaves if not addressed |
| **Harrim** | Indifferent | Finds it tiresome | Mildly approves (chaos) | Approves; +1 Brotherhood |
| **Regongar** | Approves | Approves +1 | Approves +1; offers help | Approves +2; wants in next time |
| **Amiri** | Ignores | Ignores unless victim was warrior | Disapproves if cowardly | −1 if victim couldn't fight back |
| **Nok-Nok** | Impressed | Very impressed | "Teach Nok-Nok?" | Legendary in his eyes; +1 Relationship |
| **Octavia** | Arches eyebrow | Notes it; no judgment | −1 if victim was vulnerable | −2 if victim was enslaved/powerless |
| **Jaethal** | Interested | Approves | Approves +1 | Approves +2; admires commitment |
| **Ekundayo** | Disapproves | −1 Relationship | −1 Relationship; cold for 1 session | −2 Relationship; formal objection |

**Companion assist in crime:**
Some companions will actively help with certain crimes if asked and relationship is Friendly+.

| Companion | Will assist with |
|-----------|-----------------|
| Regongar | Assault, extortion, intimidation |
| Nok-Nok | Theft (enthusiastically), distraction |
| Jaethal | Murder, assassination (if target "deserves it") |
| Octavia | Fraud, forgery, impersonation |
| Harrim | Will stand watch; will not report |

Asking a companion to assist who would refuse: −1 Relationship and they remember you asked.

---

## 💾 CRIME SAVE BLOCK

```json
"crime": {
  "infamy": 0,
  "active_bounties": [],
  "outstanding_fines": 0,
  "known_crimes": [],
  "witnesses_outstanding": [],
  "fugitive_regions": [],
  "trial_pending": false,
  "last_crime_chapter": null,
  "companion_crime_reactions": {}
}
```

**`known_crimes` entry format:**
```json
{
  "type": "murder",
  "severity": 4,
  "location": "Oleg's Trading Post",
  "chapter": 1,
  "witnesses": 1,
  "evidence_tier": "SUBTLE",
  "resolved": false
}
```

---

## 🖥️ CRIME COMMANDS

| Command | Output |
|---------|--------|
| `.crime` | Current Infamy, active bounties, outstanding warrants |
| `.crime history` | All logged crimes this campaign |
| `.bounty` | Active bounty hunters: location, level, distance |
| `.wanted` | Wanted status per region |
| `.trial` | Current trial status and available defense options |

---

## ⚠️ DESIGN RULES FOR THE DM

1. **Never punish crime automatically.** The system fires on witness results and evidence. If the player genuinely got away clean, they got away clean. Do not retroactively add witnesses.
2. **Consequences are lived, not announced.** Don't say "your Infamy increases." Show the wanted poster at the next settlement gate. Show the bounty hunter asking the innkeeper about someone matching the player's description.
3. **Companions are not the morality police.** They react once, clearly, then move on. They do not lecture repeatedly. Harrim's indifference is as valid as Tristian's prayer.
4. **Ruler crimes have political weight.** The player is building a kingdom. A ruler who murders merchants in their own territory is not just a criminal — they are a policy.
5. **Crime can be strategic.** Assassination of a faction leader, theft of a key document, framing a rival — these are valid campaign tools. Run the consequences faithfully, not punitively.
6. **Getting away with it is satisfying.** A clean crime with no witnesses and buried evidence should feel like a win. The system earns its tension by being fair in both directions.

---

*KM_CrimeSystem.md — Kingmaker PF2e Text Adventure | Crime & Infamy System v1.0*
*Uses: PF2e Thievery, Stealth, Deception, Intimidation core rules | No new mechanics invented*
