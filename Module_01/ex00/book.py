from datetime import datetime
from recipe import Recipe

class Book(object):
    def __init__(self, name=None, recipes_list=None, last_update=datetime.now(), creation_date=datetime.now()):
        """
        name : Book name
        last_update : datetime of last modification
        creation_date : datetime
        recipes_list : dictionary with 3 keys "starter", "lunch", "dessert"
        """
        try:
            self.name = name
            self.last_update = last_update
            self.creation_date = creation_date
            self.recipes_list = recipes_list
            self._verify_input()
        except Exception as e:
            print(e)

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
                    raise NameError("Input error: Recipes list dictionary has invalid key '{}'. It must be one of the following: 'starter', 'lunch' or 'dessert'.".format(recipe_type))
            missing_keys = []
            for recipe_type in ['starter', 'lunch', 'dessert']:
                if recipe_type not in list(self.recipes_list.keys()):
                    missing_keys.append(recipe_type)
            if len(missing_keys) > 0:
                raise NameError("Input error: Recipes list must have the following key: {}".format(missing_keys))
        for recipe_array in self.recipes_list.values():
            for recipe in recipe_array:
                if isinstance(recipe, Recipe) == False:
                    raise NameError("Input error: Recipes in recipe list dictionary must be Recipe instances.")

    def __str__(self):
        """Return the string to print with the recipe info"""
        first = True
        empty = True
        txt = "{} BOOK (created {})\n\n".format(self.name.upper(), self.creation_date.strftime("%Y-%m-%d %H:%M:%S"))
        for meal in self.recipes_list.keys():
            if len(self.recipes_list[meal]) > 0:
                if first == True:
                    txt = txt + "{} RECIPES".format(meal.upper())
                    first = False
                    empty = False
                else:
                    txt = txt + "\n\n{} RECIPES".format(meal.upper())
                for recipe in self.recipes_list[meal]:
                    txt = txt + '\n\n' + str(recipe)
        if empty == True:
            txt = "{} BOOK has no recipe yet. Feel free to add your recipes!".format(self.name.upper())
        return txt

    def get_recipe_by_name(self, name=None):
        """Prints a recipe with the name and returns the instance"""
        if name == None:
            return "Input error: You need to give a recipe name to search."
        for meal, recipes in self.recipes_list.items():
            for recipe in recipes:
                if recipe.name == name:
                    return recipe
        return "Couldn't find {} recipe in the book. Are you sure you spelled it correctly?".format(name)

    def get_recipes_by_types(self, recipe_type=None):
        """Get all recipe names for a given recipe_type"""
        if recipe_type == None:
            return "Input error: You need to give a recipe_type to search"
        ret = []
        for meal, recipes in self.recipes_list.items():
            if meal == recipe_type:
                for recipe in recipes:
                    ret.append(recipe.name)
                return ret
        return "Couldn't find {} recipes in the book. Are you sure you spelled it correctly?".format(recipe_type)

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe) == False:
            print("Type error: {} is not a Recipe object.".format(recipe))
            return
        if recipe.recipe_type in ["starter", "lunch", "dessert"]:
            print("Adding {} to {} recipes. Updated {} book at {}".format(recipe.name, recipe.recipe_type, self.name, self.last_update.strftime("%Y-%m-%d %H:%M:%S")))
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
