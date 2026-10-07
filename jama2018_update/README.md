# JAMA 2018 ranked-matrix figures — modern data update

Rebuilds the seven ranked colored-cell matrix figures (Figures 1, 4, 5, 7, 9,
10, 11) of Papanicolas, Woskie & Jha, *JAMA* 2018;319(10):1024-1039, using the
newest comparable data from the same sources the paper used.

## Layout

| Path | Contents |
|---|---|
| `spec/indicators.py` | All 99 indicator rows: label, unit, definition, 2018 source/year, 2018 values, planned modern source, owner agent, preliminary status |
| `docs/01_figure_inventory_and_methodology_map.md` | Deliverables 1-2 (figure inventory + source-methodology map) |
| `docs/methodology_map.csv` | Same map, machine-readable |
| `docs/agent_briefs.md` | Output contract and ownership for the research agents |
| `data/original_2018/values_2018.csv` | 2018 baseline, long format |
| `src/render.py` | Deterministic JAMA-style renderer (matplotlib) with a fixed country colour map |
| `src/render_2018_check.py` | Re-draws the 2018 figures from the transcribed values (renderer fidelity check) |
| `src/qc.py` | QC tests (ranks, duplicates, omissions, units, %/fraction, mean, sourcing, change notes) |
| `output/figures_2018_check/` | 2018 re-draws (check only; not deliverables) |

## Rebuild

```
pip install matplotlib pandas openpyxl
python3 src/build_inventory.py
python3 src/render_2018_check.py
python3 src/qc.py data/modern/master_dataset.csv   # once the modern data exist
```

## Notes from the transcription

* Figure values are recorded where they differ from Supplement 2 (US inpatient 19
  vs 17, US outpatient 42 vs 44, the retail pharma per capita row, Germany Lantus
  54 vs 61).
* The printed 2018 means do not match the printed cells for three rows
  (overweight/obese 55.6 vs 52.2 recomputed, nurse remuneration 51 795 vs
  56 512, Humira 1436 vs 1397). The modern figures recompute every mean.
* Figure 10 label "30-d Mortality per 1000 patients" with AMI is per 100
  (eTable 14). Figure 11 "Population density per sq mile" values are per km².
