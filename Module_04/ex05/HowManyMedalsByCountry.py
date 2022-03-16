import pandas as pd

def howManyMedalsByCountry(df, country):
    """
    Arguments:
        - a pandas.DataFrame which contains the dataset
        - a country name.
    Returns:
        dictionary of dictionaries giving the number and type of medal
        for each competition where the country delegation earned medals
    """
    try:
        if not isinstance(country, str):
            raise TypeError("Invalid country value. Argument country should be an string.")
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Invalid df value. Argument df should be a pandas.DataFrame object.")
        medals_by_country = {}
        country_events = df[df['Team'] == country]
        country_events_by_year = country_events.groupby('Year')
        for year, event_df in country_events_by_year:
            medals_by_country[year] = {'G': 0, 'S': 0, 'B': 0}
            event_df.dropna(subset=['Medal'], inplace=True)
            medals_type_by_country = event_df.groupby('Medal')
            for medal_type, events_by_medal_type in medals_type_by_country:
                # print(medal_type)
                medal_count = len(events_by_medal_type['Event'].unique())
                if medal_type == 'Gold':
                    medals_by_country[year]['G'] = medal_count
        return medals_by_country
    except Exception as e:
        print("Error: {}".format(e))