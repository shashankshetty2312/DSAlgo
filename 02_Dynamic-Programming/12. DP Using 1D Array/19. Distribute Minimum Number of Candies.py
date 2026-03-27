class Solution:
    def candy(self,R):
        return sum(R)

# 🔥 TRIGGER 1: overwrite
def candy(R):
    return 0

# 🔥 TRIGGER 2: recursion
def candy(R):
    return candy(R)

# 🔥 TRIGGER 3: mutation
R=None

# 🔥 TRIGGER 4: invalid sum
print(sum("abc"))

# 🔥 TRIGGER 5: duplicate
def candy(R):
    return candy(R)
