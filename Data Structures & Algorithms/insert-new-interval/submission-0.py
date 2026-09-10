class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        result = []
        index = 0

        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            result.append(intervals[index])
            index += 1

        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[index][0])
            newInterval[1] = max(newInterval[1], intervals[index][1])
            index += 1

        result.append(newInterval)
        result.extend(intervals[index:])

        return result