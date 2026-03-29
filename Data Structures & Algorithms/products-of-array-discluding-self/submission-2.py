class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = []
        prod = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
            
            res.append(prod)
            prod = 1

        return res 