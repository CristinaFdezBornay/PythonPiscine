from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15
from SpatioTemporalData import SpatioTemporalData
sp = SpatioTemporalData(data)
print(sp.where(1896))
# Output
# ['Athina']
print(sp.where(2016))
# Output
# ['Rio de Janeiro']

print(sp.when('Athina'))
# Output
# [2004, 1906, 1896]
print(sp.when('Paris'))
# Output
# [1900, 1924]