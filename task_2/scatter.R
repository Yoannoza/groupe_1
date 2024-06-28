library(ggplot2)

dataset <- read.csv("Housing.csv")

ggplot(dataset, aes(x = area, y = price)) +
  geom_point(alpha = 0.5) +
  labs(title = "Graphique de dispersion entre la surface et le prix", x = "Surface (area)", y = "Prix (price)") +
  theme_minimal()