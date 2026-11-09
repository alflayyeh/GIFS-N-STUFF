library(ggplot2)
library(dplyr)
library(fixest)

df <- read.csv(file.choose())   # pick vehicle_data.csv

head(df)
summary(df)
# note: the Tesla Model 3 shows up twice (once in the top-25 list, once in the top-10 EV list).
# I keep both rows as given; dropping one barely changes any result.

#### 1. Descriptive correlations ####

# 1A. scatterplot of price vs quantity
ggplot(df, aes(x = quantity, y = price)) +
  geom_point() +
  labs(title = "Price vs. quantity sold, 2022",
       x = "Units sold (000s)", y = "Price ($000s)")

# 1C. lifetime CO2 damages at a $190/ton social cost of carbon
df <- df %>% mutate(co2cost = co2 * 190)

df %>%
  group_by(ev) %>%
  summarise(avg_co2cost = mean(co2cost))

# 1D. histogram of CO2 damages for mass-market gasoline vehicles (non-EV, price under $50k)
mass_market <- df %>% filter(ev == 0, price < 50)

ggplot(mass_market, aes(x = co2cost)) +
  geom_histogram(bins = 10) +
  labs(title = "Lifetime CO2 damages, mass-market gasoline vehicles",
       x = "Lifetime CO2 damages ($)", y = "Number of models")

#### 2. Logit model estimation ####

Q <- 250000000   # market size

df <- df %>% mutate(share = quantity * 1000 / Q)
s0 <- 1 - sum(df$share)                     # outside option share
df <- df %>% mutate(ln_share_ratio = log(share / s0))

# 2A. equation (1) with robust standard errors
logit_reg <- feols(ln_share_ratio ~ price + weight + hp + fuel_cost + ev,
                   data = df, vcov = "hetero")
summary(logit_reg)
etable(logit_reg)

b_price <- logit_reg$coefficients["price"]

#### 3. Counterfactual policy analysis ####

# 3B. optimal tax = lifetime CO2 damages
mean(df$co2cost)

# 3C. representative utility in each scenario (price is in $000s)
# baseline V_j = ln(s_j / s_0), because the outside option has V_0 = 0
df <- df %>%
  mutate(V_B = ln_share_ratio,
         V_T = V_B + b_price * (co2cost / 1000),      # tax raises the price by co2cost
         V_S = V_B + b_price * (-7.5 * eligible))     # $7,500 credit lowers the price of eligible EVs

df %>% summarise(mean(V_B), mean(V_T), mean(V_S))

# 3D. counterfactual market shares
df <- df %>%
  mutate(s_B = exp(V_B) / (1 + sum(exp(V_B))),
         s_T = exp(V_T) / (1 + sum(exp(V_T))),
         s_S = exp(V_S) / (1 + sum(exp(V_S))))

# outside option shares in each scenario
c(baseline = 1 - sum(df$s_B), tax = 1 - sum(df$s_T), subsidy = 1 - sum(df$s_S))

# percent change in each vehicle's market share
df %>%
  mutate(pct_change_tax = 100 * (s_T / s_B - 1),
         pct_change_subsidy = 100 * (s_S / s_B - 1)) %>%
  select(make, model, ev, eligible, co2cost, pct_change_tax, pct_change_subsidy) %>%
  arrange(co2cost)

# 3E. changes in surplus, in $ per consumer per year
logsum <- function(V) log(1 + sum(exp(V)))

# consumer surplus: log-sum formula (x1000 because price is in $000s)
dCS_T <- (logsum(df$V_T) - logsum(df$V_B)) / (-b_price) * 1000
dCS_S <- (logsum(df$V_S) - logsum(df$V_B)) / (-b_price) * 1000

# producer surplus: zero, because supply is perfectly elastic
dPS_T <- 0
dPS_S <- 0

# government revenue: tax collected, or subsidy paid out
dG_T <- sum(df$s_T * df$co2cost)
dG_S <- -sum(df$s_S * 7500 * df$eligible)

# externality: change in CO2 damages
dE_T <- sum((df$s_T - df$s_B) * df$co2cost)
dE_S <- sum((df$s_S - df$s_B) * df$co2cost)

# total surplus
dTS_T <- dCS_T + dPS_T + dG_T - dE_T
dTS_S <- dCS_S + dPS_S + dG_S - dE_S

# cost per ton abated = (CS + PS + G change) / tons of CO2 abated
abated_T <- -sum((df$s_T - df$s_B) * df$co2)
abated_S <- -sum((df$s_S - df$s_B) * df$co2)
cost_per_ton_T <- (dCS_T + dPS_T + dG_T) / abated_T
cost_per_ton_S <- (dCS_S + dPS_S + dG_S) / abated_S

results <- data.frame(
  row = c("Consumer surplus change", "Producer surplus change", "Government revenue change",
          "Externality change", "Total surplus change", "Cost per ton of carbon abated"),
  tax_vs_baseline = c(dCS_T, dPS_T, dG_T, dE_T, dTS_T, cost_per_ton_T),
  subsidy_vs_baseline = c(dCS_S, dPS_S, dG_S, dE_S, dTS_S, cost_per_ton_S)
)
results

# tons of CO2 abated per consumer (negative = emissions went up)
c(tax = abated_T, subsidy = abated_S)
