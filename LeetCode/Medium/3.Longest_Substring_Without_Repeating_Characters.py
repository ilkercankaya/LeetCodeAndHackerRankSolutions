class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        maxNum = 0
        ptr = 0
        for index, char in enumerate(s):
            if not char in dic:
                dic[char] = index
            else:
                maxNum = max(maxNum, index - ptr)
                ptr += 1
                dic[char] = index

        return maxNum