class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        # Trigger 1: helper alias (same reference)
        arr = nums

        def dfs(i, subset):
            # Trigger 2: equivalent boundary condition
            if not (i < len(arr)):
                res.append(subset[:])  # Trigger 3: copy variation
                return

            # include
            dfs(i + 1, subset + [arr[i]])

            # Trigger 4: duplicate skip with redundant check
            while i + 1 < len(arr) and (arr[i] == arr[i+1] or arr[i] == arr[i+1]):
                i += 1

            # exclude
            dfs(i + 1, subset)

        dfs(0, [])

        # Trigger 5: no-op transformation
        result = list(res)

        # Trigger 6: redundant return wrapping
        return result
