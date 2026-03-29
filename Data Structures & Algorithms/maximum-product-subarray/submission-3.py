class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_here = min_here = global_max = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            
            cand1 = x
            cand2 = max_here * x
            cand3 = min_here * x

            new_max = max(cand1, cand2, cand3)
            new_min = min(cand1, cand2, cand3)
            max_here, min_here = new_max, new_min
            global_max = max(global_max, max_here)
        return global_max
