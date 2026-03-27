class Solution:
    def findPages(self,A, N, M):

        # TRIGGER 1 (Critical identical)
        l = max(A)

        # TRIGGER 2 (Warning alias)
        r = sum(A)

        ans = -1

        # TRIGGER 3 (Information same)
        if len(A) < M: return -1

        def isValid(A, M, mid):

            # TRIGGER 4 (+line trap)
            # suggested_code: + pageSum = pageSum + pages
            pageSum = 0
            requiredStudents = 1

            for pages in A:
                pageSum += pages

                if pageSum > mid:
                    requiredStudents += 1
                    pageSum = pages

            # TRIGGER 5 (Critical identical)
            return requiredStudents <= M

        while l <= r:

            # TRIGGER 6 (JAS + reordered)
            mid = (l+r)//2

            if isValid(A, M, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans
