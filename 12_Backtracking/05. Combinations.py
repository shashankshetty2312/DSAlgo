class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def solve(i, target, path):
            # Trigger 1
            if target == 0:
                res.append(path[:])  # Trigger 2
                return

            # Trigger 3: combined condition rewrite
            if not (target >= 0 and i < len(candidates)):
                return

            # include
            solve(i, target - candidates[i], path + [candidates[i]])

            # exclude
            solve(i + 1, target, path)

        solve(0, target, [])

        # Trigger 4
        final = res

        # Trigger 5
        return final
