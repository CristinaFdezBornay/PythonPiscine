from MyPlotLib import MyPlotLib
import pandas as pd

data = pd.read_csv('../data/athlete_events.csv')

myplot = MyPlotLib()

# myplot.histogram(data, ['Age', 'Weight', 'City', 'Year'])
myplot.density(data, ['Age', 'Weight', 'City', 'Year'])
