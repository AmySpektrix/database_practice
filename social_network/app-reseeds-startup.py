from lib.database_connection import DatabaseConnection
from lib.posts_repository import PostsRepository
from lib.users_repository import UsersRepository
from lib.posts import Post

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/social_network.sql")

    def run(self):
        print("Welcome to the basic social network!")
        program_continue = "Y"
        while program_continue == "Y":
            print("""
    What would you like to do?
    1 - See all posts by a user by their username
    2 - Add a new post
    3 - Delete a post
            """)
            choice = input("Enter your choice:")
            print("")

            if choice == "1":
                repository = UsersRepository(self._connection)
                username = input("Enter the required username:")
                posts = repository.find_posts_by_username(username)
                for post in posts:
                    print(f" * {post.id} - {post.post_title} : {post.post_contents} | views: {post.post_views}")

            elif choice == "2":
                repository_post = PostsRepository(self._connection)
                repository_user = UsersRepository(self._connection)            
                username = input("Enter your username:")
                user_id = repository_user.find_user_id(username)
                title = input("What is the title of your post:")
                contents = input("What do you want to say in your post:")
                repository_post.create(Post(None, user_id, title, contents, 0))

            elif choice == "3":
                repository = PostsRepository(self._connection)
                repository_post = PostsRepository(self._connection)
                repository_user = UsersRepository(self._connection)            
                username = input("Enter your username:")
                user_id = repository_user.find_user_id(username)
                print("Your posts are below:")
                posts = repository_user.find_posts_by_username(username)
                for post in posts:
                    print(f" * {post.id} - {post.post_title} : {post.post_contents} | views: {post.post_views}")
                choice = input("Which post do you want to delete?")
                repository_post.delete(choice)
                print(f"You have deleted post with the id {choice}")
            else:
                print ("that is not a valid choice please re-run the app to start again")
            
            print("")
            program_continue = input("Type 'Y' to continue with the program or any other character to exit the program")

if __name__ == '__main__':
    app = Application()
    app.run()