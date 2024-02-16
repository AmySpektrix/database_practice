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
    
    def find(self, album_id):
        single_album = self.connection.execute('SELECT * FROM albums WHERE id = %s',[album_id])
        row = single_album[0]
        return  Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def create(self, album):
        self.connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [album.title, album.release_year, album.artist_id])
        return album.id

    def delete(self, album_id):
        self.connection.execute('DELETE FROM albums WHERE id =(%s)', [album_id])