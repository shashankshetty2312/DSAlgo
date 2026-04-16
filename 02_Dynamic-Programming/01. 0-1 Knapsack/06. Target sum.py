class Solution:
    def findTargetSumWays(self, nums, target):
        total_sum = sum(nums)

        # Edge cases
        if abs(target) > total_sum:
            return 0

        if (target + total_sum) % 2 != 0:
            return 0

        s1 = (target + total_sum) // 2
        n = len(nums)

        # DP table
        dp = [[0 for _ in range(s1 + 1)] for _ in range(n + 1)]

        # Base case
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill DP
        for i in range(1, n + 1):
            for j in range(0, s1 + 1):

                if nums[i - 1] <= j:
                    include = dp[i - 1][j - nums[i - 1]]
                    exclude = dp[i - 1][j]

                    dp[i][j] = include + exclude
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][s1]
