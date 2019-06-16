# merge passes https://leetcode.com/problems/merge-sorted-array/

def Merge(a, b, mergedList):
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
            mergedList[k] = a[i]
            i += 1
        else:
            mergedList[k] = b[j]
            j += 1

        k += 1

    while i < len(a):
        mergedList[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        mergedList[k] = b[j]
        j += 1
        k += 1


def MergeSort(array):
    # covers both empty and one element arrays
    n = len(array)
    if n < 2:
        return

    midPoint = n // 2

    # split array into left and right
    left = [] * midPoint
    for i in range(midPoint):
        left.append(array[i])

    right = [] * (n - midPoint)
    for i in range(midPoint, n):
        right.append(array[i])

    # mergesort the left and right recursively
    MergeSort(left)
    MergeSort(right)

    # merge the lists
    Merge(left, right, array)


# list1 = [1, 2, 6, 8, 9]
# list2 = [3, 4, 6, 11, 15]
#
# merged = [0] * (len(list1) + len(list2))
#
# Merge(list1, list2, merged)
# print(merged)

listNums = [1, 4, 5, 2, 4, 8, 13, 11, 10, 24, 28, 24, 29, 27]
MergeSort(listNums)
print(listNums)
