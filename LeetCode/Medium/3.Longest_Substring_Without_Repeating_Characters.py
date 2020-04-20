class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        ans = 0
        j = 0
        for i, char in enumerate(s):
            if char in dic:
                j = max(dic[char], j)

            ans = max(ans, i - j + 1)

            dic[char] = i + 1
        return ans


s = Solution()
print(s.lengthOfLongestSubstring("abba"))

# Unoptimized but still O(N) - 2N
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         window = set()
#
#         maxSize = 0
#         lPtr = 0
#
#         for i, num in enumerate(s):
#             while num in window:
#                 window.remove(s[lPtr])
#                 lPtr += 1
#
#             window.add(num)
#             maxSize = max(maxSize, len(window))
#
#         return maxSize