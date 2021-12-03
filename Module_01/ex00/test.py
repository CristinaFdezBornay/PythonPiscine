from recipe import Recipe
from book import Book

def main():
    print("Creating valid recipes quiche, salad, cake, tartines, stir fry.")
    quiche = Recipe("quiche", 2, 35,['puff pastry', 'eggs', 'leeks', 'cheese'],
                    'lunch', 'Delicious leeks quiche')
    salad = Recipe("salad", 1, 15, ['romaine', 'tomatoes', 'avocado', 'egg'],
                   'lunch', 'Quick and easy')
    cake = Recipe("cake", 4, 45, ['chocolate', 'flour', 'eggs', 'sugar', 'butter'],
                  'dessert', 'Goey and very rich')
    tartines = Recipe("tartines", 1, 10, ['bread', 'butter', 'pate', 'pickles'],
                      'starter')
    stir_fry = Recipe("stir fry", 3, 20, ['noodles', 'broccoli', 'carrots', 'onions',
                      'soy sauce', 'peanut butter'], 'lunch', 'Asian style noodles')

    input("\n=> Press ENTER to continue with the testing.\n")

    print("\n=> Testing error management for Recipe class.\n")
    wrong_recipe = Recipe("hello", "this is should be an int", 10, [], 'lunch')
    wrong_recipe = Recipe("hello", 1, "this should be an int", [], 'lunch')
    wrong_recipe = Recipe("hello", 1, 10, "this should be an array", 'lunch')
    wrong_recipe = Recipe("hello", 1, 10, [], 'this should be starter, lunch or dessert')
    wrong_recipe = Recipe("hello", 1, 10, [], 'lunch', ['description must be a str'])

    input("\n=> Press ENTER to continue with the testing.\n")

    print("\n=> Instantiating a valid empty Book class object.\n")
    recipes = Book("lunches", {"starter":[], "lunch":[], "dessert":[]})
    print(recipes)

    input("\n=> Press ENTER to continue with the testing.\n")

    print("\n=> Testing error management for Book class.\n")
    wrong_book = Book(["Book name should be a string"], {"starter":[], "lunch":[], "dessert":[]})
    wrong_book = Book("Wrong book", ['recipe list should be a dictionary'])
    wrong_book = Book("Wrong book", {'wrong key': 'this should be a recipe list'})
    wrong_book = Book("Wrong book", {'starter': 'this should be a recipe list'})
    wrong_book = Book("Wrong book", {'starter': 'this should be a recipe list', 'lunch':[],
                      'dessert':[]})

    input("\n=> Press ENTER to continue with the testing.\n")

    print("\n=> Adding recipes to book.\n")
    recipes.add_recipe(quiche)
    input("\n=> Press ENTER to continue with the testing.\n")
    print(recipes)
    input("\n=> Press ENTER to continue with the testing.\n")

    recipes.add_recipe(salad)
    input("\n=> Press ENTER to continue with the testing.\n")
    print(recipes)
    input("\n=> Press ENTER to continue with the testing.\n")

    recipes.add_recipe(cake)
    input("\n=> Press ENTER to continue with the testing.\n")
    print(recipes)
    input("\n=> Press ENTER to continue with the testing.\n")

    recipes.add_recipe(tartines)
    input("\n=> Press ENTER to continue with the testing.\n")
    print(recipes)
    input("\n=> Press ENTER to continue with the testing.\n")

    recipes.add_recipe(stir_fry)
    input("\n=> Press ENTER to continue with the testing.\n")
    print(recipes)
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\n=> Testing get recipe by name method: looking for cake recipe.\n")
    print(recipes.get_recipe_by_name("cake"))
    input("\n=> Press ENTER to continue with the testing.\n")
    print("\n=> Testing error management: Looking for non existing recipe.\n")
    print(recipes.get_recipe_by_name("non_existing_recipe"))
    input("\n=> Press ENTER to continue with the testing.\n")
    print("\n=> Testing get recipes by type method: looking for lunch recipes.\n")
    print(recipes.get_recipes_by_types("lunch"))
    print(recipes.get_recipes_by_types())
    input("\n=> Press ENTER to continue with the testing.\n")
    print("\n=> Testing error management: looking for non existing meal type.\n")
    print(recipes.get_recipes_by_types("non_existing_mealtype"))
    print(recipes.get_recipes_by_types())

if __name__=="__main__":
    main()
