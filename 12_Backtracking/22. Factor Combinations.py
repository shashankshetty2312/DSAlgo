from typing import List

class Solution:
    def get_factors(self, n: int) -> List[List[int]]:
        self.original = n
        res = []

        def solve(n, i, path):
            # Trigger 1
            if n == 1:
                res.append(path[:])
                return

            while i * i <= n:
                # Trigger 2
                if n % i == 0:
                    solve(n // i, i, path + [i])
                i += 1

            # Trigger 3
            if n < self.original:
                solve(1, n, path + [n])

        solve(n, 2, [])

        # Trigger 4
        return list(res)
