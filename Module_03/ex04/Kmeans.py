import pickle
import random
import numpy as np

MIN_CENTROID_ITER_DIFF = 0.005

class KmeansClustering:
    def __init__(self, ncentroid=4, max_iter=20):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []
        self.centroids_iter_diff = MIN_CENTROID_ITER_DIFF
        self.distances = np.zeros(ncentroid)

    def _distanceL1(self, x1, x2):
        return sum(abs(x1-x2))

    def _append_x_to_data_per_centroid(self, centroid_index, x):
        if centroid_index in self.data_per_centroid.keys():
            self.data_per_centroid[centroid_index].append(x)
        else:
            self.data_per_centroid[centroid_index] = [x]

    def _recalculate_centroid_position(self):
        print(len(self.centroids))
        print(len(self.data_per_centroid))
        new_centroids = np.zeros((self.ncentroid, len(self.centroids)))
        for i, centroid in enumerate(self.centroids):
            features_per_centroid = np.array(self.data_per_centroid[i])
            print(sum(features_per_centroid))
            print(len(features_per_centroid))
            print(sum(features_per_centroid) / len(features_per_centroid))
            new_centroids[i] = sum(features_per_centroid) / len(features_per_centroid)
        self.centroids_iter_diff = self._distanceL1(self.centroids, new_centroids)
        self.centroids = new_centroids

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
        self.centroids = random.choices(data, k=self.ncentroid)
        for _ in range(self.max_iter):
            if self.centroids_iter_diff < MIN_CENTROID_ITER_DIFF:
                return
            self.data_per_centroid = dict()
            for x in data:
                for i, centroid in enumerate(self.centroids):
                    self.distances[i] = self._distanceL1(centroid, x)
                centroid_index = np.where(self.distances == min(self.distances))[0][0]
                self._append_x_to_data_per_centroid(centroid_index, x)
            self._recalculate_centroid_position()
            input("=>")
        return

    def save_model(self):
        model = {
            "ncentroid": self.ncentroid,
            "max_iter": self.max_iter,
            "centroids": self.centroids,
        }
        with open('model.pickle', 'wb') as save_model_file:
            pickle.dump(model, save_model_file)

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
            data: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
            The prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
            This function should not raise any Exception.
        """
        return X
