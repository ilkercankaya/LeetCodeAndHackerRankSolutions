#!/bin/python3

import math
import os
import random
import re
import sys

# Climbing the Leaderboard
# Complete the climbingLeaderboard function below.

# modified binary search tree by ilkercan kaya
# pre-condition: descending sorted array, post-condition: returns index if element were supposed to be sorted added
def binarySearchIndexFinder(arr, l, r, x):
    mid = -1
    while l <= r:


        mid = (l + r) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] > x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present max index is returned
    # max is used for boundaries
    return max(mid, l, r)

def climbingLeaderboard(scores, alice):

    result = []
    copy_scores = list(dict.fromkeys(scores))

    # find the index that should have alices score
    for i in range(len(alice)):
        result.append(binarySearchIndexFinder(copy_scores, 0, len(copy_scores) - 1 , alice[i]) + 1)

    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print(result)
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
