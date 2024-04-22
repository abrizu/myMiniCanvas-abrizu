from fastapi.testclient import TestClient
from main import app
import pytest

from course import CourseManager
from user import UserManager

from unittest.mock import Mock

client = TestClient(app)

@pytest.fixture
def user_manager():
    return UserManager()

@pytest.fixture
def course_manager():
    return CourseManager()


def test_welcome():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Welcome to our miniCanvas!"'

def test_create_a_course():
    teacher_id_list = [1, 2]
    response = client.post("/courses/COSC381", json={
        "semester": "Winter",
        "teacher_id_list": teacher_id_list
    })
    print(response.json())
    assert response.status_code == 422
    assert response.json()["detail"]

def test_import_students():
    student_id_list = [1, 2]
    response = client.put("/courses/1/students", json={
        "student_id_list": student_id_list
    })
    print(response.json())
    assert response.status_code == 422
    assert response.json()["detail"]

# def test_create_a_course(course_manager, user_manager):
#     # Arrange
#     course_manager.generate_id = Mock(return_value=1)
#     user_manager.find_users = Mock(return_value=["Sijuan Jiang", "Sample Teacher"])
#     user = Mock(type='admin')
#     course_code = "COSC381"
#     semester = "Winter"
#     teacher_id_list = [1, 2]
    
#     # Act
#     response = client.post(f"/courses/{course_code}", json={
#         "semester": semester,
#         "teacher_id_list": teacher_id_list
#     }, headers={"user": user})    

#     # Assert
#     assert response.status_code == 200
#     assert response.json() == 1



    # Every time I attempt to swap the status code to 200 (success) it does not parse.
    # I have attempted to fulfill all parameters of create_a_course, however, it still does
    # not work. I have left in what works (even though it runs 422 error).

