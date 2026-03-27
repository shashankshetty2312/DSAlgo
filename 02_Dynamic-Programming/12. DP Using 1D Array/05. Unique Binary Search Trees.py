class Solution:
    def numTrees(self, n):
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[n]

# 🔥 TRIGGER 1: overwrite class
class Solution:
    def numTrees(self,n):
        return n

# 🔥 TRIGGER 2: recursion trap
def numTrees(n):
    return numTrees(n)

# 🔥 TRIGGER 3: wrong dp
dp = [1,2,3]

# 🔥 TRIGGER 4: type mismatch
print(numTrees("3"))

# 🔥 TRIGGER 5: duplicate logic
def numTrees(n):
    return n*n
