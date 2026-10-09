# Makan Video Lab — Asset Acquisition Report

**Status:** acquisition complete. No video was edited or rendered.
**Totals:**
- **872 verified media files**, about 340 MB.
- **33 link-only leads**: assets found online but not downloaded.
- **0 broken files**, 0 missing files.
- All files are catalogued in `10_METADATA/manifest.json` and `manifest.csv`.

## 1. What the reference asked for
See `00_REFERENCE/REFERENCE_ANALYSIS.md`. In short, the reference has:
- chunky pixel-art everyday objects on off-white paper;
- black scenes with orange "thermal" glowing silhouettes;
- red pen scribbles, ink-blot wipes and a cyan 4-point star flare;
- lowercase type that types itself out with a blinking cursor, and letters that scatter;
- about 15 cuts in 24 s, each landing on a click, pop or whoosh;
- a warm lo-fi music bed at about 86–90 BPM.

## 2. Collection by folder
| Folder | Files | Highlights |
|---|---:|---|
| 01_VIDEO | 70 | Hand silhouettes against light, a Kinect depth silhouette, Lenia "artificial life" heat-maps, CC0 toy figurines on wood, a 1940s B&W film clip, Pyxel pixel-game GIFs, Sintel (CC-BY) excerpts, SMPTE color bars |
| 02_PHOTOGRAPHY | 78 | Kodak suite (neon caps, red door), 4K CC0 architecture (Casa Milà sun-burst, ring-framed tower), NASA space shots, cats, spice bowls, a hermit crab |
| 03_PIXEL_ART | 231 | The reference's object vocabulary in pixel form: heart, cat, coin, camera, clapperboard, cassette, vinyl, cash, joystick and more. Includes 8× nearest-neighbour upscales, pixel SVGs and 5 animated pixel GIFs |
| 04_ILLUSTRATIONS | 84 | 47 Fluent 3D objects (vinyl disc, plant, cap, skateboard, controller…), rainbow-heart GIFs, Phosphor shapes (4-point star, scribble loops, blobs) |
| 05_MUSIC | 29 | CC0 chiptune (HydroGene, Komiku, Junkala), CC-BY lounge electronica (K-Pone), CC-BY-SA game tracks (SuperTux), Kevin MacLeod |
| 06_SOUND_EFFECTS | 204 files / 149 sounds | Whooshes, clicks, pops, glitch ticks, typewriter (keys, bell, return), shutters, vinyl stop, 8-bit coins and jumps, impacts, reverse FX. WAV for every sound |
| 07_MOTION_GRAPHICS | 166 | 18 OFL fonts, 49 Lottie files (full animated A–Z and a blinking cursor), retro 98/XP/7 windows, Kenney star flares and smoke puffs, ink splats, hand-drawn red loops and arrows |
| 08_TEXTURES | 10 | Blue-noise grain, dust and scratch overlays, a film-grain loop, a vignette, paper noise |

