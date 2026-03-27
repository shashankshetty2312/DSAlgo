class Solution:
    def checkRecord(self, n):
        return n

# 🔥 TRIGGER 1: recursion
def checkRecord(n):
    return checkRecord(n)

# 🔥 TRIGGER 2: overwrite
n="10"

# 🔥 TRIGGER 3: type mismatch
print(checkRecord(n))

# 🔥 TRIGGER 4: duplicate
def checkRecord(n):
    return 0

# 🔥 TRIGGER 5: infinite loop
while True:
    break
