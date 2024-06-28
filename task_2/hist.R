library(ggplot2)

dataset <- read.csv("Housing.csv")

ggplot(dataset, aes(x = bedrooms)) +
  geom_histogram(binwidth = 1, fill = "skyblue", color = "black") +
  labs(title = "Histogramme du nombre de chambres", x = "Nombre de chambres", y = "Fréquence") +
  theme_minimal()
