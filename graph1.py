import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'Segoe UI Emoji'
df = pd.read_csv("retail_store_inventory.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

monthly = df['Units Sold'].resample('M').mean()
monthly.index = monthly.index.strftime('%b %Y')

x = np.arange(len(monthly))
y = monthly.values

plt.figure(figsize=(12,6))

# 🔥 brighter gradient (plasma instead of viridis)
for i in range(len(x)-1):
    plt.plot(x[i:i+2], y[i:i+2],
             color=plt.cm.plasma(i/len(x)),
             linewidth=3)

# 🔥 add bright points
plt.scatter(x, y,
            c=np.linspace(0,1,len(x)),
            cmap='plasma',
            s=80,
            edgecolors='black')

# labels
plt.xticks(x, monthly.index, rotation=45)

# ❌ remove emoji (causes box)
plt.title("📈 Monthly Demand Trend Analysis 📈", fontsize=16)

plt.xlabel("Month")
plt.ylabel("Average Units Sold")

plt.grid(alpha=0.3)
plt.tight_layout()

plt.show()
