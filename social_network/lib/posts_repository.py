from lib.posts import Post

class PostsRepository:
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["user_id"], row["post_title"], row["post_contents"], row["post_views"])
            posts.append(item)
        return posts
    
    def find(self, post_id):
        rows = self._connection.execute('SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["user_id"], row["post_title"], row["post_contents"], row["post_views"])
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (user_id, post_title, post_contents, post_views) VALUES (%s, %s, %s, %s)', [post.user_id, post.post_title, post.post_contents, post.post_views])
        return post.id
    
    def delete(self, post_id):
        self._connection.execute('DELETE FROM posts WHERE id = %s', [post_id])
        return None