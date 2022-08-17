from datetime import datetime
from connection import connection
import mysql.connector

class Student:
    connection = connection
    cursor = connection.cursor()

    def __init__(self, sno, name, sname, birthdate, gender) -> None:
        self.sno = sno
        self.name = name
        self.sname = sname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO students (no, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        value = (self.sno, self.name, self.sname, self.birthdate, self.gender)
        Student.cursor.execute(sql, value)

        try:
            Student.connection.commit()
            print("Kaydınız yapıldı.")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kesildi.")

    @staticmethod
    def saveStudents(values):
        sql = "INSERT INTO students (no, name, surname, birthdate, gender) VALUES (%s, %s, %s, %s, %s)"
        Student.cursor.executemany(sql, values)

        try:
            Student.connection.commit()
            print(f"{Student.cursor.rowcount} adet kayıt yapıldı.")
            print(f"Son yapılan kayıtın ID numarası -> {Student.cursor.lastrowid}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()
            print("Database bağlantısı kesildi.")
        
# Tek kayıt eklemek için.
# ahmet = Student("102", "Ahmet", "Yılmaz", datetime(2005, 5, 17), "E")
# ahmet.saveStudent()

# Birden fazla kayıt eklemek için.
ogrenciler = [
    ("501","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("502","Ali","Can",datetime(2005, 6, 17),"E"),
    ("503","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("504","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("505","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("506","Ali","Cenk",datetime(2003, 8, 25),"E")
]
Student.saveStudents(ogrenciler)