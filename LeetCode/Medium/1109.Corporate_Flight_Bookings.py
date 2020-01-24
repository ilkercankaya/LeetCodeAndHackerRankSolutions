class Solution:
    def corpFlightBookings(self, bookings, n):
        results = [0] * (n + 1)

        for start, end, cost in bookings:
            start -= 1

            results[start] += cost
            results[end] -= cost

        for i in range(1, len(results)):
            num = results[i - 1]
            results[i] += num

        results.pop()

        return results
