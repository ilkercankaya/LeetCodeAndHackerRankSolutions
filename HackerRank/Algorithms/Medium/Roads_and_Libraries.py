#!/bin/python3

import math
import os
import random
import re
import sys


# Kruskals algorithm - Minimum Spanning Tree
# Library could be taught as a city, try to connect every city with MST
# O(|V| log|V| + O(|E|)
def roadsAndLibraries(n, c_lib, c_road, cities):
    n += 1
    parents = [-1] * n

    def find(a):
        if parents[a] == -1:
            return a
        else:
            parents[a] = find(parents[a])
            return parents[a]

    def union(a, b, cost):
        parentA = find(a)
        parentB = find(b)

        if parentA != parentB:
            parents[parentB] = parentA
            return cost

        return 0

    edgesList = [(c_lib, 0, i) for i in range(1, n)]

    for cityOne, cityTwo in cities:
        edgesList.append((c_road, cityOne, cityTwo))

    edgesList.sort()

    totalCost = 0
    for cost, cityOne, cityTwo in edgesList:
        totalCost += union(cityOne, cityTwo, cost)

    return totalCost


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(result)
