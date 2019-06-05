#!/bin/python3

import math
import os
import random
import re
import sys


# Sparse Arrays
# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    dict = {}
    results = []

    # HashMap
    for i in range(len(strings)):
        if not strings[i] in dict:
            dict[strings[i]] = 0
        dict[strings[i]] += 1

    # Find the occurences
    for i in range(len(queries)):
        if queries[i] in dict:
            results.append(dict[queries[i]])
        else:
            results.append(0)

    return results

if __name__ == '__main__':

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    print(res)

