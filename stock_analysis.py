import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read stock data
data = pd.read_csv("stock_data.csv")

# Simple Moving Average (SMA)
data['SMA'] = data['Close'].rolling(window=5).mean()

# Exponential Moving Average (EMA)
data['EMA'] = data['Close'].ewm(span=5, adjust=False).mean()

# RSI Calculation
change = data['Close'].diff()
gain = np.where(change > 0, change, 0)
loss = np.where(change < 0, -change, 0)

avg_gain = pd.Series(gain).rolling(5).mean()
avg_loss = pd.Series(loss).rolling(5).mean()

rs = avg_gain / avg_loss
data['RSI'] = 100 - (100 / (1 + rs))

# Display Output
print("\nStock Technical Indicators:\n")
print(data)

# Plot graph
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA'], label='SMA')
plt.plot(data['EMA'], label='EMA')
plt.legend()
plt.title("Stock Technical Indicator Analysis")
plt.show()