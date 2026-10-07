# Research-agent briefs (ready to launch)

All agents share one output contract so the validation agent can merge them
mechanically.

**Output:** `data/modern/agent_<name>.csv`, one row per indicator × country
(all 11 countries, NA rows included), columns:

`figure, indicator_id, indicator, country, value, unit, obs_year,
modern_source, source_url, retrieval_date, status, notes`

* `value`: number exactly as published (no rounding beyond the source), blank = NA
* `unit`: must state the basis explicitly (e.g. `US$ PPP, current prices`,
  `per 100 000 population`, `% of current health expenditure`)
* `obs_year`: per country; newest comparable year, prefer 2025/2026 then 2024, 2023…
* `source_url`: direct query/table URL (OECD Data Explorer SDMX query,
  WDI API call, GHO API call, CMWF chartpack/data page)
* `status`: DIRECTLY UPDATED | CLOSE MODERN EQUIVALENT | NOT COMPARABLE | UNAVAILABLE
* `notes`: definition changes, series breaks, national deviations
* Never interpolate, never fill from a different definition, never use
  Statista/Wikipedia/news/blogs when the official source exists.

Indicator ownership is in `spec/indicators.py` (`agent` field) and
`docs/methodology_map.csv`.

| Agent | Indicators | Primary hosts |
|---|---|---|
| paper-extraction | done (spec/indicators.py) | — |
| oecd | 60 rows (SHA functions, population, IDD, health status, resources, utilisation, HCQI, pharma market, remuneration, wages) | sdmx.oecd.org, data-explorer.oecd.org, www.oecd.org, read.oecd-ilibrary.org |
| worldbank_who | population, surface area, GHED spending (3), OOP % CHE, rural %, density, HALE, prevalence denominators for f10 ratios | api.worldbank.org, data.worldbank.org, ghoapi.azureedge.net, apps.who.int, diabetesatlas.org |
| commonwealth | same/next-day appt, 2-month specialist wait, 3 system-view items, unmet need by income | www.commonwealthfund.org |
| pharma | total pharma spend per capita, 4 brand prices, NCEs | iqvia.com, ifpma.org, efpia.eu, oecd.org, rand.org, aspe.hhs.gov |
| country | coverage (US: CBO), PCP/specialist shares, neonatal mortality excl. <1000 g, urban/rural physicians, US PTCA (HCUP) | cbo.gov, census.gov, cdc.gov, hcup-us.ahrq.gov, kff.org, gmc-uk.org, cma.ca, ec.europa.eu, socialstyrelsen.se, mhlw.go.jp, ahpra/medicalboard.gov.au, europeristat.com |
| validation | independent re-pull of a sample per agent from the official source; resolves conflicts at source; finalises status + change log | all of the above |
| visualization | `src/render.py` from validated `master_dataset.csv` after `src/qc.py` passes | — |
