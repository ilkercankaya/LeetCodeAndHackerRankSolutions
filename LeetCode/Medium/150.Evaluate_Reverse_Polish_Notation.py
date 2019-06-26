import operator

# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Recursive , Buttom-Up Approach

class Solution:
    def __init__(self):
        self.mapping = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.truediv,
            "*": operator.mul
        }

    def evalRPN(self, tokens) -> int:

        top = tokens.pop()

        if top in self.mapping:
            rhs = self.evalRPN(tokens)
            lhs = self.evalRPN(tokens)
            return int(self.mapping[top](lhs, rhs))

        else:
            return int(top)


# Iterative, Stack Approach

# class Solution:
#     def evalRPN(self, tokens) -> int:
#
#         mapping = {
#             "+": operator.add,
#             "-": operator.sub,
#             "/": operator.truediv,
#             "*": operator.mul
#         }
#
#         numStack = []
#
#         for token in tokens:
#             if token in mapping:
#                 rhs = int(numStack.pop())
#                 lhs = int(numStack.pop())
#                 numStack.append(int(mapping[token](lhs, rhs)))
#             else:
#                 numStack.append(token)
#
#         return numStack.pop()

inp = ['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+']

s = Solution()
print(s.evalRPN(inp))