#!/usr/bin/env python3
"""Merge agent metadata, QC every asset, build previews, manifest and gallery.

Usage:  python3 -I MAKAN_VIDEO_LAB/10_METADATA/tools/build_library.py [--no-dedupe-delete]

Idempotent: safe to re-run after adding assets. Inputs are the per-agent
JSONL files in 10_METADATA/agents/. Outputs:
  10_METADATA/manifest.json, manifest.csv, qc_report.json
  09_PREVIEWS/thumbs/*, 09_PREVIEWS/contact_sheets/*
  asset_browser.html (library root)
"""
import csv
import hashlib
import html
import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageSequence

ROOT = Path(__file__).resolve().parents[2]
META = ROOT / "10_METADATA"
PREV = ROOT / "09_PREVIEWS"
THUMBS = PREV / "thumbs"
SHEETS = PREV / "contact_sheets"
ASSET_DIRS = ["01_VIDEO", "02_PHOTOGRAPHY", "03_PIXEL_ART", "04_ILLUSTRATIONS",
              "05_MUSIC", "06_SOUND_EFFECTS", "07_MOTION_GRAPHICS", "08_TEXTURES"]
IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff"}
VID_EXT = {".mp4", ".webm", ".mov", ".mkv", ".avi", ".m4v", ".ogv"}
AUD_EXT = {".wav", ".ogg", ".mp3", ".flac", ".m4a", ".aiff", ".aif", ".opus"}
FONT_EXT = {".ttf", ".otf", ".woff", ".woff2"}
SKIP_NAMES = {".DS_Store", "Thumbs.db"}
DELETE_DUPES = "--no-dedupe-delete" not in sys.argv

FIELDS = ["id", "filename", "category_folder", "asset_type", "title", "artist", "description",
          "source_name", "source_url", "download_url", "creator", "license", "license_url",
          "attribution_required", "attribution_text", "format", "width", "height",
          "duration_sec", "bpm", "has_alpha", "keywords", "creative_uses", "combo_tags",
          "reference_match", "watermark", "low_res", "download_status", "notes",
          "qc_exists", "qc_opens", "qc_flags", "bytes", "sha256", "similar_to",
          "thumbnail", "agent"]


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=180)


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def ffprobe(p):
    r = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_format", "-show_streams", str(p)])
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def dhash(img, size=8):
    g = img.convert("L").resize((size + 1, size), Image.LANCZOS)
    px = list(g.tobytes())
    bits = 0
    for row in range(size):
        for col in range(size):
            bits = (bits << 1) | (px[row * (size + 1) + col] > px[row * (size + 1) + col + 1])
    return bits


