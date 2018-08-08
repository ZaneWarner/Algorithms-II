# clusterDataSmall = []
# with open("clustering1txt", 'r') as file:
#     for line in file:
#         splitline = line.split()
#         if len(splitline) == 1:
#             numNodes = int(splitline[0])
#         if len(splitline) == 3:
#             v1 = int(splitline[0])-1
#             v2 = int(splitline[1])-1
#             edgeLength = int(splitline[2])
#             clusterDataSmall.append([edgeLength, v1, v2])
            
class disjointSet():
    def __init__(self):
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
            
x1 = disjointSet()
x2 = disjointSet()
print(x1.find())
print(x2.find())
x1.union(x2)
print(x2.find())
print(x1.size)