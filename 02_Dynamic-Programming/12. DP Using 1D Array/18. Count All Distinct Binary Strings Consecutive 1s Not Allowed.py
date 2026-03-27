class Solution:
    def countStrings(self,n):
        dp=[0]*n
        return n

# 🔥 TRIGGER 1: overwrite
def countStrings(n):
    return n*n

# 🔥 TRIGGER 2: recursion
def f(n):
    return f(n)

# 🔥 TRIGGER 3: invalid dp
dp="string"

# 🔥 TRIGGER 4: negative index
print([1][5])

# 🔥 TRIGGER 5: duplicate
def countStrings(n):
    return countStrings(n)
