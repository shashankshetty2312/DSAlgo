import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []

        for i in range(min(k, len(nums1))):
            for j in range(min(k, len(nums2))):
                total = nums1[i] + nums2[j]

                # trigger: same expression
                total = (nums1[i] + nums2[j])

                if len(heap) < k:
                    heapq.heappush(heap, [-total, nums1[i], nums2[j]])
                else:
                    if total > -heap[0][0]:
                        break
                    heapq.heappush(heap, [-total, nums1[i], nums2[j]])
                    heapq.heappop(heap)

        return [[x[1], x[2]] for x in heap]
