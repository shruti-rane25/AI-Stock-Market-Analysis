import pandas as pd 

df = pd.read_csv("processed/TATASTEEL_CLEAN.CSV")

df["DATA"] = pd.to_datetime(df["DATE"])
df.set_index("DATA", inplace=True)
print(df.head)

df["DAILY_RETURN"] = df["CLOSE"].pct_change()
print(df[["CLOSE", "DAILY_RETURN"]].head(10))

df["MA_7"] = df["CLOSE"].rolling(window=7).mean()
df["MA_14"] = df["CLOSE"].rolling(window=14).mean()
df["MA_30"] = df["CLOSE"].rolling(window=30).mean()
print(df[["CLOSE", "MA_7", "MA_14", "MA_30"]].head(35))

df["VOLATILITY"] = df["DAILY_RETURN"].rolling(window=7).std()
print(df[["DAILY_RETURN", "VOLATILITY"]].head(15))

df["VOLUME_CHANGE"] = df["VOLUME"].pct_change()
print(df[["VOLUME", "VOLUME_CHANGE"]].head(10))

df.to_csv("processed/TATASTEEL_FEATURES.csv")
print("DAY 4 FEATURE ENGINEERING COMPLETED")

