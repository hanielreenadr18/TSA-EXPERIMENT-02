import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
temperature = [
    25, 27, 29, 32, 34, 33,
    32, 31, 30, 29, 27, 25,
    25, 27, 29, 32, 34, 33,
    32, 31, 30, 29, 27, 25
]
dates = pd.date_range(
    start="2025-01-01",
    periods=24,
    freq="ME"
)
data = pd.Series(
    temperature,
    index=dates
)
print("Monthly Temperature:")
print(data)
plt.figure(figsize=(10, 5))
plt.plot(data.index, data.values, marker="o")
plt.title("Monthly Average Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()
result = seasonal_decompose(
    data,
    model="additive",
    period=12
)
result.plot()
plt.show()
