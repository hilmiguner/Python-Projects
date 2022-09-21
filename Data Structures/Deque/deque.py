class Deque():
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        print(self.list, end="")
        return ""

    def addRight(self, item):
        self.list.append(item)

    def addLeft(self, item):
        self.list.insert(0, item)

    def removeRight(self):
        try:
            self.list.pop()
        except IndexError as err:
            if str(err) == "pop from empty list":
                print("Cannot remove because the deque is empty.")

    def removeLeft(self):
        try:
            self.list.pop(0)
        except IndexError as err:
            if str(err) == "pop from empty list":
                print("Cannot remove because the deque is empty.")

    def size(self):
        return len(self.list)

    def isEmpty(self) -> bool:
        return True if len(self.list) == 0 else False

    def getFront(self):
        try:
            result = self.list[-1]
            return result
        except IndexError as err:
            if str(err) == "list index out of range":
                print("There is no front element because the queue is empty.")
        
    def getRear(self):
        try:
            result = self.list[0]
            return result
        except IndexError as err:
            if str(err) == "list index out of range":
                print("There is no rear element because the queue is empty.")