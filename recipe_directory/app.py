from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
# connection.seed("seeds/music_library.sql")

# Retrieve all recipes
all_recipes = RecipeRepository(connection)
list_of_all_recipes = all_recipes.all()

# List them out
for recipe in list_of_all_recipes:
    print (recipe)

