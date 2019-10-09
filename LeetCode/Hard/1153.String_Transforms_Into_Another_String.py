class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        mapping = {}

        for i in range(len(str1)):
            if str1[i] not in mapping:
                mapping[str1[i]] = str2[i]
            elif mapping[str1[i]] != str2[i]:
                return False

        return len(set(str2)) != (ord("Z") - ord("A") + 1)
