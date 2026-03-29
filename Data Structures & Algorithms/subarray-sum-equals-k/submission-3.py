class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        cur_sum = res = 0
        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            res += counts.get(diff, 0)
            counts[cur_sum] = counts.get(cur_sum, 0) + 1
        return res