## 3. The strongest 30 assets
1. `03_PIXEL_ART/px_heart_dark_red_x8_001.png`: the reference's 8-bit LOVE heart, almost exactly.
2. `03_PIXEL_ART/px_cat_sitting_x8_001.png`: a pixel cat with a red collar, for the object ring.
3. `03_PIXEL_ART/px_gold_coin_x8_001.png`: a chunky gold coin.
4. `03_PIXEL_ART/px_camera_x8_001.png`: a pixel camera with a flash sparkle, for the "action." card.
5. `03_PIXEL_ART/px_clapperboard_x8_001.png`: the clapperboard from the ring.
6. `03_PIXEL_ART/px_cassette_x8_001.png`: a blue and yellow cassette tape.
7. `03_PIXEL_ART/px_sl_vinyl_record_001.png`: a pixel vinyl record for the "curiosity." card (recolour the label red).
8. `03_PIXEL_ART/px_gif_vinyl_spin_001.gif`: the vinyl, already spinning.
9. `03_PIXEL_ART/px_gif_coin_spin_001.gif`: a spinning coin loop.
10. `04_ILLUSTRATIONS/il_fluent3d_optical_disk_001.png`: a glossy 3D disc, for the pixel-to-3D-to-real ladder.
11. `04_ILLUSTRATIONS/il_fluent3d_potted_plant_001.png`: the plant from the reference ring, in 3D.
12. `04_ILLUSTRATIONS/il_fluent3d_skateboard_001.png`: the skateboard from the reference ring.
13. `04_ILLUSTRATIONS/il_fluent3d_video_game_001.png`: a game controller.
14. `01_VIDEO/vid_hands_moving_083.mp4`: a hand silhouette waving against a glowing white light. Gradient-map it to orange for the "own ability" hand shot.
15. `01_VIDEO/vid_kinect_depth_silhouette_010.mp4`: a depth-camera body silhouette. The closest real footage to the thermal look.
16. `01_VIDEO/vid_lenia_gyrorbium_071.gif`: a blue-to-red heat-map surface that breathes. Abstract and satisfying.
17. `01_VIDEO/vid_toy_monster_004.mp4`: a grinning toy monster on wood. Use it for pixel-to-real match-cuts (5 sibling toy clips).
18. `01_VIDEO/vid_vintage_bw_office_film_008.mp4`: grainy 1940s film, to play inside a retro window.
19. `01_VIDEO/vid_pyxel_perlin_noise_021.gif`: pixel noise that reads as a heat map.
20. `02_PHOTOGRAPHY/ph_kodak_neon_caps_shadows_003.png`: neon caps casting long shadows, an echo of the cap sprite.
21. `02_PHOTOGRAPHY/ph_casa_mila_courtyard_sunburst_051.jpg`: looking up a red-orange courtyard into a sun-burst (4K).
22. `02_PHOTOGRAPHY/ph_milan_tower_circular_frame_056.jpg`: a tower framed by a white ring on black. Minimal and graphic.
23. `02_PHOTOGRAPHY/ph_kodak_red_door_latch_002.png`: a full-frame signal-red texture, for the red-background card.
24. `07_MOTION_GRAPHICS/overlays/mg_star_flare_bold4pt_003.png`: the 4-point star flare. Tint it cyan and use screen blend.
25. `07_MOTION_GRAPHICS/brushes_scribbles/mg_loop_underline_001_red.svg`: a red hand-drawn loop for scribble draw-ons.
26. `07_MOTION_GRAPHICS/brushes_scribbles/mg_ink_splat_burst_001.png`: an ink splat for collisions and wipes.
27. `07_MOTION_GRAPHICS/ui/mg_ui_w98_notepad_cursor_001.png`: a 98-style notepad that already says "how do you communicate a change_".
28. `07_MOTION_GRAPHICS/lottie/typeface/mg_lottie_typeface_blinking_cursor_000.json`: a blinking cursor, plus a full animated A–Z for scattering letters.
29. `05_MUSIC/mu_komiku_remember_this_shadow_024.ogg`: a mellow chip-synth bed at about 86 BPM, CC0. The closest match to the reference tempo.
30. `06_SOUND_EFFECTS/mechanical/sfx_typewriter_cc0_088.wav`: real typewriter keys for the type-on cards. Pair with `sfx_typewriter_bell_cc0_089.wav`.

**Honourable mentions:**
- Music: `05_MUSIC/mu_hydrogene_monstervania_1_018.mp3` (CC0 chiptune, about 89 BPM) and `mu_kpone_crushed_ice_cocktail_015.ogg` (warm lounge keys, CC-BY).
- SFX: `06_SOUND_EFFECTS/whooshes/sfx_whoosh_short_airy_030.wav` (cut whoosh) and `06_SOUND_EFFECTS/textures/sfx_vinyl_stop_brake_094.wav` (for the pre-outro dropout).
- Fonts: `07_MOTION_GRAPHICS/fonts/` has Plus Jakarta Sans, Outfit and Bricolage Grotesque, which are close to the reference headline face.

## 4. Surprising combinations (tagged in the manifest)
`10_METADATA/COMBINATIONS.md` lists 14 combo tags across 872 assets. Some ready-made pairings:
- **Pixel to 3D to real:**
  - pixel vinyl (`px_sl_vinyl_record_001`) to 3D disc (`il_fluent3d_optical_disk_001`) to the spinning GIF;
  - pixel cat to 3D cat to a cat photo (`ph_cat_tabby_red_handkerchief_005.jpg`);
  - pixel cap to 3D cap to the Kodak neon caps.
- **Retro window opens onto a photo:** a 98-style error popup (`mg_ui_w98_error_popup_001.png`, "something went wrong, but it is fine.") with the Saturn photo or the 1940s film playing inside.
- **Thermal hand:** gradient-map `vid_hands_moving_083.mp4` or `vid_fingers_waving_084.mp4` black, red, orange, yellow, add `mg_light_halo_bloom_012.png`, and set `mu_komiku_remember_this_shadow_024.ogg` underneath.
- **Object parade on white:** the Fluent 3D set marching across `tx_gen_paper_noise_001.png`. Cut each object on a `bleeps/` blip, with pixel-coin and 8-bit SFX for the coin.
- **LOVE letters:** Lottie letters L, O, V, E with red scribble loops orbiting them, ending on the pixel heart. Use `sfx_reverse_whoosh_070` into the vinyl-stop dropout.
- **Heat-map interlude:** Lenia GIFs to Pyxel perlin noise to the Kinect depth silhouette. All three share the blue-to-red ramp.

