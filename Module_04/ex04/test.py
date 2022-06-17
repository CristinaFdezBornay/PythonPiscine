from SpatioTemporalData import SpatioTemporalData
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

        sp = SpatioTemporalData(data)

        print(f"\n=> Test correct where")
        print(f"1896 : {sp.where(1896)}")
        print(f"2016 : {sp.where(2016)}")

        print(f"\n=> Test error where: no data for year")
        print(f"1991 : {sp.where(1991)}")

        print(f"\n=> Test error where: year None")
        print(f"None : {sp.where(None)}")

        print(f"\n=> Test correct when")
        print(f"Athina : {sp.when('Athina')}")
        print(f"Paris  : {sp.when('Paris')}")

        print(f"\n=> Test error where: no data for location")
        print(f"Madrid : {sp.when('Madrid')}")

        print(f"\n=> Test error where: location None")
        print(f"None   : {sp.when(None)}")

    except Exception as e:
        print(e)