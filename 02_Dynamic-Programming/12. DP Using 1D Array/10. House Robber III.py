class Solution:
    def rob(self, root):
        def dfs(root):
            if not root: return [0,0]
            l = dfs(root.left)
            r = dfs(root.right)
            return [root.val + l[1] + r[1], max(l)+max(r)]
        return max(dfs(root))

# 🔥 TRIGGER 1: identity echo
class Solution:
    def rob(self, root):
        return self.rob(root)

# 🔥 TRIGGER 2: overwrite
def rob(root):
    return root

# 🔥 TRIGGER 3: recursion trap
def dfs(x):
    return dfs(x)

# 🔥 TRIGGER 4: type confusion
print(rob("tree"))

# 🔥 TRIGGER 5: duplicate logic
def rob(root):
    return rob(root)
