import sys

class Recipe(object):
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description=""):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        try:
            self._verify_input()
        except Exception as e:
            print(e)
            sys.exit()

    def _verify_input(self):
        if type(self.name) != str:
            raise NameError("Input error: Recipe name must be a string.")
        if type(self.cooking_lvl) != int or self.cooking_lvl not in [1,2,3,4,5]:
            raise NameError("Input error: Recipe cooking level must be an integer between 1 and 5.")
        if type(self.cooking_time) != int or self.cooking_time < 0:
            raise NameError("Input error: Recipe cooking time is in minutes. It must be a positive integer.")
        if type(self.ingredients) != list:
            raise NameError("Input error: Recipe ingredients must be a list of strings.")
        if type(self.description) != str:
            raise NameError("Input error: Recipe description must be a string")
        if type(self.recipe_type) != str or self.recipe_type not in ['starter', 'lunch', 'dessert']:
            raise NameError("Input error: Recipe type must be one of the following: 'starter', 'lunch' or 'dessert'.")

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "Recipe for {}".format(self.name)
        if self.description != "":
            txt = txt + ": {}".format(self.description)
        txt = txt + "\nThis is a {} recipe ".format(self.recipe_type)
        txt = txt + "| Difficulty: {} ".format(self.cooking_lvl)
        txt = txt + "| Prep time: {} minutes".format(self.cooking_time)
        txt = txt + "\nIngredients list: {}".format(self.ingredients)
        return txt
