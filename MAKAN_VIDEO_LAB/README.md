# MAKAN_VIDEO_LAB: asset library for an experimental launch video

This folder holds an organized, licence-tracked library of **872 verified media files**. The files are video, photos, pixel art, 3D objects, music, SFX, motion graphics, fonts and textures. They were gathered for a playful, internet-scrapbook launch video. Nothing here is edited yet. The library exists so that an editing session can start experimenting immediately.

## Quick start for a new Claude Code session
1. **Read these first, in order:**
   - `00_REFERENCE/REFERENCE_ANALYSIS.md`: the creative north star, a breakdown of `reference.mp4`.
   - `REPORT.md`: what's here, the strongest 30 assets, gaps, licensing.
   - `10_METADATA/COMBINATIONS.md`: assets grouped by creative combination tag.
2. **Query the manifest** rather than listing folders:
   ```bash
   python3 -c "
   import json; m=json.load(open('MAKAN_VIDEO_LAB/10_METADATA/manifest.json'))
   for a in m['assets']:
       if a['download_status']=='downloaded' and 'object-ring' in (a.get('combo_tags') or []) and a.get('reference_match')=='high':
           print(a['filename'], '|', a.get('description'))
   "
   ```
   Paths in the manifest are relative to `MAKAN_VIDEO_LAB/`. A spreadsheet version is in `10_METADATA/manifest.csv`.
3. **Browse visually:**
   - Open `asset_browser.html` in a browser, from this folder so the relative paths resolve. It has search, filters by folder, type, licence, combo tag and reference match, inline previews and audio players.
   - Or look at the contact sheets in `09_PREVIEWS/contact_sheets/`.
4. **Use the files directly.** Originals are untouched; derived files are labelled in `notes`.

## Folder map
| Folder | Contents | Filename prefix |
|---|---|---|
| `00_REFERENCE/` | The reference MP4, its analysis, contact sheets and audio spectrogram. Study only, not a reusable asset. | — |
| `01_VIDEO/` | 70 clips: mp4, mov, mpg and GIF. | `vid_` |
| `02_PHOTOGRAPHY/` | 78 photos, up to 6000 px. | `ph_` |
| `03_PIXEL_ART/` | 231 pixel sprites. `*_x8_*` files are 8× nearest-neighbour upscales; pixel SVGs each have a PNG render; `px_gif_*` are animated. | `px_` |
| `04_ILLUSTRATIONS/` | 3D emoji objects, isometric tiles, shapes and GIFs, all with alpha. | `il_` |
| `05_MUSIC/` | 29 tracks (OGG and MP3 originals). | `mu_` |
| `06_SOUND_EFFECTS/` | Subfolders: `glitch/ ui/ clicks_pops/ whooshes/ mechanical/ bleeps/ camera/ reverse/ transitions/ impacts/ textures/`. Every sound has a WAV. | `sfx_` |
| `07_MOTION_GRAPHICS/` | Subfolders: `fonts/` (OFL TTFs with OFL.txt), `lottie/` (bodymovin JSON), `ui/` (98/XP/7 CSS kits and rendered PNG windows), `overlays/` (flares, smoke, sparks), `brushes_scribbles/`, `shapes/`. | `mg_` |
| `08_TEXTURES/` | Grain, dust, scratches, vignette, paper noise. | `tx_` |
| `09_PREVIEWS/` | `thumbs/` (one per asset, named by manifest `id`; videos also get a `_strip.jpg`), `contact_sheets/`, `lottie_renders/`. | — |
| `10_METADATA/` | `manifest.json` and `.csv`, `qc_report.json`, `COMBINATIONS.md`, raw per-agent JSONL in `agents/`, `AGENT_BRIEF.md`, and `tools/`. | — |

## Manifest fields
Each asset row has these fields:
- **Identity:** `id`, `filename`, `category_folder`, `asset_type`, `title`, `artist`, `description`.
- **Source and licence:** `source_name`, `source_url`, `download_url`, `creator`, `license`, `license_url`, `attribution_required`, `attribution_text`.
- **Technical:** `format`, `width`, `height`, `duration_sec`, `bpm`, `has_alpha`.
- **Creative:** `keywords`, `creative_uses`, `combo_tags`, `reference_match` (high, medium or low).
- **QC:** `watermark`, `low_res`, `download_status`, `notes`, `qc_exists`, `qc_opens`, `qc_flags`, `bytes`, `sha256`, `similar_to`, `thumbnail`, `agent`.

