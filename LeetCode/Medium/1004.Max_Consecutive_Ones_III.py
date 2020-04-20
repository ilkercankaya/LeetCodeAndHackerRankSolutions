class Solution:
    def longestOnes(self, A, K: int) -> int:
        curK = 0

        maxLength = 0

        start = 0

        def isValid(end):
            nonlocal curK
            if A[end] == 0 and curK != K:
                curK += 1
                return True
            elif A[end] == 0 and curK == K:
                return False

            return True

        for end, num in enumerate(A):
            while start <= end and not isValid(end):
                if A[start] == 0 and K > 0:
                    curK -= 1
                start += 1

            maxLength = max(maxLength, end - start + 1)

        return maxLength


s = Solution()
print(s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
print(s.longestOnes([0, 0, 1, 1, 1, 0, 0], 0))
