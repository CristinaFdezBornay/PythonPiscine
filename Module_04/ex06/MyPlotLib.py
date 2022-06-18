from numpy import isin
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import seaborn
import numpy as np

class MyPlotLib():
    """
    This class implements different plotting methods, each of which take two arguments
    - a pandas.DataFrame which contains the dataset
    - a list of feature names
    """

    def __init__(self):
        """
        """

    def _error_management(self, data, features):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Invalid df value. Argument df should be a pandas.DataFrame object.")
        if not isinstance(features, list):
            raise TypeError("Invalid features value. Argument features should be a list of features (str)")
        for feature in features:
            if not isinstance(feature, str):
                raise TypeError(f"Invalid feature value. Feature {feature} should be a (str)")
    
    def _select_features_histogram(self, data, features):
        selected_features = []
        for feature in features:
            if feature not in data.columns:
                raise TypeError(f"Invalid feature value {feature}. Please make sure feature list is a valid column name.")
            feature_data = data[feature].dropna()
            if not all(isinstance(x, int) for x in feature_data) and not all(isinstance(x, float) for x in feature_data):
                print(f"Cannot plot {feature} histogram, not a numerical value.")
                continue
            selected_features.append(feature)
        return selected_features

    def histogram(self, data, features):
        """
        plots one histogram for each numerical feature in the list
        """

        try:
            self._error_management(data, features)
            selected_features = self._select_features_histogram(data, features)
            if len(selected_features) == 0:
                raise Exception("None of the provided features can be plotted as an histogram.")
            fig, axes = plt.subplots(nrows=len(selected_features), ncols=1)
            for count, feature in enumerate(selected_features):
                selected_data = data[feature].dropna().sort_values()
                min = (round(selected_data.min()/10) - 1) * 10
                max = (round(selected_data.min()/10) + 1) * 10
                bin_number = max - min
                print(f"Plotting {feature} hist, with {bin_number} bins")
                plt.style.use('ggplot')
                ax = axes if len(selected_features) == 1 else axes[count]
                data.hist(column=feature, ax=ax, bins=bin_number)
            plt.show()
        except Exception as e:
            print("Error: {}".format(e))

    def density(self, data, features):
        """
        plots the density curve of each numerical feature in the list
        """
        try:
            self._error_management(data, features)
            selected_features = self._select_features_histogram(data, features)
            if len(selected_features) == 0:
                raise Exception("None of the provided features can be plotted as an histogram.")
            plt.style.use('ggplot')
            fig, axes = plt.subplots()
            for count, feature in enumerate(selected_features):
                selected_data = data[feature].dropna().sort_values()
                density = gaussian_kde(selected_data)
                xs = np.linspace(min(selected_data), max(selected_data), 200)
                density.covariance_factor = lambda : .25
                density._compute_covariance()
                plt.plot(xs, density(xs))
            plt.show()
        except Exception as e:
            print("Error: {}".format(e))

    def pair_plot(self, data, features):
        """
        plots a matrix of subplots (also called scatter plot matrix). 
        On each subplot shows a scatter plot of one numerical variable against another one. 
        The main diagonal of this matrix shows simple histograms.
        """
        try:
            self._error_management(data, features)
            selected_features = self._select_features_histogram(data, features)
            if len(selected_features) == 0:
                raise Exception("None of the provided features can be plotted as an histogram.")
            plt.style.use('ggplot')
            selected_data = data[selected_features].dropna()
            seaborn.pairplot(selected_data)
            plt.show()
        except Exception as e:
            print("Error: {}".format(e))

    def box_plot(self, data, features):
        """
        displays a box plot for each numerical variable in the dataset.
        """
        try:
            self._error_management(data, features)
            selected_features = self._select_features_histogram(data, features)
            if len(selected_features) == 0:
                raise Exception("None of the provided features can be plotted as an histogram.")
            plt.style.use('ggplot')
            selected_data = data[selected_features].dropna()
            seaborn.boxplot(data=selected_data)
            plt.show()
        except Exception as e:
            print("Error: {}".format(e))
