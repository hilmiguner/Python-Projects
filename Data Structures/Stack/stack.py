class Stack():
    def __init__(self):
        self.list = []

    def __str__(self) -> str:
        print(self.list, end="")
        return ""
    
    def push(self, item):
        self.list.append(item)

    def pop(self):
        try:
            self.list.pop()
        except IndexError as err:
            if str(err) == "pop from empty list":
                print("Cannot pop because stack is empty.")

    def getLast(self):
        return self.list[-1]
    
    def size(self):
        return len(self.list)

    def isEmpty(self) -> bool:
        return True if len(self.list) == 0 else False 