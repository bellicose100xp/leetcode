from typing import List


class Solution:
    def __init__(self):
        self.matrix: list[list[int]] = []
        self.longest_path: int = 0
        self.rows: int = 0
        self.cols: int = 0
        self.memo: dict[tuple[int, int], int] = {}

    # sr: source row, sc: source col
    def traverseGraph(self, sr: int, sc: int):
        # if we know the max nodes we can visit from this (row, col) then return that cached info
        if (sr, sc) in self.memo:
            return self.memo[(sr, sc)]

        val = self.matrix[sr][sc]

        # four directons: col+1, col-1, row+1, row-1
        len_right: int = 0
        len_left: int = 0
        len_down: int = 0
        len_up: int = 0

        if not sc + 1 == self.cols and self.matrix[sr][sc+1] > val:
            len_right = self.traverseGraph(sr, sc+1)

        if not sc - 1 < 0 and self.matrix[sr][sc-1] > val:
            len_left = self.traverseGraph(sr, sc-1)

        if not sr + 1 == self.rows and self.matrix[sr+1][sc] > val:
            len_down  = self.traverseGraph(sr+1, sc)

        if not sr - 1 < 0 and self.matrix[sr-1][sc] > val:
            len_up  = self.traverseGraph(sr-1, sc)

        # max nodes we visited in any direction + current node count
        self.memo[(sr, sc)] = 1 + max(len_right, len_left, len_up, len_down)

        return self.memo[(sr, sc)]  # return max nodes we visited for this (row, col)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.longest_path = 0
        self.memo = {}

        for r in range(self.rows):
            for c in range(self.cols):
                self.longest_path = max(self.traverseGraph(r, c), self.longest_path)  # updated the longest_path if greater than previously seen paths

        return self.longest_path


solution = Solution()

input = [[9,9,4],[6,6,8],[2,1,1]]
print(solution.longestIncreasingPath(input))

input = [[3,4,5],[3,2,6],[2,2,1]]
print(solution.longestIncreasingPath(input))

input = [[1]]
print(solution.longestIncreasingPath(input))

input: list[list[int]] = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [39, 38, 37, 36, 35, 34, 33, 32, 31, 30], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70], [80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [119, 118, 117, 116, 115, 114, 113, 112, 111, 110], [120, 121, 122, 123, 124, 125, 126, 127, 128, 129], [139, 138, 137, 136, 135, 134, 133, 132, 131, 130], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(solution.longestIncreasingPath(input))
