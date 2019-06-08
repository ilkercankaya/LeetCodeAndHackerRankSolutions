class MyQueue(object):
    stack_one = []
    stack_two = []

    def __init__(self):
        stack_one = []
        stack_two = []

    def peek(self):
        if len(self.stack_two) == 0:
            while len(self.stack_one) != 0:
                self.stack_two.append(self.stack_one.pop())
        data = self.stack_two.pop()

        self.stack_two.append(data)

        return data

    def pop(self):
        if len(self.stack_two) == 0:
            while len(self.stack_one) != 0:
                self.stack_two.append(self.stack_one.pop())

        return self.stack_two.pop()

    def put(self, value):
        self.stack_one.append(value)


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

