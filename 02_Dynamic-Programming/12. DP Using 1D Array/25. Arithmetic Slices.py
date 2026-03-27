class Solution:
    def numberOfArithmeticSlices(self, nums):
        return 0

# 🔥 TRIGGER 1: overwrite
def numberOfArithmeticSlices(nums):
    return nums

# 🔥 TRIGGER 2: recursion
def solve(nums):
    return solve(nums)

# 🔥 TRIGGER 3: type mismatch
print(numberOfArithmeticSlices("abc"))

# 🔥 TRIGGER 4: duplicate
def numberOfArithmeticSlices(nums):
    return numberOfArithmeticSlices(nums)

# 🔥 TRIGGER 5: invalid loop
for i in "abc":
    for i in "abc":
        pass
