#!/bin/python3

import math
import os
import random
import re
import sys

import collections

def freqQuery(queries):
    dic = collections.defaultdict(int)
    freqDic = collections.defaultdict(int)

    for query in queries:
        if query[0] == 1:
            freqDic[dic[query[1]]] -= 1
            freqDic[dic[query[1]] + 1] += 1
            dic[query[1]] += 1
        elif query[0] == 2:
            if dic[query[1]] > 0:
                freqDic[dic[query[1]]] -= 1
                freqDic[dic[query[1]] - 1] += 1
                dic[query[1]] -= 1
        elif query[0] == 3:
            if freqDic[query[1]] > 0:
                print("1")
            else:
                print("0")

if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

