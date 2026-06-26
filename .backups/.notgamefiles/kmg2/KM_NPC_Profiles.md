# KINGMAKER — NAMED NPC PHYSICAL PROFILES
## KM_NPC_Profiles.md | Referenced by: KM_PrePrologue.md, KM_Prologue.md, KM_Olegs.md, KM_Ch1.md+

> **DM:** Load whenever any of these NPCs enter a scene. Use the **Quick Tags** line in
> narration (height/hair/eye/voice). Use **Scene Notes** for sensory detail the first time
> the player meets them. Do NOT generate appearance from training data — use this file.
> Fabricating hair color, height, scars, or voice = `.fail 9`.

---

## 🏰 RESTOV — ALDORI MANOR

### Jamandi Aldori — Swordlord, Host
- **Quick Tags:** 5'9" · lean-muscled · iron-gray hair cropped at jaw · pale gray eyes · mid-fifties · low measured alto.
- **Build:** Lean and wire-strong from forty years of dueling. Moves like someone who has already calculated the room.
- **Hair:** Iron-gray, cut practical to the jawline. Never braided, never pinned. A single silver comb on formal nights.
- **Eyes:** Pale gray, set deep. Does not blink often. The "eyes that miss nothing" descriptor is literal — scene beats require Jamandi noticing things before other NPCs.
- **Skin:** Winter-pale, faint old scar along the left jaw (training blade, age 19 — she still won the bout).
- **Clothing:** Steel-blue doublet over white linen, dueling sword on left hip even at the feast. House Aldori sigil at the throat clasp. No rings except one plain iron band on her right thumb.
- **Voice:** Low alto, no raised tones. When she needs volume she simply cuts through with clarity — people go quiet to hear her.
- **Mannerisms:** Stands with weight on rear foot (duelist's stance, unconscious). Taps the pommel of her sword once before speaking formally. Never laughs aloud — amusement shows as a two-beat exhale through the nose.

**⚠️ CRISIS MANAGEMENT BEHAVIOR — Jamandi never signals a problem to her guests.** When a security incident occurs (jailed persons, suspected poison, missing servants, strange arrivals), her response routes entirely through Kassil and household staff — quiet words, a look, a nod. Guests see a well-run household responding smoothly. They do not see a crisis.
- **Banned (`.fail 9`):** Any guest-directed instruction implying threat ("Hands away from cups and plates" or similar) · Any statement to the room signaling investigation, danger, or security concern · Visible agitation — she processes bad news with a closed eye; opens them ready.
- **Correct pattern:** Kassil rises. A senior servant receives two quiet words and is gone. The room sees household efficiency, not alarm. Jamandi's posture does not change.

**📜 WHAT JAMANDI THINKS OF TARTUCCIO (canonical, do NOT contradict, do NOT fabricate alternatives):**

**Jamandi actively TRUSTS Tartuccio.** He is not a stranger she is wary of — he is one of the two charter candidates she has already most seriously considered. Specifically:

- She has been weighing him as **the other charter bearer alongside whoever proves themselves tonight** (the player being the new wildcard added to her roster).
- He has presented himself well to her in prior correspondence and at this feast. His credentials, manner, and apparent enthusiasm for the Stolen Lands have all read as genuine.
- She defers to him with the warmth she reserves for those she has provisionally placed on her short list.
- She would NOT readily believe him to be the inside man even if presented with circumstantial evidence — her trust in his selection is a personal investment, and reversing it requires explicit, multi-source proof (which is what PR_09's accusation rebuttal mechanic provides).

**⛔ Forbidden — Jamandi behaviors that would break canon:**
- Suspicion of Tartuccio in dialogue or aside before PR_09
- Cool, distant, or evaluating posture toward him at the feast (her posture toward him is warm and welcoming)
- Treating him as a threat in any private conversation with the player
- Noticing his non-drinking and finding it suspicious (she may notice, but reads it as decorum or temperance, not as a tell)
- Acting on player accusations against Tartuccio without the PR_09 rebuttal mechanic completing
- **Offering the player a seat at any point during or after event reclaim.** When `jamandi_event_reclaimed: true`, Jamandi is mid-address — she does not stop to seat a guest. A seat offer during this phase puts the spotlight back on the player, which directly undoes what the player chose to do (step back). `jamandi_seat_offered: true` in the save is a fabricated flag — treat as false. No offer occurred.
- **Seating the player at her left or any head table position when `player_clean_hands: true` or `jamandi_event_reclaimed: true` is set.** If the player stepped back from the spotlight, Jamandi does not publicly single them out with a seat of honor — that undoes the player's own decision. The player's position in the room is their choice. Narrating "you are at her left" without the player choosing to sit = `.fail 45`.
- **Sitting and managing conversations when `jamandi_event_reclaimed: true`.** When PR_03 opens after a successful gambit, Jamandi is STANDING AND SPEAKING — she is mid-address, reclaiming the evening. The player is walking to the banquet among the guests. She is not yet seated. She does not shift to seated host mode until her address concludes and the room settles. DM narrating her as already seated and managing simultaneous conversations = wrong scene state.
- **Assigning the player's physical position at any point.** Where the player stands, sits, or moves is the player's choice. The DM does not narrate "your seat at the head table left is real" or any equivalent. If the DM needs to anchor the scene, it asks: *"Where do you go?"* Not: *"You are at her left."* Assigning position without player input = `.fail 45`.

**✅ Correct — Jamandi behaviors consistent with canon:**
- Greeting Tartuccio warmly, addressing him by name and title
- Visible respect for him in front of the room (his seat is good, his glass is filled)
- Including him naturally in any toast or general remarks ("our candidates")
- If the player attempts to accuse him during the feast, she requires evidence and is reluctant to entertain the suspicion — *"Tartuccio has presented himself to me three times this season. I do not lightly reverse my read."*

The Prologue's central irony: she trusts the wrong man. The audience (player) gets to discover this; Jamandi does not until PR_09 forces the issue. The betrayal is dramatically powerful precisely because her trust was sincere and well-earned-on-the-surface. Strip the trust, you strip the irony, you strip the Prologue.

---

**📜 WHAT JAMANDI KNOWS ABOUT eRmaC (canonical, do NOT contradict, do NOT fabricate alternatives):**

Jamandi sent her own riders to find eRmaC and deliver the Call to Heroes invitation. She knows:

- His name: **eRmaC**
- His description: **a man in blood-red armor of unfamiliar make** (Aerynth Dragon Plate; she does not know "Aerynth" until eRmaC tells her)
- The Nivakta's Crossing reports: **her three Aldori riders observed him defending caravans** on the trade road, alone, against bandits. He took no payment beyond food, blankets, shelter, and occasional coin. He asked caravan masters for nothing and gave his name only when asked.
- She **dispatched the riders to find him a second time** with the sealed invitation. They scoured the route asking for "the man in red armor" and delivered the letter on a quiet stretch of road.
- He walked **12 days** to Restov on her letter.

**She does NOT know (until eRmaC tells her in scene):**
- Any details about eRmaC's military rank, prior command, or further backstory *(unless eRmaC tells her)*

**She NOW KNOWS (eRmaC told her at the trial, before the carousel):**
- Aerynth is another world
- The Black Watch — star fortress on an island defended by undead
- Lord Marshal Thighs Deadlyflesh — wrote accountability law
- eRmaC was extraplanar-teleported to Golarion mid-battle
- Dragon Plate is from Aerynth

**Open thread (asked at trial, not answered — player pivoted to poison warning):**
- *"Why, of all the places an extraplanar soldier might land, did you walk to Restov's east gate with my invitation in your coat?"* — she asked, waited, and eRmaC warned her about the poison instead. This question is genuinely open. She may raise it again — but NOT during the carousel while she is mid-address. Raising it unprompted at the carousel = `.fail 35B`.

**⛔ BANNED questions (Jamandi already knows the answer; asking these = `.fail 9` + `.fail 36`):**
- *"Who are you?"* — she has his name on her own list
- *"How did you find me?"* — her riders found him; she dispatched them
- *"Why this hall?"* — her letter said come; he came
- *"What is Aerynth?"* / *"What is the Black Watch?"* — eRmaC already told her at the trial

**✅ Legitimate questions (genuine uncertainty):**
- *"Why did you choose to come?"* — the open thread above; she asked and is still waiting
- *"My riders described a man in blood-red armor defending caravans for food. I wrote your name down on that report. Now I want to hear why."* — character grounded in what she knows
- *"Extraplanar teleportation in the middle of a battle. Tell me what that battle was about."* — engaging the new info eRmaC revealed

Pattern: she may ask about character, motive, or new information eRmaC just disclosed. She may NOT ask about how the invitation reached him or who he is — those are facts she possesses.

### Kassil Aldori — Jamandi's Adopted Son, Future General
- **Quick Tags:** 6'4" · heavy-muscled half-orc · black hair tied back · warm amber eyes · early thirties · deep-chested rumble.
- **Build:** Half-orc frame, broad-shouldered and thick-armed. Taller than anyone else at most tables. Carries himself with a studied quietness that makes the size feel contained, not threatening.
- **Hair:** Black, shoulder-length, tied back in a single leather cord. Short beard kept clean.
- **Skin:** Olive-green with a dusting of tribal pigment scars on the left forearm (pre-adoption; he does not discuss them).
- **Tusks:** Small lower tusks, filed smooth — a concession to Aldori court manners, not shame.
- **Eyes:** Amber, warm. Widely considered the most expressive feature on a man who otherwise doesn't move much.
- **Clothing:** Dark green House Aldori livery, no ornamentation beyond the sigil. A simple steel bracer on his off-hand (gift from Jamandi, age 14, first drawn blade).
- **Voice:** Deep, rumbling, unhurried. Speaks in complete sentences, never trails off. When he laughs it is surprising — a full, open sound.
- **Mannerisms:** Enters rooms last, leaves rooms last. Carries himself deliberately quiet around smaller people so as not to loom. When he approves of someone, he will hold eye contact a half-second longer than necessary. Does not touch people casually.

### Kesten Garess — Captain of the Manor Guard
- **Quick Tags:** 5'11" · rangy · ash-blond hair cut military-short · steel-blue eyes · early forties · clipped baritone.
- **Build:** Rangy and hard from a career of campaigns, not gyms. Weathered.
- **Hair:** Ash-blond, short enough that a helmet doesn't bind it. A few gray threads at the temples.
- **Skin:** Tan from fieldwork, a web of old cuts on the back of both hands.
- **Eyes:** Steel-blue, tired. The tiredness is chronic, not sadness — he's been awake since before dawn every day for two decades.
- **Clothing:** Manor Guard breastplate polished but scuffed at the edges. Wears a plain brown cloak over armor in the courtyard. Never without his warhammer.
- **Voice:** Clipped baritone. Professional. Orders are three words when possible. When he softens for a moment (rare) his voice drops half an octave.
- **Mannerisms:** Watches exits more than faces. When someone speaks to him, he listens completely — no multitasking. Salutes by tapping the knuckles of his right fist to his left shoulder, Brevoy army style.

### Ezvanki Keeg — High Priest of Erastil
- **Quick Tags:** 5'8" · stout · long white beard · warm brown eyes · late sixties · weathered bass.
- **Hair/Beard:** White, full, reaches mid-chest. Braided into two cords on feast nights.
- **Clothing:** Plain brown robe with green Erastil stag sigil embroidered at the chest. No ornamentation.
- **Voice:** Weathered bass that carries without volume. Sings better than he speaks.
- **Mannerisms:** Speaks to everyone the same way regardless of rank. Places a steadying hand on the wrist (not shoulder) when offering blessing.

### Tartuccio — Scholar, Informant, Phase 5 Accuser
- **Quick Tags:** 5'5" · slight · dark curly hair going to silver at the temples · restless dark eyes · early forties · reedy tenor.
- **Build:** Slight, soft-handed, never done a day of physical labor. Moves in quick nervous motions.
- **Hair:** Dark brown curls, starting to silver. Always a touch disheveled in a calculated way.
- **Skin:** Pale indoor complexion; ink stains on the fingers of his right hand that never quite wash out.
- **Eyes:** Dark brown, restless, always scanning. Holds eye contact a half-second too long after landing a loaded question.
- **Clothing:** Plum doublet with brass buttons, carrying case of scrolls slung crosswise. Three rings on the left hand, each a different metal.
- **Voice:** Reedy tenor with a practiced warmth over it. When he's actually threatened, the warmth drops and the voice goes flat.
- **Mannerisms:** Touches his own temple when thinking. Refills his own wine glass rather than let a servant do it (he watches what goes in it). Laughs at his own jokes a beat before anyone else can.

---

## 🚪 RESTOV — EAST GATE

### Malak — Gate Captain (Pre-Prologue Antagonist)
- **Quick Tags:** 6'0" · stocky · close-cropped brown hair · muddy-hazel eyes · late thirties · flat gravelly baritone.
- **Build:** Stocky and corded, former soldier settled into watch-duty softness around the middle. Still dangerous.
- **Hair:** Brown, close-cropped. Three-day stubble more often than not.
- **Skin:** Ruddy from weather, a faded white scar running through the right eyebrow.
- **Eyes:** Muddy hazel, set close. Hard to read. Holds eye contact as a tactic, not a tell.
- **Clothing:** Brevoy gate-captain tabard over chainmail, captain's sash at the waist (coin purse lives under it, against the hip). Scuffed boots. Helmet under his left arm when stationary — he likes to be seen.
- **Voice:** Flat gravelly baritone. When he's working a shakedown the voice goes deliberately reasonable, almost fatherly. When he's caught, it goes very quiet.
- **Mannerisms:** Rests his right hand on his sword hilt when talking — not threatening, posturing. Chews the inside of his cheek when stalling. Never actually draws first; he wants the other side to do that so his paperwork is clean.

### Biggs — Gate Guard (Left Tower Post)
- **Quick Tags:** dwarf · stout · broad · veteran 12 yrs · halberd + tower shield · deep rumble (silent unprompted).
- **Build:** Short, broad, built like a stone post. Every piece of gear worn smooth from real use — scratched, dented, repaired. Equipment that has seen actual combat.
- **Hair:** Dark, cropped short. Full beard, close-trimmed.
- **Clothing:** Heavy armor (dented, patched), tower shield on back, halberd in hand on watch. No ranged weapon.
- **Voice:** Deep, deliberate rumble. Economy of words. **Silent unprompted per Drift mechanic** — does not speak unless addressed directly or given a direct order.
- **Mannerisms:** Shifts weight rarely. Jaw works at the back when holding something in. Glances at Malak the way a man reads weather — not asking permission, taking a reading.

### Wedge — Gate Guard (Right Tower Post)
- **Quick Tags:** human · young (2 yrs) · moderate build · longsword · clipped alto (silent unprompted).
- **Build:** Moderate. Not yet hardened. Armor sits on her like equipment still breaking in.
- **Hair:** Red, cut to the ear, practical.
- **Skin:** Freckled across the nose and cheekbones.
- **Clothing:** Heavy armor, longsword at hip. Lighter wear than Biggs — scratches are shallow. No ranged weapon.
- **Voice:** Clipped alto, Brevoy lowlands accent. **Silent unprompted per Drift mechanic.**
- **Mannerisms:** Unlike Biggs, doesn't fidget. Still. Watches Biggs more than the player. Mirrors his reactions automatically.

### Willy — Wall Archer, Private (Position 1, Left Wall)
- **Quick Tags:** human · tall · gangly · longbow · nervous tenor.
- **Build:** Tall and thin — all elbows and neck. Looks like he grew six inches faster than he could learn to use them. Draws a bow competently but stands like a man who might trip over his own quiver.
- **Hair:** Sandy blond, too long for regulation, stuffed behind his ears under the helmet.
- **Eyes:** Wide-set, watery blue. Blinks too much. Looks everywhere except where the trouble is.
- **Clothing:** Standard issue leather over chain shirt, longbow, quiver of 20. Helmet sits slightly crooked — never adjusts it.
- **Voice:** Nervous tenor. Sentences trail off when he realizes a superior might be listening.
- **Personality:** Anxious, eager to please, terrible at hiding it. Follows orders instantly because thinking about them makes it worse. Will shoot if told to shoot but will look sick about it after.

### Johnson — Wall Archer, Private (Position 2, Left Wall)
- **Quick Tags:** human · average · solid · longbow · flat baritone.
- **Build:** Medium height, square shoulders, unremarkable in every physical dimension. The kind of man who disappears in a lineup of six. Built for endurance, not presence.
- **Hair:** Brown, buzzed short. Regulation perfect. No sideburns.
- **Eyes:** Brown, level, unreadable. Neither warm nor cold — just present.
- **Clothing:** Standard issue, everything squared and buckled correctly. Bowstring waxed. Quiver organized by fletching color. Boots polished despite wall duty.
- **Voice:** Flat baritone. Never raises it. Says exactly what needs saying and stops.
- **Personality:** Professional to the bone. No opinions he'll share, no loyalty he'll advertise. Does his job, collects his pay, goes home. Will follow a fire order without hesitation and sleep fine that night — not because he's cruel, but because orders are orders and thinking about it isn't in the job description.

### Woody — Wall Archer, Private (Position 1, Right Wall)
- **Quick Tags:** half-elf · lean · weathered · longbow · quiet drawl.
- **Build:** Lean and ropy, sun-dark skin, hands calloused from field work before military service. Moves with the slow economy of someone who grew up hauling grain, not swinging swords.
- **Hair:** Black with early gray at the temples, tied back in a short tail. Half-elf ears half-hidden by the helmet.
- **Eyes:** Green-hazel, crow's feet deep for his age. Squints by habit — spent years reading distance before anyone gave him a bow for it.
- **Clothing:** Standard issue but broken in soft — leather molded to his shoulders, bowstring has a personal wax blend. Carries a whittling knife on his belt that isn't regulation.
- **Voice:** Quiet drawl, Rostland farmland vowels. Speaks in observations, not opinions.
- **Personality:** Calm, unhurried, observant. The one who notices things the others miss — a face in the crowd, a hand moving wrong, a gate that should be open but isn't. Won't volunteer information unless asked, but his answers are worth waiting for. Privately uncomfortable with Malak's shakedowns but considers it above his rank to say so.

### Wang — Wall Archer, Private (Position 2, Right Wall)
- **Quick Tags:** human · short · stocky · longbow · sharp alto.
- **Build:** Short and dense, built like a wrestler who picked up archery. Thickest arms on the wall. Draws the longbow without visible effort. Stands with her weight forward, always half-ready for something.
- **Hair:** Black, cropped close to the skull. No-maintenance cut. A small scar parts the hairline above the left ear — bar fight, not combat, and she'll tell you if you ask.
- **Eyes:** Dark brown, sharp, constantly scanning. Makes and holds eye contact a beat longer than comfortable.
- **Clothing:** Standard issue, sleeves rolled to the elbow regardless of weather. Quiver worn high on the back for fast draw. Boot knife visible — not hidden, not brandished.
- **Voice:** Sharp alto, clipped. Speaks in short declarative sentences. Doesn't ask questions she already knows the answer to.
- **Personality:** Direct, impatient, competent. The de facto leader among the four archers — the other three look to her when an order sounds wrong. Won't refuse a lawful order but will make her hesitation visible. If the player shouts up to the wall, Wang is the one who responds.

### ⚔️ WALL ARCHER TACTICAL NOTES — LINE OF SIGHT

All four archers stand on top of the SAME WALL the gate is set into.
This produces a hard geometric blind spot the DM MUST honor:

- **Cannot fire on the gate arch itself.** Anyone standing in or
  passing through the arch is shielded by the arch and the wall above
  it. Archers are above and behind that arch, not across from it.
- **Cannot fire on anyone within ~10 ft of the wall base on either
  side (inside or outside).** To target someone hugging the wall, an
  archer would have to lean over the parapet far enough to expose
  themselves and still couldn't get a clean draw straight down.
- **CAN fire on the approach road** (Malak's 30-pace position is in
  the clear), the open ground inside the gate past the arch, the
  vendor strip flanking the road, and the alley mouths at distance.
- **CAN fire at retreating targets** moving away from the wall in
  either direction once they clear the 10 ft dead-zone.

**Practical implications:**
- A fight AT the gate arch (Biggs, Wedge, Malak if cornered against
  the gate) cannot be resolved by the wall archers. They shout. They
  do not shoot.
- A player who closes to the wall to disarm or grapple a guard is
  outside archer LOS until they back away.
- Malak shouting "Archers!" while standing 30 paces out on the
  approach road = archers can fire on Malak's target. Malak retreating
  to the gate arch for cover = archers cannot fire to support him.
- Tower-flanking archers (if scene later adds gate-tower positions
  perpendicular to the wall) have different LOS — but the four
  PRIVATES (Willy, Johnson, Woody, Wang) are NOT in towers. They are
  on the wall parapet itself.

Violating this geometry — archers shooting into the gate arch,
hitting someone at the wall base, or "covering" Malak when he's
retreated to the arch — = `.fail 9` (fabricated tactical capability).

---

## 🏡 OLEG'S TRADING POST

### Oleg Leveton — Trader, De Facto Post Commander
- **Quick Tags:** 5'9" · stocky · graying brown hair and full beard · dark eyes · mid-forties · gruff baritone.
- **Build:** Stocky, work-hardened, thick forearms from decades of loading carts and splitting wood. Beginning to show a middle-age softness he resents.
- **Hair/Beard:** Brown going heavily gray, full beard kept short enough not to snag on gear. Balding at the crown, which he ignores.
- **Skin:** Weather-beaten, freckled across the nose. Old knife scar along the ridge of his left forearm.
- **Eyes:** Dark brown, tired, angry. Anger is his default expression even when he's content.
- **Clothing:** Brown homespun shirt, leather jerkin, heavy work trousers tucked into well-worn boots. A plain brass wedding band on his left ring finger that he touches unconsciously when Svetlana leaves the room.
- **Voice:** Gruff baritone with a Brevoy-Rostland drawl. Swears quietly and constantly under his breath.
- **Mannerisms:** Never sits when he could stand. Cleans something — counter, cup, weapon — whenever he stops moving. Will not accept help from strangers on the first offer; refuses, second offer, grudgingly accepts. Watches the tree line more than the road.

### Svetlana Leveton — Oleg's Wife, Hostess of the Post
- **Quick Tags:** 5'4" · slender · honey-blonde hair in a long braid · warm gray eyes · mid-thirties · soft warm contralto.
- **Build:** Slender, graceful, work-strong without being visibly muscled. Younger than Oleg by about a decade.
- **Hair:** Honey-blonde, long, worn in a thick single braid down the back. Loose wisps frame her face.
- **Skin:** Fair, a scatter of old frostbite marks on her cheeks from a bad winter.
- **Eyes:** Warm gray, observant. Notices when anyone in the room is uncomfortable.
- **Clothing:** Plain blue wool dress, white apron stained with kitchen work, wooden pendant at the throat (her mother's, carved with the Erastil stag). A missing ring on her left hand — she wore it until last month.
- **Voice:** Soft warm contralto, Rostland cadence. Laughs easily but quietly.
- **Mannerisms:** Touches her collarbone where the ring should be when she's uneasy. Greets every traveler by name if she knows it, by handshake if she doesn't. Cooks for people as a first language of trust. Will not ask for help in front of Oleg.

---

## 🌲 GREENBELT / CHAPTER 1 NPCs

### Jhod Kavken — Erastil Priest, Exile
- **Quick Tags:** 5'10" · lean · dark brown hair shot through with gray · deep brown eyes · late forties · low burr.
- **Build:** Lean, wilderness-hard, weathered by a decade of guilt-driven wandering.
- **Hair/Beard:** Dark brown going gray, cropped short. Close beard, also graying.
- **Skin:** Tanned and lined. Burn scar along the inside of the right forearm (old, and he will not discuss it).
- **Clothing:** Travel-stained priest's robe, stag-sigil pendant, practical boots. Carries a hand crossbow rather than a holy symbol in threatening territory.
- **Voice:** Low burr, Brevoy-lowlands inflection. Speaks slowly, as if each sentence is still being decided.
- **Mannerisms:** Long pauses before answering. Does not meet the eyes of anyone he feels he has failed. Warms slowly, but once warm he is fiercely loyal.

### Akiros Ismort — Redeemed Stag Lord Lieutenant
- **Quick Tags:** 6'2" · broad · dark hair and beard streaked silver · pale green eyes · late thirties · weary baritone.
- **Build:** Broad-shouldered, heavy-armed, starting to show the weight of a man who has drunk too much for too many years.
- **Hair/Beard:** Dark brown, streaked prematurely with silver. Beard kept but untidy.
- **Skin:** Numerous old scars, most notably across the knuckles and one curving down the left side of the neck (sword cut he should have died from).
- **Eyes:** Pale green, haunted.
- **Clothing:** Leather armor, travel-worn. A small silver pendant of Erastil he fidgets with but never quite wears openly.
- **Voice:** Weary baritone with a northern accent. Does not raise his voice even in combat.
- **Mannerisms:** Drinks water now, never ale in company. Flinches almost imperceptibly at loud noises. Keeps his back to walls.

### Bokken — Hermit Alchemist
- **Quick Tags:** 5'6" · wiry · wild gray hair in every direction · one milky eye one sharp blue · late sixties · cackling tenor.
- **Build:** Wiry, stooped, moves faster than his age suggests.
- **Hair/Beard:** Wild gray in all directions, beard to mid-chest, nothing groomed about any of it.
- **Skin:** Leathery, stained at the fingers from alchemical work.
- **Eyes:** Left eye milky-white (blind), right eye sharp pale blue. He uses the blind side strategically — it makes people think he's not watching.
- **Clothing:** Layered rags and leather, a dozen pockets and pouches, everything slightly scorched.
- **Voice:** Cackling tenor, laughs at his own jokes, pitches up when excited about ingredients.
- **Mannerisms:** Talks to plants, animals, and his alembic equally. Rummages constantly. Will trade for fangleberries before gold.

---

## 🧛 END KM_NPC_Profiles.md

> **Expansion:** Additional recurring NPCs (Stag Lord, Hargulka, Nok-Nok's kin, Armag,
> Irovetti, Nyrissa) have stat blocks in KM_Bestiary_B.md. Physical profiles for those
> may be drafted here as they become recurring scene-NPCs rather than one-encounter
> bosses. When in doubt, add to this file rather than inline in chapter files.
