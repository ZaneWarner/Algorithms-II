#This is first coding assignment for Algorithms II from Stanford Lagunita
#The task is to implement a greedy algorithm for scheduling tasks to minimize a weighted sum of completion times
#It is not guaranteed to compute an optimal solution

x = []
with open("jobs.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) == 2:
            weight = int(splitline[0])
            length = int(splitline[1])
            print("weight {}, length {}".format(weight, length))
            x.append(weight - length)
        
print(x)