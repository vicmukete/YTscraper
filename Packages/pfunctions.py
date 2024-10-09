import pandas as pd

dfr = pd.read_csv('../YTdata.csv')

# Most popular and basic methods to explore data
'''(dfr.info())
(dfr.head())
(dfr.tail())
(dfr.describe())'''

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
            vid = int(vid.replace('videos', '').replace(',', '').strip())
            filtered_vids.append(vid)
        self.dataframe['Video Count'] = filtered_vids
        print(filtered_vids)
        return self.dataframe['Video Count']

    # View Count
    def convert_views(self):
        filtered_views = []
        view_count = self.dataframe['Views']
        for view in view_count:
            view = int(view.replace('views', '').replace(',', '').strip())
            filtered_views.append(view)
        self.dataframe['Views'] = filtered_views
        print(filtered_views)
        return self.dataframe['Views']

    def convert_date(self):
        filtered_dates = []
        date_joined = self.dataframe['Date Joined']
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
        sub_count = self.dataframe['Subscriber Count']
        for data in sub_count:
            data = data.replace('subscribers', '').strip()
            if 'M' in data:
                data = data.replace("M", '')
                if '.' in data:
                    # Split by '.' to handle the decimal part
                    whole, decimal = data.split('.')
                    # Ensure decimal part is up to 2 digits, then pad zeros accordingly | ljust - the method
                    # will left align the string, using a specified character (space is default) as the fill
                    # character. ljust(length (required), character (optional)) *parameters
                    decimal = decimal.ljust(2, '0')  # Add '0' to make 2 digits if needed
                    convert_m = whole + decimal + '0000'
                    filtered_sub.append(int(convert_m))
                else:
                    convert_m = data.replace('M', '000000')
                    filtered_sub.append(convert_m)
            elif 'K' in data:
                convert_k = data.replace('K', ",000").replace('.', '').replace(',', '').strip()
                filtered_sub.append(int(convert_k))
            else:
                filtered_sub.append(data)
        self.dataframe['Subscriber Count'] = filtered_sub
        print(filtered_sub)
        return self.dataframe['Subscriber Count']

    # return self.dataframe['Subscriber Count']

    def cleaned_csv(self, new_file='YTdata_Cleaned.csv'):
        self.dataframe.to_csv(new_file, index=False)
        print()
        print(f'Data saved to {new_file}')


# Instantiate and process the df
converter = Conversions(dfr)

converter.convert_subs()
print()
converter.convert_date()
print()
converter.convert_vids()
print()
converter.convert_views()

converter.cleaned_csv()
