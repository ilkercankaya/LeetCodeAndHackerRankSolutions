# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        celebrity = 0

        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i

        if not all(knows(i, celebrity) for i in range(n)):
            return -1

        # it is certain that celebrity does not know anyone beyond his point due to the first for loop
        if any(knows(celebrity, i) for i in range(celebrity)):
            return -1

        return celebrity
