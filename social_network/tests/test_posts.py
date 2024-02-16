from lib.posts import Post

"""
Posts constructs with an id, user_id, post_title, post_contents, and post_views
"""
def test_posts_construct():
    test_post = Post(1, 1, "test post title", "some testing contents", 100)
    assert test_post.id == 1
    assert test_post.user_id == 1
    assert test_post.post_title == "test post title"
    assert test_post.post_contents == "some testing contents"
    assert test_post.post_views == 100


"""
We can format users to strings nicely
"""
def test_posts_format_nicely():
    test_post = Post(1, 1, "test post title", "some testing contents", 100)
    assert str(test_post) == "Post(1, 1, test post title, some testing contents, 100)"

"""
We can compare two identical users
And have them be equal - even if different instantiations
"""
def test_posts_are_equal():
    test_post1 = Post(1, 1, "test post title", "some testing contents", 100)
    test_post2 = Post(1, 1, "test post title", "some testing contents", 100)
    assert test_post1 == test_post2

