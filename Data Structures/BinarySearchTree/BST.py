from BSTNode import Node

class BST:
    size = 0
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        """
        Returns 'True' if node was successfully inserted.
        Returns 'False' if node was not successfully inserted. 
        """
        newNode = Node(value)
        if not self.root:
            self.root = newNode
            BST.size += 1
            return True
        else:
            temp = self.root
            while True:
                if newNode.value == temp.value:
                    return False
                elif newNode.value < temp.value:
                    if not temp.left:
                        temp.left = newNode
                        BST.size += 1
                        return True
                    temp = temp.left
                elif newNode.value > temp.value:
                    if not temp.right:
                        temp.right = newNode
                        BST.size += 1
                        return True
                    temp = temp.right
    
    def isContains(self, value):
        """
        Returns 'True' if BST contains the value.
        Returns 'False' if BST doesn't contain the value. 
        """
        if not self.root:
            return False
        temp = self.root
        while temp:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False
    
    def minimumNode(self):
        if not self.root:
            return -1
        temp = self.root
        while temp.left:
            temp = temp.left
        return temp

    def minimumValue(self):
        return self.minimumNode().value

    def maximumNode(self):
        if not self.root:
            return -1
        temp = self.root
        while temp.right:
            temp = temp.right
        return temp

    def maximumValue(self):
        return self.maximumNode().value
    
    

