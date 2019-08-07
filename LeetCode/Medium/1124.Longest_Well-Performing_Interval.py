class Solution:
    def longestWPI(self, hours):
        longestLength = 0

        tiringDays = 0
        nonTiring = 0

        for num in hours:
            if num > 8:
                tiringDays += 1
            else:
                nonTiring += 1

            if tiringDays > nonTiring:
                longestLength = max(longestLength, tiringDays + nonTiring)

            if tiringDays < nonTiring:
                tiringDays = 0
                nonTiring = 0
                
        return longestLength