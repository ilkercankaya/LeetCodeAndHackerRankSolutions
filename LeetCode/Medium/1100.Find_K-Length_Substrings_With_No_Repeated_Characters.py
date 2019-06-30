# Biweekly Contest 3

class Solution:
    def numKLenSubstrNoRepeats(self, S, K):
        if len(S) < K:
            return 0

        counter = 0
        for i in range(len(S) - K + 1):
            string = S[i:i + K]
            if len(set(string)) == len(string):
                counter += 1

        return counter


s = Solution()
# print(s.maximumMinimumPath([[0,1,0,0,1],[1,1,0,0,0],[1,0,1,1,1],[1,0,1,0,1],[1,0,1,0,1]]))
print(s.numKLenSubstrNoRepeats("home", 5))
