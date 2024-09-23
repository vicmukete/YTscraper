import pandas as pd

dfr = pd.read_csv('../YTdata.csv')

# Most popular and basic methods to explore data
'''(df.info())
(df.head())
(df.tail())
(df.describe())'''

sub_count0 = dfr['Subscriber Count'].astype(str)
vid_count0 = dfr['Video Count'].astype(str)
view_count0 = dfr['Views'].astype(str)
date_joined0 = dfr['Date Joined'].astype(str)


class Conversions:
    def __init__(self, df):
        self.dataframe = df

    # Video Count
    # Need it to be one column specific and separated when put into the df
    def convert_vids(self):
        filtered_vids = []
        vid_count = self.dataframe['Video Count'].astype(str)
        for vid in vid_count:
            vid = (vid.replace('videos', '').replace(',', '').strip())
            filtered_vids.append(vid)
        self.dataframe['Video Count'] = filtered_vids
        print(filtered_vids)
        return self.dataframe['Video Count']

    # View Count
    def convert_views(self):
        filtered_views = []
        view_count = self.dataframe['Views'].astype(str)
        for view in view_count:
            view = (view.replace('views', '').replace(',', '').strip())
            filtered_views.append(view)
        self.dataframe['Views'] = filtered_views
        print(filtered_views)
        return self.dataframe['Views']

    def convert_date(self):
        filtered_dates = []
        date_joined = self.dataframe['Date Joined'].astype(str)
        for date in date_joined:
            date = date.replace('Joined', '').strip()
            filtered_dates.append(date)
        self.dataframe['Date Joined'] = filtered_dates
        print(filtered_dates)
        return self.dataframe['Date Joined']

    # convert_vid()
    # ------------
    print()

    def convert_subs(self):
        filtered_sub = []
        sub_count = self.dataframe['Subscriber Count'].astype(str)
        for data in sub_count:
            data = (data.replace('subscribers', '').strip())
            if 'K' in data:
                convert_k = (data.replace('K', ',000').replace(',', '').replace('.', ''))
                filtered_sub.append(convert_k)
                self.dataframe['Subscriber Count'] = filtered_sub
                print(filtered_sub)
                return self.dataframe['Subscriber Count']
            elif 'M' in data:
                convert_m = data.replace('M', ',000,000')
                replaced_data_list = convert_m.replace('.', '').replace(',', '')
                if '.' in convert_m:
                    new_convert = (replaced_data_list[0:7])
                    filtered_sub.append(new_convert)
                    self.dataframe['Subscriber Count'] = filtered_sub
                    print(filtered_sub)
                    return self.dataframe['Subscriber Count']
                    # len_new_convert = len(replaced_data_list)
                    # print(len_new_convert, 'digits')
            else:
                continue

    # def save_conversions()

    def cleaned_csv(self, new_file='YTdata_Cleaned'):
        self.dataframe.to_csv(new_file, index=False)
        print()
        print(f'Data saved to {new_file}')


# Instantiate and process the df
converter = Conversions(dfr)

converter.convert_date()
print()
converter.convert_subs()
print()
converter.convert_vids()
print()
converter.convert_views()

converter.cleaned_csv()

