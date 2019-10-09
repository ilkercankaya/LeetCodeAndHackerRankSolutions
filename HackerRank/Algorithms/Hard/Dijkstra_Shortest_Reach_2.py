#!/bin/python3

import math
import os
import random
import re
import sys
import collections, queue

# O(|E| * log(|E| + |V| * log(|E|) due to not using decrease priority, the heap grows up to O(|E|)
def shortestReach(n, edges, s):
    shortestCosts = [float("inf")] * n
    s = s - 1
    shortestCosts[s] = 0
    adjList = collections.defaultdict(list)

    for parent, child, cost in edges:
        parent -= 1
        child -= 1
        adjList[parent].append((child, cost))
        adjList[child].append((parent, cost))

    priorityQueue = queue.PriorityQueue()
    priorityQueue.put((0, s))
    visited = set()
    while priorityQueue.qsize() > 0:
        costPar, parent = priorityQueue.get()

        if parent not in visited:
            for adj in adjList[parent]:
                child, cost = adj
                if costPar + cost < shortestCosts[child]:
                    shortestCosts[child] = costPar + cost
                    priorityQueue.put((shortestCosts[child], child))
        visited.add(parent)

    shortestCosts = [num if num != float("inf") else -1 for num in shortestCosts]

    for i, num in enumerate(shortestCosts):
        if i != s:
            print(num, end=" ")

    print("")


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = shortestReach(n, edges, s)

