from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # size of matrix / number of cities
        size = len(isConnected)
        # parent vertex array: initialized with each vertex being it's own root
        parent: list[int] = [i for i in range(size)]

        # find root
        def find(x: int) -> int:
            if x == parent[x]:
                return x
            return find(parent[x])

        # update parent array
        def Union(x: int, y: int):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                parent[root_y] = root_x

        for first_city in range(size-1):
            for second_city in range(first_city + 1, size):
                if isConnected[first_city][second_city] == 1:
                    Union(first_city, second_city)

        return len(set([find(x) for x in range(size)]))


solution = Solution()
matrix = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
]

print(solution.findCircleNum(matrix))
