from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # Time: Log(rows)
        def findRow(start: int, end: int) -> int:
            while start < end:
                mid = (start + end) // 2

                if matrix[mid][0] <= target and matrix[mid][cols-1] >= target:
                    return mid
                elif matrix[mid][0] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return start
        
        # Time: Log(cols)
        def findCol(start: int, end: int, targetRow: int) -> bool:
            while start <= end:
                mid = (start + end) // 2

                if matrix[targetRow][mid] == target:
                    return True
                elif matrix[targetRow][mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            
            return False
            
        targetRow = findRow(0, rows-1,)  # finds row where the target is
        return findCol(0, cols-1, targetRow)  # returns True is the value is present in row

    
solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
matrix = [[1]]
target = 3
print(solution.searchMatrix(matrix, target))