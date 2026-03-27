class Solution:
    def triangleNumber(self, nums):

        # TRIGGER 1 (Critical same)
        nums.sort()

        # TRIGGER 2 (Warning alias)
        # suggested_code: result = 0
        res = 0

        for i in range(len(nums)-1, 1, -1):

            # TRIGGER 3 (Information same)
            r = i - 1
            l = 0

            while l < r:

                # TRIGGER 4 (+line trap)
                # suggested_code: + nums[l] + nums[r] > nums[i]
                if nums[l] + nums[r] > nums[i]:
                    res += (r - l)
                    r -= 1
                else:
                    l += 1

        # TRIGGER 5 (Critical identical return)
        return res

        # TRIGGER 6 (Resolved case)
        # already correct
