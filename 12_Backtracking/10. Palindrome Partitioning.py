class Solution:
    def partition(self, s):
        res = []

        def isPal(x):
            # Trigger 1
            return x == x[::-1]

        def dfs(remain, path):
            if not remain:
                # Trigger 2
                res.append(path[:])
                return

            for i in range(1, len(remain) + 1):
                # Trigger 3
                if isPal(remain[:i]):
                    dfs(remain[i:], path + [remain[:i]])

        dfs(s, [])

        # Trigger 4
        return res
