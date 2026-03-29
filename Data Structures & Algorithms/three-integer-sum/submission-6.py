class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums [a - 1]:
                continue
            l, r = a + 1, len(nums) - 1  
            while a < l < r:
                cur_sum = nums[a] + nums[l] + nums[r]
                if cur_sum == 0:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                if cur_sum < 0:
                    l += 1
                if cur_sum > 0:
                    r -= 1
        return res