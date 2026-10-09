#!/usr/bin/env python3
"""Generate CREDITS.md and COMBINATIONS.md from 10_METADATA/manifest.json.

Run after build_library.py:  python3 -I MAKAN_VIDEO_LAB/10_METADATA/tools/make_docs.py
"""
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = json.loads((ROOT / "10_METADATA" / "manifest.json").read_text(encoding="utf-8"))
ASSETS = [a for a in MANIFEST["assets"] if a.get("download_status") == "downloaded"]

COMBO_NOTES = {
    "object-ring": "Objects orbiting / colliding in a ring, like the reference's pixel-object carousel.",
    "white-canvas-parade": "Isolated things marching across an off-white paper canvas.",
    "pixel-to-real": "A pixel sprite that match-cuts or morphs into a real photo/clip of the same thing.",
    "retro-window": "A 98/XP-style window that opens onto a photo, clip or object.",
    "paper-collage": "Cut-out layering on paper: scribbles, stickers, photos, type.",
    "type-on": "Typewriter text with a blinking cursor and click SFX.",
    "scatter-letters": "Letters that drift, tumble and re-form (the L-O-V-E beat).",
    "thermal-glow": "Orange/red heat-map silhouettes on black (gradient-map footage).",
    "star-flare": "4-point anamorphic star sweeps (tint cyan, screen blend).",
    "ink-wipe": "Ink blots, brush strokes and splats used as transitions.",
    "glitch-transition": "Digital glitch ticks, noise, error popups between cuts.",
    "beat-sync-montage": "Fast unrelated-object sequence cut to music hits.",
    "match-cut": "Shape/colour/object match between consecutive shots.",
    "loop-bg": "Loopable backgrounds and textures.",
}


def rank(a):
    return ({"high": 0, "medium": 1, "low": 2}.get(a.get("reference_match"), 3), a["filename"])


def credits():
    groups = defaultdict(list)
    for a in ASSETS:
        groups[(a.get("source_name") or "unknown", a.get("license") or "UNKNOWN")].append(a)
    out = ["# Credits & Licenses", "",
           "Auto-generated from `10_METADATA/manifest.json` by `tools/make_docs.py`. "
           "Entries marked **ATTRIBUTION REQUIRED** must be credited if used in a published video. "
           "`license_caveat` in the manifest marks licences that rest on a repo-level or README-only claim.", ""]
    for (src, lic), items in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        req = any(i.get("attribution_required") for i in items)
        creators = sorted({str(i.get("creator")) for i in items if i.get("creator")})
        out.append(f"## {src}")
        out.append(f"- License: **{lic}**{'  —  ATTRIBUTION REQUIRED' if req else ''}")
        if creators:
            out.append(f"- Creator(s): {', '.join(creators[:12])}{' …' if len(creators) > 12 else ''}")
        texts = sorted({i.get("attribution_text") for i in items if i.get("attribution_text")})
        for t in texts[:5]:
            out.append(f"- Attribution: `{t}`")
        url = next((i.get("source_url") for i in items if i.get("source_url")), "")
        if url:
            out.append(f"- Source: {url}")
        out.append(f"- Files ({len(items)}): " + ", ".join(f"`{Path(i['filename']).name}`" for i in items[:15])
                   + (" …" if len(items) > 15 else ""))
        out.append("")
    (ROOT / "CREDITS.md").write_text("\n".join(out), encoding="utf-8")


def combinations():
    by_tag = defaultdict(list)
    for a in ASSETS:
        for t in a.get("combo_tags") or []:
            by_tag[t].append(a)
    out = ["# Combination Tags", "",
           "Assets that agents tagged as working together. Each list is ordered by reference match, "
           "capped at 4 per folder for variety. Filter by tag in `asset_browser.html` for the full set.", ""]
    for tag, items in sorted(by_tag.items(), key=lambda kv: -len(kv[1])):
        out.append(f"## `{tag}` ({len(items)} assets)")
        if tag in COMBO_NOTES:
            out.append(f"_{COMBO_NOTES[tag]}_")
        out.append("")
        per_folder = defaultdict(int)
        for a in sorted(items, key=rank):
            f = a["category_folder"]
            if per_folder[f] >= 4:
                continue
            per_folder[f] += 1
            out.append(f"- `{a['filename']}` — {str(a.get('description') or '')[:90]}")
        out.append("")
    (ROOT / "10_METADATA" / "COMBINATIONS.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    credits()
    combinations()
    print("wrote CREDITS.md and 10_METADATA/COMBINATIONS.md")
