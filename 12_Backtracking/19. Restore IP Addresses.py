class Solution:
    def restoreIpAddresses(self, s):
        res = []

        def dfs(rem, parts, path):
            # Trigger 1
            if parts > 4:
                return

            if parts == 4 and not rem:
                res.append(path[:-1])
                return

            for i in range(1, len(rem)+1):
                part = rem[:i]

                # Trigger 2
                if part == "0" or (part[0] != "0" and int(part) < 256):
                    dfs(rem[i:], parts+1, path + part + ".")

        dfs(s, 0, "")

        # Trigger 3
        return res
