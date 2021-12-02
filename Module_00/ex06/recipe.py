import sys

def init_cookbook():
    global cookbook
    cookbook = {}
    add_recipe('sandwich', ['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', 10)
    add_recipe('cake', ['flour', 'sugar', 'eggs'], 'dessert', 60)
    add_recipe('salad', ['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', 15)

def print_recipe(recipe_name):
    if recipe_name in cookbook.keys():
        recipe = "Recipe for {recipe_name}:\nIngredients list: {ingredients}\nTo be eaten for {meal}\nTakes {prep_time} minutes for cooking.".format(recipe_name=recipe_name, ingredients=cookbook[recipe_name]['ingredients'], meal=cookbook[recipe_name]['meal'], prep_time=cookbook[recipe_name]['prep_time'])
        print(recipe)
    else:
        print("Couldn't find the {} recipe in the cookbook. Make sure you give an existing recipe to print.".format(recipe_name))

def add_recipe(recipe_name, ingredients, meal_type, prep_time):
    if recipe_name not in cookbook.keys():
        cookbook[recipe_name] = {
            'ingredients': ingredients,
            'meal': meal_type,
            'prep_time': prep_time
        }
    else:
        print("Recipe {} already exists in the cookbook. Remove the existing recipe if you want to change it.".format(recipe_name))

def delete_recipe(recipe_name):
    if recipe_name in cookbook.keys():
        del cookbook[recipe_name]
        print("Successfully removed {} recipe from cookbook.".format(recipe_name))
    else:
        print("Couldn't find the {} recipe in the cookbook. Make sure you give an existing recipe to delete.".format(recipe_name))

def print_cookbook():
    print("Here are all the recipes in your cookbook")
    for recipe_name, recipe in cookbook.items():
        print()
        print_recipe(recipe_name)

def is_valid_response(user_response):
    if user_response not in ['1', '2', '3', '4', '5']:
        return False
    return True

def process_response(user_response):
    if user_response == '1':
        print("\nWhat is the name of the recipe you want to add to your cookbook?")
        recipe_name = input()
        print("\nWhat are the ingredients required for this {} recipe? Write them with a comma in between to separate each ingredient.".format(recipe_name))
        ingredients_str = input()
        print("\nWhat is the meal type of this {} (breakfast, lunch, dinner, snack, dessert, etc...)?".format(recipe_name))
        meal = input()
        print("\nHow long does it take to prepare this {}(in mins)?".format(recipe_name))
        preptime = input()
        recipe_name, ingredients, preptime = format_recipe(recipe_name, ingredients_str, preptime)
        return add_recipe(recipe_name, ingredients, meal, preptime)
    if user_response == '2':
        print("\nPlease enter the recipe's name to be deleted:")
        recipe_name = input()
        return delete_recipe(recipe_name)
    if user_response == '3':
        print("\nPlease enter the recipe's name to get its details:")
        recipe_name = input()
        print()
        return print_recipe(recipe_name)
    if user_response == '4':
        return print_cookbook()
    if user_response == '5':
        print("\nCookbook closed.")
        sys.exit(0)

def format_recipe(recipe_name, ingredients_str, preptime):
    ingredients = []
    recipe_name = recipe_name.strip()
    ingredients_list = ingredients_str.split(',')
    for ingredient in ingredients_list:
        ingredient = ingredient.strip()
        ingredients.append(ingredient)
    try:
        preptime = int(preptime)
        return recipe_name, ingredients, preptime
    except:
        print("Preparation time must be an integer.")
        print("Couldn't add {} recipe to cookbook. Please make sure all the elements correspond.".format(recipe_name))
        sys.exit(-1)

def main():
    init_cookbook()
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    user_response = input()
    while is_valid_response(user_response) == False:
        print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.")
        user_response = input()
    process_response(user_response)
    while is_valid_response(user_response) == True and user_response != '5':
        print("\nAnything else?")
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        user_response = input()
        while is_valid_response(user_response) == False:
            print("\nThis option does not exist, please type the corresponding number.\nTo exit, enter 5.")
            user_response = input()
        process_response(user_response)

if __name__=='__main__':
    main()