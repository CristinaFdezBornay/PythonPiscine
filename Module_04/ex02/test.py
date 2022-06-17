from ProportionBySport import proportionBySport
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
        print(f"% M 2004 Gymnastics : {proportionBySport(data, 2004, 'Gymnastics', 'M')}")
        print(f"% F 2004 Gymnastics : {proportionBySport(data, 2004, 'Gymnastics', 'F')}")
        print(f"% F 2004 Tennis     : {proportionBySport(data, 2004, 'Tennis', 'F')}")

        print(f"\n=> Test error: no year 1991")
        print(proportionBySport(data, 1991, 'Gymnastics', 'M'))

        print(f"\n=> Test error: no sport Chess")
        print(proportionBySport(data, 2004, 'Chess', 'M'))

        print(f"\n=> Test error: no year")
        print(proportionBySport(data, None, 'Gymnastics', 'W'))

        print(f"\n=> Test error: no sport")
        print(proportionBySport(data, 2004, None, 'W'))

        print(f"\n=> Test error: no gender")
        print(proportionBySport(data, 2004, 'Gymnastics', None))
    except Exception as e:
        print(e)