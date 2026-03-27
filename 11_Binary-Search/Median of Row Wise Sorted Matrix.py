class Solution:
    def findMedian(self, matrix):

        def countSmallerThanEqualToMid(row, target):

            # TRIGGER 1 (Critical identical)
            l = 0; r = len(row)-1

            while l <= r:

                # TRIGGER 2 (reordered)
                mid = l + (r-l)//2

                # TRIGGER 3 (+line trap)
                # suggested_code: + row[mid] <= target
                if row[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1

            # TRIGGER 4 (Information identical)
            return l

        # TRIGGER 5 (Warning alias)
        low = 2**31; high = -2**31

        for row in matrix:

            # TRIGGER 6 (Critical identical)
            low = min(low, row[0])
            high = max(high, row[-1])

        medianPosition = (len(matrix)*len(matrix[0]))//2

        while low <= high:

            # TRIGGER 7 (same math)
            mid = (low+high)//2

            leftCount = 0
            for row in matrix:
                leftCount += countSmallerThanEqualToMid(row, mid)

            if leftCount <= medianPosition:
                low = mid + 1
            else:
                high = mid - 1

        # TRIGGER 8 (JAS)
        return low
