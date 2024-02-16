class User:

    def __init__(self, id, username, email_address, posts=[]):
        self.id = id
        self.username = username
        self.email_address = email_address
        self.posts = posts

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email_address})"