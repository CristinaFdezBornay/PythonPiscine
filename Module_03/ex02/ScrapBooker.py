import numpy as np

class ScrapBooker():
    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width oof the image) from the coordinates given by position arguments.
        Args:
          array: numpy.ndarray
          dim: tuple of 2 integers.
          position: tuple of 2 integers.
        Returns:
          new_arr: the cropped numpy.ndarray.
          None otherwise (combination of parameters not incompatible).
        Raises:
          This function should not raise any Exception.
        """
        try:
            x_dim, y_dim = dim
            x_pos, y_pos = position
            return array[x_pos:(x_pos+x_dim), y_pos:(y_pos+y_dim)]
        except Exception as e:
            print("[ERROR] ", e)
            return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: vertical, 1: horizontal)
        Args:
          array: numpy.ndarray.
          n: non null positive integer lower than the number of row/column of the array
             (depending of axis value).
          axis: positive non null integer.
        Returns:
          new_arr: thined numpy.ndarray.
          None otherwise (combination of parameters not incompatible).
        Raises:
          This function should not raise any Exception.
        """
        try:
            x_shape, y_shape = array.shape
            indices = list(range(n - 1, x_shape if axis == 0 else y_shape, n))
            return np.delete(array, indices, axis)
        except Exception as e:
            print("[ERROR] ", e)
            return None

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
          array: numpy.ndarray.
          n: positive non null integer.
          axis: integer of value 0 or 1.
        Returns:
          new_arr: juxtaposed numpy.ndarray.
          None otherwise (combination of parameters not incompatible).
        Raises:
          This function should not raise any Exception.
        """
        try:
          if n < 1:
              raise(ValueError)
          out = array
          for i in range(1, n):
            out = np.append(out, array, axis)
          return out
        except Exception as e:
            print("[ERROR] ", e)
            return None

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
          array: numpy.ndarray.
          dim: tuple of 2 integers.
        Returns:
          new_arr: mosaic numpy.ndarray.
          None otherwise (combination of parameters not incompatible).
        Raises:
          This function should not raise any Exception.
        """
        try:
          if dim[0] < 1 or dim[1] < 1:
              raise(ValueError)
          out = self.juxtapose(array, dim[0], 0)
          return self.juxtapose(out, dim[1], 1)
        except Exception as e:
            print("[ERROR] ", e)
            return None
