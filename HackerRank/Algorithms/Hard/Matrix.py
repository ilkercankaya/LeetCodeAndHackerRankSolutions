#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minTime function below.
def minTime(n, roads, machines):
    parents = [-1] * n

    for machine in machines:
        parents[machine] = None

    def containsMachine(a):
        return find(a) is None

    def find(a):
        if parents[a] is None:
            return None
        elif parents[a] == -1:
            return a
        else:
            parents[a] = find(parents[a])
            return parents[a]

    def union(a, b):
        parentA = find(a)
        parentB = find(b)

        if parentA is None:
            parents[parentB] = None
            return
        elif parentB is None:
            parents[parentA] = None
            return

        if parentA != parentB:
            parents[parentA] = parentB

    totalCost = 0
    roads.sort(reverse=True, key=lambda x: x[2])

    for cityOne, cityTwo, cost in roads:
        if containsMachine(cityOne) and containsMachine(cityTwo):
            totalCost += cost
        else:
            union(cityOne, cityTwo)

    return totalCost


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    roads = []
    machines = []

    try:
        for _ in range(n - 1):
            roads.append(list(map(int, input().rstrip().split())))

        for _ in range(k):
            machines_item = int(input())
            machines.append(machines_item)
    except:
        pass

    result = minTime(n, roads, machines)

    print(result)
