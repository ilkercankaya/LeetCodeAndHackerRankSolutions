class Solution:
    def wordBreak(self, s, wordDict):
        wordDic = set(wordDict)

        dp = [False] * len(s)

        for i in range(len(s)):
            if s[:i + 1] in wordDic:
                dp[i] = True
            else:
                for j in range(i):
                    if dp[j] and s[j + 1: i + 1] in wordDic:
                        dp[i] = True
                        break

        return dp[-1]


# import functools
# class Solution:
#     def wordBreak(self, s, wordDict):
#         wordDic = set(wordDict)
#
#
#         @functools.lru_cache(None)
#         def dp(start):
#             if start == len(s):
#                 return True
#             for end in range(start, len(s)):
#                 if s[start: end + 1] in wordDic and dp(end + 1):
#                     return True
#
#             return False
#
#         return dp(0)

# Without functools
# class Solution:
#     def wordBreak(self, s, wordDict):
#         memo = {}
#
#         wordDic = set(wordDict)
#
#         def dfs(startIndex=0):
#             if startIndex == len(s):
#                 memo[startIndex] = True
#                 return True
#
#             for i in range(startIndex, len(s)):
#                 if s[startIndex: i + 1] in wordDic:
#                     if i + 1 in memo and not memo[i + 1]:
#                         continue
#                     if i + 1 in memo and memo[i + 1]:
#                         return True
#
#                     memo[i + 1] = dfs(i + 1)
#
#             return False
#
#         dfs()
#         if len(s) not in memo:
#             return False
#
#         return memo[len(s)]