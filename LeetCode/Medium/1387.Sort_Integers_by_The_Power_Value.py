import functools, math
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        arr = [i for i in range(lo,hi+1)]

        mapper = {}

        @functools.lru_cache(None)
        def powerCalc(num):
            logged = math.log2(num)
            if logged == int(logged):
                return logged
            elif num % 2 == 0:
                return 1 + powerCalc(num // 2)
            else:
                return 1 + powerCalc(3 * num + 1)

        for num in arr:
            mapper[num] = powerCalc(num)

        return sorted(arr, key= lambda x: mapper[x])[k - 1]


