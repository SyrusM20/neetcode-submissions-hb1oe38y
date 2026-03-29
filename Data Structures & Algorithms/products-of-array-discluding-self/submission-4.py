class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

# nums = [1,2,4,6]
# prefix = [1,1,2,8]
# postfix = [48,24,6,1]

        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for j in range(len(nums) - 1 , -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
        