"""Indicator specification for the seven ranked-matrix figures in
Papanicolas, Woskie & Jha, JAMA 2018;319(10):1024-1039.

Every row in Figures 1, 4, 5, 7, 9, 10 and 11 is listed here, in figure order,
with:
  * the label exactly as printed in the figure ("\n" = printed line break),
  * the unit and definition from Supplement 1 (eTables 6, 8-15),
  * the 2018 source and data year from Supplement 1,
  * the 2018 values exactly as printed in the figure (order = COUNTRIES),
  * the planned modern source and the research agent responsible,
  * a preliminary comparability status (finalised by the validation step).

Where the figure and the Supplement 2 eTables disagree, the figure value is
recorded (it is what the figure shows) and the disagreement is noted.
"""

COUNTRIES = ["US", "UK", "Germany", "Sweden", "France", "NLD", "CHE",
             "Denmark", "Canada", "Japan", "Australia"]

COUNTRY_NAMES = {
    "US": "United States", "UK": "United Kingdom", "Germany": "Germany",
    "Sweden": "Sweden", "France": "France", "NLD": "Netherlands",
    "CHE": "Switzerland", "Denmark": "Denmark", "Canada": "Canada",
    "Japan": "Japan", "Australia": "Australia",
}

ISO3 = {"US": "USA", "UK": "GBR", "Germany": "DEU", "Sweden": "SWE",
        "France": "FRA", "NLD": "NLD", "CHE": "CHE", "Denmark": "DNK",
        "Canada": "CAN", "Japan": "JPN", "Australia": "AUS"}

FIGURES = {
    1: "Spending",
    4: "Population Health",
    5: "Workforce and Structural Capacity",
    7: "Utilization",
    9: "Pharmaceuticals",
    10: "Access and Quality",
    11: "Distribution and Equity",
}

# Status vocabulary required by the brief
DIRECT = "DIRECTLY UPDATED"
CLOSE = "CLOSE MODERN EQUIVALENT"
NOTCOMP = "NOT COMPARABLE"
UNAVAIL = "UNAVAILABLE"

# Research agent ownership
A_OECD, A_WB, A_CMWF, A_PHARMA, A_CTRY = (
    "oecd", "worldbank_who", "commonwealth", "pharma", "country")

N = None


def ind(id, fig, section, label, unit, definition, orig_source, orig_year,
        orig_values, modern_source, agent, status, notes="", decimals=None,
        bold=False, mean_2018=None):
    return dict(id=id, fig=fig, section=section, label=label, unit=unit,
                definition=definition, orig_source=orig_source,
                orig_year=orig_year,
                orig_values=dict(zip(COUNTRIES, orig_values)),
                mean_2018=mean_2018, modern_source=modern_source,
                agent=agent, prelim_status=status, notes=notes,
                decimals=decimals, bold=bold)


