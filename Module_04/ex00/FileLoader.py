import pandas as pd

class FileLoader():
    def __init__(self):
        self.init = True

    def load(self, path):
        """
        Takes as an argument the file path of the dataset to load, displays a
        message specifying the dimensions of the dataset (e.g. 340 x 500) and returns the
        dataset loaded as a pandas.DataFrame
        """
        try:
            df = pd.read_csv(path)
            print("Loading dataset of dimensions {} x {}".format(len(df.index), len(df.columns)))
            return df
        except Exception as e:
            print("Could not read file located at '{}'. Please make sure it is a valid csv file.".format(path))
            return None

    def display(self, df, n):
        """
        Takes a pandas.DataFrame and an integer as arguments, displays
        the first n rows of the dataset if n is positive, or the last n rows if n is negative
        """
        try:
            if type(n) != int:
                raise TypeError('Argument n must be an integer.')
            elif not isinstance(df, pd.DataFrame):
                raise TypeError('Argument df must be a pandas DataFrame.')
            if n >= 0:
                print(df.head(n))
            else:
                print(df.tail(-n))
        except TypeError as e:
            print("Error: {}".format(e))
            return
