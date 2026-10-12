###############################################################################
# Problem Set: The Effect of Superfund Cleanups on Housing Markets
# (rough replication of Greenstone & Gallagher, 2008)
#
# Input : SuperFund_panel.csv  (tract x year panel; key = fips, year)
# Output: figures/*.png, tables/*.txt
#
# Packages: data.table, ggplot2, fixest
###############################################################################

rm(list = ls())

library(data.table)
library(ggplot2)
library(fixest)

# ---- Paths (edit if needed) -------------------------------------------------
data_path <- "SuperFund_panel.csv"
fig_dir   <- "figures"
tab_dir   <- "tables"
dir.create(fig_dir, showWarnings = FALSE)
dir.create(tab_dir, showWarnings = FALSE)

theme_set(theme_bw(base_size = 12))
pal <- c("Control" = "#1f77b4", "Treatment" = "#d62728")

save_plot <- function(p, name, w = 7, h = 4.5) {
  ggsave(file.path(fig_dir, name), p, width = w, height = h, dpi = 300)
}

raw <- fread(data_path)
raw[, V1 := NULL]


###############################################################################
# 1. Descriptive histograms
###############################################################################

# ---- 1A. Histograms of house_price for each year (raw data) ----------------
p1a <- ggplot(raw[!is.na(house_price)], aes(x = house_price)) +
  geom_histogram(bins = 60, fill = "grey40", colour = "white", linewidth = 0.1) +
  facet_wrap(~ year, scales = "free") +
  scale_x_continuous(labels = scales::label_dollar()) +
  scale_y_continuous(labels = scales::label_comma()) +
  labs(title = "House prices by census year (raw data)",
       subtitle = "Free axes per panel; 1980 axis is stretched by values up to $70 million",
       x = "Average house price (nominal $)", y = "Number of tracts") +
  theme(axis.text.x = element_text(angle = 30, hjust = 1))
save_plot(p1a, "fig1a_hist_house_price_raw.png", w = 9, h = 6)

# Log scale makes the outliers easy to see
p1a_log <- ggplot(raw[!is.na(house_price) & house_price > 0], aes(x = house_price)) +
  geom_histogram(bins = 60, fill = "grey40", colour = "white", linewidth = 0.1) +
  facet_wrap(~ year, ncol = 2) +
  scale_x_log10(labels = scales::label_dollar()) +
  labs(title = "House prices by census year (raw data, log scale)",
       subtitle = "Zeros (1980 only, n = 3,757) cannot be shown on a log axis",
       x = "Average house price (nominal $, log scale)", y = "Number of tracts")
save_plot(p1a_log, "fig1a_hist_house_price_raw_log.png", w = 9, h = 6)

# Quick look at the tails
raw[, .(n          = sum(!is.na(house_price)),
        zeros      = sum(house_price == 0, na.rm = TRUE),
        p99        = quantile(house_price, 0.99, na.rm = TRUE),
        max        = max(house_price, na.rm = TRUE),
        n_gt_250k  = sum(house_price > 250000, na.rm = TRUE)), by = year]

# ---- 1B. Outliers ----------------------------------------------------------
# Yes. 1980 is the problem year:
#  * 3,757 tracts have house_price == 0. An average house value of $0 is not
#    possible -> these are missing values coded as 0.
#  * The 1980 maximum is $70.4 million and 90 tracts are above $1 million, even
#    though the 1980 99th percentile is ~$200k, the 1970 max is ~$90k and the
#    1990 max is ~$665k. The 1980 Census top-coded owner-reported home values
#    at $200,000+ and there is a clear mass point at exactly $250,000 (the
#    value assigned to the top-coded bin), so a tract average above $250k is
#    mechanically impossible -> data errors. Many of these tracts also have
#    implausible 1980 incomes (e.g. a mean household income of $95), which
#    looks like a mis-merge / shifted columns.
#  * The 1970, 1990 and 2000 distributions look reasonable: the right tails
#    (e.g. $1.25M in 2000) are plausible for rich tracts and line up with the
#    Census top codes of the time.
#
# Other variables:
#  * In 1970 and 1980 many tracts have housing_units == 0 and income == 0 (and
#    share_black == 0, pop_den == 0). Those areas were not tracted yet in that
#    census, so these zeros are really "missing".
#  * A few tracts have income == 0 with positive housing units, and ~100 tracts
#    in 1980 have mean household income below $1,000. Both are implausible.

# ---- 1C. Data cleaning -----------------------------------------------------
d <- copy(raw)

# (i) Not-yet-tracted areas: every 0 is really "missing"
d[housing_units == 0,
  c("income", "housing_units", "share_black", "share_college",
    "pop_den", "house_price") := NA]

