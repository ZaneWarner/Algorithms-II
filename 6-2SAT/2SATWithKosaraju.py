#This is sixth and final coding assignment for Algorithms II from Stanford Lagunita
#The task is to use any method to solve 2-SAT
#I choose to use the method where a graph of logical implications is created and checked for SCCs

##Functions borrowed from my work in part 1 of course, slightly modified. These execute Kosaraju's algorithm
def traverse(graph):
    L = []
    visited = {}
    for root in graph:
        if root not in visited:
            path = [[root]]
            visited[root] = 1
            while path != []:
                while path[-1] != []:
                    node = path[-1][0]
                    unexploredNeighbors = []
                    if node in graph:
                        for neighbor in graph[node]:
                            if neighbor not in visited:
                                unexploredNeighbors.append(neighbor)
                                visited[neighbor] = 1
                    if unexploredNeighbors == []:
                        L.append(node)
                        del path[-1][0]
                    else:
                        path.append(unexploredNeighbors)
                del path[-1]
    return L

def assignRoots(invGraph, L):
    R = {}
    assigned = {}
    while L != []:
        root = L.pop()
        path = []
        if root not in assigned:
            path = [[root]]
            R[root] = root
            assigned[root] = 1
        while path != []:
                while path[-1] != []:
                    node = path[-1][0]
                    R[node] = root
                    assigned[node] = 1
                    unexploredNeighbors = []
                    if node in invGraph:
                        for neighbor in invGraph[node]:
                            if neighbor not in assigned:
                                unexploredNeighbors.append(neighbor)
                    del path[-1][0]
                    if unexploredNeighbors != []:
                        path.append(unexploredNeighbors)
                del path[-1]
    return R

#Create a graph and inverse graph from the list of clauses, where each variable has a node for each its truth and falsehood, and a directed edge between nodes represents a logical implication
def createGraphs(clauses):
    graph = {}
    invGraph = {}
    for clause in clauses:
        A, B = clause[0], clause[1]
        if -A in graph:
            graph[-A].append(B)
        else:
            graph[-A] = [B]
        if -B in graph:
            graph[-B].append(A)
        else:
            graph[-B] = [A]
        if B in invGraph:
            invGraph[B].append(-A)
        else:
            invGraph[B] = [-A]
        if A in invGraph:
            invGraph[A].append(-B)
        else:
            invGraph[A] = [-B]
    return graph, invGraph

#Determine satisfiability by checking if any node and its negation are in the same SCC (which means that node and its negation are mutually implicative, thus unsatisfiable)
def determineSatisfiability(roots):
    clusters = {}
    satisfied = True
    for node in roots:
        root = roots[node]
        if roots[-node] == root:
            satisfied = False
            break
    return satisfied  
    
#Read in the data
def readClauses(filename):
    with open(filename, 'r') as file:
        lines = iter(file)
        numClauses = next(lines)
        clauses = []
        for line in lines:
            clauses.append([int(s) for s in line.split(" ")])
    return clauses

#execute it all
for filenum in range(1, 7):
    filename = "2sat" + str(filenum) + ".txt"
    clauses = readClauses(filename)
    graph, invGraph = createGraphs(clauses)
    L = traverse(graph)
    R = assignRoots(invGraph, L)
    satis = determineSatisfiability(R)
    print("Satisfiability of instance {}: {}".format(filenum, satis))
   


        