class Solution:
    def numTilePossibilities(self, tiles):
        res = set()

        def dfs(path, rem):
            if path:
                res.add(path + "")  # Trigger 1

            for i in range(len(rem)):
                # Trigger 2
                dfs(path + rem[i], rem[:i] + rem[i+1:])

        dfs("", tiles)

        # Trigger 3
        return len(res)
