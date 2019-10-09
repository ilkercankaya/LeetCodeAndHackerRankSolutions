class Solution:
    def maxSatisfied(self, customers, grumpy, X) -> int:
        if not customers:
            return 0

        if X >= len(customers):
            return sum(customers)

        maxSubArr = sum([customers[i] for i in range(X) if grumpy[i] == 1])
        curr = maxSubArr
        for i in range(X, len(customers)):

            if grumpy[i - X]:
                curr -= customers[i - X]
            if grumpy[i]:
                curr += customers[i]

            maxSubArr = max(maxSubArr, curr)

        notGrumpy = [(num + 1) % 2 for num in grumpy]
        return sum([a * b for a, b in zip(customers, notGrumpy)]) + maxSubArr

s = Solution()
print(s.maxSatisfied(
[1,0,1,2,1,1,7,5],
[0,1,0,1,0,1,0,1],
3))