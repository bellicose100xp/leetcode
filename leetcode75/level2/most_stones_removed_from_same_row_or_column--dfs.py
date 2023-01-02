from typing import List

class Solution:
    def __init__(self):
        self.visited: set[tuple[int, int]] = set()
        # adj: Adjacency Matrix
        self.adj: dict[tuple[int, int], list[tuple[int, int]]] = {}
    
    def dfs(self, stone: tuple[int, int]) -> None:
        self.visited.add(stone)
        print(self.adj[stone])
        for next_stone in self.adj[stone]:
            if next_stone not in self.visited:
                self.dfs(next_stone)

    def removeStones(self, stones: List[List[int]]) -> int:
        # length of stones
        stones_count = len(stones)

        # create adjacency matrix
        for i in range(stones_count-1):
            for j in range(i+1,stones_count):
                stone1 = (stones[i][0], stones[i][1]) # tuple
                row1, col1 = stone1
                stone2 = (stones[j][0], stones[j][1]) # tuple
                row2, col2 = stone2

                if stone1 not in self.adj:
                    self.adj[stone1] = []
                if stone2 not in self.adj:
                    self.adj[stone2] = []
                
                if row1 == row2 or col1 == col2:
                    self.adj[stone1].append(stone2)
                    self.adj[stone2].append(stone1)
        
        disconnected_graphs: int = 0

        for i in stones:
            stone = (i[0], i[1]) # tuple
            if stone not in self.visited:
                disconnected_graphs += 1
                self.dfs(stone)

        return stones_count - disconnected_graphs

solution = Solution()
print(solution.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]])) # 5