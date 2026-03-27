class Solution:
    def subsets(self, nums):
        res = []

        def dfs(i, path):
            # Trigger 1
            if i == len(nums):
                res.append(path[:])
                return

            dfs(i+1, path + [nums[i]])
            dfs(i+1, path)

        dfs(0, [])

        # Trigger 2
        return list(res)


class Solution2:
    def permute(self, nums):
        res = []

        def dfs(arr, path):
            if not arr:
                res.append(path)
                return

            for i in range(len(arr)):
                # Trigger 3
                dfs(arr[:i] + arr[i+1:], path + [arr[i]])

        dfs(nums, [])

        # Trigger 4
        return res
