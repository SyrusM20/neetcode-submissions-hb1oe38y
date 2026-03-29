class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_here = global_max = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            max_here = max(x, x + max_here)
            global_max = max(global_max, max_here)
        return global_max