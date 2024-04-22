import pytest
from assignment import Assignment, Submission

@pytest.fixture
def assignment():
    return Assignment(1, "2024-04-22", 381)

# covered init in assignment 
def test_assignment_init():
    # Arrange
    assignment_id = 1
    due_date = "2024-04-22"
    course_id = 381
    
    # Act
    assignment = Assignment(assignment_id, due_date, course_id)
    
    # Assert
    assert assignment.assignment_id == assignment_id
    assert assignment.due_date == due_date
    assert assignment.course_id == course_id
    assert assignment.submission_list == []

# covered submit in assignment
def test_submit(assignment):
    # Arrange
    submission = Submission(1, "Submission 1")
    
    # Act
    assignment.submit(submission)
    
    # Assert
    assert submission in assignment.submission_list
    assert len(assignment.submission_list) == 1
    assert assignment.submission_list[0] == submission

# covered init in submission 
def test_submission_init():
    # Arrange
    student_id = 1
    content = "Test content"
    
    # Act
    submission = Submission(student_id, content)
    
    # Assert
    assert submission.student_id == student_id
    assert submission.submission == content
    assert submission.grade == -1.0

# returned coverage (current status)
# Name                 Stmts   Miss  Cover
# ----------------------------------------
# assignment.py           13      0   100%
# course.py               49      0   100%
# main.py                 29     12    59%
# test_assignment.py      27      0   100%
# test_course.py          74      0   100%
# test_main.py             3      0   100%
# test_user.py             0      0   100%
# user.py                 25      6    76%
# ----------------------------------------
# TOTAL                  220     18    92%