"""Write deliverables 1 & 2 (figure inventory, source-methodology map) and
the 2018 baseline dataset from the spec."""
import sys
from collections import OrderedDict
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "spec"))
from indicators import INDICATORS, FIGURES, COUNTRIES, COUNTRY_NAMES  # noqa

NOT_QUALIFYING = [
    ("Figure 2", "Health Spending as a Percentage of GDP",
     "Clustered bar chart"),
    ("Figure 3", "Social Spending as a Percentage of GDP",
     "Clustered bar chart"),
    ("Figure 6", "Practicing Physicians by Primary Care Specialization",
     "Stacked bar chart"),
    ("Figure 8", "Performance on Key Measures of Utilization",
     "Four horizontal bar-chart panels"),
    ("Table", "Insurance System Characteristics", "Text table (no ranking)"),
]


def main():
    out = ROOT / "docs"
    out.mkdir(exist_ok=True)
    md = ["# Figure inventory and source-methodology map", "",
          "Source paper: Papanicolas I, Woskie LR, Jha AK. Health Care "
          "Spending in the United States and Other High-Income Countries. "
          "*JAMA*. 2018;319(10):1024-1039. Definitions and sources from "
          "Supplement 1 (eTables 5-15); values from the printed figures "
          "(Supplement 2 eTables 1-7 used as a cross-check).", "",
          "## 1. Qualifying figures (ranked colored-cell matrices)", "",
          "| Figure | Domain | Page | Indicator rows | Sections |",
          "|---|---|---|---|---|"]
    pages = {1: 1026, 4: 1030, 5: 1031, 7: 1033, 9: 1035, 10: 1036,
             11: 1037}
    for f, t in FIGURES.items():
        rows = [i for i in INDICATORS if i["fig"] == f]
        secs = list(OrderedDict.fromkeys(r["section"] for r in rows
                                         if r["section"]))
        md.append(f"| Figure {f} | {t} | {pages[f]} | {len(rows)} | "
                  f"{'; '.join(secs)} |")
    md += ["", f"Total indicator rows: **{len(INDICATORS)}** (the paper "
           "says 98 indicators; the 99th row is the non-health mean wage "
           "used as the denominator for the Figure 5 remuneration ratios).",
           "", "### Figures checked and excluded (different visual format)",
           "", "| Item | Title | Format |", "|---|---|---|"]
    md += [f"| {a} | {b} | {c} |" for a, b, c in NOT_QUALIFYING]

    md += ["", "## 2. Indicators and source-methodology map", "",
           "Status is preliminary (from documentation review); the final "
           "status per indicator is in the audit table after validation.",
           ""]
    for f, t in FIGURES.items():
        md += [f"### Figure {f}. {t}", "",
               "| # | Section | Indicator | Unit | 2018 source (year) | "
               "Planned modern source | Agent | Preliminary status |",
               "|---|---|---|---|---|---|---|---|"]
        for n, i in enumerate([i for i in INDICATORS if i["fig"] == f], 1):
            md.append(
                f"| {n} | {i['section'] or '—'} | "
                f"{i['label'].replace(chr(10), ' ')} | {i['unit']} | "
                f"{i['orig_source']} ({i['orig_year']}) | "
                f"{i['modern_source']} | {i['agent']} | "
                f"{i['prelim_status']} |")
        md.append("")
    (out / "01_figure_inventory_and_methodology_map.md").write_text(
        "\n".join(md))

    # machine-readable map
    rows = []
    for i in INDICATORS:
        rows.append(dict(figure=i["fig"], domain=FIGURES[i["fig"]],
                         section=i["section"], indicator_id=i["id"],
                         indicator=i["label"].replace("\n", " "),
                         unit=i["unit"], definition=i["definition"],
                         orig_source=i["orig_source"],
                         orig_year=i["orig_year"],
                         planned_modern_source=i["modern_source"],
                         agent=i["agent"],
                         preliminary_status=i["prelim_status"],
                         notes=i["notes"]))
    pd.DataFrame(rows).to_csv(out / "methodology_map.csv", index=False)

    # 2018 baseline long table
    base = []
    for i in INDICATORS:
        for c in COUNTRIES:
            base.append(dict(figure=i["fig"], indicator_id=i["id"],
                             indicator=i["label"].replace("\n", " "),
                             country=c, country_name=COUNTRY_NAMES[c],
                             value_2018=i["orig_values"][c],
                             unit=i["unit"], source_2018=i["orig_source"],
                             year_2018=i["orig_year"]))
    pd.DataFrame(base).to_csv(ROOT / "data/original_2018/values_2018.csv",
                              index=False)
    print("wrote inventory, methodology map, 2018 baseline")


if __name__ == "__main__":
    main()
