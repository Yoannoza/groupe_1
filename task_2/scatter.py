import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Housing.csv')

#Premières lignes du dataset
data.head()

# Histogramme
plt.figure(figsize=(8, 6))
plt.scatter(data['area'], data['price'], edgecolor='black', color='#2502d4')
plt.title('Nuage de point entre la surface et le prix', fontsize=15)
plt.xlabel('Surface (area)', fontsize=15)
plt.ylabel('Prix (price)', fontsize=15)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.show()