# (ii) House prices of 0, and 1980 averages above the $250k top-code value
d[house_price == 0, house_price := NA]
d[year == 1980 & house_price > 250000, house_price := NA]

# (iii) Mean household income of $0, or < $1,000 in 1980
d[income == 0 | (year == 1980 & income < 1000), income := NA]

# Analysis variables
d[, ln_price := log(house_price)]
d[, ln_units := log(housing_units)]
d[, has_hrs  := as.integer(!is.na(hrs_1982))]

# Histograms after cleaning
p1c <- ggplot(d[!is.na(house_price)], aes(x = house_price)) +
  geom_histogram(bins = 60, fill = "grey40", colour = "white", linewidth = 0.1) +
  facet_wrap(~ year, scales = "free") +
  scale_x_continuous(labels = scales::label_dollar()) +
  scale_y_continuous(labels = scales::label_comma()) +
  labs(title = "House prices by census year (after cleaning)",
       x = "Average house price (nominal $)", y = "Number of tracts") +
  theme(axis.text.x = element_text(angle = 30, hjust = 1))
save_plot(p1c, "fig1c_hist_house_price_clean.png", w = 9, h = 6)


###############################################################################
# 2. Cross-sectional hedonic relationship (1980)
###############################################################################

m_cs <- feols(ln_price ~ has_hrs, data = d[year == 1980], vcov = "hetero")
summary(m_cs)
etable(m_cs, file = file.path(tab_dir, "table2_cross_section.txt"), replace = TRUE)

# Result (my run): alpha = -0.143 (robust SE 0.020), N = 48,367.
#
# 2C. Interpretation: in 1980, the average census tract with a hazardous waste
# site that received an HRS score has house prices about 14.3 log points
# (exp(-0.143) - 1 = 13.3%) lower than the average tract without one.
#
# 2D. No. This is not the population-average WTP to avoid the disamenity:
#  * It isn't causal. Hazardous waste sites are not randomly placed. They are
#    in industrial, older, lower-income areas with worse housing stock and
#    other disamenities, all of which lower prices. So alpha is very likely
#    biased away from zero (omitted variable bias).
#  * Even if it were causal, the hedonic gradient shows the marginal WTP of the
#    people who actually sort into these tracts (Rosen, 1974). People with
#    low distaste for pollution (or low income) sort near the sites, so the
#    estimate understates the WTP of the average person in the population.
#  * It is a large (non-marginal) change, and it compares across different
#    housing markets nationwide, so the "single hedonic price function"
#    assumption is strained.


###############################################################################
# 3. Causal analysis
###############################################################################
#
# 3A. Controls (income, share_black, share_college): NOT included in the main
# specification. These are "bad controls": they vary over time within a tract
# and can respond to NPL listing and cleanup (people re-sort when a
# neighborhood is cleaned up or stigmatized). Conditioning on them would
# absorb part of the treatment effect and could introduce selection bias.
# The tract fixed effects already absorb all time-invariant tract
# characteristics, and the year fixed effects absorb national shocks.
# (Robustness check below shows the estimate with controls is similar.)
#
# 3B. Treatment indicator: npl_1982. NPL status in 1982 is a deterministic
# function of the 1982 HRS score (> 28.5). The cutoff was set for
# administrative reasons and the score is hard to manipulate, so it gives
# quasi-random assignment near the threshold. npl_ever also includes sites
# added to the NPL later (after re-scoring, lobbying, or new information),
# and those additions are likely correlated with local trends. So npl_ever is
# endogenous. Using npl_1982 gives an intent-to-treat estimate that is cleanly
# identified (37 of 232 below-cutoff sites were listed later; 5 above-cutoff
# sites never were).
#
# 3C. Standard errors: robust SEs clustered by county. Errors are serially
# correlated within a tract over time (need at least tract clustering, as in
# Bertrand, Duflo & Mullainathan, 2004). They are also spatially correlated
# across nearby tracts that share a local housing market (county-level
# economic shocks, assessors, school districts). Several HRS tracts share a
# county. County clustering allows for both, nests tract clustering, and is
# the more conservative choice. There are still enough clusters
# (356 counties in sample (i), 215 in sample (ii)).
#
# 3D. The event-study dummies N_c * 1{t = s} for all four years would sum to
# N_c. N_c is time-invariant, so it is perfectly collinear with the tract
# fixed effect gamma_c. One year must be dropped (normalized to 0) for the
# model to be identified. We drop 1980 because it is the last pre-treatment
# census (NPL listing happened in 1982-83). All tau_s are then measured
# relative to the period just before treatment: tau_1970 is a pre-trend
# test, and tau_1990 / tau_2000 are post-treatment effects relative to the
# 1980 baseline.

hrs   <- d[has_hrs == 1]                                        # sample (i)
hrs_b <- d[has_hrs == 1 & hrs_1982 >= 16.5 & hrs_1982 <= 40.5]  # sample (ii)

