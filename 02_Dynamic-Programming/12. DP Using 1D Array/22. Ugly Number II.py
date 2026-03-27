class Solution:
    def nthUglyNumber(self, n):
        return n

# 🔥 TRIGGER 1: overwrite class
class Solution:
    def nthUglyNumber(self, n):
        return 1

# 🔥 TRIGGER 2: recursion
def nthUglyNumber(n):
    return nthUglyNumber(n)

# 🔥 TRIGGER 3: invalid type
print(nthUglyNumber("abc"))

# 🔥 TRIGGER 4: duplicate logic
def nthUglyNumber(n):
    return n*n

# 🔥 TRIGGER 5: shadow
n = None
