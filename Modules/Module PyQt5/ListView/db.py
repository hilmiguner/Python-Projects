import sqlite3

class db:
    def __init__(self):
        self.connection = sqlite3.connect("Modules/Module PyQt5/ListView/names.db")
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
        print("Bağlantı koptu")