def node_left_right_traversal(root, resultList = []):
    resultList.append(root.value)
    if root.left:
        resultList = node_left_right_traversal(root.left, resultList)
    if root.right:
        resultList = node_left_right_traversal(root.right, resultList)
    return resultList

def node_right_left_raversal(root, resultList = []):
    resultList.append(root.value)
    if root.right:
        resultList = node_right_left_raversal(root.right, resultList)
    if root.left:
        resultList = node_right_left_raversal(root.left, resultList)
    return resultList




def left_node_right_traversal(root, resultList = []):
    if root.left:
        resultList = left_node_right_traversal(root.left, resultList)
    resultList.append(root.value)
    if root.right:
        resultList = left_node_right_traversal(root.right, resultList)
    return resultList

def right_node_left_traversal(root, resultList = []):
    if root.right:
        resultList = right_node_left_traversal(root.right, resultList)
    resultList.append(root.value)
    if root.left:
        resultList = right_node_left_traversal(root.left, resultList)
    return resultList




def left_right_node_traversal(root, resultList = []):
    if root.left:
        resultList = left_right_node_traversal(root.left, resultList)
    if root.right:
        resultList = left_right_node_traversal(root.right, resultList)
    resultList.append(root.value)
    return resultList

def right_left_node_traversal(root, resultList = []):
    if root.right:
        resultList = right_left_node_traversal(root.right, resultList)
    if root.left:
        resultList = right_left_node_traversal(root.left, resultList)
    resultList.append(root.value) 
    return resultList

