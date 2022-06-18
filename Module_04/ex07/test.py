from Komparator import Komparator
import pandas as pd

features_to_test_correct = {
    'Correct 1': {
        'categorical': 'Sex',
        'numerical': 'Height',
    },
    'Correct 2': {
        'categorical': 'Sex',
        'numerical': 'Weight',
    },
    'Correct 3': {
        'categorical': 'NOC',
        'numerical': 'Weight',
    }
}

features_to_test_error = {
    'Error 1': {
        'categorical': None,
        'numerical': 'Height',
    },
    'Error 2': {
        'categorical': 'Sex',
        'numerical': None,
    },
    'Error 3': {
        'categorical': 'LOL',
        'numerical': 'Height',
    },
    'Error 4': {
        'categorical': 'Sex',
        'numerical': 'LOL',
    },
    'Error 5': {
        'categorical': 'Weight',
        'numerical': 'Height',
    },
    'Error 6': {
        'categorical': 'Sex',
        'numerical': 'City',
    }
}

if __name__=="__main__":
    try:
        file = '../data/athlete_events.csv'
        print(f"\n=> Loading file")
        data = pd.read_csv('../data/athlete_events.csv')

        komparator = Komparator(data)

        print(f"\n==> TESTING ERROR")
        for test in features_to_test_error.keys():
            categorical_var = features_to_test_error[test]['categorical']
            numerical_var = features_to_test_error[test]['numerical']
            print(f"\n=> Test {test}: Categorical = {categorical_var} || Numerical = {numerical_var}")
            komparator.compare_box_plots(categorical_var, numerical_var)

        print(f"\n==> TESTING COMPARE BOX PLOTS")
        for test in features_to_test_correct.keys():
            categorical_var = features_to_test_correct[test]['categorical']
            numerical_var = features_to_test_correct[test]['numerical']
            print(f"\n=> Test {test}: Categorical = {categorical_var} || Numerical = {numerical_var}")
            komparator.compare_box_plots(categorical_var, numerical_var)

        print(f"\n==> TESTING DENSITY")
        for test in features_to_test_correct.keys():
            categorical_var = features_to_test_correct[test]['categorical']
            numerical_var = features_to_test_correct[test]['numerical']
            print(f"\n=> Test {test}: Categorical = {categorical_var} || Numerical = {numerical_var}")
            komparator.density(categorical_var, numerical_var)

        print(f"\n==> TESTING COMPARE HISTOGRAMS")
        for test in features_to_test_correct.keys():
            categorical_var = features_to_test_correct[test]['categorical']
            numerical_var = features_to_test_correct[test]['numerical']
            print(f"\n=> Test {test}: Categorical = {categorical_var} || Numerical = {numerical_var}")
            komparator.compare_histograms(categorical_var, numerical_var)

    except Exception as e:
        print(e)

