class Post:
    def __init__(self, id, user_id, post_title, post_contents, post_views):
        self.id = id
        self.user_id = user_id
        self.post_title = post_title
        self.post_contents = post_contents
        self.post_views = post_views

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Post({self.id}, {self.user_id}, {self.post_title}, {self.post_contents}, {self.post_views})"    