class Node:
    size = 0
    def __init__(self, value) -> None:
        self.value = value
        self.nextNode = None
        Node.size += 1 