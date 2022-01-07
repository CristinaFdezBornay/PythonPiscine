from datetime import datetime
from recipe import Recipe

class Book():
    """
    This class allows the user to store recipes in a Book object.
    The book has a name, creation date, update date, recipe list
    """
    def __init__(self, name=None, recipes_list={'starter':[], 'lunch':[], 'dessert':[]},
                 last_update=datetime.now(), creation_date=datetime.now()):
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
        except Exception as exception:
            print(exception)
            return None

    def _verify_input(self):
        """Verifies if user input is valid with type and value"""
        if not isinstance(self.name, str):
            raise NameError("Input error: Book name must be a string.")
        if not isinstance(self.last_update, datetime):
            raise NameError("Input error: Book last update must be a datetime.")
        if not isinstance(self.creation_date, datetime):
            raise NameError("Input error: Book creation date must be a datetime.")
        if not isinstance(self.recipes_list, dict):
            raise NameError("Input error: Recipes list must be a dictionary with the following keys: 'starter', 'lunch' or 'dessert'.")
        for recipe_type in list(self.recipes_list.keys()):
            if recipe_type not in ['starter', 'lunch', 'dessert']:
                raise NameError(f"Input error: Recipes list dictionary has invalid key '{recipe_type}'. It must be one of the following: 'starter', 'lunch' or 'dessert'.")
        missing_keys = []
        for recipe_type in ['starter', 'lunch', 'dessert']:
            if recipe_type not in list(self.recipes_list.keys()):
                missing_keys.append(recipe_type)
        if len(missing_keys) > 0:
            raise NameError(f"Input error: Recipes list must have the following key: {missing_keys}")
        for recipe_array in self.recipes_list.values():
            for recipe in recipe_array:
                if not isinstance(recipe, Recipe):
                    raise NameError("Input error: Recipes in recipe list dictionary must be Recipe instances.")

    def __str__(self):
        """Return the string to print with the recipe info"""
        first = True
        empty = True
        formated_creation_date = self.creation_date.strftime("%Y-%m-%d %H:%M:%S")
        txt = f"{self.name.upper()} BOOK (created {formated_creation_date})\n\n"
        for meal in self.recipes_list.keys():
            if len(self.recipes_list[meal]) > 0:
                if first:
                    txt = txt + f"{meal.upper()} RECIPES"
                    first = False
                    empty = False
                else:
                    txt = txt + f"\n\n{meal.upper()} RECIPES"
                for recipe in self.recipes_list[meal]:
                    txt = txt + '\n\n' + str(recipe)
        if empty:
            txt = f"{self.name.upper()} BOOK has no recipe yet. Feel free to add your recipes!"
        return txt

    def get_recipe_by_name(self, name=None):
        """Prints a recipe with the name and returns the instance"""
        if name is None:
            return "Input error: You need to give a recipe name to search."
        for _, recipes in self.recipes_list.items():
            for recipe in recipes:
                if recipe.name == name:
                    return recipe
        print(f"Couldn't find {name} recipe in the book. Are you sure you spelled it correctly?")
        return None

    def get_recipes_by_types(self, recipe_type=None):
        """Get all recipe names for a given recipe_type"""
        if recipe_type is None:
            return "Input error: You need to give a recipe_type to search"
        ret = []
        for meal, recipes in self.recipes_list.items():
            if meal == recipe_type:
                for recipe in recipes:
                    ret.append(recipe.name)
                return ret
        print(f"Couldn't find {recipe_type} recipes in the book. Are you sure you spelled it correctly?")
        return None

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            print(f"Type error: {recipe} is not a Recipe object.")
            return
        if recipe.recipe_type in ["starter", "lunch", "dessert"]:
            formated_last_update = self.last_update.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Adding {recipe.name} to {recipe.recipe_type} recipes. Updated {self.name} book at {formated_last_update}.")
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
