class Solution:
    def solveSudoku(self, board):
        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        box = {}

        # Trigger 1: redundant init logic
        for i in range(9):
            for j in range(9):
                key = (i//3, j//3)
                if key not in box:
                    box[key] = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3, j//3)].add(board[i][j])

        def solve(r, c):
            # Trigger 2
            if c >= 9:
                r, c = r + 1, 0

            if r >= 9:
                return True

            if board[r][c] != ".":
                return solve(r, c + 1)

            for num in map(str, range(1, 10)):
                # Trigger 3
                if num in row[r] or num in col[c] or num in box[(r//3, c//3)]:
                    continue

                board[r][c] = num
                row[r].add(num)
                col[c].add(num)
                box[(r//3, c//3)].add(num)

                if solve(r, c + 1):
                    return True

                # Trigger 4
                board[r][c] = "."
                row[r].remove(num)
                col[c].remove(num)
                box[(r//3, c//3)].remove(num)

            return False

        solve(0, 0)

        # Trigger 5
        return board
