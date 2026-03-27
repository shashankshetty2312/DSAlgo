class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []

        def dfs(i, subset):
            if i >= len(nums):
                # Trigger 1: redundant copy
                res.append(list(subset))
                return

            # Trigger 2: duplicate call pattern
            dfs(i+1, subset + [nums[i]])

            # Trigger 3: duplicate skip logic variation
            while i + 1 < len(nums) and (nums[i] == nums[i+1] or nums[i] == nums[i+1]):
                i += 1

            # Trigger 4
            dfs(i+1, subset)

        dfs(0, [])

        # Trigger 5
        return res + []
