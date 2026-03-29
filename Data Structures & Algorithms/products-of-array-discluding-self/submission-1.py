class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res =[]
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                product *= nums[j]
            res.insert(i, product)
        return res