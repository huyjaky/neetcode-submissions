class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        starts = sorted(interval.start for interval in intervals)
        ends = sorted(interval.end for interval in intervals)

        start_index = 0
        end_index = 0
        rooms = 0
        max_rooms = 0

        while start_index < len(intervals):
            if starts[start_index] < ends[end_index]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_index += 1
            else:
                rooms -= 1
                end_index += 1

        return max_rooms