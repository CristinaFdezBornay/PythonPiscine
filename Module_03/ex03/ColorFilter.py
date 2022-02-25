import numpy as np

class ColorFilter():
    def invert(array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        array_I = 1 - array[:,:,0:3]
        return array_I

    def to_blue(array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        array_B = array.copy()
        array_B[:, :, (0, 1)] = 0
        return array_B

    def to_green(array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        array_G = array.copy()
        array_G[:, :, (0, 2)] = 0
        return array_G

    def to_red(array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        array_R = array.copy()
        array_R[:, :, (1, 2)] = 0
        return array_R

    def to_celluloid(array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        array: numpy.ndarray corresponding to the image.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        # threshold = 4
        # array_C = (((array  * threshold).astype(np.int32)).astype(np.float) / threshold)
        array_C = array
        return array_C

    def to_grayscale(array, filter, weights=None):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        if filter not in ['m', 'mean', 'w', 'weight']:
            raise(ValueError("Argument filter should be 'mean' or 'weight'"))
        if filter in ['w', 'weight'] and (weights == None or sum(weights) != 1):
            raise(ValueError("Weights should be a list of 3 floats and the sum(weights) == 1"))
        if filter in ['m', 'mean']:
            weights = [1/3, 1/3, 1/3]

        weights = [weights[0], weights[1], weights[2], 0.0]
        array_G = array * weights
        array_G = array_G.sum(axis = 2)
        return array_G
