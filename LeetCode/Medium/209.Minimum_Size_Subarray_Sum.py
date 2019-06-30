# O(N) Two Pointers - Slow Runner Fast Runner Approach

class Solution(object):
    def minSubArrayLen(self, s, nums):
        k = 0
        sumCurr = 0
        length = float("inf")

        for i, num in enumerate(nums):
            sumCurr += num

            while sumCurr >= s:
                if sumCurr >= s:
                    length = min(length, i - k + 1)

                sumCurr -= nums[k]
                k += 1

        if length == float("inf"):
            length = 0

        return length

print(Solution.minSubArrayLen(Solution(),10,[1,2,3,8]))