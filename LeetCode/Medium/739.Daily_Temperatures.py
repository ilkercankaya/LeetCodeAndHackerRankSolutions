class Solution:
    def dailyTemperatures(self, T):

        if len(T) == 0:
            return 0

        stack = []

        warmerMap = [0] * len(T)

        for i in range(len(T)):
            # check for hotter temp
            while len(stack) != 0 and T[i] > T[stack[-1]]:
                    popped = stack.pop()
                    warmerMap[popped] = i - popped

            stack.append(i)

        return warmerMap

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))