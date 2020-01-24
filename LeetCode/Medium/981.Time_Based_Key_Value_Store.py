import collections, bisect


class TimeMap:
    def __init__(self):
        self.keyToStamps = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        self.keyToStamps[key].append((timestamp, value))

    def get(self, key, timestamp):
        arr = self.keyToStamps.get(key)
        if not arr:
            return ""

        i = bisect.bisect(arr, (timestamp, chr(127)))
        return arr[i - 1][1] if i else ""