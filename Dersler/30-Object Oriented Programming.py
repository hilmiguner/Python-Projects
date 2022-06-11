#class
class Person:
    # attributes
    address = "no information"

    # constructor
    def __init__(self,n,by):
        self.name = n
        self.birthyear = by
        print("Constructor method worked.")

    # methods
    def getAddress(self):
        self.address = input("Please enter your address:")

    def calculateAge(self):
        self.age = 2021 - self.birthyear
        return self.age

#object
p1 = Person("Hilmi",2001)
p1.getAddress()
print(f"Name : {p1.name}, birthyear : {p1.birthyear}, age : {p1.calculateAge()}, address : {p1.address}")