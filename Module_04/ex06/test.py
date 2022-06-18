from MyPlotLib import MyPlotLib
import pandas as pd

features_to_test = [
    ['Age'],
    ['Age', 'Weight'],
    ['Age', 'Weight', 'City', 'Year'],
    ['Age', 'Weight', 'LOOL', 'Year'],
    ['Age', 'Weight', None, 'Year'],
    None
]

if __name__=="__main__":
    try:
        file = '../data/athlete_events.csv'
        print(f"\n=> Loading file")
        data = pd.read_csv('../data/athlete_events.csv')

        myplot = MyPlotLib()

        print(f"\n==> TESTING HISTOGRAM")
        for test in features_to_test:
            print(f"\n=> Test :{test}")
            myplot.histogram(data, test)

        print(f"\n==> TESTING DENSITY")
        for test in features_to_test:
            print(f"\n=> Test :{test}")
            myplot.density(data, test)

        print(f"\n==> TESTING PAIR PLOT")
        for test in features_to_test:
            print(f"\n=> Test :{test}")
            myplot.pair_plot(data, test)

        print(f"\n==> TESTING BOX PLOT")
        for test in features_to_test:
            print(f"\n=> Test :{test}")
            myplot.box_plot(data, test)

    except Exception as e:
        print(e)

