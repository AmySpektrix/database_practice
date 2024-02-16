from lib.users import User

class UsersRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email_address"])
            users.append(item)
        return users

    def find(self, artist_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [artist_id])
        row = rows[0]
        return User(row["id"], row["username"], row["email_address"])


    def create(self, user):
        self._connection.execute('INSERT INTO users (username, email_address) VALUES (%s, %s)', [user.username, user.email_address])
        return user.id

    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None
