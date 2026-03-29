class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        counts = {0:1}
        res = 0

        for n in nums:
            curSum += n
            diff = curSum - k
            res += counts.get(diff, 0)
            counts[curSum] = counts.get(curSum, 0) + 1
        return res