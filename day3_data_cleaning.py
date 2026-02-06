import pandas as pd 
df = pd.read_csv("processed/TATASTEEL_2023_2026.csv")
print(df.head())
print(df.tail())

df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace(".", "")
df.columns = df.columns.str.upper()
print(df.columns)

df["DATE"] = pd.to_datetime(df["DATE"])

df.set_index("DATE", inplace=True)
print(df.head())

df.drop(["SERIES"], axis=1, inplace=True)
print(df.head())

df.to_csv("processed/TATASTEEL_CLEAN.csv")
print("DAY 3 CLEANING COMPLETED")

