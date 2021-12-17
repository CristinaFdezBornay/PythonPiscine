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

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nTESTING ERROR MANAGEMENT FOR RECIPE CLASS\n")
    print("\nCreating Recipe object with string instead of int as difficulty level")
    Recipe("hello", "this is should be an int", 10, [], 'lunch')
    print("\nCreating Recipe object with string instead of int as cooking time")
    Recipe("hello", 1, "this should be an int", [], 'lunch')
    print("\nCreating Recipe object with string instead of list as ingredients list")
    Recipe("hello", 1, 10, "this should be an array", 'lunch')
    print("\nCreating Recipe object with non existing meal type")
    Recipe("hello", 1, 10, [], 'this should be starter, lunch or dessert')
    print("\nCreating Recipe object with array instead of str as recipe description")
    Recipe("hello", 1, 10, [], 'lunch', ['description must be a str'])
    print("\nCreating Recipe object with int instead of str as recipe name")
    Recipe(12, 1, 10, [], 'lunch')

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nINSTANTIATING A VALID EMPTY BOOK CLASS OBJECT.\n")
    recipes = Book("lunches", {"starter":[], "lunch":[], "dessert":[]})
    print(recipes)

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nTESTING ERROR MANAGEMENT FOR BOOK CLASS.\n")
    print("\nCreating Book object with array as book name instead of str")
    Book(["Book name should be a string"], {"starter":[], "lunch":[], "dessert":[]})
    print("\nCreating Book object with array as recipe list instead of dict")
    Book("Wrong book", ['recipe list should be a dictionary'])
    print("\nCreating Book object with non existing meal type as recipe list dict key")
    Book("Wrong book", {'wrong key': 'this should be a recipe list'})
    print("\nCreating Book object with string type instead of array for recipe list dict values")
    Book("Wrong book", {'starter': 'this should be a recipe list'})
    print("\nCreating Book object with string type instead of array for recipe list dict values")
    Book("Wrong book", {'starter': 'this should be a recipe list', 'lunch':[],'dessert':[]})

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nADDING QUICHE RECIPE TO BOOK.\n")
    recipes.add_recipe(quiche)
    print()
    print(recipes)

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nADDING SALAD RECIPE TO BOOK.\n")
    recipes.add_recipe(salad)
    print()
    print(recipes)

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nADDING CAKE RECIPE TO BOOK.\n")
    recipes.add_recipe(cake)
    print()
    print(recipes)

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nADDING TARTINES RECIPE TO BOOK.\n")
    recipes.add_recipe(tartines)
    print()
    print(recipes)

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nADDING STIR FRY RECIPE TO BOOK.\n")
    recipes.add_recipe(stir_fry)
    print()
    print(recipes)

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("Printing book creation date vs last update")
    print(recipes.creation_date)
    print(recipes.last_update)

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nBOOK GET_RECIPE METHOD BY NAME: looking for cake recipe.\n")
    print(recipes.get_recipe_by_name("cake"))

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nBOOK GET_RECIPE METHOD BY MEAL TYPE: looking for lunch recipes.\n")
    print(recipes.get_recipes_by_types("lunch"))

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nERROR MANAGEMENT BOOK: Looking for non existing recipe.\n")
    print(recipes.get_recipe_by_name("non_existing_recipe"))

    print("\n================================================")
    input("\n=> Press ENTER to continue with the testing.\n")

    print("\nBOOK GET_RECIPE METHOD BY MEAL TYPE: looking for non existing meal type.\n")
    print(recipes.get_recipes_by_types("non_existing_mealtype"))
    print()
    print("\nBOOK GET_RECIPE METHOD BY MEAL TYPE: no recipe type argument given.\n")
    print(recipes.get_recipes_by_types())

if __name__=="__main__":
    main()
