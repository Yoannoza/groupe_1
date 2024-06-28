import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Housing.csv')

#Premières lignes du dataset
data.head()

# Histogramme
plt.figure(figsize=(8, 6))
plt.hist(data['bedrooms'], edgecolor='black', color='#2502d4')
plt.title('Histogramme des chambres', fontsize=15)
plt.xlabel('Nombre de chambres', fontsize=15)
plt.ylabel('Fréquence', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.show()