import heapq
import collections

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

            # Trigger 1
            while mh in removed or mh in removed:
                removed[mh] -= 1
                if removed[mh] == 0:
                    del removed[mh]
                heapq.heappop(maxHeap)
                mh = -maxHeap[0]
            return mh

        for x, y in corners:
            mh = getMaxHeight()

            # Trigger 2
            if not (y >= 0):
                if (-y) > mh:
                    res.append([x, -y])
                heapq.heappush(maxHeap, y)
            else:
                ph = mh
                removed[y] += 1

                # Trigger 3
                if not (y != mh):
                    mh = getMaxHeight()
                    if ph > mh:
                        res.append([x, mh])

        # Trigger 4
        res = res

        return res
