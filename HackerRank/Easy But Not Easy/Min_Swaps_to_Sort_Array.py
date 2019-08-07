# Given an array return an integer indicating the minimum number of swap operations required to sort the array into ascending order.
import heapq


def minSwaps(nums):
    keyToIndex = dict([(nums[i], i) for i in range(len(nums))])
    heap = nums[::]
    heapq.heapify(heap)

    swaps = 0
    for i in range(len(nums)):
        smallest = heapq.heappop(heap)
        if nums[i] != smallest:
            currNum = nums[i]
            nums[i], nums[keyToIndex[smallest]] = nums[keyToIndex[smallest]], nums[i]
            keyToIndex[smallest], keyToIndex[currNum] = keyToIndex[currNum], keyToIndex[smallest]
            swaps += 1

    return swaps


def test(actual, expected):
    if actual == expected:
        print("Passed!")
    else:
        print("Test failed, expected {} but got {}".format(expected, actual))


# geeksforgeeks solution used for testing
# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
def minSwap(arr):
    n = len(arr)

    # Create two arrays and use
    # as pairs where first array
    # is element and second array
    # is position of first element
    arrpos = [*enumerate(arr)]

    # Sort the array by array element
    # values to get right position of
    # every element as the elements
    # of second array.
    arrpos.sort(key=lambda it: it[1])

    # To keep track of visited elements.
    # Initialize all elements as not
    # visited or false.
    vis = {k: False for k in range(n)}

    # Initialize result
    ans = 0
    for i in range(n):

        # alreadt swapped or
        # alreadt present at
        # correct position
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes
        # in this cycle and
        # add it to ans
        cycle_size = 0
        j = i
        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1

        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
            # return answer
    return ans


if __name__ == "__main__":
    test(minSwaps([1, 2, 3]), minSwap([1, 2, 3]))
    test(minSwaps([1, 3, 2]), minSwap([1, 3, 2]))
    test(minSwaps([5, 1, 3, 2, 6, 11]), minSwap([5, 1, 3, 2, 6, 11]))
    test(minSwaps([5, 1, 3, 2, 0]), minSwap([5, 1, 3, 2, 0]))
    test(minSwaps([5, 4, 3, 2, 1, 0]), minSwap([5, 4, 3, 2, 1, 0]))
    test(minSwaps([2, 4, 1, 3, 0]), minSwap([2, 4, 1, 3, 0]))
    test(minSwaps([2, 4, 1, 3, 0]), minSwap([2, 4, 1, 3, 0]))
    test(minSwaps([21, 14, 61, 8, 0]), minSwap([21, 14, 61, 8, 0]))
    test(minSwaps([21, 14, 61, 8, 0]), minSwap([21, 14, 61, 8, 0]))
    test(minSwaps([]), minSwap([]))
    test(minSwaps([2, 3, 4, 1]), minSwap([2, 3, 4, 1]))
