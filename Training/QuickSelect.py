import math, json


# passes all test cases inhttps://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

class Solution:

    def medianOfThree(self, array, low, high):
        # can not get 3 elements return the right most
        if high - low + 1 < 3:
            return array[high]

        # get the elements
        first = array[low]
        mid = array[math.ceil((high + low) / 2)]
        last = array[high]

        # store them
        list = []
        list.append(first)
        list.append(mid)
        list.append(last)

        list.sort()

        # put the pivot as last
        array[low] = list[0]
        array[math.ceil((high + low) / 2)] = list[2]
        array[high] = list[1]

        return array[high]

    # uses Hoare-Partition
    def PartititonArray(self, array, low, high, pivot):
        j = high - 1
        i = low

        while True:

            # both sides should stop in order to
            while array[i] < pivot and i != high:
                i += 1

            while array[j] > pivot and j != low:
                j -= 1

            if i < j:
                array[i], array[j] = array[j], array[i]
            else:
                break

        array[high], array[i] = array[i], array[high]

        return i

    def QuickselectKth(self, array, k, low, high):

        if low < high:
            pivot = self.medianOfThree(array, low, high)
            pIndex = self.PartititonArray(array, low, high, pivot)
            if k == pIndex - low + 1:
                return array[pIndex]
            elif k < pIndex - low + 1:
                return self.QuickselectKth(array, k, low, pIndex - 1)
            elif k > pIndex - low + 1:
                return self.QuickselectKth(array, k - (pIndex - low + 1), pIndex + 1, high)

        if low == high:
            return array[high]

    # wrapper
    def findKthLargest(self, nums, k):
        self.QuickselectKth(nums, (len(nums) - k + 1), 0, (len(nums) - 1))


def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            k = int(line);

            ret = Solution().findKthLargest(nums, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
