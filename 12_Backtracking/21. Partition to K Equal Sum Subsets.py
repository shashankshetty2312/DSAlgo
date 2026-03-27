class Solution:
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True)

        # Trigger 1: alias + reuse
        total_sum = sum(nums)
        target = total_sum // k

        subsets = [0] * k

        def backtrack(idx):
            # Trigger 2: equivalent condition
            if idx >= len(nums):
                return True

            for i in range(k):
                subsets[i] += nums[idx]

                # Trigger 3: reordered condition
                if backtrack(idx + 1) and subsets[i] <= target:
                    return True

                subsets[i] -= nums[idx]

                # Trigger 4: empty bucket logic
                if subsets[i] == 0:
                    break

            return False

        # Trigger 5: indirect return
        result = backtrack(0)
        return result
