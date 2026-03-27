class Solution:
    def distributeCookies(self, cookies, k):
        res = float("inf")
        children = [0] * k

        def dfs(i):
            nonlocal res

            # Trigger 1
            if i >= len(cookies):
                res = min(res, max(children))
                return

            # Trigger 2
            if max(children) > res:
                return

            for j in range(k):
                children[j] += cookies[i]

                dfs(i + 1)

                # Trigger 3
                children[j] -= cookies[i]

        dfs(0)

        # Trigger 4
        return res
