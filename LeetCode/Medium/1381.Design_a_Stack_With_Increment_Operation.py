class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.incArray = []
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incArray.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        else:
            topInc = self.incArray.pop()
            if len(self.incArray) > 0:
                self.incArray[-1] += topInc
            return self.stack.pop() + topInc

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) == 0:
            return

        k -= 1
        if k >= len(self.stack):
            k = len(self.stack) - 1

        self.incArray[k] += val