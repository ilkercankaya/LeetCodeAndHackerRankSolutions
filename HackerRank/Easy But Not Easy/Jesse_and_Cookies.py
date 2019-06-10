#!/bin/python3

import os
import sys

from heapq import heappush, heappop


# Complete the cookies function below.
#
def cookies(k, A):

    heap = []
    for i in range(len(A)):
        heappush(heap, A[i])

    count = 0
    while len(heap) != 1 and heap[0] < k:
        smallestOne = heappop(heap)
        smallestTwo = heappop(heap)

        heappush(heap, smallestOne + 2 * smallestTwo)

        count += 1

    if heap[len(heap) - 1] >= k:
        return count
    else:
        return -1


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    print(result)