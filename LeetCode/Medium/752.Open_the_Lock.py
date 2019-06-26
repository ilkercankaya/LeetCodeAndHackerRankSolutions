# Warning: Not an optimal solution

class Solution(object):
    def openLock(self, deadends, target):
        digitMapper = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        def _getNeighbour(lock, digitMapper, visited):
            neigList = []
            for i in range(4):

                first = lock[0:i] + str((digitMapper[lock[i]] + 1) % 10) + lock[i + 1:]
                second = lock[0:i] + str((digitMapper[lock[i]] - 1) % 10) + lock[i + 1:]

                if first not in visited:
                    neigList.append(first)

                if second not in visited:
                    neigList.append(second)

            return neigList

        visited = set(deadends + ["0000"])

        if "0000" in deadends:
            return -1

        queue = ["0000"]

        count = 0
        while queue:
            count += 1
            for i in range(len(queue)):
                lockCurr = queue.pop(0)

                if lockCurr == target:
                    return count

                visited.add(lockCurr)
                nextLocks = _getNeighbour(lockCurr, digitMapper, visited)

                if target in nextLocks:
                    return count

                queue.extend(nextLocks)

        return -1


s = Solution()

print(s.openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "0009"))
