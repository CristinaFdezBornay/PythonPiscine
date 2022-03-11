import csv
import argparse
import numpy as np
from Kmeans import KmeansClustering

def parse_args():
    parser = argparse.ArgumentParser(description='Program to perform the Kmeans clustering algorithm.')
    parser.add_argument('filepath', type=str, help='Path to the CSV file with the dataset.')
    parser.add_argument('ncentroid', type=int, help='Number of clusters/centroids.')
    parser.add_argument('max_iter', type=int, help='Max number of iterations.')
    args = parser.parse_args()
    print(args)
    return args.filepath, args.ncentroid, args.max_iter

def get_header_and_data(filepath):
    header = ['id', 'height', 'weight', 'bone_density']
    data = np.genfromtxt(filepath, delimiter=',', dtype=[int, float, float, float], names=True)
    iterator = map(lambda x: np.array(list(x)[1:4]), data)
    return header, list(iterator)

if __name__ == '__main__':
    filepath, ncentroid, max_iter = parse_args()
    header, data = get_header_and_data(filepath)
    kmc = KmeansClustering(ncentroid, max_iter)
    kmc.fit(data)

    input("\n\n=> Press Enter to test the prediction")
    data_to_test = [[174.62647624,  78.54049084,   0.93052647], [193.78446742,  87.06534183,   0.79283106]]
    print(f"Data to test : {data_to_test}")
    prediction = kmc.predict(data_to_test)
    print(f"Prediction   : {prediction}")
