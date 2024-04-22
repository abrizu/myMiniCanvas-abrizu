import pytest
from user import UserManager, User

@pytest.fixture
def user_manager():
    return UserManager()

# covers generate_id
def test_generate_id(user_manager):
    # Arrange, Act
    id1 = user_manager.generate_id()
    id2 = user_manager.generate_id()

    # Assert
    assert id1 == 1
    assert id2 == 2

# covers create_a_user
def test_create_a_user(user_manager):
    # Arrange
    name = "Joe"
    password = "password"
    type = "student"

    # Act
    user_manager.create_a_user(name, password, type)
    
    # Assert
    assert len(user_manager.user_list) == 1
    assert user_manager.user_list[0].name == name
    assert user_manager.user_list[0].password == password
    assert user_manager.user_list[0].type == type

# covers find_users
def test_find_users(user_manager):
    # Arrange
    user_manager.create_a_user("Joe", "pwd", "student")
    user_manager.create_a_user("Jim", "pass", "teacher")
    
    # Act
    found_users = user_manager.find_users([1, 2])
    
    # Assert
    assert len(found_users) == 2
    assert found_users[0].name == "Joe"
    assert found_users[1].name == "Jim"

# covers __str__
def test_user_str():
    # Arrange
    user = User(1, "John", "password", "student")
    
    # Act
    result = str(user)
    
    # Assert
    assert result == "ID: 1, name: John, type: student"

# returned coverage (current status)
# Name                 Stmts   Miss  Cover
# ----------------------------------------
# assignment.py           13      0   100%
# course.py               49      0   100%
# main.py                 29     12    59%
# test_assignment.py      27      0   100%
# test_course.py          74      0   100%
# test_main.py             3      0   100%
# test_user.py            30      0   100%
# user.py                 25      0   100%
# ----------------------------------------
# TOTAL                  250     12    95%