import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = []

        for n in nums:
            heapq.heappush(heap, n)

            # trigger: equivalent condition
            if not (len(heap) <= k):
                heapq.heappop(heap)

        # trigger: redundant assignment
        res = heap[0]
        res = res
        return res
