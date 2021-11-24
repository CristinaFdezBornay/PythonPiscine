from csvreader import CsvReader

if __name__ == "__main__":
    with CsvReader("bad.csv") as file:
        if file == None:
            print("File is corrupted")