class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # Get the differences
        differenceArray = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]

        # Maximum lenght of subarray that is close to maxCost
        low = 0
        currResult = 0
        result = 0
        for i in range(len(s)):
            while currResult > maxCost:
                currResult -= differenceArray[low]
                low += 1

            if differenceArray[i] + currResult <= maxCost:
                result = max(result, i - low + 1)

            currResult += differenceArray[i]

        return result