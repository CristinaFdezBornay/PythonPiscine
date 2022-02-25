from numpy import asarray

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
        array_I = 255 - array
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
        return array

    def to_grayscale(array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        This function should not raise any Exception.
        """
        return array