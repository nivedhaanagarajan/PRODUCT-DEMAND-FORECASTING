import pandas as pd
import matplotlib.pyplot as plt

# 📌 Load dataset
df = pd.read_csv("retail_store_inventory.csv")

# 📌 Create price ranges
df['Price Range'] = pd.cut(df['Price'], bins=6)

# 📌 Group and sort
grouped = df.groupby('Price Range')['Units Sold'].mean().sort_values()

# 📌 Plot line graph
plt.figure(figsize=(10,6))

plt.plot(grouped.index.astype(str), grouped.values,
         marker='o',
         linewidth=2,
         color='#e74c3c')

# 📌 Add values on points
for i, val in enumerate(grouped.values):
    plt.text(i, val, round(val,1),
             ha='center', va='bottom', fontsize=9)

# 📌 Labels
plt.title("Demand Variation across Price Ranges")
plt.xlabel("Price Range")
plt.ylabel("Average Units Sold")

plt.xticks(rotation=45)
plt.grid(alpha=0.3)

plt.tight_layout()
plt.show()
