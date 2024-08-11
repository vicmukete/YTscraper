import pandas as pd

df = pd.read_csv('YT Data.csv')

# Most popular and basic methods to explore data
print(df.info())
print(df.head(6))
print(df.tail(6))
print(df.describe())

# Filtering Data
# Create a condition to filter for data
