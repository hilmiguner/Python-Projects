import json
import os.path


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = None

    def loadUser(self):
        liste = []
        newDict = {}
        if os.path.exists("users.json"):
            with open("users.json", "r", encoding="utf-8") as file:
                liste = json.load(file)
            for i in liste:
                newDict = json.loads(i)
                newUser = User(newDict["username"], newDict["password"], newDict["email"])
                self.users.append(newUser)

    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanıcı oluşturuldu.")

    def login(self, username, password):
        for i in self.users:
            if i.username == username and i.password == password:
                self.isLoggedIn = True
                self.currentUser = i
                print("Giriş yapıldı.")
                break
        if not self.isLoggedIn:
            print("Giriş yapılamadı.")
    def saveToFile(self):
        liste = []

        for i in self.users:
            liste.append(json.dumps(i.__dict__))

        with open("users.json", "w") as file:
            json.dump(liste, file)

    def logOut(self):
        if self.isLoggedIn:
            self.currentUser = {}
            self.isLoggedIn = False
            print("Çıkış yapıldı.")
        else:
            print("Şu anda herhangi bir hesap etkin değil.")

    def printIdentity(self):
        if self.isLoggedIn:
            print("Username:", self.currentUser.username, "\nPassword:", self.currentUser.password, "\nEmail:", self.currentUser.email)
        else:
            print("Şu anda açık olan bir hesap yok.")

repistory = UserRepository()
repistory.loadUser()

while True:
    print("Menü".center(50, "*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz: ")
    if secim == '5':
        break
    else:
        if secim == '1':
            username = input("Username: ")
            password = input("Password: ")
            email = input("Email: ")
            user = User(username, password, email)
            repistory.register(user)
        elif secim == '2':
            if not repistory.isLoggedIn:
                username = input("Username: ")
                password = input("Password: ")
                repistory.login(username, password)
            else:
                print("Yeni bir hesaba giriş yapmak için şu an ki hesabınızdan çıkış yapınız.")
        elif secim == '3':
            repistory.logOut()
        elif secim == '4':
            repistory.printIdentity()
