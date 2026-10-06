# World Architecture: SF → NYC → Jeddah → Riyadh → Italy → Our Wedding

Phase: **world design only**. Nothing here is code, final art, mechanics, dialogue, or sound.

**Final count:** 19 playable rooms and 6 transition scenes (one of them a 3-second micro-cut).

**Process:**
1. Five city agents wrote proposals, 20 rooms in total.
2. The Director integrated them into an 18-room draft.
3. An Opus critic attacked the draft.
4. The Director revised it into the 19-room final below.

---

## Director's ground rules (apply to every room)

### Scale
Each room is a small diorama of about 1–2 screens, at the scale of the reference image.
- **MEDIUM** is the default size.
- **LARGE** is capped at 3 rooms: Midtown, KAFD Wadi, and the Garden Ceremony.
- The ceremony is the biggest room in the game.

### Chapters, not one trip
The acts are chapters of the relationship, not one continuous 3-day itinerary.
- Every inter-city transition ends on a **postcard** carrying a chapter title. This makes each jump read as "a new chapter" without needing clock-accurate travel.
- Spatial continuity is strict: you always leave through something and arrive through something.
- Temporal continuity is per-act.

### Who owns which visual motif
Each motif belongs to exactly one place:

| Motif | Belongs to |
|---|---|
| Fog | San Francisco |
| Neon and bare bulbs | New York |
| Fanous lanterns and amber sodium light | Jeddah |
| Glass and tower-crown lighting at blue hour | Riyadh |
| String lights, white ribbons, the open valley vista at night | Italy only |

No other act uses string lights or a big "lights switch on" moment.

### Mementos (set dressing only, no mechanics)
Each chapter visibly contains one small object. All of them reappear on the getting-ready dresser and the reception tables in Italy.

| Chapter | Memento |
|---|---|
| SF café | Polaroid |
| Crissy Field | Sand dollar |
| NYC | Library-lion keychain |
| Jeddah | Entrecôte matchbook |
| Riyadh | Finjan coffee cup |

### Cameo NPCs
One named local per chapter reappears at the wedding reception:
- **SF:** Barista
- **NYC:** Stoop neighbor with the bodega cat
- **Jeddah:** Entrecôte waiter
- **Riyadh:** Coffee-kiosk host
- **Italy:** Florist, who appears in the piazza and on the road

### Partner
The partner walks beside the player for the entire game, until the Villa Courtyard. There they are taken away, and the player is alone for the first time. That separation is the climax setup.

---

## DELIVERABLE A — Master World Flow

```
ACT 1 · SAN FRANCISCO  (morning fog → clear noon)
SF_01_OUR_STREET            start on our stoop
↓  corner café front door
SF_02_CORNER_CAFE
↓  back patio gate
SF_03_LYON_STREET_STEPS
↓  Presidio stone gate at the bottom
SF_04_CRISSY_FIELD          fog lifts → Golden Gate revealed
↓  car in the beach lot
[T1 · POSTCARD: SF → NYC]

ACT 2 · NEW YORK  (late afternoon → night)
NYC_01_42ND_ST_BRYANT_PARK
↓  subway entrance
[T2 · MICRO-CUT: subway ride uptown]
NYC_02_BROWNSTONE_BLOCK
↓  our building's stoop door (stairwell fade)
NYC_03_ROOFTOP_NIGHT
↓  plane lights cross the skyline
[T3 · POSTCARD: NYC → JEDDAH]

ACT 3 · JEDDAH  (warm night)
JED_01_AIRPORT_ARRIVALS
↓  waiting car (door fade)
JED_02_CORNICHE
↓  lantern arch, inland
JED_03_ENTRECOTE_STREET
↓  front door
JED_04_ENTRECOTE_INTERIOR
↓  leave after dinner
[T4 · BOARDING-PASS STAMP: JEDDAH → RIYADH]

ACT 4 · RIYADH  (golden hour → blue hour)
RUH_01_KAFD_WADI            rising out of the metro canopy
↓  top steps between the towers
RUH_02_KAFD_PLAZA           the promise
↓  camera rises; tower crowns become stars
[T5 · POSTCARD: RIYADH → ITALY]

ACT 5 · ITALY / WEDDING  (golden afternoon → sunset → string-lit dusk → night)
ITA_01_HILL_TOWN_PIAZZA     first white ribbon
↓  east gate arch
ITA_02_CYPRESS_ROAD         ribbons on every post
↓  estate gate
ITA_03_VILLA_COURTYARD      partner is taken away
↓  villa front door
ITA_04_GETTING_READY        alone; mementos on the dresser
↓  back French doors
ITA_05_GARDEN_CEREMONY      partner waiting at the arch; vows
↓  through the arch
ITA_06_RECEPTION_TERRACE    valley opens; everyone is here
↓  last dance
[T6 · ENDING]
```

The only branch is backtracking inside a city. Every room has exactly one story-forward exit.

---

## DELIVERABLE B — Master Room Table

| # | ID | City | Room name | Purpose | Size | From | To |
|---|---|---|---|---|---|---|---|
| 1 | SF_01_OUR_STREET | San Francisco | Our Street | Opening: meet "us" and set the tone | MEDIUM | Game start | SF_02 |
| 2 | SF_02_CORNER_CAFE | San Francisco | The Corner Café | Warm intimate memory; first cameo and memento | SMALL | SF_01 | SF_03 |
| 3 | SF_03_LYON_STREET_STEPS | San Francisco | Lyon Street Steps | Descent toward the bay; first vista; anticipation | MEDIUM (vertical) | SF_02 | SF_04 |
| 4 | SF_04_CRISSY_FIELD | San Francisco | Crissy Field | Fog lifts and the Golden Gate is revealed; coastal payoff; departure | MEDIUM | SF_03 | T1 |
| 5 | NYC_01_42ND_ST_BRYANT_PARK | New York | 42nd St & Bryant Park | "The world got bigger"; densest street | LARGE | T1 | T2 |
| 6 | NYC_02_BROWNSTONE_BLOCK | New York | Brownstone Block | Quiet residential counterweight; where we stayed | MEDIUM (vertical) | T2 | NYC_03 |
| 7 | NYC_03_ROOFTOP_NIGHT | New York | The Rooftop | Night-skyline romance; NYC's emotional peak | MEDIUM | NYC_02 | T3 |
| 8 | JED_01_AIRPORT_ARRIVALS | Jeddah | Arrivals & Curb | Stepping into warm Saudi night air | SMALL-MEDIUM | T3 | JED_02 |
| 9 | JED_02_CORNICHE | Jeddah | The Corniche | Jeddah as a place: Red Sea walk | MEDIUM (wide) | JED_01 | JED_03 |
| 10 | JED_03_ENTRECOTE_STREET | Jeddah | Entrecôte Street | Anticipation; lively Jeddah street life | SMALL-MEDIUM | JED_02 | JED_04 |
| 11 | JED_04_ENTRECOTE_INTERIOR | Jeddah | Inside Entrecôte | Act 3 payoff: the dinner memory | MEDIUM | JED_03 | T4 |
| 12 | RUH_01_KAFD_WADI | Riyadh | KAFD Wadi Approach | The impressive approach; futuristic scale | LARGE (vertical) | T4 | RUH_02 |
| 13 | RUH_02_KAFD_PLAZA | Riyadh | KAFD Plaza & Terrace | Human-scale future; the promise | MEDIUM | RUH_01 | T5 |
| 14 | ITA_01_HILL_TOWN_PIAZZA | Italy | The Piazza | Dreamy Italy; first wedding hint | MEDIUM | T5 | ITA_02 |
| 15 | ITA_02_CYPRESS_ROAD | Italy | Cypress Road | Hints accumulate; the realization | MEDIUM | ITA_01 | ITA_03 |
| 16 | ITA_03_VILLA_COURTYARD | Italy | Villa Courtyard | It's a wedding; the partner is taken away | MEDIUM | ITA_02 | ITA_04 |
| 17 | ITA_04_GETTING_READY | Italy | The Getting-Ready Room | Alone; the whole journey on one dresser | SMALL | ITA_03 | ITA_05 |
| 18 | ITA_05_GARDEN_CEREMONY | Italy | Garden Ceremony | The climax: aisle, arch, vows | LARGE (largest) | ITA_04 | ITA_06 |
| 19 | ITA_06_RECEPTION_TERRACE | Italy | Reception Terrace | Resolution: valley vista, everyone you met | MEDIUM | ITA_05 | T6 |

**Room count by act:**

| Act | Rooms |
|---|---|
| San Francisco | 4 |
| New York | 3 |
| Jeddah | 4 |
| Riyadh | 2 |
| Italy | 6 |
| **Total** | **19** |

**LARGE rooms (3):** NYC_01, RUH_01, ITA_05.

---

## DELIVERABLE C — Detailed Room Specs

### ACT 1 — SAN FRANCISCO
**Palette:** fog grey, sea-green hedges, pastel facades, cool air with warm windows.
**Light:** morning fog that burns off to a clear noon.

---

#### SF_01_OUR_STREET
- **ROOM NAME:** Our Street
- **CITY / REGION:** San Francisco, Pacific Heights
- **STORY PURPOSE:** The first screen of the game. "This is us, this is where it started."
- **WHY THIS ROOM EXISTS:** The opening has to say "San Francisco" and "us" within one screen.
- **VISUAL SUMMARY:** A sloped residential street climbing gently from left to right. A row of pastel bay-window Victorians and Edwardians sits along the top. Morning fog hangs at the top of the frame.
- **KEY LANDMARKS:**
  - Our Victorian (butter-yellow, bay window, tiny stoop, two potted plants, a mailbox) at left-center
  - The Corner Café on the corner building at the far right
- **ENVIRONMENTAL DETAILS:**
  - Stair-stepped sidewalk on the slope
  - Street trees, power lines, a parked compact car angled into the curb
  - A gull on a lamp post, a newspaper on a stoop
  - A neighbor's cat in a window
- **APPROXIMATE SHAPE:** Horizontal street on a slope, about 1.5 screens wide.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Game start. The player and partner are on our stoop at left-center.
- **EXIT(S):**
  - **Café door** (top-right): the corner building's glass door under a green awning.
  - **Left edge:** the street drops downhill into thick fog. This is a soft visual boundary (moving boxes and the fog wall), not an exit.
- **DIRECT CONNECTIONS:** SF_02 (café door).
- **PLAYER FLOW:** Step off the stoop, walk right and uphill along the sidewalk past the neighbors' houses, and reach the café's awning on the corner.
- **IMPORTANT VISUAL MOMENT:** The first frame: two small figures on a pastel stoop in soft fog.
- **IMPORTANT STORY MOMENT:** The introduction of the couple. The partner suggests coffee first. This is a story nudge, not a gate.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Tree canopy and hedge along the bottom edge
  - Stoop railings and lamp posts
- **BACKGROUND DETAILS:**
  - Stacked rooflines and chimneys going up the hill
  - The fog bank
  - A sliver of grey bay far off at the top-right
  - **The Golden Gate is deliberately NOT visible.** It is saved for SF_04.
- **RECOGNIZABILITY:** Bay-window row houses on a steep grade in fog. That reads as SF instantly.
- **TRANSITION NOTES:** None.

---

#### SF_02_CORNER_CAFE
- **ROOM NAME:** The Corner Café
- **CITY / REGION:** San Francisco, Pacific Heights (the corner of Broadway and Lyon)
- **STORY PURPOSE:** A warm, intimate memory spot, such as "our first coffee" or "our first date". The creator should personalize this.
- **WHY THIS ROOM EXISTS:** It is the only SF interior. It gives the cool outdoor act a warm pocket, and it introduces the first cameo NPC and the first memento.
- **VISUAL SUMMARY:** A small, warm wooden café. The windows are steamed up, and fog presses against the glass outside.
- **KEY LANDMARKS:**
  - The window booth ("our table")
  - The espresso counter with a pastry case
  - A corkboard of polaroids, one of them ours (the memento)
- **ENVIRONMENTAL DETAILS:**
  - Sourdough loaves in a basket
  - A chalkboard menu
  - A hanging plant, mismatched mugs
  - A small Golden Gate poster
  - The barista (cameo NPC) behind the counter
- **APPROXIMATE SHAPE:** Small rectangular interior, slightly wider than tall.
- **RELATIVE SIZE:** SMALL
- **ENTRANCE(S):** Front door at bottom-center (from SF_01).
- **EXIT(S):**
  - **Front door** (bottom-center): back to SF_01. The player appears under the awning, facing down.
  - **Back patio door** (top-right): a glass door onto a tiny patio. Beyond its little iron gate you can see the top of a long hedge-lined stairway.
- **DIRECT CONNECTIONS:** SF_01, SF_03.
- **PLAYER FLOW:** Enter, go to the counter, sit at the window booth, then go out through the back patio.
- **IMPORTANT VISUAL MOMENT:** Two cups on the window table, with fog outside.
- **IMPORTANT STORY MOMENT:** The first-date memory and the polaroid. The barista is introduced by name.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Chair backs and a plant in the bottom corners
  - Hanging pendant lamps across the top
- **BACKGROUND DETAILS:**
  - Shelves of beans
  - A window view of the foggy street
  - A second customer with a laptop
- **RECOGNIZABILITY:** Fog through the windows, sourdough, and a cozy indie-café texture.
- **TRANSITION NOTES:** The back patio gate opens directly onto the top of SF_03. This is a real spatial adjacency, not a fade.

---

#### SF_03_LYON_STREET_STEPS
- **ROOM NAME:** Lyon Street Steps
- **CITY / REGION:** San Francisco, Pacific Heights to the Presidio edge
- **STORY PURPOSE:** The adventure begins. The couple heads down toward the water, and the world opens up.
- **WHY THIS ROOM EXISTS:** It is a real, specific SF place, not generic. It gives SF its first vista and turns "walk to the coast" into a memorable vertical descent instead of filler street.
- **VISUAL SUMMARY:**
  - Long switchback stone stairs going down through manicured hedges and terraced flowerbeds
  - Grand houses at the top
  - The fog is thinning
- **KEY LANDMARKS:**
  - The sculpted hedge terraces and flowerbeds
  - The mid-landing overlook
  - The Palace of Fine Arts dome and the bay, seen through a gap in the hedges
- **ENVIRONMENTAL DETAILS:**
  - People jogging the steps (one stopping to stretch)
  - A dog walker with three dogs
  - A bench on the landing
  - Eucalyptus trees on one side
- **APPROXIMATE SHAPE:** Vertical corridor with a zigzag stair. It is about 1 screen wide and 1.5 screens tall.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Top, through the café patio gate.
- **EXIT(S):**
  - **Top:** the patio gate, back to SF_02.
  - **Bottom:** a pair of old Presidio stone gate pillars with a eucalyptus path continuing north. This leads to SF_04.
- **DIRECT CONNECTIONS:** SF_02, SF_04.
- **PLAYER FLOW:** Walk down the switchbacks, stop at the left-side landing overlook, then continue down to the stone pillars.
- **IMPORTANT VISUAL MOMENT:** At the landing, the hedges part and the fog begins to lift off the bay. The Palace dome glows below.
- **IMPORTANT STORY MOMENT:** A small "where should we go today?" beat at the overlook.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Clipped hedges framing both sides of the stairs
  - Eucalyptus canopy cutting across the top-left
- **BACKGROUND DETAILS:**
  - The Palace of Fine Arts rotunda
  - Bay water
  - The Marina's rooftops
  - Thinning fog
- **RECOGNIZABILITY:** The famous hedge-lined staircase plus the Palace dome below. Locals recognize it instantly.
- **TRANSITION NOTES:** None. The pillars lead straight into SF_04 as a walk-through.

---

#### SF_04_CRISSY_FIELD
- **ROOM NAME:** Crissy Field
- **CITY / REGION:** San Francisco, Presidio shoreline
- **STORY PURPOSE:** The coastal payoff and the end of the first chapter. The world's first "wow" moment.
- **WHY THIS ROOM EXISTS:** It delivers the "coastal" tone and gives the Golden Gate a real reveal instead of a cliché backdrop. It is also where SF ends.
- **VISUAL SUMMARY:**
  - A horizontal shoreline with a strip of sandy beach and dune grass
  - A meadow path at the bottom
  - Blue bay water across the top
  - The Golden Gate Bridge emerging from burning-off fog at the top-left
- **KEY LANDMARKS:**
  - The Golden Gate Bridge (top-left background)
  - The little Warming Hut building (left)
  - A beach log to sit on
