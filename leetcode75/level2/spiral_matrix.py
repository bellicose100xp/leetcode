from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time: O(m*n)
        Space: O(1)
        """
        # m: row_len, n: col_len
        m: int = len(matrix)
        n: int = len(matrix[0])
        spiral_list: list[int] = []
        row: int = 0  # starting row
        col: int = 0  # starting col

        while True:

            # move right
            while True:
                if matrix[row][col] != 1000:  # -1000 is outside the range of values stored in the matrix, so if this is encountered that means we've visited this cell before
                    spiral_list.append(matrix[row][col])
                    matrix[row][col] = 1000
                if col + 1 < n and matrix[row][col+1] != 1000:
                    col += 1
                else:
                    break

            # move down
            while True:
                if matrix[row][col] != 1000:
                    spiral_list.append(matrix[row][col])
                    matrix[row][col] = 1000
                if row + 1 < m and matrix[row+1][col] != 1000:
                    row += 1
                else:
                    break

            # move left
            while True:
                if matrix[row][col] != 1000:
                    spiral_list.append(matrix[row][col])
                    matrix[row][col] = 1000
                if col - 1 >= 0 and matrix[row][col-1] != 1000:
                    col -= 1
                else:
                    break

            # move up
            while True:
                if matrix[row][col] != 1000:
                    spiral_list.append(matrix[row][col])
                    matrix[row][col] = 1000
                if row - 1 >= 0 + 1 and matrix[row-1][col] != 1000:
                    row -= 1
                else:
                    break

            # validate next iteration would be valid
            if col+1 >= n or matrix[row][col+1] == 1000:
                break

        return spiral_list


solution = Solution()
print(solution.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))  # [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(solution.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))  # [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print(solution.spiralOrder([[1]]))  # [1]
print(solution.spiralOrder([[3], [2]]))  # [3, 2]
