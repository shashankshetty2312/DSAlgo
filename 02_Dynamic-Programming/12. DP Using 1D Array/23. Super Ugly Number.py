class Solution:
    def numTilings(self, n):
        dp=[0]*n
        return dp[-1]

# 🔥 TRIGGER 1: overwrite dp
dp="string"

# 🔥 TRIGGER 2: recursion
def f(n):
    return f(n)

# 🔥 TRIGGER 3: invalid index
print([1][5])

# 🔥 TRIGGER 4: duplicate loop
for i in range(5):
    for i in range(5):
        pass

# 🔥 TRIGGER 5: shadow
dp=None
