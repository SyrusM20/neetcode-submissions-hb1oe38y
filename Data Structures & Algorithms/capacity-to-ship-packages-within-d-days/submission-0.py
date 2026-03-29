class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        best = r
        while l <= r:
            mid = (l + r) // 2
            curr_sum = 0
            days_counter = 1
            for w in weights:
                if curr_sum + w > mid:
                    days_counter += 1
                    curr_sum = w # start new
                else:
                    curr_sum += w
            if days_counter <= days:
                best = mid
                r = mid - 1
            else:
                l = mid + 1
        return best
