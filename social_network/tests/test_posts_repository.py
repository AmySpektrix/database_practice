from lib.posts_repository import PostsRepository
from lib.posts import Post

"""
When we call PostsRepository#all
We get a list of Post objects reflecting the seed data.
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/social_network.sql") 
    repository = PostsRepository(db_connection)
    posts = repository.all() # Get all posts
    assert posts == [
        Post(1, 1, 'What I did on my Holidays', 'It was great, I went to the beach', 10),
        Post(2, 2, 'I am the best poster ever', 'Why yes read all about my excellent time in this post of brilliance', 1),
        Post(3, 1, 'What I did when I got back from my Holidays', 'actually not a lot really, just went to the shops because we were out of milk :(', 300),
        Post(4, 3, 'Mwahahhahahahah', 'noone can know about my evil plot, here is my 10 step plan of how I will rob all the banks in the WORLD!!!! ', 666),
    ]

"""
When we call PostsRepository#find
We get a single Post object reflecting the seed data.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepository(db_connection)
    post = repository.find(2)
    assert post == Post(2, 2, 'I am the best poster ever', 'Why yes read all about my excellent time in this post of brilliance', 1)

"""
When we call PostsRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepository(db_connection)

    repository.create(Post(None, 3, 'What a great day!', 'Oh yeah, it was good I suppose.', 1))

    posts = repository.all()
    assert posts == [
        Post(1, 1, 'What I did on my Holidays', 'It was great, I went to the beach', 10),
        Post(2, 2, 'I am the best poster ever', 'Why yes read all about my excellent time in this post of brilliance', 1),
        Post(3, 1, 'What I did when I got back from my Holidays', 'actually not a lot really, just went to the shops because we were out of milk :(', 300),
        Post(4, 3, 'Mwahahhahahahah', 'noone can know about my evil plot, here is my 10 step plan of how I will rob all the banks in the WORLD!!!! ', 666),
        Post(5, 3, 'What a great day!', 'Oh yeah, it was good I suppose.', 1)
    ]

"""
When we call PostsRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostsRepository(db_connection)
    repository.delete(4) # doesn't want to reveal his secret plan!

    posts = repository.all()
    assert posts == [
        Post(1, 1, 'What I did on my Holidays', 'It was great, I went to the beach', 10),
        Post(2, 2, 'I am the best poster ever', 'Why yes read all about my excellent time in this post of brilliance', 1),
        Post(3, 1, 'What I did when I got back from my Holidays', 'actually not a lot really, just went to the shops because we were out of milk :(', 300)
    ]
