from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        max_minutes: int = -1
        rows: int = len(grid)
        cols: int = len(grid[0])
        stack: list[tuple[int, int]] = []

        fresh_oranges: int = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] ==1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    stack.append((row, col))

        while stack:
            max_minutes += 1  # first time it will be 0, this indicates there are rotten oranges in grid
            
            prev_stack = stack[:]
            stack = []
            
            while prev_stack:
                rotten: tuple[int, int] = prev_stack.pop()
                row: int = rotten[0]
                col: int = rotten[1]

                # four directions that we can move in
                directions: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for d in directions:
                    next_row: int = row + d[0]
                    next_col: int = col + d[1]

                    if rows > next_row >= 0 and cols > next_col >= 0 and grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        fresh_oranges -= 1
                        stack.append((next_row, next_col))

        # Edge Case: There were no rotten oranges in grid and no fresh oranges in the grid
        if max_minutes == -1 and fresh_oranges == 0:
            return 0

        return max_minutes if fresh_oranges == 0 else -1


solution = Solution()
print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))