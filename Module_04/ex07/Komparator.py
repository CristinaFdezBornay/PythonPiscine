import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator():
    def __init__(self, df):
        """
        Initialize class with pandas DataFrame
        """
        self.df = df
        print("Initializing done.")

    def _error_management(self, data, categorical_var, numerical_var):
        def _test_feature(type_feature, feature):
            if not isinstance(feature, str):
                raise TypeError(f"Invalid {type_feature} feature value. Argument should be a str.")
            if feature not in data.columns:
                raise TypeError(f"Invalid {type_feature} feature. Please make sure {feature} is a valid column name.")
            feature_data = data[feature].dropna()
            if not all(isinstance(x, str if type_feature == "categorical" else float) for x in feature_data):
                raise TypeError(f"The feature {feature} should be a {type_feature} feature.")

        if not isinstance(data, pd.DataFrame):
            raise TypeError("Invalid df value. Argument df should be a pandas.DataFrame object.")
        _test_feature("categorical", categorical_var)
        _test_feature("numerical", numerical_var)

    def compare_box_plots(self, categorical_var, numerical_var):
        """
        displays a series of box plots to compare how the distribution
        of the numerical variable changes if we only consider the subpopulation
        which belongs to each category.
        There should be as many box plots as categories.
        """
        try:
            self._error_management(self.df, categorical_var, numerical_var)
            plt.style.use('ggplot')
            sns.boxplot(data=self.df, x=categorical_var, y=numerical_var )
            plt.show()

        except Exception as e:
            print("Error: {}".format(e))

    def density(self, categorical_var, numerical_var):
        """
        displays the density of the numerical variable. Each subpopulation
        should be represented by a separate curve on the graph.
        """
        try:
            self._error_management(self.df, categorical_var, numerical_var)
            plt.style.use('ggplot')
            sns.displot(data=self.df, x=numerical_var, hue=categorical_var, kind="kde", warn_singular=False)
            plt.show()

        except Exception as e:
            print("Error: {}".format(e))

    def compare_histograms(self, categorical_var, numerical_var):
        """
        plots the numerical variable in a separate histogram for each category.
        """
        try:
            self._error_management(self.df, categorical_var, numerical_var)
            plt.style.use('ggplot')
            sns.histplot(data=self.df, x=numerical_var, hue=categorical_var)
            plt.show()

        except Exception as e:
            print("Error: {}".format(e))