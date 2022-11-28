from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited: dict[tuple[int, int], int] = {}
        islands: int = 0
        
        # mark which cells have been visited
        def trace_island(r: int, c: int) -> None:
            visited[(r,c)] = 1
            if c+1 < cols and grid[r][c+1] == "1" and (r, c+1) not in visited:
                trace_island(r, c+1)
            if r+1 < rows and grid[r+1][c] == "1" and (r+1, c) not in visited:
                trace_island(r+1, c)
            

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "0" and (i, j) not in visited:
                    islands += 1
                    trace_island(i, j)
        
        return islands
                
solution = Solution()
solution.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]) #?
solution.numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]) #?


