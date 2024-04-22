from fastapi import FastAPI, HTTPException
from typing import List
from course import CourseManager
from user import UserManager, User
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

coursemanager = CourseManager()
usermanager = UserManager()

usermanager.create_a_user("John", "pwd", "student")
usermanager.create_a_user("Alice", "pwd", "teacher")
usermanager.create_a_user("Jimmy", "pwd", "admin")

class CreateCourseRequest(BaseModel):
    semester: str
    teacher_id_list: List[int]

class ImportStudentsRequest(BaseModel):
    student_id_list: List[int]

app = FastAPI()

@app.get("/")
def welcome():
    return "Welcome to our miniCanvas!"

@app.post("/courses/{coursecode}", response_model=CreateCourseRequest)
def create_a_course(coursecode: str, 
                    semester: str, 
                    teacher_id_list: List[int], user) -> int:
    ### an admin should create a course
    teacher_list = usermanager.find_users(teacher_id_list)

    if user.type != 'admin':
        raise PermissionError("Only admin users can import students.")
    
    course_id = coursemanager.create_a_course(coursecode, semester, teacher_list)
    
    course = coursemanager.find_a_course(course_id)
    print(str(course.teacher_list[0]))

    return course_id

@app.put("/courses/{courseid}/students", response_model=ImportStudentsRequest)
def import_students(courseid: int,
                    student_id_list: List[int]) -> None:
    course = coursemanager.find_a_course(courseid)
    student_list = usermanager.find_users(student_id_list)
    course.import_students(student_list)
    
    print(course.course_id)
    print(course.student_list)
    
    return None