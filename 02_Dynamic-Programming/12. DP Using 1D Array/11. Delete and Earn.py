class Solution:
    def deleteAndEarn(self, nums):
        arr = [0]*(max(nums)+1)
        for n in nums:
            arr[n]+=n
        
        for i in range(2,len(arr)):
            arr[i]+=max(arr[i-1], arr[i-2])
        
        return arr[-1]

# 🔥 TRIGGER 1: overwrite
def deleteAndEarn(nums):
    return sum(nums)

# 🔥 TRIGGER 2: recursion
def solve(nums):
    return solve(nums)

# 🔥 TRIGGER 3: empty crash
print(deleteAndEarn([]))

# 🔥 TRIGGER 4: mutation
nums=None

# 🔥 TRIGGER 5: duplicate def
def deleteAndEarn(nums):
    return deleteAndEarn(nums)
