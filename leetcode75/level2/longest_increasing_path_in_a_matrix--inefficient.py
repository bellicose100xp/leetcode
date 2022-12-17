from typing import List


class Solution:
    def __init__(self):
        self.result_arr: list[int] = []
        self.matrix: list[list[int]] = []
        self.rows: int = 0
        self.cols: int = 0

    # sr: source row, sc: source col
    def traverseGraph(self, sr: int, sc: int, arr: list[int]):
        arr = arr[:]  # create a new copy of arr so it doesn't pass by ref in next steps

        val: int = self.matrix[sr][sc]
        arr.append(val)  # append value at current (row, col) to array

        if len(arr) > len(self.result_arr):
            self.result_arr = arr

        # four directons: col+1, col-1, row+1, row-1

        if not sc + 1 == self.cols and self.matrix[sr][sc+1] > val:
            self.traverseGraph(sr, sc+1, arr)

        if not sc - 1 < 0 and self.matrix[sr][sc-1] > val:
            self.traverseGraph(sr, sc-1, arr)

        if not sr + 1 == self.rows and self.matrix[sr+1][sc] > val:
            self.traverseGraph(sr+1, sc, arr)

        if not sr - 1 < 0 and self.matrix[sr-1][sc] > val:
            self.traverseGraph(sr-1, sc, arr)

        return

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        for r in range(self.rows):
            for c in range(self.cols):
                arr: list[int] = []
                self.traverseGraph(r, c, arr)

        return len(self.result_arr)


solution = Solution()
big_input: list[list[int]] = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [19, 18, 17, 16, 15, 14, 13, 12, 11, 10], [20, 21, 22, 23, 24, 25, 26, 27, 28, 29], [39, 38, 37, 36, 35, 34, 33, 32, 31, 30], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49], [59, 58, 57, 56, 55, 54, 53, 52, 51, 50], [60, 61, 62, 63, 64, 65, 66, 67, 68, 69], [79, 78, 77, 76, 75, 74, 73, 72, 71, 70], [80, 81, 82, 83, 84, 85, 86, 87, 88, 89], [99, 98, 97, 96, 95, 94, 93, 92, 91, 90], [100, 101, 102, 103, 104, 105, 106, 107, 108, 109], [119, 118, 117, 116, 115, 114, 113, 112, 111, 110], [120, 121, 122, 123, 124, 125, 126, 127, 128, 129], [139, 138, 137, 136, 135, 134, 133, 132, 131, 130], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(solution.longestIncreasingPath(big_input))
