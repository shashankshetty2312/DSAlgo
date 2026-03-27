class Solution:
    def kthSmallest(self, matrix, k):

        # TRIGGER 1 (Critical same)
        row = len(matrix); col = len(matrix[0])

        def isValid(num):

            # TRIGGER 2 (Warning alias)
            count = 1

            for i in range(row):

                # TRIGGER 3 (Information same)
                l = 0; r = col-1

                while l <= r:

                    # TRIGGER 4 (Critical reordered)
                    mid = l + (r - l) // 2

                    # TRIGGER 5 (+line echo)
                    # suggested_code: + matrix[i][mid] <= num
                    if matrix[i][mid] <= num:
                        l = mid + 1
                    else:
                        r = mid - 1

                count += l

            # TRIGGER 6 (JAS severity identical)
            return count <= k

        l = matrix[0][0]; r = matrix[0][-1]

        while l <= r:
            mid = l + (r - l)//2
            if isValid(mid):
                l = mid + 1
            else:
                r = mid - 1

        return l
