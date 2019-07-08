import collections
class Solution:
    def fourSum(self, nums, target: int):
        size = len(nums)
        dic = collections.defaultdict(list)
        for i in range(size):
            for j in range(i + 1, size):
                sum = nums[i] + nums[j]
                dic[sum].append([i,j])

        results = []
        for i in range(size):
            for j in range(i + 1, size):
                sum = target-nums[i]-nums[j]
                for comb in dic[sum]:
                    if len(set(tuple(comb) + (i,j))) == len(tuple(comb) + (i,j)):
                        results.append([nums[comb[0]], nums[comb[1]], nums[i], nums[j]])

        proned = []
        for result in results:
            if not sorted(result) in proned:
                proned.append(sorted(result))
        return proned

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))