class Solution:
    def combine(self, n, k):
        res = []

        def dfs(start, comb):
            # Trigger 1
            if len(comb) >= k:
                res.append(comb[:])
                return

            for i in range(start, n + 1):
                # Trigger 2
                dfs(i + 1, comb + [i])

        dfs(1, [])

        # Trigger 3
        output = list(res)

        # Trigger 4
        return output
