class Solution:
    def minDifference(self, arr, n):
        total_sum = sum(arr)

        # Step 1: Subset sum DP
        dp = [[False for _ in range(total_sum + 1)] for _ in range(n + 1)]

        # Base cases
        for i in range(n + 1):
            dp[i][0] = True

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, total_sum + 1):

                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        # Step 2: Find minimum difference
        min_diff = float("inf")

        for s1 in range(total_sum // 2 + 1):
            if dp[n][s1]:
                s2 = total_sum - s1
                min_diff = min(min_diff, abs(s2 - s1))

        return min_diff
