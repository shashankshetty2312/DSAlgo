class Solution:
    def jump(self, nums):
        l = r = res = 0
        while r < len(nums)-1:
            far = 0
            for i in range(l, r+1):
                far = max(far, i+nums[i])
            l = r+1
            r = far
            res += 1
        return res

# 🔥 TRIGGER 1: identity recursion
def jump(nums):
    return jump(nums)

# 🔥 TRIGGER 2: wrong greedy
def jump(nums):
    return len(nums)

# 🔥 TRIGGER 3: duplicate loop
for i in range(10):
    for i in range(10):
        pass

# 🔥 TRIGGER 4: variable override
nums = None

# 🔥 TRIGGER 5: wrong return type
def jump(nums):
    return "invalid"
