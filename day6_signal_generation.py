import pandas as pd 
# Load feature dataset

df = pd.read_csv("processed/TATASTEEL_FEATURES.csv")
df["DATE"] = pd.to_datetime(df["DATE"])
df.set_index("DATE", inplace=True)

# Drop NaN rows (important)
df = df.dropna()
print(df[["CLOSE"]].head())

from sklearn.linear_model import LinearRegression

# Define features (same as regression)
features = [
    "OPEN",
    "HIGH",
    "LOW",
    "VOLUME",
    "MA_7",
    "MA_14",
    "MA_30",
    "VOLATILITY"
]

X = df[features]
y = df["CLOSE"]

# Train regression model
model = LinearRegression()
model.fit(X, y)

# Predict next-day price
df["PREDICTED_CLOSE"] = model.predict(X)
print(df[["CLOSE", "PREDICTED_CLOSE"]].head())

# calculate expected percentage change
df["EXPECTED_RETURN"] = (df["PREDICTED_CLOSE"] - df["CLOSE"]) / df["CLOSE"]

# generate signals 
def generate_signals(x):
    if x > 0.005:
        return "BUY"
    elif x < -0.005:
        return "SELL"
    else:
        return "HOLD"

df["SIGNAL"] = df["EXPECTED_RETURN"].apply(generate_signals)
print(df[["CLOSE", "PREDICTED_CLOSE", "EXPECTED_RETURN", "SIGNAL"]].head(10))

# Save final signals dataset
df.to_csv("processed/TATASTEEL_SIGNALS.csv")
print("DAY 6 SIGNAL GENERATION COMPLETED")
