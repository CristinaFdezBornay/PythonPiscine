import pickle
import random
import numpy as np
import matplotlib.pyplot as plt

PICKLE_FILENAME = 'model.pickle'

class KmeansClustering:
    def __init__(self, ncentroid=4, max_iter=20):
        self.ncentroid = ncentroid
        self.max_iter = max_iter

    def _distanceL1(self, x1, x2):
        return sum(abs(x1-x2))

    def _get_cluster_for_x(self, centroids, x):
        distances = np.zeros(self.ncentroid)
        for i, centroid in enumerate(centroids):
            distances[i] = self._distanceL1(centroid, x)
        cluster_for_x = np.where(distances == min(distances))[0][0]
        return cluster_for_x

    def _append_x_to_dictionary(self, dictionary, i, x):
        if i in dictionary.keys():
            dictionary[i].append(x)
        else:
            dictionary[i] = [x]
        return dictionary

    def _recalculate_centroids(self, data_per_cluster, centroids):
        for i in data_per_cluster.keys():
            features_per_centroid = np.array(data_per_cluster[i])
            centroids[i] = sum(features_per_centroid) / len(features_per_centroid)
        return centroids

    def _get_cluster_dispersion(self, data_per_cluster, centroids):
        dispersion = dict()
        for i in data_per_cluster.keys():
            distances = []
            for x in data_per_cluster[i]:
                distances.append(self._distanceL1(x, centroids[i]))
            avg_distance = round(sum(distances) / len(distances), 2)
            dispersion = self._append_x_to_dictionary(dispersion, i, avg_distance)
        return dispersion

    def _save_model(self, data_per_cluster, centroids, dispersion):
        model = {
            "ncentroid": self.ncentroid,
            "max_iter": self.max_iter,
            "centroids": centroids,
            "dispersion": dispersion,
            "data_per_cluster": data_per_cluster,
        }
        with open(PICKLE_FILENAME, 'wb') as save_model_file:
            pickle.dump(model, save_model_file)

    def _print_model(self, data_per_cluster, centroids, random_centroids, dispersion):
        print(f"Number of clusters       : {self.ncentroid}")
        print(f"Max number of iterations : {self.max_iter}")
        print("Random initialization")
        for i in range(self.ncentroid):
            print(f"Centroid [{i}] => {random_centroids[i]}")
        print("\nFinal Model Centroids")
        for i in range(self.ncentroid):
            print(f"Centroid [{i}] => {centroids[i]} || Number of datapoints : {len(data_per_cluster[i])} || Dispersion : {dispersion[i][0]}")

    def fit(self, data):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
            data: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            None.
        Raises:
            This function should not raise any Exception.
        """
        random_centroids = random.choices(data, k=self.ncentroid)
        centroids = random_centroids.copy()
        for _ in range(self.max_iter):
            data_per_cluster = dict()
            for x in data:
                cluster_for_x = self._get_cluster_for_x(centroids, x)
                data_per_cluster = self._append_x_to_dictionary(data_per_cluster, cluster_for_x, x)
            centroids = self._recalculate_centroids(data_per_cluster, centroids)
        dispersion = self._get_cluster_dispersion(data_per_cluster, centroids)
        self._save_model(data_per_cluster, centroids, dispersion)
        self._print_model(data_per_cluster, centroids, random_centroids, dispersion)

    def predict(self, data):
        """
        Predict from which cluster each datapoint belongs to.
        Args:
            data: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            The prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        prediction = []
        with open(PICKLE_FILENAME, 'rb') as read_model_file:
            model = pickle.load(read_model_file)
        for x in data:
            cluster_for_x = self._get_cluster_for_x(model['centroids'], x)
            prediction.append(cluster_for_x)
        return np.array(prediction)
