
from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.graph = defaultdict(list)
        self.E = edges

    def addEdge(self, x, e):
        self.graph[x].append(e)

    def traverse_Sort(self, e, traverse, stack):
        traverse[e] = True
        for k in self.graph[e]:
            if traverse[k] == False:
                self.traverse_Sort(k, traverse, stack)
        stack.append(e)

    def traverseStack(self):
        traverse = [False] * self.E
        stack = []

        for k in range(self.E):
            if traverse[k] == False:
                self.traverse_Sort(k, traverse, stack)
            print(stack[::-1])


g = Graph(8)
g.addEdge(5, 6)
g.addEdge(5, 7)
g.addEdge(9, 8)
g.addEdge(9, 15)
g.addEdge(9, 11)
g.addEdge(7, 5)

print("Following is a path for the graph")
g.traverseStack()