def checker(size, sq=12):
    bg = Image.new("RGB", size, (236, 234, 232))
    d = ImageDraw.Draw(bg)
    for y in range(0, size[1], sq):
        for x in range(0, size[0], sq):
            if (x // sq + y // sq) % 2:
                d.rectangle([x, y, x + sq - 1, y + sq - 1], fill=(222, 219, 216))
    return bg


def flatten(img, box=320, pixel=False):
    img = img.copy()
    resample = Image.NEAREST if pixel else Image.LANCZOS
    scale = min(box / img.width, box / img.height)
    if pixel or scale < 1:
        img = img.resize((max(1, int(img.width * scale)), max(1, int(img.height * scale))), resample)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        bg = checker(img.size)
        bg.paste(img, mask=img.split()[3])
        return bg
    return img.convert("RGB")


def svg_to_png(src, dst):
    try:  # pip install cairosvg (ImageMagick's SVG delegate is unavailable here)
        import cairosvg
        cairosvg.svg2png(url=str(src), write_to=str(dst), output_width=640)
        if dst.exists():
            return True
    except Exception:
        pass
    for cmd in (["rsvg-convert", "-w", "640", "-b", "none", str(src), "-o", str(dst)],
                ["convert", "-background", "none", "-density", "200", str(src), "-resize", "640x640", str(dst)]):
        try:
            if run(cmd).returncode == 0 and dst.exists():
                return True
        except FileNotFoundError:
            continue
    return False


def font_card(src, dst):
    try:
        f1 = ImageFont.truetype(str(src), 56)
        f2 = ImageFont.truetype(str(src), 26)
    except Exception:
        return False
    im = Image.new("RGB", (640, 320), (230, 228, 227))
    d = ImageDraw.Draw(im)
    d.text((24, 40), "makan", font=f1, fill=(14, 12, 12))
    d.text((24, 140), "how do you show it?", font=f2, fill=(224, 38, 27))
    d.text((24, 200), "ABCDEFG 0123456789 !?", font=f2, fill=(43, 43, 43))
    d.text((24, 260), src.name[:48], font=ImageFont.load_default(), fill=(100, 100, 100))
    im.save(dst, quality=88)
    return True


def lottie_card(data, dst, name):
    im = Image.new("RGB", (640, 360), (14, 12, 12))
    d = ImageDraw.Draw(im)
    w, h = data.get("w"), data.get("h")
    fr, ip, op = data.get("fr") or 30, data.get("ip") or 0, data.get("op") or 0
    lines = ["LOTTIE ANIMATION", name[:44], f"{w}x{h}  {fr} fps  {(op - ip) / fr:.2f}s",
             f"layers: {len(data.get('layers', []))}"]
    for i, t in enumerate(lines):
        d.text((24, 40 + i * 40), t, fill=(255, 90, 0) if i == 0 else (230, 228, 227))
    im.save(dst, quality=88)


def text_card(dst, title, sub):
    im = Image.new("RGB", (640, 360), (230, 228, 227))
    d = ImageDraw.Draw(im)
    d.text((24, 140), title, fill=(14, 12, 12))
    d.text((24, 180), sub[:80], fill=(224, 38, 27))
    im.save(dst, quality=88)


def is_pixel(entry):
    return entry.get("asset_type") == "pixel_art" or entry.get("category_folder") == "03_PIXEL_ART"


def probe(entry, path, thumb_base):
    """Return (opens, info dict, flags, dhash or None, thumb relpath or None)."""
    ext = path.suffix.lower()
    info, flags, dh, thumb = {}, [], None, None
    tjpg = thumb_base.with_suffix(".jpg")
    try:
        if ext in IMG_EXT:
            with Image.open(path) as im:
                im.verify()
            with Image.open(path) as im:
                info["width"], info["height"] = im.size
                info["has_alpha"] = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
                frames = getattr(im, "n_frames", 1)
                if frames > 1:
                    info["frames"] = frames
                    durs = [fr.info.get("duration", 0) for fr in ImageSequence.Iterator(im)]
                    info["duration_sec"] = round(sum(durs) / 1000, 2) or None
                    im.seek(0)
                first = im.convert("RGBA")
                dh = dhash(first)
                flatten(first, pixel=is_pixel(entry) and max(im.size) < 320).save(tjpg, quality=86)
                thumb = tjpg
                if max(im.size) < 512 and not is_pixel(entry) and entry.get("asset_type") not in ("icon", "pixel_art", "sticker"):
                    flags.append("low_res")
            return True, info, flags, dh, thumb
        if ext == ".svg":
            ET.parse(path)
            png = thumb_base.with_name(thumb_base.name + "_svg.png")
            if svg_to_png(path, png):
                with Image.open(png) as im:
                    info["width"], info["height"] = im.size
                    first = im.convert("RGBA")
                    dh = dhash(first)
                    flatten(first).save(tjpg, quality=86)
                png.unlink(missing_ok=True)
                thumb = tjpg
            info["has_alpha"] = True
            return True, info, flags, dh, thumb
        if ext in VID_EXT:
            pr = ffprobe(path)
            if not pr:
                return False, info, ["unreadable"], None, None
            vs = [s for s in pr["streams"] if s.get("codec_type") == "video"]
            if not vs:
                return False, info, ["no_video_stream"], None, None
            info["width"], info["height"] = vs[0].get("width"), vs[0].get("height")
            dur = float(pr["format"].get("duration") or vs[0].get("duration") or 0)
            info["duration_sec"] = round(dur, 2)
            info["has_audio"] = any(s.get("codec_type") == "audio" for s in pr["streams"])
            ss = max(0.0, dur * 0.3)
            run(["ffmpeg", "-y", "-v", "error", "-ss", f"{ss:.2f}", "-i", str(path), "-frames:v", "1",
                 "-vf", "scale=320:320:force_original_aspect_ratio=decrease", str(tjpg)])
            strip = thumb_base.with_name(thumb_base.name + "_strip.jpg")
            fps = 6 / dur if dur > 0 else 1
            run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-vf",
                 f"fps={fps:.4f},scale=200:-2,tile=6x1", "-frames:v", "1", str(strip)])
            if tjpg.exists():
                thumb = tjpg
                with Image.open(tjpg) as im:
                    dh = dhash(im)
            if (info["height"] or 0) < 360:
                flags.append("low_res")
            return True, info, flags, dh, thumb
        if ext in AUD_EXT:
            pr = ffprobe(path)
            if not pr or not any(s.get("codec_type") == "audio" for s in pr["streams"]):
                return False, info, ["unreadable"], None, None
            a = [s for s in pr["streams"] if s.get("codec_type") == "audio"][0]
            info["duration_sec"] = round(float(pr["format"].get("duration") or 0), 3)
            info["sample_rate"] = int(a.get("sample_rate") or 0)
            info["channels"] = a.get("channels")
            png = thumb_base.with_suffix(".png")
            run(["ffmpeg", "-y", "-v", "error", "-i", str(path), "-filter_complex",
                 "aformat=channel_layouts=mono,showwavespic=s=640x160:colors=E0261B", "-frames:v", "1", str(png)])
            if png.exists():
                with Image.open(png) as im:
                    bg = Image.new("RGB", im.size, (230, 228, 227))
                    bg.paste(im.convert("RGBA"), mask=im.convert("RGBA").split()[3])
                    bg.save(tjpg, quality=86)
                png.unlink()
                thumb = tjpg
            return True, info, flags, None, thumb
        if ext in FONT_EXT:
            with open(path, "rb") as f:
                magic = f.read(4)
            ok = magic in (b"\x00\x01\x00\x00", b"OTTO", b"true", b"wOFF", b"wOF2")
            if ok and font_card(path, tjpg):
                thumb = tjpg
            return ok, info, flags if ok else ["bad_font_magic"], None, thumb
        if ext == ".json":
            data = json.loads(path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "layers" in data and "fr" in data:
                info["width"], info["height"] = data.get("w"), data.get("h")
                fr = data.get("fr") or 30
                info["duration_sec"] = round(((data.get("op") or 0) - (data.get("ip") or 0)) / fr, 2)
                lottie_card(data, tjpg, path.name)
                thumb = tjpg
            return True, info, flags, None, thumb
        # css, txt, zip, etc.: existence is all we can check
        if path.stat().st_size == 0:
            return False, info, ["empty_file"], None, None
        text_card(tjpg, ext.upper().lstrip(".") + " FILE", path.name)
        return True, info, flags, None, tjpg
    except Exception as e:  # noqa: BLE001 - QC must never crash on one bad file
        return False, info, [f"error:{type(e).__name__}"], None, None


def load_entries():
    entries, bad = [], []
    for jl in sorted((META / "agents").glob("*.jsonl")):
        agent = jl.stem.replace("agent_", "")
        for n, line in enumerate(jl.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError:
                bad.append(f"{jl.name}:{n}")
                continue
            e["agent"] = agent
            fn = e.get("filename")
            if fn:
                fn = str(fn).replace("\\", "/")
                if fn.startswith(str(ROOT)):
                    fn = os.path.relpath(fn, ROOT)
                fn = fn.split("MAKAN_VIDEO_LAB/")[-1]
                e["filename"] = fn
                e["category_folder"] = fn.split("/")[0]
            entries.append(e)
    return entries, bad


def main():
    THUMBS.mkdir(parents=True, exist_ok=True)
    SHEETS.mkdir(parents=True, exist_ok=True)
    entries, bad_lines = load_entries()

    # Deduplicate metadata rows that point at the same file (keep the last, most complete one).
    by_file, linkonly = {}, []
    for e in entries:
        if e.get("filename"):
            prev = by_file.get(e["filename"])
            if prev:
                prev.update({k: v for k, v in e.items() if v not in (None, "", [])})
            else:
                by_file[e["filename"]] = e
        else:
            linkonly.append(e)

    # Orphans: files on disk with no metadata row.
    on_disk = set()
    for d in ASSET_DIRS:
        for p in (ROOT / d).rglob("*"):
            if p.is_file() and p.name not in SKIP_NAMES and not p.name.startswith("."):
                rel = p.relative_to(ROOT).as_posix()
                on_disk.add(rel)
                if rel not in by_file:
                    by_file[rel] = {"filename": rel, "category_folder": d, "download_status": "downloaded",
                                    "agent": "orphan", "notes": "No metadata row from an agent; provenance unknown.",
                                    "asset_type": "unknown", "license": "UNKNOWN"}

    assets = list(by_file.values())
    hashes, dhashes, removed = {}, {}, []
    for i, e in enumerate(sorted(assets, key=lambda x: x["filename"])):
        rel = e["filename"]
        p = ROOT / rel
        flags = list(e.get("qc_flags") or []) if isinstance(e.get("qc_flags"), list) else []
        flags = [f for f in flags if not f.startswith(("missing", "duplicate", "unreadable", "error:"))]
        e["id"] = "A" + hashlib.md5(rel.encode()).hexdigest()[:8]
        e["qc_exists"] = p.exists()
        if not p.exists():
            e["qc_opens"] = False
            e["qc_flags"] = flags + ["missing_file"]
            e["download_status"] = "missing"
            continue
        e["bytes"] = p.stat().st_size
        h = sha256(p)
        e["sha256"] = h
        if h in hashes:
            keep = hashes[h]
            e["qc_flags"] = flags + [f"duplicate_of:{keep['filename']}"]
            e["download_status"] = "removed_duplicate"
            removed.append(rel)
            if DELETE_DUPES:
                p.unlink()
            continue
        hashes[h] = e
        tb = THUMBS / e["id"]
        opens, info, pflags, dh, thumb = probe(e, p, tb)
        e["qc_opens"] = opens
        for k, v in info.items():
            if v is not None and (k not in ("width", "height", "duration_sec", "has_alpha") or True):
                e[k] = v
        e["format"] = e.get("format") or p.suffix.lower().lstrip(".")
        flags += pflags
        if "low_res" in flags:
            e["low_res"] = True
        if e.get("watermark"):
            flags.append("watermark")
        lic = str(e.get("license") or "").upper()
        if not lic or "UNKNOWN" in lic or "UNCLEAR" in lic:
            flags.append("license_unverified")
        elif any(t in lic for t in ("NC", "ND", "GPL", "SA", "EDITORIAL")):
            flags.append("license_restrictions")
        if e.get("attribution_required"):
            flags.append("attribution_required")
        e["qc_flags"] = sorted(set(flags))
        if thumb:
            e["thumbnail"] = thumb.relative_to(ROOT).as_posix()
        if dh is not None:
            dhashes[e["id"]] = dh

    # Visual similarity (dHash hamming distance).
    ids = list(dhashes)
    sim = {i: [] for i in ids}
    for a in range(len(ids)):
        for b in range(a + 1, len(ids)):
            if bin(dhashes[ids[a]] ^ dhashes[ids[b]]).count("1") <= 5:
                sim[ids[a]].append(ids[b])
                sim[ids[b]].append(ids[a])
    id2file = {e["id"]: e["filename"] for e in assets}
    for e in assets:
        e["similar_to"] = [id2file[x] for x in sim.get(e.get("id"), [])]

    for e in linkonly:
        e["id"] = "L" + hashlib.md5((e.get("source_url") or json.dumps(e, sort_keys=True)).encode()).hexdigest()[:8]
        e["download_status"] = "not_downloaded"
        e.setdefault("category_folder", {"A": "01_VIDEO", "B": "02_PHOTOGRAPHY", "C": "04_ILLUSTRATIONS",
                                         "D": "05_MUSIC", "E": "06_SOUND_EFFECTS",
                                         "F": "07_MOTION_GRAPHICS"}.get(e["agent"], "LINK_ONLY"))
        e["qc_flags"] = ["link_only"]

    live = [e for e in assets if e.get("download_status") == "downloaded" and e.get("qc_opens")]
    all_rows = sorted(assets, key=lambda x: x["filename"]) + linkonly

    # Contact sheets per category (visual assets only).
    for f in SHEETS.glob("*.jpg"):
        f.unlink()
    sheet_index = []
    try:
        lab = ImageFont.truetype("DejaVuSans.ttf", 11)
    except Exception:
        lab = ImageFont.load_default()
    for d in ASSET_DIRS:
        items = [e for e in live if e["category_folder"] == d and e.get("thumbnail")
                 and not e["filename"].lower().endswith(tuple(AUD_EXT))]
        if not items:
            continue
        per, cols, tw, th = 48, 6, 240, 200
        for page in range((len(items) + per - 1) // per):
            chunk = items[page * per:(page + 1) * per]
            rows = (len(chunk) + cols - 1) // cols
            sheet = Image.new("RGB", (cols * tw, rows * th + 40), (230, 228, 227))
            dr = ImageDraw.Draw(sheet)
            dr.text((10, 12), f"{d}  page {page + 1}  ({len(items)} assets)", fill=(14, 12, 12), font=lab)
            for k, e in enumerate(chunk):
                with Image.open(ROOT / e["thumbnail"]) as t:
                    t = t.convert("RGB")
                    t.thumbnail((tw - 12, th - 30))
                    x, y = (k % cols) * tw, 40 + (k // cols) * th
                    sheet.paste(t, (x + (tw - t.width) // 2, y + 4))
                    dr.text((x + 6, y + th - 22), Path(e["filename"]).name[:36], fill=(43, 43, 43), font=lab)
            out = SHEETS / f"contact_{d}_p{page + 1}.jpg"
            sheet.save(out, quality=85)
            sheet_index.append(out.relative_to(ROOT).as_posix())

    # Manifest JSON / CSV.
    manifest = {
        "library": "MAKAN_VIDEO_LAB",
        "root": str(ROOT),
        "counts": {
            "total_rows": len(all_rows),
            "downloaded_ok": len(live),
            "link_only": len(linkonly),
            "removed_duplicates": len(removed),
            "broken_or_missing": len([e for e in assets if e.get("download_status") in ("missing",)
                                      or (e.get("download_status") == "downloaded" and not e.get("qc_opens"))]),
            "by_folder": {d: len([e for e in live if e["category_folder"] == d]) for d in ASSET_DIRS},
        },
        "contact_sheets": sheet_index,
        "assets": all_rows,
    }
    (META / "manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    extra = sorted({k for e in all_rows for k in e} - set(FIELDS))
    with open(META / "manifest.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS + extra, extrasaction="ignore")
        w.writeheader()
        for e in all_rows:
            w.writerow({k: ("; ".join(map(str, v)) if isinstance(v, list) else v) for k, v in e.items()})
    qc = {
        "bad_jsonl_lines": bad_lines,
        "removed_duplicates": removed,
        "broken": [e["filename"] for e in assets if e.get("download_status") == "downloaded" and not e.get("qc_opens")],
        "missing": [e["filename"] for e in assets if e.get("download_status") == "missing"],
        "orphans_no_metadata": [e["filename"] for e in assets if e.get("agent") == "orphan"],
        "low_res": [e["filename"] for e in live if "low_res" in e.get("qc_flags", [])],
        "watermark": [e["filename"] for e in live if e.get("watermark")],
        "license_restrictions": [f'{e["filename"]} ({e.get("license")})' for e in live if "license_restrictions" in e["qc_flags"]],
        "license_unverified": [e["filename"] for e in live if "license_unverified" in e["qc_flags"]],
        "similar_groups": sorted({tuple(sorted([e["filename"]] + e["similar_to"])) for e in live if e.get("similar_to")}),
    }
    (META / "qc_report.json").write_text(json.dumps(qc, indent=1), encoding="utf-8")
    build_gallery(all_rows, manifest["counts"])
    print(json.dumps(manifest["counts"], indent=1))
    print({k: len(v) for k, v in qc.items()})


def build_gallery(rows, counts):
    slim_keys = ["id", "filename", "category_folder", "asset_type", "title", "description", "creator", "license",
                 "attribution_text", "source_url", "width", "height", "duration_sec", "bpm", "keywords",
                 "combo_tags", "creative_uses", "reference_match", "qc_flags", "thumbnail", "download_status",
                 "notes", "has_alpha", "similar_to"]
    data = [{k: r.get(k) for k in slim_keys if r.get(k) not in (None, "", [])} for r in rows]
    tpl = (Path(__file__).parent / "gallery_template.html").read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = tpl.replace("/*__DATA__*/[]", payload).replace("/*__COUNTS__*/{}", json.dumps(counts))
    (ROOT / "asset_browser.html").write_text(out, encoding="utf-8")


if __name__ == "__main__":
    main()
