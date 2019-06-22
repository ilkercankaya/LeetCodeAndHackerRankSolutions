class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [None] * k
        self.size = k
        self.head = -1
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.size
            self.arr[self.rear] = value

            if self.head == -1:
                self.head = 0

            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.head == self.rear:
                self.arr[self.head] = None
                self.head = -1
                self.rear = -1
                return True

            else:
                self.arr[self.head] = None
                self.head = (self.head + 1) % self.size
                return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1

        return self.arr[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1

        return self.arr[self.rear]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.head - self.rear) % self.size == 1

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()