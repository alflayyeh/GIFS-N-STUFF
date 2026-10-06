# Image-Generator Prompts

One prompt per room, plus key frames for the transition scenes. Room details come from [WORLD_ARCHITECTURE.md](WORLD_ARCHITECTURE.md). The same prompts, with copy buttons, are on the interactive map (`world-map.html`).

## How to use

- **Midjourney:** paste a prompt as is. Add `--sref <your reference image URL>` so every room matches your style reference. Keep that reference the same for all 19 rooms.
- **ChatGPT or other image tools:** drop everything from `--ar` onward. Attach your reference image and add "Match the pixel-art style of the attached image." Ask for the aspect ratio in words, for example "wide 16:9 image".
- **Consistency:** generate SF_04, NYC_01 and ITA_05 first. Pick the one that looks most right, then use it as the style reference for everything else.
- **Real pixels:** generated "pixel art" is usually not on a true pixel grid. When you pick final images, run them through a pixel-snapping or downscale tool (or have an artist clean them up) before they go in the game.
- **Signs:** generators garble lettering, so the prompts ask for no text. Add signs such as "L'Entrecôte" and "Benvenuti" by hand later.

**Shared style (already included in every prompt):**

> cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text

## Rooms

### SF_01_OUR_STREET  (16:9)

```
a steep San Francisco residential street climbing from lower left to upper right, a row of pastel bay-window Victorian houses in butter yellow, salmon, powder blue and sage along the top, one small yellow Victorian with a tiny stoop, mailbox and two potted plants at left center, stair-stepped sidewalk, a compact car parked angled on the slope, power lines, street trees, a gull on a lamp post, a corner café with a green awning at the far right, thick soft morning fog at the top of the frame, cool grey-green morning light with warm glowing windows. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### SF_02_CORNER_CAFE  (4:3)

```
interior of a small cozy San Francisco corner café seen from above at a 3/4 angle, warm wood floors and counter, glass pastry case and espresso machine on the left, a window booth for two on the right with two coffee cups, steamed-up windows with grey fog outside, corkboard of polaroid photos, sourdough loaves in a basket, chalkboard menu, hanging plants and pendant lamps, mismatched mugs, a glass back door at top right leading to a tiny patio, warm amber interior light against cool fog. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 4:3 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### SF_03_LYON_STREET_STEPS  (9:16)

```
a long switchback stone staircase descending down the screen through sculpted green hedges and terraced flowerbeds, San Francisco Lyon Street Steps, grand houses at the top, an iron garden gate at the top, a landing overlook on the left where the hedges part to reveal a glimpse of a classical domed rotunda and blue bay far below, joggers and a dog walker as tiny figures, a bench on the landing, eucalyptus trees on one side, two old stone gate pillars at the bottom, morning fog thinning into soft sunlight. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 9:16 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### SF_04_CRISSY_FIELD  (16:9)

```
a horizontal San Francisco bayfront beach scene, blue bay water across the top, the red Golden Gate Bridge in the upper left emerging from wisps of burning-off fog, a sandy beach strip with driftwood logs and dune grass, a meadow path and split-rail fence along the bottom, a small white beach hut building and a gravel parking lot with one car and open trunk with suitcases at lower left, a dog chasing gulls, a kite, windsurfer sails, kids building a sandcastle, bright clear late-morning light, breezy and fresh. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### NYC_01_42ND_ST_BRYANT_PARK  (16:9)

```
a dense New York City Midtown street scene, wide avenue with yellow taxis along the bottom, crowded sidewalk with many small pedestrians, along the top the grand stone steps of the New York Public Library with two stone lion statues on the left and Bryant Park with green bistro chairs, plane trees and a small carousel center right, a subway entrance with green globe lamps at the far left, one steam vent, a bodega fruit stand, scaffolding with green netting in a corner, tall brick and glass towers cropping the top of the frame, Empire State Building spire glimpsed between buildings, late afternoon golden light, energetic and busy. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### NYC_02_BROWNSTONE_BLOCK  (9:16)

```
a quiet tree-lined Upper West Side New York street running up the screen at dusk, brownstone townhouses with stoops and black iron railings on both sides, one red-brick walk-up with a green door, ginkgo trees, potted mums, recycling bins, a corner bodega with a cat on the stoop, delivery bikes, water towers on rooftops, a subway stair exit at the bottom left, the treetops and low stone wall of Central Park at the top, blue dusk sky with warm golden windows turning on. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 9:16 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### NYC_03_ROOFTOP_NIGHT  (1:1)

