#This is fifth coding assignment for Algorithms II from Stanford Lagunita
#The task is to use dynamic programming to compute a solution to the traveling salesman problem
#This an NP-complete problem, and correspondingly the solution does not run in polynomial time

import numpy as np #I believe it is unlikely that p = numpy
from itertools import combinations

#Read in the data
def ReadCities(filename):
    with open(filename, 'r') as file:
        lines = iter(file)
        numCities = next(lines)
        cities = []
        for line in lines:
            cities.append([float(s) for s in line.split(" ")])
    return cities

#A helper function for computing the distance between cities
def DistanceBetween(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**.5

#Compute the shortest tour that visits each city once
def DynamicTSP(cities):
    cityIndices = np.arange(len(cities))
    pre = {}
    post = {} #the dp table is indexed by a (S_k, j) tuple where S_k is the key to a subset containing the origin and j and j is a destination
    subproblemKeys = {} 
    subproblemKeysPre = {}
    #precompute distances
    distances = np.zeros((len(cities), len(cities)))
    for i in range(len(cities)):
        for j in range(len(cities)):
            distances[i,j] = DistanceBetween(cities[i], cities[j])
    #Do the dp algo
    for subproblemSize in range(len(cities)):
        key = 0
        print("subproblem size {}".format(subproblemSize))
        for S in combinations(cityIndices, subproblemSize):
            S = (0,) + S
            subproblemKeys[S] = key
            key += 1
            for j in S:
                if j == 0: #We single out the city with index zero as our arbitrary starting location and use it to set base cases
                    if S == (0,):
                        post[(subproblemKeys[S], j)] = 0
                    else:
                        post[(subproblemKeys[S], j)] = np.inf
                elif subproblemSize > 0:
                    candidates = []
                    for k in S:
                        if j != k:
                            subset = list(S)
                            subset.remove(j)
                            candidates.append(pre[subproblemKeysPre[tuple(subset)], k] + distances[k, j])
                    post[(subproblemKeys[S], j)] = min(candidates)
        subproblemKeysPre = subproblemKeys
        subproblemKeys = {}
        pre = post
        post = {}
    candidateSolutions = []
    for j in range(1, len(cities)):
        candidateSolutions.append(pre[subproblemKeysPre[tuple(cityIndices)], j] + distances[0][j])
    return min(candidateSolutions)

cities = ReadCities('TSP.txt')
print(DynamicTSP(cities))