samples <- list(
  i  = list(data = hrs,   label = "Sample (i): all tracts with HRS scores"),
  ii = list(data = hrs_b, label = "Sample (ii): 1982 HRS score within 12 of cutoff (16.5-40.5)")
)

# Number of tracts / counties per sample
sapply(samples, function(s) c(tracts   = uniqueN(s$data$fips),
                               counties = uniqueN(s$data$county)))

# ---- Helper: raw means plot (3E(a)) ---------------------------------------
plot_raw_means <- function(dat, yvar, ylab, title) {
  mm <- dat[!is.na(get(yvar)),
            .(mean = mean(get(yvar)), se = sd(get(yvar)) / sqrt(.N), n = .N),
            by = .(year, group = ifelse(npl_1982 == 1, "Treatment", "Control"))]
  ggplot(mm, aes(x = year, y = mean, colour = group)) +
    geom_vline(xintercept = 1982, linetype = "dashed", colour = "grey50") +
    geom_line(linewidth = 0.8) +
    geom_point(size = 2.2) +
    scale_colour_manual(values = pal, name = NULL,
                        labels = c(Control = "Control (HRS < 28.5)",
                                   Treatment = "Treatment (HRS > 28.5, NPL 1982)")) +
    scale_x_continuous(breaks = c(1970, 1980, 1990, 2000)) +
    labs(title = title, x = "Census year", y = ylab) +
    theme(legend.position = "bottom")
}

# ---- Helper: event study (equation 3) -------------------------------------
# i(year, npl_1982, ref = 1980) creates npl_1982 x 1{year = s} for
# s in {1970, 1990, 2000}, dropping 1980.
run_es <- function(dat, yvar) {
  feols(as.formula(paste0(yvar, " ~ i(year, npl_1982, ref = 1980) | fips + year")),
        data = dat, cluster = ~county)
}

es_coefs <- function(m) {
  ct <- as.data.table(coeftable(m), keep.rownames = "term")
  ct[, year := as.integer(sub(".*::([0-9]{4}).*", "\\1", term))]
  ct <- ct[, .(year, est = Estimate, se = `Std. Error`)]
  ct <- rbind(ct, data.table(year = 1980L, est = 0, se = 0))[order(year)]
  ct[, `:=`(lo = est - 1.96 * se, hi = est + 1.96 * se)]
  ct[]
}

plot_es <- function(ct, ylab, title) {
  ggplot(ct, aes(x = year, y = est)) +
    geom_hline(yintercept = 0, colour = "grey40") +
    geom_vline(xintercept = 1982, linetype = "dashed", colour = "grey50") +
    geom_ribbon(aes(ymin = lo, ymax = hi), fill = "#d62728", alpha = 0.12) +
    geom_errorbar(aes(ymin = lo, ymax = hi), width = 1.2, colour = "#d62728") +
    geom_line(colour = "#d62728", linewidth = 0.8) +
    geom_point(size = 2.5, colour = "#d62728") +
    scale_x_continuous(breaks = c(1970, 1980, 1990, 2000)) +
    labs(title = title,
         subtitle = "NPL(1982) x year; 1980 omitted; 95% CI (county-clustered SEs)",
         x = "Census year", y = ylab)
}

# ---- 3E. Raw means and event studies for both samples ---------------------
es_models <- list()
for (k in names(samples)) {
  s <- samples[[k]]

  p_raw <- plot_raw_means(s$data, "ln_price", "Mean ln(house price)",
                          paste0("Raw means of ln(house price)\n", s$label))
  save_plot(p_raw, paste0("fig3e_raw_means_sample_", k, ".png"))

  es_models[[k]] <- run_es(s$data, "ln_price")
  ct <- es_coefs(es_models[[k]])
  print(ct)
  p_es <- plot_es(ct, "Treatment - Control, ln(house price)",
                  paste0("Event study: ln(house price)\n", s$label))
  save_plot(p_es, paste0("fig3e_event_study_sample_", k, ".png"))
}
etable(es_models$i, es_models$ii, headers = c("Sample (i)", "Sample (ii)"),
       file = file.path(tab_dir, "table3e_event_study.txt"), replace = TRUE)

