from HowManyMedals import howManyMedals
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
        print(howManyMedals(data, 'Kjetil Andr Aamodt'))

        print(f"\n=> Test error: no participant Cristina Fernández Bornay")
        print(howManyMedals(data, 'Cristina Fernández Bornay'))

        print(f"\n=> Test error: participant None")
        print(howManyMedals(data, None))

        print(f"\n=> Test error: data None")
        print(howManyMedals(None, 'Kjetil Andr Aamodt'))

    except Exception as e:
        print(e)