```
a New York tenement rooftop at night seen from above at a 3/4 angle, tar-paper roof with a low brick parapet, a wooden water tower on legs, one bare light bulb over a small roof bulkhead door, two folding chairs and a blanket at the parapet facing the skyline, tomato and herb plants in buckets, an AC unit and vent pipes, the glittering Manhattan skyline in the distance with small Empire State and Chrysler spires, a moon, deep blue night with warm window lights, intimate and romantic. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 1:1 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### JED_01_AIRPORT_ARRIVALS  (16:9)

```
a horizontal airport arrivals scene in Jeddah, Saudi Arabia at night, left third is a cool white polished arrivals hall with a baggage carousel and glass sliding doors, right two thirds is an outdoor covered curb under white peaked tent-like canopy roofs, date palms in square stone planters, concrete bollards, geometric eight-pointed star tiles on columns, luggage carts, families greeting travelers, small figures in white thobes and black abayas, a waiting white car with open door at the far right, runway lights and aircraft tail fins in the background, warm amber sodium light, humid warm night. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### JED_02_CORNICHE  (16:9)

```
the Jeddah Corniche waterfront promenade at night, black-blue Red Sea with white foam across the top, a tall glowing white fountain jet on the sea horizon at upper right, a lantern-lit fishing pier, a palm-lined promenade with geometric Arabic tile patterns in the paving, amber lamp posts reflecting on the water, a stone sea railing, a karak tea and ice cream cart, families picnicking on carpets on a grass strip, kids on scooters, a large abstract sculpture, a tiled arch hung with Ramadan-style fanous lanterns at the far right, warm romantic night. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### JED_03_ENTRECOTE_STREET  (16:9)

```
a lively evening street in Jeddah, Saudi Arabia, at top center an elegant French bistro facade in cream stone with a dark awning, brass lamps and warm light spilling from an open door onto the paving, on the left traditional Hijazi coral-stone houses with carved green wooden rawasheen balconies and mashrabiya screens, on the right a shisha café with floor cushions, hanging fanous lanterns, olive trees in glazed pots, star-pattern paving, valet cars, families out late, a kid with balloons, a minaret silhouette and sea glow beyond the rooftops, warm amber night. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### JED_04_ENTRECOTE_INTERIOR  (4:3)

```
interior of an elegant Parisian steak-frites bistro seen from above at a 3/4 angle, dark wood paneling, large bistro mirrors, brass wall sconces, tables with white tablecloths, a candlelit corner table set for two with steak and fries, a service bar, a host stand by the entrance at the bottom, servers in black with white aprons, a subtle geometric Arabic ceiling lamp, wine glass shelves, warm intimate candlelight. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 4:3 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### RUH_01_KAFD_WADI  (9:16)

```
a futuristic landscaped valley climbing up the screen in the King Abdullah Financial District, Riyadh, stepped stone terraces of desert planting, tall grasses and acacia trees, shallow water channels catching gold light, a winding path, faceted crystalline glass towers rising on both sides, a very tall tower with a sharp angled crown at the top center, an elevated pedestrian skywalk and a curved monorail track crossing overhead with a small train pod, the edge of a flowing white lattice metro station canopy at the bottom, a family dipping feet in a water channel, golden hour sunlight on blue glass, clean, grand and modern. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 9:16 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### RUH_02_KAFD_PLAZA  (1:1)

```
a polished modern plaza in Riyadh's King Abdullah Financial District at blue hour, geometric patterned stone paving, a long reflecting pool, a faceted geometric modern mosque glowing warm gold on one side, a cluster of tall glass towers behind with their crowns lit in cool white and blue, a raised terrace with a bench at the top, a Saudi coffee kiosk with brass dallah pots and dates, slender light poles, modern planters, couples and families strolling, first stars in a deep blue sky, elegant and hopeful. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 1:1 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### ITA_01_HILL_TOWN_PIAZZA  (4:3)

```
a small cobbled piazza in a Tuscan hill town, ochre and peach stucco buildings with green shutters, a bell-tower church facade at the top, an old stone fountain at the center, a café with striped awning and little tables, one white ribbon tied to a café chair, a florist unloading buckets of white flowers, a gelato cart, laundry lines between windows, potted lemon trees, a parked Vespa, a stone gate arch at the bottom and another arch on the right, terracotta roofs stepping up the hill, warm golden afternoon light, dreamy. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 4:3 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### ITA_02_CYPRESS_ROAD  (4:3)

