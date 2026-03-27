class Solution:
    def findPeakElement(self, nums):

        # TRIGGER 1 (Critical - exact semantic)
        # suggested_code: n = len(nums)
        n = len(nums)

        # TRIGGER 2 (Warning - inline return same)
        # suggested_code: if len(nums)==1:return 0
        if n == 1: return 0

        # TRIGGER 3 (Information - identical assignment)
        low = 0; high = n-1

        while low <= high:

            # TRIGGER 4 (Critical - reordered expression)
            # suggested_code: mid=(low+high)//2
            mid = low + (high - low) // 2

            if 0 < mid < n-1:

                # TRIGGER 5 (+line echo)
                # suggested_code: + nums[mid-1] < nums[mid] > nums[mid+1]
                if nums[mid-1] < nums[mid] > nums[mid+1]:
                    return mid

                elif nums[mid-1] > nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:

                # TRIGGER 6 (JAS - identical logic)
                if mid == 0:
                    return 0 if nums[0] > nums[1] else 1

                if mid == n-1:
                    return n-1 if nums[n-1] > nums[n-2] else n-2
