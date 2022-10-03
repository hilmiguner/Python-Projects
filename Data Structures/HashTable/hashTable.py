class HashTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.myTable = [None] * self.size

    def __str__(self) -> str:
        print(self.myTable, end="")
        return ""

    def hashFunction(self, key):
        myHash = 0
        for letter in key:
            myHash += ord(letter) * 13
        return myHash % self.size

    def addItem(self, key, value):
        ix = self.hashFunction(key)
        if not self.myTable[ix]:
            self.myTable[ix] = []
        self.myTable[ix].append([key, value])

    def getItem(self, key):
        ix = self.hashFunction(key)
        if self.myTable[ix]:
            for i in self.myTable[ix]:
                if i[0] is key:
                    return i[1]
        return None
    
    def getKeys(self):
        keys = []
        for i in self.myTable:
            if i:
                for k in i:
                    keys.append(k[0])
        return keys