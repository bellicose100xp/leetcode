from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # rows == cols in isConnected
        rows: int = len(isConnected)
        cols: int = rows

        # cities that we've visited
        visited_cities: list[int] = [0]*rows
        provinces: int = 0

        def dfs_find_connected(city: int):
            for another_city in range(cols):
                if visited_cities[another_city] == 0 and isConnected[city][another_city] == 1:
                    visited_cities[another_city] = 1
                    dfs_find_connected(another_city)

        for city, visited in enumerate(visited_cities):
            if visited == 0:
                visited_cities[city] = 1
                dfs_find_connected(city)
                provinces += 1
        
        return provinces

solution = Solution()

matrix = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
]
print(solution.findCircleNum(matrix)) # 8

matrix = [
    [1,0,0,1],
    [0,1,1,0],
    [0,1,1,1],
    [1,0,1,1]
    ]
print(solution.findCircleNum(matrix)) # 1