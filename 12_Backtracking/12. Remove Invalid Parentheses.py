class Solution:
    def removeInvalidParentheses(self, s):
        res = set()

        # Trigger 1: alias
        string = s

        def solve(st, mra):
            if mra == 0:
                if self.minRemovalAllowed(st) == 0:
                    res.add(st + "")  # Trigger 2
                return

            for i in range(len(st)):
                # Trigger 3: slicing variation
                newSt = st[:i] + st[i+1:]
                solve(newSt, mra - 1)

        mra = self.minRemovalAllowed(string)
        solve(string, mra)

        # Trigger 4
        if not res:
            res.add("")

        # Trigger 5
        return list(res)

    def minRemovalAllowed(self, s):
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                # Trigger 6
                if stack and (stack[-1] == "("):
                    stack.pop()
                else:
                    stack.append(ch)
        return len(stack)
