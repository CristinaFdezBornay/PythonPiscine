class Vector(object):
    def __new__(cls, input):
        """Verify input type before creating class object"""
        if type(input) == tuple:
            if len(input) > 2:
                print(ValueError("Input error: Vector initialization with range invalid. Please make sure your range is of size 2"))
                return None
            elif type(input[0]) != int or type(input[1]) != int:
                print(ValueError("Input error: Vector initialization with range invalid. Please make sure range limits are of int type"))
                return None 
        elif type(input) == list:
            vec_type = None
            for value in input:
                if type(value) == list and vec_type == None:
                    vec_type = "column"
                elif type(value) == float and vec_type == None:
                    vec_type = "row"
                elif vec_type == None:
                    print(TypeError("Input error: Invalid type. Please make sure you give an array of array of floats for column vectors, or array of floats for row vectors"))
                    return None
                if type(value) != list and vec_type == "column":
                    print(TypeError("Input error: Your vector is inconsistent. For column vector, please make sure you give a list of lists of floats"))
                    return None
                elif type(value) == list and vec_type == "row":
                    print(TypeError("Input error: Your vector is inconsistent. For row vector, please make sure you give a list of floats"))
                if vec_type == "column":
                    # column vector
                    for val in value:
                        if type(val) != float:
                            print(TypeError("Input error: Vector values (column or row vector ) must be floats"))
                            return None
        elif type(input) != int:
            print(TypeError("Input error: Please make sure your input is either a vector size (int), a size range (tuple) or an array"))
            return None
        return super(Vector, cls).__new__(cls)

    def __init__(self, input):
        self.input = input
        self.values = []
        self.type = None
        try:
            if type(self.input) == int:
                self.values = self._get_vector_by_size()
            elif type(self.input) == tuple:
                self.values = self._get_vector_by_range()
            elif type(self.input) == list:
                self.values = self._get_row_column_vector()
            self.shape = self._get_shape()
        except Exception as e:
            print(e)

    def _get_vector_by_size(self):
        """Initialize vector of size input"""
        values = []
        for value in range(self.input):
            values.append([float(value)])
        self.type = "column"
        return values

    def _get_vector_by_range(self):
        """Initialize vector from range"""
        values = []
        for value in range(self.input[0], self.input[1]):
            values.append([float(value)])
        self.type = "column"
        return values

    def _get_row_column_vector(self):
        """Initialize either row (array of floats) or column vector (array of array of floats)"""
        values = []
        for value in self.input:
            if type(value) == list and self.type == None:
                self.type = "column"
            elif type(value) == float and self.type == None:
                self.type = "row"
            if self.type == "column":
                for val in value:
                    values.append([val])
            elif self.type == "row":
                values.append(value)
        return values

    def _get_shape(self):
        """Returns shape of vector depending on whether it is a column or row vector"""
        if self.type == "row":
            shape = (1, len(self.values))
        else:
            shape = (len(self.values), 1)
        return shape

    def __add__(self, other):
        """add : only vectors of same dimensions."""
        if isinstance(other, Vector):
            if self.shape != other.shape:
                print("Shape error: Cannot add a vector of shape {} to a vector of shape {}".format(self.shape, other.shape))
            else:
                ret = []
                for i in range(len(self.values)):
                    if self.type == "column":
                        ret.append([self.values[i][0] + other.values[i][0]])
                    else:
                        ret.append(self.values[i] + other.values[i])
                return Vector(ret)
        else:
            print("Type error: Please make sure both types are Vector instances. Cannot add a {} type to {} type".format(type(self), type(other)))

    def __radd__(self, other):
        """add : only vectors of same dimensions."""
        return self.__add__(other)

    def __sub__(self, other):
        """sub : only vectors of same dimensions."""
        if isinstance(other, Vector):
            if self.shape != other.shape:
                print(ValueError("Shape error: cannot add a vector of shape {} to a vector of shape {}".format(self.shape, other.shape)))
                return None
            else:
                ret = []
                for i in range(len(self.values)):
                    if self.type == "column":
                        ret.append([self.values[i][0] - other.values[i][0]])
                    else:
                        ret.append(self.values[i] - other.values[i])
                return Vector(ret)
        else:
            print(ValueError("Type error: Please make sure both types are Vector instances. Cannot substract a {} type to {} type".format(type(self), type(other))))
            return None

    def __rsub__(self, other):
        """sub : only vectors of same dimensions."""
        self.__sub__(other)

    def __truediv__(self, other):
        """div : only scalars."""
        if isinstance(other, int) or isinstance(other, float):
            ret = []
            if other == 0 or other == 0.0:
                print(ValueError("Value error: Cannot divide vector by 0"))
                return None
            for i in range(len(self.values)):
                if self.type == "column":
                    ret.append([self.values[i][0] / other])
                else:
                    ret.append(self.values[i] / other)
            return Vector(ret)
        else:
            print(ValueError("Type error: Please make sure you are dividing a Vector instance with a scalar value. Cannot divide a {} type to {} type".format(type(self), type(other))))
            return None

    def __rtruediv__(self, other):
        """div : only scalars."""
        return self.__truediv__(other)

    def __mul__(self, other):
        """mul : only scalars."""
        if isinstance(other, int) or isinstance(other, float):
            ret = []
            for i in range(len(self.values)):
                if self.type == "column":
                    ret.append([self.values[i][0] * other])
                else:
                    ret.append(self.values[i] * other)
            return Vector(ret)
        else:
            print(ValueError("Type error: Please make sure you are multiplying a Vector instance with a scalar value. Cannot multiply a {} type to {} type".format(type(self), type(other))))
            return None

    def __rmul__(self, other):
        """mul : only scalars."""
        return self.__mul__(other)

    def __str__(self):
        txt = """Vector({})""".format(self.values)
        return txt

    def __repr__(self):
        txt = """Vector({})""".format(self.values)
        return txt

    def T(self):
        """Transpose vector"""
        values = []
        if self.type == "column":
            for val in self.values:
                values.append(val[0])
        else:
            for val in self.values:
                values.append([val])
        return Vector(values)

    def dot(self, other):
        """Performs dot product between two vectors of same shape. Returns scalar"""
        if isinstance(other, Vector):
            if self.shape != other.shape:
                print(ValueError("Shape error: cannot dot product a vector of shape {} with a vector of shape {}".format(self.shape, other.shape)))
                return None
            else:
                ret = 0
                for i in range(len(self.values)):
                    if self.type == "column":
                        ret += self.values[i][0] * other.values[i][0]
                    else:
                        ret += self.values[i] * other.values[i]
                return ret
        else:
            return TypeError("Type error: Please make sure argument is a Vector instance. Cannot perform dot product between a Vector and {}".format(type(other)))