- **ENVIRONMENTAL DETAILS:**
  - A dog chasing gulls
  - A kite
  - Windsurfer sails on the bay
  - Kids building a sandcastle
  - A sand dollar at the waterline (the memento)
- **APPROXIMATE SHAPE:** Horizontal strip, about 1.5 screens wide.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Right edge, on the eucalyptus path, coming from SF_03.
- **EXIT(S):**
  - **Right edge:** back to SF_03.
  - **Bottom-left:** a small gravel parking lot beside the Warming Hut, where a car waits with the trunk open and two suitcases inside. This leads to T1.
- **DIRECT CONNECTIONS:** SF_03, T1.
- **PLAYER FLOW:** Walk west along the beach toward the bridge, sit on the log, find the sand dollar, then go to the car by the Warming Hut.
- **IMPORTANT VISUAL MOMENT:** As the player walks west, the fog peels away from the bridge towers until the whole span is visible. This is the act's money shot.
- **IMPORTANT STORY MOMENT:** "What if we went somewhere?" The idea of the journey is born. The suitcases in the car answer it.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Dune grass and a split-rail fence along the bottom
  - Beach logs
- **BACKGROUND DETAILS:**
  - The bridge
  - The Marin headlands
  - Sailboats
  - A distant container ship
- **RECOGNIZABILITY:** The Golden Gate, with fog, from the beach.
- **TRANSITION NOTES:** Getting into the car triggers T1. The final SF image, through the car window, is the bridge.

---

### ACT 2 — NEW YORK
**Palette:** brick red, slate, yellow taxis, neon and warm windows.
**Light:** late afternoon, then dusk, then night.
**Density rule:** buildings crop the top of every frame, and there are more NPCs here than anywhere else in the game.

---

#### NYC_01_42ND_ST_BRYANT_PARK
- **ROOM NAME:** 42nd Street & Bryant Park
- **CITY / REGION:** New York, Midtown Manhattan
- **STORY PURPOSE:** "The world just got bigger." Energy, speed, and wonder.
- **WHY THIS ROOM EXISTS:** It is the contrast with SF, and the reason the act exists. It is anchored on one specific place (the Library lions and Bryant Park) rather than a checklist of clichés. The creator can swap in their own real NYC corner here.
- **VISUAL SUMMARY:**
  - A wide avenue band along the bottom with taxis
  - A packed sidewalk in the middle
  - Along the top: the New York Public Library's stone steps and the two lions on the left, and Bryant Park's green bistro chairs and plane trees in the center-right
  - Towers crop the top edge
- **KEY LANDMARKS:**
  - The Library lions
  - Bryant Park's green chairs and carousel
  - A subway entrance with green globe lamps (far left)
- **ENVIRONMENTAL DETAILS:**
  - One steam vent
  - A bodega fruit stand
  - A scaffolding shed with green netting at one corner
  - A busker on the library steps
  - Pigeons
  - 6–10 NPC pedestrians moving in lanes (the highest density in the game)
  - A lion keychain at a street vendor (the memento)
- **APPROXIMATE SHAPE:** Wide horizontal avenue, about 2 screens wide.
- **RELATIVE SIZE:** LARGE
- **ENTRANCE(S):** Bottom-right curb. The player is already standing on the sidewalk as the T1 taxi pulls away.
- **EXIT(S):**
  - **Subway entrance** (far left): stairs going down under the green globes. This leads to T2.
  - **Right edge:** a crosswalk with traffic. This is a soft boundary, not an exit.
- **DIRECT CONNECTIONS:** T1, T2.
- **PLAYER FLOW:** Walk left along the sidewalk, cross into Bryant Park's chairs, pass the library lions, and go down the subway stairs.
- **IMPORTANT VISUAL MOMENT:** The first look up. The towers are so tall they leave the frame.
- **IMPORTANT STORY MOMENT:** A small moment on the green chairs, maybe sitting by the carousel.
- **FOREGROUND / FRAMING ELEMENTS:**
  - A traffic light and fire hydrant along the bottom
  - Plane-tree canopy
  - The scaffolding corner
- **BACKGROUND DETAILS:**
  - Glass and brick towers
  - Billboards
  - The Empire State Building's spire glimpsed between buildings
  - Moving taxis
- **RECOGNIZABILITY:** The Library lions, yellow taxis, subway globes, and Bryant Park chairs.
- **TRANSITION NOTES:** The subway stairs lead to the T2 micro-cut.

---

#### NYC_02_BROWNSTONE_BLOCK
- **ROOM NAME:** Brownstone Block
- **CITY / REGION:** New York, Upper West Side
- **STORY PURPOSE:** The cozy counterweight, and the place where we stayed (the creator should specify whose place).
- **WHY THIS ROOM EXISTS:** NYC needs a quiet, personal beat between the noise and the rooftop. It is also the physical route to the roof.
- **VISUAL SUMMARY:** A tree-lined residential street running up the screen, with brownstone stoops on both sides at dusk. Warm windows are coming on.
- **KEY LANDMARKS:**
  - Our building: a red-brick walk-up with a green door, among the brownstones
  - A corner bodega with a cat sitting on the stoop next door
- **ENVIRONMENTAL DETAILS:**
  - Black iron railings
  - Ginkgo trees
  - Potted mums
  - Recycling bins
  - A neighbor on a stoop with the bodega cat (cameo NPC)
  - Delivery bikes
- **APPROXIMATE SHAPE:** Vertical street, about 1 screen wide and 1.5 screens tall.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Bottom-left. The player climbs up out of a subway stair entrance.
- **EXIT(S):**
  - **Our building's stoop door** (middle-right). This leads to NYC_03 through a short stairwell fade.
  - **Top end:** Central Park's low stone wall and treetops. This is a soft boundary, not an exit.
  - **Subway stairs** (bottom-left): these lead back through T2 in reverse to NYC_01.
- **DIRECT CONNECTIONS:** T2, NYC_03.
- **PLAYER FLOW:** Climb out of the subway, walk up the block, chat with the neighbor and cat, then go up our stoop.
- **IMPORTANT VISUAL MOMENT:** The dusk street with every window turning golden, one by one, with the treetops of the park at the top.
- **IMPORTANT STORY MOMENT:** "Home for the night." The neighbor is introduced by name.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Tree canopies over the top corners
  - Stoop railings and a parked car along the bottom
- **BACKGROUND DETAILS:**
  - Rear-facing fire escapes visible on the tenement corner
  - Water towers on the roofs
  - A church spire
- **RECOGNIZABILITY:** Brownstone stoops, iron railings, a bodega cat, and the edge of Central Park.
- **TRANSITION NOTES:** The stoop door uses a door-fade (a quick climb up the stairwell), not a transition scene. The player appears in NYC_03 at the roof bulkhead door.

---

#### NYC_03_ROOFTOP_NIGHT
- **ROOM NAME:** The Rooftop
- **CITY / REGION:** New York, Upper West Side rooftop
- **STORY PURPOSE:** NYC's romantic peak: "we made it here together."
- **WHY THIS ROOM EXISTS:** It delivers the skyline and city-lights beat in one intimate frame, and it is the launch point for the long flight.
- **VISUAL SUMMARY:** A tar-paper rooftop with a low parapet, a wooden water tower, and a single bare bulb over the bulkhead door. The midtown skyline glitters in the distance.
- **KEY LANDMARKS:**
  - The water tower
  - Two folding chairs and a blanket at the parapet
- **ENVIRONMENTAL DETAILS:**
  - Tomato and herb planters in buckets
  - An AC unit
  - A neighbor's roof garden across the gap
  - The moon
- **APPROXIMATE SHAPE:** Roughly square rooftop.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Bulkhead door at bottom-center.
- **EXIT(S):**
  - **Bulkhead door:** back to NYC_02.
  - **Story exit:** sitting at the parapet chairs triggers T3.
- **DIRECT CONNECTIONS:** NYC_02, T3.
- **PLAYER FLOW:** Step out of the bulkhead, walk past the water tower, and sit on the chairs at the parapet facing the skyline.
- **IMPORTANT VISUAL MOMENT:** The skyline spread across the top. The Empire State and Chrysler spires are small, because they are far away from the UWS.
- **IMPORTANT STORY MOMENT:** The quiet NYC night moment. A plane's blinking lights cross the sky, and the next chapter calls.
- **FOREGROUND / FRAMING ELEMENTS:**
  - The parapet and vent pipes along the bottom
  - Water-tower legs
