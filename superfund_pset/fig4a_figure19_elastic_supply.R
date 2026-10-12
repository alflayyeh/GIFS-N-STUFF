library(ggplot2)
# Figure 19 redrawn for perfectly elastic supply (illustrative linear demand)
p0 <- 4; t1 <- 3; q0 <- 10 - p0; q1 <- 10 - (p0 + t1)
lab <- function(x, y, s, ...) annotate("text", x = x, y = y, label = s, size = 4.2, ...)
p <- ggplot() +
  annotate("rect", xmin = 0, xmax = q1, ymin = p0, ymax = p0 + t1, fill = "#1f77b4", alpha = 0.22) +
  annotate("polygon", x = c(q1, q0, q1), y = c(p0 + t1, p0, p0), fill = "#d62728", alpha = 0.25) +
  annotate("polygon", x = c(q1, q0, q0), y = c(p0 + t1, p0, p0 + t1), fill = "#2ca02c", alpha = 0.28) +
  geom_abline(intercept = 10, slope = -1, colour = "#8c1c13", linewidth = 1) +
  geom_hline(yintercept = p0, colour = "#8c1c13", linewidth = 1) +
  geom_hline(yintercept = p0 + t1, colour = "#ff7f0e", linewidth = 1, linetype = "dashed") +
  annotate("segment", x = c(q1, q0), xend = c(q1, q0), y = 0, yend = p0 + t1, linetype = "dotted") +
  annotate("point", x = c(q0, q1), y = c(p0, p0 + t1), size = 3, colour = "#1f4e9c") +
  lab(0.15, p0 + t1 + 0.3, "C", hjust = 0) + lab(0.15, p0 - 0.3, "D = E", hjust = 0) +
  lab(q1 - 0.12, p0 - 0.3, "F", hjust = 1) +
  lab(q1 - 0.12, p0 + t1 + 0.35, "B", hjust = 1) + lab(q0 + 0.12, p0 - 0.35, "A", hjust = 0) +
  lab(q0 + 0.12, p0 + t1 + 0.35, "G", hjust = 0) +
  lab(0.9, 9.6, "Demand D(p + t)", hjust = 0) +
  lab(9.1, p0 + 0.3, "Supply S(p)", hjust = 1) +
  lab(9.1, p0 + t1 + 0.3, "Social MC", hjust = 1) +
  lab(q1 / 2, p0 + t1 / 2, "Tax revenue\nBCDF") +
  lab(q1 + 0.75, p0 + 0.8, "ABF", colour = "#b22222") +
  lab(q0 - 0.75, p0 + t1 - 0.8, "ABG\n= net gain", colour = "#1e7b1e") +
  scale_x_continuous(breaks = c(q1, q0), labels = c(expression(q[1]), expression(q[0])), limits = c(0, 9.2), expand = c(0, 0)) +
  scale_y_continuous(breaks = c(p0, p0 + t1), labels = c(expression(p[0] == p[1]), expression(p[1] + t[1])), limits = c(0, 10.2), expand = c(0, 0)) +
  labs(title = "Figure 19 with perfectly elastic supply",
       subtitle = "p1 = p0: consumers bear the whole tax; PS = 0 before and after",
       x = "Quantity q", y = "Price p") +
  theme_classic(base_size = 13) + theme(axis.text = element_text(size = 13))
ggsave("/home/user/GIFS-N-STUFF/superfund_pset/figures/fig4a_fig19_elastic_supply.png", p, width = 7, height = 5, dpi = 300)
