from ImageProcessor import ImageProcessor as imp

if __name__=="__main__":
    print("\n=> TESTING NON EXISTING FILE\n")
    arr = imp.load("non_existing_file.png")
    print(arr)

    print("\n=> TESTING EMPTY FILE\n")
    arr = imp.load("empty_file.png")
    print(arr)

    print("\n=> TESTING 42AI LOGO FILE\n")
    arr = imp.load("42AI.png")
    print(arr)