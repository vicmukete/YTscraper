import pandas as pd

df = pd.read_csv('../YTdata.csv')

# Most popular and basic methods to explore data
'''(df.info())
(df.head())
(df.tail())
(df.describe())'''

sub_count0 = df['Subscriber Count'].astype(str)
vid_count0 = df['Video Count'].astype(str)
view_count0 = df['Views'].astype(str)
date_joined0 = df['Date Joined'].astype(str)


# Video Count
def convert_vid():
    vid_count = df['Video Count'].astype(str)
    for vid in vid_count:
        vid = int(vid.replace('videos', '').replace(',', '').strip())
        print(vid)


# View Count      
def convert_views():
    view_count = df['Views'].astype(str)
    for view in view_count:
        view = int(view.replace('views', '').replace(',', '').strip())
        print(view)


def convert_date():
    date_joined = df['Date Joined'].astype(str)
    for date in date_joined:
        date = date.replace('Joined', '').strip()
        print(date)


# convert_vid()
# ------------
print()


def convert_subs():
    sub_count = df['Subscriber Count'].astype(str)
    for data in sub_count:
        data = (data.replace('subscribers', '').strip())
        if 'K' in data:
            convert_k = int(data.replace('K', ',000').replace(',', '').replace('.', ''))
            print(convert_k)
        elif 'M' in data:
            convert_m = data.replace('M', ',000,000')
            replaced_data_list = convert_m.replace('.', '').replace(',', '')
            if '.' in convert_m:
                new_convert = int(replaced_data_list[0:7])
                print(new_convert)
        else:
            continue


convert_subs()
print()
convert_vid()
print()
convert_views()
print()
convert_date()

# write if statement in M's for when there's
# a period in the first 2 ch's of string
# if there is switch 3
