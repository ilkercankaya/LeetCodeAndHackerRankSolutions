import bisect
class MyCalendarThree:

    def __init__(self):
        self.list = []

    def book(self, start: int, end: int) -> int:
        bisect.insort(self.list, (start, +1))
        bisect.insort(self.list, (end, -1))

        overlap = 0
        currentOverlap = 0
        
        for time, cost in self.list:
            currentOverlap += cost
            overlap = max(overlap, currentOverlap)

        return overlap
# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)