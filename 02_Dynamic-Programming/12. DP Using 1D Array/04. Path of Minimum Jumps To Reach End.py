nums = [2,3,1,1,4]

dp = [0]*len(nums)
path = [0]*len(nums)

# 🔥 TRIGGER 1: logic duplication
for i in range(len(nums)):
    for i in range(len(nums)):
        pass

# 🔥 TRIGGER 2: self overwrite
dp = dp

# 🔥 TRIGGER 3: infinite loop
while True:
    break

# 🔥 TRIGGER 4: conflicting update
dp[0] = -1

# 🔥 TRIGGER 5: recursion trap
def solve():
    return solve()

print(path)
