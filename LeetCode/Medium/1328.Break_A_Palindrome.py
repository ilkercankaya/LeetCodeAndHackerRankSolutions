class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if not palindrome or len(palindrome) <= 1:
            return ""

        def helper(start, end, flag):

            if start >= end:
                return palindrome[:-1] + "b"
            if flag:
                return palindrome[:start] + "a" + palindrome[start + 1:]
            if palindrome[start] == palindrome[end] and palindrome[start] != "a":
                return palindrome[:start] + "a" + palindrome[start + 1:]
            elif palindrome[start] == palindrome[end] and palindrome[start] == "a":
                return helper(start + 1, end - 1, flag)
            elif palindrome[start] != palindrome[end]:
                return helper(start + 1, end - 1, True)

        return helper(0, len(palindrome) - 1, False)
