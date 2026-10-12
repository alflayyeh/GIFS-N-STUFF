library(ggplot2)
library(dplyr)
library(fixest)

df <- read.csv(file.choose())   # pick SuperFund_panel.csv

head(df)
summary(df)

#### 1. Descriptive histograms ####

# 1A. histograms of house_price for each year
ggplot(df, aes(x = house_price)) +
  geom_histogram(bins = 50) +
  facet_wrap(~ year, scales = "free")

# 1B. look at the outliers
df %>%
  group_by(year) %>%
  summarise(zeros = sum(house_price == 0, na.rm = TRUE),
            max = max(house_price, na.rm = TRUE),
            over_250k = sum(house_price > 250000, na.rm = TRUE))

# 1C. set data errors to missing
df <- df %>%
  mutate(
    house_price = ifelse(house_price == 0, NA, house_price),
    house_price = ifelse(year == 1980 & house_price > 250000, NA, house_price),
    income = ifelse(income == 0, NA, income),
    income = ifelse(year == 1980 & income < 1000, NA, income),
    share_black = ifelse(housing_units == 0, NA, share_black),
    housing_units = ifelse(housing_units == 0, NA, housing_units),
    log_price = log(house_price),
    log_units = log(housing_units)
  )

# histograms after cleaning
ggplot(df, aes(x = house_price)) +
  geom_histogram(bins = 50) +
  facet_wrap(~ year, scales = "free")

#### 2. Cross-sectional hedonic relationship ####

cross <- df %>%
  filter(year == 1980) %>%
  mutate(has_hrs = ifelse(is.na(hrs_1982), 0, 1))

reg_cross <- feols(log_price ~ has_hrs, data = cross, vcov = "hetero")
summary(reg_cross)

#### 3. Causal analysis ####

# sample (i): all tracts with an HRS score
sample1 <- df %>% filter(!is.na(hrs_1982))

# sample (ii): HRS score within 12 of the 28.5 cutoff
sample2 <- sample1 %>% filter(hrs_1982 >= 16.5 & hrs_1982 <= 40.5)

# 3E(a). raw averages by year, treatment vs control
means1 <- sample1 %>%
  group_by(year, npl_1982) %>%
  summarise(mean_log_price = mean(log_price, na.rm = TRUE))

ggplot(means1, aes(x = year, y = mean_log_price, color = factor(npl_1982))) +
  geom_line() +
  geom_point() +
  labs(title = "Sample (i): raw averages", color = "NPL 1982")

means2 <- sample2 %>%
  group_by(year, npl_1982) %>%
  summarise(mean_log_price = mean(log_price, na.rm = TRUE))

ggplot(means2, aes(x = year, y = mean_log_price, color = factor(npl_1982))) +
  geom_line() +
  geom_point() +
  labs(title = "Sample (ii): raw averages", color = "NPL 1982")

# 3E(b). event studies (equation 3), 1980 is the omitted year
es1 <- feols(log_price ~ i(year, npl_1982, ref = 1980) | fips + year,
             data = sample1, cluster = ~county)
summary(es1)
iplot(es1, main = "Sample (i): event study")

es2 <- feols(log_price ~ i(year, npl_1982, ref = 1980) | fips + year,
             data = sample2, cluster = ~county)
summary(es2)
iplot(es2, main = "Sample (ii): event study")

# 3H. diff-in-diff (equation 2) in the primary sample (ii)
sample2 <- sample2 %>% mutate(post_npl = npl_1982 * (year >= 1990))

did <- feols(log_price ~ post_npl | fips + year, data = sample2, cluster = ~county)
summary(did)
confint(did)
etable(did)

# robustness: with controls
did_controls <- feols(log_price ~ post_npl + income + share_black + share_college | fips + year,
                      data = sample2, cluster = ~county)
etable(did, did_controls)

# 3I. event study with log(housing_units) as the outcome
es_units <- feols(log_units ~ i(year, npl_1982, ref = 1980) | fips + year,
                  data = sample2, cluster = ~county)
summary(es_units)
iplot(es_units, main = "Sample (ii): event study, log(housing units)")
