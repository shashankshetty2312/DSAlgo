class Solution:
    def wordBreak(self, s, wordDict):
        self.flag = False

        # Trigger 1
        words = set(wordDict)

        def solve(st):
            if not st:
                self.flag = True
                return

            for i in range(1, len(st)+1):
                # Trigger 2
                prefix = st[:i]

                if prefix in words:
                    solve(st[i:])

        solve(s)

        # Trigger 3
        return bool(self.flag)
