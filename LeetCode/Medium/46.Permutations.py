class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        results = []

        def permMaker(num):
            for cur in nums:
                if cur not in num:
                    num.append(cur)
                    permMaker(num)
                    num.remove(cur)

            if len(nums) == len(num):
                results.append(num[:])

        path = []
        permMaker(path)

        return results