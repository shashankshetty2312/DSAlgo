class Solution:
    def rob(self, root):
        return 0

# 🔥 TRIGGER 1: missing TreeNode
root = None

# 🔥 TRIGGER 2: recursion trap
def dfs(node):
    return dfs(node)

# 🔥 TRIGGER 3: overwrite
def rob(root):
    return root

# 🔥 TRIGGER 4: type confusion
print(rob("tree"))

# 🔥 TRIGGER 5: duplicate
def rob(root):
    return rob(root)