- **BACKGROUND DETAILS:**
  - Thousands of lit windows
  - Neighboring water towers
  - A helicopter light
  - Bridge lights
- **RECOGNIZABILITY:** The water tower against the Manhattan skyline at night.
- **TRANSITION NOTES:** The plane crossing the sky turns into T3.
- **Motif rule:** no string lights here (Italy owns them). One bare bulb only.

---

### ACT 3 — JEDDAH
**Palette:** black-blue sea, amber sodium light, coral stone, deep green wood, gold.
**Light:** warm night throughout.

---

#### JED_01_AIRPORT_ARRIVALS
- **ROOM NAME:** Arrivals & Curb
- **CITY / REGION:** Jeddah, King Abdulaziz International Airport
- **STORY PURPOSE:** The first breath of Saudi night air. The arrival is the moment the warmth hits.
- **WHY THIS ROOM EXISTS:**
  - It was required.
  - It is the only airport room in the whole game.
  - It gives the physical "we landed, we stepped out" moment.
- **VISUAL SUMMARY:**
  - The left third is the arrivals hall: a polished floor, a baggage carousel, a bilingual "Welcome / أهلاً وسهلاً" sign, and glass sliding doors.
  - The right two thirds is a covered curb under a white, tent-like canopy (echoing KAIA's famous tent roofs), with palms in stone planters and amber light.
- **KEY LANDMARKS:**
  - The tent-canopy roofline
  - The sliding doors
  - The waiting car at the far right, with its door open
- **ENVIRONMENTAL DETAILS:**
  - Luggage carts
  - Families greeting arrivals with flowers
  - Arabic/English wayfinding
  - Geometric star tiles on the columns
  - Small NPCs in thobes and abayas
- **APPROXIMATE SHAPE:** Horizontal strip, about 1.5 screens wide.
- **RELATIVE SIZE:** SMALL-MEDIUM
- **ENTRANCE(S):** Left, inside the hall beside the carousel (the end of T3).
- **EXIT(S):** **Car door** (far right). A door-fade (the car door closes, then opens) leads to JED_02.
- **DIRECT CONNECTIONS:** T3, JED_02.
- **PLAYER FLOW:** Pick up the bags at the carousel, walk through the sliding doors, feel the warm air outside (heat-shimmer pixels), and walk along the curb to the car.
- **IMPORTANT VISUAL MOMENT:** The sliding doors open, and the cool, white interior palette flips to amber night.
- **IMPORTANT STORY MOMENT:** None. It is a breath, a pause.
- **FOREGROUND / FRAMING ELEMENTS:**
  - The canopy edge across the top
  - Palms
  - Bollards
- **BACKGROUND DETAILS:**
  - Runway lights
  - Aircraft tail fins
  - A glow in the sky from the city
- **RECOGNIZABILITY:** The tent canopy, bilingual signage, and palms under sodium light.
- **TRANSITION NOTES:** The car ride is a door-fade, not a transition scene. The former night-drive scene was cut because it repeated JED_02's fountain.

---

#### JED_02_CORNICHE
- **ROOM NAME:** The Corniche
- **CITY / REGION:** Jeddah, Red Sea waterfront
- **STORY PURPOSE:** Jeddah as a place: the romantic walk by the sea before dinner.
- **WHY THIS ROOM EXISTS:** It is the required "city between the airport and the restaurant." Without it, Act 3 is just an airport and a restaurant.
- **VISUAL SUMMARY:** A wide waterfront promenade at night. Black-blue sea with white foam fills the top. Amber lamps reflect on the water, and palms stand in rows on geometric-tiled paving.
- **KEY LANDMARKS (one sightline only):**
  - King Fahd's Fountain: a glowing white jet on the sea horizon at the top-right
  - A lantern-lit fishing pier
  - A large abstract Corniche sculpture
- **ENVIRONMENTAL DETAILS:** Three stops along the walk:
  1. A karak tea and ice-cream cart
  2. The pier, with fishermen
  3. A bench facing the fountain
  - Families picnicking on carpets on the grass strip
  - Kids on scooters
- **APPROXIMATE SHAPE:** Wide horizontal promenade, about 1.5 screens wide. It is not L-shaped.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Left edge, at the car drop-off. The car pulls away.
- **EXIT(S):**
  - **Right end:** a tiled inland arch hung with fanous lanterns, with the glow of a street beyond it. This leads to JED_03.
  - **Left edge:** a soft boundary (traffic), not an exit.
- **DIRECT CONNECTIONS:** JED_01, JED_03.
- **PLAYER FLOW:** Walk right along the railing: the cart, then the pier, then the fountain bench, then the lantern arch.
- **IMPORTANT VISUAL MOMENT:** Sitting on the bench, with the fountain jet rising and the lamps rippling on the sea.
- **IMPORTANT STORY MOMENT:** A quiet, close moment before dinner.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Palm trunks and fronds crossing the top corners
  - The stone sea railing
  - Round shrubs
- **BACKGROUND DETAILS:**
  - The sea
  - Boat lights
  - The fountain jet
  - A distant tower skyline at the far left
- **RECOGNIZABILITY:** The King Fahd Fountain over the dark Red Sea, palm promenade, and families on carpets.
- **TRANSITION NOTES:** None. The arch walks straight into JED_03.

---

#### JED_03_ENTRECOTE_STREET
- **ROOM NAME:** Entrecôte Street
- **CITY / REGION:** Jeddah, inland street one block from the waterfront
- **STORY PURPOSE:** Anticipation. You see the restaurant before you enter it.
- **WHY THIS ROOM EXISTS:** It was required. It also holds the act's Saudi architectural identity and street life, so the restaurant sits inside a living city.
- **VISUAL SUMMARY:**
  - A lively evening street
  - L'Entrecôte's cream-stone facade at top-center, with a dark awning, gold script sign, brass lamps, and warm light spilling onto the paving
  - On the left: heritage-style coral-stone buildings with carved green wooden rawasheen balconies and mashrabiya screens
  - On the right: a shisha café with floor cushions
- **KEY LANDMARKS:**
  - The Entrecôte facade and its doorman
  - The rawasheen facades
- **ENVIRONMENTAL DETAILS:**
  - Valet cars pulling in
  - A kid with balloons
  - Families out late
  - Fanous lanterns
  - Olive trees in glazed pots
  - A star-pattern paving inlay
- **APPROXIMATE SHAPE:** Horizontal street plaza, about 1 screen wide.
- **RELATIVE SIZE:** SMALL-MEDIUM
- **ENTRANCE(S):** Left edge, under the matching lantern arch, facing right.
- **EXIT(S):**
  - **Front door** (top-center). This leads to JED_04.
  - **Left arch:** back to JED_02 (backtracking allowed).
- **DIRECT CONNECTIONS:** JED_02, JED_04.
- **PLAYER FLOW:** Come through the arch, cross the bustling street, and reach the lit doorway, where the doorman opens the door.
- **IMPORTANT VISUAL MOMENT:** The warm rectangle of light from the open door across the paving.
- **IMPORTANT STORY MOMENT:** None. This room is anticipation.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Lanterns hanging along the top
  - Potted olive trees
  - Valet cars in the corners
- **BACKGROUND DETAILS:**
  - Rooftops and a minaret silhouette
  - A strip of sea-glow between buildings
- **RECOGNIZABILITY:** Rawasheen balconies, bilingual signage, and the Entrecôte awning.
- **OPEN QUESTION FOR THE CREATOR:** Confirm the real Jeddah branch you went to and its street, and share photos if possible. The street character and facade should match it.

---

#### JED_04_ENTRECOTE_INTERIOR
- **ROOM NAME:** Inside Entrecôte
- **CITY / REGION:** Jeddah
- **STORY PURPOSE:** The payoff of Act 3: a specific dinner memory (an anniversary, the "there's no menu, just steak-frites" joke, or whatever it really was).
- **WHY THIS ROOM EXISTS:** It was required. It is the emotional destination of the chapter.
- **VISUAL SUMMARY:** An elegant French bistro: wood paneling, mirrors, brass sconces, white tablecloths, and servers in black with white aprons. A corner table for two is set with a candle.
- **KEY LANDMARKS:**
  - Our table
  - The service bar
  - A big bistro mirror
- **ENVIRONMENTAL DETAILS:**
  - Steak-frites plates in their famous sauce, plus the salad with walnuts
  - A matchbook on our table (the memento)
  - The waiter (cameo NPC, introduced by name)
  - A geometric ceiling lamp as a subtle local touch
- **APPROXIMATE SHAPE:** Rectangular interior, slightly deeper than wide.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Front door at bottom-center.
- **EXIT(S):** **Front door** (after dinner). Stepping out into the night street triggers T4.
- **DIRECT CONNECTIONS:** JED_03, T4.
- **PLAYER FLOW:** The host stand, then a route between tables, then our corner table. After dinner, go back to the front door.
- **IMPORTANT VISUAL MOMENT:** The candle between two plates, with the mirror reflecting the couple.
- **IMPORTANT STORY MOMENT:** The dinner. The creator should define what made it special.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Chair backs
  - A coat rack
  - A pillar with a plant
- **BACKGROUND DETAILS:**
  - Wine and glass shelving
  - Other diners
  - A server crossing the room
- **RECOGNIZABILITY:** The Relais de l'Entrecôte bistro look and its signature dish.
- **OPEN QUESTION FOR THE CREATOR:** Interior details must be matched to your photos. The sea-view window from the draft was removed as unverified.

---

### ACT 4 — RIYADH
**Palette:** pale stone, glass blue, desert gold, cool white light.
**Light:** golden hour, then blue hour. The architecture lights up; there are no string lights.

---

#### RUH_01_KAFD_WADI
- **ROOM NAME:** KAFD Wadi Approach
- **CITY / REGION:** Riyadh, King Abdullah Financial District
- **STORY PURPOSE:** The impressive approach. The world feels like the future.
- **WHY THIS ROOM EXISTS:**
  - It is the showpiece and the main recognizability anchor for KAFD.
  - It absorbs the arrival: the metro station is drawn as this room's bottom edge, which saves a separate station room.
- **VISUAL SUMMARY:**
  - A wadi-inspired landscaped valley climbing up the screen in stone terraces of native planting and water channels
  - Faceted crystalline towers rise on both sides
  - The PIF Tower's sharp crown sits at top-center
  - An elevated skywalk crosses overhead
- **KEY LANDMARKS:**
  - The white lattice canopy of the KAFD Metro Station (bottom edge)
  - The PIF Tower
  - The skywalk
  - The monorail loop, with a small pod gliding across once
- **ENVIRONMENTAL DETAILS (mid-climb beats so it never reads as a hallway):**
  - A family dipping their feet in a water channel
  - Young professionals with coffee cups
  - Shade under acacias, with a bench
  - Water steps catching gold light
- **APPROXIMATE SHAPE:** Vertical climb with a gently winding path. It is about 1 screen wide and 2 screens tall, with vertical scroll.
- **RELATIVE SIZE:** LARGE
- **ENTRANCE(S):** Bottom-center. The player steps out from under the metro station's lattice canopy, at the top of an escalator (the end of T4).
- **EXIT(S):**
  - **Top-center:** wide stone steps between two crystalline towers, with the plaza's glow visible above. This leads to RUH_02.
  - **Bottom:** the station canopy. This is a soft boundary, not a way back.
- **DIRECT CONNECTIONS:** T4, RUH_02.
- **PLAYER FLOW:** Wind up through the terraces, pass the family at the water and the acacia bench, walk under the skywalk, and reach the top steps.
- **IMPORTANT VISUAL MOMENT:** Passing under the skywalk as the monorail pod glides overhead and the PIF crown catches the last gold light.
- **IMPORTANT STORY MOMENT:** None. This room is awe.
- **FOREGROUND / FRAMING ELEMENTS:**
  - The skywalk's underside across the top band
  - Terrace planters
  - Tall grasses
- **BACKGROUND DETAILS:**
  - Layered towers with diamond-cut glass
  - Clean skies
  - Distant city haze
- **RECOGNIZABILITY:** The PIF crown, faceted towers, the elevated skywalk and monorail, and the lattice station canopy.
- **TRANSITION NOTES:** T4 ends on the escalator rising into the canopy, and the room begins there.

---

#### RUH_02_KAFD_PLAZA
- **ROOM NAME:** KAFD Plaza & Terrace
- **CITY / REGION:** Riyadh, KAFD
- **STORY PURPOSE:** **The promise.** This is the concrete, future-facing story beat that motivates Italy.
- **WHY THIS ROOM EXISTS:** It is the act's one place to stop and feel something, and it gives the futuristic district a human scale.
- **VISUAL SUMMARY:**
  - A square, polished stone plaza with geometric paving inlay and a long reflecting pool
  - The KAFD Grand Mosque's faceted form is lit warmly to one side
  - The tower cluster rises behind
  - A raised terrace with a bench sits at the top
- **KEY LANDMARKS:**
  - The Grand Mosque
  - The reflecting pool
  - The terrace bench
  - A Saudi coffee kiosk (dallah pots, dates)
- **ENVIRONMENTAL DETAILS:**
  - The kiosk host (cameo NPC) pouring qahwa
  - A finjan cup (the memento)
  - Couples and families strolling
  - Slender light poles
  - Modern planters
- **APPROXIMATE SHAPE:** Square plaza.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Bottom-center, at the top of the wadi steps.
- **EXIT(S):**
  - **Story exit:** the terrace bench. The camera rises into the sky and the tower crowns become stars, which leads to T5.
  - **Bottom steps:** back to RUH_01.
- **DIRECT CONNECTIONS:** RUH_01, T5.
- **PLAYER FLOW:** Go to the kiosk for qahwa and dates, walk along the reflecting pool, climb to the terrace, and sit.
- **IMPORTANT VISUAL MOMENT:** At blue hour the tower crowns light up, and their reflections stretch down the pool toward the couple.
- **IMPORTANT STORY MOMENT:** The promise: a ring, a question, or a decision about the future. The creator decides the exact moment. It must clearly motivate the trip to Italy without spoiling the ceremony.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Planters
  - Light poles
  - Kiosk umbrellas
- **BACKGROUND DETAILS:**
  - The skyline cluster
  - The skywalk crossing in an upper corner
  - The first stars
- **RECOGNIZABILITY:** The mosque's geometry with the KAFD towers behind it.
- **TRANSITION NOTES:** The camera lifts, and T5 begins.

---

### ACT 5 — ITALY / WEDDING
**Region:** generic Tuscan-style hill country. It can be reskinned as a lake or coastal setting without changing the layout.

**Light progression:**
1. Golden afternoon
2. Sunset
3. Inside at sunset
4. String-lit dusk
5. Night

**Reveal ladder:**
1. One ribbon
2. A ribbon on every post
3. Benvenuti board and guests
4. Alone in the dressing room
5. The aisle

All Italy rooms share one tileset (stone, stucco, terracotta, cypress) for producibility.

---

#### ITA_01_HILL_TOWN_PIAZZA
- **ROOM NAME:** The Piazza
- **CITY / REGION:** Italy, a Tuscan hill town
- **STORY PURPOSE:** Italy is beautiful and dreamy, and there is the first tiny hint.
- **WHY THIS ROOM EXISTS:** It is the postcard "charming Italy" room and the only lived-in Italian place before the estate.
- **VISUAL SUMMARY:** A small cobbled piazza in ochre and peach stucco around an old stone fountain. A bell-tower church stands at the top, beside a café with a striped awning.
- **KEY LANDMARKS:**
  - The bell tower
  - The fountain
  - The café tables
  - The florist's stall
- **ENVIRONMENTAL DETAILS:**
  - A gelato cart
  - Shuttered windows with laundry lines
  - Potted lemon trees
  - A Vespa
  - The florist (cameo NPC) unloading white flowers
  - **One white ribbon** tied to a café chair
- **APPROXIMATE SHAPE:** Plus-shaped piazza. The side alleys are decorative dead ends: a closed door and a flower-box nook.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** The bottom stone town-gate arch (from the train halt in T5).
- **EXIT(S):** **East gate arch** (right side), with a white ribbon tied on the gatepost and a little "Villa ➝" sign. This leads to ITA_02.
- **DIRECT CONNECTIONS:** T5, ITA_02.
- **PLAYER FLOW:** Through the arch, around the fountain, past the café and florist, and out the east arch.
- **IMPORTANT VISUAL MOMENT:** Coming through the arch into full golden light with the bell tower above.
- **IMPORTANT STORY MOMENT:** The florist mentions "a big celebration up the hill tonight."
- **FOREGROUND / FRAMING ELEMENTS:**
  - The entry arch
  - Flower boxes
  - Awning edges
- **BACKGROUND DETAILS:**
  - Terracotta roofs stepping up the hill
  - The valley glimpsed between buildings
  - Swallows
- **RECOGNIZABILITY:** Piazza, bell tower, café umbrellas, and laundry lines.
- **TRANSITION NOTES:** This room is the end of T5.

---

#### ITA_02_CYPRESS_ROAD
- **ROOM NAME:** Cypress Road
- **CITY / REGION:** Italy, countryside
- **STORY PURPOSE:** The realization. The hints are now everywhere.
- **WHY THIS ROOM EXISTS:** It is the emotional ramp, a quiet open space between the busy town and the busy estate. It has an event, so it isn't just a corridor.
- **VISUAL SUMMARY:** A white gravel road curving in an S through vineyards and olive groves, lined with cypress trees. The sky is turning orange.
- **KEY LANDMARKS:**
  - A stone bridge over a stream
  - A roadside shrine
  - The florist's little truck, stopped at the bridge with roses spilling out
  - The villa's tower on the far hill
- **ENVIRONMENTAL DETAILS:**
  - **A white ribbon on every fence post**
  - Vineyard rows
  - Poppies
  - A wooden "Villa" signpost
- **APPROXIMATE SHAPE:** S-curve running from the bottom-left to the top-right.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** Bottom-left, coming from the piazza's east arch.
- **EXIT(S):**
  - **Top-right:** a tall wrought-iron estate gate, ribboned, with the villa visible behind. This leads to ITA_03.
  - **Bottom-left:** back to ITA_01.
- **DIRECT CONNECTIONS:** ITA_01, ITA_03.
- **PLAYER FLOW:** Walk up the S-curve, cross the bridge past the stalled flower truck, then reach the shrine and the gate.
- **IMPORTANT VISUAL MOMENT:** Cresting the last curve to see the villa's first string lights on the hill against the sunset.
- **IMPORTANT STORY MOMENT:** Helping the florist gather spilled roses. The partner glances at the ribbons, and the realization lands.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Cypress trunks
  - Vine rows
  - Stone walls
- **BACKGROUND DETAILS:**
  - Rolling hills
  - The distant hill town you just left
  - Birds
- **RECOGNIZABILITY:** A cypress-lined white road through vineyards.
- **TRANSITION NOTES:** None. The gate is a walk-through.

---

#### ITA_03_VILLA_COURTYARD
- **ROOM NAME:** Villa Courtyard
- **CITY / REGION:** Italy, the wedding estate
- **STORY PURPOSE:** Certainty: this is a wedding. Then the separation, as the partner is taken away.
- **WHY THIS ROOM EXISTS:** It is the estate reveal and the setup for the climax's most powerful beat.
- **VISUAL SUMMARY:**
  - A gravel courtyard in front of a grand ochre villa with a loggia and big wooden doors
  - A flower-wrapped fountain sits at the center
  - A white-rose welcome arch stands at the entry
- **KEY LANDMARKS:**
  - The villa facade and front door
  - The "Benvenuti" chalkboard with a seating chart
  - A ribboned vintage car
- **ENVIRONMENTAL DETAILS:**
  - Early guests arriving in their best clothes
  - Helpers carrying chairs
  - Terracotta urns
  - Lemon trees
  - Hedges
- **APPROXIMATE SHAPE:** Rectangular courtyard. The villa runs along the top and the gate arch is at the bottom.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** The bottom gate arch, from ITA_02.
- **EXIT(S):**
  - **Villa front door** (top-center). This leads to ITA_04.
  - **Side pergola to the garden:** closed with a flower garland ("not yet").
  - **Bottom gate:** back to ITA_02.
- **DIRECT CONNECTIONS:** ITA_02, ITA_04.
- **PLAYER FLOW:** Under the rose arch, past the fountain and guests, to the Benvenuti board (our names) and the front door.
- **IMPORTANT VISUAL MOMENT:** Reading the Benvenuti board. The names are ours.
- **IMPORTANT STORY MOMENT:** **Separation.** Friends laughingly whisk the partner away through the loggia's side door. For the first time in the game, the player walks alone.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Cypress and hedges at the sides
  - The rose arch
  - Urns
- **BACKGROUND DETAILS:**
  - The villa's roofline and bell gable
  - Vineyard beyond the wall
- **RECOGNIZABILITY:** An Italian villa at sunset dressed for a wedding.
- **TRANSITION NOTES:** The front door is a plain door. The player appears inside ITA_04.

---

#### ITA_04_GETTING_READY
- **ROOM NAME:** The Getting-Ready Room
- **CITY / REGION:** Italy, inside the villa
- **STORY PURPOSE:** A quiet breath before the climax. The whole journey sits on one dresser.
- **WHY THIS ROOM EXISTS:**
  - The critic's strongest addition: a solitary, interior pause makes the aisle walk land.
  - It pays off every memento.
  - It holds the "lights coming on" moment, seen through a window.
- **VISUAL SUMMARY:** A small, sunlit villa bedroom with frescoed plaster, a tall mirror, and a dresser. French doors open onto the back loggia.
- **KEY LANDMARKS:**
  - The mirror
  - The dresser with every memento laid out
  - The window overlooking the garden
- **ENVIRONMENTAL DETAILS:**
  - The garment (dress or suit) on a stand
  - A bouquet in a vase
  - A note from the partner
  - Late sun through the shutters
- **APPROXIMATE SHAPE:** Small rectangular interior.
- **RELATIVE SIZE:** SMALL
- **ENTRANCE(S):** Bottom door (from the villa front door).
- **EXIT(S):** **Back French doors** (top-right), which open onto the loggia steps above the garden. This leads to ITA_05.
- **DIRECT CONNECTIONS:** ITA_03, ITA_05.
- **PLAYER FLOW:** Enter, walk to the dresser and look at each memento, then the mirror, then the window, then the French doors.
- **IMPORTANT VISUAL MOMENT:** Through the window, the garden's string lights switch on, row by row. This is the game's only "lights on" moment.
- **IMPORTANT STORY MOMENT:** Remembering every chapter. The partner's note.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Curtain edges
  - A chair with a veil or jacket draped over it
- **BACKGROUND DETAILS:** Frescoes, shutters, and the garden view.
- **RECOGNIZABILITY:** An old Italian villa bedroom.
- **TRANSITION NOTES:** The French doors lead directly onto the garden, which is real adjacency.

---

#### ITA_05_GARDEN_CEREMONY
- **ROOM NAME:** Garden Ceremony
- **CITY / REGION:** Italy, the villa gardens
- **STORY PURPOSE:** The climax of the whole game.
- **WHY THIS ROOM EXISTS:** It is the point of the game. It is the largest, densest, and most beautiful room.
- **VISUAL SUMMARY:**
  - A walled garden at string-lit dusk
  - Loggia steps and a vine pergola at the bottom
  - A petal-strewn aisle running straight up the middle between ribboned chairs full of guests
  - A canopy of string lights and lanterns overhead
  - A flower-covered ceremony arch at the top, framed by a tall cypress and hedge wall that only hints at the valley beyond
- **KEY LANDMARKS:**
  - The aisle
  - The arch, with **the partner waiting there**
  - The string-light canopy
  - A violinist
- **ENVIRONMENTAL DETAILS:**
  - Roses and wisteria
  - Candles in jars along the aisle
  - Family and friends turning to look
  - Petals drifting
  - A fountain
  - Olive trees
- **APPROXIMATE SHAPE:** Large vertical garden, about 1.5 screens wide and 2 screens tall.
- **RELATIVE SIZE:** LARGE (the largest in the game)
- **ENTRANCE(S):** Bottom, down the loggia steps from ITA_04.
- **EXIT(S):** **Through the ceremony arch** (top), after the vows. This leads to ITA_06.
- **DIRECT CONNECTIONS:** ITA_04, ITA_06.
- **PLAYER FLOW:** Down the loggia steps, under the pergola, then a slow walk straight up the aisle to the arch.
- **IMPORTANT VISUAL MOMENT:** The first sight, from the top of the steps, of the partner standing under the arch at the far end of the lit aisle.
- **IMPORTANT STORY MOMENT:** **The vows**, played as an in-room scene. The vows name each city.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Pergola vines across the bottom
  - Cypress columns on both sides
  - Hanging lanterns
- **BACKGROUND DETAILS:**
  - The hedge wall behind the arch, with only a sliver of dusk valley showing
  - The villa glowing behind
  - The first stars
- **RECOGNIZABILITY:** An Italian garden wedding: aisle, arch, and cypress under string lights.
- **TRANSITION NOTES:** After the vows, the arch's hedge opening leads onto the terrace path. That is real adjacency, not a fade.

---

#### ITA_06_RECEPTION_TERRACE
- **ROOM NAME:** Reception Terrace
- **CITY / REGION:** Italy, the villa terrace
- **STORY PURPOSE:** Resolution: "everyone who was part of our story is here."
- **WHY THIS ROOM EXISTS:**
  - It is the exhale after the climax.
  - It pays off the cameo NPCs and mementos.
  - It owns the best vista in the game.
- **VISUAL SUMMARY:**
  - A stone terrace on the edge of the hill at night
  - Long banquet tables under string lights
  - A small dance floor
  - A balustrade opening onto the **full night valley** for the first time: village lights, stars, cypress silhouettes
- **KEY LANDMARKS:**
  - The balustrade view
  - The dance floor
  - The cake table
  - The cameo table with the barista, neighbor and cat, waiter, kiosk host, and florist
- **ENVIRONMENTAL DETAILS:**
  - The mementos used as table centerpieces
  - Lanterns
  - The band
  - Kids running between tables
  - Toasting glasses
- **APPROXIMATE SHAPE:** Wide horizontal terrace, about 1.5 screens wide.
- **RELATIVE SIZE:** MEDIUM
- **ENTRANCE(S):** The arch path (left or top-left), coming from ITA_05.
- **EXIT(S):** **Story exit:** the first dance in the center of the floor triggers T6. There is no other exit, by design. This is the end of the world.
- **DIRECT CONNECTIONS:** ITA_05, T6.
- **PLAYER FLOW:** Along the tables, greeting each cameo, to the balustrade view, then the dance floor.
- **IMPORTANT VISUAL MOMENT:** Arriving at the balustrade: the valley finally fully open under the stars.
- **IMPORTANT STORY MOMENT:** Reunion with everyone from the journey, then the first dance.
- **FOREGROUND / FRAMING ELEMENTS:**
  - Table edges and chairs
  - Lantern poles
  - Potted lemon trees
- **BACKGROUND DETAILS:**
  - Valley lights
  - The silhouette of the hill town (ITA_01) with its bell tower
  - Stars
- **RECOGNIZABILITY:** An Italian hillside reception at night.
- **TRANSITION NOTES:** The first dance leads to T6, the ending.

---

## DELIVERABLE D — Transition Scenes

All transitions are non-playable and skippable.

**"Postcard" grammar:**
1. Vehicle window
2. Pixel map arc
3. Postcard with a chapter title stamped

There are three full postcards (T1, T3, T5) and one short stamp (T4).

**Not counted as transitions:** door-fades. These are a car door, the NYC stairwell, and building doors. They are under 1 second, involve no travel montage, and keep the spatial logic intact.

---

#### T1 — POSTCARD: SAN FRANCISCO → NEW YORK
- **FROM:** SF_04 (the car at the Warming Hut lot)
- **TO:** NYC_01 (the bottom-right curb)
- **WHAT WE SEE:**
  1. The Golden Gate through the car's side window
  2. A plane window, with the bay and its fog falling away
  3. A pixel map arc across the US
  4. A yellow taxi crossing the Queensboro Bridge as Manhattan's towers rise
  5. The postcard: "Chapter II — New York"
- **EMOTIONAL PURPOSE:** The leap. Something small becomes something big.
- **WHY IT IS NOT A ROOM:** A plane cabin and an airport would add nothing that SF_04 and NYC_01 don't already deliver.

#### T2 — MICRO-CUT: SUBWAY UPTOWN
- **FROM:** NYC_01 (the subway entrance)
- **TO:** NYC_02 (climbing out of the subway at bottom-left)
- **WHAT WE SEE:** About 3 seconds: a swaying subway car with hanging straps, flickering lights, and a station sign flashing past.
- **EMOTIONAL PURPOSE:** NYC speed and texture. It also justifies moving from Midtown to the Upper West Side.
- **WHY IT IS NOT A ROOM:** A playable platform would just be a travel room.

#### T3 — POSTCARD: NEW YORK → JEDDAH
- **FROM:** NYC_03 (the rooftop chairs, as a plane's lights cross the sky)
- **TO:** JED_01 (inside the arrivals hall, by the carousel)
- **WHAT WE SEE:**
  1. The camera follows the plane's lights into the night
  2. A plane window over a moonlit Atlantic
  3. A map arc
  4. The descent toward a coastline of amber lights on the dark Red Sea
  5. The postcard: "Chapter III — Jeddah"
- **EMOTIONAL PURPOSE:** The world becomes far and warm. It is the longest leap.
- **WHY IT IS NOT A ROOM:** The flight has no story content of its own.

#### T4 — BOARDING-PASS STAMP: JEDDAH → RIYADH
- **FROM:** JED_04 (the front door after dinner)
- **TO:** RUH_01 (rising up the escalator under the metro canopy)
- **WHAT WE SEE:** About 4 seconds:
  1. A boarding pass, stamped "JED → RUH"
  2. A quick window shot of the desert at golden hour, with the KAFD towers rising ahead
  3. An escalator rising toward a white lattice canopy
- **EMOTIONAL PURPOSE:** A short domestic hop. It is deliberately brisk, to vary the rhythm between the two long postcards.
- **WHY IT IS NOT A ROOM:** It is a second airport, which the game avoids. The station canopy is folded into RUH_01.

#### T5 — POSTCARD: RIYADH → ITALY
- **FROM:** RUH_02 (the camera rising from the terrace bench)
- **TO:** ITA_01 (the bottom town-gate arch)
- **WHAT WE SEE:**
  1. The tower crowns dissolve into stars
  2. A plane window as the clouds part over green hills and cypress ridges at golden hour
  3. A small vintage train crossing poppy fields with a hill town on the horizon
  4. The train stops at a tiny halt
  5. The couple walks up toward the town gate
  6. The postcard: "Chapter V — Italy"
- **EMOTIONAL PURPOSE:** Dreaminess. The promise from Riyadh is carried into the final chapter.
- **WHY IT IS NOT A ROOM:** The piazza is the arrival. A station room would be a third arrival hub (it was cut).

#### T6 — ENDING
- **FROM:** ITA_06 (the first dance)
- **TO:** The end
- **WHAT WE SEE:**
  1. Lanterns rise from the terrace
  2. The camera pulls up over the whole lit estate and valley
  3. The journey map reappears, and its six stops light up one by one: SF, NYC, Jeddah, Riyadh, Italy, and a heart
  4. A title card with the creator's message
- **EMOTIONAL PURPOSE:** The whole journey, remembered at once.
- **WHY IT IS NOT A ROOM:** Nothing is left to walk to.

**Transition tally:**
- 6 transitions in total (1 of them a micro-cut).
- 4 flights, which are all geographically unavoidable and each presented differently.
- 1 airport room in the whole game.

---

## DELIVERABLE E — Full Walkthrough (player's eyes)

**San Francisco**
- I wake into the game standing on our yellow stoop with my partner in morning fog. The street climbs to the right, and a gull watches from a lamp post. My partner says "coffee first?" and I walk uphill along the sidewalk to the corner, where a green awning hangs over a glass door.
- I enter the café. It's warm and the windows are steamed. The barista greets us by name. We sit in the window booth, and there's our polaroid on the corkboard.
- I go out the back patio door. Past a small iron gate, the Lyon Street Steps drop away in hedged switchbacks. I head down them. At the landing the hedges open, the fog is lifting off the bay, and the Palace of Fine Arts dome glows below.
- At the bottom I pass between two old stone gate pillars onto a eucalyptus path. I come out at the east end of Crissy Field. Wind, dune grass, a dog chasing gulls.
- I walk west along the sand. With every step the fog peels off the Golden Gate Bridge until it is fully revealed. I pick up a sand dollar.
- By the little Warming Hut, a car waits with its trunk open and two suitcases inside. I get in. Through the window, the bridge…

**T1:**
- A plane climbs out of the fog, and a map arc crosses the country.
- A taxi crosses the Queensboro Bridge toward Manhattan.
- *Chapter II — New York.*

**New York**
- I'm on a 42nd Street sidewalk as the taxi pulls away. Towers leave the top of the screen, and crowds stream past. I walk left past a steam vent and a bodega, into Bryant Park's green chairs (we sit for a moment by the carousel), then past the Library's stone lions, where I buy a lion keychain from a vendor.
- I take the subway stairs under the green globes. (T2: a swaying car, a flashing sign.)
- I climb out at the corner of an Upper West Side block at dusk. Brownstone stoops run up the street, and windows turn gold. A neighbor on a stoop introduces their bodega cat.
- Halfway up is our red-brick walk-up. I climb the stoop, go through the door, and climb the stairwell.
- I push open the roof bulkhead into the night. A wooden water tower, one bare bulb, tomato buckets, and two folding chairs at the parapet facing the glittering skyline. We sit. A plane's lights blink across the sky…

**T3:**
- The camera follows the plane over a moonlit ocean.
- The descent toward amber lights on a dark sea.
- *Chapter III — Jeddah.*

**Jeddah**
- I'm in the arrivals hall by the carousel, under a bilingual welcome sign. I walk to the glass doors, they slide open, and the warm night hits: amber light, palms, a white tent canopy overhead.
- I walk along the curb to the waiting car and get in. The door closes, then opens again.
- I step out at the left end of the Corniche. The car pulls away, and the Red Sea lies dark and wide ahead.
- I walk right along the railing. Karak tea from the cart. The lantern pier with its fishermen. Then a bench facing King Fahd's Fountain rising white on the horizon. We sit.
- At the end of the promenade a tiled arch hung with fanous lanterns leads inland. I pass under it into a lively street: coral-stone buildings with carved green balconies, a shisha café, a kid with balloons, valets.
- At the top of the street, warm light spills from L'Entrecôte's door. The doorman opens it, and I step inside. Wood, mirrors, white cloths. The waiter leads us to the corner table and the candle. Steak-frites. Our dinner.
- Afterward I walk back to the front door and step out into the night…

**T4:**
- A boarding pass is stamped JED → RUH.
- Desert at golden hour, then the KAFD towers rising.
- An escalator rises into a white lattice canopy.

**Riyadh**
- I step off the escalator from under the station's lattice at the foot of the KAFD wadi. Terraces of native planting and water channels climb ahead between faceted glass towers. I wind upward past a family cooling their feet in a channel, then a shaded acacia bench.
- I pass under the skywalk as a monorail pod glides overhead. The PIF Tower's crown catches the last gold light.
- At the top, wide stone steps between two towers lead up into the plaza. A long reflecting pool, the Grand Mosque's faceted form glowing to one side. The kiosk host pours us qahwa and hands us dates.
- I walk along the pool, climb to the terrace, and sit. The towers light up for blue hour, and their reflections reach toward us. The promise is made. The camera rises, and the tower lights become stars…

**T5:**
- Clouds part over cypress hills.
- A little train crosses the poppy fields and stops at a tiny halt.
- We walk up toward a stone gate.
- *Chapter V — Italy.*

**Italy**
- I pass through the town-gate arch into a golden piazza: a bell tower, a fountain, café umbrellas, laundry overhead. A white ribbon is tied to one café chair. The florist, unloading white flowers, mentions a celebration up the hill tonight.
- I leave by the east arch, where a ribbon is tied to the gatepost and a sign points to "Villa".
- A white road curves through vineyards and cypress. A ribbon is on every post. At the stone bridge the florist's truck has stalled with roses spilling out, and we help gather them. Past the shrine, I crest the last curve: the villa on the hill, its first lights against the sunset. My partner looks at me.
- I pass through the wrought-iron gate under a white-rose arch into the courtyard. Guests are arriving, and a vintage car is tied with ribbons. On the Benvenuti board: our names. Friends laughingly sweep my partner away through a side door, and for the first time I'm alone.
- I enter the villa's front door into a small sunlit bedroom. On the dresser are the polaroid, the sand dollar, the lion keychain, the matchbook, and the finjan cup. A note from my partner. I look in the mirror. Through the window the garden's lights switch on, row by row.
- I open the back French doors onto the loggia steps. Below, a lit aisle runs up through the garden between rows of guests, and at the far end, under the flowered arch, my partner is waiting.
- I walk down the steps, under the pergola, and slowly up the aisle while the guests turn. At the arch: the vows, naming every city we passed through.
- Together we walk through the opening in the hedge behind the arch onto the terrace. For the first time the whole valley opens up beneath the stars. At one long table sit the barista, the neighbor (with the cat), the Jeddah waiter, the Riyadh kiosk host, and the florist. Our mementos sit among the candles. I walk to the dance floor. The first dance…

**T6:**
- Lanterns rise, and the camera lifts over the estate.
- The journey map lights its six stops.
- The end.

---

## DELIVERABLE F — Final Connection Audit

| Check | Result |
|---|---|
| Dead ends | **None.** Every room has a story-forward exit except ITA_06, which ends the game by design. Decorative side alleys and fog walls are soft boundaries, not exits. |
| Inaccessible rooms | **None.** All 19 rooms sit on the single critical path. The draft's café spur and uphill gate were removed, and the café is now on the route. |
| Nonsensical exits | **Fixed.** NYC: the street-facing fire escape on a brownstone was replaced with stoop → stairwell → roof bulkhead. Jeddah: the sea-view window in the restaurant was removed as unverified. KAFD: the arrival now shows the KAFD towers, not Kingdom Centre. Every other exit is a door, gate, arch, stair, or vehicle with real adjacency. |
| Repeated room types | **Resolved.** There is one airport and no station rooms. There is one restaurant interior; the NYC restaurant was cut so it doesn't duplicate the Entrecôte or Italy. There is one park-like green (Crissy Field, a beach); the Alamo Square park was cut. There are two residential streets (SF_01, NYC_02), deliberately contrasted: a sloped pastel street versus a vertical brick block. |
| Overly long sections | Only three rooms are LARGE: NYC_01, RUH_01, ITA_05. RUH_01 and ITA_02 have mid-room beats so they don't read as corridors. The Corniche was reduced to MEDIUM with three stops. |
| Too many transitions | Reduced from 7 to 6, one of them a 3-second micro-cut. The Jeddah night drive was cut. |
| Too many airports | 1 (Jeddah, required). Every other flight is shown only through a window. |
| Rooms with no narrative purpose | **None.** Each room carries a beat, a memento, a cameo, or a reveal. JED_01 is the only pure "breath" room, and it was required. |
| Awkward geography | Each move is a real, walkable adjacency: Pacific Heights → Lyon Steps → Presidio → Crissy Field; Midtown → UWS by subway; the Corniche → one block inland; the KAFD station → wadi → plaza; the town → road → villa → garden → terrace. The Jeddah draft mixed sights from different parts of town into one view; it now uses one sightline (the fountain), and the rawasheen facades moved to the street. |
| Visual redundancy | Each motif has one owner (see ground rules). There are three night "view" moments (the NYC skyline, the Jeddah sea, the Italy valley), each a different subject. Riyadh's view happens at blue hour, and the valley at night is reserved for the finale. |
| Emotional escalation | The progression runs: playful (SF), then big and exciting (NYC), then warm and intimate (Jeddah), then the future and a promise (Riyadh), then dream, realization, separation, the aisle, the vows, and the reunion (Italy). Italy has the most rooms, the largest room, the unique motifs, and the only separation from the partner. |

### Critic suggestions deliberately not adopted
- **A strict single-trip clock** (Riyadh moved to morning). The acts are chapters, not one 3-day itinerary, and the brief asked for dramatic evening light at KAFD. The golden-hour → blue-hour setting keeps that, while the "night skyline" beat stays with NYC.
- **A playable subway platform.** It would be a pure travel room. The 3-second micro-cut does the job.
- **Shrinking Cypress Road into the piazza.** Kept, because the realization needs its own quiet space between the town and the estate.

### Open questions for the creator (do not block the architecture)
1. Who does the player control: you, her, or both? The layout works for any of these, but the separation and aisle beat should be framed to match.
2. Real details for personal anchors:
   - **SF:** our street and the café
   - **NYC:** whose building it was, and your real NYC spot, if it isn't Bryant Park and the Library
   - **Jeddah:** the actual Entrecôte branch, with photos
   - **Riyadh:** what the promise moment is
3. The Italy region: Tuscan by default, swappable to a lake or coastal setting with no layout change.
