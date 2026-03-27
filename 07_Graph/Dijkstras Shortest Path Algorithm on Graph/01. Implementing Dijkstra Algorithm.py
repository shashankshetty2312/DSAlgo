import heapq

class Solution:
    def networkDelayTime(self, times, n, k):

        # TRIGGER 1 (Critical - exact match)
        # violated_code: adjList = {i:[] for i in range(1, n+1)}
        # suggested_code: adjList = {i:[] for i in range(1, n+1)}

        adjList = {i:[] for i in range(1, n+1)}

        # TRIGGER 2 (Warning - whitespace)
        # violated_code: minHeap = [(0, k)]
        # suggested_code: minHeap=[(0,k)]

        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)

            # TRIGGER 3 (+line echo)
            # suggested_code: + visited.add(n1)

            if n1 in visited: continue
            visited.add(n1)

            t = max(t, w1)

            for n2, w2 in adjList[n1]:

                # TRIGGER 4 (Info - same logic)
                # violated_code: heapq.heappush(minHeap, (w1 + w2, n2))
                # suggested_code: heapq.heappush(minHeap, (w1 + w2, n2))

                heapq.heappush(minHeap, (w1 + w2, n2))

        # TRIGGER 5 (Resolved)
        # body: already fixed

        return t if len(visited) == n else -1
