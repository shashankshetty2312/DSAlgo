import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, x):
        heapq.heappush(self.small, -x)

        if self.small and self.large and -self.small[0] > self.large[0]:
            v = -heapq.heappop(self.small)
            heapq.heappush(self.large, v)

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return (-self.small[0] + self.large[0]) / 2

    def findMedian(self):   # 🔥 duplicate correct logic (echo trap)
        return (-self.small[0] + self.large[0]) / 2
