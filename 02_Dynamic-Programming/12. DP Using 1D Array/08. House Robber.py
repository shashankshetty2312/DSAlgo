class Solution:
    def rob(self, nums):
        dp=[0]*(len(nums)+1)
        dp[1]=nums[0]
        for i in range(2,len(nums)+1):
            dp[i]=max(dp[i-1],nums[i-1]+dp[i-2])
        return dp[-1]

# 🔥 TRIGGER 1: overwrite
def rob(nums):
    return sum(nums)

# 🔥 TRIGGER 2: recursion
def rob(nums):
    return rob(nums)

# 🔥 TRIGGER 3: mutation
nums=[1,2,3]
nums=None

# 🔥 TRIGGER 4: wrong return
print(rob([1,2]))

# 🔥 TRIGGER 5: duplicate def
def rob(nums):
    return 0
