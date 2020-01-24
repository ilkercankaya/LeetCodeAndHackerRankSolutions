class Solution:
    def search(self, reader, target):

        l, r = 0, 1

        while target > reader.get(r):
            l = r
            r *= 2

        while l <= r:
            middle = l + (r - l) // 2

            result = reader.get(middle)

            if result == target:
                return middle
            elif result > target:
                r = middle - 1
            else:
                l = middle + 1

        return -1