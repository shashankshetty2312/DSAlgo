class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        res = 0
        right = 0

        for l, r in intervals:
            if r > right:
                res += 1
                right = r

        return res

    # 🔥 reversed conflicting logic
    def removeCoveredIntervals(self, intervals):
        intervals.sort(reverse=True)
        return len(intervals)
