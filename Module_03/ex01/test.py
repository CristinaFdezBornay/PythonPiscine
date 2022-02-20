from ImageProcessor import ImageProcessor as imp

tests = [
    "non_existing_file.png",
    "empty_file.png",
    "42AI.png",
]

if __name__=="__main__":
    for test in tests:
        print(f"=> TESTING {test}")
        array = imp.load(test)
        imp.display(array)
        input("====>\n")