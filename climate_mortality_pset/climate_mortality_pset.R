library(ggplot2)
library(dplyr)
library(fixest)
library(binsreg)
library(usmap)

df <- read.csv(file.choose())   # pick climate_mortality.csv

head(df)
summary(df)
# note: the 80-90 F bin is called days_8090 in the data (the codebook says days_8089)

#### 1. Descriptive relationships ####

# 1A. average by calendar month
by_month <- df %>%
  group_by(month) %>%
  summarise(ave_temp = mean(ave_temp), drate_6599 = mean(drate_6599))

ggplot(by_month, aes(x = month, y = ave_temp)) +
  geom_line() +
  geom_point() +
  scale_x_continuous(breaks = 1:12) +
  labs(title = "Average temperature by month", y = "Average temperature (F)")

ggplot(by_month, aes(x = month, y = drate_6599)) +
  geom_line() +
  geom_point() +
  scale_x_continuous(breaks = 1:12) +
  labs(title = "Mortality rate (65+) by month", y = "Deaths per 100,000")

# 1B. average by year
by_year <- df %>%
  group_by(year) %>%
  summarise(ave_temp = mean(ave_temp), drate_6599 = mean(drate_6599))

ggplot(by_year, aes(x = year, y = ave_temp)) +
  geom_line() +
  geom_point() +
  labs(title = "Average temperature by year", y = "Average temperature (F)")

ggplot(by_year, aes(x = year, y = drate_6599)) +
  geom_line() +
  geom_point() +
  labs(title = "Mortality rate (65+) by year", y = "Deaths per 100,000")

# 1C. map of the average by state
by_state <- df %>%
  group_by(stfips) %>%
  summarise(ave_temp = mean(ave_temp), drate_6599 = mean(drate_6599)) %>%
  mutate(fips = sprintf("%02d", stfips))

plot_usmap(data = by_state, values = "ave_temp") +
  scale_fill_continuous(low = "lightyellow", high = "red", name = "Avg temp (F)") +
  labs(title = "Average temperature by state")

plot_usmap(data = by_state, values = "drate_6599") +
  scale_fill_continuous(low = "lightyellow", high = "darkred", name = "Deaths per 100k") +
  labs(title = "Mortality rate (65+) by state")

#### 2. Cross-sectional correlations ####

# 2A. binned scatterplot, no controls
binsreg(y = df$drate_6599, x = df$ave_temp)

# 2B. binned scatterplot with state and year fixed effects as controls
W <- model.matrix(~ factor(stfips) + factor(year), data = df)[, -1]
binsreg(y = df$drate_6599, x = df$ave_temp, w = W)

#### 3. Causal analysis ####

# 3A. equation (1): temperature bins + precipitation, state-by-month FE and month-of-sample FE
reg1 <- feols(ln_drate_6599 ~ days_above90 + days_8090 + days_below40 + devp25 + devp75 |
                stfips^month + year^month,
              data = df, cluster = ~stfips)
summary(reg1)
etable(reg1)

# 3D. same regression with average temperature instead of the bins
reg_avg <- feols(ln_drate_6599 ~ ave_temp + devp25 + devp75 |
                   stfips^month + year^month,
                 data = df, cluster = ~stfips)
summary(reg_avg)
etable(reg1, reg_avg)

# 3E. four sub-samples: South = climate regions 7, 8, 9
df <- df %>% mutate(south = ifelse(uscr %in% c(7, 8, 9), 1, 0))

south_early    <- df %>% filter(south == 1, year <= 1980)
south_late     <- df %>% filter(south == 1, year >= 1981)
nonsouth_early <- df %>% filter(south == 0, year <= 1980)
nonsouth_late  <- df %>% filter(south == 0, year >= 1981)

fml <- ln_drate_6599 ~ days_above90 + days_8090 + days_below40 + devp25 + devp75 |
  stfips^month + year^month

r1 <- feols(fml, data = south_early,    cluster = ~stfips)
r2 <- feols(fml, data = south_late,     cluster = ~stfips)
r3 <- feols(fml, data = nonsouth_early, cluster = ~stfips)
r4 <- feols(fml, data = nonsouth_late,  cluster = ~stfips)

etable(r1, r2, r3, r4,
       headers = c("South 1960-80", "South 1981-2004", "Non-South 1960-80", "Non-South 1981-2004"))

#### 4. Placebo test (extra credit) ####

# 4A. infectious disease death rate as the outcome
reg_ifd <- feols(drate_ifd ~ days_above90 + days_8090 + days_below40 + devp25 + devp75 |
                   stfips^month + year^month,
                 data = df, cluster = ~stfips)
summary(reg_ifd)
etable(reg_ifd)
