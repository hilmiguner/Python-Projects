class Student:
    def __init__(self, id, no, name, surname, birthdate, gender, classId) -> None:
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.no = no

        #---------------------------------------------------------------------
        # CHECKING THE LENGTH OF THE NAME
        if len(name) > 45:
            raise Exception("'Name' için maksimum 45 karakter girmelisiniz.")
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------
        # CHECKING THE LENGTH OF THE SURNAME
        if len(surname) > 45:
            raise Exception("'Surname' için maksimum 45 karakter girmelisiniz.")
        #---------------------------------------------------------------------

        #---------------------------------------------------------------------
        # CHECKING THE LENGTH OF THE GENDER
        if len(gender) > 1:
            raise Exception("'Gender' için maksimum 1 karakter girmelisiniz.")
        #---------------------------------------------------------------------

        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        

        self.gender = gender
        self.classId = classId

    def __repr__(self) -> str:
        return "{},{},{},{},{},{},{}".format(self.id, self.no, self.name, self.surname, self.birthdate, self.gender, self.classId)

    @staticmethod
    def create_student(student):
        student_list = []
        if isinstance(student, tuple):
            return Student(*student)
        elif isinstance(student, list):
            for i in student:
                student_list.append(Student(*i))
        return student_list