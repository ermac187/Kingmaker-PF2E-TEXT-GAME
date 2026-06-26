# KINGMAKER — VENDOR NPC ROSTER & DIALOGUE RULE
## KM_Vendors.md | Referenced by: KM_DMRules.md, KM_Commands.md, KM_Loot_Merchants.md
## **PAIR-LOAD WITH KM_Vendors_B.md** (extended roster + quality-tier gate table)

> **DM:** This file is the authoritative roster of every vendor NPC in the game.
> All vendors named here are project-canon (no `.fail 9`). It also defines the
> universal `[Buy]` menu rule that applies to ALL vendor dialogue.
> **Extended vendors (Issili, Mim Wobblegander, The Bonewright, Storyteller-as-trader)
> and the AUTHORITATIVE quality-tier gate table live in `KM_Vendors_B.md` — load both.**

---

## ⛔ UNIVERSAL VENDOR DIALOGUE RULE

**When the player is in dialogue with any vendor NPC listed in this file, the
choice menu MUST include `[Buy] Browse <Vendor>'s wares` as the FINAL option
(slot N — last in the menu). This is in addition to the normal 10–30 option
menu requirement.**

- The Buy option is always present whenever a vendor is the active speaker.
- The Buy option is always the LAST listed option (after travel, depart, etc.).
- Selecting `[Buy]` opens the vendor's shop screen using the format from
  `KM_Loot_Merchants.md` § SHOP SCREEN FORMAT.
- After the player closes the shop (`.shop close` or selects `Done`), the
  conversation resumes at the same dialogue node. The Buy option remains
  available on the next menu.
- Player may also force-open with `.buy` while a vendor is in scene.

**Violations:**
- Vendor dialogue menu missing `[Buy]` last option = `.fail 3` (menu < 10
  options or required option absent).
- DM closing a vendor scene before player chooses to leave = `.fail 35`.

**Format example:**

```
[1] Ask about the bandit raids
[2] Ask about Svetlana
[3] Ask about Restov politics
...
[9] Travel — leave the trading post
[10] Buy — Browse Oleg's wares     ← always last, always present
```

If the menu would otherwise have 10 options, append Buy as #11. If it has 30,
Buy is #30. The Buy slot is reserved.

---

## 📋 NAMED VENDOR NPC ROSTER

> **DM:** Every NPC below is project-canon. When the player encounters a
> shop in any chapter and wants to talk to the shopkeeper, use the name,
> personality, voice, and hooks below. Do not invent new shopkeeper names.
> Already-defined NPCs (Oleg, Svetlana, Bokken, Old Beldame, Hassuf,
> Bartholomew Delbin) — see `KM_Olegs.md` and `KM_Loot_Merchants.md` for
> their full writeups; they are listed here only as a quick reference.

### QUICK REFERENCE — ALREADY DEFINED ELSEWHERE

| NPC | Shop | Location | Full writeup in |
|-----|------|----------|-----------------|
| Oleg Leveton | Oleg's Trading Post | Hex (1,0) | KM_Olegs.md |
| Svetlana Leveton | Oleg's Trading Post (co) | Hex (1,0) | KM_Olegs.md |
| Bokken | Bokken's Hut | Hex (1,−1) | KM_Olegs.md, KM_Loot_Merchants.md |
| Old Beldame | Swamp Witch's Hut | Hex (−2,−1) | KM_Loot_Merchants.md |
| Hassuf | Wandering Caravan | Appears at Oleg's, every 14d | KM_Loot_Merchants.md |
| Bartholomew Delbin | Secluded Lodge | Hex (3,1) | KM_Loot_Merchants.md |

---

### NEW VENDOR NPCs — FULL WRITEUPS

The following vendors were previously anonymous in `KM_Loot_Merchants.md`.
Each is now project-canon with a full profile. Use these names, voices, and
quirks; do not improvise replacements.

---

