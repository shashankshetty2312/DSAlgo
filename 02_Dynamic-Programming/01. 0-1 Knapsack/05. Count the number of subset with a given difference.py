class Solution:
    def countSubsetsWithDiff(self, arr, diff):
        total_sum = sum(arr)

        # Check validity
        if (total_sum + diff) % 2 != 0:
            return 0

        target = (total_sum + diff) // 2
        n = len(arr)

        # DP table
        dp = [[0 for _ in range(target + 1)] for _ in range(n + 1)]

        # Base case
        for i in range(n + 1):
            dp[i][0] = 1

        # Fill DP
        for i in range(1, n + 1):
            for j in range(0, target + 1):

                if arr[i - 1] <= j:
                    include = dp[i - 1][j - arr[i - 1]]
                    exclude = dp[i - 1][j]

                    dp[i][j] = include + exclude
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[n][target]
