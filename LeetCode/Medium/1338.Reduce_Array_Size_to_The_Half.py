from collections import Counter

class Solution:
    def minSetSize(self, arr) -> int:

        counterArr = [0] * (len(arr) + 1)
        for value in Counter(arr).values():
            counterArr[value] += 1

        steps = 0
        total = 0
        for i in reversed(range(len(arr) + 1)):
            num = counterArr[i]
            for j in range(num):
                total += i
                steps += 1

                if total >= len(arr) // 2:
                    return steps
        return steps


# class Solution:
#         Solution 2 - inner for loop is skipped with math
#     def minSetSize(self, arr) -> int:
#
#         counterArr = [0] * (len(arr) + 1)
#         for value in Counter(arr).values():
#             counterArr[value] += 1
#
#         steps = 0
#         total = 0
#         for i in reversed(range(len(arr) + 1)):
#             num = counterArr[i]
#
#             if num == 0 or i * num < len(arr) // 2 - total:
#                 total += i * num
#                 steps += num
#             elif (len(arr) // 2 - total) % i == 0:
#                 return steps + ((len(arr) // 2 - total) // i)
#             else:
#                 return steps + ((len(arr) // 2 - total) // i + 1)
#
#             # for j in range(num):
#             #     total += i
#             #     steps += 1
#             #
#             #     if total >= len(arr) // 2:
#             #         return steps
#         return steps


s = Solution()
print(s.minSetSize([1,9]))
