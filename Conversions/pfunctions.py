import pandas as pd

df = pd.read_csv('../YTdata.csv')

# Most popular and basic methods to explore data
'''(df.info())
(df.head())
(df.tail())
(df.describe())'''

sub_count = df['Subscriber Count'].astype(str)
vid_count = df['Video Count'].astype(str)
view_count = df['Views'].astype(str)
date_joined = df['Date Joined'].astype(str)


# Video Count
def convert_vid():
    for vid in vid_count:
        vid0 = vid.replace('videos', '').strip()
        int(vid0)


# View Count      
def convert_views():
    for view in view_count:
        view0 = view.replace('views', '').strip()
        int(view0)  # needs work


def convert_date():
    for date in date_joined:
        date = date.replace('joined', '').strip()
        return date


# convert_vid()
# ------------
print()


def convert_subs():
    sub_count = df['Subscriber Count'].astype(str)
    for data in sub_count:
        data = (data.replace('subscribers', '').strip())
        if 'K' in data:
            convert_k = data.replace('K', ',000')
            # print(convert_k)
        elif 'M' in data:
            convert_m = data.replace('M', ',000,000')
            replaced_data_list = convert_m.replace('.', '').replace(',', '')
            if '.' in convert_m:
                new_convert = int(replaced_data_list[0:7])
                print(new_convert)
            print(convert_m)
            print()
            # print(len(replaced_data_list))
            # print(len(convert_m))
        else:
            continue


convert_subs()

# write if statement in M's for when there's
# a period in the first 2 ch's of string
# if there is switch 3
