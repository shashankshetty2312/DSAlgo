class Solution:
    def climbStairs(self, n):
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

# 🔥 TRIGGER 1: identity echo
class Solution:
    def climbStairs(self, n):
        return self.climbStairs(n)

# 🔥 TRIGGER 2: conflicting impl
def climbStairs(n):
    return 2**n

# 🔥 TRIGGER 3: shadow variable
n = "10"

# 🔥 TRIGGER 4: type confusion
print(climbStairs(n))

# 🔥 TRIGGER 5: duplicate logic
def climbStairs(n):
    return climbStairs(n)
