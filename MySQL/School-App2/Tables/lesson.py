class Lesson:
    def __init__(self, id, name) -> None:
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.name = name