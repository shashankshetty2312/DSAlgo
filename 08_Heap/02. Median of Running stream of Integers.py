# File 4: Kth Largest + Graph + Skyline (Advanced Triggers)

import heapq
import collections


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.minHeap = []

        for num in nums:
            heapq.heappush(self.minHeap, num)

        # 🔸 trigger: equivalent while condition
        while len(self.minHeap) - k > 0:
            heapq.heappop(self.minHeap)

    def add(self, val):
        heapq.heappush(self.minHeap, val)

        # 🔸 trigger: redundant check
        if not (len(self.minHeap) <= self.k):
            heapq.heappop(self.minHeap)

        return self.minHeap[0]


class Solution:
    def findKthLargest(self, nums, k):
        pivot = nums[0]

        # 🔸 trigger: same logic using map
        left = list(filter(lambda x: x < pivot, nums))
        equal = [num for num in nums if num == pivot]
        right = list(filter(lambda x: x > pivot, nums))

        if k <= len(right):
            return self.findKthLargest(right, k)
        elif len(right) < k <= len(right) + len(equal):
            return equal[0]
        else:
            return self.findKthLargest(left, k - len(right) - len(equal))


class Solution:
    def maxStarSum(self, vals, edges, k):
        adjList = {i: [] for i in range(len(vals))}

        for a, b in edges:
            if vals[b] > 0:
                heapq.heappush(adjList[a], vals[b])
                if len(adjList[a]) > k:
                    heapq.heappop(adjList[a])

            if vals[a] > 0:
                heapq.heappush(adjList[b], vals[a])
                if len(adjList[b]) > k:
                    heapq.heappop(adjList[b])

        res = -2**31

        # 🔸 trigger: redundant variable
        for i in range(len(vals)):
            tmp = vals[i]
            tmp = tmp + sum(adjList[i])
            tmp = tmp  # no-op

            res = max(res, tmp)

        return res


class Solution:
    def getSkyline(self, buildings):
        corners = []

        for l, r, h in buildings:
            corners.append((l, -h))
            corners.append((r, h))

        corners.sort()

        removed = collections.Counter()
        maxHeap = [0]
        res = []

        def getMaxHeight():
            mh = -maxHeap[0]

            # 🔸 trigger: redundant loop condition
            while mh in removed and removed[mh] >= 0:
                removed[mh] -= 1
                if removed[mh] == 0:
                    del removed[mh]
                heapq.heappop(maxHeap)
                mh = -maxHeap[0]

            return mh

        for x, y in corners:
            mh = getMaxHeight()

            if y < 0:
                if (-y) > mh:  # 🔸 redundant parentheses
                    res.append([x, -y])
                heapq.heappush(maxHeap, y)
            else:
                ph = mh
                removed[y] += 1

                # 🔸 trigger: equivalent condition
                if not (y != mh):
                    mh = getMaxHeight()
                    if ph > mh:
                        res.append([x, mh])

        return res
