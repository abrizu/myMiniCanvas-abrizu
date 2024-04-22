import pytest
from course import CourseManager, Course 
from user import User
from unittest.mock import patch, Mock

@pytest.fixture
def course_manager():
    return CourseManager()

# covered create_a_course
def test_create_a_course(course_manager):
    # Arrange
    course_manager.generate_id = Mock(return_value = 1)
    course_code = "COSC381"
    semester = "Winter"
    teacher_list = ["Sijuan Jiang", "Sample Teacher"]
    
    # Act
    course_id = course_manager.create_a_course(course_code, semester, teacher_list)
    
    # Assert
    assert course_id == 1
    assert len(course_manager.course_list) == 1
    assert course_manager.course_list[0].course_id == 1

# # HANDLES EMPTY COURSE TO RETURN FULL COVERAGE
def test_create_a_course_empty_values(course_manager):
    # Arrange
    course_code = ""
    semester = "Winter"
    teacher_list = ["Sijuan Jiang", "Sample Teacher"]

    # Act : Assert
    with pytest.raises(ValueError, match="Invalid course code"):
        course_manager.create_a_course(course_code, semester, teacher_list)

    # Arrange
    course_code = "COSC381"
    semester = ""
    teacher_list = ["Sijuan Jiang", "Sample Teacher"]

    # Act : Assert
    with pytest.raises(ValueError, match="Invalid semester code"):
        course_manager.create_a_course(course_code, semester, teacher_list)

    # Arrange
    course_code = "COSC381"
    semester = "Winter"
    teacher_list = []

    # Act : Assert
    with pytest.raises(ValueError, match="Invalid teacher list"):
        course_manager.create_a_course(course_code, semester, teacher_list)

# covered generate_id
def test_generate_id(course_manager):
    # Act
    id1 = course_manager.generate_id()
    id2 = course_manager.generate_id()
    
    # Assert
    assert id1 == 1
    assert id2 == 2

# covered find_a_course
def test_find_a_course(course_manager, mock_course):
    # Arrange
    mock_course.course_id = 1
    course_manager.course_list.append(mock_course)
    
    # Act
    found_course = course_manager.find_a_course(1)
    
    # Assert
    assert found_course == mock_course

# covered if course doesnt exist
def test_find_nonexistent_course(course_manager):
    # Arrange
    course_id = 9999
    
    # Act
    found_course = course_manager.find_a_course(course_id)
    
    # Assert
    assert found_course is None

# sync_with_database temp covered to cover course.py
# returns 100% coverage on test_course.py but 95% without this test method

def test_sync_with_database():
    # Arrange
    course_manager = CourseManager()
    
    # Act
    result = course_manager.sync_with_database()
    
    # Assert
    assert result is None 

@pytest.fixture
def mock_course():
    return Mock(spec=Course)

# covered import_students
def test_import_students():
    # Arrange
    course = Course(1, "COSC381", "Winter", ["Student 1", "Student 2"])
    students = ["John", "Alice", "Jimmy"]
    
    # Act
    admin_user = User(user_id=1, name="Admin", password="password123", type="admin")
    
    course.import_students(admin_user, students)
    
    # Assert
    assert course.student_list == students

    # Assert : non admin
    non_admin_user = User(user_id=2, name="Student", password="password", type="student")
    with pytest.raises(PermissionError):
        course.import_students(non_admin_user, ["John", "Alice", "Jimmy"])

# covered create_an_assignment
def test_create_an_assignment():
    # Arrange
    course = Course(1, "COSC381", "Winter", ["Student 1", "Student 2"])
    due_date = "2024-04-22"
    
    # Act
    course.create_an_assignment(due_date)
    
    # Assert
    assert len(course.assignment_list) == 1
    assert course.assignment_list[0].due_date == due_date

# covered generate_assignment_id
def test_generate_assignment_id():
    # Arrange
    course = Course(1, "COSC381", "Winter", ["Student 1", "Student 2"])
    
    # Act
    assignment_id1 = course.generate_assignment_id()
    assignment_id2 = course.generate_assignment_id()
    
    # Assert
    assert assignment_id1 == 1
    assert assignment_id2 == 2

# covered course_str
def test_course_str():
    # Arrange
    course = Course(1, "COSC381", "Winter", ["Student 1", "Student 2"])
    
    admin_user = User(user_id=1, name="Admin", password="password123", type="admin")
    course.import_students(admin_user, ["John", "Alice", "Jimmy"])
    
    # Act
    result = str(course)
    
    # Assert
    assert result == "ID: 1, code: COSC381, teachers: ['Student 1', 'Student 2']. students: ['John', 'Alice', 'Jimmy']"

# returned coverage (current status)
# Name                 Stmts   Miss  Cover
# ----------------------------------------
# assignment.py           13      0   100%
# course.py               49      0   100%
# main.py                 29     12    59%
# test_assignment.py      11      0   100%
# test_course.py          74      0   100%
# test_main.py             3      0   100%
# test_user.py             0      0   100%
# user.py                 25      6    76%
# ----------------------------------------
# TOTAL                  204     18    91%