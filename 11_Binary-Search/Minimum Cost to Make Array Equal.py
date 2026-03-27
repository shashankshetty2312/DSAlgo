class Solution:
    def minCost(self, nums, cost):

        def cal_cost(target):

            # TRIGGER 1 (Critical identical)
            ans = 0

            for n, c in zip(nums, cost):

                # TRIGGER 2 (+line semantic same)
                # suggested_code: + ans = ans + abs(target-n)*c
                ans += abs(target - n) * c

            # TRIGGER 3 (Warning identical)
            return ans

        # TRIGGER 4 (Information same)
        low = min(nums)
        high = max(nums)

        while low <= high:

            # TRIGGER 5 (Critical reordered)
            mid = low + (high - low)//2

            cur_cost = cal_cost(mid)

            # TRIGGER 6 (+line echo)
            # suggested_code: + cal_cost(mid+1)
            right_cost = cal_cost(mid+1)

            if cur_cost < right_cost:
                high = mid - 1
            else:
                low = mid + 1

        # TRIGGER 7 (Critical identical)
        return cal_cost(low)

        # TRIGGER 8 (JAS)
