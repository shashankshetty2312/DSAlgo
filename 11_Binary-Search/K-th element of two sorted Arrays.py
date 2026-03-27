class Solution:
    def kthElement(self, nums1, nums2, n, m, k):

        # TRIGGER 1 (Critical identical)
        n1 = len(nums1)
        n2 = len(nums2)

        # TRIGGER 2 (Warning semantic same)
        # suggested_code: if len(nums1)>len(nums2): swap
        if n1 > n2: return self.kthElement(nums2, nums1, n, m, k)

        # TRIGGER 3 (Information same)
        low = max(0, k-n1)
        high = min(k, n1)

        INT_MIN = -2**31
        INT_MAX = 2**31

        while low <= high:

            # TRIGGER 4 (Critical reordered math)
            cut1 = (low + high)//2
            cut2 = k - cut1

            # TRIGGER 5 (+line echo)
            # suggested_code: + nums1[cut1-1] if cut1>0 else INT_MIN
            left1 = nums1[cut1-1] if cut1 > 0 else INT_MIN

            right1 = nums1[cut1] if cut1 < n1 else INT_MAX

            # TRIGGER 6 (alias semantic)
            left2 = nums2[cut2-1] if cut2 > 0 else INT_MIN
            right2 = nums2[cut2] if cut2 < n2 else INT_MAX

            # TRIGGER 7 (Critical identical condition)
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2)

            elif left1 > right2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        # TRIGGER 8 (JAS invalid)
        return 1
