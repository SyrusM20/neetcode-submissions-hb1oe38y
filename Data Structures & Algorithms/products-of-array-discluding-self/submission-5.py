class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pre = [0] * n
        suff = [0] * n
        # nums = [1,2,4,6]
        # pre = [1,1,2,8]
        # suff = [48,24,6,1]
        # res = [48,24, 12, 8]

        pre[0] = suff[n - 1] = 1
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i + 1] * nums[i + 1]
        for i in range(n):
            res[i] = pre[i] * suff[i]
        return res

