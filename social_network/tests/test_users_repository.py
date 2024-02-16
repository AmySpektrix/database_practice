from lib.users_repository import UsersRepository
from lib.users import User
from lib.posts import Post

"""
When we call UsersRepository#all
We get a list of User objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = UsersRepository(db_connection)
    users = repository.all()
    assert users == [
                User(1,'amy_brown', 'amys-fake-email@hotmail.com'),
                User(2, 'best_username_ever', 'what-a-great-email@email.com'),
                User(3, 'dr-evil', 'evil@evilcity.com')
        ]
"""
When we call UsersRepository#find
We get a single User object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UsersRepository(db_connection)
    user = repository.find(2)
    assert user == User(2, 'best_username_ever', 'what-a-great-email@email.com')

"""
When we call UsersRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UsersRepository(db_connection)

    repository.create(User(None, 'what_a_fantastic_user', 'best-user@tip-top-email.com'))

    users = repository.all()
    assert users == [
                User(1,'amy_brown', 'amys-fake-email@hotmail.com'),
                User(2, 'best_username_ever', 'what-a-great-email@email.com'),
                User(3, 'dr-evil', 'evil@evilcity.com'),
                User(4, 'what_a_fantastic_user', 'best-user@tip-top-email.com')
        ]

"""
When we call UsersRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UsersRepository(db_connection)
    repository.delete(3)

    users = repository.all()
    assert users == [
                User(1,'amy_brown', 'amys-fake-email@hotmail.com'),
                User(2, 'best_username_ever', 'what-a-great-email@email.com')
        ]
    
"""
We can find a users posts by calling Users# find_posts_by_username
"""

def test_find_posts_by_username(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UsersRepository(db_connection)
    users_posts = repository.find_posts_by_username("amy_brown")
    assert users_posts == [Post(1, 1, 'What I did on my Holidays', 'It was great, I went to the beach', 10), Post(3, 1, 'What I did when I got back from my Holidays', 'actually not a lot really, just went to the shops because we were out of milk :(', 300)]   

def test_find_userid_by_username(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UsersRepository(db_connection)
    user_id = repository.find_user_id("amy_brown")
    assert user_id == 1