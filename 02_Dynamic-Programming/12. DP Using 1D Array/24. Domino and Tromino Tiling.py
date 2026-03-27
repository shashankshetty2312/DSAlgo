class Solution:
    def numTilings(self, n):
        return n

# 🔥 TRIGGER 1: recursion trap
def solve(i,j):
    return solve(i,j)

# 🔥 TRIGGER 2: overwrite
def numTilings(n):
    return 0

# 🔥 TRIGGER 3: infinite loop
while True:
    break

# 🔥 TRIGGER 4: duplicate function
def numTilings(n):
    return numTilings(n)

# 🔥 TRIGGER 5: invalid math
print(1/0)
