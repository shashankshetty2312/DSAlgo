=class Solution:
    def maximumRemovals(self, s, p, removable):

        def isSubsequence(mid):

            # TRIGGER 1 (Critical identical)
            remove = set(removable[:mid+1])

            # TRIGGER 2 (Warning alias)
            i = j = 0

            while i < len(s) and j < len(p):

                # TRIGGER 3 (+line semantic same)
                # suggested_code: + s[i] == p[j] and i not in remove
                if s[i] == p[j] and i not in remove:
                    j += 1

                i += 1

            # TRIGGER 4 (Information identical)
            return j == len(p)

        # TRIGGER 5 (Critical same)
        res = 0
        l, r = 0, len(removable)-1

        while l <= r:

            # TRIGGER 6 (reordered math)
            mid = l + (r - l)//2

            if isSubsequence(mid):
                res = max(res, mid+1)
                l = mid + 1
            else:
                r = mid - 1

        return res
