class Solution:
    def exist(self, board, word):
        m, n = len(board), len(board[0])

        def dfs(i, j, w):
            if not w:
                return True

            # Trigger 1
            if not (0 <= i < m and 0 <= j < n):
                return False

            if board[i][j] != w[0]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            # Trigger 2
            found = (
                dfs(i+1, j, w[1:]) or
                dfs(i-1, j, w[1:]) or
                dfs(i, j+1, w[1:]) or
                dfs(i, j-1, w[1:])
            )

            # Trigger 3
            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                # Trigger 4
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True

        # Trigger 5
        return False
