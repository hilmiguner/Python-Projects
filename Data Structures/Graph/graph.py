class DirectionalGraph:
    def __init__(self) -> None:
        self.adjDict = {}

    def __str__(self) -> str:
        if not self.adjDict:
            print("There is no vertex.")
            return ""
        for vertex in self.adjDict:
            print(f"Edge(s) of {vertex} are/is {self.adjDict[vertex]}")
        return ""
        
    def addVertex(self, vertex):
        """
        Returns True if vertex added successfully.\n
        Returns False if vertex couldn't added.
        """
        if vertex not in self.adjDict.keys():
            self.adjDict[vertex] = []
            return True
        return False

    def removeVertex(self, vertex):
        """
        Returns True if vertex deleted successfully.\n
        Returns False if vertex couldn't deleted.
        """
        if vertex in self.adjDict.keys():
            for i in self.adjDict:
                if vertex in self.adjDict[i]:
                    self.adjDict[i].remove(vertex)
            self.adjDict.pop(vertex)
            return True
        return False

    def addEdge(self, vertex1, vertex2):
        """
        Returns True if edge added successfully.\n
        Returns False if edge couldn't added.
        """
        if vertex1 in self.adjDict.keys() and vertex2 in self.adjDict.keys():
            self.adjDict[vertex1].append(vertex2)
            self.adjDict[vertex2].append(vertex1)
            return True
        return False

    def removeEdge(self, vertex1, vertex2, bidirectionalRemove = True):
        """
        Returns True if edge deleted successfully.\n
        Returns False if edge couldn't deleted.
        """
        if vertex1 in self.adjDict.keys() and vertex2 in self.adjDict.keys():
            try:
                self.adjDict[vertex1].remove(vertex2)
            except:
                pass
            if not bidirectionalRemove:
                try:
                    self.adjDict[vertex2].remove(vertex1)
                except:
                    pass
            return True
        return False
    

