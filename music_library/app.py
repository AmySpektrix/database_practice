from lib.artist_repository import ArtistRepository
from lib.artist import Artist
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

    def run(self):
        print("Welcome to the music library manager!")
        program_continue = "Y"
        while program_continue == "Y":
            print("""
What would you like to do?
1 - List all albums
2 - List all artists
3 - Add an artist
        """)
        choice = input("Enter your choice:")
        print("")

        if choice == "1":
            album_repository = AlbumRepository(self._connection)
            albums = album_repository.all()
            print("Here is the list of albums:")
            for album in albums:
                print(f" * {album.id} - {album.title}") 

        elif choice == "2":
            artist_repository = ArtistRepository(self._connection)
            artists = artist_repository.all()
            print("Here is the list of artists:")
            for artist in artists:
                print(f" * {artist.id} - {artist.name} ({artist.genre})")
        
        elif choice == "3":
            artist_repository = ArtistRepository(self._connection)
            artist_name = input("What is the artist's name?:")
            artist_genre = input("What is the artist's genre?:")
            new_artist = Artist(None, artist_name, artist_genre)
            artist_repository.create(new_artist)
            print(f"Great, so you have added a new artist called {artist_name} with the genre {artist_genre}")
            

        else:
            print ("that is not a valid choice please re-run the app to start again")
            
        print("")
        program_continue = input("Type 'Y' to continue with the program or any other character to exit the program")

if __name__ == '__main__':
    app = Application()
    app.run()
