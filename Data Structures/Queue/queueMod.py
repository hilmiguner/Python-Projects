class Queue():
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        print(self.list, end="")
        return ""

    def enqueue(self, item):
        self.list.insert(0, item)

    def dequeue(self):
        try:
            self.list.pop()
        except IndexError as err:
            if str(err) == "pop from empty list":
                print("Cannot pop because the queue is empty.")

    def size(self) -> int:
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