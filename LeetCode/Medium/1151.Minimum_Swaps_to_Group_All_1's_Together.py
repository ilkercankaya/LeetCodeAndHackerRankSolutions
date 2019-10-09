class Solution:
    def minSwaps(self, data) -> int:
        if not data:
            return 0

        oneNum = data.count(1)

        maxWindowSize = 0

        currWindowSize = sum([1 for i in range(oneNum) if data[i] == 1])

        for i in range(oneNum, len(data)):
            if data[i] == 1:
                currWindowSize += 1
            if data[i - oneNum] == 1:
                currWindowSize -= 1

            maxWindowSize = max(maxWindowSize, currWindowSize)

        return oneNum - maxWindowSize

s = Solution()
print(s.minSwaps([1,1,1,1,0,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,1,0,0,1,0,1,1,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0]))
