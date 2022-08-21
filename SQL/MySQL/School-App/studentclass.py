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
        Student.connection.connect()
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
        Student.connection.connect()
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

    @staticmethod
    def get_all_students():
        Student.connection.connect()
        Student.cursor.execute("SELECT * FROM students")
        result = -1
        try:
            result = Student.cursor.fetchall()
            if len(result) == 0:
                print("Successfully fetched students but there is no student in database.")
            else:
                for student in result:
                    print(f"Id: {student[0]}, No: {student[1]}, Name: {student[2]}, Surname: {student[3]}, Birthday: {student[4]}, Gender: {student[5]}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()

    @staticmethod
    def get_all_students_specify(*args):
        Student.connection.connect()
        if len(args) != 0:
            str = "SELECT " + (",".join(args)) + " FROM students"
            Student.cursor.execute(str)
            result = -1
            try:
                result = Student.cursor.fetchall()
                if len(result) == 0:
                    print("Successfully fetched students but there is no student in database.")
                else:
                    temp = []
                    for i in args:
                        if i == "id":
                            temp.append(0)
                        elif i == "no":
                            temp.append(1)
                        elif i == "name":
                            temp.append(2)
                        elif i == "surname":
                            temp.append(3)
                        elif i == "birthdate":
                            temp.append(4)
                        elif i == "gender":
                            temp.append(5)      
                    str2 = ": {}, ".join(args) + ": {}"
                    temp1 = []
                    for i in result:
                        for k in i:
                            temp1.append(k)
                        print(str2.format(*temp1))
                        temp1.clear()
            except mysql.connector.errors.Error as err:
                print("Hata ->", err)
            finally:
                Student.connection.close()
        else:
            Student.get_all_students()

    @staticmethod
    def get_all_girls_name_surname():
        Student.connection.connect()
        sql = "SELECT name,surname FROM students WHERE gender='K'"
        Student.cursor.execute(sql)
        try:
            result = Student.cursor.fetchall()
            if len(result) == 0:
                print("Successfully fetched students but there is no student in database.")
            else:
                for student in result:
                    print(f"Name: {student[0]}, Surname: {student[1]}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()

    @staticmethod
    def get_all_students_by_birthyear(year: int):
        Student.connection.connect()
        sql = "SELECT * FROM students WHERE YEAR(birthdate)=%s"
        Student.cursor.execute(sql, [year])
        try:
            result = Student.cursor.fetchall()
            if len(result) == 0:
                print("Successfully fetched students but there is no student in database.")
            else:
                for student in result:
                    print(f"Id: {student[0]}, No: {student[1]}, Name: {student[2]}, Surname: {student[3]}, Birthday: {student[4]}, Gender: {student[5]}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()

    @staticmethod
    def get_students_by_name_and_birthyear(name: str, year: int):
        Student.connection.connect()
        sql = "SELECT * FROM students WHERE YEAR(birthdate)=%s and name=%s"
        Student.cursor.execute(sql, [year, name])
        try:
            result = Student.cursor.fetchall()
            if len(result) == 0:
                print("Successfully fetched students but there is no student in database.")
            else:
                for student in result:
                    print(f"Id: {student[0]}, No: {student[1]}, Name: {student[2]}, Surname: {student[3]}, Birthday: {student[4]}, Gender: {student[5]}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()
    
    @staticmethod
    def get_students_by_including_txt_in_name_or_surname(txt: str):
        Student.connection.connect()
        sql = "SELECT * FROM students WHERE name LIKE '%{}%' or surname LIKE '%{}%'"
        sql = sql.format(txt, txt)
        Student.cursor.execute(sql)
        try:
            result = Student.cursor.fetchall()
            if len(result) == 0:
                print("Successfully fetched students but there is no student in database.")
            else:
                for student in result:
                    print(f"Id: {student[0]}, No: {student[1]}, Name: {student[2]}, Surname: {student[3]}, Birthday: {student[4]}, Gender: {student[5]}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()

    @staticmethod
    def get_student_number_by_gender(gender: str):
        Student.connection.connect()
        sql = "SELECT COUNT(*) FROM students WHERE gender=%s"
        Student.cursor.execute(sql, [gender])
        result = -1
        try:
            result = Student.cursor.fetchone()
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()
            return result

    @staticmethod
    def get_girls_by_name_order():
        Student.connection.connect()
        sql = "SELECT * FROM students WHERE gender='K' ORDER BY name"
        Student.cursor.execute(sql)
        try:
            result = Student.cursor.fetchall()
            if len(result) == 0:
                print("Successfully fetched students but there is no student in database.")
            else:
                for student in result:
                    print(f"Id: {student[0]}, No: {student[1]}, Name: {student[2]}, Surname: {student[3]}, Birthday: {student[4]}, Gender: {student[5]}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()

    @staticmethod
    def get_students_by_limit(limit: int):
        Student.connection.connect()
        sql = "SELECT * FROM students LIMIT %s"
        Student.cursor.execute(sql, [limit])
        try:
            result = Student.cursor.fetchall()
            if len(result) == 0:
                print("Successfully fetched students but there is no student in database.")
            else:
                for student in result:
                    print(f"Id: {student[0]}, No: {student[1]}, Name: {student[2]}, Surname: {student[3]}, Birthday: {student[4]}, Gender: {student[5]}")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()

    @staticmethod
    def set_student_by_id(id, **kwargs):
        Student.connection.connect()
        list1 = []
        for i in kwargs.keys():
            list1.append("{}=%s".format(str(i)))
        sql = "UPDATE students SET " + ",".join(list1) + " WHERE id=%s"
        list2 = []
        for key, value in kwargs.items():
            list2.append(str(value))
        Student.cursor.execute(sql, [*list2, id])
        try:
            Student.connection.commit()
            print("Informations successfully are changed.")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()

    @staticmethod
    def set_student_by_gender(gender, **kwargs):
        Student.connection.connect()
        list1 = []
        for i in kwargs.keys():
            list1.append("{}=%s".format(str(i)))
        sql = "UPDATE students SET " + ",".join(list1) + " WHERE gender=%s"
        list2 = []
        for key, value in kwargs.items():
            list2.append(str(value))
        Student.cursor.execute(sql, [*list2, gender])
        try:
            Student.connection.commit()
            print("Informations successfully are changed.")
        except mysql.connector.errors.Error as err:
            print("Hata ->", err)
        finally:
            Student.connection.close()