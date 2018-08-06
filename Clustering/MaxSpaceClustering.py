clusterDataSmall = []
with open("clustering1txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) == 3:
            v1 = int(splitline[0])-1
            v2 = int(splitline[1])-1
            edgeLength = int(splitline[2])
            clusterDataSmall.append([v1, v2, edgeLength])