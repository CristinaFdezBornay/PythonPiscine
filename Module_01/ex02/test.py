from vector import Vector

def main():
    # Example 1:
    print("Initializing column vector with values [[0.0], [1.0], [2.0], [3.0]]")
    v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v1.shape: "), v1.shape) # should be (4,1)
    print("{0: <20}".format("v1.T()"), v1.T()) # Output: Vector([0.0, 1.0, 2.0, 3.0])
    print("{0: <20}".format("v1.T().shape"), v1.T().shape) # Output: (1,4)
    input("\n================================================ Press ENTER to continue ==>")

    # Example 2:
    print("\nInitializing row vector with values [0.0, 1.0, 2.0, 3.0]")
    v2 = Vector([0.0, 1.0, 2.0, 3.0])
    print("{0: <20}".format("v2: "), v2)
    print("{0: <20}".format("v2.shape: "), v2.shape) # should be (1,4)
    print("{0: <20}".format("v2.T(): "), v2.T()) # Output: Vector([[0.0], [1.0], [2.0], [3.0]])
    print("{0: <20}".format("v2.T().shape"), v2.T().shape) # Output: (4,1)
    input("\n================================================ Press ENTER to continue ==>")

    # Example 3:
    print("\nInitializing column vector with size 10")
    v3 = Vector(10)
    print("{0: <20}".format("v3: "), v3)
    print("{0: <20}".format("v3.shape: "), v3.shape)
    print("{0: <20}".format("v3.T(): "), v3.T())
    print("{0: <20}".format("v3.T().shape"), v3.T().shape)
    input("\n================================================ Press ENTER to continue ==>")

    # Example 4:
    print("\nInitializing column vector with range (2, 9)")
    v4 = Vector((2, 9))
    print("{0: <20}".format("v4: "), v4)
    print("{0: <20}".format("v4.shape: "), v4.shape)
    print("{0: <20}".format("v4.T(): "), v4.T()) 
    print("{0: <20}".format("v4.T().shape"), v4.T().shape)
    input("\n================================================ Press ENTER to continue ==>")
    # ADDITION
    print("\nVECTOR ADDITION")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v2.T(): "), v2.T()) # Output: Vector([[0.0], [1.0], [2.0], [3.0]])
    print("{0: <20}".format("v1 + v2.T(): "), v1 + v2.T())
    print("{0: <20}".format("(v1 + v2.T()).shape: "), (v1 + v2.T()).shape)
    input("\n================================================ Press ENTER to continue ==>")

    # SUBSTRACTION
    print("\nVECTOR SUBSTRACTION")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v2.T(): "), v2.T()) # Output: Vector([[0.0], [1.0], [2.0], [3.0]])
    print("{0: <20}".format("v1 - v2.T(): "), v1 - v2.T())
    print("{0: <20}".format("(v1 - v2.T()).shape: "), (v1 - v2.T()).shape)
    input("\n================================================ Press ENTER to continue ==>")

    # DIVISION
    print("\nVECTOR DIVISION BY SCALAR")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v1 / 2: "), v1 / 2)
    print("{0: <20}".format("(v1 / 2).shape: "), (v1 / 2).shape)
    input("\n================================================ Press ENTER to continue ==>")

    # Error management
    print("\n===========================ERROR MANAGEMENT=========================")

    print("\nInitializing vector with str argument")
    v5 = Vector("Hello")
    print("{0: <20}".format("v5: "), v5)

    print("\nInitializing vector with float argument")
    v5 = Vector(0.15)
    print("{0: <20}".format("v5: "), v5)

    print("\nInitializing vector with array of string")
    v5 = Vector(["hello", "how", "are", "you"])
    print("{0: <20}".format("v5: "), v5)

    print("\nInitializing vector with array of inconsistent types")
    v5 = Vector(["hello", 15, 0.5, None])
    print("{0: <20}".format("v5: "), v5)
    input("\n================================================ Press ENTER to continue ==>")

    print("\nVector addition with scalar")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v1 + 15: "), v1 + 15)

    print("\nString addition with vector")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("'hello' + v1: "), "hello" + v1)
    input("\n================================================ Press ENTER to continue ==>")

    print("\nVector division by 0")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v1 / 0: "), v1 / 0)

    print("\nVector division by another vector")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v2: "), v2)
    print("{0: <20}".format("v1 / v2: "), v1 / v2)

    print("\nVector multiplication by another vector")
    print("{0: <20}".format("v1: "), v1)
    print("{0: <20}".format("v2: "), v2)
    print("{0: <20}".format("v1 * v2: "), v1 * v2)

if __name__=="__main__":
    main()
