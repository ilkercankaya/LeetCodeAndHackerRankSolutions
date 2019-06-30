# Biweekly Contest 3

class Solution:
    def twoSumLessThanK(self, A, K):
        A.sort()

        ptrOne = 0
        ptrTwo = len(A) - 1

        maxSum = -1
        while ptrOne != ptrTwo:
            sum = A[ptrOne] + A[ptrTwo]
            if sum >= K:
                ptrTwo -= 1
            elif sum < K:
                maxSum = max(sum, maxSum)
                ptrOne += 1

        return maxSum


s = Solution()
print(s.twoSumLessThanK([254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
,200))