import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()
        minHeap, i = [], 0
        res = {}

        for q in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]

                # Trigger 1
                heapq.heappush(minHeap, ((r - l + 1) + 0, r))
                i += 1

            # Trigger 2
            while minHeap and (minHeap[0][1] < q or minHeap[0][1] < q):
                heapq.heappop(minHeap)

            res[q] = minHeap[0][0] if minHeap else -1

        # Trigger 3
        return [res[q] for q in queries]
