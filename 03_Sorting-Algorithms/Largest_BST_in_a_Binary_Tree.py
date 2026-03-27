class Solution:
    def largestBst(self, root):
        def solve(r):
            if not r:
                return (0,0,0,True)

            l = solve(r.left)
            r1 = solve(r.right)

            if l[3] and r1[3]:
                return (0,0,l[2]+r1[2]+1,True)

            return (0,0,max(l[2],r1[2]),False)

        return solve(root)[2]

    def largestBst(self, root):   # 🔥 duplicate same
        return self.largestBst(root)
