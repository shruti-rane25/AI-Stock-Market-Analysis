import pandas as pd 
# Load signal data
df = pd.read_csv("processed/TATASTEEL_SIGNALS.csv")
df["DATE"] = pd.to_datetime(df["DATE"])
df.set_index("DATE", inplace=True)
print(df[["CLOSE", "PREDICTED_CLOSE", "SIGNAL"]].head(10))

# Calculate daily market return
df["MARKET_RETURN"] = df["CLOSE"].pct_change()

# Strategy: take return only on BUY signal
df["STRATEGY_RETURN"] = df.apply(
    lambda row: row["MARKET_RETURN"] if row["SIGNAL"] == "BUY" else 0,
    axis=1
)
print(df[["CLOSE", "SIGNAL", "MARKET_RETURN", "STRATEGY_RETURN"]].head(15))


import matplotlib.pyplot as plt

# Cumulative returns
df["CUM_MARKET_RETURN"] = (1 + df["MARKET_RETURN"]).cumprod()
df["CUM_STRATEGY_RETURN"] = (1 + df["STRATEGY_RETURN"]).cumprod()

print(df[["CUM_MARKET_RETURN", "CUM_STRATEGY_RETURN"]].tail())

# Plot comparison
plt.figure()
plt.plot(df.index, df["CUM_MARKET_RETURN"], label="Market Return")
plt.plot(df.index, df["CUM_STRATEGY_RETURN"], label="AI Strategy Return")
plt.legend()
plt.title("AI Strategy vs Market Performance")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.show()

