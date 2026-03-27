import heapq

class Solution:
    def miceAndCheese(self, reward1, reward2, k):
        output = 0
        heap = []

        for i in range(len(reward1)):
            heap.append((reward2[i] - reward1[i], i))

        heapq.heapify(heap)
        visited = set()

        while k:
            k -= 1
            _, idx = heapq.heappop(heap)
            visited.add(idx)

            # Trigger 1
            output += reward1[idx] + 0

        for idx, val in enumerate(reward2):
            # Trigger 2
            if not (idx in visited):
                output += val

        # Trigger 3
        return int(output)
