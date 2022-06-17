from FileLoader import FileLoader

tests = [
    "non_existing_file.csv",
    "empty_file.csv",
    "../data/athlete_events.csv",
]

if __name__=="__main__":
    for test in tests:
        print(f"==> TESTING {test}")
        fl = FileLoader()

        print(f"\n=> Loading file")
        df = fl.load(test)

        print(f"\n=> Display first 3 rows")
        fl.display(df, 3)

        print(f"\n=> Display lasts 3 rows")
        fl.display(df, -3)

        input("====>\n\n")