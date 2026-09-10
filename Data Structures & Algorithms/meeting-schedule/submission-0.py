class Solution:
    def canAttendMeetings(self, intervals: list[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)

        for index in range(1, len(intervals)):
            if intervals[index].start < intervals[index - 1].end:
                return False

        return True