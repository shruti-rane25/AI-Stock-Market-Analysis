import pandas as pd

df1 = pd.read_csv("data/raw/TATASTEEL_2023-24.csv")
df2 = pd.read_csv("data/raw/TATASTEEL_2025-26.csv")

merged = pd.concat([df1, df2], ignore_index=True)

# FIX: correct date column name
merged["DATE"] = pd.to_datetime(merged["DATE"])

# Sort by date
merged = merged.sort_values("DATE")

# Save merged file
merged.to_csv("processed/TATASTEEL_2023_2026.csv", index=False)

print("MERGE COMPLETED SUCCESSFULLY")
