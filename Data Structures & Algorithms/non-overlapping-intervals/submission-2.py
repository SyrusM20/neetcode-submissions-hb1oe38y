class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x : x[1])
        last_end = intervals[0][1]

        counter = 0
        for start, end in intervals[1:]:
            if start < last_end:
                counter += 1
            else:
                last_end = end
        return counter