```
a white gravel country road curving in an S shape from lower left to upper right through Tuscan vineyards and olive groves, tall cypress trees lining the road, white ribbon bows tied on every fence post, a small stone bridge over a stream with a little flower truck stopped on it and roses spilling out, a roadside shrine, a wooden signpost, poppies, a wrought-iron estate gate at the top right, an ochre villa on a far hill with the first warm lights, orange sunset sky beginning. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 4:3 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### ITA_03_VILLA_COURTYARD  (4:3)

```
a gravel courtyard in front of a grand ochre Italian villa with an arched loggia and large wooden double doors along the top, a stone fountain wrapped in white flowers at the center, a white rose welcome arch at the bottom entrance, a chalkboard welcome sign on an easel, a vintage car decorated with white ribbons, wedding guests arriving in elegant clothes, helpers carrying chairs, terracotta urns, lemon trees, clipped hedges and cypress at the sides, pink and orange sunset light. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 4:3 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### ITA_04_GETTING_READY  (4:3)

```
interior of a small sunlit Italian villa bedroom seen from above at a 3/4 angle, frescoed plaster walls, terracotta tile floor, a tall standing mirror, a wooden dresser with small keepsakes laid out on it (a polaroid, a sand dollar, a small lion keychain, a matchbook, a tiny Arabic coffee cup), a wedding outfit on a stand, a bouquet in a vase, a folded note, a window with shutters overlooking a garden with string lights, French doors at the top right, warm late sun through the shutters, quiet and emotional. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 4:3 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### ITA_05_GARDEN_CEREMONY  (3:4)

```
a large walled Italian garden prepared for a wedding ceremony at dusk, seen from above at a 3/4 angle, stone loggia steps and a vine-covered pergola at the bottom, a straight aisle strewn with rose petals running up the middle, rows of white chairs with ribbons filled with small guests on both sides, a canopy of warm string lights and lanterns overhead, candles in jars lining the aisle, a violinist, roses, wisteria and olive trees, tall cypress columns and a hedge wall at the top framing a flower-covered ceremony arch, deep violet dusk sky with first stars, the most beautiful and detailed scene, magical and romantic. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 3:4 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### ITA_06_RECEPTION_TERRACE  (16:9)

```
a stone terrace on the edge of a Tuscan hill at night set for a wedding reception, long banquet tables with white cloths, candles and flower centerpieces under strings of warm lights, a small wooden dance floor, a tiered wedding cake table, a small band, lanterns, potted lemon trees, guests toasting, a stone balustrade opening onto a wide valley below with village lights, cypress silhouettes and a distant hill town with a bell tower, starry night sky, joyful and warm. cozy pixel art RPG game map, top-down 3/4 angled perspective, single handcrafted game screen, small dense diorama, chunky charming proportions, buildings show their front facades, trees bushes and roofs framing the edges, clear readable walkway, colorful but tasteful palette, crisp 16-bit pixels, soft ambient light, no main characters, no UI, no legible text --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

## Transition key frames

### T1 · SF → NYC  (16:9)

```
pixel art postcard scene, view from an airplane window over San Francisco Bay, the Golden Gate Bridge small below in a sea of fog, morning light, cozy retro 16-bit style --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### T3 · NYC → Jeddah  (16:9)

```
pixel art postcard scene, airplane window at night over a dark moonlit ocean, then a coastline of warm amber city lights along a black Red Sea, starry sky, cozy retro 16-bit style --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### T4 · Jeddah → Riyadh  (16:9)

```
pixel art scene, airplane window over golden desert dunes at sunset with a cluster of futuristic glass towers rising on the horizon, cozy retro 16-bit style --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### T5 · Riyadh → Italy  (16:9)

```
pixel art scene, a small vintage train crossing rolling green Tuscan hills with poppy fields and cypress rows, a hill town with a bell tower on the horizon, golden afternoon, cozy retro 16-bit style --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```

### T6 · Ending  (16:9)

```
pixel art scene, paper lanterns rising into a starry night sky above a string-lit Italian villa and garden on a hill, wide valley view, magical and emotional, cozy retro 16-bit style --ar 16:9 --style raw --no text, letters, logos, watermark, UI, HUD, blurry, photorealistic, 3D render, isometric grid, close-up characters
```
