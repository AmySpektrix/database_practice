from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/recipe_directory.sql") 
    repository = RecipeRepository(db_connection) 

    recipes = repository.all()

    assert recipes == [
        Recipe(1, 'Puttanesca Pasta Sauce', 25, 4),
        Recipe(2, 'Lentil Lasagna', 60, 4),
        Recipe(3, 'Leek and Potato Soup', 20, 3),
        Recipe(4, 'Aubergine Parmagiana', 90, 5),
        Recipe(5, 'Spinach and Sweet Potato Enchilada Bake', 60, 2)
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/recipe_directory.sql") 
    repository = RecipeRepository(db_connection) 

    recipe = repository.find(3)
    assert recipe == Recipe(3, 'Leek and Potato Soup', 20, 3)

# """
# When we call ArtistRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)

#     repository.create(Artist(None, "The Beatles", "Rock"))

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(3, "Taylor Swift", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#         Artist(5, "The Beatles", "Rock"),
#     ]

# """
# When we call ArtistRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/music_library.sql")
#     repository = ArtistRepository(db_connection)
#     repository.delete(3) # Apologies to Taylor Swift fans

#     result = repository.all()
#     assert result == [
#         Artist(1, "Pixies", "Rock"),
#         Artist(2, "ABBA", "Pop"),
#         Artist(4, "Nina Simone", "Jazz"),
#     ]
