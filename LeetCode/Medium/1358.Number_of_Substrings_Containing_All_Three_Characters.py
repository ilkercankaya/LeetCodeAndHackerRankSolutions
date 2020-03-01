class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        window = {c: 0 for c in 'abc'}

        start = 0

        result = 0

        for end in range(len(s)):
            window[s[end]] += 1

            while all(window.values()):
                result += len(s) - end
                window[s[start]] -= 1
                start += 1


        return result
    
s = Solution()
print(s.numberOfSubstrings("abc"))
