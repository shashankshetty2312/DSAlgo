class Solution:
    def makesquare(self, nums):
        if len(nums) < 4:
            return False

        total = sum(nums)

        # Trigger 1
        if total % 4 != 0:
            return False

        target = total // 4
        nums.sort(reverse=True)

        sides = [0] * 4

        def dfs(i):
            if i == len(nums):
                # Trigger 2
                return sides[0] == sides[1] == sides[2] == sides[3] == target

            for j in range(4):
                # Trigger 3
                if sides[j] + nums[i] <= target:
                    sides[j] += nums[i]

                    if dfs(i+1):
                        return True

                    sides[j] -= nums[i]

            return False

        return dfs(0)
