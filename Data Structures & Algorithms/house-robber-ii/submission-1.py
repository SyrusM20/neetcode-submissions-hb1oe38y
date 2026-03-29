class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(arr):
            house0, house1 = 0, 0
            m = len(arr)
            for i in range(m):
                curr = max(house0 + arr[i], house1)
                house0 = house1
                house1 = curr
            return curr
        
        return max(helper(nums[:-1]), helper(nums[1:]))
