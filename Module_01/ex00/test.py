from recipe import Recipe
from book import Book

def main():
    print("Creating valid recipes quiche, salad, cake, tartines, stir fry")
    quiche = Recipe("quiche", 2, 35, ['puff pastry', 'eggs', 'leeks', 'cheese'], 'lunch', 'Delicious leeks quiche')
    salad = Recipe("salad", 1, 15, ['romaine', 'tomatoes', 'avocado', 'egg'], 'lunch', 'Quick and easy')
    cake = Recipe("cake", 4, 45, ['chocolate', 'flour', 'eggs', 'sugar', 'butter'], 'dessert', 'Goey and very rich')
    tartines = Recipe("tartines", 1, 10, ['bread', 'butter', 'pate', 'pickles'], 'starter')
    stir_fry = Recipe("stir fry", 3, 20, ['noodles', 'broccoli', 'carrots', 'onions', 'soy sauce', 'peanut butter'], 'lunch', 'Asian style noodles')

    input()

    print("Testing error management for Recipe class")
    wrong_recipe = Recipe("hello", "this is should be an int", 10, [], 'lunch')
    wrong_recipe = Recipe("hello", 1, "this should be an int", [], 'lunch')
    wrong_recipe = Recipe("hello", 1, 10, "this should be an array", 'lunch')
    wrong_recipe = Recipe("hello", 1, 10, [], 'this should be starter, lunch or dessert')
    wrong_recipe = Recipe("hello", 1, 10, [], 'lunch', ['description must be a str'])

    input()

    print("Instantiating a valid empty Book class object")
    recipes = Book("lunches", {"starter":[], "lunch":[], "dessert":[]})
    print(recipes)

    input()

    print("Testing error management for Book class")
    wrong_book = Book(["Book name should be a string"], {"starter":[], "lunch":[], "dessert":[]})
    wrong_book = Book("Wrong book", ['recipe list should be a dictionary'])
    wrong_book = Book("Wrong book", {'wrong key': 'this should be a recipe list'})
    wrong_book = Book("Wrong book", {'starter': 'this should be a recipe list'})
    wrong_book = Book("Wrong book", {'starter': 'this should be a recipe list', 'lunch':[], 'dessert':[]})

    input()

    print("Adding recipes to book")
    recipes.add_recipe(quiche)
    input()
    print(recipes)
    input()

    recipes.add_recipe(salad)
    input()
    print(recipes)
    input()

    recipes.add_recipe(cake)
    input()
    print(recipes)
    input()

    recipes.add_recipe(tartines)
    input()
    print(recipes)
    input()

    recipes.add_recipe(stir_fry)
    input()
    print(recipes)
    input()

    print("Testing get recipe by name method: looking for cake recipe")
    print(recipes.get_recipe_by_name("cake"))
    input()
    print("Testing error management: Looking for non existing recipe")
    print(recipes.get_recipe_by_name("non_existing_recipe"))
    input()
    print("Testing get recipes by type method: looking for lunch recipes")
    print(recipes.get_recipes_by_types("lunch"))
    print(recipes.get_recipes_by_types())
    input()
    print("Testing error management: looking for non existing meal type")
    print(recipes.get_recipes_by_types("non_existing_mealtype"))
    print(recipes.get_recipes_by_types())

if __name__=="__main__":
    main()