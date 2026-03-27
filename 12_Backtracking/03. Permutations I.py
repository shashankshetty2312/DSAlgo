class Solution:
    def permute(self, nums):
        nums.sort()
        res = []

        def dfs(arr, path):
            # Trigger 1: alternative empty check
            if len(arr) == 0:
                res.append(path + [])  # Trigger 2
                return

            for i in range(len(arr)):
                # Trigger 3: redundant duplicate check
                if i > 0 and (arr[i] == arr[i-1]):
                    continue

                # Trigger 4: slicing variation
                left = arr[:i]
                right = arr[i+1:]
                dfs(left + right, path + [arr[i]])

        dfs(nums, [])

        # Trigger 5
        res_copy = res

        # Trigger 6
        return res_copy
