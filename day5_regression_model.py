import pandas as pd 

# Load feature-engineered data
df = pd.read_csv("processed/TATASTEEL_FEATURES.csv")

# Convert DATE and set as index (safe practice)
df["DATE"] = pd.to_datetime(df["DATE"])
df.set_index("DATE", inplace=True)

# IMPORTANT: remove rows with NaN values
df = df.dropna()

# Select target (what to predict)
y = df["CLOSE"]

# Select features (inputs)
X = df[
    [
        "OPEN",
        "HIGH",
        "LOW",
        "VOLUME",
        "MA_7",
        "MA_14",
        "MA_30",
        "VOLATILITY"
    ]
]

print("X shape:", X.shape)
print("y shape:", y.shape)
print(X.head())

# Train–test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# Train Linear Regression model
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)
print("Model trained successfully")

from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# make predictions on test data
y_pred = model.predict(X_test)

# Evulation metrics

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print("Mean_Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)