- `download_status` is `downloaded` or `not_downloaded`. Not-downloaded rows are link-only leads, with the reason in `notes`.
- `qc_flags` can include:
  - `low_res`;
  - `attribution_required`;
  - `license_restrictions` (ShareAlike or GPL);
  - `license_caveat` (repo-level or README-only licence evidence);
  - `link_only`.
- `similar_to` lists visually near-identical assets (perceptual hash). Use it to avoid repeats.
- Combo tags:
  - `object-ring`, `white-canvas-parade`, `pixel-to-real`, `retro-window`, `paper-collage`;
  - `type-on`, `scatter-letters`, `thermal-glow`, `star-flare`, `ink-wipe`;
  - `glitch-transition`, `beat-sync-montage`, `match-cut`, `loop-bg`.

## Licensing in one paragraph
Most assets are CC0, MIT, Apache, BSD or OFL. Anything with `attribution_required: true` must be credited in a published video. `CREDITS.md` has the credit text grouped by source. Check `license_restrictions` (CC-BY-SA music, MS Sans Serif in the 98.css windows) and `license_caveat` before any commercial release. Reference footage is not reusable. No trademarked logos were collected on purpose.

## Practical tips for editing
- **Pixel art:** scale with nearest-neighbour (`ffmpeg -vf scale=iw*8:ih*8:flags=neighbor`), or use the `*_x8_*` files.
- **White overlays** (`07_MOTION_GRAPHICS/overlays/`) are white on alpha. Tint them, for example cyan `#19C8FF` for star flares, and use screen or add blend.
- **Thermal look:** gradient-map the hand and silhouette clips (`vid_hands_moving_083`, `vid_fingers_waving_084`, `vid_kinect_depth_silhouette_010`) to black, `#E0261B`, `#FF5A00` and `#FFB000`.
- **Lottie:** render it with lottie-web (`10_METADATA/tools/vendor/lottie.min.js`) or import it with the bodymovin or After Effects pipeline. `09_PREVIEWS/lottie_renders/` shows three frames of each.
- **Music:** the files are compressed originals. Make a WAV when needed with `ffmpeg -i in.ogg out.wav`.
- **Reference tempo** is about 86–90 BPM. The closest tracks are `mu_komiku_remember_this_shadow_024` and `mu_hydrogene_monstervania_1_018`. The `bpm` values are autocorrelation estimates and may be half or double the true tempo.
- **Palette:** paper `#E6E4E3`, ink `#0E0C0C`, signal red `#E0261B`, thermal orange `#FF5A00`, flare cyan `#19C8FF`.

## Rebuilding the catalogue after adding assets
1. Add files to the right folder.
2. Append one JSON object per asset to a JSONL file in `10_METADATA/agents/`. Follow the schema in `10_METADATA/AGENT_BRIEF.md`.
3. Run:
```bash
pip install cairosvg playwright   # SVG thumbnails; Lottie previews (uses Chromium in /opt/pw-browsers)
python3 -I MAKAN_VIDEO_LAB/10_METADATA/tools/render_lottie.py    # optional: Lottie preview frames
python3 -I MAKAN_VIDEO_LAB/10_METADATA/tools/build_library.py    # QC, dedupe, thumbs, contact sheets, manifest, gallery
python3 -I MAKAN_VIDEO_LAB/10_METADATA/tools/make_docs.py        # CREDITS.md + COMBINATIONS.md
```
- `build_library.py` verifies that every file opens (with ffprobe, Pillow and font magic bytes).
- It deletes exact duplicates; pass `--no-dedupe-delete` to keep them. Files bundled inside packages are never deleted.
- It flags low-res files and licence issues, finds near-duplicates, and adds files on disk that have no metadata as `orphan` rows.

## Acquisition context
Six parallel agents gathered the assets: video, photography, pixel art and illustrations, music, SFX, and motion graphics with textures. The sandbox's network policy only allowed GitHub, GitLab, npm and PyPI, so every file comes from open-licence mirrors on those hosts. Stock sites (Pexels, Pixabay, Unsplash, Freesound, Wikimedia, Internet Archive, OpenGameArt) were blocked. Their best finds are recorded as link-only leads in the manifest. To expand the library, allow those domains in the environment's network settings and run another acquisition pass that uses `10_METADATA/AGENT_BRIEF.md`.
