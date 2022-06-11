class Person:
    def __init__(self,n,s):
        self.name = n
        self.surname = s
        print("Person created.")
    def getName(self):
        print(self.name,self.surname)
class Student(Person):
    def __init__(self,n,s):
        Person.__init__(self,n,s)
        print("Student created.")
s1 = Student("Hilmi","Güner")
s1.getName()