class Recipe(object):
    def __init__(self, name=None, cooking_lvl=None, cooking_time=None,
                 ingredients=None, recipe_type=None, description=""):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type
        try:
            self._verify_input()
        except Exception as exception:
            print(exception)

    def _verify_input(self):
        if not isinstance(self.name, str):
            raise NameError("Input error: Recipe name must be a string.")
        if not isinstance(self.cooking_lvl, int) or self.cooking_lvl not in [1,2,3,4,5]:
            raise NameError("Input error: Recipe cooking level must be an integer between 1 and 5.")
        if not isinstance(self.cooking_time, int) or self.cooking_time < 0:
            raise NameError("""Input error: Recipe cooking time is in minutes.
             It must be a positive integer.""")
        if not isinstance(self.ingredients, list):
            raise NameError("Input error: Recipe ingredients must be a list of strings.")
        if not isinstance(self.description, str):
            raise NameError("Input error: Recipe description must be a string")
        if not isinstance(self.recipe_type, str) \
           or self.recipe_type not in ['starter', 'lunch', 'dessert']:
            raise NameError("""Input error: Recipe type must be one of the following:
             'starter', 'lunch' or 'dessert'.""")

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
