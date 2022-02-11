from csvreader import CsvReader

if __name__ == "__main__":
    try:
        print("\n=> Test 1 : Passing None as file")
        with CsvReader(None) as file:
            data = file.getdata()
            header = file.getheader()
    except Exception as exception:
        print(exception)

    try:
        input("\n============= Press ENTER to continue ==>\n")
        print("\n=> Test 2 : Passing a not existing file")
        with CsvReader("boom.csv") as file:
            data = file.getdata()
            header = file.getheader()
    except Exception as exception:
        print(exception)

    try:
        input("\n============= Press ENTER to continue ==>\n")
        print("\n=> Test 3 : Passing a corrupted CSV file")
        with CsvReader("bad.csv", header=True) as file:
            data = file.getdata()
            header = file.getheader()
    except Exception as exception:
        print(exception)

    try:
        input("\n============= Press ENTER to continue ==>\n")
        print("\n=> Test 4 : Passing a valid CSV file")
        with CsvReader("good.csv", header=True) as file:
            data = file.getdata()
            print("Data: ", data)
            header = file.getheader()
            print("Header: ", header)
    except Exception as exception:
        print(exception)