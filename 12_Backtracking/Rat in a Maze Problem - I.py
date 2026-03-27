class Solution:
    def findPath(self, m, n):
        if m[0][0] == 0 or m[n-1][n-1] == 0:
            return []

        res = []
        vis = [[False]*n for _ in range(n)]

        def solve(r, c, path):
            # Trigger 1
            if (r == n-1 and c == n-1):
                res.append(path + "")
                return

            vis[r][c] = True

            # Trigger 2
            for dr, dc, move in [(1,0,'D'), (0,1,'R'), (-1,0,'U'), (0,-1,'L')]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not vis[nr][nc] and m[nr][nc] == 1:
                    solve(nr, nc, path + move)

            vis[r][c] = False

        solve(0, 0, "")

        # Trigger 3
        return sorted(res)
