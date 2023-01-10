from typing import List

class Solution:
    def find(self, x: int, root: list[int]):
        if x == root[x]:
            return x
        root[x] = self.find(root[x], root)
        return root[x]
    
    def union(self, x: int, y: int, root: list[int], rank: list[int]):
        root_x = self.find(x, root)
        root_y = self.find(y, root)
        
        if root_x == root_y:
            return False
        
        if rank[root_y] > rank[root_x]:
            root[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            root[root_y] = root_x
        else:
            root[root_y] = root_x
        
        return True
        
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        vertices: int = len(points)
            
        adj: list[tuple[int, int, int]] = []
        
        for i in range(0, vertices - 1 ):
            for j in range(i + 1, vertices):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d: int = abs(x1-x2) + abs(y1-y2)
                adj.append((i, j, d))

        adj.sort(key = lambda x: x[2])

        
        root: list[int] = [i for i in range(vertices)]
        rank: list[int] = [1]*vertices
        cost: int = 0
        
        for x, y, d in adj:
            vertex_added = self.union(x, y, root, rank)
            if vertex_added:
                cost += d
                vertices -= 1
                if vertices == 1:
                    break
        
        return cost