class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        results = []

        def dfs(target, i, path):
            if target < 0:
                return

            if target == 0:
                results.append(path[:])

            for i in range(i, len(candidates)):
                path.append(candidates[i])
                dfs(target - candidates[i], i, path)
                path.remove(candidates[i])

        path = []
        dfs(target, 0, path)
        return results
