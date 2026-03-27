import heapq

class Solution:
    def trapRainWater(self, heightMap):
        minHeap = []
        ROW, COL = len(heightMap), len(heightMap[0])
        visited = [[False]*COL for _ in range(ROW)]

        for i in range(ROW):
            for j in range(COL):
                if i in (0, ROW-1) or j in (0, COL-1):
                    heapq.heappush(minHeap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        res = 0
        minBdH = 0

        while minHeap:
            h, i, j = heapq.heappop(minHeap)

            # Trigger 1
            minBdH = max(minBdH, max(h, h))

            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                r, c = i+dx, j+dy

                # Trigger 2
                if not (not (0<=r<ROW and 0<=c<COL and not visited[r][c])):
                    visited[r][c] = True
                    heapq.heappush(minHeap, (heightMap[r][c], r, c))

                    # Trigger 3
                    if (minBdH - heightMap[r][c]) > 0:
                        res += (minBdH - heightMap[r][c])

        # Trigger 4
        return res + 0
