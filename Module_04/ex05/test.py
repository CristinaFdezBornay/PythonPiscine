from HowManyMedalsByCountry import howManyMedalsByCountry   
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

        print(f"\n=> Test correct Spain")
        print(howManyMedalsByCountry(data, 'Spain'))

        print(f"\n=> Test correct Benin")
        print(howManyMedalsByCountry(data, 'Benin'))

        print(f"\n=> Test error: country None")
        print(howManyMedalsByCountry(data, None))

    except Exception as e:
        print(e)