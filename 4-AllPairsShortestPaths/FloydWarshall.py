#This is fourth coding assignment for Algorithms II from Stanford Lagunita
#The task is to compute all-pairs shortest paths on a sequence of graphs and report the shortest shortest path.
#This is the implementation of the Floyd-Warshall Algorithm to serve that purpose

import numpy as np

#First, reading in data and creating an adjacency list
def makeAdjacencyList(filename):
    with open(filename, 'r') as file:
        lines = iter(file)
        vertices, edges = map(int, next(lines).split())
        adjacencyList = {}
        for line in lines:
            v1, v2, edgeLen = map(int, line.split())
            v1 -= 1
            v2 -= 1
            if v1 in adjacencyList:
                adjacencyList[v1].append((v2, edgeLen))
            else: adjacencyList[v1] = [(v2, edgeLen)]
    return adjacencyList


def FloydWarshall(G):
    numNodes = len(G)
    dp_pre = np.full((numNodes, numNodes), np.inf) #the dimensions of the dp table denote the source node and the sink node respectively
    dp_post = np.full((numNodes, numNodes), np.inf) #pre tracks the results of the prior iteration, while post tracks the ongoing one--results from smaller subproblems are not needed past this
    #Initialize base cases
    for source in G:
        dp_pre[source, source] = 0
        for neighbor in G[source]:
            node = neighbor[0]
            edgeLen = neighbor[1]
            dp_pre[source, node] = edgeLen
    #Execute the algorithm--highestNode controls subproblem size by limiting the highest (arbitrarily) numbered intermediate node allowed to be used in any path
    for highestNode in range(numNodes):
        print("highest intermediate node allowed: {}".format(highestNode))
        for source in G:
            for sink in G:
                dp_post[source, sink] = min(dp_pre[source,sink],
                                            dp_pre[source,highestNode] + dp_pre[highestNode,sink])
        dp_pre = np.copy(dp_post)
    for source in G:
        if dp_post[source, source] < 0:
            return None
    return np.amin(dp_post[:])
    
gAdj= makeAdjacencyList('g3.txt')
print(FloydWarshall(gAdj))
#g1 None
#g2 None
#g3 -19.0