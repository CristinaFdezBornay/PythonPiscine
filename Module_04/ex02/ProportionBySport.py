import pandas as pd

def proportionBySport(df, year, sport, gender):
    """
    The function returns a float corresponding to the proportion (percentage) of participants who played the given sport among the participants of the given gender.
    The function answers questions like the following: "What was the percentage of female
    basketball players among all the female participants of the 2016 Olympics?"
    Returns:
    proportion: float, percentage of participants who played the given sport among participants of given gender.
    """
    proportion = 0.0
    try:
        if not isinstance(year, int):
            raise ValueError("Invalid year value. Argument year should be an int.")
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Invalid df value. Argument df should be a pandas.DataFrame object.")
        if not isinstance(sport, str):
            raise ValueError("Invalid sport value. Argument sport should be a string.")
        if not isinstance(gender, str):
            raise ValueError("Invalid gender value. Argument gender should be a string.")
        selected_year = df[df['Year'] == year]
        if len(selected_year) == 0:
            raise ValueError("No data for the provided year.")
        selected_gender = selected_year[selected_year['Sex'] == gender]
        selected_gender = selected_gender.drop_duplicates(['Name', 'Sport'])
        selected_sport = selected_gender[selected_gender['Sport'] == sport]
        proportion = len(selected_sport) / len(selected_gender)
        return proportion
    except ValueError as e:
        print("Error: {}".format(e))
        return None
