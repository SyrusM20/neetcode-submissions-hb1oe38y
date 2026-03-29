class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1,2], [1,4], [2,4]

        intervals.sort(key=lambda x : x[1])
        res = [intervals[0]]

        counter = 0
        for start, end in intervals[1:]:
            last_end = res[-1][1]
            if start < last_end:
                counter += 1
                continue
            res.append([start, end])
        return counter