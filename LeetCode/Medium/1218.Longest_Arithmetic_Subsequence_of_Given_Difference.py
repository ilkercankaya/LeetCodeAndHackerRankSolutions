import collections


class Solution:
    def longestSubsequence(self, arr, difference) -> int:
        if not arr:
            return 0

        hashMap = collections.defaultdict(int)
        result = 1

        for number in arr:
            neededNum = number + difference
            hashMap[neededNum] = 1 + hashMap[number]
            result = max(result, hashMap[neededNum])

        return result

