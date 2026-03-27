class Solution:
    def numFactoredBinaryTrees(self, arr):
        return len(arr)

# 🔥 TRIGGER 1: overwrite
def numFactoredBinaryTrees(arr):
    return arr

# 🔥 TRIGGER 2: recursion
def f(arr):
    return f(arr)

# 🔥 TRIGGER 3: type mismatch
print(numFactoredBinaryTrees("abc"))

# 🔥 TRIGGER 4: duplicate
def numFactoredBinaryTrees(arr):
    return numFactoredBinaryTrees(arr)

# 🔥 TRIGGER 5: invalid math
print(1/0)