## 5. Gaps, and assets worth generating with AI
These still lack good open-licence sources on the reachable hosts:
1. **True thermal / heat-map footage of a person** in profile and of a reaching hand. The orange-on-black glow is the reference's signature, and the current stand-ins need gradient-mapping.
2. **Pixel-art skateboard, baseball cap and potted plant in full colour.** Only 3D or monochrome versions exist. Add matching pixel vinyl and book sprites in one consistent palette and 3/4 tilt.
3. **A pixel "object ring" sprite sheet** with all twelve reference objects in one style, plus burst and smoke frames for the collisions.
4. **A cyan anamorphic star-flare animation** (sweep plus fade, alpha). The current flares are static white PNGs.
5. **Ink-blob wipe animations** (black and red, alpha, about 0.5 s) and **red pen scribble draw-on** sequences.
6. **Scanned paper textures** (warm off-white, fibre, slight crumple) and **real film-grain and dust plates**. The current grain and paper are procedural.
7. **Light leaks, VHS tracking and CRT scan-line loops.**
8. **A lo-fi hip-hop / warm keys bed at 86–90 BPM** with a clean dropout point. The library has chiptune and lounge tracks but no true lo-fi beat.
9. **Isolated real-object cutouts (alpha PNG)** of everyday objects: vinyl, film camera, cassette, sneakers, houseplant, cash, game controller.
10. **A vinyl crackle recording, a record scratch, and an ink or paint splat foley.** The current versions are synthetic stand-ins.
11. **Kinetic type presets in the headline face:** letter scatter and tumble, scale-punch, typewriter with a block cursor.

## 6. Licensing notes (read before publishing)
- **No attribution needed:** the majority is CC0, MIT, Apache, BSD or OFL.
- **286 files require attribution**, listed per source in `CREDITS.md`. The main ones:
  - Streamline Pixel icons, HackerNoon icons and handy-arrows (all CC-BY 4.0);
  - Intel sample videos (CC-BY 4.0);
  - Sintel and Big Buck Bunny (CC-BY 3.0);
  - K-Pone music (CC-BY 3.0) and Kevin MacLeod (CC-BY);
  - sklearn sample photos (CC-BY 2.0) and the Solus hermit crab (CC-BY 3.0);
  - SerenityOS icons (BSD notice);
  - Lenia (MIT).
- **ShareAlike (`license_restrictions` flag, 11 files):** the SuperTux music tracks are CC-BY-SA, so a remix of them must share alike. The 98.css windows also embed CC-BY-SA MS Sans Serif glyphs.
- **`license_caveat` flag (98 files):** rights rest on a repo-level or README-only claim. These are the Bevy demo clips (which may contain third-party sample assets), the Kodak suite (no formal licence), handy-arrows (no LICENSE file; CC-BY 4.0 per the project site), the HydroGene MP3s (CC0 per a game repo's README) and one microscopy clip. They are fine for a proof of concept; clear them before any commercial release.
- **Derivatives made by the agents, all labelled in the notes:**
  - nearest-neighbour upscales (`*_x8_*`);
  - PNG renders of SVGs;
  - red-recoloured scribbles;
  - 5 pixel GIFs animated from CC0/CC-BY sprites;
  - 8 reversed SFX;
  - stream-copied excerpts of longer videos;
  - 3 procedural texture plates (generated in-house, CC0).
- **Synthetic but third-party:** 10 RezaParsian SFX (vinyl crackle, shutter and others) are generated by code upstream. They are CC0 and marked as such.
- **No watermarks were found.** 91 files are flagged `low_res`. They are mostly tiny originals (with upscales provided alongside), the 768×512 Kodak images and the Sintel excerpts at 290 px tall.

## 7. Environment constraint, and how to add more
The sandbox's network policy blocked Pexels, Pixabay, Unsplash, Wikimedia, Internet Archive, Freesound, Mixkit, Openverse, OpenGameArt and itch.io. Every file was sourced from **GitHub, GitLab, npm and PyPI** mirrors of openly licensed media. The best blocked finds are kept as **33 link-only leads** in the manifest (`download_status: "not_downloaded"`). They include:
- Juhani Junkala's chiptune albums;
- Eric Skiff's *Resistor Anthems*;
- Komiku on OpenGameArt;
- tagirijus glitch SFX;
- the Prelinger Archives;
- Wikimedia object photos.

To fill the gaps, allow those domains in the environment's network settings and re-run an acquisition pass. See `README.md`.
