from recipe import Recipe
from book import Book
from datetime import datetime

quiche = Recipe("quiche", 2, 35, ['puff pastry', 'eggs', 'leeks', 'cheese'], 'lunch', 'Delicious leeks quiche')
salad = Recipe("salad", 1, 15, ['romaine', 'tomatoes', 'avocado', 'egg'], 'lunch', 'Quick and easy')
chocolate_cake = Recipe("cake", 4, 45, ['chocolate', 'flour', 'eggs', 'sugar', 'butter'], 'dessert', 'Goey and very rich')
tartines = Recipe("tartines", 1, 10, ['bread', 'butter', 'pate', 'pickles'], 'starter')

test = 1
recipes = Book("lunches", {"starter":[tartines], "lunch":[quiche, salad], "dessert":[chocolate_cake]})
print(str(recipes))