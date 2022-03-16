from numpy import isin
import pandas as pd
import matplotlib.pyplot as plt
import scipy
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

    def histogram(self, data, features):
        """
        plots one histogram for each numerical feature in the list
        """
        try:
            if not isinstance(data, pd.DataFrame):
                raise TypeError("Invalid df value. Argument df should be a pandas.DataFrame object.")
            if not isinstance(features, list):
                raise TypeError("Invalid features value. Argument features should be a list of features (str)")
            selected_features = []
            for feature in features:
                if feature not in data.columns:
                    raise TypeError("Invalid feature value {}. Please make sure feature list is a valid column name.".format(feature))
                feature_data = data[feature].dropna()
                if not all(isinstance(x, int) for x in feature_data) and not all(isinstance(x, float) for x in feature_data):
                    print("Cannot plot {} histogram, not a numerical value.".format(feature))
                    continue
                selected_features.append(feature)
            fig, axes = plt.subplots(nrows=len(selected_features), ncols=1)
            count = 0
            data
            for feature in selected_features:
                if feature not in data.columns:
                    raise ValueError("Invalid features value. Are you sure the feature you are trying to plot is in the dataframe?")
                selected_data = data[feature]
                print(selected_data.unique())
                selected_data = selected_data.dropna()
                selected_data = selected_data.sort_values()
                min = (round(selected_data.min()/10) - 1) * 10
                max = (round(selected_data.min()/10) + 1) * 10
                bin_number = max - min
                print("Plotting {} hist, with {} bins".format(feature, bin_number))
                plt.style.use('ggplot')
                ax = axes if len(selected_features) == 1 else axes[count]
                data.hist(column=feature, ax=ax, bins=bin_number)
                count += 1
            plt.show()

        except Exception as e:
            print("Error: {}".format(e))

    def density(self, data, features):
        """
        plots the density curve of each numerical feature in the list
        """
        try:
            if not isinstance(data, pd.DataFrame):
                raise TypeError("Invalid df value. Argument df should be a pandas.DataFrame object.")
            if not isinstance(features, list):
                raise TypeError("Invalid features value. Argument features should be a list of features (str)")
            
            selected_features = []
            for feature in features:
                if feature not in data.columns:
                    raise TypeError("Invalid feature value {}. Please make sure feature list is a valid column name.".format(feature))
                feature_data = data[feature].dropna()
                if not all(isinstance(x, int) for x in feature_data) and not all(isinstance(x, float) for x in feature_data):
                    print("Cannot plot {} histogram, not a numerical value.".format(feature))
                    continue
                selected_features.append(feature)
            fig, axes = plt.subplots(nrows=len(selected_features), ncols=1)
            count = 0
            data
            for feature in selected_features:
                if feature not in data.columns:
                    raise ValueError("Invalid features value. Are you sure the feature you are trying to plot is in the dataframe?")
                selected_data = data[feature]
                print(selected_data.unique())
                selected_data = selected_data.dropna()
                selected_data = selected_data.sort_values()
                # min = (round(selected_data.min()/10) - 1) * 10
                # max = (round(selected_data.min()/10) + 1) * 10
                # bin_number = max - min
                print("Plotting {} density".format(feature))
                # plt.style.use('ggplot')
                # ax = axes if len(selected_features) == 1 else axes[count]
                # data.hist(column=feature, ax=ax, bins=bin_number)
                ax = selected_data.plot.kde()
                count += 1
            plt.show()

        except Exception as e:
            print("Error: {}".format(e))


    def pair_plot(self, data, features):
        """
        plots a matrix of subplots (also called scatter plot matrix). 
        On each subplot shows a scatter plot of one numerical variable against another one. 
        The main diagonal of this matrix shows simple histograms.
        """

    def box_plot(self, data, features):
        """
        displays a box plot for each numerical variable in the dataset.
        """
