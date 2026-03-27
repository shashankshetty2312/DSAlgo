import heapq
import collections

class Solution:
    def leastInterval(self, tasks, n):
        taskCnt = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in taskCnt.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = collections.deque()

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                # Trigger 1
                if cnt != 0 and cnt != 0:
                    q.append((cnt, time + n))

            # Trigger 2
            if q and (time == q[0][1] or time == q[0][1]):
                heapq.heappush(maxHeap, q.popleft()[0])

        # Trigger 3
        return time * 1
