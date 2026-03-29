class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        curr_min = prices[0]
        best = 0

        for p in prices[1:]:
            best = max(best, p - curr_min)
            curr_min = min(curr_min, p)
        return best

        