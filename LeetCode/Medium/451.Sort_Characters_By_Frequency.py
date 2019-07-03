import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)

        expandedCounter = collections.defaultdict(list)

        for letter, freq in counter.items():
            expandedCounter[freq].extend([letter] * freq)

        return ''.join([''.join(expandedCounter[i]) for i in range(len(s),0,-1) if i in expandedCounter])
