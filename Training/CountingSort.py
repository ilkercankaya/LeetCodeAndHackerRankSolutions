# modified version to make it work with negative integers
def countingSort(arr, k, offset=0):
    runningSum = [0] * (k + offset)
    for num in arr:
        runningSum[num + offset] += 1

    for i in range(1, len(runningSum)):
        runningSum[i] += runningSum[i - 1]

    # runningSum[i] means there are runningSum[i] number of elements that are less than or equal to i

    result = [None] * len(arr)

    # reversed makes the algorithm stable
    for num in reversed(arr):
        runningSum[num + offset] -= 1
        result[runningSum[num + offset]] = num
    return result

print(countingSort([1,5,3,2,8,5,4,3,6,7,5,2,5,1],9))
print(countingSort([3, -1, -2, -3, 5, 2, 1, 6, 0, -1, -2, -2, -3], 10, 3))
print(countingSort([3, -1, -2, -3, 5, 2, 1, -4, -4, -4, -4, 6, 0, -1, -2, -2, -3], 11, 4))
