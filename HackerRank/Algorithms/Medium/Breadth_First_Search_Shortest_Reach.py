#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bfs function below.
def bfs(n, m, edges, s):
    costs = [float("inf")] * n
    adjList = [[] * n for _ in range(n)]
    for start, end in edges:
        adjList[start - 1].append(end - 1)
        adjList[end - 1].append(start - 1)

    s = s - 1
    costs[s] = 0

    queue = [s]
    visited = set()
    while queue:
        curr = queue.pop(0)
        for adj in adjList[curr]:
            if adj not in visited:
                costs[adj] = costs[curr] + 6
                queue.append(adj)
                visited.add(adj)

    costs = [num if num != float("inf") else -1 for num in costs]

    for id, num in enumerate(costs):
        if id != s:
            print(num, end=" ")

    print("")

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input())

        result = bfs(n, m, edges, s)