# Event-study coefficients (my run; SEs clustered by county):
#                Sample (i)          Sample (ii)
#   tau_1970   -0.056 (0.048)       0.017 (0.057)
#   tau_1990    0.068 (0.050)      -0.034 (0.055)
#   tau_2000    0.018 (0.038)      -0.056 (0.045)
#
# 3F. tau_1970 is the treatment-control gap in 1970 relative to 1980, before
# anyone knew about NPL listing. In sample (i), tau_1970 = -0.056: treated
# tracts were about 5.6 log points further behind controls in 1970 than in
# 1980. So they were already on a faster price growth path before
# treatment (a pre-trend, though imprecise). In sample (ii), tau_1970 = 0.017
# is small and close to zero, so treatment and control tracts were on parallel
# paths in 1970-1980. Parallel trends, and so an unbiased tau_1990, is more
# plausible in sample (ii).
#
# 3G. Primary sample: (ii).
#  * Its pre-period coefficient is near zero, while sample (i) shows a
#    pre-existing differential trend that would bias tau_1990 upward.
#  * Close to the 28.5 cutoff, sites with scores of 25 vs 32 are very
#    similar (the HRS score is noisy, and the cutoff was chosen to produce a
#    list of ~400 sites, not based on health thresholds). So the
#    control group is a much better counterfactual, as in an RD.
#  * Sites far from the cutoff (scores near 0 or 70) differ systematically
#    in severity, location and economic trends.
#  * Cost: fewer observations (288 vs 591 tracts), so less precision. The
#    identification gain is worth it.

# ---- 3H. Difference-in-differences (equation 2), primary sample -----------
hrs_b[, post_npl := npl_1982 * (year >= 1990)]
hrs[,   post_npl := npl_1982 * (year >= 1990)]

did_main  <- feols(ln_price ~ post_npl | fips + year, data = hrs_b, cluster = ~county)
did_ctrl  <- feols(ln_price ~ post_npl + income + share_black + share_college | fips + year,
                   data = hrs_b, cluster = ~county)
did_tract <- feols(ln_price ~ post_npl | fips + year, data = hrs_b, cluster = ~fips)
did_all   <- feols(ln_price ~ post_npl | fips + year, data = hrs,   cluster = ~county)

etable(did_main, did_ctrl, did_tract, did_all,
       headers = c("Main: (ii)", "(ii) + controls", "(ii) tract cl.", "Sample (i)"),
       file = file.path(tab_dir, "table3h_did.txt"), replace = TRUE)
etable(did_main, did_ctrl, did_tract, did_all,
       headers = c("Main: (ii)", "(ii) + controls", "(ii) tract cl.", "Sample (i)"))

confint(did_main)   # 95% CI on tau

# Results (my run):
#                     tau       SE      95% CI              N
#   Main (ii)       -0.052   (0.047)  [-0.143, 0.040]     919
#   (ii) + controls -0.058   (0.036)  [-0.130, 0.013]     919
#   (ii) tract cl.  -0.052   (0.048)  [-0.146, 0.042]     919
#   Sample (i)       0.066   (0.046)  [-0.025, 0.157]    1918
#
# Interpretation: After 1982, house prices in tracts whose site was placed on
# the NPL changed by about -5.2 log points (about -5%) relative to tracts with
# sites that scored just below the cutoff, compared with the same 1980
# difference. This is not statistically different from zero (p = 0.27).
# With 95% confidence we can rule out effects larger than +4.0% (a price
# increase) or larger in magnitude than -14.3% (a price decrease). So any
# capitalization of NPL listing and cleanup into house prices bigger than
# about +4% is ruled out. This matches Greenstone & Gallagher's conclusion
# that Superfund cleanups had small (statistically zero) effects on
# local property values.

# ---- 3I. Event study with ln(housing_units) as outcome ---------------------
es_units <- run_es(hrs_b, "ln_units")
ct_units <- es_coefs(es_units)
print(ct_units)
save_plot(plot_es(ct_units, "Treatment - Control, ln(housing units)",
                  paste0("Event study: ln(housing units)\n", samples$ii$label)),
          "fig3i_event_study_housing_units.png")
save_plot(plot_raw_means(hrs_b, "ln_units", "Mean ln(housing units)",
                         paste0("Raw means of ln(housing units)\n", samples$ii$label)),
          "fig3i_raw_means_housing_units.png")
etable(es_units, file = file.path(tab_dir, "table3i_housing_units.txt"), replace = TRUE)

# Results (my run): tau_1970 = -0.055 (0.098), tau_1990 = 0.006 (0.048),
#                   tau_2000 = 0.024 (0.063). All small and insignificant.
#
# Interpretation: In the hedonic model, a change in house prices measures the
# change in WTP for the local amenity only if housing supply (and the
# population living there) doesn't respond. If cleanup led to new
# construction, the supply shift would push prices down and the price change
# would understate WTP. Here NPL listing has no detectable effect on the
# number of housing units: the coefficients are close to zero and stable over
# time. That is consistent with housing supply being fixed in the short-to-
# medium run, so a price effect (if there were one) could be read as the
# change in WTP for the local amenity. (Caveat: confidence intervals are wide
# and the 1970 coefficient is imprecise, so we cannot rule out modest supply
# responses. In sample (i) housing units do grow faster in treated tracts,
# another reason to prefer sample (ii).)
