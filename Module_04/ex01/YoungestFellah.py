import pandas as pd

def youngestFellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
    df: pandas.DataFrame object containing the dataset.
    year: integer corresponding to a year.
    Returns:
    youngest_dict: dictionary with 2 keys for female and male athlete.
    """
    youngest_dict = {'f': 'nan', 'm': 'nan'}
    try:
        if not isinstance(year, int):
            raise ValueError("Invalid year value. Argument year should be an int.")
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Invalid df value. Argument df should be a pandas.DataFrame object.")
        selected_year = df[df['Year'] == year]
        if len(selected_year) == 0:
            raise ValueError("No data for the provided year.")
        female_athletes = selected_year[selected_year['Sex'] == 'F']
        male_athletes = selected_year[selected_year['Sex'] == 'M']
        youngest_dict['f'] = female_athletes.min()['Age']
        youngest_dict['m'] = male_athletes.min()['Age']
    except ValueError as e:
        print("Error: {}".format(e))
    return youngest_dict