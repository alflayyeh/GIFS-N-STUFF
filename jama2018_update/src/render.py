"""Deterministic JAMA-style ranked-matrix renderer.

Every number drawn comes from the `values` mapping passed in; nothing is typed
into the figure by hand. Ranking, tie-breaking, NA placement and the mean are
computed here and re-checked by qc.py.
"""
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "spec"))
from indicators import COUNTRIES  # noqa: E402

# Fixed country colours, sampled to approximate the 2018 JAMA figures.
# Used unchanged in every figure.
COUNTRY_COLORS = {
    "US": "#F6F18F",        # yellow
    "UK": "#D9D9D9",        # light grey
    "Germany": "#BDD5EE",   # light blue
    "Sweden": "#F1C3E6",    # pink
    "France": "#DCEAA2",    # yellow-green
    "NLD": "#D3BCE6",       # lavender
    "CHE": "#BEE2E3",       # light teal
    "Denmark": "#DDBBA4",   # tan
    "Canada": "#F8D3AA",    # peach
    "Japan": "#C7E6B5",     # light green
    "Australia": "#F4A9AE", # rose
}
NA_FILL = None              # NA cells keep the country colour, as in 2018
JAMA_RED = "#C8102E"
GRID = "#9A9A9A"
INK = "#1A1A1A"
FONT = "Carlito"

plt.rcParams.update({"font.family": FONT, "pdf.fonttype": 42,
                     "svg.fonttype": "none"})


def fmt(v, decimals):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "NA"
    if decimals is None:
        decimals = 0
    s = f"{v:.{decimals}f}"
    return s


def rank_row(values):
    """Highest to lowest; ties broken by the paper's country order; NA last
    (also in paper country order). Returns list of (country, value)."""
    order = {c: i for i, c in enumerate(COUNTRIES)}
    have = [(c, v) for c, v in values.items() if v is not None]
    na = [(c, None) for c, v in values.items() if v is None]
    have.sort(key=lambda cv: (-cv[1], order[cv[0]]))
    na.sort(key=lambda cv: order[cv[0]])
    return have + na


def row_mean(values):
    v = [x for x in values.values() if x is not None]
    return (sum(v) / len(v), len(v)) if v else (None, 0)


