#This is first coding assignment for Algorithms II from Stanford Lagunita
#The task is to implement max space clustering using union-find
#And produce the max-spacing of 4 clusters in a small dataset

clusterDataSmall = []
with open("clustering1.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) == 1:
            numNodes = int(splitline[0])
        if len(splitline) == 3:
            v1 = int(splitline[0])-1
            v2 = int(splitline[1])-1
            edgeLength = int(splitline[2])
            clusterDataSmall.append([edgeLength, v1, v2])

class disjointSet():
    def __init__(self, node):
        self.node = node
        self.parent = self
        self.size = 1
        
    def find(self):
        if self.parent.parent == self.parent:
            return self.parent
        else: 
            leader = self.parent.find()
            self.parent = leader
            return leader
        
    def union(self, otherSet):
        otherLeader = otherSet.find()
        leader = self.find()
        if leader.size >= otherLeader.size:
            otherLeader.parent = leader
            leader.size += otherLeader.size
        else:
            leader.parent = otherLeader
            otherLeader.size += leader.size
            
def kruskalClustering(edges, numNodes,numClusters):
    edges.sort()
    nodes = []
    for node in range(numNodes):
        nodes.append(disjointSet(node))
    clusters = numNodes
    for edge in edges:
        node1 = nodes[edge[1]]
        node2 = nodes[edge[2]]
        if node1.find() != node2.find():
            if clusters <= numClusters:
                spacing = edge[0]
                return spacing
            node1.union(node2)
            clusters -= 1
            
spacing = kruskalClustering(clusterDataSmall, numNodes, 4)
print(spacing)
          
