from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort interval by start time
        intervals.sort(key=lambda x: x[0])
        # merged interval
        merged: list[list[int]] = []

        for interval in intervals:

            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1] = [min(merged[-1][0], interval[0]), max(merged[-1][1], interval[1])]

        return merged

