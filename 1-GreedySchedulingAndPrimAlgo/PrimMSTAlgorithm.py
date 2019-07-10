#This is first coding assignment for Algorithms II from Stanford Lagunita
#The task is to implement a Prim's algorithm for computing a minimum spanning tree, and report the sum of its edge lengths
#Using a heap-based solution for improved performance is optional, and will be done here

import heapq

x = []
with open("edges.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) == 2:
            numNodes = int(splitline[0])
            numEdges = int(splitline[1])
        if len(splitline) == 3:
            v1 = int(splitline[0])-1
            v2 = int(splitline[1])-1
            edgeLength = int(splitline[2])
            x.append([v1, v2, edgeLength])

def makeAdjacencyList(x, numNodes):
    adjacencyList = [[]]*numNodes
    for edge in x:
        v1 = edge[0]
        v2 = edge[1]
        edgeLength = edge[2]
        adjacencyList[v1] = adjacencyList[v1] + [[v2, edgeLength]]
        adjacencyList[v2] = adjacencyList[v2] + [[v1, edgeLength]]
    return adjacencyList

adjacencyList = makeAdjacencyList(x, numNodes)

def PrimMST(adjacencyList):
    ##Init
    nodesSpanned = {0 : 1}
    edgeLengthTotal = 0
    edgesCrossingCut = []
    vertexSmallestEdges = {}
    for edge in adjacencyList[0]:
        candidateVertex = edge[0]
        candidateEdgeLength = edge[1]
        candidateEdge = [candidateEdgeLength, candidateVertex]
        if candidateVertex not in vertexSmallestEdges or vertexSmallestEdges[candidateVertex] > candidateEdgeLength:
            vertexSmallestEdges[candidateVertex] = candidateEdgeLength
            heapq.heappush(edgesCrossingCut, candidateEdge)
    ##Init Done
    while edgesCrossingCut != []:
        newEdge = heapq.heappop(edgesCrossingCut)
        newVert = newEdge[1]
        if newVert not in nodesSpanned:
            nodesSpanned[newVert] = 1
            edgeLengthTotal += newEdge[0]
            for edge in adjacencyList[newVert]:
                candidateVertex = edge[0]
                candidateEdgeLength = edge[1]
                candidateEdge = [candidateEdgeLength, candidateVertex]
                if candidateVertex not in vertexSmallestEdges or vertexSmallestEdges[candidateVertex] > candidateEdgeLength:
                    vertexSmallestEdges[candidateVertex] = candidateEdgeLength
                    heapq.heappush(edgesCrossingCut, candidateEdge)
    return edgeLengthTotal

edgeLengthSum = PrimMST(adjacencyList)
print(edgeLengthSum)