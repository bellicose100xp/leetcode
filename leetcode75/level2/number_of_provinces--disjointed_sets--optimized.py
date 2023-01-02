from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # size of matrix / number of cities
        size = len(isConnected)
        # root array: initialized with each vertex being it's own root
        root: list[int] = [i for i in range(size)]
        
        # Union Rank (height of tree): initilize with 1
        rank: list[int] = [1] * size

        # find root with Path Compression
        def find(x: int) -> int:
            if x == root[x]:
                return x
            root[x] = find(root[x])
            return root[x]

        # update parent array - with Union by Rank
        def Union(x: int, y: int):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    root[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    root[root_x] = root_y
                else:
                    root[root_y] = root_x
                    rank[root_x] += 1

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
