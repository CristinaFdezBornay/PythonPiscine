class Vector(object):
    def __init__(self, input):
        self.input = input
        self.values = []
        try:
            self._verify_input()
        except Exception as e:
            print(e)
        # self.shape

    def _verify_input(self):
        column_vector = False
        row_vector = False
        self.values = []
        if type(self.input) == int:
            # Initialize vector of size self.input
            for value in range(self.input):
                self.values.append([float(value)])
        elif type(self.input) == tuple:
            if len(self.input) > 2:
                raise NameError("Input error: Vector initialization with range invalid. Please make sure your range is of size 2")
            elif type(self.input[0]) != int or type(self.input[1]) != int:
                raise NameError("Input error: Vector initialization with range invalid. Please make sure range limits are of int type")
            else:
                # Initialize vector of range self.input[0], self.input[1]
                for value in range(self.input[0], self.input[1]):
                    self.values.append([float(value)])
        elif type(self.input) == list:
            for value in self.input:
                if type(value) == list and column_vector == False and row_vector == False:
                    column_vector = True
                elif type(value) != list and column_vector == False and row_vector == False:
                    row_vector = True
                if type(value) != list and column_vector == True and row_vector == False:
                    raise NameError("Input error: Your vector is inconsistent. For column vector, please make sure you give a list of lists of floats")
                elif type(value) == list and column_vector == False and row_vector == True:
                    raise NameError("Input error: Your vector is inconsistent. For row vector, please make sure you give a list of floats")
                if type(value) == list:
                    # column vector
                    for val in value:
                        if type(val) != float:
                            raise NameError("Input error: Vector values (column or row vector ) must be floats")
                elif type(value) == float:
                    # row vector
                    
        print(self.values)

    def __add__(self):
        pass

    def __radd__(self):
        """add : only vectors of same dimensions."""
        pass

    def __sub__(self):
        pass

    def __rsub__(self):
        """sub : only vectors of same dimensions."""
        pass

    def __truediv__(self):
        pass

    def __rtruediv__(self):
        """div : only scalars."""
        pass

    def __mul__(self):
        pass

    def __rmul__(self):
        """mul : only scalars."""
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass