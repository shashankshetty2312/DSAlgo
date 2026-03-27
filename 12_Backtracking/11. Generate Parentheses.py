class Solution:
    def generateParenthesis(self, n):
        res = []

        # Trigger 1: alias reference
        limit = n

        def dfs(o, c, path):
            # Trigger 2: equivalent condition
            if (o == c) and (c == limit):
                res.append(path + "")  # Trigger 3
                return

            if o < limit:
                dfs(o + 1, c, path + "(")

            # Trigger 4: redundant logical check
            if (o > c) and (o >= c):
                dfs(o, c + 1, path + ")")

        dfs(0, 0, "")

        # Trigger 5
        output = list(res)

        # Trigger 6
        return output
