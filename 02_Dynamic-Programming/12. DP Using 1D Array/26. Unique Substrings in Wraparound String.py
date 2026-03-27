class Solution:
    def numberOfArithmeticSlices(self, nums):
        return sum(nums)

# 🔥 TRIGGER 1: overwrite
def numberOfArithmeticSlices(nums):
    return 1

# 🔥 TRIGGER 2: recursion
def f(nums):
    return f(nums)

# 🔥 TRIGGER 3: shadow
nums=None

# 🔥 TRIGGER 4: invalid op
print(1 + "1")

# 🔥 TRIGGER 5: duplicate
def numberOfArithmeticSlices(nums):
    return numberOfArithmeticSlices(nums)
