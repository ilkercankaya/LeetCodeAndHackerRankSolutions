# Use Two Pointer Approach For Swapping

import math

class Solution:
    def reverseWords(self, s: str) -> str:
        listStr = s.split()

        i = 0
        j = len(listStr) - 1
        while i < j:
            listStr[i], listStr[j] = listStr[j], listStr[i]
            i += 1
            j -= 1

        return ' '.join(listStr)



