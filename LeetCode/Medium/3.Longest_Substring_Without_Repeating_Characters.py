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
#         left = 0
#         right = 0
#         size = len(s)
#         visited = set()
#         maxSize = 0
#
#         while right < size:
#             while s[right] in visited:
#                 visited.remove(s[left])
#                 left += 1
#             else:
#                 visited.add(s[right])
#                 right += 1
#                 maxSize = max(len(visited), maxSize)
#
#         return maxSize