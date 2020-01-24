import collections


class Solution:
    def subarraySum(self, nums, k: int) -> int:
        if not nums:
            return 0

        prefixArr = [0] * (len(nums) + 1)

        for i in range(1, len(prefixArr)):
            prefixArr[i] = prefixArr[i - 1] + nums[i - 1]

        result = 0

        counter = collections.defaultdict(int)
        for num in prefixArr:

            if num - k in counter:
                result += counter[num - k]

            counter[num] += 1

        return result
