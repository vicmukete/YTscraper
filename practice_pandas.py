import pandas as pd

df = pd.read_csv('YTdata.csv')

# Most popular and basic methods to explore data
'''print(df.info())
print(df.head())
print(df.tail())
print(df.describe())'''

# Filtering Data
# Create a condition to filter for data

'''vid_count0 = df['Video Count']
print(vid_count0.str.replace('videos', ''))
print()
print()'''

sub_count0 = df['Subscriber Count']
sub_count1 = sub_count0.str.replace('subscribers', '')
sub_count3 = sub_count1.str.replace('M', ',000,000').str.replace('K', ',000')
print(sub_count3)
print()
print()

'''date_joined0 = df['Date Joined']
print(date_joined0.str.replace('Joined', ''))
print()
print()'''




