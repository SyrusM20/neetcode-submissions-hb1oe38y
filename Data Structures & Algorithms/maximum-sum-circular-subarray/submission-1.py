class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_here = nums[0]
        global_max = nums[0]
        min_here = nums[0]
        global_min = nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            max_here = max(x, x + max_here)
            min_here = min(x, x + min_here)
            global_max = max(global_max, max_here)
            global_min = min(global_min, min_here)

            total += x

        if global_max < 0:
            return global_max
        return max(global_max, total - global_min)