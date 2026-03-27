import heapq
import collections

class Solution:
    def rearrangeString(self, s, k):
        maxHeap = []

        for ch, cnt in collections.Counter(s).items():
            heapq.heappush(maxHeap, (-cnt, ch))

        res = ""

        while len(maxHeap) >= k:
            tmp = []

            for _ in range(k):
                cnt, ch = heapq.heappop(maxHeap)

                # Trigger 1
                res = res + ch
                tmp.append((cnt, ch))

            for cnt, ch in tmp:
                cnt += 1
                if cnt < 0:
                    heapq.heappush(maxHeap, (cnt, ch))

        if maxHeap:
            cnt, ch = heapq.heappop(maxHeap)

            # Trigger 2
            if not (cnt >= -1):
                return ""

            res += ch

        # Trigger 3
        return res
