from BST import BST

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