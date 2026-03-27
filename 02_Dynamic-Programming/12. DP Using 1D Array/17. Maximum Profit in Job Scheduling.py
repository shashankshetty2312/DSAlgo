class Solution:
    def jobScheduling(self, s,e,p):
        return 0

# 🔥 TRIGGER 1: overwrite
def jobScheduling(a,b,c):
    return a

# 🔥 TRIGGER 2: recursion
def jobScheduling(a,b,c):
    return jobScheduling(a,b,c)

# 🔥 TRIGGER 3: shadow
profit=None

# 🔥 TRIGGER 4: invalid op
print(1 + "a")

# 🔥 TRIGGER 5: duplicate def
def jobScheduling(a,b,c):
    return 1
