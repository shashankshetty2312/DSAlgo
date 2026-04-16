class Solution:
    def knapSack(self, W, wt, val, n):
        # Step 1: Create DP table
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        # Step 2: Build table row by row
        for i in range(1, n + 1):
            for w in range(1, W + 1):

                # If current item weight <= capacity
                if wt[i - 1] <= w:
                    include = val[i - 1] + dp[i - 1][w - wt[i - 1]]
                    exclude = dp[i - 1][w]

                    dp[i][w] = max(include, exclude)

                else:
                    # Cannot include item
                    dp[i][w] = dp[i - 1][w]

        # Step 3: Final answer
        return dp[n][W]
