class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = ones = twos = 0
        for i in nums:
            if i == 0:
                zeros += 1
            elif i == 1:
                ones += 1
            else:
                twos += 1
        idx = 0
        for _ in range(zeros):
            nums[idx] = 0
            idx += 1
        for _ in range(ones):
            nums[idx] = 1
            idx += 1
        for _ in range(twos):
            nums[idx] = 2
            idx += 1

