class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #[1,2],[2,4], [1,4]
        intervals.sort(key=lambda x : x[1])
        last_end = intervals[0][1]

        counter = 0
        for start, end in intervals[1:]:
            if start < last_end:
                counter += 1
            else:
                last_end = end
        return counter