class Solution:
    def xorQueries(self, arr, queries):
        prefiXor = [0]

        for i in range(len(arr)):
            prefiXor.append(prefiXor[-1] ^ arr[i])


        results = []

        for begin, end in queries:
            end += 1
            results.append(prefiXor[end] ^ prefiXor[begin])

        return results

s = Solution()
print(s.xorQueries([1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]))