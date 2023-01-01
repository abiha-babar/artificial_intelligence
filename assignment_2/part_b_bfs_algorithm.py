#dfs
from collections import defaultdict, deque
class Graph:

    def __init__(self): #constructor
        self.graph = defaultdict(list)
        # print("instructor called")
    
    def addEdge(self,u,v):
        self.graph[u].append(v) # {0:[1,2],1:[2],2:[0,3],3:[3]}
        # print(self.graph)
    
    def DFS(self,s):
        visited = set()
        self.DFSlop(s, visited)
    
    def DFSlop(self,s,visited):
        visited.add(s)

        print(str(s) + " ", end="")
        for edge in self.graph[s]:
            if edge not in visited:
                print("edges", edge)
                print("visited", visited)
                self.DFSlop(edge, visited)

    def BFS(self, s):
        visited = set()
        queue = [s]
        self.BFSloop(queue, visited)

    def BFSloop(self, queue, visited):
        while queue:
            key = queue[0]
            print(str(key) + " ", end="")

            queue = queue[1:] # removed element from queue

            for edge in self.graph[key]:
                if edge not in visited:
                    visited.add(edge)
                    queue.append(edge)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 6)
g.addEdge(1, 6)
g.addEdge(1, 9)
g.addEdge(1, 13)
g.addEdge(1, 4)
g.addEdge(2, 17)
g.addEdge(2, 0)
g.addEdge(3, 11)
g.addEdge(4, 7)
g.addEdge(4, 8)


g.BFS(0)


