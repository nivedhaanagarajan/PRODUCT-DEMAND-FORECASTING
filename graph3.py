import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("retail_store_inventory.csv")

# Feature engineering
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Year'] = df['Date'].dt.year

# Features
X = df[['Month', 'Day', 'Year', 'Price', 'Discount']]
y = df['Units Sold']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

# Take first 10 values
actual = y_test.values[:10]
predicted = pred[:10]

x = range(len(actual))

plt.figure(figsize=(10,6))

# 🔥 Vibrant colors
plt.bar(x, actual, width=0.4, label='Actual', color='#00c2ff')      # bright blue
plt.bar([i+0.4 for i in x], predicted, width=0.4, label='Predicted', color='#ff4d6d')  # bright pink/red

# Labels
plt.xlabel("Test Samples")
plt.title("Actual vs Predicted Demand (Bar Chart)")
plt.ylabel("Units Sold")

plt.legend()
plt.tight_layout()
plt.show()
