from datetime import datetime
from dbmanager import DBManager
from Tables.student import Student

dbmanager = DBManager()

# student = dbmanager.get_student_by_id(5)
# print(student.name, student.surname)

# students = dbmanager.get_students_by_class_id(3)
# for student in students:
#     print(student.name, student.surname)

# dbmanager.add_student(Student(None, 1747, "Hilmi", "Güner", datetime(2001, 2, 15, 0, 0, 0, 0), "E", 1))

# dbmanager.edit_student(Student(7, 102, "Ahmet", "Kara", datetime(2005, 2, 20, 0, 0, 0, 0), "E", 2))