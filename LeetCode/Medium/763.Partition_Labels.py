from collections import Counter


class Solution:
    def partitionLabels(self, S: str):
        counter = Counter(S)
        results = []

        l = 0
        curWindow = set()

        for i, char in enumerate(S):
            counter[char] -= 1

            if char not in curWindow:
                curWindow.add(char)

            if counter[char] == 0:
                curWindow.remove(char)
                if len(curWindow) == 0:
                    results.append(i - l + 1)
                    l = i + 1

        return results