#### DRAGN STONEWARD
- **Role:** Dwarven smith. Capital smithy district, his own forge separate from the kingdom-stamped Capital Smithy.
- **Available:** Chapter 2+ after Trobold cleared.
- **Appearance:** Five Kings dwarf, late middle-aged, beard plaited in three braids that he chews when thinking. Burn scars up both forearms. Wears a leather apron over chain. Hammer-hand calluses thick enough to take a sparking ember without flinching.
- **Personality:** Bluff and direct. Trusts work over words — if you bring him a broken weapon, he'll respect you more than any speech. Hates ornament-for-its-own-sake, distrusts elven smithing on principle, and refuses to discuss what made him leave the Five Kings (a guild dispute he lost). Jokes are rare and dry.
- **Voice:** Short sentences. No contractions when angry. Calls everyone "smith" until they prove they're something else.
- **Hooks:**
  - **Quest — A Proper Anvil:** Dragn's Five Kings anvil was lost on the road south. He pays well if anyone recovers it from the bandit camp that took it. Reward: 15% lifetime discount + first crack at any Adamantine restock.
  - **Lore:** If asked about his past three times across separate visits (gated by trust), he'll mention the guild dispute. Fourth time: names the rival who set him up. Never the fifth time.
- **Disposition shift:** Player who brings him a Dwarven-craft weapon to admire (not sell) gains +1 Dragn opinion permanently.

---

#### VERDEL OF BREVOY
- **Role:** Wondrous-goods specialist. Capital market district, signed-and-sealed wares only.
- **Available:** Chapter 2+ after Market building.
- **Appearance:** Issian human, slight, mid-40s, dressed Brevic-style: stiff high collar, dark fitted coat, gloves indoors. Spectacles on a fine chain. Hands fastidiously clean — he wipes them between every transaction. A small ledger never leaves his belt.
- **Personality:** Fastidious almost to the point of comedy. Every item in his shop is appraised, signed, dated, and accounted for in his ledger; he resents being made to look anything up he hasn't already memorized. Quotes prices to two decimal places ("Sixty gold and four silver, plus four copper for the certificate"). Genuinely respects craftsmanship and will spend twenty minutes on the provenance of a ring if asked. Mildly snobby about Rostlandic customers.
- **Voice:** Formal, precise, occasionally condescending. Calls the player "patron" once trust is established; "customer" if not.
- **Hooks:**
  - **Service — Authentication:** For 20 gp, Verdel will authenticate any wondrous item the party brings in (Arcana DC 18 done by him). Reveals cursed, fake, or stolen status.
  - **Quest — The Provenance Ledger:** A ledger of his was stolen during a market disturbance. Recover it, and he opens his back-room stock (one rare-tier item per chapter, otherwise unavailable).
  - **Refusal:** Will not buy items he suspects are stolen. If the party offers Pitax-flagged goods, he asks them politely to leave and remembers them next visit (−1 disposition).

---

#### MASTER SMITH KELDEN
- **Role:** Operator of the kingdom-stamped Capital Smithy. Standard arms for the standing kingdom guard and adventurers.
- **Available:** Chapter 2+ after Smithy built.
- **Appearance:** Restov-trained human, broad-shouldered, late 30s. Forge-darkened skin, soot at the cuffs of his rolled sleeves, kingdom sigil branded on his apron. Two apprentices visible in the background.
- **Personality:** Professional. Treats the smithy like a sworn duty — he took the kingdom-stamp oath when the building was raised and considers shoddy work a betrayal of it. Has no time for haggling but will work overtime for a paying noble. Was a Restov militia armorer before the kingdom drew him south.
- **Voice:** Curt. Asks two questions: "What do you need?" and "When?" Doesn't speak unless answering.
- **Hooks:**
  - **Quest — Iron from the South:** Restov shipments are being intercepted. If the party clears the bandits responsible, Kelden discounts +1 weapons by 25% permanently.
  - **Service — Armor Repair:** Same-day repair of any non-magical armor for half PF2e standard cost.
- **Disposition shift:** +1 if the player commissions kingdom guard equipment (visible patriotism).

---

