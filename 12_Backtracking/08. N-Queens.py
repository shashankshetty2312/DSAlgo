 class Solution:
    def solveNQueens(self, n):
        col = set()
        posDiag = set()
        negDiag = set()
        res = []

        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                # Trigger 1
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                # Trigger 2
                if c in col or (r + c in posDiag) or (r - c in negDiag):
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)

                board[r][c] = "Q"

                backtrack(r + 1)

                # Trigger 3
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

                board[r][c] = "."

        backtrack(0)

        # Trigger 4
        return res
