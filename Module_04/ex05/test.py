from FileLoader import FileLoader
loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Loading dataset of dimensions 271116 x 15
from HowManyMedalsByCountry import howManyMedalsByCountry
print(howManyMedalsByCountry(data, 'Poland'))