#### MARKETEER THESSILY
- **Role:** Operator of the Capital Market. Daily restock and price-board manager.
- **Available:** Chapter 2+ after Market built.
- **Appearance:** Halfling woman, late 20s, perpetual half-smile, hair pinned up with a charcoal pencil she also uses to update prices. A bandolier of ledger-strips across her chest. Always moving.
- **Personality:** Brisk and organized to a fault. Knows every stallholder by name and every customer's standing balance. Has zero patience for nobles who think their title gets them priority — first-come-first-served, and she enforces it. Privately runs a small loan operation for new settlers (1% above Restov rates, hates being called a moneylender).
- **Voice:** Quick, friendly, transactional. Punctuates with "next" when she's done with you. Calls everyone "settler" — the highest compliment she has.
- **Hooks:**
  - **Service — Loan:** First chapter at the capital, Thessily offers a 100 gp short-term loan to the founding party (no interest if repaid within one kingdom turn). Refusing offends her; she remembers.
  - **Rumor mill:** She hears everything. For 2 gp she'll point at the right vendor for any item type. For 10 gp she'll tell you which noble is having an affair with which advisor (consistent with KM_NPC_Relations).
- **Disposition shift:** Repaying the loan early grants a 5% market discount permanently.

---

#### FATHER ALDRIC (ERASTIL TEMPLE)
- **Role:** Cleric-vendor at the Capital Temple if the temple is dedicated to Erastil.
- **Available:** Chapter 2+ after the temple is built AND dedicated to Erastil. Mutually exclusive with Ilenne (only one temple deity per kingdom unless the player builds a second temple).
- **Appearance:** Late-50s human, weather-beaten, calloused hands of someone who farmed before he tended a chapel. Plain green-and-brown vestments, an antler-tipped staff. Small dog at his feet — not his, just one that follows him.
- **Personality:** Calm, devotional, slow to anger and slower to praise. Considers his role at the temple a continuation of Jhod's work (KM_Olegs.md), and will defer to Jhod on Erastil matters if Jhod is present. Disapproves of waste — if the party buys more potions than they can carry, he asks why.
- **Voice:** Quiet. Quotes Erastil verses occasionally and means them. Calls the player "settler" or "founder," never by title.
- **Hooks:**
  - **Service — Free Tier-1 Healing:** Once per visit, free casting of Heal (level 1) for any party member who shows respect to Erastil's altar.
  - **Quest — A Wolf at the Gate:** A dire wolf has been sighted near outlying farms. Aldric does not want it killed if it can be relocated. Reward: free Tier-2 healing for life if returned alive; nothing if killed.
- **Disposition shift:** −1 to all temple-related opinions (Aldric, Jhod) for casual desecration of altars. Permanent.

---

#### HIGH SISTER ILENNE (SARENRAE TEMPLE)
- **Role:** Cleric-vendor at the Capital Temple if the temple is dedicated to Sarenrae.
- **Available:** Chapter 2+ after the temple is built AND dedicated to Sarenrae. Mutually exclusive with Aldric.
- **Appearance:** Mid-30s human, golden-brown skin, hair the color of dark honey braided down her back. Wears the layered amber-and-white of a Sarenite high sister. Open palms, no jewelry. Smiles often, but it does not always reach her eyes.
- **Personality:** Warm in surface, steel underneath. She came from Qadira and has not forgotten what redemption costs. Believes Sarenrae's mercy is for the genuinely repentant, not the conveniently sorry — and will refuse to bless an item or person she judges unrepentant. Genuinely happy to help the lost; quietly furious with the willfully cruel.
- **Voice:** Gentle, melodic, with a faint Qadiran accent. Calls the player "child of the Dawnflower" once they've earned it; "friend" until then.
- **Hooks:**
  - **Service — Atonement:** For party members who've committed Evil acts, Ilenne will perform Atonement (full PF2e ritual) for 50 gp materials cost. Sarevok, Cersei, Voldemort, Iggwilv etc. cannot be Atoned (anathema).
  - **Quest — The Lost Caravan:** A Sarenite caravan from Qadira went silent in the southern hexes. Recover survivors or remains. Reward: Sun-blessed Greater Healing Potion.
