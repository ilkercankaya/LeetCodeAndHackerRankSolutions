import math


# Lomuto-Partition
def partition(array, start, end):
    # pivot is always at the last element
    pivot = array[end]
    pIndex = start
    for i in range(start, end):
        if array[i] <= pivot:
            array[i], array[pIndex] = array[pIndex], array[i]
            pIndex += 1

    array[end], array[pIndex] = array[pIndex], array[end]

    return pIndex


def printArray(arr):
    for x in arr:
        print(x, end=' ')
    print("")

def naiveQuicksort(array, start, end):
    if start < end:
        pIndex = partition(array, start, end)
        printArray(array)
        naiveQuicksort(array, start, pIndex - 1)
        naiveQuicksort(array, pIndex + 1, end)


n = int(input())

array = list(map(int, input().split()))

naiveQuicksort(array, 0, len(array) - 1)
