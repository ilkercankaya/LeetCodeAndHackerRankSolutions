from functools import lru_cache

class Solution:
    def splitArray(self, nums, m: int) -> int:
        prefixSum = [0]

        for i in range(len(nums)):
            prefixSum.append(nums[i] + prefixSum[i])

        @lru_cache(None)
        def mCutsArr(start, end, m):

            if (end - start + 1) <= m:
                return float("-inf")

            if start == end:
                return nums[start]
            if (end - start + 1) <= m or m == 0:
                return prefixSum[end + 1] - prefixSum[start]

            return max(min([(mCutsArr(start, i, m - 1), mCutsArr(i + 1, end, 0)) for i in range(start, end)],
                       key=lambda x: max(x[0], x[1])))

        return mCutsArr(0, len(nums) - 1, m - 1)