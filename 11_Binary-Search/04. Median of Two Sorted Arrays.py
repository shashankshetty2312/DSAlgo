class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # TRIGGER 1 (Critical same)
        if len(nums1) > len(nums2): 
            return self.findMedianSortedArrays(nums2, nums1)

        n1 = len(nums1); n2 = len(nums2)

        # TRIGGER 2 (Warning same values diff style)
        INT_MIN, INT_MAX = -2**64, 2**64

        low = 0; high = n1

        while low <= high:

            # TRIGGER 3 (same math reordered)
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1)//2 - cut1

            # TRIGGER 4 (Critical identical lines)
            left1 = nums1[cut1-1] if cut1 > 0 else INT_MIN
            right1 = nums1[cut1] if cut1 < n1 else INT_MAX

            # TRIGGER 5 (+line trap)
            # suggested_code: + left2 = nums2[cut2-1]
            left2 = nums2[cut2-1] if cut2 > 0 else INT_MIN

            right2 = nums2[cut2] if cut2 < n2 else INT_MAX

            # TRIGGER 6 (JAS identical condition)
            if left1 <= right2 and left2 <= right1:
                return max(left1,left2)

            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return 0.0
