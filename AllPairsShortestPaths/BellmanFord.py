#This is fourth coding assignment for Algorithms II from Stanford Lagunita
#The task is to compute all-pairs shortest paths on a sequence of graphs and report the shortest shortest path.
#As an additional challenge, I will be implementing all of Bellman-Ford, Floyd-Warshall, and Johnson's algorithms to do this
#This is the implementation of Bellman-Ford

#First, reading in data and creating an adjacency list
def makeAdjacencyList(filename):
    with open(filename, 'r') as file:
        lines = iter(file)
        vertices, edges = map(int, next(lines).split())
        adjacencyList = {}
        for line in lines:
            v1, v2, len = map(int, line.split())
            v1 -= 1
            v2 -= 1
            if v1 in adjacencyList:
                adjacencyList[v1].append((v2, len))
            else: adjacencyList[v1] = [(v2, len)]
            if v2 in adjacencyList:
                adjacencyList[v2].append((v1, len))
            else: adjacencyList[v2] = [(v1, len)]
    return adjacencyList
    
g1adj = makeAdjacencyList('g1.txt')
print(g1adj[0])