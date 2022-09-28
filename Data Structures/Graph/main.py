from hmac import digest
from graph import DirectionalGraph

diGraph1 = DirectionalGraph()

diGraph1.addVertex("A")
diGraph1.addVertex("B")
diGraph1.addVertex("C")
diGraph1.addVertex("D")
diGraph1.addVertex("E")

diGraph1.addEdge("A", "B")
diGraph1.addEdge("A", "E")
diGraph1.addEdge("B", "E")
diGraph1.addEdge("B", "D")
diGraph1.addEdge("B", "C")
diGraph1.addEdge("C", "D")
diGraph1.addEdge("D", "E")

print(diGraph1)

diGraph1.removeEdge("E", "B")
diGraph1.removeVertex("C")

print(diGraph1)