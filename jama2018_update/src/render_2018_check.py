"""Render the 2018 figures from the transcribed 2018 values.

Purpose: a fidelity check of the renderer against the printed JAMA figures
(same ranks, same cells, same means). Output goes to
output/figures_2018_check/ and is never mixed with the modern figures.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "spec"))
sys.path.insert(0, str(ROOT / "src"))
from indicators import (INDICATORS, FIGURES, FOOTNOTES_2018, LABEL_MARKS,  # noqa
                        SECTION_MARKS, CELL_MARKS_2018)
from render import render_figure  # noqa


def main():
    for fig_no, title in FIGURES.items():
        rows = []
        for i in INDICATORS:
            if i["fig"] != fig_no:
                continue
            r = dict(i)
            r["values"] = dict(i["orig_values"])
            rows.append(r)
        means = {r["id"]: r["mean_2018"] for r in rows}
        render_figure(fig_no, title, rows,
                      ROOT / "output/figures_2018_check" / f"fig{fig_no}_2018",
                      ["2018 VALUES (renderer fidelity check, transcribed "
                       "from Papanicolas et al, JAMA 2018)."] +
                      FOOTNOTES_2018[fig_no],
                      LABEL_MARKS, SECTION_MARKS, CELL_MARKS_2018,
                      mean_override=means, show_n=False, formats=("png",))


if __name__ == "__main__":
    main()
