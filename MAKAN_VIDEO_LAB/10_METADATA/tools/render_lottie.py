#!/usr/bin/env python3
"""Render preview frames for every Lottie JSON in the library.

Writes 09_PREVIEWS/lottie_renders/<stem>.png: a 3-frame strip (25/50/75%)
on paper-white. build_library.py uses these as thumbnails when present.

Needs: pip install playwright; Chromium at /opt/pw-browsers (or set CHROME).
Usage: python3 -I MAKAN_VIDEO_LAB/10_METADATA/tools/render_lottie.py
"""
import glob
import json
import os
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "09_PREVIEWS" / "lottie_renders"
PLAYER = (Path(__file__).parent / "vendor" / "lottie.min.js").read_text(encoding="utf-8")
CHROME = os.environ.get("CHROME") or next(iter(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")), None)

PAGE = """<!doctype html><html><body style="margin:0;background:#E6E4E3">
<div id="row" style="display:flex;gap:8px;padding:8px"></div>
<script>%s</script></body></html>"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted((ROOT / "07_MOTION_GRAPHICS").rglob("*.json"))
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=CHROME) if CHROME else p.chromium.launch()
        page = browser.new_page(viewport={"width": 1000, "height": 360})
        for f in files:
            try:
                data = json.loads(f.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if not (isinstance(data, dict) and "layers" in data):
                continue
            page.set_content(PAGE % PLAYER)
            ok = page.evaluate("""(d) => {
                const row = document.getElementById('row');
                const ip = d.ip || 0, op = d.op || 1;
                for (const t of [0.25, 0.5, 0.75]) {
                    const box = document.createElement('div');
                    box.style.cssText = 'width:320px;height:320px;background:#fff';
                    row.appendChild(box);
                    const a = lottie.loadAnimation({container: box, renderer: 'svg', loop: false,
                        autoplay: false, animationData: JSON.parse(JSON.stringify(d))});
                    a.goToAndStop(ip + (op - ip) * t, true);
                }
                return true;
            }""", data)
            if ok:
                page.wait_for_timeout(150)
                page.locator("#row").screenshot(path=str(OUT / (f.stem + ".png")))
                print("rendered", f.relative_to(ROOT))
        browser.close()


if __name__ == "__main__":
    main()
