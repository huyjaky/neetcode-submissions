class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        removed = 0
        previous_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start < previous_end:
                removed += 1
            else:
                previous_end = end

        return removed