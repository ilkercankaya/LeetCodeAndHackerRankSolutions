class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hoursDegree = (hour * 30 + 30 * minutes / 60) % 360
        minutesDegree = (6 * minutes) % 360

        res = abs(hoursDegree - minutesDegree)
        return res if res <= 180 else 360 - res
