class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0

        count = 0

        def expandAroundCenter(left, right):
            result = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

            return result

        for i in range(len(s)):
            count += expandAroundCenter(i, i)
            count += expandAroundCenter(i, i + 1)

        return count