INDICATORS = [
    # ------------------------------------------------------------------
    # FIGURE 1. SPENDING  (Supplement 1 eTable 6; Supplement 2 eTable 1)
    # ------------------------------------------------------------------
    ind("f1_pop", 1, "General", "Overall population (in millions)",
        "millions", "Total population, de facto, midyear estimate",
        "World Bank WDI SP.POP.TOTL", "2016",
        [323, 66, 83, 10, 64, 17, 8, 6, 36, 127, 24],
        "World Bank WDI SP.POP.TOTL (latest year)", A_WB, DIRECT,
        decimals=0, mean_2018=69),
    ind("f1_pop65", 1, "General", "Population ≥65 y, %", "% of population",
        "Population aged 65 and over as share of total population",
        "OECD.stat (Elderly population); JP, NL, CH from Commonwealth Fund",
        "2014 or closest",
        [14.5, 17.3, 21.4, 19.9, 18.2, 17.3, 17.5, 18.1, 15.7, 25.1, 14.7],
        "OECD Data Explorer, Population (elderly population, % of total)",
        A_OECD, DIRECT, decimals=1, mean_2018=18.2,
        notes="2018 used Commonwealth Fund profiles for JP/NL/CH; modern "
              "update uses OECD for all 11 (same concept)."),
    ind("f1_gdp", 1, "General", "GDP per capita, US $\n(in thousands)",
        "US$ thousands, current prices, current PPPs",
        "GDP per head, current prices and current PPPs (SNA 2008)",
        "OECD.stat Productivity database (PDB_LV)", "2016 or closest",
        [52.1, 38.5, 42.9, 51.6, 41.0, 46.3, 54.0, 53.4, 42.4, 37.5, 45.1],
        "OECD Data Explorer, GDP per capita, USD current prices & PPPs",
        A_OECD, DIRECT, decimals=2, mean_2018=45.90),
    ind("f1_land", 1, "General", "Land area (× 1000 sq km)", "1000 km²",
        "Surface area, incl. inland water bodies and some coastal waterways",
        "World Bank WDI AG.SRF.TOTL.K2", "2015",
        [9834, 244, 357, 450, 549, 42, 42, 43, 9985, 378, 7741],
        "World Bank WDI AG.SRF.TOTL.K2", A_WB, DIRECT, decimals=0,
        mean_2018=2697,
        notes="Label says 'land area' but 2018 source is WDI surface area; "
              "kept the same WDI series."),
    ind("f1_pov", 1, "General", "Poverty rate, % below poverty\nline of 60%",
        "% of population",
        "Poverty rate after taxes and transfers, 60% of median equivalised "
        "disposable income", "OECD Income Distribution Database (IDD)",
        "2015",
        [24, 18, 16, 17, 15, 15, 17, 12, 21, 22, 20],
        "OECD Data Explorer, Income Distribution Database (poverty rate, "
        "60% line, after taxes and transfers)", A_OECD, DIRECT, decimals=0,
        mean_2018=18,
        notes="IDD moved to the 2012 income definition; flag series breaks."),
    ind("f1_the", 1, "Health spending",
        "Total spending on health,\n% of total national GDP", "% of GDP",
        "Total health expenditure (public + private), % of GDP",
        "WHO Global Health Expenditure Database via World Bank "
        "SH.XPD.TOTL.ZS", "2016",
        [17.8, 9.7, 11.3, 11.9, 11.0, 10.5, 12.4, 10.8, 10.3, 10.9, 9.6],
        "WHO GHED via World Bank SH.XPD.CHEX.GD.ZS (current health "
        "expenditure, % GDP)", A_WB, CLOSE, decimals=1, mean_2018=11.5,
        notes="SH.XPD.TOTL.ZS (total incl. capital) was discontinued when "
              "GHED moved to SHA 2011; successor is current health "
              "expenditure, which excludes capital formation."),
    ind("f1_pub", 1, "Health spending",
        "Public spending on health,\n% of total national GDP", "% of GDP",
        "Public (government + social/compulsory insurance) health "
        "expenditure, % of GDP", "World Bank SH.XPD.PUBL (WHO GHED)",
        "2016",
        [8.3, 7.6, 8.7, 10.0, 8.7, 9.5, 7.7, 9.2, 7.4, 8.6, 6.3],
        "WHO GHED via World Bank SH.XPD.GHED.GD.ZS (domestic general "
        "government health expenditure, % GDP)", A_WB, CLOSE, decimals=1,
        mean_2018=8.4,
        notes="SH.XPD.PUBL discontinued. GHED-D includes social health "
              "insurance; compulsory private insurance (CHE, NLD) treatment "
              "must be checked by validation."),
    ind("f1_pc", 1, "Health spending",
        "Mean spending on health\nper capita, US $", "US$ per capita, "
        "current (nominal) exchange rates",
        "Health expenditure per capita, current US$",
        "World Bank SH.XPD.PCAP (WHO GHED)", "2016",
        [9403, 3377, 5182, 6808, 3661, 5202, 6787, 6463, 4641, 3727, 4357],
        "WHO GHED via World Bank SH.XPD.CHEX.PC.CD (current health "
        "expenditure per capita, current US$)", A_WB, CLOSE, decimals=0,
        mean_2018=5419,
        notes="Nominal US$ (not PPP), as in 2018. Successor series is "
              "current health expenditure (excludes capital)."),
    ind("f1_inp", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Inpatient care", "% of current health "
        "expenditure", "Inpatient curative & rehabilitative care "
        "(HC.1.1+HC.2.1)", "OECD/Eurostat/WHO SHA joint questionnaire",
        "2015 or closest",
        [19, 24, 27, 21, 30, 32, 28, 28, 17, 27, 31],
        "OECD Data Explorer, Health expenditure and financing (SHA), by "
        "function", A_OECD, CLOSE, decimals=0, mean_2018=26,
        notes="2018 added ~2 pp of US multi-day observation stays to US "
              "inpatient (17%->19%, an author estimate). That adjustment is "
              "not reproducible from a public series; modern value is the "
              "unadjusted SHA share."),
    ind("f1_outp", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Outpatient care", "% of current health "
        "expenditure", "Outpatient curative & rehabilitative care plus day "
        "care (HC.1.2+HC.1.3+HC.2.2+HC.2.3) for non-US countries",
        "OECD SHA", "2015 or closest",
        [42, 30, 23, 31, 23, 22, 33, 34, 36, 27, 39],
        "OECD SHA by function", A_OECD, CLOSE, decimals=0, mean_2018=31,
        notes="Figure shows US 42 (eTable 1 says 44). Day care added to "
              "outpatient for comparability, as in 2018."),
    ind("f1_ltc", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Long-term care", "% of current health "
        "expenditure", "Long-term care (health), HC.3", "OECD SHA",
        "2015 or closest",
        [5, 18, 16, 26, 11, 26, 19, 24, 14, 19, 2],
        "OECD SHA by function", A_OECD, DIRECT, decimals=0, mean_2018=16),
    ind("f1_goods", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Medical goods", "% of current health "
        "expenditure", "Medical goods (non-specified by function), HC.5",
        "OECD SHA", "2015 or closest",
        [14, 15, 20, 12, 20, 12, 13, 10, 20, 20, 17],
        "OECD SHA by function", A_OECD, DIRECT, decimals=0, mean_2018=16),
    ind("f1_admin", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Governance and\nadministration",
        "% of current health expenditure",
        "Governance and health system & financing administration, HC.7",
        "OECD SHA", "2015 or closest",
        [8, 2, 5, 2, 1, 4, 4, 2, 3, 1, 3],
        "OECD SHA by function", A_OECD, DIRECT, decimals=0, mean_2018=3),
    ind("f1_home", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Home-based care",
        "% of current health expenditure",
        "Home-based curative & rehabilitative care (HC.1.4+HC.2.4)",
        "OECD SHA", "2015 or closest",
        [3, 3, 1, 0, 4, 0, N, N, 0, 3, 0],
        "OECD SHA by function", A_OECD, DIRECT, decimals=0, mean_2018=2),
    ind("f1_prev", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Preventive care",
        "% of current health expenditure", "Preventive care, HC.6",
        "OECD SHA", "2015 or closest",
        [3, 5, 3, 3, 2, 4, 2, 3, 6, 3, 2],
        "OECD SHA by function", A_OECD, DIRECT, decimals=0, mean_2018=3,
        notes="COVID-19 testing/vaccination is recorded in HC.6; 2020-2022 "
              "values are inflated. Validation must check the year used."),
    ind("f1_other", 1,
        "Health expenditure by function of care as a % of total national "
        "health expenditure", "Other",
        "% of current health expenditure",
        "Ancillary services (HC.4) and other/unknown functions", "OECD SHA",
        "2015 or closest",
        [6, 3, 5, 5, 9, 0, 1, 0, 4, 1, 6],
        "OECD SHA by function", A_OECD, DIRECT, decimals=0, mean_2018=4,
        notes="2018 defines 'Other' as HC.4 ancillary; any residual (HC.9) "
              "handling to be documented."),
    ind("f1_cov", 1, None, "Population with health care\ncoverage, %",
        "% of population",
        "Total public and primary private health insurance coverage",
        "OECD Health Statistics (social protection); US: CBO", "2017",
        [90, 100, 99.8, 100, 99.9, 99.9, 100, 100, 100, 100, 100],
        "OECD Data Explorer, Social protection (total health care "
        "coverage); US: CBO baseline (country-specific, as in 2018)",
        A_CTRY, DIRECT, decimals=1, bold=True, mean_2018=99),

    # ------------------------------------------------------------------
    # FIGURE 4. POPULATION HEALTH  (eTable 8; Supplement 2 eTable 2)
    # ------------------------------------------------------------------
    ind("f4_smoke", 4, "Determinants of health",
        "Smoking, % of population\naged ≥15 y who smoke daily",
        "% of population aged 15+", "Daily smokers aged 15+",
        "OECD Health at a Glance 2017", "2015 or closest",
        [11.4, 16.1, 20.9, 11.2, 22.4, 19.0, 20.4, 17.0, 14.0, 18.2, 12.4],
        "OECD Data Explorer, Non-medical determinants of health (tobacco)",
        A_OECD, DIRECT, decimals=1, mean_2018=16.6),
    ind("f4_alc", 4, "Determinants of health",
        "Alcohol consumption, L per\ncapita in population aged ≥15 y",
        "litres pure alcohol per capita 15+",
        "Recorded alcohol consumption (sales), litres per capita 15+",
        "OECD Health at a Glance 2017", "2015 or closest",
        [8.8, 9.5, 11.0, 7.2, 11.9, 8.0, 9.5, 9.4, 8.1, 7.2, 9.7],
        "OECD Data Explorer, Non-medical determinants of health (alcohol)",
        A_OECD, DIRECT, decimals=1, mean_2018=9.1),
    ind("f4_obese", 4, "Determinants of health",
        "Obese or overweight, % of\npopulation aged ≥15 y",
        "% of population aged 15+",
        "Overweight or obese (BMI≥25), measured where available, "
        "self-reported otherwise", "OECD Health at a Glance 2017",
        "2015 or closest",
        [70.1, 62.9, 60.0, 48.3, 49.0, 47.4, 41.0, 47.4, 60.3, 23.8, 63.4],
        "OECD Data Explorer, Non-medical determinants of health "
        "(overweight or obese; measured preferred, self-reported flagged)",
        A_OECD, DIRECT, decimals=1, mean_2018=55.6,
        notes="Footnote a: SE, NLD, CHE, DK self-reported in 2018. Measured "
              "and self-reported are kept as in 2018 and flagged per "
              "country."),
    ind("f4_le", 4, "Life expectancy",
        "Life expectancy in total\npopulation at birth, mean, y", "years",
        "Life expectancy at birth, total population",
        "OECD Health Statistics 2017", "2015",
        [78.8, 81.0, 80.7, 82.3, 82.4, 81.6, 83.0, 80.8, 81.7, 83.9, 82.5],
        "OECD Data Explorer, Health status (life expectancy)", A_OECD,
        DIRECT, decimals=1, mean_2018=81.7),
    ind("f4_hale", 4, "Life expectancy",
        "Health-adjusted life\nexpectancy, mean, y", "years",
        "Healthy life expectancy (HALE) at birth",
        "Listed as OECD 2017; values match WHO GHO HALE 2015", "2015",
        [69.1, 71.4, 71.3, 72.0, 72.6, 72.2, 73.1, 71.2, 72.3, 74.9, 71.9],
        "WHO Global Health Observatory, HALE at birth (WHOSIS_000002)",
        A_WB, CLOSE, decimals=1, mean_2018=72,
        notes="WHO HALE is re-estimated each GHE round; the whole time "
              "series is revised, so 2015 vs modern values are not a "
              "like-for-like trend."),
    ind("f4_le40f", 4, "Life expectancy",
        "Life expectancy for women\naged ≥40 y, mean, y", "years",
        "Remaining life expectancy at age 40, females",
        "OECD Health Statistics 2017", "2015",
        [42.6, 43.7, 43.9, 44.8, 46.4, 43.9, 45.8, 43.4, 44.8, 47.7, 45.4],
        "OECD Data Explorer, Health status (life expectancy at 40, "
        "females)", A_OECD, DIRECT, decimals=1, mean_2018=44.8),
    ind("f4_le40m", 4, "Life expectancy",
        "Life expectancy for men\naged ≥40 y, mean, y", "years",
        "Remaining life expectancy at age 40, males",
        "OECD Health Statistics 2017", "2015",
        [38.7, 40.5, 39.4, 41.5, 40.6, 40.8, 42.0, 39.8, 41.1, 41.8, 41.7],
        "OECD Data Explorer, Health status (life expectancy at 40, males)",
        A_OECD, DIRECT, decimals=1, mean_2018=40.7),
    ind("f4_mmr", 4, "Maternal and infant health",
        "Maternal mortality, deaths per\n100 000 live births",
        "per 100 000 live births", "Maternal deaths, all causes",
        "OECD 2015; Canada: Global Burden of Disease", "2015",
        [26.4, 9.2, 9.0, 4.4, 7.8, 6.7, 5.8, 4.2, 7.3, 6.4, 5.5],
        "OECD Data Explorer, Health status (maternal mortality)", A_OECD,
        DIRECT, decimals=1, mean_2018=8.4,
        notes="US NCHS changed maternal-death coding (pregnancy checkbox, "
              "2018+), which raises US rates vs 2015. Flag."),
    ind("f4_imr", 4, "Maternal and infant health",
        "Infant mortality, deaths per\n1000 live births",
        "per 1000 live births", "Deaths under age 1",
        "OECD 2015; Canada: Conference Board", "2015",
        [5.8, 3.9, 3.3, 2.5, 3.8, 2.5, 3.9, 3.7, 5.1, 2.1, 3.2],
        "OECD Data Explorer, Health status (infant mortality)", A_OECD,
        DIRECT, decimals=1, mean_2018=3.6),
    ind("f4_nmr", 4, "Maternal and infant health",
        "Neonatal mortality, deaths per\n1000 live births",
        "per 1000 live births", "Deaths under 28 days",
        "OECD 2015; Canada: World Data Atlas", "2015",
        [4.0, 2.7, 2.3, 1.7, 2.6, 2.5, 3.1, 3.0, 3.2, 0.9, 2.3],
        "OECD Data Explorer, Health status (neonatal mortality)", A_OECD,
        DIRECT, decimals=1, mean_2018=2.6),
    ind("f4_nmr1000", 4, "Maternal and infant health",
        "Neonatal mortality, deaths per\n1000 live births excluding "
        "<1000 g", "per 1000 live births",
        "Neonatal mortality excluding births <1000 g",
        "Joseph et al, BMJ 2012 (one-off study; US 2004 data)", "2004-2008",
        [1.61, 1.77, 1.49, 1.56, N, 1.96, N, 2.09, 1.63, N, N],
        "No recurring source identified (one-off BMJ study). Country-source "
        "agent to check Euro-Peristat / national vital statistics.",
        A_CTRY, UNAVAIL, decimals=2, mean_2018=1.7),
    ind("f4_lbw", 4, "Maternal and infant health",
        "Low birth weight, % of total\nlive births", "% of live births",
        "Live births <2500 g", "OECD 2015", "2015",
        [8.1, 6.9, 6.6, 4.4, 6.2, 6.5, N, 5.0, 6.3, 9.5, 6.4],
        "OECD Data Explorer, Health status (low birth weight)", A_OECD,
        DIRECT, decimals=1, mean_2018=6.6),

    # ------------------------------------------------------------------
    # FIGURE 5. WORKFORCE AND STRUCTURAL CAPACITY (eTables 9-11; S2 eT3)
    # ------------------------------------------------------------------
    ind("f5_phys", 5, "Practicing workforce",
        "Overall physicians per\n1000 population", "per 1000 population",
        "Practising physicians (total licensed & practising, excl. "
        "students/interns)", "KFF, GMC, CMA, Eurostat, national sources "
        "(eTable 10)", "2013-2017",
        [2.6, 2.1, 4.1, 4.2, 3.1, 3.5, 4.3, 3.6, 2.6, 2.4, 3.5],
        "OECD Data Explorer, Health care resources (practising "
        "physicians per 1000)", A_OECD, CLOSE, decimals=1, mean_2018=3.3,
        notes="2018 built counts from national registers (eTable 10). "
              "OECD practising physicians is the standard harmonised "
              "series; US/UK values differ (US 2.6 vs OECD 2.6)."),
    ind("f5_pcp", 5, "Practicing workforce", "Primary care physicians,\n"
        "% of total", "% of physicians",
        "Practising generalists + family medicine, paediatrics, geriatrics, "
        "internal medicine (functional PCP definition)",
        "National registers (eTable 10)", "2013-2017",
        [43, 45, 45, 33, 54, 47, 48, 22, 48, 43, 45],
        "Country-specific registers replicating eTable 10 definition; "
        "cross-check with OECD physicians by category", A_CTRY, CLOSE,
        decimals=0, mean_2018=43),
    ind("f5_spec", 5, "Practicing workforce", "Specialists, % of total",
        "% of physicians", "Practising physicians not in PCP definition",
        "National registers (eTable 10)", "2013-2017",
        [57, 55, 55, 67, 46, 53, 52, 78, 52, 57, 55],
        "Complement of PCP share (same country-specific sources)", A_CTRY,
        CLOSE, decimals=0, mean_2018=57),
    ind("f5_nurse", 5, "Practicing workforce", "Nurses per 1000 population",
        "per 1000 population", "Practising nurses",
        "OECD / national (eTable 10)", "2013-2017",
        [11.1, 8.2, 13.0, 11.2, 9.4, 12.1, 17.4, 16.3, 9.5, 10.5, 11.5],
        "OECD Data Explorer, Health care resources (practising nurses)",
        A_OECD, DIRECT, decimals=1, mean_2018=11.8),
    ind("f5_rem_gp", 5, "Workforce remuneration, US $",
        "Generalist physicians", "US$ PPP per year (2017 dollars)",
        "Annual remuneration of generalist physicians",
        "Mixed national sources (eTable 11), PPP, inflated to 2017 with "
        "US CPI", "2011-2017",
        [218173, 134671, 154126, 86607, 111769, 109586, N, N, 146286,
         124558, 108564],
        "OECD Data Explorer, Remuneration of health professionals "
        "(GPs, USD PPP); inflate to a single reference year with US CPI-U "
        "as in 2018", A_OECD, CLOSE, decimals=0, mean_2018=133723,
        notes="Footnote a: Japan value is generalists+specialists combined. "
              "2018 used heterogeneous national sources; OECD series mixes "
              "salaried and self-employed. Japan excluded from remuneration "
              "means in 2018 except nursing."),
    ind("f5_rem_sp", 5, "Workforce remuneration, US $",
        "Specialist physicians", "US$ PPP per year (2017 dollars)",
        "Annual remuneration of specialist physicians",
        "Mixed national sources (eTable 11)", "2011-2017",
        [316000, 171987, 181243, 98452, 153180, 191995, N, 140505, 188260,
         N, 202291],
        "OECD remuneration of specialists (USD PPP), CPI-adjusted",
        A_OECD, CLOSE, decimals=0, mean_2018=182657,
        notes="Japan shown as 'Japan^a' with no value in 2018 (combined "
              "figure reported under generalists)."),
    ind("f5_rem_nurse", 5, "Workforce remuneration, US $", "Nurses",
        "US$ PPP per year (2017 dollars)",
        "Annual remuneration of (hospital) nurses",
        "Mixed national sources (eTable 11)", "2011-2017",
        [74160, 49894, 53668, N, 42492, 65082, N, 58891, 55349, 44712,
         64357],
        "OECD remuneration of hospital nurses (USD PPP), CPI-adjusted",
        A_OECD, CLOSE, decimals=0, mean_2018=51795),
    ind("f5_wage", 5, "Workforce remuneration, US $",
        "Non-health-specific annual\nwage, mean", "US$ PPP per year",
        "Average annual wage, all employees (footnote b: 2016 constant "
        "prices, 2016 USD PPP)", "OECD.stat average annual wages", "2016",
        [60154, 42835, 46389, 42816, 42992, 52833, 60124, 52580, 48403,
         39113, 52063],
        "OECD Data Explorer, Average annual wages (USD PPP)", A_OECD, DIRECT,
        decimals=0, mean_2018=49118,
        notes="Must use the same price base as the remuneration rows when "
              "computing ratios."),
    ind("f5_ratio_gp", 5, "Workforce remuneration, US $",
        "Ratio of generalist\nremuneration to mean wage", "ratio",
        "Generalist remuneration / average wage", "Computed", "—",
        [3.6, 3.1, 3.3, 2.0, 2.6, 2.1, N, N, 3.0, N, 2.1],
        "OECD remuneration ratio to average wage (published) or computed "
        "from same-year values", A_OECD, CLOSE, decimals=1, mean_2018=2.7),
    ind("f5_ratio_sp", 5, "Workforce remuneration, US $",
        "Ratio of specialists\nremuneration to mean wage", "ratio",
        "Specialist remuneration / average wage", "Computed", "—",
        [5.3, 3.4, 3.9, 2.3, 3.6, 3.6, N, 2.6, 3.9, N, 3.8],
        "OECD remuneration ratio to average wage", A_OECD, CLOSE,
        decimals=1, mean_2018=3.7),
    ind("f5_ratio_nurse", 5, "Workforce remuneration, US $",
        "Ratio of nurse remuneration\nto mean wage", "ratio",
        "Nurse remuneration / average wage", "Computed", "—",
        [1.23, 1.16, 1.16, N, 0.99, 1.23, N, 1.12, 1.14, 1.14, 1.24],
        "OECD remuneration ratio to average wage", A_OECD, CLOSE,
        decimals=2, mean_2018=1.1),
    ind("f5_mri", 5, "Equipment per 1 million population",
        "Magnetic resonance\nimaging units", "per 1 000 000 population",
        "MRI units, total (hospital + ambulatory)", "OECD; Canada: CMWF",
        "2014 or closest",
        [38.1, 7.2, 30.5, N, 12.6, 12.9, N, N, 8.9, 51.7, 14.7],
        "OECD Data Explorer, Health care resources (MRI units)", A_OECD,
        DIRECT, decimals=1, mean_2018=22),
    ind("f5_ct", 5, "Equipment per 1 million population",
        "Computed tomography\nunits", "per 1 000 000 population",
        "CT scanners, total", "OECD; Canada 2007", "2015 or closest",
        [41.0, 9.5, 35.3, N, 16.6, 13.3, 36.1, 37.1, 12.7, 107.2, 56.1],
        "OECD Data Explorer, Health care resources (CT scanners)", A_OECD,
        DIRECT, decimals=1, mean_2018=36.5),
    ind("f5_mammo", 5, "Equipment per 1 million population",
        "Mammography machine\nunits", "per 1 000 000 population",
        "Mammography machines, total", "OECD; UK: journal article",
        "2015 or closest",
        [43.3, 21.0, N, N, 7.5, N, 28.3, 14.2, 17.3, 33.0, 23.0],
        "OECD Data Explorer, Health care resources (mammographs)", A_OECD,
        DIRECT, decimals=1, mean_2018=23.5,
        notes="2018 per-1M rate appears to be per 1M total population "
              "(OECD reports mammographs per 1M; some editions per 1M "
              "women 50-69). Validation to confirm denominator."),
    ind("f5_beds", 5, "Beds", "Hospital beds per 1000\npopulation",
        "per 1000 population", "Total hospital beds", "OECD",
        "2014 or closest",
        [2.8, 2.7, 8.2, 2.5, 6.1, 3.3, 4.6, 2.7, 2.7, 13.2, 3.8],
        "OECD Data Explorer, Health care resources (hospital beds)", A_OECD,
        DIRECT, decimals=1, mean_2018=4.8),
    ind("f5_ltcbeds", 5, "Beds", "Long-term beds per 1000\npopulation aged "
        "≥65 y", "per 1000 population aged 65+",
        "Long-term care beds in institutions and hospitals", "OECD",
        "2015 or closest",
        [38.8, 49.5, 53.1, 70.6, 59.0, 65.5, 67.6, 48.9, 53.7, 35.1, 54.0],
        "OECD Data Explorer, Long-term care resources (beds in "
        "institutions and hospitals per 1000 65+)", A_OECD, DIRECT,
        decimals=1, mean_2018=54.2),

    # ------------------------------------------------------------------
    # FIGURE 7. UTILIZATION (eTable 12; S2 eTable 4)
    # ------------------------------------------------------------------
    ind("f7_dis_ami", 7, "Discharges per 100 000 population",
        "Acute myocardial infarction", "per 100 000 population",
        "Inpatient discharges, AMI (ICD-10 I21-I22)", "OECD; US 2010",
        "2016 or closest",
        [192, 160, 287, 273, 124, 175, 223, 174, 193, 89, 196],
        "OECD Data Explorer, Hospital discharges by diagnostic category",
        A_OECD, DIRECT, decimals=0, mean_2018=190),
    ind("f7_dis_mental", 7, "Discharges per 100 000 population",
        "Mental and behavioral", "per 100 000 population",
        "Inpatient discharges, mental & behavioural disorders (F00-F99)",
        "OECD", "2016 or closest",
        [679, 269, 1719, 1068, 368, 119, 1182, 892, 629, 319, 856],
        "OECD hospital discharges by diagnostic category", A_OECD, DIRECT,
        decimals=0, mean_2018=736),
    ind("f7_dis_pneu", 7, "Discharges per 100 000 population", "Pneumonia",
        "per 100 000 population", "Inpatient discharges, pneumonia",
        "OECD", "2016 or closest",
        [365, 459, 380, 432, 271, 224, 269, 567, 187, 378, 338],
        "OECD hospital discharges by diagnostic category", A_OECD, DIRECT,
        decimals=0, mean_2018=352,
        notes="2020-2022 pneumonia discharges distorted by COVID-19 coding; "
              "validation to check."),
    ind("f7_dis_copd", 7, "Discharges per 100 000 population",
        "Chronic obstructive\npulmonary disease", "per 100 000 population",
        "Inpatient discharges, COPD", "OECD", "2016 or closest",
        [230, 251, 352, 186, 138, 161, 142, 234, 241, 45, 286],
        "OECD hospital discharges by diagnostic category", A_OECD, DIRECT,
        decimals=0, mean_2018=206),
    ind("f7_mri_ex", 7, "Examinations per 1000 population",
        "Magnetic resonance imaging", "per 1000 population",
        "MRI exams, total", "OECD", "2015 or closest",
        [118, 53, 131, N, 105, 52, 70, 82, 56, 112, 41],
        "OECD Data Explorer, Health care utilisation (diagnostic exams)",
        A_OECD, DIRECT, decimals=0, mean_2018=82),
    ind("f7_ct_ex", 7, "Examinations per 1000 population",
        "Computed tomography", "per 1000 population", "CT exams, total",
        "OECD", "2015 or closest",
        [245, 79, 144, N, 197, 81, 100, 162, 153, 231, 120],
        "OECD health care utilisation (diagnostic exams)", A_OECD, DIRECT,
        decimals=0, mean_2018=151),
    ind("f7_hip", 7, "Surgical procedures",
        "Total hip replacement\nper 100 000 population",
        "per 100 000 population", "Hip replacement (inpatient + day case)",
        "OECD", "2013 or closest",
        [204, 183, 283, 234, 236, 216, 292, 237, 136, 90, 171],
        "OECD Data Explorer, Surgical procedures", A_OECD, DIRECT,
        decimals=0, mean_2018=207),
    ind("f7_knee", 7, "Surgical procedures",
        "Total knee replacement\nper 100 000 population",
        "per 100 000 population", "Knee replacement", "OECD",
        "2013 or closest",
        [226, 141, 190, 124, 145, 118, 176, 168, 166, N, 180],
        "OECD surgical procedures", A_OECD, DIRECT, decimals=0,
        mean_2018=163),
    ind("f7_hyst", 7, "Surgical procedures", "Hysterectomy per 100 000\n"
        "women", "per 100 000 females", "Hysterectomy", "OECD",
        "2013 or closest",
        [266, 161, 301, 186, 182, 167, 291, 197, 232, N, 262],
        "OECD surgical procedures", A_OECD, DIRECT, decimals=0,
        mean_2018=225),
    ind("f7_csec", 7, "Surgical procedures", "Cesarean delivery per\n"
        "100 live births", "per 100 live births", "Caesarean sections",
        "OECD Health at a Glance 2015", "2013 or closest",
        [33, 23, 31, 17, 21, 16, 33, 21, 26, 18, 32],
        "OECD Data Explorer, Health care utilisation (caesarean sections)",
        A_OECD, DIRECT, decimals=0, mean_2018=25),
    ind("f7_cat", 7, "Surgical procedures", "Cataract surgery per 100 000\n"
        "population", "per 100 000 population",
        "Cataract surgery (inpatient + day case)", "OECD.stat",
        "2013 or closest",
        [1110, 736, 1027, 1029, 1207, 1005, 438, 1037, 1060, N, 1060],
        "OECD surgical procedures", A_OECD, DIRECT, decimals=0,
        mean_2018=971),
    ind("f7_cabg", 7, "Cardiovascular procedures per 100 000 population",
        "Coronary artery bypass graft\nsurgery", "per 100 000 population",
        "CABG", "OECD Health at a Glance 2015", "2015 or closest",
        [79, 26, 64, 31, 29, 69, N, 73, 58, N, 54],
        "OECD surgical procedures (CABG)", A_OECD, DIRECT, decimals=0,
        mean_2018=54),
    ind("f7_ptca", 7, "Cardiovascular procedures per 100 000 population",
        "Coronary angioplasty", "per 100 000 population",
        "Transluminal coronary angioplasty (PTCA), incl. outpatient for US",
        "OECD; US from HCUP (incl. outpatient)", "2015 or closest",
        [248, 128, 393, 205, 237, 248, N, 190, 157, 193, 172],
        "OECD surgical procedures (PTCA); US from AHRQ HCUP incl. "
        "outpatient, as in 2018", A_OECD, DIRECT, decimals=0, mean_2018=217),
    ind("f7_los_del", 7, "Length of stay per capita, mean, d",
        "Normal delivery", "days", "ALOS, normal (single spontaneous) "
        "delivery", "OECD Health at a Glance 2015", "2013 or closest",
        [2.0, 1.5, 2.9, 2.3, 4.1, 1.9, 3.6, 2.7, 1.6, 5.7, 2.7],
        "OECD Data Explorer, Health care utilisation (ALOS by diagnostic "
        "category)", A_OECD, DIRECT, decimals=1, mean_2018=2.8),
    ind("f7_los_ami", 7, "Length of stay per capita, mean, d",
        "Acute myocardial infarction", "days", "ALOS, AMI",
        "OECD Health at a Glance 2015", "2013 or closest",
        [5.4, 7.1, 10.3, 4.7, 6.0, 5.6, 7.3, 3.9, 5.5, N, 5.4],
        "OECD ALOS by diagnostic category", A_OECD, DIRECT, decimals=1,
        mean_2018=6.1),

    # ------------------------------------------------------------------
    # FIGURE 9. PHARMACEUTICALS (eTable 13; S2 eTable 5)
    # ------------------------------------------------------------------
    ind("f9_total", 9, None, "Total spending per capita, US $",
        "US$ per capita",
        "Total pharmaceutical spending incl. hospital, retail and OTC",
        "IMS Health (2016) or IFPMA (2014)", "2014-2016",
        [1443, 779, 667, 566, 697, 466, 939, 675, 613, 837, 560],
        "IQVIA (proprietary) / IFPMA Facts & Figures; pharma agent to "
        "determine public equivalent", A_PHARMA, UNAVAIL, decimals=0,
        bold=True, mean_2018=749),
    ind("f9_retail", 9, None, "Retail pharmaceutical spending\n"
        "per capita, US $", "US$ PPP per capita",
        "Retail pharmaceutical expenditure (HC.5.1), incl. OTC & margins, "
        "excl. hospital", "OECD.stat", "2015 or closest",
        [1026, 383, 480, 501, 541, 292, 776, 573, 587, 443, 346],
        "OECD Data Explorer, SHA HC.5.1 per capita, USD PPP", A_OECD,
        DIRECT, decimals=0, bold=True, mean_2018=541,
        notes="Figure values differ from Supplement 2 eTable 5 (e.g. "
              "UK 383 vs 485); figure values recorded."),
    ind("f9_crestor", 9, "Prices, US $ per mo", "Crestor (cholesterol)",
        "US$ per month", "Monthly manufacturer price, 30-day supply",
        "Bloomberg 2015 drug-price graphic (SSR Health / IHS)", "2015",
        [86, 26, 41, N, 20, N, N, N, 32, 29, 9],
        "Bloomberg series discontinued; pharma agent to search", A_PHARMA,
        UNAVAIL, decimals=0, mean_2018=35,
        notes="Footnote a: US discounted prices shown (list $216.00)."),
    ind("f9_lantus", 9, "Prices, US $ per mo", "Lantus (diabetes)",
        "US$ per month", "Monthly price", "Bloomberg 2015", "2015",
        [186, 64, 54, N, 47, N, N, N, 67, 64, 54],
        "Bloomberg series discontinued", A_PHARMA, UNAVAIL, decimals=0,
        mean_2018=78,
        notes="Figure shows Germany 54 (eTable 5 says 61)."),
    ind("f9_advair", 9, "Prices, US $ per mo", "Advair (asthma)",
        "US$ per month", "Monthly price", "Bloomberg 2015", "2015",
        [155, N, 38, N, 35, N, N, N, 74, 51, 29],
        "Bloomberg series discontinued", A_PHARMA, UNAVAIL, decimals=0,
        mean_2018=64),
    ind("f9_humira", 9, "Prices, US $ per mo", "Humira (rheumatoid arthritis)",
        "US$ per month", "Monthly price", "Bloomberg 2015", "2015",
        [2505, 1158, 1749, N, 982, N, N, N, 1164, 980, 1243],
        "Bloomberg series discontinued", A_PHARMA, UNAVAIL, decimals=0,
        mean_2018=1436),
    ind("f9_nce", 9, None, "New chemical entities, No.", "count",
        "New chemical entities by country of origin",
        "Daemmrich 2009, HBS working paper", "1982-2003 (cumulative)",
        [111, 16, 12, N, 11, N, 26, N, N, 18, N],
        "Pharma agent: current equivalent (e.g. EFPIA/IFPMA NCE by "
        "nationality of parent company)", A_PHARMA, UNAVAIL, decimals=0,
        bold=True, mean_2018=None,
        notes="Mean shown as NA in 2018."),
    ind("f9_fin_pub", 9, "Pharmaceutical expenditure by financing type, % "
        "of total spending", "Public spending", "% of retail pharma spending",
        "Government/compulsory schemes share of retail pharma spending",
        "OECD Health at a Glance 2015", "2011 or closest",
        [34, 66, 75, 52, 80, 65, 43, 43, 36, 71, 49],
        "OECD SHA HC.5.1 by financing scheme (HF.1)", A_OECD, DIRECT,
        decimals=0, mean_2018=56),
    ind("f9_fin_vhi", 9, "Pharmaceutical expenditure by financing type, % "
        "of total spending", "Private insurance",
        "% of retail pharma spending", "Voluntary health insurance share",
        "OECD Health at a Glance 2015", "2011 or closest",
        [36, 0, 7, 0, 1, 2, 8, 8, 30, 1, 0],
        "OECD SHA HC.5.1 by financing scheme (HF.2.1)", A_OECD, DIRECT,
        decimals=0, mean_2018=8),
    ind("f9_fin_oop", 9, "Pharmaceutical expenditure by financing type, % "
        "of total spending", "Private out-of-pocket spending",
        "% of retail pharma spending", "Household out-of-pocket share",
        "OECD Health at a Glance 2015", "2011 or closest",
        [30, 36, 18, 48, 19, 33, 51, 51, 34, 28, 50],
        "OECD SHA HC.5.1 by financing scheme (HF.3)", A_OECD, DIRECT,
        decimals=0, mean_2018=36),
    ind("f9_gen_vol", 9, "Share of generics, % of total", "Volume",
        "% of pharma market volume", "Generics share of volume",
        "OECD HaaG (p187); Japan: Cabinet Office", "2013 or closest",
        [84, 83, 80, 44, 70, 17, 54, 54, 70, 56, 30],
        "OECD Data Explorer, Pharmaceutical market (generics share)",
        A_OECD, DIRECT, decimals=0, mean_2018=58),
    ind("f9_gen_val", 9, "Share of generics, % of total", "Value",
        "% of pharma market value", "Generics share of value",
        "OECD HaaG (p187); Japan: Cabinet Office", "2013 or closest",
        [28, 33, 37, 15, 16, 16, 14, 14, 29, 33, 15],
        "OECD pharmaceutical market (generics share)", A_OECD, DIRECT,
        decimals=0, mean_2018=23),
    ind("f9_abx", 9, None, "Antibiotic prescribing, defined\ndaily doses per "
        "1000 population", "DDD per 1000 population per day",
        "Antibacterials for systemic use (ATC J01), DDD/1000/day",
        "OECD Health at a Glance 2017; US 2004", "2015 or closest",
        [24.0, 20.1, 14.4, 12.9, 29.9, 10.7, N, 16.6, 25.0, N, 28.3],
        "OECD Data Explorer, Pharmaceutical consumption (J01)", A_OECD,
        DIRECT, decimals=1, bold=True, mean_2018=20.2),

    # ------------------------------------------------------------------
    # FIGURE 10. ACCESS AND QUALITY (eTable 14; S2 eTable 6)
    # ------------------------------------------------------------------
    ind("f10_sameday", 10, "Access, %", "Able to get same- or next-\nday "
        "appointment", "% of adults",
        "Able to get same/next-day appointment when sick (excl. those who "
        "did not need care)", "Commonwealth Fund IHP Survey 2016",
        "2016", [51, 57, 53, 49, 56, 77, N, N, 43, N, 67],
        "Commonwealth Fund International Health Policy Survey (latest "
        "general-population wave)", A_CMWF, DIRECT, decimals=0,
        mean_2018=57),
    ind("f10_wait", 10, "Access, %", "2-mo Wait time to see specialist",
        "% of adults", "Waited ≥2 months for specialist appointment",
        "Commonwealth Fund IHP Survey 2016", "2016",
        [6, 19, 3, 19, 4, 7, 9, N, 39, N, 13],
        "Commonwealth Fund IHP Survey (latest general-population wave)",
        A_CMWF, DIRECT, decimals=0, mean_2018=13),
    ind("f10_time", 10, "Access, %", "Adequate time with regular\n(primary) "
        "physician", "% of patients",
        "Patients reporting enough time with regular doctor",
        "OECD.stat Health Care Quality Indicators (patient experience)",
        "2016 or closest", [81, 86, 88, 78, N, 85, 84, N, 79, N, 83],
        "OECD Data Explorer, Health care quality: patient experiences",
        A_OECD, DIRECT, decimals=0, mean_2018=83),
    ind("f10_works", 10, "Perceptions, %", "System works well",
        "% of adults", "Health system works well, only minor changes needed",
        "Commonwealth Fund IHP Survey 2016", "2016",
        [19, 44, 60, 44, 54, N, 58, N, 35, N, 44],
        "Commonwealth Fund IHP Survey (latest wave with this item)",
        A_CMWF, DIRECT, decimals=0, mean_2018=45),
    ind("f10_fund", 10, "Perceptions, %", "Fundamental changes needed",
        "% of adults", "Some good things but fundamental changes needed",
        "Commonwealth Fund IHP Survey 2016", "2016",
        [53, 46, 37, 46, 41, N, 37, N, 55, N, 46],
        "Commonwealth Fund IHP Survey", A_CMWF, DIRECT, decimals=0,
        mean_2018=45),
    ind("f10_rebuild", 10, "Perceptions, %", "Complete rebuild of health\n"
        "system needed", "% of adults", "So much wrong, needs complete "
        "rebuilding", "Commonwealth Fund IHP Survey 2016", "2016",
        [23, 7, 3, 10, 4, N, 3, N, 9, N, 4],
        "Commonwealth Fund IHP Survey", A_CMWF, DIRECT, decimals=0,
        mean_2018=8),
    ind("f10_measles", 10, "Prevention", "Measles immunization, %\nof "
        "children", "% of children", "Children immunised against measles "
        "by age 1-2", "OECD.stat", "2015 or closest",
        [92, 93, 97, 98, 91, 96, 93, 91, 90, 98, 93],
        "OECD Data Explorer, Health care quality (childhood vaccination)",
        A_OECD, DIRECT, decimals=0, mean_2018=94),
    ind("f10_mammo", 10, "Prevention", "Breast cancer screening, %\nof women "
        "aged 50-69 y", "% of women 50-69",
        "Mammography screening within past 2 years (survey or programme)",
        "OECD.stat; Sweden 40-49 y study", "2013 or closest",
        [81, 76, 71, 75, 52, 79, 47, 84, 72, 41, 55],
        "OECD Data Explorer, Health care quality (mammography screening)",
        A_OECD, DIRECT, decimals=0, mean_2018=67,
        notes="Footnote b: Sweden women 40-49 in 2018 (non-OECD source); "
              "modern update uses OECD 50-69 for Sweden if available."),
    ind("f10_stroke", 10, "Clinical outcomes", "30-d Stroke mortality per\n"
        "100 patients", "per 100 admissions (age-sex standardised)",
        "30-day mortality after admission for ischaemic stroke, age 45+",
        "OECD HCQI", "2014 or closest",
        [4.2, 9.2, 6.4, 9.6, 7.9, N, 6.9, N, 10.0, N, 9.3],
        "OECD Data Explorer, Health care quality: acute care (ischaemic "
        "stroke 30-day mortality)", A_OECD, DIRECT, decimals=1,
        mean_2018=7.9,
        notes="eTable 14 describes linked definition but 'unlinked' text; "
              "validation to pick the variant matching 2018 values."),
    ind("f10_ami", 10, "Clinical outcomes", "30-d Mortality per 1000 "
        "patients\nwith acute myocardial infarction",
        "per 100 admissions (age-sex standardised)",
        "30-day in-hospital mortality after admission for AMI, age 45+, "
        "unlinked data", "OECD HCQI", "2013 or closest",
        [5.5, 7.6, 8.7, 8.3, 7.2, N, 7.7, N, 6.7, N, 4.1],
        "OECD health care quality: acute care (AMI 30-day mortality, "
        "unlinked)", A_OECD, DIRECT, decimals=1, mean_2018=7,
        notes="Label in 2018 figure says 'per 1000' but values are per 100 "
              "(eTable 14). Label kept; error noted."),
    ind("f10_fb", 10, "Clinical outcomes", "Foreign body left per\n100 000 "
        "discharges", "per 100 000 discharges",
        "Foreign body left in during procedure", "OECD HCQI patient safety",
        "2013 or closest",
        [4.1, 6.1, 5.5, 4.6, 6.2, N, 12.3, N, 8.6, N, 8.6],
        "OECD health care quality: patient safety", A_OECD, DIRECT,
        decimals=1, mean_2018=7),
    ind("f10_obs", 10, "Clinical outcomes", "Obstetric trauma without\n"
        "instrument per 100 deliveries", "per 100 vaginal deliveries",
        "3rd/4th degree obstetric trauma, vaginal delivery without "
        "instrument", "OECD HCQI patient safety", "2013 or closest",
        [1.5, 2.8, 2.1, 2.8, 0.6, 2.5, 2.6, 2.6, 3.1, N, 2.4],
        "OECD health care quality: patient safety", A_OECD, DIRECT,
        decimals=1, mean_2018=2.3),
    ind("f10_diab", 10, "Avoidable hospitalizations",
        "Diabetes hospitalizations per\n100 000 population",
        "per 100 000 population 15+ (age-sex standardised)",
        "Diabetes hospital admissions, adults 15+",
        "OECD Health at a Glance 2015", "2013 or closest",
        [191.0, 72.8, 218.3, 96.0, 150.6, 69.8, 72.6, 113.4, 93.7, 162.3,
         141.1],
        "OECD health care quality: primary care (diabetes admissions)",
        A_OECD, DIRECT, decimals=1, mean_2018=125.6),
    ind("f10_diab_ratio", 10, "Avoidable hospitalizations",
        "Diabetes hospitalizations as a\nratio of population with diabetes",
        "admissions per 100 people with diabetes (as printed)",
        "Diabetes admissions / population with diabetes (×100 as printed)",
        "Computed; prevalence source not documented in 2018", "2013",
        [2.0, 1.7, 2.4, 1.9, 1.2, 1.2, 1.2, 1.8, 1.3, 2.8, 2.8],
        "Computed from OECD admissions and IDF Diabetes Atlas prevalence "
        "(prevalence source undocumented in 2018)", A_WB, NOTCOMP,
        decimals=2, mean_2018=2.0,
        notes="eTable 6 gives ratios as fractions (0.02); figure prints "
              "×100. 2018 does not cite the prevalence source."),
    ind("f10_asthma", 10, "Avoidable hospitalizations",
        "Asthma hospitalizations per\n100 000 population",
        "per 100 000 population 15+ (age-sex standardised)",
        "Asthma hospital admissions, adults 15+",
        "OECD Health at a Glance 2015", "2013 or closest",
        [89.7, 71.0, 28.7, 19.0, 29.6, 36.0, 27.5, 50.6, 14.6, 34.7, 64.8],
        "OECD health care quality: primary care (asthma admissions)",
        A_OECD, DIRECT, decimals=1, mean_2018=42.4),
    ind("f10_asthma_ratio", 10, "Avoidable hospitalizations",
        "Asthma hospitalizations as a\nratio of population with asthma",
        "admissions per 100 people with asthma (as printed)",
        "Asthma admissions / population with asthma (×100 as printed)",
        "Computed; prevalence source not documented in 2018", "2013",
        [1.2, 1.0, 0.7, 0.3, 0.8, 0.7, 0.4, 0.8, 0.2, 0.3, 0.6],
        "Computed from OECD admissions and a prevalence source "
        "(undocumented in 2018)", A_WB, NOTCOMP, decimals=2, mean_2018=0.7),

    # ------------------------------------------------------------------
    # FIGURE 11. DISTRIBUTION AND EQUITY (eTable 15; S2 eTable 7)
    # ------------------------------------------------------------------
    ind("f11_hi", 11, "Equity", "Horizontal inequity index, %",
        "index ×100", "Horizontal inequity index, probability of doctor "
        "visit in past 12 months by income", "OECD Health at a Glance 2013",
        "2009", [6.0, 0.4, 1.0, N, 1.3, N, N, N, 1.9, N, N],
        "No recurring OECD series; OECD agent to check later HaaG/working "
        "papers", A_OECD, UNAVAIL, decimals=2, mean_2018=2.10,
        notes="eTable 7 prints fractions (0.06); figure prints ×100."),
    ind("f11_oop_the", 11, "Out-of-pocket spending",
        "As % of total health expenditure", "% of health expenditure",
        "Out-of-pocket expenditure, % of total health expenditure",
        "World Bank SH.XPD.OOPC.TO.ZS", "2014 or closest",
        [11.0, 9.7, 13.2, 14.1, 6.3, 5.2, 26.8, 13.4, 13.6, 13.9, 18.8],
        "WHO GHED via World Bank SH.XPD.OOPC.CH.ZS (% of current health "
        "expenditure)", A_WB, CLOSE, decimals=1, mean_2018=13.3,
        notes="Denominator changed from total to current health "
              "expenditure."),
    ind("f11_oop_hh", 11, "Out-of-pocket spending",
        "As % of household consumption", "% of household final consumption",
        "OOP medical spending (excl. LTC) as share of household final "
        "consumption", "OECD Health at a Glance 2015", "2013 or closest",
        [2.6, 1.4, 1.8, 3.4, 1.4, 1.3, 4.5, 2.6, 2.3, 2.2, 3.2],
        "OECD Health at a Glance 2025 / SHA (OOP excl. LTC % household "
        "consumption)", A_OECD, DIRECT, decimals=1, mean_2018=2.4),
    ind("f11_skip", 11, "Unmet need", "Consultation skipped\nbecause of cost",
        "% of adults with a medical problem",
        "Consultation skipped due to cost", "OECD.stat (from CMWF/EHIS)",
        "2016 or closest",
        [22.3, 4.2, 2.6, 3.9, 9.0, 12.5, 7.0, N, 6.6, N, 16.2],
        "OECD Data Explorer, Health care quality: patient experiences "
        "(consultation skipped due to cost)", A_OECD, DIRECT, decimals=1,
        mean_2018=9.4),
    ind("f11_unmet_low", 11, "Unmet need", "% Unmet need, below-average\n"
        "income", "% of adults", "Any cost-related access problem, "
        "below-average income", "Commonwealth Fund IHP Survey 2016", "2016",
        [43, 8, 16, 16, 30, 29, 31, N, 30, N, 24],
        "Commonwealth Fund IHP Survey (latest general-population wave)",
        A_CMWF, DIRECT, decimals=0, mean_2018=25.2),
    ind("f11_unmet_high", 11, "Unmet need", "% Unmet need, above-average\n"
        "income", "% of adults", "Any cost-related access problem, "
        "above-average income", "Commonwealth Fund IHP Survey 2016", "2016",
        [32, 7, 6, 7, 14, 16, 22, N, 13, N, 13],
        "Commonwealth Fund IHP Survey", A_CMWF, DIRECT, decimals=0,
        mean_2018=14.4),
    ind("f11_rural", 11, "Geographic breakdown", "Rural population, % of\n"
        "total population", "% of population", "Rural population share",
        "OECD Country Statistical Profiles", "2015-2016",
        [18, 17, 18, 14, 20, 9, 26, 12, 18, 6, 10],
        "OECD Country Statistical Profiles discontinued; World Bank WDI "
        "SP.RUR.TOTL.ZS (UN WUP-based)", A_WB, CLOSE, decimals=0,
        mean_2018=15),
    ind("f11_density", 11, "Geographic breakdown", "Population density per "
        "sq mile", "persons per km² (label says sq mile)",
        "Population density", "OECD Country Statistical Profiles",
        "2015-2016", [35, 271, 237, 24, 122, 505, 212, 136, 4, 348, 3],
        "World Bank WDI EN.POP.DNST (persons per km² of land area)", A_WB,
        CLOSE, decimals=0, mean_2018=173,
        notes="2018 label says 'per sq mile' but values are per km². "
              "Modern figure keeps per km² and corrects the label."),
    ind("f11_phys_urban", 11, "Geographic breakdown", "Urban physicians per\n"
        "1000 population", "per 1000 population",
        "Physician density in urban areas", "Mixed country studies "
        "(eTable 15)", "various",
        [3.2, N, 2.0, 4.5, 4.1, N, 2.8, N, 4.1, 2.9, 2.6],
        "OECD Health at a Glance (physician density, predominantly urban "
        "vs rural TL2 regions)", A_CTRY, CLOSE, decimals=1, mean_2018=3.3),
    ind("f11_phys_rural", 11, "Geographic breakdown", "Rural physicians per\n"
        "1000 population", "per 1000 population",
        "Physician density in rural areas", "Mixed country studies "
        "(eTable 15)", "various",
        [1.4, N, 1.3, 3.5, 2.5, N, 4.4, N, 0.4, 1.4, 1.7],
        "OECD Health at a Glance (physician density, predominantly rural "
        "regions)", A_CTRY, CLOSE, decimals=1, mean_2018=2.1),
]