def render_figure(fig_no, title, rows, out_base, footnotes,
                  label_marks=None, section_marks=None, cell_marks=None,
                  mean_override=None, show_n=True, fig_width=7.3,
                  formats=("png", "pdf", "svg")):
    """rows: list of indicator dicts (spec) each with key 'values'
    {country: float|None}. mean_override: {id: value or 'NA'} used only to
    reproduce the 2018 printed means for the fidelity check."""
    label_marks = label_marks or {}
    section_marks = section_marks or {}
    cell_marks = cell_marks or {}
    mean_override = mean_override or {}

    # ---- geometry (inches) ----
    W = fig_width
    margin = 0.12
    label_w = 1.78
    mean_w = 0.42
    n = len(COUNTRIES)
    cell_w = (W - 2 * margin - label_w - mean_w) / n
    head_h = 0.17
    sec_h = 0.17
    row_h = 0.30
    title_h = 0.36

    # pre-compute layout
    items = []
    last_sec = object()
    for r in rows:
        if r["section"] != last_sec:
            if r["section"] is not None:
                items.append(("sec", r["section"]))
            last_sec = r["section"]
        items.append(("row", r))
    table_h = head_h + sum(sec_h if k == "sec" else row_h for k, _ in items)

    # footnotes: wrap to two columns of text
    import textwrap
    fn_lines = []
    for f in footnotes:
        fn_lines += textwrap.wrap(f, 165) or [""]
    fn_h = 0.13 * len(fn_lines) + 0.18
    H = title_h + table_h + fn_h + 0.12

    fig = plt.figure(figsize=(W, H), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)     # y grows downward
    ax.axis("off")

    # ---- title + rules ----
    ax.add_line(plt.Line2D([margin, W - margin], [0.06, 0.06],
                           color=JAMA_RED, lw=1.6))
    ax.text(margin, 0.21, f"Figure {fig_no}. {title}", fontsize=9.5,
            fontweight="bold", color=INK, va="center", ha="left")
    ax.add_line(plt.Line2D([margin, W - margin], [title_h - 0.04] * 2,
                           color=INK, lw=0.6))

    y = title_h
    x0 = margin
    xl = x0 + label_w
    xm = xl + n * cell_w
    xe = xm + mean_w

    def hline(yy, lw=0.5, c=GRID):
        ax.add_line(plt.Line2D([x0, xe], [yy, yy], color=c, lw=lw))

    # header
    hline(y, 0.8, INK)
    ax.text(x0 + 0.04, y + head_h / 2, "Rank (highest to lowest)",
            fontsize=6.6, fontweight="bold", va="center")
    for i in range(n):
        ax.text(xl + (i + 0.5) * cell_w, y + head_h / 2, str(i + 1),
                fontsize=6.6, fontweight="bold", ha="center", va="center")
    ax.text(xm + 0.04, y + head_h / 2, "Mean", fontsize=6.6,
            fontweight="bold", va="center")
    for xx in [xl + i * cell_w for i in range(n + 1)] + [x0, xe]:
        ax.add_line(plt.Line2D([xx, xx], [y, y + head_h], color=GRID,
                               lw=0.5))
    y += head_h
    hline(y, 0.8, INK)

    for kind, obj in items:
        if kind == "sec":
            mark = section_marks.get((fig_no, obj), "")
            ax.add_patch(Rectangle((x0, y), xe - x0, sec_h, fc="#FFFFFF",
                                   ec="none"))
            t = ax.text(x0 + 0.04, y + sec_h / 2, obj, fontsize=6.6,
                        fontweight="bold", va="center")
            if mark:
                _sup(ax, t, mark, fig)
            for xx in (x0, xe):
                ax.add_line(plt.Line2D([xx, xx], [y, y + sec_h],
                                       color=GRID, lw=0.5))
            y += sec_h
            hline(y)
            continue

        r = obj
        vals = r["values"]
        ranked = rank_row(vals)
        # label
        lab = r["label"]
        mark = label_marks.get(r["id"], "")
        t = ax.text(x0 + 0.04, y + row_h / 2, lab, fontsize=6.4,
                    fontweight="bold" if r.get("bold") else "normal",
                    va="center", ha="left", linespacing=1.05, color=INK)
        if mark:
            _sup(ax, t, mark, fig)
        # cells
        pad = 0.018
        for i, (c, v) in enumerate(ranked):
            cx = xl + i * cell_w
            ax.add_patch(Rectangle((cx + pad, y + pad), cell_w - 2 * pad,
                                   row_h - 2 * pad, fc=COUNTRY_COLORS[c],
                                   ec="#8C8C8C", lw=0.35))
            cm = cell_marks.get((r["id"], c), "")
            ax.text(cx + 0.035, y + 0.095, c, fontsize=6.1, va="center",
                    ha="left", color=INK)
            vt = ax.text(cx + 0.035, y + 0.205,
                         fmt(v, r.get("decimals")) if v is not None
                         else "NA", fontsize=6.1, va="center", ha="left",
                         color=INK)
            if cm:
                _sup(ax, vt if v is not None else vt, cm, fig)
        # mean
        if r["id"] in mean_override:
            mv = mean_override[r["id"]]
            mtxt = "NA" if mv is None else fmt(mv, r.get("mean_decimals",
                                                          r.get("decimals")))
            k = None
        else:
            m, k = row_mean(vals)
            mtxt = "NA" if m is None else fmt(m, r.get("mean_decimals",
                                                        r.get("decimals")))
        ax.text(xm + 0.04, y + (0.12 if (show_n and k and k < n) else
                                row_h / 2), mtxt, fontsize=6.3,
                va="center", ha="left")
        if show_n and k and k < n:
            ax.text(xm + 0.04, y + 0.225, f"(n={k})", fontsize=5.0,
                    va="center", ha="left", color="#555555")
        for xx in (x0, xl, xm, xe):
            ax.add_line(plt.Line2D([xx, xx], [y, y + row_h], color=GRID,
                                   lw=0.5))
        y += row_h
        hline(y)

    hline(y, 0.8, INK)
    y += 0.08
    for ln in fn_lines:
        y += 0.13
        ax.text(x0, y, ln, fontsize=5.6, va="bottom", ha="left",
                color="#333333")
    y += 0.08
    ax.add_line(plt.Line2D([margin, W - margin], [y, y], color=INK, lw=0.6))

    out_base = Path(out_base)
    out_base.parent.mkdir(parents=True, exist_ok=True)
    for f in formats:
        fig.savefig(out_base.with_suffix("." + f), dpi=400 if f == "png"
                    else None)
    plt.close(fig)
    return out_base


def _sup(ax, text_artist, mark, fig):
    """Place a small superscript mark after the last line of a text."""
    fig.canvas.draw_idle()
    r = fig.canvas.get_renderer()
    bb = text_artist.get_window_extent(renderer=r)
    inv = ax.transData.inverted()
    # last-line end: approximate with bbox right edge, top of last line
    (x1, y1) = inv.transform((bb.x1, bb.y0))
    lines = text_artist.get_text().split("\n")
    if len(lines) > 1:
        # width of last line
        tmp = ax.text(0, 0, lines[-1], fontsize=text_artist.get_fontsize(),
                      fontweight=text_artist.get_fontweight())
        bb2 = tmp.get_window_extent(renderer=r)
        tmp.remove()
        (x0d, _), (x1d, _) = inv.transform((bb.x0, 0)), \
            inv.transform((bb.x0 + bb2.width, 0))
        x1 = x1d
    ax.text(x1 + 0.005, y1 - 0.075, mark, fontsize=4.6, va="center",
            ha="left")
