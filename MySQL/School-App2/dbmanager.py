import mysql.connector
from connection import connection
from Tables.student import Student
from Tables.teacher import Teacher

class DBManager:
    def __init__(self) -> None:
        self.connection = connection
        self.cursor = self.connection.cursor()
    
    def __del__(self) -> None:
        try:
            self.connection.disconnect()
            print("Connection with database has been successfully disconnected.")
        except mysql.connector.Error as err:
            print("Error has been occured while trying to disconnect the connection to database ->", err)

    def add_student(self, student: Student):
        sql = "INSERT INTO student (no, name, surname, birthdate, gender, classId) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (student.no, student.name, student.surname, student.birthdate, student.gender, student.classId)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"Entry with {self.cursor.lastrowid} id has been registered.")
        except mysql.connector.errors.Error as err:
            print("Error has been occured ->", err)

    def edit_student(self, student: Student):
        sql = "UPDATE student SET no=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classId=%s WHERE id=%s"
        values = (*str(student).split(",")[1:], student.id)
        self.cursor.execute(sql, values)
        try:
            self.connection.commit()
            print(f"The entry has been updated successfully.")
        except mysql.connector.Error as err:
            print("Error has been occured ->", err)
    
    def get_all_students(self):
        sql = "SELECT * FROM (student INNER JOIN class ON student.classId=class.id) LEFT JOIN teacher ON class.teacherId=teacher.id ORDER BY student.id"
        self.cursor.execute(sql)
        student_list = []
        try:
            students = self.cursor.fetchall()
            if students is not None:
                for student in students:
                    student_list.append(student)
                return student_list
        except mysql.connector.Error as err:
            print("Error has been occured ->", err)

    def get_student_by_id(self, id: int) -> Student:
        sql = "SELECT * FROM student WHERE id=%s"
        self.cursor.execute(sql, [id])
        try:
            student = self.cursor.fetchone()
            if student is not None:
                return Student.create_student(student)
        except mysql.connector.Error as err:
            print("Error has been occured ->", err)

    def get_students_by_class_id(self, classId: int) -> list:
        sql = "SELECT * FROM student WHERE classId=%s"
        self.cursor.execute(sql, [classId])
        try:
            students = self.cursor.fetchall()
            if students is not None:
                return Student.create_student(students)
        except mysql.connector.Error as err:
            print("Error has been occured ->", err)

    def del_student(self, id: int):
        sql = "DELETE FROM student WHERE id=%s"
        self.cursor.execute(sql, [id])
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} registry has been deleted from table.")
        except mysql.connector.errors.Error as err:
            print("Error ->", err)

    def add_teacher(self, teacher: Teacher):
        sql = "INSERT INTO teacher (id, branch, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s, %s)"
        value = (teacher.id, teacher.branch, teacher.name, teacher.surname, teacher.birthdate, teacher.gender)
        self.cursor.execute(sql, value)
        try:
            self.connection.commit()
            print(f"Entry with {self.cursor.lastrowid} id has been registered.")
        except mysql.connector.errors.Error as err:
            print("Error has been occured ->", err)
    
    def edit_teacher(self, teacher: Teacher):
        pass
