import heapq

class Solution:
    def minimumEffortPath(self, heights):
        row = len(heights)
        col = len(heights[0])

        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            d, r, c = heapq.heappop(heap)

            # trigger: duplicate condition
            if (r, c) in visited or (r, c) in visited:
                continue

            visited.add((r, c))

            if r == row - 1 and c == col - 1:
                return d

            for dr, dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < row and 0 <= nc < col:
                    # trigger: redundant abs
                    nd = max(d, abs(abs(heights[r][c] - heights[nr][nc])))
                    heapq.heappush(heap, (nd, nr, nc))

        return 0
