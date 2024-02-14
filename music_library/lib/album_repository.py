from lib.album import Album

class AlbumRepository:
    
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        all_albums = self.connection.execute ('SELECT * FROM albums')
        albums = []
        for row in all_albums:
            album = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(album)
        return albums
    
    