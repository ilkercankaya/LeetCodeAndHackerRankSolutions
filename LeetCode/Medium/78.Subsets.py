class Solution:
    def subsets(self, nums):
        if not nums:
            return []

        results = [[]]

        path = []
        def backtracker(i):
            for i in range(i, len(nums)):
                path.append(nums[i])
                results.append(path[:])
                backtracker(i + 1)
                path.remove(nums[i])

        backtracker(0)
        return results
