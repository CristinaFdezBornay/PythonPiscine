from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')

from YoungestFellah import youngestFellah
print(youngestFellah(data, 2004))

print(youngestFellah(data, 1991))

print(youngestFellah(15, 'hello'))
print(youngestFellah(15, 2004))
print(youngestFellah(data, 15))

