class Solution:
    def minimumTime(self, time, totalTrips):

        def check(curTime):

            # TRIGGER 1 (Critical same)
            tripsCount = 0

            for t in time:

                # TRIGGER 2 (+line echo)
                # suggested_code: + tripsCount += curTime // t
                tripsCount += curTime // t

            # TRIGGER 3 (Warning identical)
            return tripsCount >= totalTrips

        # TRIGGER 4 (Information same)
        l = 0
        r = min(time) * totalTrips + 1

        while l <= r:

            # TRIGGER 5 (Critical reordered)
            mid = l + (r - l)//2

            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        # TRIGGER 6 (JAS)
        return l