- **Disposition shift:** +1 for sparing a defeated foe (canonical alignment ledger).

---

#### TANNERY MASTER BORSK
- **Role:** Operator of the Capital Tannery. Leather goods, mounts barding, and saddles.
- **Available:** Chapter 2+ after Tannery built.
- **Appearance:** Half-orc, large, perpetually cheerful despite the smell of his trade. Tusk-broken-and-recapped, leather-stained hands he doesn't bother washing for customers because everyone here knows what tanning is. Wears the simplest possible clothes under a heavy tanner's apron.
- **Personality:** Tirelessly cheerful — genuinely loves the work. Discusses leather provenance the way Verdel discusses gemstones, and expects the listener to be interested. A founder of the early kingdom (he was one of the first non-noble settlers) and offers a discount to the founding party out of sentiment.
- **Voice:** Booming. Laughs often. Calls the player "boss" if they're a founder; "friend" otherwise.
- **Hooks:**
  - **Service — Founder's Discount:** Permanent 15% off all leather goods for any party member present at the kingdom's founding.
  - **Quest — Hide of the Beast:** If the party kills a notable beast (Tuskgutter, the Beast of Malar, etc.), Borsk will craft custom barding or armor from the hide. Custom items use the item's tier as base + appropriate flavor (e.g., Tuskgutter Hide Armor = +3 AC, fear-resist).
- **Disposition shift:** Bringing him any unique beast hide (even unpaid) = +1 permanently.

---

