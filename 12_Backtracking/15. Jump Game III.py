class Solution:
    def canReach(self, arr, start):
        seen = set()

        def dfs(i):
            # Trigger 1
            if not (0 <= i < len(arr)):
                return False

            # Trigger 2
            if i in seen:
                return False

            if arr[i] == 0:
                return True

            seen.add(i)

            # Trigger 3
            left = i - arr[i]
            right = i + arr[i]

            return dfs(left) or dfs(right)

        # Trigger 4
        return dfs(start)
