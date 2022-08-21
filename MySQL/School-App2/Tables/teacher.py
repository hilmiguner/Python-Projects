class Teacher:
    def __init__(self, id, branch, name, sname, birthdate, gender) -> None:
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.sname = sname
        self.birthdate = birthdate
        self.gender = gender