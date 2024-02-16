from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.album import Album

# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/music_library.sql")

# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()

# List them out
print("ARTISTS")
for artist in artists:
    print(artist)

album_repository = AlbumRepository(connection)
albums = album_repository.all()

print("STARTING ALBUMS")
for album in albums:
    print(album)

print("FIRST ALBUM")
first_album = album_repository.find(1)
print (first_album)

album_repository.create(Album(None,'Red (Taylors Version)', 2021, 3))
album_repository.delete(3)

albums = album_repository.all()
print("ADDING NEW AT 13 AND REMOVING 3")
for album in albums:
    print(album)