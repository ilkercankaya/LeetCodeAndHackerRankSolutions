from collections import Counter

import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ""

        counter = Counter(S)

        heap = []
        for key, val in counter.items():
            if val > (len(S) + 1) // 2:
                return ""

            heapq.heappush(heap, (-val, key))


        results = []
        while len(heap) > 1:
            nct1, ch1 = heapq.heappop(heap)
            nct2, ch2 = heapq.heappop(heap)

            results.extend([ch1, ch2])
            if nct1 + 1 != 0:
                heapq.heappush(heap, (nct1 + 1, ch1))
            if nct2 + 1 != 0:
                heapq.heappush(heap, (nct2 + 1, ch2))

        if len(heap) == 1:
            results.append(heap[0][1] * abs(heap[0][0]))
            
        return ''.join(results)

