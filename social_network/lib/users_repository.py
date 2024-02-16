from lib.users import User
from lib.posts import Post

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

    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from users WHERE id = %s', [user_id])
        row = rows[0]
        return User(row["id"], row["username"], row["email_address"])


    def create(self, user):
        self._connection.execute('INSERT INTO users (username, email_address) VALUES (%s, %s)', [user.username, user.email_address])
        return user.id

    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None

    def find_posts_by_username(self,username):
        rows = self._connection.execute(
            'SELECT users.id AS user_id, users.username, users.email_address, posts.id AS post_id, posts.post_title, posts.post_contents, posts.post_views FROM users JOIN posts on users.id = posts.user_id WHERE users.username = %s', [username])
        posts = []
        for row in rows:
            post = Post(row["post_id"],row["user_id"], row ["post_title"], row["post_contents"], row["post_views"])
            posts.append(post)
        return posts
    
    def find_user_id(self,username):
        rows = self._connection.execute(
            'SELECT * from users WHERE username = %s', [username])
        row = rows[0]
        return row["id"]