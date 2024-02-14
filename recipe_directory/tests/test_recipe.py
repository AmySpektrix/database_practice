from lib.recipe import Recipe

"""
Recipe constructs with an id, recipe_name, cooking_time and rating
"""
def test_recipes_construct():
    test_recipe = Recipe(1, "Test Recipe", 50, 5)
    assert test_recipe.id == 1
    assert test_recipe.recipe_name == "Test Recipe"
    assert test_recipe.cooking_time == 50
    assert test_recipe.rating == 5

"""
We can format recipes to strings nicely
"""
def test_recipes_format_nicely():
    test_recipe = Recipe(1, "Test Recipe", 50, 5)
    assert str(test_recipe) == "Recipe(1, Test Recipe, 50, 5)"
    # Try commenting out the `__repr__` method in lib/artist.py
    # And see what happens when you run this test again.

"""
We can compare two identical recipes
And have them be equal
"""
def test_recipes_are_equal():
    test_recipe = Recipe(1, "Test Recipe", 50, 5)
    test_recipe2 = Recipe(1, "Test Recipe", 50, 5)
    assert test_recipe == test_recipe2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
