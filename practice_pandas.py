import pandas as pd

df = pd.read_csv('YTdata.csv')

# Most popular and basic methods to explore data
(df.info())
(df.head())
(df.tail())
(df.describe())

vid_count = df['Video Count'].astype(str)

def convert_vid():
    for vid in vid_count:
        vid0 = vid.replace('videos', '').strip()
        print(vid0)


convert_vid()
# ------------
sub_count = df['Subscriber Count'].astype(str)


# Create a function with two parts for the two sets of data
def convert_subs():
    for data in sub_count:
        data0 = data.replace('subscribers', '').strip()
        if 'K' in data0:
            convert_k = data0.replace('K', '')
            print(convert_k)
        elif 'M' in data0:
            convert_m = data0.replace('M', '')
            print(convert_m)
        else:
            exit()


convert_subs()

'''date_joined0 = df['Date Joined']
print(date_joined0.str.replace('Joined', ''))
print()
print()'''
