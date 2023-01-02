from typing import List

class Solution:
    
    # will always return root since it's doing path compression
    def find(self, root: list[int], x: int):
        if x == root[x]:
            return x
        root[x] = self.find(root, root[x])
        return root[x]

    def union(self, x: int, y: int, stones:list[list[int]], root: list[int], size: list[int]):
        root_x = self.find(root, x)
        root_y = self.find(root, y)

        # both component part of the same graph
        if root_x == root_y:
            return 0
        
        # merge disconnected graphs
        if size[root_x] < size[root_y]:
            root[root_x] = root_y
            size[root_y] += 1
        else:
            root[root_y] = root_x
            size[root_x] += 1
        
        return 1  # we connected one disconnected graph to another disconnected graph

    def removeStones(self, stones: List[List[int]]) -> int:
        # length of stones
        stones_count = len(stones)

        # root array -- effectively root as we'll be using path compression
        root: list[int] = [i for i in range(stones_count)]
        
        # union by rank - optimization
        size: list[int] = [1 for i in range(stones_count)]

        disconnected_graphs = stones_count

        for stone1 in range(stones_count - 1):
            for stone2 in range(stone1+1, stones_count):
                row1, col1 = stones[stone1]
                row2, col2 = stones[stone2]
                
                # if the stones share common row or col
                if row1 == row2 or col1 == col2:
                    disconnected_graphs -= self.union(stone1, stone2, stones, root, size)
        
        return stones_count - disconnected_graphs

