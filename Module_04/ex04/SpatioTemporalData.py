import pandas as pd

class SpatioTemporalData():
    def __init__(self, df):
        """
        Initialize class with pandas DataFrame
        """
        self.df = df
        print("Initializing done.")

    def when(self, location):
        """
        takes a location as an argument (string, city)
        returns a list containing the years where games were held in the given location
        """
        try:
            if not isinstance(self.df, pd.DataFrame):
                raise TypeError("Invalid Data. Please make sure you instantiate the class with a valid pandas DataFrame object.")
            elif not isinstance(location, str):
                raise TypeError("Invalid location value. Argument location should be a str.")
            location_events = self.df[self.df['City'] == location]
            grouped_by_year = location_events.groupby('Year')
            years = list(grouped_by_year.groups.keys())
            return years

        except Exception as e:
            print("Error: {}".format(e))
            return None

    def where(self, date):
        """
        takes a date as an argument : date = year (int) 
        returns list of the location where the Olympics took place in the given year
        """
        try:
            if not isinstance(self.df, pd.DataFrame):
                raise TypeError("Invalid Data. Please make sure you instantiate the class with a valid pandas DataFrame object.")
            elif not isinstance(date, int):
                raise TypeError("Invalid date value. Argument date should be an int.")
            year_events = self.df[self.df['Year'] == date]
            grouped_by_city = year_events.groupby('City')
            city = list(grouped_by_city.groups.keys())
            return city

        except Exception as e:
            print("Error: {}".format(e))
            return None