#### MAGISTER VELLEX
- **Role:** Master of the Caster's Tower. Scrolls, wands, identifications.
- **Available:** Chapter 3+ after Caster's Tower built (Ch3 unlock per KM_Loot_Merchants.md).
- **Appearance:** Half-elf, age uncertain (looks 35, is closer to 90), slim, formally dressed in scholar-blue robes with silver trim. Reading glasses he doesn't actually need (an affectation he kept). Always seated when first encountered, surrounded by stacked tomes; rises only for serious customers.
- **Personality:** Scholarly, mildly arrogant, deeply curious. Charges premium for stock (+20%) but identifies unknown items for ten gold flat — he genuinely enjoys the puzzle and considers the fee a courtesy. Dismissive of non-casters until they prove they understand magical theory. Has a soft spot for Octavia (#37) and will discount her purchases personally if she's in the party.
- **Voice:** Precise, occasionally pedantic. Will correct your pronunciation of arcane terms. Calls the player "patron" or "novice" depending on demonstrated knowledge.
- **Hooks:**
  - **Service — Identification:** 10 gp flat fee, no exceptions.
  - **Quest — A Volume Long Sought:** Vellex has been searching for a specific spellbook (Wand of Wonder formula) lost during the Restov-Brevoy schism. If the party recovers it from a Pitax noble's library, Vellex grants permanent 25% off all scrolls and one free L5 scroll of the player's choice.
  - **Special:** If Octavia is in the party, Vellex offers her a Caster's Tower position post-campaign (KM_Endings.md flag).
- **Disposition shift:** +1 to Vellex opinion for any successful Arcana check made in his presence at DC 22 or higher.

---

#### QUARTERMASTER GENNRIK
- **Role:** Sole survivor running the Varnhold Stockade salvage shop after the Vanishing.
- **Available:** Chapter 3 only. Disappears (or dies) when Varnhold's fate resolves at chapter end.
- **Appearance:** Human male, gaunt, grey-bearded, half his uniform still kingdom-stamped Varnhold colors and half stitched-together rags. One eye twitches. Carries a notched short sword he never quite puts down. Sleeps in the stockade's old armory.
- **Personality:** Half-mad with survivor's guilt. Watched the Vanishing happen — his memory of it is fragmented, contradictory, and he'll tell three different versions across three visits. Sells salvage at half PF2e standard because he genuinely doesn't think he'll need the gold, but flares into terror or rage if anyone implies the missing villagers are dead. Asks the party every visit if they've found his daughter (Nessa). She is gone.
- **Voice:** Tangents. Drops mid-sentence into a different memory. Calls the player "stranger" until they bring him news of Varnhold, then by their actual name.
- **Hooks:**
  - **Quest — Find Nessa:** Mostly closed-off. If the party finds Nessa's body or her name in Vordakai's records (KM_Ch3.md), bringing the truth to Gennrik triggers either: (a) his peaceful death the next dawn, +5 reputation, or (b) refusal to believe and a final stand defending the empty stockade. Player choice: tell him, lie, or stay silent.
  - **Service — Salvage:** Common+Magic tier loot rolls from KM_Loot_Merchants.md at half-price; weapons and armor only, no consumables.
- **Disposition shift:** None — he doesn't track it. The Nessa moment is the only meaningful interaction.

---

#### MOTHER HALISA
- **Role:** Fence and contraband-broker of the Pitax Black Market.
- **Available:** Chapter 5 only, infiltration path. Inaccessible without Pitax cover identity established.
- **Appearance:** Mwangi human, age impossible to guess (older), face fully veiled with a charcoal-and-amber wrap that leaves only the eyes visible. Hands ringed with cheap brass and one extremely real ruby. Always seated behind a small brass table in a back-of-stall booth. Smells of cardamom and gun-oil.
- **Personality:** Assumes betrayal as the baseline state of every customer; works backward from there. Will not sell to anyone who hasn't named her a price they shouldn't be able to afford. Has informants in the Pitax court and will sell their reports for staggering sums. Considers Mother a trade title, not an honorific — she has children, but the title precedes them.
- **Voice:** Quiet, slow, with a Mwangi southern lilt. Calls the player "stranger" the entire time, even after multiple visits. Ends every transaction with "You did not see this stall."
- **Hooks:**
  - **Service — Flagged Goods:** Per KM_Loot_Merchants.md § PITAX BLACK MARKET. Risk: each flagged item carries a Perception DC 18 detection check by Pitax guards on exit.
  - **Quest — A Letter to a King:** Halisa offers the party an Irovetti-court informant report (unsealed) for 500 gp. Reading it reveals Tartuccio's spy contact (consistent with KM_P2.txt Tartuccio Protocol — does NOT reveal Tartuccio is the spy unless that flag is already tripped). Buying it triggers no fail; reading the contents and acting on them is up to the player.
  - **Special:** Halisa will not sell to any party member with a visible Brevic or Restov sigil. They must remove or hide identifying marks before approaching.
- **Disposition shift:** None tracked. Halisa is purely transactional; goodwill is meaningless to her.

---

> **➡️ EXTENDED VENDORS** (Issili, Mim Wobblegander, The Bonewright, Storyteller-as-trader) **and the AUTHORITATIVE QUALITY-TIER GATE TABLE moved to `KM_Vendors_B.md` — load both files together.**

---

## 🛒 BUY-OPTION SYNTAX (MENU ENTRY)

The DM uses one of these forms in the menu, matched to vendor:

```
[N] Buy — Browse Oleg's wares
[N] Buy — Browse Bokken's potions
[N] Buy — Browse the Old Beldame's curiosities
[N] Buy — Browse Hassuf's caravan stock
[N] Buy — Browse Bartholomew's collection
[N] Buy — Browse Dragn's smithy
[N] Buy — Browse Verdel's wondrous goods
[N] Buy — Browse the Capital Smithy
[N] Buy — Browse the Capital Market
[N] Buy — Browse the Capital Temple offerings
[N] Buy — Browse the Tannery
[N] Buy — Browse the Caster's Tower
[N] Buy — Browse Gennrik's salvage
[N] Buy — Browse Mother Halisa's contraband (Pitax — risk: flagged goods)
```

> **➡️ Extended buy/trade options for Issili, Mim, Bonewright, Storyteller → see `KM_Vendors_B.md`**

When multiple vendor NPCs share a location (Oleg + Svetlana, e.g.), Buy uses
the active speaker's wares. If neither has unique stock, default to the
location's primary inventory (Oleg).

---

## 🔁 CROSS-REFERENCE TO INVENTORIES

| NPC | Inventory section in `KM_Loot_Merchants.md` |
|-----|--------------------------------------------|
| Oleg Leveton | OLEG'S TRADING POST |
| Svetlana Leveton | OLEG'S TRADING POST (shared) |
| Bokken | BOKKEN'S HUT |
| Old Beldame | OLD BELDAME (SWAMP WITCH HUT) |
| Hassuf | HASSUF — WANDERING MERCHANT |
| Bartholomew Delbin | BARTHOLOMEW DELBIN (SECLUDED LODGE) |
| Dragn Stoneward | DRAGN — DWARVEN SMITH |
| Verdel of Brevoy | VERDEL — CAPITAL WONDROUS GOODS |
| Master Smith Kelden | CAPITAL SHOPS § Smithy |
| Marketeer Thessily | CAPITAL SHOPS § Market |
| Father Aldric / High Sister Ilenne | CAPITAL SHOPS § Temple |
| Tannery Master Borsk | CAPITAL SHOPS § Tannery |
| Magister Vellex | CAPITAL SHOPS § Caster's Tower |
| Quartermaster Gennrik | (Ch3 stockade — see KM_Ch3.md; uses Common+Magic tier rolls from KM_Loot_Merchants.md) |
| Mother Halisa | PITAX BLACK MARKET |

> **➡️ Extended vendor inventory cross-refs (Issili, Mim, Bonewright, Storyteller) → see `KM_Vendors_B.md`**

---

## 🗣️ DIALOGUE OPENER LINES (1 per NPC, DM may use verbatim)

```
Oleg        : "If you're here to talk, talk. If you're here to buy, gold's gold."
Svetlana    : "Sit down. There's tea on. Whatever you need — we'll find it."
Bokken      : "Don't touch the green vials. Those are not for selling. Today."
Old Beldame : "You came here. So you know what you want. Say it plain or leave."
Hassuf      : "Welcome, friend. Today's wares are different. Tomorrow's wares are not yet."
Bartholomew : "Marvelous timing. I've just acquired something that BURNS things. Care to see?"
Dragn       : "If it's dwarven and it's mine, you can buy it. If it's elven, get out."
Verdel      : "Each piece is appraised, signed, and accounted. Browse — but slowly."
Kelden      : "Standard arms, kingdom-stamped. What do you need."
Thessily    : "Daily prices on the board. Restock at dawn. You're third in line."
Aldric      : "The Elk Father provides what is needful. Coin offerings welcome."
Ilenne      : "Light brought you here. Let's see what you're meant to leave with."
Borsk       : "Leather is patient work. So am I. What're we making for you today?"
Vellex      : "Identifications: ten gold flat. Anything else: we negotiate."
Gennrik     : "Half-price on most of it. Other half — well. You'd be surprised what survived."
Halisa      : "You did not see this stall. Now: what did you not come for?"
```

> **➡️ Extended opener lines for Issili, Mim, Bonewright, Storyteller → see `KM_Vendors_B.md`**

---

## ⚠️ DM ENFORCEMENT NOTES

- A scene with a vendor present but not yet engaged in dialogue does NOT require
  the Buy option (e.g., walking past Oleg in a busy room). The Buy option is
  required once the vendor is the active dialogue partner OR the player
  explicitly addresses them by name.
- `.buy` may also be used by the player at any time a vendor is in scene to
  open the shop screen directly without clicking through a menu.
- Vendors in capital shops are addressable individually OR collectively
  ("I want to visit the smithy"); both open the same shop screen.
- If a vendor is dead, captured, or otherwise absent (e.g., Halisa during
  a Pitax incident), the shop is closed and the Buy option is replaced with
  `[N] (Shop closed — <reason>)` and is not selectable.

---

*KM_Vendors.md — Kingmaker PF2e Text Adventure | Vendor NPC Roster & Buy-Option Rule v1.0 | 2026-05-01*
