#This is first coding assignment for Algorithms II from Stanford Lagunita
#The task is to implement max space clustering using union-find
#And produce the largest number of clusters such that max-spacing is 3
#With the caveat that the dataset is so large that all the edges cannot be stored explicitly in memory

nodes = {}
with open("clustering_big.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) != 2:
            intline = []
            for char in splitline:
                intline.append(int(char))
            nodes[line] = intline

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

def generateDifferences(length, differences):
    if differences == 0:
        yield [0]*length
    elif length == differences:
        yield [1]*length
    else:
        for i in generateDifferences(length-1, differences):
            yield [0] + i
        for i in generateDifferences(length-1, differences-1):
            yield [1] + i
            
def neighbors(node, distance):
    differences = generateDifferences(len(node), distance)
    neighbors = []
    for dif in differences:
        neighbors.append(list(map(lambda x, y: x ^ y, dif, node)))
    return neighbors

print(neighbors([1, 1, 0, 0], 1))
            
def kruskalClustering(nodes, maxSpacing):
    disjointSets = []
    for node in nodes:
        disjointSets.append(disjointSet(node))
    clusters = len(nodes)
    for edge in edges:
        node1 = nodes[edge[1]]
        node2 = nodes[edge[2]]
        if node1.find() != node2.find():
            if clusters <= numClusters:
                spacing = edge[0]
                return spacing
            node1.union(node2)
            clusters -= 1