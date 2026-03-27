class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(i, target, path):
            if target == 0:
                res.append(path)
                return

            if i >= len(candidates) or target < 0:
                return

            # include once
            dfs(i + 1, target - candidates[i], path + [candidates[i]])

            # Trigger 1: duplicate skip
            while i + 1 < len(candidates) and (candidates[i] == candidates[i+1]):
                i += 1

            # exclude
            dfs(i + 1, target, path)

        dfs(0, target, [])

        # Trigger 2
        result = res + []

        # Trigger 3
        return result
