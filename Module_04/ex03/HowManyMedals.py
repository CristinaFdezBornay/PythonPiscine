import pandas as pd

def howManyMedals(df, name):
    """
    The function returns a dictionary of dictionaries giving the number and type of medals
    for each year during which the participant won medals. The keys of the main dictionary are the Olympic games years. In each year's dictionary, the keys are 'G', 'S', 'B'
    corresponding to the type of medals won (gold, silver, bronze). The innermost values
    correspond to the number of medals of a given type won for a given year.
    """
    medals_dict = {}
    try:
        if not isinstance(name, str):
            raise ValueError("Invalid name value. Argument name should be a str.")
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Invalid df value. Argument df should be a pandas.DataFrame object.")
        all_games = df[df['Name'] == name]
        grouped_year = all_games.groupby('Year')
        for year, events in grouped_year:
            medals_dict[year] = {'G': 0, 'S': 0, 'B': 0}
            events.dropna(subset=['Medal'], inplace=True)
            grouped_medals = events.groupby('Medal')
            for medal, year_events in grouped_medals:
                if medal == 'Gold':
                    medals_dict[year]['G'] = len(year_events)
                elif medal == 'Silver':
                    medals_dict[year]['S'] = len(year_events)
                elif medal == 'Bronze':
                    medals_dict[year]['B'] = len(year_events)
        return medals_dict

    except ValueError as e:
        print("Error: {}".format(e))
        return None