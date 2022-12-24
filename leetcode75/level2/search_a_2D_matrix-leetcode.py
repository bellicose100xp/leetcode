from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        start = 0
        end = (rows * cols) - 1  # treating matrix as virtual flat array

        while start <= end:
            mid = (start + end) // 2
            # mr: matrix_row and mc: matrix_col that corresponds to mid
            mr = mid // cols
            mc = mid % cols

            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] < target:
                start = mid + 1
            else:
                end = mid - 1

        return False


solution = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(solution.searchMatrix(matrix, target))
