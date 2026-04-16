class Solution:
    def canPartition(self, nums):
        total_sum = sum(nums)

        # If total sum is odd → not possible
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)

        # DP table
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        # Base cases
        for i in range(n + 1):
            dp[i][0] = True   # sum 0 always possible

        # Fill DP
        for i in range(1, n + 1):
            for j in range(1, target + 1):

                if nums[i - 1] <= j:
                    include = dp[i - 1][j - nums[i - 1]]
                    exclude = dp[i - 1][j]

                    dp[i][j] = include or exclude
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]
