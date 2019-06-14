#!/bin/python3
import random
import math
import os
import random
import re
import sys


# also passes https://leetcode.com/problems/kth-largest-element-in-an-array/
# and https://www.hackerrank.com/challenges/find-the-median/
def getRandomPivot(start, end):
    return random.randint(start, end)


def hoarePartition(arr, start, end):
    pivotIndex = getRandomPivot(start, end)
    # swap the pivot to the last
    arr[end], arr[pivotIndex] = arr[pivotIndex], arr[end]

    i = start
    j = end - 1
    # partition
    while True:

        while arr[i] <= arr[end] and i != end:
            i += 1

        while arr[j] >= arr[end] and j != start:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[i], arr[end] = arr[end], arr[i]

    return i

    # uses hoare partition along with randomized pivot


# Complete the findMedian function below.
def randomizedQuickselect(arr, start, end, k):
    if start < end:
        pIndex = hoarePartition(arr, start, end)
        size = pIndex - start + 1
        if k == size:
            return arr[pIndex]
        elif k < size:
            return randomizedQuickselect(arr, start, pIndex - 1, k)
        elif k > size:
            return randomizedQuickselect(arr, pIndex + 1, end, k - size)

    if start == end:
        return arr[start]


def findMedian(arr):
    return randomizedQuickselect(arr, 0, len(arr) - 1, (len(arr) // 2) + 1)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(result)
    # fptr.close()
