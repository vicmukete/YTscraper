import pandas as pd

df = pd.read_csv('YTdata.csv')

# Most popular and basic methods to explore data
'''print(df.info())
print(df.head())
print(df.tail())
print(df.describe())'''

print(df.tail(2))


# Filtering Data
# Create a condition to filter for data

vid_count = df['Video Count']
print(vid_count.replace('videos', 'xx'))
print()
sub_count = df['Subscriber Count']
print(sub_count.replace('Subscribers', ''))
