from datetime import datetime
from recipe import Recipe
import sys

class Book(object):
    def __init__(self, name, recipes_list, last_update=datetime.now(), creation_date=datetime.now()):
        """
        name : Book name
        last_update : datetime of last modification
        creation_date : datetime
        recipes_list : dictionary with 3 keys "starter", "lunch", "dessert"
        """
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list
        try:
            self._verify_input()
        except Exception as e:
            print(e)
            sys.exit()

    def _verify_input(self):
        if type(self.name) != str:
            raise NameError("Input error: Book name must be a string.")
        if type(self.last_update) != datetime:
            raise NameError("Input error: Book last update must be a datetime.")
        if type(self.creation_date) != datetime:
            raise NameError("Input error: Book creation date must be a datetime.")
        if type(self.recipes_list) != dict:
            raise NameError("Input error: Recipes list must be a dictionary with the following keys: 'starter', 'lunch' or 'dessert'.")
        else:
            for recipe_type in list(self.recipes_list.keys()):
                if recipe_type not in ['starter', 'lunch', 'dessert']:
                    raise NameError("Input error: Recipes list dictionary has invalid key {}. It must be one of the following: 'starter', 'lunch' or 'dessert'.".format(recipe_type))
            for recipe_type in ['starter', 'lunch', 'dessert']:
                if recipe_type not in list(self.recipes_list.keys()):
                    raise NameError("Input error: Recipes list must have the following key: {}".format(recipe_type))
        for recipe in self.recipes_list.values():
            print(recipe)
            print(isinstance(recipe, Recipe))
            quiche = Recipe("quiche", 2, 35, ['puff pastry', 'eggs', 'leeks', 'cheese'], 'lunch', 'Delicious leeks quiche')
            print(isinstance(quiche, Recipe))
            print(quiche)
            if isinstance(recipe, Recipe) == False:
                raise NameError("Input error: Recipes in recipe list dictionary must be Recipe instances.")

    def __str__(self):
        """Return the string to print with the recipe info"""
        first = True
        txt = "{} BOOK\n".format(self.name.upper())
        for meal in self.recipes_list.keys():
            if len(self.recipes_list[meal]) > 0:
                if first == True:
                    txt = txt + "{} RECIPES\n".format(meal.upper())
                    first = False
                else:
                    txt = txt + "\n\n{} RECIPES\n".format(meal.upper())
                for recipe in self.recipes_list[meal]:
                    txt = txt + "\n{} recipe".format(recipe.name.upper())
                    if recipe.description != "":
                        txt = txt + ": {}".format(recipe.description)
                    txt = txt + " | Difficulty: {} ".format(recipe.cooking_lvl)
                    txt = txt + "| Prep time: {} minutes".format(recipe.cooking_time)
                    txt = txt + "\nIngredients list: {}\n".format(recipe.ingredients)
        return txt

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
