from YoungestFellah import youngestFellah
try:
    from FileLoader import FileLoader
except:
    print("Please import FileLoader from ex00")


if __name__=="__main__":
    try:
        file = '../data/athlete_events.csv'
        print(f"==> TESTING {file}")
        loader = FileLoader()

        print(f"\n=> Loading file")
        data = loader.load(file)

        print(f"\n=> Test correct")
        print(youngestFellah(data, 2004))

        print(f"\n=> Test error: no year 1991")
        print(youngestFellah(data, 1991))

        print(f"\n=> Test error: sending no data")
        print(youngestFellah(None, 2014))

        print(f"\n=> Test error: sending no year")
        print(youngestFellah(data, None))
    except Exception as e:
        print(e)


### [ WARNING ]
### The first example throws a FutureWarning:
### "Dropping of nuisance columns in DataFrame reductions (with 'numeric_only=None') is deprecated;"
### in a future version this will raise TypeError.  Select only valid columns before calling the reduction."
### => python3 test.py 2&>/dev/null