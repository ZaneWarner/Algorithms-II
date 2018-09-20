#This is second coding assignment for Algorithms II from Stanford Lagunita
#The task is to implement a greedy algorithm for scheduling tasks to minimize a weighted sum of completion times
#We sort tasks by weight/length
#It is guaranteed to compute an optimal solution

x = []
with open("jobs.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) == 2:
            weight = int(splitline[0])
            length = int(splitline[1])
            x.append([weight/length, weight, length])

x.sort()
x.reverse()
print(x)

def calculateWeightedCompletionTime(x):
    time = 0
    weightedCompletionTime = 0
    for job in x:
        time += job[2]
        weightedCompletionTime += job[1]*time
    return weightedCompletionTime   

weightedCompletionTime = calculateWeightedCompletionTime(x)
print(weightedCompletionTime)