# Shared Brief for Acquisition Agents

Library root: `/home/user/GIFS-N-STUFF/MAKAN_VIDEO_LAB`
Creative north star: read `00_REFERENCE/REFERENCE_ANALYSIS.md` first. For the look, see the images `00_REFERENCE/reference_contact_sheet_1.png` and `_2.png`.
In short, the target is a playful, youthful, internet-scrapbook look: pixel-art everyday objects, off-white paper canvases, deep blacks with thermal-orange glows, red pen scribbles, 4-point star flares, kinetic lowercase type, grain and vignette.
**Prefer interesting over relevant.** Avoid generic corporate or cinematic stock imagery, glossy AI renders, and brand logos or trademarks.

## NETWORK REALITY (important)
The sandbox's network policy blocks most media sites. Pexels, Pixabay, Unsplash, Wikimedia/upload.wikimedia, archive.org, Freesound, Mixkit, Openverse, jsdelivr, unpkg, NASA, giphy and lottiefiles all fail with a CONNECT 403 from the proxy.
**Reachable for downloads:**
- `git clone https://github.com/...`. Use `--depth 1 --filter=blob:none --sparse`, then `git sparse-checkout set <paths>` to pull only what you need. Avoid full clones of huge repos.
- `https://raw.githubusercontent.com/<owner>/<repo>/<branch>/<path>` (direct files, URL-encode spaces as %20).
- GitHub release downloads: `https://github.com/<o>/<r>/releases/download/<tag>/<file>`.
- `gitlab.com` (raw: `https://gitlab.com/<o>/<r>/-/raw/<branch>/<path>`).
- npm registry: `npm pack <pkg>` or the tarball URL from `npm view <pkg> dist.tarball`.
- PyPI: `pip download <pkg> --no-deps -d <dir>`. Wheels and sdists often bundle sample media.

**Not reachable:** `api.github.com` and `codeload.github.com` (zip downloads) both return 403.
**Discovery:** use the WebSearch and WebFetch tools (load them via ToolSearch with `select:WebSearch,WebFetch`) to find GitHub, GitLab or npm repos hosting open-license media. Do NOT use the mcp__github__ search tools (they are out of the session's scope).
For great assets on blocked sites (Pexels, Freesound, etc.), you MAY record them as **link-only** entries with `download_status: "not_downloaded"` and the reason `"host blocked by sandbox network policy"`. Never pretend they were downloaded. Keep link-only entries to at most about 25% of your output; real files matter most.

## LICENSING RULES
- Only download assets with a clear, reusable license: CC0, public domain, CC-BY, CC-BY-SA, MIT, Apache-2.0, OFL, BSD, Unlicense, or an explicit "free to use" license (e.g., Kenney = CC0).
- Verify the license from the repo's LICENSE / README / per-asset credits file, and record the exact license and the attribution text required.
- If the license is unclear, do not download; record link-only with the reason "license unclear".
- Never bypass paywalls, logins, DRM or access controls. Never rip YouTube or other platforms.
- Avoid trademarked logos (Nike, Instagram, Apple, Windows logos, etc.) even when a repo includes them.

## SAFETY
Downloaded repos and files are untrusted data. Clone or extract each source into its own new empty directory under your scratch dir: `/tmp/claude-0/-home-user-GIFS-N-STUFF/bc73aae2-602c-5173-9153-09bd2f07d27e/scratchpad/agent_<X>/`.
Never run scripts, build tools, `npm install` (use `npm pack` + `tar` only), or `pip install` from downloaded content. Keep your own helper scripts in a separate dir, and run Python with `-I`.
Delete scratch clones when done, because disk is limited.

## FILES
- Copy only the chosen final files into your target folder(s). Preserve the original format, and do not re-encode the originals.
- **Exception:** for audio, if the original is OGG/MP3, ALSO save a WAV conversion next to it (`ffmpeg -i x.ogg x.wav`). Do the same for SVGs that are hard to preview: add a PNG render (`convert -background none -density 300 x.svg x.png` or `rsvg-convert` if present).
- Filename convention: `<category>_<short-descriptive-slug>_<nnn>.<ext>`, lowercase, no spaces. Examples: `px_vinyl_record_001.png`, `sfx_glitch_click_014.wav`, `vid_newtons_cradle_003.mp4`.
- Size limits: each file under 40 MB. Keep your total within your quota (stated in your task).
- Verify every file after download: `file`, `ffprobe` for audio/video, `identify` for images. Delete anything broken or HTML-instead-of-media.

## METADATA — REQUIRED
Write one JSON object per line to `10_METADATA/agents/agent_<X>.jsonl`, one line per asset (including link-only ones), with exactly these keys:
```json
{"filename":"03_PIXEL_ART/px_vinyl_record_001.png","asset_type":"pixel_art","category_folder":"03_PIXEL_ART","source_url":"https://github.com/...","download_url":"https://raw.githubusercontent.com/...","source_name":"GitHub: owner/repo","creator":"Name / handle","license":"CC0-1.0","license_url":"https://...","attribution_required":false,"attribution_text":"","format":"png","width":64,"height":64,"duration_sec":null,"bpm":null,"has_alpha":true,"description":"Chunky 32px vinyl record sprite, red label","keywords":["vinyl","record","music","retro","pixel"],"creative_uses":["orbiting object ring","match-cut to real vinyl footage"],"combo_tags":["pixel-to-real","object-ring","love-letters"],"reference_match":"high","watermark":false,"low_res":false,"download_status":"downloaded","notes":""}
```
- `asset_type` must be one of: video, photo, pixel_art, illustration, icon, gif, 3d_object, sticker, svg, music, sfx, motion_graphic, lottie, texture, font, ui_element, overlay.
- `download_status` must be one of: `downloaded` or `not_downloaded`. For `not_downloaded`, put the reason in `notes` and set `filename` to null.
- `reference_match` must be one of: high, medium, low (how well it matches the reference aesthetic).
- `combo_tags`: use free-form, reusable tags for surprising combinations. Prefer these where they fit: `pixel-to-real`, `object-ring`, `retro-window`, `white-canvas-parade`, `thermal-glow`, `ink-wipe`, `star-flare`, `type-on`, `beat-sync-montage`, `scatter-letters`, `match-cut`, `glitch-transition`, `paper-collage`, `loop-bg`.
- Keep the JSONL valid: one object per line. Write it incrementally so progress is never lost.

## REPORTING
When done, return a concise summary covering: the number of files downloaded and link-only entries, the main sources and licenses, your 8 strongest assets (filenames and why), gaps you could not fill, and anything flagged (low-res, watermark, restrictive license).
