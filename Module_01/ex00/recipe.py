class Recipe(object):
    """
    Class that allows user to store recipe information in a recipe object
    """
    def __new__(cls, name=None, cooking_lvl=None, cooking_time=None,
                 ingredients=None, description="", recipe_type=None):
        """
        Only creating class object if arguments are valid
        """
        try:
        # def _verify_input(name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
            if not isinstance(name, str):
                raise NameError("Input error: Recipe name must be a string.")
            if not isinstance(cooking_lvl, int) or cooking_lvl not in [1,2,3,4,5]:
                raise NameError("Input error: Recipe cooking level must be an integer between 1 and 5.")
            if not isinstance(cooking_time, int) or cooking_time < 0:
                raise NameError("Input error: Recipe cooking time is in minutes. \
    It must be a positive integer.")
            if not isinstance(ingredients, list) or len(ingredients) == 0:
                raise NameError("Input error: Recipe ingredients must be a non empty list of strings.")
            if not isinstance(description, str):
                raise NameError("Input error: Recipe description must be a string")
            if not isinstance(recipe_type, str) \
            or recipe_type not in ['starter', 'lunch', 'dessert']:
                raise NameError("Input error: Recipe type must be one of the following: \
'starter', 'lunch' or 'dessert'.")
        # try:?
            # verify_input(name, cooking_lvl, cooking_time, ingredients, description, recipe_type)
            return super(Recipe, cls).__new__(cls)
        except NameError as e:
            print(e)
            return None

    def __init__(self, name=None, cooking_lvl=None, cooking_time=None,
                 ingredients=None, description="", recipe_type=None):
        """
        Initializing attributes: recipe name, cooking level, ingredients, description, recipe type
        """
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        # try:
            # self._verify_input()
        # except Exception as exception:
            # print(exception)


    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = f"Recipe for {self.name}"
        if self.description != "":
            txt = txt + f": {self.description}"
        txt = txt + f"\nThis is a {self.recipe_type} recipe "
        txt = txt + f"| Difficulty: {self.cooking_lvl} "
        txt = txt + f"| Prep time: {self.cooking_time} minutes"
        txt = txt + f"\nIngredients list: {self.ingredients}"
        return txt
