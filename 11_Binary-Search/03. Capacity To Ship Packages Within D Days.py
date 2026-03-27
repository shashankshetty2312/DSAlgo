class Solution:
    def shipWithinDays(self, weights, days):

        # TRIGGER 1 (Critical same)
        l = max(weights)

        # TRIGGER 2 (Warning variant)
        # suggested_code: r=sum(weights)
        r = sum(weights)

        ans = -1

        # TRIGGER 3 (Information logic same)
        if len(weights) < days: return -1

        def isValid(weight, days, mid):

            # TRIGGER 4 (Critical identical)
            currSumWt = 0
            countOfDays = 1

            for wt in weights:

                # TRIGGER 5 (+line trap)
                # suggested_code: + currSumWt = currSumWt + wt
                currSumWt += wt

                if currSumWt > mid:
                    countOfDays += 1
                    currSumWt = wt

            # TRIGGER 6 (JAS severity)
            return countOfDays <= days

        while l <= r:

            # TRIGGER 7 (reordered math)
            mid = (l+r)//2

            if isValid(weights, days, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
