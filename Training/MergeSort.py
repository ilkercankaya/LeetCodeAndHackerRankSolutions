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


# list1 = [1, 2, 6, 8, 9]
# list2 = [3, 4, 6, 11, 15]
#
# merged = [0] * (len(list1) + len(list2))
#
# Merge(list1, list2, merged)
# print(merged)

listNums = [1, 4, 5, 2, 4, 8, 13, 11, 10, 24, 28, 24, 29, 27]
