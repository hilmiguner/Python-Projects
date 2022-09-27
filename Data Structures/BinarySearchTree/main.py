from BST import BST
from Traversals.BFS import breadthFirstSearch
from Traversals.DFS import node_left_right_traversal
from Traversals.DFS import node_right_left_raversal
from Traversals.DFS import left_node_right_traversal
from Traversals.DFS import right_node_left_traversal
from Traversals.DFS import left_right_node_traversal
from Traversals.DFS import right_left_node_traversal

bst = BST()

bst.insert(10)
bst.insert(20)
bst.insert(5)

bst.insert(2)
bst.insert(6)

bst.insert(16)
bst.insert(25)

print(bst.isContains(25))

print(bst.minimumNode())
print(bst.maximumNode())

print(bst.minimumValue())
print(bst.maximumValue())

print(f"Breadth first traversal -> {breadthFirstSearch(bst.root)}")
print(f"Depth first traversel(N-L-R) -> {node_left_right_traversal(bst.root)}")
print(f"Depth first traversel(N-R-L) -> {node_right_left_raversal(bst.root)}")
print(f"Depth first traversel(L-N-R) -> {left_node_right_traversal(bst.root)}")
print(f"Depth first traversel(R-N-L) -> {right_node_left_traversal(bst.root)}")
print(f"Depth first traversel(L-R-N) -> {left_right_node_traversal(bst.root)}")
print(f"Depth first traversel(R-L-N) -> {right_left_node_traversal(bst.root)}")
