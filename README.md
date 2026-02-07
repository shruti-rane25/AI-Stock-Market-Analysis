## Day 1 – Data Loading & Understanding

- Loaded stock market data from CSV files
- Explored the dataset using 'head()', 'info()', and 'describe()'
- Analyzed dataset shape (rows and columns)
- Understood the meaning and data type of each column
- Identified date/time columns and checked their format
- Checked for missing values and duplicate records
- Defined the objective of analysis and potential target variables
- Recorded initial observations and data quality issues

## Day 2 – Data Merging & Preparation
- Merged multiple Tata Steel CSV files into one dataset
- Sorted data by date and fixed column issues
- Created final processed dataset for analysis

## Day 3 – Data Cleaning
- Cleaned column names
- Converted DATE column
- Removed unnecessary columns
- Created cleaned dataset for AI

## Day 4 – Feature Engineering
- Created daily return feature
- Generated moving averages
- Calculated volatility
- Added volume change indicator
- Prepared dataset for ML training

## Day 5 – Regression Model
- Built Linear Regression model for next-day price prediction
- Used engineered features (MA, volatility, volume)
- Achieved MAE ≈ 0.55 and RMSE ≈ 0.72

## Day 6 – Trading Signal System
- Generated next-day price estimates using regression logic
- Converted predictions into BUY / SELL / HOLD signals
- Built explainable decision rules for trading actions

## Day 7 – Backtesting & Visualization
- Simulated AI-based trading strategy
- Compared strategy returns with market returns
- Visualized cumulative performance
