from lib.users import User

"""
User constructs with an id, username and email
"""
def test_user_constructs():
    test_user = User(1, "test_username", "test@testing.com")
    assert test_user.id == 1
    assert test_user.username == "test_username"
    assert test_user.email_address == "test@testing.com"

"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    test_user = User(1, 'test_username', 'test@testing.com')
    assert str(test_user) == "User(1, test_username, test@testing.com)"

"""
We can compare two identical users
And have them be equal - even if different instantiations
"""
def test_users_are_equal():
    test_user1 = User(1, "test_username", "test@testing.com")
    test_user2 = User(1, "test_username", "test@testing.com")
    assert test_user1 == test_user2

