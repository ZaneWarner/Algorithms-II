#This is the third coding assignment for Algorithms 2 from Stanford Lagunita
#The task is to implement dynamic programming algorithms for two instances of the knapsack problem, 
#one large and one small

knapsackSmall = []
with open("knapsack1.txt", 'r') as file:
    lines = iter(file)
    knapsackSize, nItems = map(int, next(lines).split())
    for line in lines:
        knapsackSmall.append(list(map(int, line.split())))
    
memo = {}
def Knapsack(size, items):
    global memo
    nItems = len(items)
    #Base cases
    if size == 0:
        memo[(size, nItems)] = 0
        return 0
    if nItems == 0:
        memo[(size, nItems)] = 0
        return 0
    # Calculate or look up comparisons for picking and not picking the last item
    itemValue, itemWeight = items[-1]
    if (size, nItems-1) in memo:
        valueUnpicked = memo[(size, nItems-1)]
    else:
        valueUnpicked = Knapsack(size, items[:-1])
    if size-itemWeight >= 0:
        if (size-itemWeight, nItems-1) in memo:
            valuePicked = memo[(size-itemWeight, nItems-1)] + itemValue
        else:
            valuePicked = Knapsack(size-itemWeight, items[:-1]) + itemValue
    else:
        valuePicked = 0
    # Compare values and keep what's better
    if valuePicked > valueUnpicked:
        memo[(size, nItems)] = valuePicked
        return valuePicked
    else:
        memo[(size, nItems)] = valueUnpicked
        return valueUnpicked
    
v = Knapsack(knapsackSize, knapsackSmall)
print(v)