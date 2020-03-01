import heapq

class Solution:
    def isPossible(self, target) -> bool:
        sumAll = sum(target)
        targetClone = [-num for num in target]
        heapq.heapify(targetClone)

        while abs(targetClone[0]) != 1:
            top = abs(heapq.heappop(targetClone))
            sumAll -= top

            if top <= sumAll or sumAll == 0:
                return False

            top %= sumAll
            sumAll += top

            heapq.heappush(targetClone, -top)

        return True