FOOTNOTES_2018 = {
    1: ["GDP indicates gross domestic product; NA, not applicable. CHE "
        "indicates Switzerland; NLD, the Netherlands."],
    4: ["NA indicates not applicable. CHE indicates Switzerland; NLD, the "
        "Netherlands.", "a Patient self-reported data."],
    5: ["NA indicates not applicable. CHE indicates Switzerland; NLD, the "
        "Netherlands. Generalist physicians are defined as any practicing "
        "physician registered in his or her country as a generalist "
        "physician or a specialist in the field of family medicine, "
        "pediatrics, geriatrics, or internal medicine and excludes students, "
        "interns, and nonpracticing physicians.",
        "a The number for Japan is a combined total of generalists and "
        "specialists.", "b In 2016 constant prices at 2016 US dollar "
        "purchasing power parities."],
    7: ["NA indicates not applicable. CHE indicates Switzerland; NLD, the "
        "Netherlands."],
    9: ["NA indicates not applicable. CHE indicates Switzerland; NLD, the "
        "Netherlands.", "a US discounted prices are listed.",
        "b A new chemical entity is a compound without any precedent among "
        "the regulated and approved drug products.",
        "c Volume is most often the proportion of total prescriptions that "
        "were for generic brands; value is most often the proportion of "
        "total cost.", "d Defined daily dose is the assumed mean "
        "maintenance dose per day for a drug used for its main indication "
        "in adults."],
    10: ["NA indicates not applicable. CHE indicates Switzerland; NLD, the "
         "Netherlands."],
    11: ["NA indicates not applicable. CHE indicates Switzerland; NLD, the "
         "Netherlands."],
}

# Superscript footnote marks as printed in the 2018 figures
LABEL_MARKS = {
    "f5_wage": "b", "f9_nce": "b", "f9_abx": "d",
    "f10_sameday": "a", "f10_mammo": "b", "f10_stroke": "c",
    "f10_diab": "d", "f10_diab_ratio": "e", "f10_asthma": "f",
    "f10_asthma_ratio": "g", "f11_hi": "a",
}
SECTION_MARKS = {
    (9, "Prices, US $ per mo"): "a",
    (9, "Share of generics, % of total"): "c",
    (11, "Unmet need"): "b",
}
CELL_MARKS_2018 = {
    ("f4_obese", "Sweden"): "a", ("f4_obese", "NLD"): "a",
    ("f4_obese", "CHE"): "a", ("f4_obese", "Denmark"): "a",
    ("f5_rem_gp", "Japan"): "a", ("f5_rem_sp", "Japan"): "a",
}

assert len({i["id"] for i in INDICATORS}) == len(INDICATORS)
