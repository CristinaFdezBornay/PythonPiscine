class Vector(object):
    def __new__(cls, input):
        """Verify input type before creating class object"""
        if isinstance(input, tuple):
            if len(input) > 2:
                print(ValueError("""Input error: Vector initialization with range invalid.
                Please make sure your range is of size 2"""))
                return None
            elif not isinstance(input[0], int) or not isinstance(input[1], int):
                print(ValueError("""Input error: Vector initialization with range invalid.
                Please make sure range limits are of int type"""))
                return None
        elif isinstance(input, list):
            vec_type = None
            for value in input:
                if isinstance(value, list) and vec_type is None:
                    vec_type = "column"
                elif isinstance(value, float) and vec_type is None:
                    vec_type = "row"
                elif vec_type is None:
                    print(TypeError("""Input error: Invalid type.
                    Please make sure you give an array of array of floats
                    for column vectors, or array of floats for row vectors"""))
                    return None
                if not isinstance(value, list) and vec_type == "column":
                    print(TypeError("""Input error: Your vector is inconsistent. For column vector,
                    please make sure you give a list of lists of floats"""))
                    return None
                elif isinstance(value, list) and vec_type == "row":
                    print(TypeError("""Input error: Your vector is inconsistent. For row vector,
                    please make sure you give a list of floats"""))
                if vec_type == "column":
                    for val in value:
                        if not isinstance(val, float):
                            print(TypeError("""Input error: Vector values (column or row vector)
                            must be floats"""))
                            return None
        elif not isinstance(input, int):
            print(TypeError("""Input error: Please make sure your input is either a vector size
            (int), a size range (tuple) or an array"""))
            return None
        return super(Vector, cls).__new__(cls)

    def __init__(self, input):
        self.input = input
        self.values = []
        self.type = None
        try:
            if isinstance(self.input, int):
                self.values = self._get_vector_by_size()
            elif isinstance(self.input, tuple):
                self.values = self._get_vector_by_range()
            elif isinstance(self.input, list):
                self.values = self._get_row_column_vector()
            self.shape = self._get_shape()
        except Exception as exception:
            print(exception)

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
            if isinstance(value, list) and self.type is None:
                self.type = "column"
            elif isinstance(value, float) and self.type is None:
                self.type = "row"
            if self.type == "column":
                for val in value:
                    values.append([val])
            elif self.type == "row":
                values.append(value)
        return values

    def _get_shape(self):
        """Returns shape of vector depending on whether it is a column or row vector"""
        return (1, len(self.values)) if self.type == "row" else (len(self.values), 1)

    def __add__(self, other):
        """add : only vectors of same dimensions."""
        if not isinstance(other, Vector):
            print(f"""Type error: Please make sure both types are Vector instances.
            Cannot add a {type(self)} type to {type(other)} type""")
            return None
        if self.shape != other.shape:
            print(f"""Shape error: Cannot add a vector of shape {self.shape}
                      to a vector of shape {other.shape}.""")
            return None
        ret = []
        for i, _ in enumerate(self.values):
            if self.type == "column":
                ret.append([self.values[i][0] + other.values[i][0]])
            else:
                ret.append(self.values[i] + other.values[i])
        return Vector(ret)

    def __radd__(self, other):
        """add : only vectors of same dimensions."""
        return self.__add__(other)

    def __sub__(self, other):
        """sub : only vectors of same dimensions."""
        if not isinstance(other, Vector):
            print(ValueError(f"""Type error: Please make sure both types are Vector instances.
            Cannot substract a {type(self)} type to {type(other)} type"""))
            return None
        if self.shape != other.shape:
            print(ValueError(f"""Shape error: cannot add a vector of shape {self.shape}
            to a vector of shape {other.shape}"""))
            return None
        ret = []
        for i, _ in enumerate(self.values):
            if self.type == "column":
                ret.append([self.values[i][0] - other.values[i][0]])
            else:
                ret.append(self.values[i] - other.values[i])
        return Vector(ret)

    def __rsub__(self, other):
        """sub : only vectors of same dimensions."""
        self.__sub__(other)

    def __truediv__(self, other):
        """div : only scalars."""
        if not isinstance(other, int) and not isinstance(other, float):
            print(ValueError(f"""Type error: Please make sure you are dividing a Vector
            instance with a scalar value. Cannot divide a {type(self)} type to {type(other)} type"""))
            return None
        ret = []
        if other == 0 or other == 0.0:
            print(ValueError("Value error: Cannot divide vector by 0"))
            return None
        for i, _ in enumerate(self.values):
            if self.type == "column":
                ret.append([self.values[i][0] / other])
            else:
                ret.append(self.values[i] / other)
        return Vector(ret)

    def __rtruediv__(self, other):
        """div : only scalars."""
        return self.__truediv__(other)

    def __mul__(self, other):
        """mul : only scalars."""
        if not isinstance(other, int) and not isinstance(other, float):
            print(ValueError(f"""Type error: Please make sure you are multiplying a Vector
            instance with a scalar value. Cannot multiply a {type(self)} type to {type(other)} type"""))
            return None
        ret = []
        for i, _ in enumerate(self.values):
            if self.type == "column":
                ret.append([self.values[i][0] * other])
            else:
                ret.append(self.values[i] * other)
        return Vector(ret)

    def __rmul__(self, other):
        """mul : only scalars."""
        return self.__mul__(other)

    def __str__(self):
        txt = f"Vector({self.values})"
        return txt

    def __repr__(self):
        txt = f"Vector({self.values})"
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
        if not isinstance(other, Vector):
            return TypeError(f"""Type error: Please make sure argument is a Vector instance.
            Cannot perform dot product between a Vector and {type(other)}""")
        if self.shape != other.shape:
            print(ValueError(f"""Shape error: cannot dot product a vector of shape
            {self.shape} with a vector of shape {other.shape}"""))
            return None
        ret = 0
        for i, _ in enumerate(self.values):
            if self.type == "column":
                ret += self.values[i][0] * other.values[i][0]
            else:
                ret += self.values[i] * other.values[i]
        return ret
