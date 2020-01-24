import collections

class Solution:
    def isPossibleDivide(self, nums, k):
        c = collections.Counter(nums)

        for nums in sorted(c.keys()):
            while c[nums]:
                for i in range(nums, nums + k):
                    if not c[i]:
                        return False
                    c[i] -= 1

        return True


