"""Automated quality-control tests run before any modern figure is drawn.

Input: data/modern/master_dataset.csv (long format, one row per
indicator x country). Exits non-zero if any hard check fails.
"""
import math
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "spec"))
sys.path.insert(0, str(ROOT / "src"))
from indicators import INDICATORS, COUNTRIES  # noqa: E402
from render import rank_row, row_mean  # noqa: E402

REQUIRED = ["figure", "indicator_id", "indicator", "country", "value",
            "unit", "obs_year", "modern_source", "source_url",
            "retrieval_date", "status", "notes"]
STATUSES = {"DIRECTLY UPDATED", "CLOSE MODERN EQUIVALENT", "NOT COMPARABLE",
            "UNAVAILABLE"}


def isna(v):
    return v is None or (isinstance(v, float) and math.isnan(v))


def run(path):
    df = pd.read_csv(path)
    errors, warnings = [], []
    missing_cols = [c for c in REQUIRED if c not in df.columns]
    if missing_cols:
        return [f"missing columns {missing_cols}"], []

    spec = {i["id"]: i for i in INDICATORS}
    for iid, g in df.groupby("indicator_id"):
        s = spec.get(iid)
        if s is None:
            errors.append(f"{iid}: not in spec")
            continue
        # duplicate / omitted countries
        dup = g["country"][g["country"].duplicated()].tolist()
        if dup:
            errors.append(f"{iid}: duplicate countries {dup}")
        miss = set(COUNTRIES) - set(g["country"])
        if miss:
            errors.append(f"{iid}: countries omitted (must be NA rows) "
                          f"{sorted(miss)}")
        # status vocabulary
        bad = set(g["status"]) - STATUSES
        if bad:
            errors.append(f"{iid}: bad status {bad}")
        have = g[~g["value"].isna()]
        # every value must have source + URL + year
        for _, r in have.iterrows():
            for col in ("modern_source", "source_url", "obs_year",
                        "retrieval_date"):
                if isna(r[col]) or str(r[col]).strip() == "":
                    errors.append(f"{iid}/{r.country}: value without {col}")
        # identical units (catches per-1000 vs per-100 000, PPP vs nominal,
        # current vs constant dollars, which are all encoded in `unit`)
        units = set(have["unit"])
        if len(units) > 1:
            errors.append(f"{iid}: mixed units {units}")
        u = " ".join(units).lower()
        # percentage vs fraction confusion
        if "%" in u or "percent" in u:
            vals = have["value"].astype(float)
            if (vals > 100).any() or (vals < 0).any():
                errors.append(f"{iid}: % outside 0-100")
            if len(vals) and vals.max() <= 1.0 and s["orig_values"] and \
                    max(v for v in s["orig_values"].values()
                        if v is not None) > 1.5:
                errors.append(f"{iid}: looks like fractions, 2018 used %")
        # order-of-magnitude drift vs 2018 (flags unit errors)
        for _, r in have.iterrows():
            o = s["orig_values"].get(r.country)
            if o not in (None, 0) and r.value not in (0,):
                ratio = float(r.value) / o
                if ratio > 5 or ratio < 0.2:
                    warnings.append(f"{iid}/{r.country}: {r.value} vs 2018 "
                                    f"{o} (x{ratio:.2f}) - check units")
        # obs_year sanity
        for _, r in have.iterrows():
            if not re.fullmatch(r"\d{4}(-\d{4})?", str(r.obs_year)
                                .replace(".0", "")):
                errors.append(f"{iid}/{r.country}: obs_year '{r.obs_year}'")
        # rank/mean recomputation
        vals = {c: (None if isna(v) else float(v))
                for c, v in zip(g["country"], g["value"])}
        ranked = rank_row(vals)
        nums = [v for _, v in ranked if v is not None]
        if nums != sorted(nums, reverse=True):
            errors.append(f"{iid}: rank order does not match values")
        m, k = row_mean(vals)
        if m is not None:
            mm = sum(nums) / len(nums)
            if abs(mm - m) > 1e-9:
                errors.append(f"{iid}: mean mismatch")
        # definition comparability must be stated when not direct
        st = g["status"].iloc[0]
        if st != "DIRECTLY UPDATED" and g["notes"].isna().all():
            errors.append(f"{iid}: status {st} but no change note")
    missing_ind = set(spec) - set(df["indicator_id"])
    if missing_ind:
        errors.append(f"indicators absent from dataset: {sorted(missing_ind)}")
    return errors, warnings


if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else \
        ROOT / "data/modern/master_dataset.csv"
    e, w = run(p)
    for x in w:
        print("WARN ", x)
    for x in e:
        print("FAIL ", x)
    print(f"{len(e)} failures, {len(w)} warnings")
    sys.exit(1 if e else 0)
