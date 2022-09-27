def breadthFirstSearch(root) -> list:
    if not root:
        return []
    currentRoot = None
    tempQueue = [root]
    resultList = []
    while tempQueue:
        currentRoot = tempQueue.pop(0)
        resultList.append(currentRoot.value)
        if currentRoot.left:
            tempQueue.append(currentRoot.left)
        if currentRoot.right:
            tempQueue.append(currentRoot.right)
    return resultList
    
