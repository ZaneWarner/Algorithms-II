#This is first coding assignment for Algorithms II from Stanford Lagunita
#The task is to implement max space clustering using union-find
#And produce the largest number of clusters such that max-spacing is 3
#With the caveat that the dataset is so large that all the edges cannot be stored explicitly in memory

nodes = []
with open("clustering_big.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) != 2:
            line = line[:-2]
            nodes.append(line)
            
nodes.sort()

class disjointSet():
    def __init__(self, nodekey):
        self.nodekey = nodekey
        self.node = list(map(int, nodekey.split()))
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
            
def calculateNeighbors(node, distance):
    differences = generateDifferences(len(node), distance)
    neighbors = []
    for dif in differences:
        neighbor = (list(map(lambda x, y: x ^ y, dif, node)))
        neighbors.append(" ".join(list(map(str, neighbor))))
    return neighbors
            
def kruskalClustering(nodes):
    clusters = len(nodes)
    duplications = 0
    disjointSets = {}
    for node in nodes:
        if node not in disjointSets:
            disjointSets[node] = disjointSet(node)
        else:
            clusters -= 1
            duplications += 1
            print("duplications {}".format(duplications))
    for key in nodes:
        currentSet = disjointSets[key]
        neighbors = calculateNeighbors(currentSet.node, 1) + calculateNeighbors(currentSet.node, 2) 
        for neighborKey in neighbors:
            if neighborKey > currentSet.nodekey:
                if neighborKey in disjointSets:
                    neighbor = disjointSets[neighborKey]
                    if currentSet.find() != neighbor.find():
                        currentSet.union(neighbor)
                        clusters -= 1
                        if clusters % 100  == 0:
                            print("clusters remaining: {}".format(clusters))
    return clusters
    
print(kruskalClustering(nodes))

                    