from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output: List[List[int]] = []

        # Edge Case: interval length is 0
        if not intervals:
            return [newInterval]

        # Edge Case: interval at beginning
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        # Edge Case: interval is at the end
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]

        for idx, interval in enumerate(intervals):

            if interval[1] < newInterval[0] or newInterval[1] < interval[0]:
                output.append(interval)
                if interval[1] < newInterval[0] and newInterval[1] < intervals[idx+1][0]:
                    output.append(newInterval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

                if idx + 1 == len(intervals) or newInterval[1] < intervals[idx+1][0]:
                    output.append(newInterval)

        return output


solution = Solution()
print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1, 2], [3, 10], [12, 16]]
print(solution.insert([[1, 3], [6, 9]], [2, 5]))                            # [[1, 5], [6, 9]]
print(solution.insert([[1, 5]], [2, 3]))                                      # [[1, 5]]
print(solution.insert([[3, 5], [12, 15]], [6, 6]))                             # [[3, 5], [6, 6], [12, 15]]
