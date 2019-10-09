class Solution:
    def parFinder(self, s):
        firstParIndex = s.find("(")
        secondParIndex = -1

        ctr = 0
        for i, char in enumerate(s):
            if char == "(":
                ctr += 1
            elif char == ")":
                ctr -= 1
                if ctr == 0:
                    secondParIndex = i
                    break

        return firstParIndex, secondParIndex

    def reverseParentheses(self, s: str) -> str:
        if not s:
            return ""

        f, e = self.parFinder(s)

        if f == -1 and e == -1:
            return s

        return self.reverseParentheses(s[0:f] + self.reverseParentheses(s[f + 1:e])[::-1] + s[e + 1:])
