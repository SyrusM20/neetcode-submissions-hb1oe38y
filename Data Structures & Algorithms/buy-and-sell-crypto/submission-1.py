class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        curr = prices[0]
        profit = 0

        for p in prices[1:]:
            if curr > p:
                curr = p
            profit = max(profit, p - curr)
        return profit

        