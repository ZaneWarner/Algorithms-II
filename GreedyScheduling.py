#This is first coding assignment for Algorithms II from Stanford Lagunita
#The task is to implement a greedy algorithm for scheduling tasks to minimize a weighted sum of completion times
#We sort tasks by weight-length, breaking ties by scheduling higher-weight tasks first, then arbitrarily
#It is not guaranteed to compute an optimal solution

x = []
with open("jobs.txt", 'r') as file:
    for line in file:
        splitline = line.split()
        if len(splitline) == 2:
            weight = int(splitline[0])
            length = int(splitline[1])
            x.append([weight - length, weight, length])

#A special implementation of merge sort that sorts by the first index normally but the second index in reverse     
def sort(x):
    if len(x) <= 1:
        return x
    midpoint = len(x)//2
    left_x = x[:midpoint]
    right_x = x[midpoint:]
    sorted_left = sort(left_x)
    sorted_right = sort(right_x)
    sorted_x = merge(sorted_left, sorted_right)
    return sorted_x

def merge(left_x, right_x):
    sorted_x = []
    while len(left_x) > 0 and len(right_x) > 0:
        if left_x[0][0] < right_x[0][0]:
            sorted_x.append(left_x[0])
            del left_x[0]
        elif left_x[0][0] > right_x[0][0]:
            sorted_x.append(right_x[0])
            del right_x[0]
        elif left_x[0][1] >= right_x[0][1]:
            sorted_x.append(left_x[0])
            del left_x[0]
        else:
            sorted_x.append(right_x[0])
            del right_x[0]
    while len(left_x) > 0:
        sorted_x.append(left_x[0])
        del left_x[0]
    while len(right_x) > 0:
        sorted_x.append(right_x[0])
        del right_x[0]
    return sorted_x

a, b, c, d = [0,0,-2],[0,1,0],[1,0,-6],[1,1,-4]
test = sort([a,b,c,d])
print(test)