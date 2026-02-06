import pandas as pd
import numpy as np

df1 = pd.read_csv("TATASTEEL_2023-24.csv")
df2= pd.read_csv("TATASTEEL_2025-26.csv")

print(df1.head())
print(df2.head())

print(df1.tail())
print(df2.tail())

print(df1.info())
print(df2.info())

print(df1.describe())
print(df2.describe())

print("Missing values:\n", df1.isnull().sum())
print("Missing values:\n", df2.isnull().sum())

print("Data types:\n", df1.dtypes)
print("Data types:\n",df2.dtypes )

print("Shape:", df1.shape)
print("Shape:", df2.shape)

print("\n--- DATA INFO ---")
print("\n--- DATA INFO ---")

print(df1.info())
print(df2.info())
